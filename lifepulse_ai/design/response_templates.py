from lifepulse_ai.engine.interaction_mode import InteractionPlan
from lifepulse_ai.engine.archetype_inference import Archetype


class ResponseRenderer:
    """
    Turns an InteractionPlan into a natural language stub.

    This is intentionally simple; real rendering would call
    a language model with structured prompts.
    """

    def render(self, plan: InteractionPlan) -> str:
        prefix = f"[{plan.archetype.value} · {plan.style}] "

        if plan.archetype == Archetype.CLARIFIER:
            return prefix + "I'll give you a clear, step-by-step structure in about " \
                   f"{plan.steps} steps."
        if plan.archetype == Archetype.EXPLORER:
            return prefix + "Let's explore a few different angles and possibilities."
        if plan.archetype == Archetype.STABILIZER:
            return prefix + "First we slow things down, then we stabilise your baseline, " \
                   "then we choose one small next step."
        if plan.archetype == Archetype.EXECUTOR:
            return prefix + "Here are concrete next actions you can take immediately."

        return prefix + "I'll respond in a concise and helpful way."
