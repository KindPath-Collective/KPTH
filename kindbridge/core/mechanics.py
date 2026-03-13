"""
core/mechanics.py — The foundational mechanics every language shares.

Before you learn any specific language, it helps enormously to understand
what ALL languages are doing. Once you see the common skeleton, learning
any new language becomes: "ah, how does THIS one handle syntax? semantics?
pragmatics?" — rather than feeling like you're starting from zero.

This module teaches the five universal layers of language. They exist (in
varying forms) whether you're reading C code, watching a bee dance, listening
to a whale, watching someone's face, or reading a novel.
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class MechanicLayer:
    """
    One layer of universal language mechanics.
    Every language, in every domain, has all five of these.
    Recognising them is the first act of language literacy.
    """
    name: str
    plain_description: str
    why_it_exists: str
    common_confusion: str
    example_human: str
    example_body: str
    example_animal: str
    example_plant: str
    example_machine: str
    example_maths: str
    example_music: str
    empowerment_note: str


MECHANIC_LAYERS: List[MechanicLayer] = [

    MechanicLayer(
        name="Symbols",
        plain_description=(
            "A symbol is anything that STANDS FOR something else. The word 'tree' "
            "is not a tree. The word is ink on paper (or pixels on a screen) that "
            "we have agreed — collectively, culturally, arbitrarily — to connect "
            "to the thing in the ground with leaves. This agreement is never written "
            "down formally. It lives in culture, in childhood, in context. This is "
            "why the same symbol means wildly different things in different cultures, "
            "different eras, or even different families."
        ),
        why_it_exists=(
            "The world is too large and too fleeting to point at directly. Symbols "
            "allow us to refer to things that aren't present, things that don't exist "
            "yet, things that are abstract. They compress reality into shareable form."
        ),
        common_confusion=(
            "The confusion: people treat symbols as if they ARE the thing. "
            "'The map is not the territory' — a map of a city is useful but "
            "is not the city. Confusing a symbol with its referent is how "
            "arguments about words obscure arguments about reality. You might "
            "be arguing about what 'freedom' means, not what freedom IS."
        ),
        example_human="The word 'grief' is not grief. It's a container we pour an experience into.",
        example_body="A raised middle finger means nothing in isolation — it's a symbol activated by culture.",
        example_animal="A bee's waggle dance angle represents the direction of food relative to the sun.",
        example_plant="The scent a plant releases when damaged is a chemical symbol: 'I am being eaten.'",
        example_machine="A variable name ('user_count') is a symbol that points to a location in memory.",
        example_maths="The symbol '∞' is not infinity itself — it is notation we agreed means 'without bound'. The concept predates the symbol by thousands of years.",
        example_music="A crotchet (quarter note) is not a sound — it is a symbol instructing a performer to produce a sound of a specific relative duration.",
        empowerment_note=(
            "If you've ever felt like a word didn't quite capture what you were "
            "experiencing, you were right. Words are imprecise containers. The "
            "experience is always more than the symbol. This is not a personal failure."
        ),
    ),

    MechanicLayer(
        name="Syntax",
        plain_description=(
            "Syntax is the rules for how symbols are arranged. The order matters. "
            "'The dog bit the man' and 'The man bit the dog' use identical words "
            "but mean different things. Every language has syntax — even languages "
            "you don't usually think of as 'languages'. A melody has syntax. "
            "Code has syntax. A handshake has syntax. Mycorrhizal chemical signals "
            "have temporal syntax (the timing and sequence of release)."
        ),
        why_it_exists=(
            "Without syntax, symbols are just a bag of unrelated things. Syntax "
            "creates relationships between symbols, and relationships are where "
            "meaning lives. It's the grammar of structure."
        ),
        common_confusion=(
            "People often confuse 'syntax errors' with being wrong. In human "
            "language, 'syntax rules' are largely invented by grammarians after "
            "the fact to describe what people were already doing. There is no "
            "central authority for English syntax — it's a collective agreement "
            "that shifts constantly. Prescriptive grammar (the rules you were "
            "taught) often reflects class and power, not correctness."
        ),
        example_human="'I saw the man with the telescope' — whose telescope? Syntax alone doesn't say.",
        example_body="Eye contact → look away → look back has a specific social syntax: interest, evaluation, decision.",
        example_animal="A wolf's tail-raise before a threat is syntactically: [posture] then [vocalisation].",
        example_plant="Root exudate timing: plant releases one compound, waits, releases another — sequential syntax.",
        example_machine="Python requires indentation where Java uses braces — same concept, different syntax rules.",
        example_maths="2 + 3 × 4 = 14, not 20. Order of operations is mathematical syntax: the rules that determine which symbols bind to which first.",
        example_music="A melody ascending (C D E F G) and the same notes descending (G F E D C) use identical symbols in opposite syntax — they feel and sound different.",
        empowerment_note=(
            "If you were ever marked wrong for 'bad grammar' in school, consider: "
            "whose grammar were they measuring against? Dialects have consistent "
            "internal syntax. African American Vernacular English (AAVE) is "
            "grammatically rigorous — it is not 'broken English'. It is a "
            "different syntax system. Being told your syntax is wrong often "
            "means: your syntax is from a different cultural context."
        ),
    ),

    MechanicLayer(
        name="Semantics",
        plain_description=(
            "Semantics is the MEANING layer — what symbols actually refer to. "
            "'Literally' now also means 'figuratively' in common use. 'Nice' "
            "once meant 'foolish'. Semantic drift is constant. Every word "
            "you use carries a specific semantic load in your head that is "
            "slightly different from what it carries in the reader's head. "
            "This is not dysfunction. This is how language works."
        ),
        why_it_exists=(
            "Syntax tells you the structure. Semantics tells you what the "
            "structure is about. Without semantics, you can follow the rules "
            "of a sentence perfectly and still say nothing meaningful. "
            "Noam Chomsky's famous example: 'Colorless green ideas sleep "
            "furiously' — perfect syntax, zero coherent semantics."
        ),
        common_confusion=(
            "Semantic ambiguity is responsible for an enormous proportion of "
            "human conflict. Couples argue because the same word ('commitment', "
            "'enough', 'home') carries different semantic weight for each person. "
            "Nations go to war over the semantics of 'territory'. Most workplace "
            "conflict is semantic — people meant different things by the same words."
        ),
        example_human="'I'm fine' can semantically mean anything from 'I'm excellent' to 'I'm devastated'.",
        example_body="A smile can mean happiness, aggression, social performance, nervousness, or contempt.",
        example_animal="A cat's slow blink has specific semantic content: safety, trust, non-aggression.",
        example_plant="The chemical 'methyl jasmonate' semantically means: 'activate defence pathways'.",
        example_machine="In Python, `True` and `1` are semantically equivalent in most contexts. Mostly.",
        example_maths="The '-' symbol means subtraction (3-1), negation (-5), or a range boundary (ages 3-5). Same symbol, three different semantic roles.",
        example_music="A minor chord carries 'sadness' in Western music — but this is a cultural convention, not an acoustic property. In jazz, the same chord means cool detachment.",
        empowerment_note=(
            "When communication fails, it's almost always a semantic mismatch, "
            "not stupidity on either side. If you've ever thought 'we were both "
            "saying the same thing but still arguing' — you were probably using "
            "the same words with different semantic content. This is not "
            "irrationality. It is the structural limitation of shared symbols."
        ),
    ),

    MechanicLayer(
        name="Pragmatics",
        plain_description=(
            "Pragmatics is context. The same sentence means different things "
            "depending on who says it, where, when, to whom, and with what "
            "tone. 'Could you open a window?' is syntactically a question about "
            "ability. Pragmatically, it almost always means 'please open the window'. "
            "Pragmatics is the gap between what language literally says and "
            "what it is actually doing in the world."
        ),
        why_it_exists=(
            "Language evolved for social coordination in specific contexts, "
            "not for perfect logical precision. Pragmatics lets us communicate "
            "efficiently without spelling out every implication. It also allows "
            "indirectness — politeness, irony, implication — which serves "
            "important social functions."
        ),
        common_confusion=(
            "Autistic people are frequently penalised for processing language "
            "closer to its literal semantic content than its pragmatic intent. "
            "This is not a deficit — it is a different (often more honest) "
            "relationship with language. The 'problem' is that neurotypical "
            "communication relies heavily on unstated pragmatic context and "
            "calls failure to read that context a 'social skills deficit'."
        ),
        example_human="'It's cold in here' — pragmatically: 'close the window / turn on the heater'.",
        example_body="Touching your face during a conversation pragmatically signals uncertainty or anxiety.",
        example_animal="A dog barking at the door pragmatically means 'let me in' even though the sound isn't a word.",
        example_plant="A plant wilting in drought pragmatically signals to caretakers: 'water needed now'.",
        example_machine="An HTTP 404 response pragmatically means: the thing you want isn't here, try elsewhere.",
        example_maths="A proof written for a journal skips steps a student needs spelled out. The mathematics is identical — the pragmatic context (who is reading?) changes what must be written.",
        example_music="A conductor's single downbeat to an orchestra is a pragmatic signal meaning 'start, now, at this tempo, together'. No notation required.",
        empowerment_note=(
            "If you've ever taken something 'too literally' and been laughed at, "
            "you weren't wrong — you were applying a perfectly valid interpretation. "
            "The gap is in the unstated pragmatic norms of a particular culture or "
            "group. Those norms were never written down or explained to you. "
            "Being confused by that gap is the right response."
        ),
    ),

    MechanicLayer(
        name="Feedback",
        plain_description=(
            "Every language has a feedback mechanism — a way for the receiver "
            "to signal back to the sender that the message was received, understood, "
            "or needs clarification. Nodding. 'Uh-huh'. A reply to an email. "
            "An error message from a compiler. The way a plant's stomata close "
            "in response to a chemical signal from a neighbour. Language is never "
            "one-directional — there is always a loop."
        ),
        why_it_exists=(
            "Without feedback, a sender cannot know if the message arrived, was "
            "understood, or had the intended effect. Feedback closes the communication "
            "loop. The absence of feedback is itself a signal — 'read but not replied' "
            "carries its own pragmatic content."
        ),
        common_confusion=(
            "Digital communication has broken many natural feedback loops. You "
            "cannot see the micro-expressions of the person reading your email. "
            "You cannot hear the pause that would have told you they're uncomfortable. "
            "The feedback layer of human language depends on physical co-presence, "
            "and most of our conflict in digital communication comes from "
            "interpretation in the absence of feedback signals."
        ),
        example_human="'Does that make sense?' is a direct request for feedback signal.",
        example_body="Mirroring someone's body posture is an automatic feedback signal: 'I'm in sync with you'.",
        example_animal="A vervet monkey's specific alarm call elicits specific responses — the response is the feedback.",
        example_plant="After releasing a volatlie compound, a plant may measure neighbouring plants' chemical responses.",
        example_machine="TCP/IP's ACK (acknowledgment) packet is the entire feedback layer of the internet.",
        example_maths="Checking an answer by working backwards (inverse operation) is arithmetic's feedback loop. A peer reviewer who finds a gap in a proof is the feedback loop of formal reasoning.",
        example_music="In call and response — blues, gospel, jazz improvisation — the listener's answer IS the communication. The feedback loop is built into the form itself.",
        empowerment_note=(
            "If you've ever felt like you were communicating into a void — "
            "no response, no acknowledgment, no indication of receipt — your "
            "discomfort is not oversensitivity. Lack of feedback is a communiation "
            "failure, and the discomfort it produces is a reasonable warning signal."
        ),
    ),
]


class LanguageMechanics:
    """
    The foundational layer of KindBridge.
    Teaches the five universal mechanics before any specific language.
    """

    def get_all_layers(self) -> List[MechanicLayer]:
        """Return all five mechanic layers in teaching order."""
        return MECHANIC_LAYERS

    def get_layer(self, name: str) -> Optional[MechanicLayer]:
        """Get a specific mechanic layer by name."""
        for layer in MECHANIC_LAYERS:
            if layer.name.lower() == name.lower():
                return layer
        return None

    def get_domain_examples(self, domain: str) -> List[dict]:
        """
        Get all examples for a specific domain across all layers.
        Shows how the mechanics manifest in that domain.
        """
        domain = domain.lower()
        examples = []
        for layer in MECHANIC_LAYERS:
            example_attr = f"example_{domain}"
            if hasattr(layer, example_attr):
                examples.append({
                    "mechanic": layer.name,
                    "example": getattr(layer, example_attr),
                    "description": layer.plain_description[:100] + "...",
                })
        return examples

    def get_introduction(self) -> str:
        """A plain-language introduction to why mechanics come first."""
        return (
            "Before we look at any specific language, let's look at what "
            "ALL languages are doing.\n\n"
            "Every type of language — human speech, body language, animal "
            "communication, plant signalling, machine code — is built from "
            "the same five layers. They look different on the surface. "
            "Underneath, they're solving the same problems.\n\n"
            "Once you see the structure, learning any language becomes "
            "recognising a familiar shape in new material. The confusion "
            "doesn't disappear entirely — but it becomes navigable.\n\n"
            "This is not simplified. This is the actual structure of language "
            "that linguists and communication theorists spend careers on. "
            "You deserve to know it clearly, not as gatekept expertise."
        )
