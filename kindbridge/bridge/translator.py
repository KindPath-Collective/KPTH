"""
bridge/translator.py — Cross-domain structural translation.

The most powerful thing KindBridge can show is structural equivalence across
domains. Once you see that a bee's waggle dance and a Python function both have
syntax, semantics, and a feedback mechanism — the next language you learn
becomes recognition, not memorisation.

This module builds explicit bridges between domains, mapping corresponding
concepts and showing the shared underlying structure. It also builds analogies —
'this is like...' statements that give people a foothold when a concept would
otherwise feel alien.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class Bridge:
    """
    A structural bridge between two domains.
    Shows that a concept in domain A corresponds to a concept in domain B.
    """
    mechanic: str             # Which language mechanic this bridge demonstrates
    from_domain: str
    from_concept: str
    from_example: str
    to_domain: str
    to_concept: str
    to_example: str
    explanation: str          # Why this equivalence is meaningful
    surprise_note: str        # Why this is not obvious — what the bridge reveals


@dataclass
class MultiDomainBridge:
    """
    A concept that appears across all five domains simultaneously.
    Shows universal language structure.
    """
    mechanic: str
    concept_name: str
    description: str
    instances: Dict[str, str]   # domain_id -> how this appears in that domain
    insight: str               # What seeing all five together reveals


MULTI_DOMAIN_BRIDGES: List[MultiDomainBridge] = [

    MultiDomainBridge(
        mechanic="Syntax",
        concept_name="Sequence matters",
        description=(
            "In every language domain, the order of signals changes the meaning. "
            "This is syntax: the structural rules about arrangement. The rules "
            "are different in each domain, but the principle is universal."
        ),
        instances={
            "human": "'Dog bites man' vs 'Man bites dog' — same words, opposite meanings because of sequence.",
            "body": "Eye contact → smile → look away reads as flirting. Same signals in reverse: discomfort.",
            "animal": "A dog play-bows BEFORE play behaviour — this frames what follows as non-aggressive. The sequence matters.",
            "plant": "Root exudate: a plant releases Signal A then Signal B. The order activates different mycorrhizal responses.",
            "machine": "In Python: x = 5 then print(x) works. print(x) then x = 5 fails. Sequence is absolute.",
            "maths": "5 − 3 = 2 but 3 − 5 = −2. Order changes the result in subtraction and division. Order of operations is the syntax rule that makes expressions unambiguous.",
            "music": "C then G feels like departure. G then C feels like arrival home. Same two notes; sequence determines whether the phrase opens or resolves.",
        },
        insight=(
            "Every language encodes sequence as meaningful. Before you learn the "
            "specific syntax of a new language, you already understand why sequence "
            "matters — because you've been using it your whole life. You're extending "
            "a skill you have, not learning a new one from scratch."
        ),
    ),

    MultiDomainBridge(
        mechanic="Semantics",
        concept_name="Context determines meaning",
        description=(
            "In every domain, the same signal can mean different things depending on "
            "context. There is no domain where signals have context-free, fixed meanings. "
            "This is not a flaw — it allows efficient communication by offloading "
            "disambiguation to context."
        ),
        instances={
            "human": "'Fine' can mean anything from excellent to devastated — context and relationship history determine which.",
            "body": "A loud voice can mean excitement, anger, or hard of hearing — posture and relationship context say which.",
            "animal": "A crow's alarm call means 'danger' — but WHICH alarm call, and the response, depend on the specific predator type.",
            "plant": "Methyl jasmonate from a damaged plant means 'attack in progress' — but neighbouring plants' response depends on their own current state.",
            "machine": "Returning -1 from a function traditionally means 'error' in C — but only if both sender and receiver agree on that convention.",
            "maths": "The '-' symbol means subtraction (3-1), negation (-5), or a range (pages 1-5) depending on context. Same symbol, three different operations.",
            "music": "A note can function as the tonic (home, resolved) in one key and the leading tone (tense, unresolved) in another. Same pitch, opposite semantic weight.",
        },
        insight=(
            "When you struggle to understand what a signal means, add context. "
            "Context is not supplementary information — it is part of the signal. "
            "Understanding language is as much about reading context as reading text."
        ),
    ),

    MultiDomainBridge(
        mechanic="Feedback",
        concept_name="Silence is a signal",
        description=(
            "The absence of expected feedback is itself communicative in every domain. "
            "Silence after a question. No reply to a message. A plant that doesn't "
            "respond to a chemical signal. A function that returns nothing. "
            "All of these carry information — often more than an explicit response."
        ),
        instances={
            "human": "Not responding to a message has a pragmatic reading. 'Left on read' carries social weight.",
            "body": "No eye contact after something sensitive is said is a body language response. The absence communicates.",
            "animal": "When alarm calls are given but no flock response follows, birds infer: false alarm, or the threat has passed.",
            "plant": "If a plant releases VOC stress signals and no mycorrhizal response follows, it may indicate network degradation.",
            "machine": "A server not responding carries different meaning from a server responding with an error. Both are signals.",
            "maths": "In a proof, an unchallenged step is tacit acknowledgment. A reviewer's silence on a deduction means: accepted. The absence of objection is a signal.",
            "music": "A rest is not absence — it is a notated silence with a specific duration. John Cage's 4'33\" makes the entire composition a notated silence. The silent moment IS the communication.",
        },
        insight=(
            "Not communicating is communicating. Every communication system includes "
            "absence as a category of message. When you feel the discomfort of silence "
            "in a conversation — that discomfort is your language system correctly "
            "interpreting the missing feedback loop."
        ),
    ),

    MultiDomainBridge(
        mechanic="Pragmatics",
        concept_name="Indirect requests",
        description=(
            "Every language domain has a mechanism for asking for things indirectly. "
            "This is not deception — it's a pragmatic softening that preserves "
            "relationship and allows the receiver to decline without direct conflict. "
            "Indirection is not unique to human language."
        ),
        instances={
            "human": "'Is there any more tea?' means 'I would like more tea' — an indirect request framed as a question.",
            "body": "Standing near a door with a coat on is an indirect communication: 'I'd like to leave now'.",
            "animal": "A cat sitting near an empty food bowl and making eye contact without vocalising is an indirect request.",
            "plant": "A plant wilting slightly before a critical threshold is an earlier indirect signal than wilting completely.",
            "machine": "An HTTP 301 (moved permanently) is an indirect instruction: don't say this here, but the correct address is over there.",
            "maths": "A theorem that 'suggests an extension' is an indirect invitation to future researchers. The proof is given; the implied work is pragmatic, not stated.",
            "music": "A deceptive cadence — an expected resolution landing on the wrong chord — says 'not yet, this is not finished'. Musical communication for 'one more thing...'.",
        },
        insight=(
            "Directness is not always the most efficient strategy. Every communication "
            "system evolved mechanisms for the situations where direct communication "
            "is socially costly. Recognising indirect signals is a language skill most "
            "people practice constantly without knowing it."
        ),
    ),

    MultiDomainBridge(
        mechanic="Symbols",
        concept_name="The symbol is not the thing",
        description=(
            "In every domain, the signal that stands for something is not the thing itself. "
            "This seems obvious. It has massive implications that almost no one is taught explicitly."
        ),
        instances={
            "human": "The word 'fire' won't burn you. The map is not the territory.",
            "body": "A frown representing sadness is not the sadness itself — it can be performed without the underlying state.",
            "animal": "A display of size in a threat posture is a signal about size, not actual size — bluffing exists.",
            "plant": "The chemical alarm signal is not the damage itself — it is information about the damage.",
            "machine": "The variable name 'dangerLevel' doesn't make anything dangerous — it points to a value that may or may not be high.",
            "maths": "The numeral '3' is not three objects — it is a symbol applicable to three apples, three centuries, three dimensions. The number is the pattern, not the instance.",
            "music": "A score is not music. It is instructions for producing music. The notation points to a performance, not the performance itself. Burning a score does not destroy the piece.",
        },
        insight=(
            "The gap between symbol and thing is where misunderstanding lives. "
            "Arguments about words (is this 'violent'? is that 'freedom'?) are often "
            "really arguments about the things the words point to. "
            "Keeping the symbol and the thing separate is a foundational thinking skill."
        ),
    ),
]


PAIRWISE_BRIDGES: List[Bridge] = [
    Bridge(
        mechanic="Syntax",
        from_domain="machine",
        from_concept="Indentation in Python",
        from_example="if x: \\n    do_something()  # the indentation is part of the grammar",
        to_domain="body",
        to_concept="Proxemics (personal space)",
        to_example="Standing too close reads as aggression or intimacy — distance is part of the grammatical structure of a social interaction",
        explanation=(
            "Both systems encode relationship using spatial arrangement. "
            "In Python, indentation encodes hierarchical containment. "
            "In body language, distance encodes relational position. "
            "The word 'inside' means different things in each domain, but the "
            "spatial-as-syntactic logic is the same."
        ),
        surprise_note=(
            "Programming is often taught as if spatial layout is arbitrary. "
            "But humans have been using spatial arrangement as syntax — "
            "who stands where in a room, how close is too close — for millions of years."
        ),
    ),

    Bridge(
        mechanic="Semantics",
        from_domain="animal",
        from_concept="Vervet alarm specificity",
        from_example="Three distinct alarm calls for three distinct predator types, each triggering a different escape response",
        to_domain="machine",
        to_concept="HTTP status codes",
        to_example="404 (not found), 403 (forbidden), 401 (unauthorised) — distinct signals for distinct error types requiring distinct responses",
        explanation=(
            "Both systems use a vocabulary of discrete signals where the specific "
            "signal triggers a specific response. The vervet evolved this to survive. "
            "HTTP designed this to route errors correctly. Same architecture: "
            "categorical signal → categorical response."
        ),
        surprise_note=(
            "When you feel confused by HTTP error codes, remember: you already "
            "understand the architectural concept from living with species that use it. "
            "The confusion is the vocabulary, not the structure."
        ),
    ),

    Bridge(
        mechanic="Feedback",
        from_domain="plant",
        from_concept="Mycorrhizal acknowledgment",
        from_example="A tree releases a chemical signal; the fungal network responds by routing nutrients",
        to_domain="machine",
        to_concept="TCP/IP acknowledgement",
        to_example="Every packet sent receives an ACK (acknowledgment) packet confirming receipt",
        explanation=(
            "Both systems require the receiver to signal back to the sender "
            "that the message was received and processed. Both fail silently "
            "when the feedback channel is broken."
        ),
        surprise_note=(
            "The internet and the forest both decided: reliable communication "
            "requires a return signal. They arrived at this independently, "
            "through completely different evolutionary paths. This is "
            "a universal principle, not a human invention."
        ),
    ),

    Bridge(
        mechanic="Syntax",
        from_domain="maths",
        from_concept="Order of operations (BODMAS/PEMDAS)",
        from_example="2 + 3 × 4 = 14, not 20. The rule specifying which operations execute first is mathematical syntax.",
        to_domain="machine",
        to_concept="Operator precedence",
        to_example="In Python: 2 + 3 * 4 == 14. The same rule, mapped directly from mathematics into code.",
        explanation=(
            "Order of operations in mathematics and operator precedence in programming "
            "are the same rule under different names. BODMAS was named in a maths classroom. "
            "Every programming language inherits it directly. The knowledge transfers completely "
            "and nobody tells you."
        ),
        surprise_note=(
            "When you learn operator precedence in Python, you are not learning a new concept. "
            "You are applying a rule you already know from primary school maths, "
            "just with a different label. The feeling of learning is recognising old knowledge "
            "in a new domain — which is exactly what bridges are."
        ),
    ),

    Bridge(
        mechanic="Semantics",
        from_domain="music",
        from_concept="Tonal function",
        from_example="The same note can be the tonic (home, resolved) in one key and the leading tone (tense, pulling upward) in another. Same pitch, opposite semantic weight.",
        to_domain="human",
        to_concept="Contronyms",
        to_example="'Sanction' means both to authorise and to penalise. 'Cleave' means both to split apart and to cling together. Context determines which.",
        explanation=(
            "In both music and human language, the meaning of a signal is relational — "
            "it depends on what it is positioned against. The chord means what it means "
            "because of the key context surrounding it. The word means what it means "
            "because of the sentence around it. Neither the note nor the word has a "
            "fixed semantic value independent of context."
        ),
        surprise_note=(
            "The puzzle 'I know what that word means but can't tell which way it cuts here' "
            "is structurally identical to 'I don't know whether this chord is home or departure' "
            "— context-dependent meaning is the same challenge across domains. "
            "You already solve one version of this puzzle every time you read."
        ),
    ),

    Bridge(
        mechanic="Pragmatics",
        from_domain="maths",
        from_concept="Proof by contradiction (reductio ad absurdum)",
        from_example="Assume the opposite of what you want to prove. Derive an impossibility. Conclude the original must be true.",
        to_domain="human",
        to_concept="Informal reductio",
        to_example="'If that were true, then pigs would fly.' The everyday argument structure is the same proof strategy.",
        explanation=(
            "Formal mathematics named a reasoning pattern that humans were already executing "
            "colloquially. When someone says 'well if that were true, you'd have to believe X, "
            "which is obviously absurd', they are running a proof by contradiction. "
            "Mathematics did not invent this — it formalised what was already there."
        ),
        surprise_note=(
            "Mathematical proof and everyday argument share most of their deep structure. "
            "Logic is not an alien language you need to learn from scratch — it is the pattern "
            "underlying reasoning you are already doing, with the steps made explicit "
            "and the vocabulary made inspectable."
        ),
    ),
]


class BridgeTranslator:
    """
    Builds bridges between language domains to reveal shared structure.
    The goal: make any new language feel like recognition, not memorisation.
    """

    def get_all_multi_domain(self) -> List[MultiDomainBridge]:
        """Return all five-domain conceptual bridges."""
        return MULTI_DOMAIN_BRIDGES

    def get_pairwise_bridges(self) -> List[Bridge]:
        """Return pairwise bridges between specific domains."""
        return PAIRWISE_BRIDGES

    def find_bridges_from(self, domain_id: str) -> List[Bridge]:
        """Find bridges that originate from a given domain."""
        return [b for b in PAIRWISE_BRIDGES if b.from_domain == domain_id]

    def find_bridges_to(self, domain_id: str) -> List[Bridge]:
        """Find bridges that lead to a given domain."""
        return [b for b in PAIRWISE_BRIDGES if b.to_domain == domain_id]

    def get_bridge_for_mechanic(self, mechanic: str) -> List[MultiDomainBridge]:
        """Get multi-domain bridges illustrating a specific mechanic."""
        return [b for b in MULTI_DOMAIN_BRIDGES if b.mechanic.lower() == mechanic.lower()]

    def get_intro(self) -> str:
        return (
            "The most useful thing we can show you is: this thing you don't understand "
            "yet is structurally like this thing you already know.\n\n"
            "Every language domain — human, body, animal, plant, machine — shares the "
            "same five mechanics. The vocabulary is different. The channel is different. "
            "The purpose is different. The structure is the same.\n\n"
            "These bridges are the shortest path between 'I don't understand this' "
            "and 'oh — it's like...'.\n\n"
            "That moment of recognition — 'oh, it's like...' — is not a simplification. "
            "It's the most accurate description of how understanding actually works."
        )
