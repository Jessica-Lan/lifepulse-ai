from dataclasses import dataclass


@dataclass
class ProductProfile:
    """Simple placeholder for product-line configuration."""
    name: str
    tier: str
    includes_org_layer: bool = False


DEFAULT_PRODUCT = ProductProfile(
    name="LifePulse Personal",
    tier="documentation-only",
    includes_org_layer=False,
)
