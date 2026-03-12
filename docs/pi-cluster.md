# Pi Cluster Deployment Guide

KindPath services on a Raspberry Pi 4 cluster (arm64, Docker Compose stack).
Tested on Pi 4 Model B (4 GB RAM) running Raspberry Pi OS Lite (64-bit) and Ubuntu Server 22.04 arm64.

## Hardware Requirements

| Node | Role | RAM | Storage |
|------|------|-----|---------|
| pi-1 | primary (API + orchestration) | 4 GB | 64 GB SD / USB SSD |
| pi-2 | database | 4 GB | 64 GB USB SSD |
| pi-3 | worker / backup | 4 GB | 32 GB SD |

A fast SD card or USB SSD is required for pi-2 — SQLite WAL and Postgres both show degraded performance on low-speed SD.

## OS Setup (each Pi)

```bash
# Enable 64-bit kernel (in /boot/config.txt if using Pi OS)
arm_64bit=1

# Install Docker Engine (official installer)
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker pi

# Install Docker Compose plugin
sudo apt-get install -y docker-compose-plugin
```

## Project Layout on Cluster

```
/opt/kindpath/
├── docker-compose.yml          ← this stack
├── .env                        ← secrets (not in git)
├── data/
│   ├── postgres/               ← postgres data volume
│   └── kindai/
│       └── db/                 ← sessions.db (SQLite)
└── config/
    └── kindai/
        └── config.yaml
```

## docker-compose.yml

```yaml
version: "3.9"

# ── Pi Cluster Docker Compose Stack ──────────────────────────────────────────
# Targets arm64 (Raspberry Pi 4, Monterey-incompatible services moved off-host).
# Runs: kindai (API + REPL), postgres (persistent sessions), pgadmin (admin).
# All images pinned to explicit versions for reproducibility.

services:

  # ── KindAI ──────────────────────────────────────────────────────────────────
  kindai:
    image: ghcr.io/kindpath-collective/kindai:latest
    platform: linux/arm64/v8
    restart: unless-stopped
    depends_on:
      postgres:
        condition: service_healthy
    environment:
      DATABASE_URL: postgresql://kindai:${POSTGRES_PASSWORD}@postgres:5432/kindai
      KINDAI_DEFAULT_BACKEND: ollama
      OLLAMA_HOST: http://ollama:11434
      ENCRYPTION_KEY: ${ENCRYPTION_KEY}
      ANTHROPIC_API_KEY: ${ANTHROPIC_API_KEY:-}
      OPENAI_API_KEY: ${OPENAI_API_KEY:-}
    ports:
      - "7860:7860"      # workspace UI
    volumes:
      - /opt/kindpath/data/kindai:/app/db
      - /opt/kindpath/config/kindai/config.yaml:/app/config.yaml:ro
    networks:
      - kindpath

  # ── Ollama (local LLM for offline-first operation) ───────────────────────────
  ollama:
    image: ollama/ollama:latest
    platform: linux/arm64/v8
    restart: unless-stopped
    ports:
      - "11434:11434"
    volumes:
      - ollama_models:/root/.ollama
    networks:
      - kindpath
    # Pull llama3.2 on first boot
    entrypoint: ["/bin/sh", "-c", "ollama serve & sleep 5 && ollama pull llama3.2 && wait"]

  # ── Postgres ─────────────────────────────────────────────────────────────────
  postgres:
    image: postgres:15-alpine
    platform: linux/arm64/v8
    restart: unless-stopped
    environment:
      POSTGRES_USER: kindai
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: kindai
    volumes:
      - /opt/kindpath/data/postgres:/var/lib/postgresql/data
    networks:
      - kindpath
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U kindai"]
      interval: 10s
      timeout: 5s
      retries: 5

  # ── PgAdmin ──────────────────────────────────────────────────────────────────
  pgadmin:
    image: dpage/pgadmin4:latest
    # pgAdmin does not publish official arm64 images — use the community build.
    # Replace with 'dpage/pgadmin4:latest' if they add arm64 support.
    platform: linux/arm64/v8
    restart: unless-stopped
    environment:
      PGADMIN_DEFAULT_EMAIL: ${PGADMIN_EMAIL:-admin@kindpath.local}
      PGADMIN_DEFAULT_PASSWORD: ${PGADMIN_PASSWORD}
      PGADMIN_LISTEN_PORT: 5050
    ports:
      - "5050:5050"
    depends_on:
      - postgres
    networks:
      - kindpath

  # ── BMR Server ───────────────────────────────────────────────────────────────
  kindpath-bmr:
    image: ghcr.io/kindpath-collective/kindpath-bmr:latest
    platform: linux/arm64/v8
    restart: unless-stopped
    environment:
      ENCRYPTION_KEY: ${ENCRYPTION_KEY}
      DATABASE_URL: postgresql://kindai:${POSTGRES_PASSWORD}@postgres:5432/kindai
    ports:
      - "8001:8001"
    depends_on:
      postgres:
        condition: service_healthy
    networks:
      - kindpath

networks:
  kindpath:
    driver: bridge

volumes:
  ollama_models:
```

## .env Template

Create `/opt/kindpath/.env` from this template. **Never commit this file.**

```env
# KindPath Pi Cluster — environment secrets
# Copy to /opt/kindpath/.env and fill in values

POSTGRES_PASSWORD=change_me_strong_password_here
ENCRYPTION_KEY=change_me_32_byte_base64_encoded_key
PGADMIN_PASSWORD=change_me_admin_password
PGADMIN_EMAIL=admin@kindpath.local

# Optional — leave blank to run fully offline on Ollama
ANTHROPIC_API_KEY=
OPENAI_API_KEY=
```

Generate `ENCRYPTION_KEY` with:
```bash
python3 -c "import secrets, base64; print(base64.urlsafe_b64encode(secrets.token_bytes(32)).decode())"
```

## First Boot

```bash
cd /opt/kindpath
docker compose pull
docker compose up -d

# Check logs
docker compose logs -f kindai

# Pull the Ollama model (runs automatically via entrypoint, but can be done manually)
docker exec -it kindpath-ollama-1 ollama pull llama3.2

# Verify workspace UI is reachable
curl http://localhost:7860/health
```

## Networking

- **Workspace UI**: `http://pi-1.local:7860`
- **PgAdmin**: `http://pi-1.local:5050`
- **BMR API**: `http://pi-1.local:8001`
- **Ollama**: `http://pi-1.local:11434` (or internal to cluster: `http://ollama:11434`)

If accessing from another device on the LAN, replace `pi-1.local` with the Pi's IP address.

## Persistent Storage Notes

| Path | Purpose | Backup Priority |
|------|---------|----------------|
| `/opt/kindpath/data/postgres/` | Postgres data | HIGH |
| `/opt/kindpath/data/kindai/` | SQLite sessions | MEDIUM |
| `/root/.ollama` (via volume) | Model weights | LOW — re-pullable |

Backup `/opt/kindpath/data/` to an external drive or remote storage regularly.
The Postgres volume contains all conversation history and BMR registry data.

## Updating

```bash
cd /opt/kindpath
docker compose pull
docker compose up -d --remove-orphans
```

## Troubleshooting

**Container exits immediately:**
```bash
docker compose logs kindai
```

**pgAdmin arm64 image unavailable:**
Use `adminer` as a lightweight alternative:
```yaml
  adminer:
    image: adminer:latest
    platform: linux/arm64/v8
    ports:
      - "8080:8080"
    networks:
      - kindpath
```

**Ollama model pull fails:**
```bash
docker exec -it kindpath-ollama-1 ollama pull llama3.2:3b  # smaller model for memory-constrained Pi
```

**Pi runs out of memory with 4 GB:**
Reduce to 3b model, or disable pgAdmin — it's the heaviest non-critical service.
`docker compose stop pgadmin`
