"""
KindBridge — Language Simplification and Unification Module

The belief that drove this module: confusion about language is not a personal
failing. It is a reasonable response to genuinely complex systems that are
frequently made MORE complex than they need to be. If you ever looked at a
word, a sentence, a gesture, a line of code — and thought "this is a fagazzi"
(fake, unnecessarily complex, designed to exclude rather than include) —
you were often right.

KindBridge teaches:
  1. The mechanics of language itself — before any specific language
  2. The five domains of language: human, body, animal, plant, machine
  3. How language fails — misinterpretation, ambiguity, deliberate obscurity
  4. How to detect fagazzi — language complexity that serves gatekeeping, not communication
  5. That you are not less intelligent for finding language difficult

Every lesson here is built on one premise: understanding is a right, not a privilege.
"""

__version__ = "1.0.0"
__author__ = "KindPath Collective"

from .core.mechanics import LanguageMechanics
from .core.domains import DomainRegistry
from .core.empowerment import EmpowermentLayer
from .core.limitations import LanguageLimitations
from .fagazzi.detector import FagazziDetector
from .bridge.translator import BridgeTranslator

__all__ = [
    "LanguageMechanics",
    "DomainRegistry",
    "EmpowermentLayer",
    "LanguageLimitations",
    "FagazziDetector",
    "BridgeTranslator",
]
