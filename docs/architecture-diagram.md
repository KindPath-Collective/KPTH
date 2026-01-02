# KindPath Collective Platform — Architecture Diagram

This is a high-level ASCII diagram of the platform architecture.

```
┌─────────────────────────────────────────────────────────────────┐
│                    KindPath Collective Platform                 │
│                    (KindEarth / KindPath)                       │
└─────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Conceptual Layers                           │
├─────────────────────────────────────────────────────────────────┤
│ 1) Interfaces (People + Community)                             │
│    - Life-Field Tool (current vs ideal reality)                │
│    - Digital Library (shared knowledge, provenance)            │
│    - (Later) Syntropic Food Tool, Q Audio Suite                │
└─────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│ 2) Intelligence (KindEarth + KindPath Analysis)                │
│    - Ecological Evaluation (constraints, capacity)             │
│    - Policy Analyser (drift, syntropy/entropy)                 │
│    - Economic Forecasting (in-house posture mapping)           │
└─────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│ 3) Operations (Pilots + Reporting)                             │
│    - Pilot templates, milestones, tapering                     │
│    - Signed exports, audit logs                                │
└─────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│ 4) Sovereignty & Integrity                                      │
│    - Consent & refusal enforcement                              │
│    - Local ownership + export controls                          │
│    - Audit trails + provenance                                  │
│    - Secret hygiene and secure transport/storage                │
└─────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Current Implementation                      │
├─────────────────────────────────────────────────────────────────┤
│ Services: Data Capture, Digital Library, Ecological Eval, Worker│
│ Infrastructure: Docker Compose, Postgres, MinIO/S3, Meilisearch │
│ Bus: Redpanda (Kafka-compatible)                                │
└─────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Data Flow Example                           │
├─────────────────────────────────────────────────────────────────┤
│ [Life-Field UI] → [Data Capture] → [Redpanda] → [Worker] → [Postgres + MinIO]
│ [Digital Library UI] → [Digital Library Service] → [Meilisearch + Storage]
│ [Eco Eval UI] → [Ecological Eval Service] → [Signed Exports]
└─────────────────────────────────────────────────────────────────┘
```

For a visual PNG diagram, export this or a similar structure from draw.io and place it in `docs/`.