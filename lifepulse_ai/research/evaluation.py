from dataclasses import dataclass


@dataclass
class EvaluationResult:
    """Placeholder for evaluation metrics."""
    clarity_gain: float | None = None
    stress_delta: float | None = None
    perceived_helpfulness: float | None = None
