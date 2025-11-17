from dataclasses import dataclass
from lifepulse_ai.engine.interaction_mode import InteractionPlan


@dataclass
class GovernanceDecision:
    """Represents a reviewed interaction plan."""
    allowed: bool
    reason: str | None = None


class GovernanceLayer:
    """
    Placeholder guardrail layer.

    Real implementation would check:
    - safety categories
    - scope constraints
    - regulatory boundaries
    """

    def review(self, plan: InteractionPlan) -> InteractionPlan:
        # For now we simply return the plan unchanged.
        # Hook point for future safety / policy logic.
        _ = GovernanceDecision(allowed=True, reason=None)
        return plan
