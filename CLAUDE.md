# CLAUDE.md — KPTH (KindPath Collective Platform)

## Session Init Protocol

Before reading code or making changes, run:
```bash
cat ~/.kindpath/HANDOVER.md
python3 ~/.kindpath/kp_memory.py dump --domain gotcha
python3 ~/.kindpath/kp_memory.py dump
```

---

## What This Is
KindPath Collective Platform — KindEarth / KindPath core. Digital-native platform
with pilot operations, community digital libraries, ecological tooling, and
KindPath life-field services.

## Operational Commands
- **Install**: `pip install -r requirements.txt`
- **Run**: `docker-compose up`
- **Test**: `pytest`

## Structure
- `kindearth/` — KindEarth ecological and community tools (see kindearth/AGENTS.md)
- `kindpath-life-field/` — KindPath life field services (see kindpath-life-field/AGENTS.md)
- `data-capture/` — data capture services
- `digital-library/` — community digital library
- `ecological-tool/` — ecological assessment tooling
- `services/` — shared microservices
- `shared/` — shared utilities

## Security Mandates
- No API keys or secrets in source
- Secrets via environment variables / docker-compose env files
