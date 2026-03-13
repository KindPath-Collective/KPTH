"""
cli.py — KindBridge command-line interface.

Invoke as: python -m kindbridge.cli <command>
Or once installed: kindbridge <command>

Every command includes a plain-language description of what it will show you.
The CLI is not a lower-tier product. It has the same information as the web UI.
"""

import click
import textwrap

from kindbridge.core.mechanics import LanguageMechanics
from kindbridge.core.domains import DomainRegistry
from kindbridge.core.limitations import LanguageLimitations
from kindbridge.core.empowerment import EmpowermentLayer
from kindbridge.fagazzi.detector import FagazziDetector
from kindbridge.bridge.translator import BridgeTranslator
from kindbridge.pedagogy.sequence import PedagogySequencer


def _wrap(text: str, width: int = 78) -> str:
    return "\n".join(
        textwrap.fill(para, width=width)
        for para in text.strip().split("\n\n")
    )


def _section(title: str) -> None:
    click.echo()
    click.echo(click.style("─" * 60, fg="cyan"))
    click.echo(click.style(f"  {title}", fg="cyan", bold=True))
    click.echo(click.style("─" * 60, fg="cyan"))
    click.echo()


@click.group()
def cli():
    """
    KindBridge — language mechanics without the gatekeeping.

    If you've ever looked at a language concept and thought
    'this is unnecessarily complicated' — you were probably right.
    This tool helps you see how language actually works across five domains.
    """
    pass


@cli.command()
def intro():
    """Print KindBridge's core statement and reason for existing."""
    layer = EmpowermentLayer()
    _section("KindBridge")
    click.echo(_wrap(layer.get_core_statement()))
    click.echo()
    click.echo(_wrap(layer.get_intro()))


@cli.command()
@click.argument("layer_name", default="")
def mechanics(layer_name: str):
    """
    Show the universal mechanics every language shares.

    Optionally pass a mechanic name: Symbols, Syntax, Semantics, Pragmatics, Feedback
    Example: kindbridge mechanics Syntax
    """
    m = LanguageMechanics()

    if layer_name:
        layer = m.get_layer(layer_name)
        if not layer:
            suggestions = ", ".join(l.name for l in m.get_all_layers())
            click.echo(f"Unknown mechanic: '{layer_name}'. Try one of: {suggestions}")
            return
        _section(f"Mechanic: {layer.name}")
        click.echo(_wrap(layer.plain_description))
        click.echo()
        click.echo(click.style("Why it exists:", bold=True))
        click.echo(_wrap(layer.why_it_exists))
        click.echo()
        click.echo(click.style("Common confusion:", bold=True))
        click.echo(_wrap(layer.common_confusion))
        click.echo()
        click.echo(click.style("Across all five domains:", bold=True))
        click.echo(f"  Human:   {layer.example_human}")
        click.echo(f"  Body:    {layer.example_body}")
        click.echo(f"  Animal:  {layer.example_animal}")
        click.echo(f"  Plant:   {layer.example_plant}")
        click.echo(f"  Machine: {layer.example_machine}")
        click.echo()
        click.echo(click.style("▸ " + layer.empowerment_note, fg="green"))
    else:
        _section("Language Mechanics")
        click.echo(_wrap(m.get_introduction()))
        click.echo()
        for layer in m.get_all_layers():
            click.echo(click.style(f"  {layer.name}", bold=True) + f" — {layer.plain_description[:80]}…")
        click.echo()
        click.echo("Use  kindbridge mechanics <name>  for detail on any mechanic.")


@cli.command()
@click.argument("domain_id", default="")
def domain(domain_id: str):
    """
    Show a language domain in full.

    Domains: human, body, animal, plant, machine
    Example: kindbridge domain body
    """
    reg = DomainRegistry()

    if domain_id:
        d = reg.get(domain_id)
        if not d:
            click.echo(f"Unknown domain: '{domain_id}'. Try: human, body, animal, plant, machine")
            return
        _section(f"Domain: {d.name}")
        click.echo(_wrap(d.description))
        click.echo()
        click.echo(click.style("Age on Earth: ", bold=True) + d.age_on_earth)
        click.echo(click.style("Primary channel: ", bold=True) + d.primary_channel)
        click.echo(click.style("Bandwidth: ", bold=True) + d.bandwidth)
        click.echo()
        click.echo(click.style("Strengths:", bold=True))
        for s in d.strengths:
            click.echo(f"  + {s}")
        click.echo()
        click.echo(click.style("Limitations:", bold=True))
        for l in d.limitations:
            click.echo(f"  - {l}")
        click.echo()
        click.echo(click.style("Misconceptions:", bold=True))
        for m_text in d.common_misconceptions:
            click.echo(f"  ✗ {m_text}")
        click.echo()
        click.echo(click.style("Sample expressions:", bold=True))
        for ex in d.example_phrases:
            click.echo(f"  • {ex}")
        click.echo()
        click.echo(click.style("Where to start:", bold=True))
        click.echo(_wrap(d.learning_entry_point))
    else:
        _section("The Five Language Domains")
        click.echo(_wrap(reg.get_intro()))
        click.echo()
        for d in reg.get_all():
            click.echo(click.style(f"  {d.id:8}", bold=True) + f" {d.name} — {d.age_on_earth}")
        click.echo()
        click.echo("Use  kindbridge domain <id>  for the full description.")


@cli.command()
def bridges():
    """Show structural equivalences across all five language domains."""
    bt = BridgeTranslator()
    _section("Cross-Domain Bridges")
    click.echo(_wrap(bt.get_intro()))
    click.echo()

    for bridge in bt.get_all_multi_domain():
        click.echo(click.style(f"  {bridge.concept_name}", bold=True))
        click.echo(f"  Mechanic: {bridge.mechanic}")
        click.echo(f"  {bridge.description}")
        for domain_id, example in bridge.instances.items():
            click.echo(f"    {domain_id:8} → {example}")
        click.echo(click.style(f"  ▸ {bridge.insight}", fg="green"))
        click.echo()

    click.echo(click.style("Specific pairwise bridges:", bold=True))
    for b in bt.get_pairwise_bridges():
        click.echo(f"\n  {b.from_domain} [{b.from_concept}] → {b.to_domain} [{b.to_concept}]")
        click.echo(f"  {b.explanation}")
        if b.surprise_note:
            click.echo(click.style(f"  ↳ {b.surprise_note}", fg="yellow"))


@cli.command()
def limits():
    """Show the five ways every language fails — and why that's useful to know."""
    ll = LanguageLimitations()
    _section("Language Limitations")
    click.echo(_wrap(ll.get_intro()))
    click.echo()
    for fm in ll.get_all():
        click.echo(click.style(f"  {fm.name}", bold=True))
        click.echo(f"  {fm.plain_description}")
        click.echo(click.style(f"  ▸ {fm.empowerment_note}", fg="green"))
        click.echo()


@cli.command()
@click.argument("feeling_keyword", default="")
def empower(feeling_keyword: str):
    """
    Show empowerment insights addressing specific language-related feelings.

    Optional: pass a keyword (e.g. 'stupid', 'complicated', 'fagazzi')
    Example: kindbridge empower complicated
    """
    layer = EmpowermentLayer()

    if feeling_keyword:
        insight = layer.get_by_feeling(feeling_keyword)
        if insight:
            _section("Empowerment: " + insight.feeling)
            click.echo(click.style(_wrap(insight.truth), fg="green"))
            click.echo()
            click.echo(click.style("Evidence:", bold=True))
            for ex in insight.examples:
                click.echo(f"  • {ex}")
            click.echo()
            click.echo(click.style("What to do with it:", bold=True))
            click.echo(_wrap(insight.action))
        else:
            click.echo(f"No direct match for '{feeling_keyword}'. Showing all insights.")
            for ins in layer.get_all():
                click.echo(f"  • {ins.feeling}")
    else:
        _section("Empowerment Layer")
        click.echo(_wrap(layer.get_core_statement()))
        click.echo()
        click.echo(click.style("Available topics:", bold=True))
        for ins in layer.get_all():
            click.echo(f"  • {ins.feeling}")
        click.echo()
        click.echo("Use  kindbridge empower <keyword>  for a specific insight.")


@cli.command()
@click.argument("text")
def fagazzi(text: str):
    """
    Analyse text for unnecessary complexity.

    Detects: corporate jargon, accountability avoidance, jargon displacement,
    length inflation — anything that makes text harder without making it clearer.

    Example: kindbridge fagazzi "We are committed to leveraging synergistic paradigm
    shifts to facilitate stakeholder alignment going forward."
    """
    detector = FagazziDetector()
    result = detector.analyse(text)

    _section(f"Fagazzi Analysis — score: {result.fagazzi_score:.2f} / 1.0")

    verdict_color = {
        "clear": "green",
        "mildly complex": "white",
        "unnecessarily complex": "yellow",
        "fagazzi": "red",
    }.get(result.verdict, "white")

    click.echo(click.style(f"  Verdict: {result.verdict.upper()}", fg=verdict_color, bold=True))
    click.echo()

    if not result.signals:
        click.echo("  No fagazzi patterns detected.")
    else:
        click.echo(click.style(f"  Signals found ({len(result.signals)}):", bold=True))
        for sig in result.signals:
            click.echo(f"\n  [{sig.severity.upper()}] {sig.signal_type}")
            click.echo(f"  Pattern: \"{sig.span}\"")
            click.echo(f"  Issue:   {sig.explanation}")
            if sig.plain_alternative:
                click.echo(click.style(f"  Plain:   {sig.plain_alternative}", fg="green"))

    click.echo()
    click.echo(click.style("▸ " + result.empowerment_note, fg="green"))


@cli.command()
def sequence():
    """Show the recommended learning sequence and estimated time."""
    seq = PedagogySequencer()
    _section(f"Learning Sequence — {seq.get_total_minutes()} minutes total")
    for step in seq.get_full_sequence():
        mins = f"{step.estimated_minutes}m"
        click.echo(
            click.style(f"  {step.step_number:2}.", bold=True) +
            f" {step.title:<45} {click.style(mins, fg='cyan')}"
        )
        click.echo(f"     Goal: {step.learning_goal}")
        click.echo()


if __name__ == "__main__":
    cli()
