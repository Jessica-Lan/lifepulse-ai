from enum import Enum
from lifepulse_ai.engine.signal_processor import SignalBundle


class Archetype(str, Enum):
    CLARIFIER = "Clarifier"
    EXPLORER = "Explorer"
    STABILIZER = "Stabilizer"
    EXECUTOR = "Executor"


class ArchetypeEngine:
    """
    Minimal rule-based archetype inference.

    This is only a placeholder; real implementation would use
    sequence models and conversational context.
    """

    def infer(self, signals: SignalBundle) -> Archetype:
        text = signals.raw_text.lower()

        if any(w in text for w in ["structure", "逻辑", "framework", "怎么拆"]):
            return Archetype.CLARIFIER

        if any(w in text for w in ["idea", "灵感", "可能", "还有什么"]):
            return Archetype.EXPLORER

        if any(w in text for w in ["焦虑", "崩溃", "抖", "overwhelmed", "anxious"]):
            return Archetype.STABILIZER

        if any(w in text for w in ["steps", "action", "next", "怎么做"]):
            return Archetype.EXECUTOR

        # default: use question vs statement as tiny heuristic
        if signals.has_question:
            return Archetype.CLARIFIER
        return Archetype.EXECUTOR
