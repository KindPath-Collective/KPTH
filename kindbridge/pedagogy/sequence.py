"""
pedagogy/sequence.py — Learning sequence engine.

The sequence in which concepts are introduced makes an enormous difference
to how well they're retained. KindBridge teaches in a specific order:

  1. Mechanics first — the universal architecture before any domain
  2. Most familiar domain first — usually human language (body language for
     those who feel disconnected from words)
  3. Bridging concepts — showing equivlences between the familiar and new
  4. Limitations — what language can't do (sets realistic expectations)
  5. Fagazzi awareness — detecting unnecessary complexity
  6. Empowerment reframes — the psychological safety layer
  7. Practice domain — explore the unfamiliar from a position of strength

The empowerment layer appears early and runs throughout. Not as a coda —
as a continuous thread. Every lesson includes the validation.
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class LessonStep:
    """A single step in the learning sequence."""
    step_number: int
    title: str
    module: str              # Which module to load ('mechanics', 'domains', etc.)
    module_key: str          # Which item within the module
    estimated_minutes: int
    learning_goal: str
    empowerment_anchor: str  # The empowerment note woven into this step


LEARNING_SEQUENCE: List[LessonStep] = [

    LessonStep(
        step_number=1,
        title="Why mechanics first",
        module="empowerment",
        module_key="intro",
        estimated_minutes=3,
        learning_goal="Reframe language learning as recognition, not memorisation",
        empowerment_anchor=(
            "Before we start: you already use all five of the mechanics you're about to "
            "learn. You use them every day. This section is naming things you already do, "
            "not introducing foreign concepts."
        ),
    ),

    LessonStep(
        step_number=2,
        title="Symbols — the foundation of all language",
        module="mechanics",
        module_key="Symbols",
        estimated_minutes=8,
        learning_goal="Understand that symbols are arbitrary agreements, not natural connections",
        empowerment_anchor=(
            "The fact that 'tree' sounds nothing like a tree, and that German calls "
            "it 'Baum', is not a quirk — it's confirmation that the connection is "
            "cultural, not inherent. Confusion about why words are what they are "
            "is the correct response."
        ),
    ),

    LessonStep(
        step_number=3,
        title="Syntax — why order matters",
        module="mechanics",
        module_key="Syntax",
        estimated_minutes=8,
        learning_goal="Identify syntax as a universal layer in all communication",
        empowerment_anchor=(
            "You've been parsing syntax since before you could spell. 'Dog bites man' "
            "versus 'man bites dog' — you knew the difference before anyone taught you "
            "what syntax was. This is not a new skill. It's a named skill."
        ),
    ),

    LessonStep(
        step_number=4,
        title="Semantics — meaning is not fixed",
        module="mechanics",
        module_key="Semantics",
        estimated_minutes=10,
        learning_goal="Understand that meaning is constructed between people, not stored in words",
        empowerment_anchor=(
            "If you've ever argued with someone and discovered you were using the same "
            "words to mean different things — that's semantics. It's not irrationality. "
            "It's the structural limit of shared symbols."
        ),
    ),

    LessonStep(
        step_number=5,
        title="Pragmatics — what language is actually doing",
        module="mechanics",
        module_key="Pragmatics",
        estimated_minutes=10,
        learning_goal="Distinguish between what language says and what it does",
        empowerment_anchor=(
            "If you've ever had a joke fall flat in a new context, or been misread "
            "over text — that's a pragmatics failure. Not a you failure. The channel "
            "removed the pragmatic cues your communication depended on."
        ),
    ),

    LessonStep(
        step_number=6,
        title="Feedback — the loop that closes communication",
        module="mechanics",
        module_key="Feedback",
        estimated_minutes=8,
        learning_goal="Identify feedback as a structural requirement, not a social nicety",
        empowerment_anchor=(
            "The anxiety of sending a message and receiving no response is your "
            "language system correctly identifying a broken feedback loop. "
            "It is not oversensitivity."
        ),
    ),

    LessonStep(
        step_number=7,
        title="The five domains — one structure, five channels",
        module="bridge",
        module_key="intro",
        estimated_minutes=5,
        learning_goal="See all five domains as variations on the same structure",
        empowerment_anchor=(
            "This is the structural insight that changes everything: "
            "the mechanics you just learned are in all five domains. "
            "You're not learning five new things. You're seeing one thing five times."
        ),
    ),

    LessonStep(
        step_number=8,
        title="Human Language — your most familiar domain",
        module="domains",
        module_key="human",
        estimated_minutes=12,
        learning_goal="Understand human language as one of five, not the definitive one",
        empowerment_anchor=(
            "Human language is your most familiar domain, but not because it's "
            "the most important. It's because you've been trained in it longest. "
            "That familiarity will be the foothold for every other domain."
        ),
    ),

    LessonStep(
        step_number=9,
        title="Body Language — the older channel",
        module="domains",
        module_key="body",
        estimated_minutes=12,
        learning_goal="Recognise body language as a full language system, not background noise",
        empowerment_anchor=(
            "Body language predates spoken language by millions of years. "
            "The channel is older. The information density, for emotional content, "
            "is higher. You're already fluent in it. You just haven't had the vocabulary."
        ),
    ),

    LessonStep(
        step_number=10,
        title="When languages fail — the limits you need to know",
        module="limitations",
        module_key="intro",
        estimated_minutes=10,
        learning_goal="Set realistic expectations about what any language can and cannot carry",
        empowerment_anchor=(
            "Knowing the limits of a tool is not pessimism. It is competence. "
            "Every practitioner of every craft knows where their tools break down."
        ),
    ),

    LessonStep(
        step_number=11,
        title="Detecting fagazzi — when complexity serves exclusion",
        module="fagazzi",
        module_key="intro",
        estimated_minutes=12,
        learning_goal="Develop active awareness of unnecessary complexity",
        empowerment_anchor=(
            "This is the instinct you've always had. We're naming it and giving it a method."
        ),
    ),

    LessonStep(
        step_number=12,
        title="Animal Language — communication without words",
        module="domains",
        module_key="animal",
        estimated_minutes=12,
        learning_goal="Expand language awareness beyond human and near-human communication",
        empowerment_anchor=(
            "If animal communication seemed simple to you before, that's because "
            "we weren't looking with the right tools. The tools you have now are enough."
        ),
    ),

    LessonStep(
        step_number=13,
        title="Plant Language — distributed, chemical, ancient",
        module="domains",
        module_key="plant",
        estimated_minutes=12,
        learning_goal="Extend language awareness to radically non-human systems",
        empowerment_anchor=(
            "The cultural resistance to taking plant communication seriously is a "
            "fagazzi pattern — it serves to keep plant knowledge in specialist hands. "
            "The evidence is clear. The resistance is cultural, not scientific."
        ),
    ),

    LessonStep(
        step_number=14,
        title="Machine Language — the literal domain",
        module="domains",
        module_key="machine",
        estimated_minutes=15,
        learning_goal="Understand machine language as uniquely literal, not uniquely complex",
        empowerment_anchor=(
            "Machine language doesn't fill in pragmatic gaps. That's not a feature "
            "of advanced intelligence — it's a feature of having no shared context. "
            "The frustration of programming is the frustration of maximum literalness."
        ),
    ),

    LessonStep(
        step_number=15,
        title="Bridges — seeing equivalence across all five",
        module="bridge",
        module_key="all",
        estimated_minutes=15,
        learning_goal="Build explicit cross-domain structural connections",
        empowerment_anchor=(
            "Every bridge you make is a new anchor. The more connections you have "
            "between domains, the more any new language becomes recognition rather "
            "than mystery."
        ),
    ),
]


class PedagogySequencer:
    """Manages the learning sequence for KindBridge."""

    def get_full_sequence(self) -> List[LessonStep]:
        return LEARNING_SEQUENCE

    def get_step(self, step_number: int) -> Optional[LessonStep]:
        for step in LEARNING_SEQUENCE:
            if step.step_number == step_number:
                return step
        return None

    def get_total_minutes(self) -> int:
        return sum(s.estimated_minutes for s in LEARNING_SEQUENCE)

    def get_domain_steps(self, domain_id: str) -> List[LessonStep]:
        return [s for s in LEARNING_SEQUENCE if s.module_key == domain_id]
