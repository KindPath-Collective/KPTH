# AI Agent Rules for KPTH

## Session Init Protocol

Before reading code or making changes, run:
```bash
cat ~/.kindpath/HANDOVER.md
python3 ~/.kindpath/kp_memory.py dump --domain gotcha
python3 ~/.kindpath/kp_memory.py dump
```

---

## What This Is

KindPath Collective Platform — the core operational platform.
Digital-native with pilot operations, community digital libraries,
ecological tooling, and KindPath life-field services.

## Structure

```
KPTH/
├── data-capture/       — Flask app capturing field signals (encrypted)
├── digital-library/    — Community digital library service
├── ecological-tool/    — Ecological assessment tooling
├── kindearth/          — KindEarth community and ecological tools
├── kindpath-life-field/— KindPath life field services
└── services/           — Shared microservices
```

## Operational Commands

- **Run all services**: `docker-compose up`
- **Run data-capture only**: `source venv/bin/activate && python data-capture/app.py`
- **Test**: `pytest`

## Rules

- `data-capture/app.py` requires `ENCRYPTION_KEY` in env — never generate at runtime
- All secrets via environment variables or docker-compose env files
- Follow KindPath doctrine: benevolence, syntropy, sovereignty
- Read `ARCHITECTURE.md` before making structural changes

## Security Mandates

- All data encrypted at rest and in transit
- `ENCRYPTION_KEY` must come from Secret Manager or `.env` — never hardcoded
- No PII in source control
