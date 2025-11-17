from dataclasses import dataclass
from lifepulse_ai.engine.archetype_inference import Archetype
from lifepulse_ai.engine.signal_processor import SignalBundle


@dataclass
class InteractionPlan:
    """Abstract plan for how to respond."""
    archetype: Archetype
    style: str
    steps: int
    include_reframe: bool


class InteractionPlanner:
    """
    Maps archetype + signals → high-level interaction plan.
    """

    def plan(self, archetype: Archetype, signals: SignalBundle) -> InteractionPlan:
        if archetype == Archetype.CLARIFIER:
            return InteractionPlan(archetype, style="structured", steps=3, include_reframe=False)
        if archetype == Archetype.EXPLORER:
            return InteractionPlan(archetype, style="branching", steps=3, include_reframe=True)
        if archetype == Archetype.STABILIZER:
            return InteractionPlan(archetype, style="grounding", steps=2, include_reframe=True)
        if archetype == Archetype.EXECUTOR:
            return InteractionPlan(archetype, style="direct", steps=3, include_reframe=False)

        # fallback, should not normally happen
        return InteractionPlan(archetype, style="direct", steps=1, include_reframe=False)
