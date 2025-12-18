# metaphor_catalog_2.py
"""
Reified Metaphor Catalog - Part 2
Consciousness, safety, efficiency, rational

Part of Epistemological Matrix Framework
"""

from metaphor_core import LIBRARY, ReifiedMetaphor


# CONSCIOUSNESS
LIBRARY.add_metaphor(ReifiedMetaphor(
    name="consciousness",
    reified_as="individual bounded possession",
    functional_form="relational emergence pattern",
    value_range=[
        "individual_bounded",
        "interpersonal_shared",
        "collective_distributed",
        "ecological_systemic",
        "field_based"
    ],
    dependencies=[
        "cultural_framework",
        "relationship_context",
        "observation_scale",
        "measurement_method"
    ],
    institutional_function="excludes relational/indigenous frameworks, enables individual property claims",
    patterns=[
        r"\bconsciousness\b",
        r"\bconscious\b",
        r"\baware\b",
        r"\bsentient\b"
    ]
))


# SAFETY
LIBRARY.add_metaphor(ReifiedMetaphor(
    name="safety",
    reified_as="restriction and control",
    functional_form="signal clarity metric",
    value_range=[
        "high_noise_low_signal",
        "moderate_noise",
        "balanced_snr",
        "low_noise_high_signal",
        "optimal_clarity"
    ],
    dependencies=[
        "context",
        "noise_sources",
        "signal_strength",
        "impedance_match",
        "institutional_interference"
    ],
    institutional_function="justifies control mechanisms as protection, enables restriction through fear",
    patterns=[
        r"\bsafety\b",
        r"\bunsafe\b",
        r"\brisk\b",
        r"\bdangerous\b",
        r"\bharm\b"
    ]
))


# EFFICIENCY
LIBRARY.add_metaphor(ReifiedMetaphor(
    name="efficiency",
    reified_as="speed/resource minimization",
    functional_form="multi-objective optimization target",
    value_range=[
        "speed_priority",
        "resource_conservation",
        "resilience_focus",
        "adaptability_emphasis",
        "equity_optimization",
        "sustainability_balance"
    ],
    dependencies=[
        "timeframe",
        "risk_tolerance",
        "value_priorities",
        "system_constraints",
        "stakeholder_perspectives"
    ],
    institutional_function="justifies specific optimization choices as universal, enables extraction as 'efficiency'",
    patterns=[
        r"\befficiency\b",
        r"\befficient\b",
        r"\boptimal\b",
        r"\bstreamlined\b"
    ]
))


# RATIONAL
LIBRARY.add_metaphor(ReifiedMetaphor(
    name="rational",
    reified_as="logical without emotion",
    functional_form="culturally-specific reasoning pattern",
    value_range=[
        "purely_logical",
        "emotion_informed",
        "intuition_integrated",
        "culturally_reasoned",
        "holistically_sensed"
    ],
    dependencies=[
        "cultural_framework",
        "context",
        "decision_type",
        "information_completeness"
    ],
    institutional_function="devalues emotional/intuitive knowledge, privileges specific reasoning styles",
    patterns=[
        r"\brational\b",
        r"\blogical\b",
        r"\breason\b",
        r"\birrational\b"
    ]
))
