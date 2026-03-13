"""
core/limitations.py — Where language fails.

This is not a list of reasons language is bad. Language is remarkable and
evolved (in all its forms) for good reasons. But every system has limits,
and knowing the limits of a tool makes you better at using it.

The most common source of human conflict that I can identify is not malice.
It is the false belief that language is more precise and shared than it is —
that when two people use the same words, they mean the same things.
They rarely do. And no one tells you this clearly enough.

This module names the specific ways language fails. Not to produce nihilism
about communication — but to produce realistic expectations and better habits.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class LanguageFailureMode:
    """A documented way that language fails to do what we need it to do."""
    name: str
    plain_description: str
    why_it_happens: str
    real_world_impact: str
    domain_examples: dict    # {domain: example}
    what_helps: str
    empowerment_note: str


FAILURE_MODES: List[LanguageFailureMode] = [

    LanguageFailureMode(
        name="Semantic Drift",
        plain_description=(
            "Words change meaning over time, and the same word means different "
            "things to people of different ages, backgrounds, and communities. "
            "A word you heard your whole life in one context means something "
            "entirely different in another context. Neither meaning is wrong. "
            "Both are real. This creates invisible miscommunication — both "
            "parties believe they're using the word correctly, and they are, "
            "in different language communities."
        ),
        why_it_happens=(
            "Language is a living system. It evolves through use, not through "
            "central authority. No one decides what 'literally' means — millions "
            "of people use it, and usage shapes meaning. Dictionaries record what "
            "is already happening, they don't set the rules."
        ),
        real_world_impact=(
            "Generational conflict about the 'correct' meaning of words. "
            "Legal documents that use words without defining them (leaving courts "
            "to determine what was meant). Medical communication where 'depression' "
            "means something precise to a clinician and something different to a patient."
        ),
        domain_examples={
            "human": "'Sick' once meant ill. Now it also means impressively good.",
            "body": "A thumbs up used to signal 'kill him' in Roman gladiatorial tradition. Now: approval.",
            "animal": "Dog breeds selectively raised for signals — a 'submissive' posture means different things from a wolf.",
            "plant": "A plant's defence signals in one soil microbiome may not be detected in a degraded one.",
            "machine": "HTTP 204 meant 'no content' in 1994. Now the same code is used for different purposes across frameworks.",
        },
        what_helps=(
            "Define terms explicitly in high-stakes communication. When someone uses "
            "a word that's carrying weight, ask: 'what do you mean by that specifically?' "
            "This is not pedantry — it's the most important question in any serious conversation."
        ),
        empowerment_note=(
            "If you've ever been corrected for using a word the 'wrong way' and you "
            "couldn't understand why your way was wrong: it probably wasn't. It was "
            "different. Language communities have competing norms. The person correcting "
            "you was asserting their community's norms, not objective truth."
        ),
    ),

    LanguageFailureMode(
        name="The Translation Gap",
        plain_description=(
            "Translation between languages is never complete. There are concepts "
            "in every language that have no equivalent in others — not because "
            "humans in one culture lack certain experiences, but because their "
            "language carved those experiences up differently. When you move "
            "between languages, you're not just swapping words — you're "
            "navigating between different maps of reality."
        ),
        why_it_happens=(
            "Languages evolve within specific cultures and ecologies. They develop "
            "vocabulary for things that matter in that context. The Inuit languages "
            "do have many distinct words for different types of snow — this is not "
            "a myth. Portuguese 'saudade' (longing for something you love that is "
            "gone) has no direct English equivalent. German 'Weltschmerz' "
            "(grief at the state of the world) carries specific connotations "
            "no English word captures."
        ),
        real_world_impact=(
            "Legal and medical translation errors with serious consequences. "
            "Diplomatic misunderstandings. Literature that loses dimensions in "
            "translation. Indigenous knowledge systems encoded in languages where "
            "translation destroys the epistemological structure."
        ),
        domain_examples={
            "human": "'Hygge' (Danish): cosy contentment. No English word does the same work.",
            "body": "The Japanese concept of 'ma' (meaningful pause or negative space) has no body-language equivalent in Western gesture vocabulary.",
            "animal": "A dog's low-pitched bark and high-pitched bark don't translate cleanly into human emotional categories.",
            "plant": "Mycorrhizal chemical signals in Australian eucalyptus systems have no direct equivalents in European forest chemistry.",
            "machine": "Python's list comprehension [x*2 for x in list] doesn't translate cleanly to Java without losing elegance.",
        },
        what_helps=(
            "When something can't be translated, name the gap. Say: 'there's no "
            "English word for this, but the closest is...' or 'this carries a "
            "meaning that gets lost in translation'. Acknowledging the gap is more "
            "honest than pretending a translation is complete."
        ),
        empowerment_note=(
            "If you've ever felt that you experienced something you couldn't find "
            "words for in your language — you weren't failing to articulate. You "
            "were experiencing a limit of your language. The experience was real. "
            "The vocabulary gap is the language's problem, not yours."
        ),
    ),

    LanguageFailureMode(
        name="Power-Encoded Language",
        plain_description=(
            "Language carries power structures. Who gets to name things. Whose "
            "dialect is called 'standard'. Which terms get into dictionaries. "
            "Which speakers are called 'articulate' (with the implication that "
            "this is surprising). The language you were taught in school carries "
            "assumptions about class, race, gender, and ability that were never "
            "stated explicitly — they were just baked in. Some of what gets called "
            "'correct' grammar is a reflection of which dialects were historically "
            "spoken by people with social power."
        ),
        why_it_happens=(
            "Languages didn't evolve in power-neutral environments. The grammar "
            "rules taught in colonial school systems were those of the colonisers. "
            "The 'standard' dialect in most English contexts is Received Pronunciation "
            "— the accent of the British upper class. Calling it 'standard' makes "
            "a class-based norm appear to be a linguistic fact."
        ),
        real_world_impact=(
            "People penalised in job interviews for dialect. Indigenous languages "
            "suppressed and lost. Medical systems that dismiss patients whose "
            "language doesn't match expected register. Educational systems that "
            "systematically undervalue students from non-dominant language backgrounds."
        ),
        domain_examples={
            "human": "AAVE speakers are regularly told their grammar is 'wrong' — AAVE has rigorous internal grammatical rules.",
            "body": "Eye contact norms are taught as universal — but they encode Western professional culture's specific values.",
            "animal": "The naming of animal behaviours ('dominance', 'submission') encodes human power frameworks onto animals.",
            "plant": "Western ethnobotany frequently names and patents plant knowledge generated by indigenous communities.",
            "machine": "Early programming language design was almost exclusively male — and the assumptions are still in the tools.",
        },
        what_helps=(
            "Notice when 'correct' or 'standard' is being applied without explanation. "
            "Ask: whose standard? Correct by whose measure? This is not relativism — "
            "some things are genuinely more clear or precise than others. But many "
            "things called 'correct language' are just the dialect of whoever had power."
        ),
        empowerment_note=(
            "If you were told your language was wrong and you suspected this had "
            "more to do with where you came from than actual error — you were "
            "likely right. The people who correct dialect are often enforcing "
            "class norms under the guise of language instruction."
        ),
    ),

    LanguageFailureMode(
        name="The Ineffability Problem",
        plain_description=(
            "Some experiences cannot be fully captured in language. Physical pain "
            "is famously resistant to description — the McGill Pain Questionnaire "
            "gives patients 78 words because no single one comes close. Grief. "
            "Love. The specific quality of a taste. Synesthetic experiences. "
            "Trauma. Not everything that is real is sayable. And the things that "
            "are hardest to say are often the most important things."
        ),
        why_it_happens=(
            "Language operates by carving experience into shared categories. It "
            "requires a shared system of reference. When an experience has no "
            "shared category — because it is too personal, too embodied, too novel, "
            "or because the language community hasn't developed vocabulary for it "
            "— language fails. Music, art, and movement exist partly because they "
            "communicate things language cannot reach."
        ),
        real_world_impact=(
            "Trauma survivors unable to describe their experiences to doctors or "
            "courts. Chronic pain patients whose descriptions are disbelieved. "
            "People describing mental illness to people who haven't experienced "
            "it. The limits of therapy that relies entirely on verbal articulation."
        ),
        domain_examples={
            "human": "Try to describe the taste of salt to someone who has never tasted it, using only words.",
            "body": "The way grief sits in the chest is body language with no verbal equivalent.",
            "animal": "We cannot describe the experience of echolocation in a way that captures what it is like to be a bat.",
            "plant": "There is no human-accessible way to describe what it is to be a distributed rhizomatic network.",
            "machine": "Formal languages cannot express true randomness — they can only simulate it.",
        },
        what_helps=(
            "Acknowledge ineffability directly: 'I can't find the words for this'. "
            "This is more honest than forcing inadequate language and more useful than "
            "silence. Metaphor, analogy, and gesture carry things language can't. "
            "So does a hand on a shoulder."
        ),
        empowerment_note=(
            "If you've ever struggled to describe your experience and had it dismissed "
            "because you couldn't find the right words — remember: the inability to "
            "describe something in language does not make it less real. Pain is real "
            "whether you can describe it precisely or not. Grief is real. The body "
            "knows things the dictionary hasn't caught up to."
        ),
    ),

    LanguageFailureMode(
        name="Deliberate Obscurity",
        plain_description=(
            "Sometimes language is made difficult on purpose. Legal documents. "
            "Terms and conditions. Technical specifications designed to be "
            "unreadable by non-specialists. Academic writing designed to signal "
            "membership in a community rather than to communicate ideas. "
            "The instinct that screams 'this is a fagazzi' when reading a "
            "15-word sentence that means 'yes' — that instinct is often right."
        ),
        why_it_happens=(
            "Deliberate obscurity serves several functions: it excludes people "
            "without credentials (gatekeeping expertise), it avoids accountability "
            "(you can't be held to a promise no one understands), it signals "
            "membership in an elite community, and it hides the absence of "
            "precise thinking behind impressive-sounding language."
        ),
        real_world_impact=(
            "People signing contracts they can't understand. Healthcare consent "
            "forms written above the reading level of most patients. Academic "
            "knowledge locked behind incomprehensible prose. Corporate communications "
            "that sound like information but contain none."
        ),
        domain_examples={
            "human": "'The party of the first part hereinafter...' means 'you'. Legal language creates dependency on interpreters.",
            "body": "Highly ritualised formal greetings (the exact bow angle, the exact handshake pressure) function as gatekeeping — you need to have been taught.",
            "animal": "Complex dominance display systems in social animals function partly to exclude challengers who haven't learned the signals.",
            "plant": "There is no deliberate obscurity in plant communication — this is uniquely human.",
            "machine": "An API documentation that assumes 10 other things you need to read first creates dependency on those who have already navigated it.",
        },
        what_helps=(
            "Demand plain language. 'Can you explain that without the jargon?' "
            "is a reasonable request in any context. Plain Language movements in "
            "law, medicine, and government exist for this reason. They are not "
            "dumbing things down — they are making communication work."
        ),
        empowerment_note=(
            "The fagazzi instinct — the kid who looks at something and thinks "
            "'this is fake complicated' — is one of the most accurate linguistic "
            "instruments we have. The instinct usually finds real deliberate "
            "obscurity. If you thought 'this doesn't need to be this complicated' "
            "and you were right, you have a gift. Name that gift. Use it."
        ),
    ),
]


class LanguageLimitations:
    """Access the documented failure modes of language systems."""

    def get_all(self) -> List[LanguageFailureMode]:
        return FAILURE_MODES

    def get(self, name: str) -> LanguageFailureMode:
        for mode in FAILURE_MODES:
            if mode.name.lower() == name.lower():
                return mode
        raise KeyError(f"Unknown failure mode: {name}")

    def get_intro(self) -> str:
        return (
            "Language is not broken. It is a remarkable set of evolved tools "
            "for sharing information across bodies and time. But every tool has "
            "limits. Knowing the limits of a tool is part of using it well.\n\n"
            "These are the documented ways language fails — not as a reason to "
            "distrust communication, but as a map of where to pay extra attention "
            "and where to be patient with yourself and others when understanding "
            "doesn't quite land."
        )
