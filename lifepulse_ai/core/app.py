from lifepulse_ai.engine.signal_processor import SignalProcessor
from lifepulse_ai.engine.archetype_inference import ArchetypeEngine
from lifepulse_ai.engine.interaction_mode import InteractionPlanner
from lifepulse_ai.design.response_templates import ResponseRenderer
from lifepulse_ai.governance.guardrails import GovernanceLayer


class LifePulseApp:
    """
    Minimal orchestration layer tying together:
    - signal processing
    - archetype inference
    - interaction planning
    - governance checks
    - response rendering
    """

    def __init__(self) -> None:
        self.signals = SignalProcessor()
        self.archetypes = ArchetypeEngine()
        self.planner = InteractionPlanner()
        self.renderer = ResponseRenderer()
        self.governance = GovernanceLayer()

    def process_message(self, text: str) -> str:
        """End-to-end demo pipeline with placeholder logic."""
        extracted = self.signals.extract(text)
        archetype = self.archetypes.infer(extracted)
        plan = self.planner.plan(archetype, extracted)
        safe_plan = self.governance.review(plan)
        response = self.renderer.render(safe_plan)
        return response

    def run_demo(self) -> None:
        """Simple CLI loop for demonstration."""
        print("LifePulse AI – Hybrid Intelligence Skeleton (Pre-MVP)")
        print("Type 'exit' to quit.\n")

        while True:
            user = input("You: ").strip()
            if not user:
                continue
            if user.lower() in {"exit", "quit"}:
                print("LifePulse: Bye.")
                break

            reply = self.process_message(user)
            print(f"LifePulse: {reply}\n")
