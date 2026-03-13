"""
core/domains.py — Domain registry for KindBridge.

The five domains of language in KindBridge are not ranked.
They are not on a hierarchy from 'primitive' to 'advanced'.
Human language is not superior to plant language — it is differently evolved
for different purposes. Machine language is not more precise than body language
— it is precise about different things.

The ranking we inherit (human language on top, everything else below) is a
cultural assumption, not a biological fact. Plants have been communicating
for 400 million years. Human spoken language: about 100,000.
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class LanguageDomain:
    """
    Defines one language domain: its nature, capabilities, and limits.
    """
    id: str
    name: str
    description: str
    age_on_earth: str          # How long this communication mode has existed
    primary_channel: str       # Physical medium of communication
    bandwidth: str             # How much information can it carry
    strengths: List[str]
    limitations: List[str]
    common_misconceptions: List[str]
    example_phrases: List[dict]   # {"expression": ..., "means": ..., "note": ...}
    learning_entry_point: str     # Where to start learning this domain


DOMAINS: List[LanguageDomain] = [

    LanguageDomain(
        id="human",
        name="Human Language",
        description=(
            "Spoken, written, and signed language as used by humans. Not one "
            "thing — there are approximately 7,000 living human languages and "
            "an unknowable number of dialects, registers, and sociolects. "
            "Human language is uniquely capable of recursion (sentences inside "
            "sentences), displacement (talking about things not present), and "
            "cultural transmission (passing patterns across generations). "
            "It is also uniquely capable of deliberate misdirection — something "
            "most other communication systems are not designed for."
        ),
        age_on_earth="~100,000 years (spoken), ~5,500 years (written)",
        primary_channel="Sound waves (spoken), light/touch (written/signed)",
        bandwidth=(
            "Moderate-to-high. Can carry abstract concepts, hypotheticals, "
            "and fiction. Cannot easily carry embodied sensation, precise "
            "spatial information, or emotional texture without significant loss."
        ),
        strengths=[
            "Carries abstract and hypothetical content",
            "Recursion: 'The person who told me that the report that was submitted...'",
            "Cultural transmission across generations",
            "Narrative: constructing shared fiction",
            "Meta-communication: talking about language itself",
        ],
        limitations=[
            "Words are imprecise containers — your meaning of 'love' and mine overlap but rarely match",
            "Designed for sequential channels (one word at a time, one speaker at a time)",
            "Cannot directly transmit embodied experience",
            "Easily used for deliberate deception",
            "Fast semantic drift — words change meaning constantly",
            "Carries enormous cultural and power assumptions as invisible freight",
        ],
        common_misconceptions=[
            "There is a 'correct' way to speak — in fact this claim almost always reflects class/cultural power",
            "More words = more precise — often the opposite is true",
            "Translation between languages is straightforward — most meaning is untranslatable",
            "Writing preserves meaning — written language is also interpretive",
        ],
        example_phrases=[
            {
                "expression": "I'm fine.",
                "means": "Could mean anything from 'I'm excellent' to 'I'm not fine at all but won't say so'",
                "note": "Context, tone, and relationship history do most of the work here",
            },
            {
                "expression": "We need to talk.",
                "means": "Pragmatically: this is serious and possibly bad",
                "note": "The literal meaning (we need to have a conversation) carries almost no weight",
            },
            {
                "expression": "You should come sometime.",
                "means": "Often: a social courtesy, not an actual invitation",
                "note": "In some cultures this IS a genuine invitation. The same phrase does different work.",
            },
        ],
        learning_entry_point=(
            "Start by noticing the gap between what words LITERALLY say and what "
            "they ACTUALLY do in context. Keep a running list for a week. You'll "
            "discover you already speak the pragmatics layer fluently — you just "
            "haven't had a word for what you were doing."
        ),
    ),

    LanguageDomain(
        id="body",
        name="Body Language",
        description=(
            "The communication system carried by posture, gesture, facial expression, "
            "eye contact, touch, distance (proxemics), and vocal qualities that aren't "
            "words (paralanguage — tone, pace, pitch, volume, silence). Body language "
            "predates spoken language by millions of years. It runs continuously "
            "alongside speech — and when the two conflict, people almost always "
            "believe the body over the words. This is not irrational. The body is "
            "harder to consciously control and less capable of deliberate deception."
        ),
        age_on_earth="~50 million years (primate precursors), continuous evolution",
        primary_channel="Light (visual), air pressure (vocal), touch (haptic)",
        bandwidth=(
            "Extremely high for emotional and relational content. Extremely low "
            "for abstract or technical content. You cannot explain quantum mechanics "
            "with body language, but you can communicate grief, danger, love, "
            "hierarchy, and intention with accuracy no words achieve."
        ),
        strengths=[
            "Continuous channel — transmitting constantly, even when 'not communicating'",
            "High accuracy for emotional content",
            "Harder to consciously fake than words",
            "Universal across many signals (fear responses, basic threat postures)",
            "Operates below conscious attention — received before words are processed",
        ],
        limitations=[
            "Cannot carry abstract content",
            "Many signals are culturally specific, not universal",
            "Invisible: you're transmitting constantly without awareness",
            "Interpretations of body language are often wrong when stripped of context",
            "Polyvagal responses (freeze, fawn) can produce misleading signals",
        ],
        common_misconceptions=[
            "Crossed arms mean 'closed off' — often people are just cold or comfortable",
            "Eye contact = honesty — many cultures consider direct eye contact rude or aggressive",
            "Body language experts can tell when you're lying — the research on this is weak",
            "Body language signals have universal fixed meanings — most are culturally variable",
        ],
        example_phrases=[
            {
                "expression": "Avoiding eye contact",
                "means": "Western cultures: possible deception or discomfort. East Asian cultures: respect.",
                "note": "Same signal, opposite meaning. Context is everything.",
            },
            {
                "expression": "Smiling",
                "means": "Can indicate happiness, social performance, nervousness, contempt (Duchenne vs social smile)",
                "note": "A Duchenne smile involves crinkling around the eyes. A social smile often doesn't.",
            },
            {
                "expression": "Leaning forward",
                "means": "Interest and engagement, OR aggression and challenge",
                "note": "The rest of the body tells you which. Single signals don't decode in isolation.",
            },
        ],
        learning_entry_point=(
            "For one day, pay attention to what you're doing with your hands and "
            "face during conversation — not to control it, just to notice it. "
            "The body is already producing language. This exercise teaches you "
            "to hear what you've always been saying."
        ),
    ),

    LanguageDomain(
        id="animal",
        name="Animal Language",
        description=(
            "Communication systems used by non-human animals. Not one thing — "
            "bee dances, whale song, vervet monkey alarm calls, elephant infrasound, "
            "octopus chromatophore patterns, dolphin signature whistles, crow "
            "facial recognition and corvid tool communication. The question 'do "
            "animals have language?' has been answered: yes, though not all animal "
            "communication has all the features of human language (and human "
            "language lacks features animal communication has). Cetacean dialects "
            "are culturally transmitted. Songbirds learn songs from adults the way "
            "children learn language. Crows hold grudges, pass information across "
            "generations, and use tools contextually."
        ),
        age_on_earth="~500 million years (chemical signalling); complex vocalisations ~150 million",
        primary_channel="Sound, chemistry, light/colour, touch, vibration, infrasound",
        bandwidth=(
            "Highly variable by species. Honeybee waggle dance carries "
            "remarkable precision (direction, distance, quality of food source). "
            "Sperm whale codas carry identity and cultural lineage. Cannot carry "
            "hypotheticals the way human language does — mostly present-tense, "
            "present-context. Some evidence for referential displacement in apes."
        ),
        strengths=[
            "Evolved for specific ecological needs — extremely efficient within that niche",
            "Chemical channels (pheromones) can carry identity, reproductive status, path information",
            "Vibration channels reach through opaque media (earth, water, wood)",
            "Some systems (cetacean, corvid) show cultural transmission",
            "No capability for deliberate misdirection in most species (no 'lying' instinct)",
        ],
        limitations=[
            "Mostly context-bound — cannot discuss hypotheticals or absence",
            "Cannot combine symbols in arbitrary new ways (limited productivity)",
            "We cannot decode most of it — the limit is on our end",
            "Inter-species miscommunication is profound and frequent",
        ],
        common_misconceptions=[
            "Animals 'just react' — crow problem-solving and tool use require planning",
            "Animal communication is simple — sperm whale coda systems are enormously complex",
            "We understand what animals are communicating — we barely scratch the surface",
            "Only humans have culture — cetacean and corvid cultures are well-documented",
        ],
        example_phrases=[
            {
                "expression": "Honeybee waggle dance (direction 30° from vertical, duration 1.5s)",
                "means": "Food source is approximately 1.5km away, at 30° from the sun's current direction",
                "note": "This encodes distance, direction, and quality simultaneously. In the dark, on a vertical surface.",
            },
            {
                "expression": "Vervet monkey 'eagle alarm'",
                "means": "Aerial predator — look up, seek cover",
                "note": "Distinct from 'snake alarm' (look down) and 'leopard alarm' (climb trees). Three distinct signals with three distinct appropriate responses.",
            },
            {
                "expression": "Dog 'play bow' (front legs down, rear up)",
                "means": "What follows is play, not aggression — even if I growl or bite",
                "note": "A meta-communicative signal: it frames the meaning of subsequent signals.",
            },
        ],
        learning_entry_point=(
            "Pick one species you interact with (dog, cat, bird in your garden) "
            "and spend a week cataloguing their signals without interpreting them. "
            "Just: 'they did X, then Y happened.' After a week, patterns emerge. "
            "You're doing field linguistics. The same method that Konrad Lorenz used."
        ),
    ),

    LanguageDomain(
        id="plant",
        name="Plant Language",
        description=(
            "Chemical, electrical, and structural communication systems used by "
            "plants and fungi. Not metaphorical — measurable, documented, "
            "functionally specific. Plants release volatile organic compounds "
            "(VOCs) when damaged that neighbouring plants detect and use to "
            "upregulate their own defences. Mycorrhizal fungal networks ('wood "
            "wide web') transmit carbon, phosphorus, and chemical signals between "
            "trees — including preferential transmission to offspring. "
            "Electrical signals propagate through plants at ~1mm/second, "
            "coordinating systemic responses. There is no central 'brain' — "
            "the network IS the communications architecture."
        ),
        age_on_earth="~470 million years (land plants); chemical signalling far older",
        primary_channel="Chemistry (volatile, root exudate), electrical, structural (growth pattern)",
        bandwidth=(
            "Low symbolic bandwidth but high relational bandwidth. Cannot encode "
            "narrative. Can encode: current threat type, its location, its severity, "
            "neighbouring plant relationships, soil chemistry, seasonal signals, "
            "and identity (plants can recognise self from non-self in root contact)."
        ),
        strengths=[
            "Operates through opaque media (soil, wood) where light and sound fail",
            "Persistence — chemical signals in soil can last hours or longer",
            "No dependency on attention — the receiver doesn't need to 'be listening'",
            "Includes identity recognition (self/non-self discrimination)",
            "Kin-selective (mycorrhizal networks preferentially support offspring)",
        ],
        limitations=[
            "Slow — electrical signals propagate at ~1mm/s, not real-time",
            "Context-bound — no evidence of displacement (talking about absence or future)",
            "Cannot carry abstract content",
            "Degraded by industrial agriculture (breaks fungal networks)",
        ],
        common_misconceptions=[
            "Plants can't communicate — the VOC and mycorrhizal research settles this",
            "Plants don't have memory — they do, both epigenetic and electrical",
            "The 'wood wide web' is purely cooperative — there is also competition and parasitism in fungal networks",
            "Plant communication requires intentionality — it's functional, not necessarily intentional",
        ],
        example_phrases=[
            {
                "expression": "Methyl jasmonate release (VOC)",
                "means": "Herbivore attack in progress — neighbouring plants upregulate defence compounds",
                "note": "Detected across species barriers. A willow's signal is received by a maple.",
            },
            {
                "expression": "Strigolactone released from roots",
                "means": "Signal to mycorrhizal fungi: 'establish symbiosis here'",
                "note": "The same compound is detected by parasitic plants like Striga, which use it to locate hosts.",
            },
            {
                "expression": "Action potential propagation after wounding",
                "means": "System-wide signal: activate wound response in distal tissues",
                "note": "Electrical signal that coordinates defence chemistry across a leaf, stem, or root system.",
            },
        ],
        learning_entry_point=(
            "Observe what happens to neighbouring plants when one is damaged. "
            "Notice timing — do they begin upregulating the same defences? "
            "Read Monica Gagliano's work and Suzanne Simard's 'Finding the Mother Tree'. "
            "The barrier here is not complexity — it's the cultural resistance to "
            "taking plant cognition seriously. That resistance is a cultural artefact, "
            "not a scientific position."
        ),
    ),

    LanguageDomain(
        id="machine",
        name="Machine Language",
        description=(
            "The communication systems of machines: programming languages, protocols, "
            "data formats, APIs, command-line interfaces, operating system calls. "
            "Not one thing — there are thousands of programming languages, each "
            "designed for specific purposes. Machine language is uniquely unambiguous "
            "by design — a computer cannot fill in pragmatic gaps the way a human "
            "listener can. Every instruction must be complete, or it fails. This "
            "precision is both its power and the reason it seems so unforgiving: "
            "it takes your words exactly at face value."
        ),
        age_on_earth="~80 years (electronic computers); concept older",
        primary_channel="Electrical signal (binary), light (optical), electromagnetic",
        bandwidth=(
            "Theoretically unbounded for structured data. Cannot carry ambiguity, "
            "pragmatics, or emotional content. What it can carry, it carries perfectly. "
            "What it can't, it doesn't carry at all — it fails rather than approximating."
        ),
        strengths=[
            "Unambiguous by design — a program either works or it doesn't",
            "Reproducible — the same input produces the same output reliably",
            "Formally verifiable — you can prove properties of programs",
            "Massively parallelisable",
            "Cross-cultural — Python works identically in Australia, Brazil, and Japan",
        ],
        limitations=[
            "No pragmatic inference — the computer does exactly what you said, not what you meant",
            "Brittle to ambiguity — one misplaced character can halt execution",
            "Context-insensitive — no shared cultural background to draw on",
            "Formal systems have inherent limits (Gödel's incompleteness theorems)",
            "Human-designed, human-biased — all the assumptions of the designer are encoded invisibly",
        ],
        common_misconceptions=[
            "Programming is about computers — it's about precisely describing intent",
            "You need to be a maths person to code — you need to be a language person",
            "Code is neutral and objective — all code encodes the assumptions of its authors",
            "More complex code is better — the best code is the simplest code that does the job",
        ],
        example_phrases=[
            {
                "expression": "404 Not Found",
                "means": "The server received your request but the thing you asked for doesn't exist at that address",
                "note": "Not 'the internet is broken'. Not 'you did something wrong'. Specifically: not found at that specific location.",
            },
            {
                "expression": "print('Hello')",
                "means": "Display the text 'Hello' to the output channel",
                "note": "Every programming language has a version of this. It's usually the first thing you learn. It is genuinely that simple to start.",
            },
            {
                "expression": "if x > 0: do_something()",
                "means": "IF the value of x is greater than zero, THEN execute do_something()",
                "note": "This is the conditional form that underlies ALL machine decision-making. Every 'smart' system is a very large pile of these.",
            },
        ],
        learning_entry_point=(
            "Before learning any syntax, understand this: programming is the activity "
            "of writing instructions for an extremely literal entity that has no "
            "common sense. Everything you need to say, you must say. Nothing can be "
            "implied. This is frustrating precisely because human language IS built "
            "on implication. The frustration is appropriate — you're working against "
            "your linguistic instincts. That's the adjustment. After that, it's "
            "just vocabulary."
        ),
    ),

    LanguageDomain(
        id="maths",
        name="Mathematical Language",
        description=(
            "Mathematics is a formal language: a system of symbols, syntax rules, and "
            "semantic conventions built to communicate precise quantitative and structural "
            "relationships. It is not a natural language — it was designed, iteratively, "
            "over millennia, by people who needed to describe things that ordinary words "
            "handle badly: quantities, relationships, change, space, proof. "
            "The reason mathematics feels alien to many people is not a failure of "
            "intelligence — it is a failure of teaching. Most people are taught "
            "mathematical procedures without being taught mathematical language. "
            "You can run the procedures perfectly and still feel like you don't understand "
            "what you're doing. That is an accurate feeling: you were taught to "
            "recite the words without being told what they mean."
        ),
        age_on_earth="~5,000 years (written numerals, Mesopotamia); counting systems far older",
        primary_channel="Visual symbols (printed/digital notation); spoken description",
        bandwidth=(
            "Extremely high for structural and quantitative information — mathematics can "
            "describe the trajectory of a planet or the curvature of spacetime with a precision "
            "words cannot approach. Zero bandwidth for emotional content or social nuance. "
            "What it can carry, it carries exactly. What it can't, it doesn't attempt."
        ),
        strengths=[
            "Unambiguous by design when notation conventions are shared",
            "Cross-cultural — 2+2=4 means the same thing in every spoken language",
            "Compresses complex relationships into compact, inspectable form",
            "Formally verifiable — you can prove things are true, not just argue they are",
            "Generative: the same rules applied to new problems produce new knowledge",
        ],
        limitations=[
            "Notation is not universal — 'billion' means different things in British and American usage",
            "Context-dependent meaning: '-' means subtraction, negation, a range, or an approximation",
            "The language itself cannot tell you what to model — that requires judgment",
            "Zero accessibility without explicit teaching of notation conventions",
            "G\u00f6del's incompleteness theorems: any sufficiently complex formal system contains true statements it cannot prove",
        ],
        common_misconceptions=[
            "'I'm not a maths person' — most maths difficulty is language difficulty, not intelligence",
            "Maths is about numbers — it is about structure, pattern, and relationship",
            "There is one right way to solve a problem — there are often many valid paths",
            "Speed = competence — fast calculation and mathematical understanding are different skills",
            "Maths is objective and bias-free — what we choose to model, and how, is full of assumptions",
        ],
        example_phrases=[
            {
                "expression": "x = 5",
                "means": "Variable assignment (code), equality (algebra), or definition (proof). Same symbols, three different relationships.",
                "note": "This is why 'x = x + 1' is valid in programming (update the value) and nonsense in algebra (no number equals itself plus one).",
            },
            {
                "expression": "\u221e",
                "means": "Not 'a very large number' — a direction: that which has no upper bound. Different kinds of infinity are different sizes (Cantor's theorem).",
                "note": "Most people learn infinity as 'biggest possible'. It's a direction, not a destination. This one concept, properly understood, unlocks most of calculus.",
            },
            {
                "expression": "\u222bf(x)dx",
                "means": "The accumulated change — if you added up infinitely many infinitely thin slices of this thing, what would you get?",
                "note": "The notation is dense. The question is not. Once the question is clear, the symbols are just shorthand for it.",
            },
        ],
        learning_entry_point=(
            "Start not with numbers but with the question: what is this trying to describe? "
            "Every mathematical expression is an attempt to capture a relationship precisely. "
            "Before asking 'how do I solve this', ask 'what is this saying?'. "
            "If a piece of maths feels opaque, the barrier is almost always a notation "
            "convention nobody explained. Ask: what does this symbol mean, in plain language, "
            "right now? That question, asked persistently, unlocks more mathematics than "
            "any number of worked examples."
        ),
    ),

    LanguageDomain(
        id="music",
        name="Music",
        description=(
            "Music is one of the oldest communication systems in human history — and one "
            "of the most misunderstood as a 'language'. Music communicates emotional states, "
            "cultural identity, relational intention, and somatic response with a directness "
            "that words cannot match. It does this through pitch, rhythm, timbre, dynamics, "
            "and structure — all of which are symbol systems with their own syntax, semantics, "
            "and pragmatics. Formal notation (scores, tabs, chord charts) is the written "
            "form of the language. Musical performance is the spoken form. "
            "The claim 'I'm not musical' almost always means 'I was not taught to read the "
            "notation' — which is like confusing reading with language. You already speak music. "
            "You have been understanding and producing musical communication since before you "
            "could speak words."
        ),
        age_on_earth="~50,000+ years (oldest known instruments — bone flutes); probably far older via voice",
        primary_channel="Sound waves (acoustic, electronic); visual notation (score, tablature)",
        bandwidth=(
            "Extremely high for emotional and somatic content — music can induce specific "
            "physiological responses (heart rate changes, goosebumps, tears, movement) that "
            "words can only approximate. Moderate for cultural and identity signals. "
            "Low for propositional content — music cannot specify facts. "
            "The channel carrying the least semantic content is often the one that lands hardest."
        ),
        strengths=[
            "Pre-linguistic — reaches past verbal processing into somatic and emotional response",
            "Cross-cultural in some dimensions (rhythm entrainment, basic tonal consonance)",
            "Temporal — communicates process and change, not just states",
            "Call and response: built-in feedback mechanism, explicit in many traditions",
            "Layered: can carry multiple simultaneous voices, each with its own syntactic line",
        ],
        limitations=[
            "Cannot specify propositions directly — music cannot say 'turn left at the lights'",
            "Semantic content is heavily culturally conditioned — 'sad minor key' is Western",
            "Western staff notation represents one musical tradition among hundreds",
            "Time-bound — music exists in the listener's present; cannot be re-read like text",
            "Production requires physical skill that notation alone does not provide",
        ],
        common_misconceptions=[
            "'I'm not musical' — you have had musical responses your entire life. You may not read notation.",
            "Music is about notes — it's about the RELATIONSHIPS between notes and the timing between events",
            "Western notation is universal — there are hundreds of notation systems and oral traditions with none",
            "Technical difficulty = quality — musical communication is often most powerful at its simplest",
            "You need to understand theory to perform music — theory describes what people were already doing",
        ],
        example_phrases=[
            {
                "expression": "A minor chord (e.g. Am: A-C-E)",
                "means": "In Western culture: tension, melancholy, introspection. That semantic content is a cultural convention, not an acoustic fact.",
                "note": "You've been trained to hear a minor chord as sad. A listener from a different musical tradition may not have the same response. The feeling is in you, shaped by years of exposure — not in the chord.",
            },
            {
                "expression": "4/4 time signature",
                "means": "Four quarter-note beats per bar. The default syntax underlying most Western pop, rock, and dance music.",
                "note": "Once you hear it as structure rather than 'the beat', odd meters and polyrhythms become legible as deliberate departures from a known norm — not chaos.",
            },
            {
                "expression": "Fermata (\U0001d110) over a note",
                "means": "Hold this note longer than its written value — exactly how long is left to the performer's judgment.",
                "note": "This is an explicit pragmatic instruction: the notation defers to contextual interpretation. The score trusts the performer to read the moment. Not all languages make this deference explicit.",
            },
        ],
        learning_entry_point=(
            "Start by listening as an analyst, not an evaluator. Pick one song you know well. "
            "First listen: track only the rhythm — tap it out. "
            "Second: track only the bass (the lowest continuous voice). "
            "Third: track the space between the sounds — the silences. "
            "You are learning to decompose a simultaneous multi-channel communication into "
            "its syntactic layers. This is the skill music education should start with, "
            "and almost never does. Hearing the structure first is the shortcut to everything "
            "that comes after."
        ),
    ),
]

class DomainRegistry:
    """Registry of all five language domains."""

    def get_all(self) -> List[LanguageDomain]:
        return DOMAINS

    def get(self, domain_id: str) -> LanguageDomain:
        for d in DOMAINS:
            if d.id == domain_id:
                return d
        raise KeyError(f"Unknown domain: {domain_id}")

    def get_intro(self) -> str:
        return (
            "Language is not one thing. Here are seven domains — seven different "
            "evolutionary and cultural solutions to the same fundamental problem: how do "
            "entities share information across space and time?\n\n"
            "Human language, body language, animal communication, plant signalling, "
            "machine code, mathematical notation, and music. "
            "They emerged independently. They use different physical channels. "
            "They are optimised for different purposes. And they share a common "
            "structure — the mechanics of symbols, syntax, semantics, pragmatics, "
            "and feedback — because those mechanics solve the same underlying problems.\n\n"
            "None of them is the 'real' language. All of them are real languages."
        )
