"""
app.py — KindBridge Flask web application.

The web interface for language mechanics education and fagazzi detection.

Routes:
  GET  /                     — Home: core statement + learning sequence nav
  GET  /mechanics            — All five mechanics
  GET  /mechanics/<name>     — Single mechanic detail
  GET  /domain/<id>          — Single domain: human / body / animal / plant / machine
  GET  /bridges              — Cross-domain structural bridges
  GET  /limits               — The five ways language fails
  GET  /empower              — Empowerment insights
  GET  /sequence             — The recommended learning sequence
  POST /fagazzi              — Fagazzi detection: POST {text: str} → JSON analysis
  GET  /fagazzi              — Fagazzi checker UI page
"""

from flask import Flask, render_template, request, jsonify, url_for

from kindbridge.core.mechanics import LanguageMechanics
from kindbridge.core.domains import DomainRegistry
from kindbridge.core.limitations import LanguageLimitations
from kindbridge.core.empowerment import EmpowermentLayer
from kindbridge.fagazzi.detector import FagazziDetector
from kindbridge.bridge.translator import BridgeTranslator
from kindbridge.pedagogy.sequence import PedagogySequencer

app = Flask(__name__)

# ── Build shared instances once at startup ────────────────────────────────

mechanics_engine = LanguageMechanics()
domain_registry = DomainRegistry()
limitations_engine = LanguageLimitations()
empowerment_layer = EmpowermentLayer()
fagazzi_detector = FagazziDetector()
bridge_translator = BridgeTranslator()
pedagogy_sequencer = PedagogySequencer()


# ── Context helper: inject nav data into every template ───────────────────

def _nav_context() -> dict:
    return {
        "domains": domain_registry.get_all(),
        "mechanics": mechanics_engine.get_all_layers(),
    }


# ── Routes ────────────────────────────────────────────────────────────────

@app.route("/")
def home():
    return render_template(
        "index.html",
        section="home",
        core_statement=empowerment_layer.get_core_statement(),
        sequence=pedagogy_sequencer.get_full_sequence(),
        total_minutes=pedagogy_sequencer.get_total_minutes(),
        **_nav_context(),
    )


@app.route("/mechanics")
def all_mechanics():
    return render_template(
        "index.html",
        section="mechanics",
        intro=mechanics_engine.get_introduction(),
        layers=mechanics_engine.get_all_layers(),
        **_nav_context(),
    )


@app.route("/mechanics/<name>")
def single_mechanic(name: str):
    layer = mechanics_engine.get_layer(name)
    if not layer:
        return render_template("index.html", section="not_found", **_nav_context()), 404
    return render_template(
        "index.html",
        section="mechanic_detail",
        layer=layer,
        **_nav_context(),
    )


@app.route("/domain/<domain_id>")
def single_domain(domain_id: str):
    d = domain_registry.get(domain_id)
    if not d:
        return render_template("index.html", section="not_found", **_nav_context()), 404
    return render_template(
        "index.html",
        section="domain_detail",
        domain=d,
        **_nav_context(),
    )


@app.route("/bridges")
def bridges():
    return render_template(
        "index.html",
        section="bridges",
        intro=bridge_translator.get_intro(),
        multi_domain=bridge_translator.get_all_multi_domain(),
        pairwise=bridge_translator.get_pairwise_bridges(),
        **_nav_context(),
    )


@app.route("/limits")
def limits():
    return render_template(
        "index.html",
        section="limits",
        intro=limitations_engine.get_intro(),
        failure_modes=limitations_engine.get_all(),
        **_nav_context(),
    )


@app.route("/empower")
def empower():
    return render_template(
        "index.html",
        section="empower",
        core_statement=empowerment_layer.get_core_statement(),
        intro=empowerment_layer.get_intro(),
        insights=empowerment_layer.get_all(),
        **_nav_context(),
    )


@app.route("/sequence")
def learning_sequence():
    return render_template(
        "index.html",
        section="sequence",
        sequence=pedagogy_sequencer.get_full_sequence(),
        total_minutes=pedagogy_sequencer.get_total_minutes(),
        **_nav_context(),
    )


@app.route("/fagazzi", methods=["GET"])
def fagazzi_page():
    return render_template(
        "index.html",
        section="fagazzi",
        **_nav_context(),
    )


@app.route("/fagazzi", methods=["POST"])
def fagazzi_check():
    """
    POST {text: str} → JSON analysis result.
    Called by the frontend JS when the user submits text.
    """
    data = request.get_json(silent=True) or {}
    text = str(data.get("text", "")).strip()

    if not text:
        return jsonify({"error": "No text provided."}), 400

    # Guard against unreasonably large inputs
    if len(text) > 10_000:
        return jsonify({"error": "Text too long. Maximum 10,000 characters."}), 400

    result = fagazzi_detector.analyse(text)

    return jsonify({
        "fagazzi_score": result.fagazzi_score,
        "verdict": result.verdict,
        "dominant_type": result.dominant_type,
        "empowerment_note": result.empowerment_note,
        "signals": [
            {
                "signal_type": s.signal_type,
                "severity": s.severity,
                "span": s.span,
                "explanation": s.explanation,
                "plain_alternative": s.plain_alternative,
            }
            for s in result.signals
        ],
    })


if __name__ == "__main__":
    app.run(debug=True, port=5030)
