from dataclasses import dataclass


@dataclass
class SignalBundle:
    """Lightweight container for extracted features."""
    raw_text: str
    length: int
    has_question: bool
    urgency_hint: bool


class SignalProcessor:
    """
    Very small placeholder feature extractor.

    In the real system this would:
    - analyse linguistic patterns
    - detect overload / clarity signals
    - recognise intent categories
    """

    def extract(self, text: str) -> SignalBundle:
        text_stripped = text.strip()
        return SignalBundle(
            raw_text=text_stripped,
            length=len(text_stripped),
            has_question=("?" in text_stripped),
            urgency_hint=any(w in text_stripped.lower()
                             for w in ["urgent", "now", "马上", "立刻"]),
        )
