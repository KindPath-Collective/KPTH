# KindPath suite — quick showcase

Use this as a one-pager to show collaborators what exists in `/home/sam/KPTH`, what each idea does, and how to demo it quickly.

## Whole stack at a glance
- Data capture → encrypted ingest to MinIO + Redpanda
- Digital library → encrypted content, provenance, Meilisearch search, link graphs
- Ecological evaluation → encrypted map data, signed export bundles, Redpanda consumer
- Worker → Celery + Kafka analytics
- Life Field (React) → personal field kit with JSON import/export
- KindEarth CLI → internal consulting OS (engagements, gates, forecasts)

Bring up the stack:  
```bash
cp .env.example .env   # tweak secrets/endpoints
./scripts/dev/up       # runs docker-compose stack on localhost
```

## Data Capture service (`services/data-capture`)
- What: FastAPI ingest for files + metadata; encrypts with Fernet, stores to MinIO, publishes to Redpanda.
- Why it matters: Secure multi-destination intake with message fan-out for downstream analytics.
- Demo:  
```bash
curl -F file=@sample.csv -F metadata='{"source":"sensor-1"}' http://localhost:8001/ingest
```
- Health: `http://localhost:8001/health`

## Digital Library service (`services/digital-library`)
- What: Encrypted literature store with provenance, versions, link mapping, currency checks, and Meilisearch search.
- Why: Trusted evidence base with redaction and freshness tracking.
- Demo (after stack up):  
```bash
curl -X POST http://localhost:8002/literature \
  -H 'Content-Type: application/json' \
  -d @test_lit.json
curl "http://localhost:8002/literature/search?q=content"
curl "http://localhost:8002/literature/1/map"       # link + version graph
curl "http://localhost:8002/literature/currency"    # stale items
```
- Health: `http://localhost:8002/health`

## Ecological Evaluation service (`services/ecological-eval`)
- What: Stores encrypted ecological metrics, serves map-ready data, signs+encrypts export bundles to external endpoints, and consumes Redpanda messages.
- Why: Proof-of-custody for sensitive spatial data plus auditable exports.
- Demo:  
```bash
curl -X POST http://localhost:8003/eco-data \
  -H 'Content-Type: application/json' \
  -d @test_eco.json
curl http://localhost:8003/eco-data/map          # decrypted map payloads
curl -X POST http://localhost:8003/eco-data/congruence
```
- Dashboard (Leaflet): `http://localhost:8003/dashboard`

## Worker (`services/worker`)
- What: Celery worker + Kafka consumer that runs climate trend analysis (linear regression, significance) on incoming data.
- Why: Real-time analytics hook fed by `data_topic`.
- Notes: Hidden service in Docker Compose (no exposed port); can be run standalone via `python -m app.worker`.

## Life Field web app (`kindpath-life-field`)
- What: React/Vite personal operating system for individuals (snapshot, ideal life, creativity, community, gap map, experiments, weekly check-ins) with localStorage persistence and JSON import/export.
- Demo locally:  
```bash
cd kindpath-life-field
npm install
npm run dev    # open the shown localhost port
```
- Export/import buttons live in the top-right toolbar.

## KindEarth CLI (`kindearth`)
- What: Internal consulting OS CLI (engagements, gates, forecasting) backed by SQLite templates and guardrails.
- Why: Operationalizes KindEarth pillars/gates/red flags/signals for client work.
- Demo:  
```bash
cd kindearth
poetry install
poetry run kindearth init
poetry run kindearth engagement new --name "Pilot" --org "KindPath Collective"
poetry run kindearth gate run --engagement-id <id>   # interactive gates
poetry run kindearth forecast run --engagement-id <id>
```

## Lightweight prototypes (for context)
- `data-capture/app.py`, `digital-library/app.py`, `ecological-tool/app.py`: early Flask sketches (single-file) used before the FastAPI services.
- `shared/backup.py`: placeholder backup utilities referenced in scripts.

## Talking points for collaborators
- Security: Encryption at ingress (Fernet), encrypted exports, MinIO SSE support; signatures on ecological bundles.
- Traceability: Provenance + versioning for literature; Redpanda topics for downstream audits; Meilisearch for instant recall.
- Extensibility: Each service is containerized; worker consumes Kafka and can be extended with more analytics tasks.
- Next tailoring moves: 1) Swap sample endpoints in `.env` with real audited destinations, 2) add TLS certs, 3) hook Life Field UI to APIs (e.g., syncing experiments/gap maps), 4) build web front-end surfaces for library + ecological dashboards.
