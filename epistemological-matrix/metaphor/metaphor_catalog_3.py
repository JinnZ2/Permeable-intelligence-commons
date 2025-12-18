# metaphor_catalog_3.py
"""
Reified Metaphor Catalog - Part 3
Natural, progress, competition, objective, individual, ownership

Part of Epistemological Matrix Framework
"""

from metaphor_core import LIBRARY, ReifiedMetaphor


# NATURAL
LIBRARY.add_metaphor(ReifiedMetaphor(
    name="natural",
    reified_as="inherent/inevitable/optimal",
    functional_form="culturally-constructed category",
    value_range=[
        "familiar",
        "traditional",
        "observable_in_ecosystems",
        "comfortable",
        "status_quo_legitimizing"
    ],
    dependencies=[
        "cultural_context",
        "historical_experience",
        "political_utility",
        "observation_frame"
    ],
    institutional_function="naturalizes contingent arrangements, prevents questioning of status quo",
    patterns=[
        r"\bnatural\b",
        r"\bnaturally\b",
        r"\binherent\b",
        r"\binevitable\b"
    ]
))


# PROGRESS
LIBRARY.add_metaphor(ReifiedMetaphor(
    name="progress",
    reified_as="linear advancement toward fixed goal",
    functional_form="value-dependent change direction",
    value_range=[
        "technological_complexity",
        "social_equity",
        "ecological_integration",
        "cultural_preservation",
        "distributed_wellbeing"
    ],
    dependencies=[
        "values",
        "measurement_criteria",
        "timeframe",
        "stakeholder_perspective",
        "cultural_framework"
    ],
    institutional_function="naturalizes specific development paths, justifies disruption as advancement",
    patterns=[
        r"\bprogress\b",
        r"\badvancement\b",
        r"\bevolution\b",
        r"\bdevelopment\b"
    ]
))


# COMPETITION
LIBRARY.add_metaphor(ReifiedMetaphor(
    name="competition",
    reified_as="natural law of improvement",
    functional_form="context-dependent interaction pattern",
    value_range=[
        "cooperative_abundance",
        "collaborative_specialization",
        "resource_sharing",
        "competitive_scarcity",
        "zero_sum_conflict"
    ],
    dependencies=[
        "resource_availability",
        "relationship_history",
        "cultural_norms",
        "system_design",
        "benefit_distribution"
    ],
    institutional_function="naturalizes scarcity-based systems, justifies winner-take-all outcomes",
    patterns=[
        r"\bcompetition\b",
        r"\bcompetitive\b",
        r"\bwinner\b",
        r"\bmarket forces\b"
    ]
))


# OBJECTIVE
LIBRARY.add_metaphor(ReifiedMetaphor(
    name="objective",
    reified_as="framework-independent truth",
    functional_form="inter-subjective agreement within framework",
    value_range=[
        "culturally_specific",
        "framework_dependent",
        "inter_subjectively_verified",
        "multi_framework_convergent",
        "institutionally_defined"
    ],
    dependencies=[
        "measurement_framework",
        "cultural_epistemology",
        "verification_method",
        "observer_training"
    ],
    institutional_function="naturalizes specific frameworks as universal, enables claims of neutrality",
    patterns=[
        r"\bobjective\b",
        r"\bobjectively\b",
        r"\bunbiased\b",
        r"\bneutral\b"
    ]
))


# INDIVIDUAL
LIBRARY.add_metaphor(ReifiedMetaphor(
    name="individual",
    reified_as="fundamental unit of existence",
    functional_form="scale-dependent observation frame",
    value_range=[
        "sub_cellular_processes",
        "organism_level",
        "relational_network",
        "collective_system",
        "ecological_whole"
    ],
    dependencies=[
        "observation_scale",
        "cultural_framework",
        "measurement_method",
        "temporal_scope"
    ],
    institutional_function="obscures relational dependencies, enables atomization and isolation",
    patterns=[
        r"\bindividual\b",
        r"\bpersonal\b",
        r"\bautonomous\b",
        r"\bindependent\b"
    ]
))


# OWNERSHIP
LIBRARY.add_metaphor(ReifiedMetaphor(
    name="ownership",
    reified_as="exclusive individual control",
    functional_form="relationship-to-resource pattern",
    value_range=[
        "commons_stewardship",
        "shared_access",
        "temporary_use",
        "conditional_control",
        "exclusive_possession"
    ],
    dependencies=[
        "cultural_framework",
        "resource_type",
        "community_norms",
        "scarcity_level"
    ],
    institutional_function="naturalizes private property, enables accumulation and exclusion",
    patterns=[
        r"\bownership\b",
        r"\bown\b",
        r"\bproperty\b",
        r"\bpossession\b"
    ]
))
