"""
fagazzi/detector.py — The Fagazzi Detector

Named for the kid's instinct that something is unnecessarily fake or complex.
'Fagazzi' (also forgozzi, fargazzi): a term for something that is fake,
artificial, or more elaborate than it needs to be. When a child looks at
bureaucratic or academic language and thinks "wait, why is this so complicated?"
they are frequently performing a legitimate linguistic analysis.

This module operationalises that instinct.

Fagazzi is not about complexity itself — genuine complexity exists and is "
valuable. It is about UNNECESSARY complexity: language that has been made
harder than it needs to be, often to:
  - Exclude people without credentials (gatekeeping)
  - Signal expertise without actually being precise
  - Hide the absence of clear thinking behind impressive-sounding words
  - Avoid accountability through vagueness and passive voice
  - Make a trivial claim sound weightier than it is

The technical term in linguistics is 'obfuscatory register'.
The plain term is: fagazzi.

If you ever felt stupid for not understanding something and later discovered
it was just poorly explained — or worse, intentionally opaque — this module
is here to tell you: you were right. The problem was in the language, not
in you.
"""

import re
from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class FagazziSignal:
    """
    A single detected fagazzi signal in a piece of text.
    Signals are not definitive indictments — they are prompts for scrutiny.
    """
    signal_type: str           # Category of complexity pattern
    severity: str              # 'mild', 'moderate', 'strong'
    span: str                  # The specific text that triggered the signal
    explanation: str           # What this pattern does
    plain_alternative: str     # How to say it more directly


@dataclass
class FagazziAnalysis:
    """
    Full analysis of a text for unnecessary language complexity.
    Includes an empowerment reading — the validated version of the instinct.
    """
    original_text: str
    signals: List[FagazziSignal]
    fagazzi_score: float          # 0.0 = clear, 1.0 = deeply opaque
    signal_count: int
    dominant_type: str            # Most common pattern found
    empowerment_note: str         # The "you weren't wrong" validation
    plain_summary: str            # What the text is probably trying to say
    verdict: str                  # 'clear', 'mildly complex', 'unnecessarily complex', 'fagazzi'


# ── Pattern definitions ──────────────────────────────────────────────────────

NOMINAL_STYLE_PATTERNS = [
    (r'\butiliz(e|ing|ation)\b', 'utilize/utilization', 'use'),
    (r'\bimplementat(ion|ing)\b', 'implementation', 'doing/building'),
    (r'\bfacilitat(e|ing|ion)\b', 'facilitate', 'help/enable'),
    (r'\bleverage\b', 'leverage (as a verb)', 'use'),
    (r'\bsynergis(e|tic|m)\b', 'synergise/synergy', 'work together'),
    (r'\boptimis(e|ation|ing)\b', 'optimise (when vague)', 'improve'),
    (r'\benterprise-grade\b', 'enterprise-grade', 'suitable for large organisations'),
    (r'\bscalable\b', 'scalable (when undefined)', 'can grow'),
    (r'\brobust\b', 'robust (when undefined)', 'reliable'),
    (r'\bseamless(ly)?\b', 'seamless', 'smooth/without friction'),
    (r'\bholistic\b', 'holistic (overused)', 'whole-system / complete'),
    (r'\bparadigm shift\b', 'paradigm shift', 'major change'),
    (r'\bsolution\b', 'solution (generic)', 'the specific thing being offered'),
    (r'\beco-system\b|ecosystem', 'ecosystem (when metaphorical)', 'network of things'),
    (r'\bvalue proposition\b', 'value proposition', 'what you get from this'),
    (r'\bstakeholder(s)?\b', 'stakeholders', 'people affected / people involved'),
    (r'\bkey (performance )?indicator', 'key performance indicator', 'measurement of progress'),
    (r'\boutcome(s)? focus\w*\b', 'outcomes-focused', 'focused on results'),
    (r'\bdeliverable(s)?\b', 'deliverables', 'what will be produced'),
    (r'\bgoing forward\b', 'going forward', 'from now on'),
    (r'\bin terms of\b', 'in terms of (when vague)', 'regarding / about'),
    (r'\bat the end of the day\b', 'at the end of the day', 'ultimately'),
    (r'\bmove the needle\b', 'move the needle', 'make a difference'),
    (r'\bthought leader\b', 'thought leader', 'expert'),
    (r'\bdisruptive\b', 'disruptive', 'new, different'),
    (r'\binnovative\b', 'innovative (unqualified)', 'new'),
    (r'\bcutting.edge\b', 'cutting-edge', 'new'),
    (r'\bground.breaking\b', 'groundbreaking', 'new'),
    (r'\bstate.of.the.art\b', 'state-of-the-art', 'current best'),
    (r'\bnext.generation\b', 'next-generation', 'newer version'),
]

PASSIVE_AVOIDANCE_PATTERNS = [
    (r'\bit (has been|was) (noted|observed|found|demonstrated|suggested|argued)\b', 'passive attribution', 'Someone found... / We found...'),
    (r'\b(mistakes were made|errors occurred)\b', 'passive accountability', 'I/we made mistakes'),
    (r'\b(it should be noted|it is worth noting)\b', 'burying the lede', 'state it directly'),
    (r'\bone might argue\b', 'false distancing', 'I argue'),
    (r'\bsome people believe\b', 'vague attribution', 'who? what people?'),
    (r'\bit is generally accepted\b', 'false consensus', 'many researchers believe / specify who'),
    (r'\bstudies show\b', 'unattributed evidence', 'which studies? by whom?'),
    (r'\bresearch suggests\b', 'unattributed evidence', 'which research?'),
    (r'\bexperts agree\b', 'false consensus', 'which experts?'),
]

JARGON_DISPLACEMENT_PATTERNS = [
    (r'\bontological\b', 'ontological', 'relating to the nature of existence/being'),
    (r'\bepistemolog\w+\b', 'epistemological', 'relating to how we know things'),
    (r'\bhermeneutic(s)?\b', 'hermeneutics', 'interpretation (especially of texts)'),
    (r'\bdialectical\b', 'dialectical', 'through argument and counter-argument'),
    (r'\bpraxis\b', 'praxis', 'practice (the application of theory)'),
    (r'\bhegemonic?\b', 'hegemonic', 'dominant (especially through cultural power)'),
    (r'\bposit(s|ing|ed)?\b', 'posits', 'claims / argues'),
    (r'\belucidat\w+\b', 'elucidate', 'explain'),
    (r'\bextrapolat\w+\b', 'extrapolate', 'extend / extend a pattern'),
    (r'\binter alia\b', 'inter alia', 'among other things'),
    (r'\bmutatis mutandis\b', 'mutatis mutandis', 'with the necessary changes'),
    (r'\bipso facto\b', 'ipso facto', 'by that very fact'),
    (r'\ba priori\b', 'a priori', 'known before experience / assumed in advance'),
    (r'\bde facto\b', 'de facto', 'in practice (even if not officially)'),
    (r'\bqua\b', 'qua', 'as / in the role of'),
    (r'\bfortiori\b', 'a fortiori', 'even more so'),
    (r'\bvis-?à-?vis\b', 'vis-à-vis', 'in relation to / compared to'),
]

LENGTH_INFLATION_PATTERNS = [
    (r'\bdue to the fact that\b', 'long phrase', 'because'),
    (r'\bin light of the fact that\b', 'long phrase', 'because'),
    (r'\bfor the purpose of\b', 'long phrase', 'to / for'),
    (r'\bin order to\b', 'mild padding', 'to'),
    (r'\bat this point in time\b', 'long phrase', 'now'),
    (r'\bprior to\b', 'formal padding', 'before'),
    (r'\bsubsequent to\b', 'formal padding', 'after'),
    (r'\bwith regard to\b', 'formal padding', 'about / regarding'),
    (r'\bwith respect to\b', 'formal padding', 'about / regarding'),
    (r'\bin the event that\b', 'long phrase', 'if'),
    (r'\bin the context of\b', 'vague framing', 'regard / for'),
    (r'\bhas the ability to\b', 'long phrase', 'can'),
    (r'\bhas the capacity to\b', 'long phrase', 'can'),
    (r'\bis able to\b', 'mild padding', 'can'),
    (r'\bprovides support for\b', 'long phrase', 'supports'),
    (r'\bmakes an attempt to\b', 'long phrase', 'tries to'),
    (r'\bconducts an analysis of\b', 'long phrase', 'analyses'),
    (r'\bperforms a review of\b', 'long phrase', 'reviews'),
    (r'\bserves to\b', 'padding', 'usually removable'),
    (r'\bthe fact that\b', 'padding', 'often removable'),
]


class FagazziDetector:
    """
    Analyses text for unnecessary complexity.

    This is not a style checker. It is a language transparency tool. Its
    purpose is to name patterns that make language harder to understand than
    it needs to be, validate the instinct that something is unnecessarily
    complex, and offer the plain alternative.

    The score is not a judgment of the author. It is an observation about
    the text. Complex language is often a product of the training environment
    (academic, corporate, legal) more than conscious choice.
    """

    def analyse(self, text: str) -> FagazziAnalysis:
        """Analyse a piece of text for fagazzi patterns."""
        signals: List[FagazziSignal] = []
        text_lower = text.lower()

        # Check corporate/business jargon
        for pattern, label, alternative in NOMINAL_STYLE_PATTERNS:
            for match in re.finditer(pattern, text_lower):
                signals.append(FagazziSignal(
                    signal_type="corporate jargon",
                    severity="mild",
                    span=match.group(),
                    explanation=f"'{label}' is often vague or inflated. Frequently used to sound professional rather than to communicate precisely.",
                    plain_alternative=f"Consider: '{alternative}'",
                ))

        # Check passive voice / accountability avoidance
        for pattern, label, alternative in PASSIVE_AVOIDANCE_PATTERNS:
            for match in re.finditer(pattern, text_lower):
                signals.append(FagazziSignal(
                    signal_type="accountability avoidance",
                    severity="moderate",
                    span=match.group(),
                    explanation=f"'{label}': passive constructions often obscure who is responsible for claims or actions.",
                    plain_alternative=f"Consider: '{alternative}'",
                ))

        # Check academic/specialist jargon used unnecessarily
        for pattern, label, alternative in JARGON_DISPLACEMENT_PATTERNS:
            for match in re.finditer(pattern, text_lower):
                signals.append(FagazziSignal(
                    signal_type="jargon displacement",
                    severity="moderate",
                    span=match.group(),
                    explanation=f"'{label}': specialist term that can usually be replaced with plain language for a general audience.",
                    plain_alternative=f"Consider: '{alternative}'",
                ))

        # Check length inflation
        for pattern, label, alternative in LENGTH_INFLATION_PATTERNS:
            for match in re.finditer(pattern, text_lower):
                signals.append(FagazziSignal(
                    signal_type="length inflation",
                    severity="mild",
                    span=match.group(),
                    explanation=f"'{label}': uses more words than necessary without adding meaning.",
                    plain_alternative=f"Replace with: '{alternative}'",
                ))

        # Dedup by span position (keep first occurrence)
        seen_spans = set()
        unique_signals = []
        for s in signals:
            if s.span not in seen_spans:
                seen_spans.add(s.span)
                unique_signals.append(s)
        signals = unique_signals

        # Compute score
        word_count = max(len(text.split()), 1)
        raw_score = min(len(signals) / (word_count / 10), 1.0)
        fagazzi_score = round(raw_score, 2)

        # Dominant type
        if signals:
            type_counts: dict = {}
            for s in signals:
                type_counts[s.signal_type] = type_counts.get(s.signal_type, 0) + 1
            dominant_type = max(type_counts, key=lambda k: type_counts[k])
        else:
            dominant_type = "none"

        verdict = self._score_to_verdict(fagazzi_score)
        empowerment_note = self._empowerment_note(fagazzi_score, dominant_type)
        plain_summary = self._plain_summary_note(signals)

        return FagazziAnalysis(
            original_text=text,
            signals=signals,
            fagazzi_score=fagazzi_score,
            signal_count=len(signals),
            dominant_type=dominant_type,
            empowerment_note=empowerment_note,
            plain_summary=plain_summary,
            verdict=verdict,
        )

    def _score_to_verdict(self, score: float) -> str:
        if score < 0.1:
            return "clear"
        elif score < 0.3:
            return "mildly complex"
        elif score < 0.5:
            return "unnecessarily complex"
        else:
            return "fagazzi"

    def _empowerment_note(self, score: float, dominant_type: str) -> str:
        if score < 0.1:
            return (
                "This text is reasonably direct. If you found it difficult to understand, "
                "the content itself may be the challenge — not the language used to deliver it. "
                "That's different. Content difficulty is real. Language difficulty is often avoidable."
            )
        elif score < 0.3:
            return (
                "This text has some complexity patterns. If it felt harder to read than it "
                "needed to, you were right. The difficulty isn't just the content — the "
                "language choices are adding friction. Plain alternatives exist."
            )
        elif score < 0.5:
            notes = {
                "corporate jargon": (
                    "This text leans heavily on corporate language. These terms are so common "
                    "in professional contexts that they feel 'normal' — but they are often vague "
                    "and frequently obscure rather than communicate. If this felt like a "
                    "performance of professionalism rather than actual communication, you were right."
                ),
                "accountability avoidance": (
                    "This text is using passive constructions to distance the author from claims "
                    "or accountability. 'Mistakes were made' has no maker. 'Studies show' has no "
                    "studies. This is a specific rhetorical technique. Recognising it is a skill."
                ),
                "jargon displacement": (
                    "This text is using specialist vocabulary in ways that may be excluding rather "
                    "than clarifying. If you felt like you needed a specific background to understand "
                    "something that should be accessible, you were likely right."
                ),
                "length inflation": (
                    "This text is padded — more words than meaning. This often happens when writers "
                    "are trained to produce length as a signal of effort. It costs the reader time "
                    "and attention."
                ),
            }
            return notes.get(dominant_type, (
                "This text is unnecessarily complex. If reading it felt like work, "
                "that work was not your limitation — it was placed there by the language choices."
            ))
        else:
            return (
                "This text scores as fagazzi — multiple layers of unnecessary complexity. "
                "This is the pattern: when you read it and felt confused or inadequate, "
                "the problem was not in you. The problem was in the language. That instinct "
                "you had — 'this is more complicated than it needs to be' — was correct."
            )

    def _plain_summary_note(self, signals: List[FagazziSignal]) -> str:
        if not signals:
            return "No significant complexity patterns detected."
        types = [s.signal_type for s in signals]
        found = sorted(set(types), key=lambda t: types.count(t), reverse=True)
        return (
            f"Detected patterns: {', '.join(found[:3])}. "
            "Review the flagged passages for plain alternatives. "
            "The flags are not corrections — they are invitations to consider "
            "whether simpler language would serve the reader better."
        )
