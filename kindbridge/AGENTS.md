# AI Agent Rules for KindBridge

## Session Init Protocol

Before reading code or making changes, run:
```bash
cat ~/.kindpath/HANDOVER.md
python3 ~/.kindpath/kp_memory.py dump --domain gotcha
python3 ~/.kindpath/kp_memory.py dump
```

---

## What This Is

KindBridge — language mechanics education module. Teaches the structural
mechanics shared by human, body, animal, plant, machine, mathematical, and musical language.
Includes a fagazzi detector (text complexity analyser) and empowerment layer.

Part of the KPTH platform, living at `KPTH/kindbridge/`.

## Structure

```
app.py              — Flask web app (port 5030)
cli.py              — click CLI
core/               — Language mechanics, domains, limitations, empowerment
fagazzi/            — Fagazzi (unnecessary complexity) detector
bridge/             — Cross-domain structural equivalences
pedagogy/           — Learning sequence engine
templates/          — Flask HTML template (single-file, section-based)
```

## Operational Commands

- **Install**: `pip install -r requirements.txt`
- **Web app**: `python app.py` → http://localhost:5030
- **CLI**: `python -m kindbridge.cli --help`
- **Fagazzi check**: `python -m kindbridge.cli fagazzi "<text>"`

## Rules

- Language in this module must be accessible — no ironic complexity in a language teaching tool
- The empowerment layer is not an add-on; it runs through every section
- `fagazzi/detector.py` is a text-analysis tool for education, separate from any other
  fagazzi-named module in the KindPath ecosystem (notably the one in orchestrator.py:510)
- Follow KindPath doctrine: benevolence, syntropy, sovereignty

## Security Mandates

- No user text stored — the fagazzi /fagazzi POST endpoint analyses and discards
- No external API calls — pure Python stdlib + Flask
- Input validation: text capped at 10,000 characters in app.py
