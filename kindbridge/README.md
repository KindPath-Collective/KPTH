# KindBridge

Language mechanics without the gatekeeping.

---

## What This Is

KindBridge teaches the structural mechanics shared by every language — human, body,
animal, plant, and machine — before teaching any specific language.

The core premise: if you ever looked at a language concept and thought
*"this is unnecessarily complicated and I feel stupid for not getting it"* —
that instinct was often correct. Complexity is sometimes a feature. But sometimes
it is a gate. KindBridge helps you tell the difference.

The module is named for **fagazzi** — a word coined by a child who noticed
that some of what grown-ups called sophisticated was just fake complexity
designed to make you feel small.

---

## Structure

```
kindbridge/
├── app.py                  — Flask web application (port 5030)
├── cli.py                  — CLI entry point
├── requirements.txt
├── core/
│   ├── mechanics.py        — 5 universal language mechanics
│   ├── domains.py          — 7 domain definitions (human → music)
│   ├── limitations.py      — 5 ways every language fails
│   └── empowerment.py      — Psychological safety layer
├── fagazzi/
│   └── detector.py         — Text analyser: detects unnecessary complexity
├── bridge/
│   └── translator.py       — Cross-domain structural equivalences
├── pedagogy/
│   └── sequence.py         — Recommended learning sequence
└── templates/
    └── index.html          — Web UI (single template, section-based)
```

---

## Running

### Web UI

```bash
cd KPTH/kindbridge
pip install -r requirements.txt
python app.py
# → http://localhost:5030
```

### CLI

```bash
python -m kindbridge.cli --help

# Core statement
python -m kindbridge.cli intro

# Mechanics
python -m kindbridge.cli mechanics
python -m kindbridge.cli mechanics Syntax

# Domains
python -m kindbridge.cli domain
python -m kindbridge.cli domain body

# Bridges
python -m kindbridge.cli bridges

# Limitations
python -m kindbridge.cli limits

# Empowerment
python -m kindbridge.cli empower
python -m kindbridge.cli empower complicated

# Fagazzi checker
python -m kindbridge.cli fagazzi "We are committed to leveraging synergistic paradigm shifts."

# Learning sequence
python -m kindbridge.cli sequence
```

---

## The Seven Domains

| Domain       | Age on Earth    | Primary channel                |
|-------------|-----------------|--------------------------------|
| Human        | ~100,000 yrs    | Spoken/written symbols         |
| Body         | ~6M yrs         | Posture, gesture, gaze         |
| Animal       | ~500M yrs       | Sound, chemical, visual        |
| Plant        | ~470M yrs       | Chemical, electrical           |
| Machine      | ~80 yrs         | Binary encoding                |
| Mathematical | ~5,000 yrs      | Visual symbols, notation       |
| Music        | ~50,000+ yrs    | Sound waves, visual notation   |

Human language is not the oldest. It is not the most information-dense.
It is the most familiar to most readers. That's the starting point — not a hierarchy.

---

## The Fagazzi Detector

Fagazzi is unnecessary complexity. The detector identifies four patterns:

1. **Nominal style** — turning verbs into noun-phrases to sound formal
   ("utilisation of" instead of "using")
2. **Accountability avoidance** — passive voice that hides the actor
   ("mistakes were made" instead of "I made a mistake")
3. **Jargon displacement** — technical terms where plain terms would do
4. **Length inflation** — filler phrases that add length without meaning

Score: 0.0 (clear) → 1.0 (fagazzi).

---

## Philosophy

Every language is a system with symbols, syntax, semantics, pragmatics, and
feedback loops. These mechanics appear in all seven domains. Once you can name them
in one domain, you can recognise them in the others.

The person who felt stupid about language was not less than.
They were encountering a real limitation — or a real gate — without a map.
KindBridge is the map.

---

## Part of the KPTH platform

KindBridge lives in `KPTH/kindbridge/` alongside other KPTH sub-services.
See `KPTH/ARCHITECTURE.md` for platform context.
