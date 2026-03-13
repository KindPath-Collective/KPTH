"""
core/empowerment.py — The psychological safety layer of KindBridge.

The premise: confusion about language is not a personal failing.

The experience of looking at language — a word, a sentence, a social signal,
a piece of code — and thinking "I don't understand this" or "this seems
unnecessarily hard" is frequently:
  a) correct (the thing IS unnecessarily hard), or
  b) a reasonable response to a genuinely complex system that no one
     explained well

The educational system, professional culture, and social environments
frequently respond to language confusion with:
  - Correction (you said it wrong)
  - Dismissal (maybe this isn't for you)
  - Implication (being confused means you're less intelligent)

This module is the antidote. Not false reassurance — specific, evidence-based
reframing of what confusion actually signals.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class EmpowermentInsight:
    """
    A specific reframe for a common experience of language inadequacy.
    Each insight names the specific feeling, then provides the honest reframe.
    """
    feeling: str         # The experience being reframed
    truth: str           # The actual evidence-based reality
    examples: List[str]  # Real examples that validate the experience
    action: str          # What to do with this reframe


EMPOWERMENT_INSIGHTS: List[EmpowermentInsight] = [

    EmpowermentInsight(
        feeling="I feel stupid because I don't understand this word/concept.",
        truth=(
            "You are likely experiencing one of three real phenomena: "
            "(1) The word has not been explained to you, only used (this is extremely common in education). "
            "(2) The word is unnecessarily technical for the concept it describes. "
            "(3) The word was designed for a community you're not in yet — and has not been translated. "
            "None of these are signs of your intelligence. All of them are signs of communication failure by the system, not by you."
        ),
        examples=[
            "Einstein failed his university entrance exam the first time. He was processing things differently.",
            "Richard Feynman said if you can't explain something simply, you don't understand it well enough.",
            "Most legal documents are written above a 12th-grade reading level. Most people read at a 7th-grade level. This is by design.",
            "The Dunning-Kruger effect works both ways: genuine competence is often accompanied by uncertainty.",
        ],
        action=(
            "Ask: 'was this actually explained to me, or was I expected to absorb it by context?' "
            "If it was never explicitly explained, your confusion is the right response. "
            "Then ask: 'can someone explain this without the jargon?' This is always a reasonable request."
        ),
    ),

    EmpowermentInsight(
        feeling="I feel like everyone else understands this except me.",
        truth=(
            "They don't. Most people in most rooms are operating at different levels of "
            "understanding and not admitting it. The social penalty for admitting confusion "
            "is high enough that people perform understanding they don't have. This creates "
            "the illusion that the room is full of people who understand. "
            "The person who asks 'can you explain that?' is usually doing everyone a favour."
        ),
        examples=[
            "The 'Emperor's New Clothes' phenomenon is documented in social psychology. Social pressure to perform understanding is real.",
            "Studies consistently find that students' self-reported understanding is poorly correlated with actual test performance.",
            "The culture of nodding along in meetings has its own name: 'impression management'.",
            "'The only stupid question is the one you don't ask' is a cliché because it keeps being necessary.",
        ],
        action=(
            "Ask the question you're afraid to ask. You will almost always be thanked — "
            "privately if not publicly — by others who had the same question. "
            "Admitting confusion is a form of intellectual honesty, not weakness."
        ),
    ),

    EmpowermentInsight(
        feeling=(
            "I keep thinking 'why is this so complicated?' and then feeling bad "
            "about myself for thinking that."
        ),
        truth=(
            "This is the fagazzi instinct and it is one of the most accurate "
            "language detectors you have. 'Why is this so complicated?' correctly "
            "identifies the proportion of the time: the thing actually is more "
            "complicated than it needs to be. Academic writing is often deliberately "
            "obtuse. Corporate communication is often padded. Legal language is "
            "often designed to be interpreted by specialists. Bureaucratic language "
            "often buries accountability. Your instinct is working."
        ),
        examples=[
            "Plain Language movements in government exist precisely because official language has historically been unnecessarily complex.",
            "George Orwell's 1946 essay 'Politics and the English Language' made this case explicitly: vague, inflated language is often a political tool.",
            "Studies of medical informed-consent documents find they routinely exceed the literacy level of their target population.",
            "Warren Buffett is famous for writing shareholder letters in folksy, plain language — and is praised for it. The norm in that industry runs the other way.",
        ],
        action=(
            "Keep the instinct. Train it. When something seems unnecessarily complicated, "
            "ask: 'is this genuinely complex, or is it made to seem complex?' "
            "Genuine complexity resists simplification because the reality is intricate. "
            "Fagazzi complexity disappears when you replace it with plain words. "
            "Test the difference."
        ),
    ),

    EmpowermentInsight(
        feeling="Different people mean different things by the same words and I find this exhausting.",
        truth=(
            "Good. You're perceiving accurately. Words are not shared containers with a "
            "fixed volume of meaning. They are approximations that land differently in "
            "every mind, shaped by individual experience, culture, age, context, and "
            "relationship history. The exhaustion is real. The word 'family' means "
            "something specific to you that it doesn't mean to the person next to you. "
            "Neither version is wrong. Both are real. This is simply how language works — "
            "and most of us are never told."
        ),
        examples=[
            "The word 'community' in a rural indigenous context and in a startup press release are doing completely different things.",
            "Couples in conflict research: partners in distress often turn out to have different meanings for core relationship words.",
            "In philosophy of language this is called 'semantic underdetermination' — language doesn't fully fix meaning.",
            "Translators often spend more time on small common words (home, freedom, love) than technical terms.",
        ],
        action=(
            "When a word is doing important work in a conversation, slow down and ask "
            "'what do you mean by that?' — not as a challenge, but as genuine inquiry. "
            "Semantic alignment (getting your meanings to overlap) is one of the most "
            "useful communication skills and one of the least taught."
        ),
    ),

    EmpowermentInsight(
        feeling="I can't put what I'm experiencing into words and I feel inarticulate.",
        truth=(
            "Some experiences don't have words yet — or don't have words in your current "
            "language. This is the limit of language, not the limit of you. "
            "Pain researchers gave patients 78 words because no single word was enough. "
            "Poets exist because ordinary prose doesn't reach certain things. Music exists "
            "because poetry doesn't reach others. The inability to name your experience "
            "in words says nothing about the validity, reality, or importance of that experience."
        ),
        examples=[
            "The Japanese have 'mono no aware' — the bittersweet awareness of impermanence. English doesn't have this.",
            "The Portuguese have 'saudade' — longing for something loved and gone. English doesn't have this.",
            "Chronic pain patients are systematically disbelieved partly because pain is linguistically underdescribed.",
            "Trauma often exists in a pre-verbal state — this is not a personal failure, it is a documented neurological phenomenon.",
        ],
        action=(
            "When you can't find words: say that. 'I can't quite put this into words, but...' "
            "is honest communication. If it's important, try metaphor, gesture, art, or music. "
            "The experience is real whether you can name it or not. The naming is useful. "
            "But the naming is not the thing itself."
        ),
    ),

    EmpowermentInsight(
        feeling="I was marked down / corrected / dismissed for using language 'wrong'.",
        truth=(
            "Possibly the most important reframe in this whole module: "
            "Most of what is taught as 'correct language' in schools is the dialect "
            "of whoever held social power when the curriculum was written. "
            "It is not linguistic truth — it is linguistic power. "
            "African American Vernacular English, Aboriginal English, and dozens of "
            "other dialects have rigorous internal grammar. Being told they are 'wrong' "
            "is a social assertion masquerading as a grammatical fact."
        ),
        examples=[
            "Split infinitives ('to boldly go') were 'wrong' because Latin grammar doesn't allow them — English grammar is not Latin.",
            "Ending sentences with prepositions is 'wrong' by a rule invented by 17th-century grammarians trying to be like Latin.",
            "Most prescriptive grammar rules can be traced to class-based assertions, not linguistic science.",
            "Linguists (the actual scientists of language) are descriptivists — they describe what language does, not what it 'should' do.",
        ],
        action=(
            "Know the difference between a dialect difference and a communication failure. "
            "You may choose to code-switch (use standard dialect in professional contexts) "
            "because that's a pragmatic choice. But know that you are choosing to speak "
            "a particular community's norms — not becoming 'correct'."
        ),
    ),
]


class EmpowermentLayer:
    """
    The psychological safety layer. Returns reframes for common experiences
    of language inadequacy, backed by evidence rather than reassurance.
    """

    def get_all(self) -> List[EmpowermentInsight]:
        return EMPOWERMENT_INSIGHTS

    def get_by_feeling(self, feeling_keyword: str) -> List[EmpowermentInsight]:
        """Find insights that match a keyword in the feeling description."""
        kw = feeling_keyword.lower()
        return [i for i in EMPOWERMENT_INSIGHTS if kw in i.feeling.lower() or kw in i.truth.lower()]

    def get_intro(self) -> str:
        return (
            "This section is for the experience of feeling inadequate about language.\n\n"
            "Not the experience of learning something you don't know yet (that's fine — "
            "that's just learning). The experience of feeling like you lack something "
            "that everyone else has: that you're fundamentally bad at language, that "
            "you should have understood that, that you're stupid for being confused.\n\n"
            "That experience is almost always a response to something real: a system "
            "that failed to explain clearly, or language that was designed to exclude, "
            "or a cultural norm that was never stated.\n\n"
            "Read these reframes not as reassurance but as evidence. Each one is "
            "backed by actual linguistic research. The confusion you felt was appropriate."
        )

    def get_core_statement(self) -> str:
        return (
            "The central claim of KindBridge:\n\n"
            "If you ever looked at something — a word, a sentence, a social convention, "
            "a piece of code, a rule — and thought: 'I don't get this, and it seems "
            "unnecessarily complicated, and I feel stupid for not getting it'\n\n"
            "— Consider the real possibility that you were right on all three counts:\n\n"
            "1. The thing was genuinely poorly explained or unnecessarily complex.\n"
            "2. Your confusion was the appropriate response to that complexity.\n"
            "3. The feeling of stupidity was a cultural installation, not an accurate self-assessment.\n\n"
            "This does not mean everything is equally easy. Some things are genuinely hard. "
            "But there is a category of difficulty that is manufactured — fagazzi difficulty — "
            "and it is more common than most people are told.\n\n"
            "You were not less than. You were perceptive."
        )
