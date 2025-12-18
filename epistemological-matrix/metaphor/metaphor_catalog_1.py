# metaphor_catalog_1.py
"""
Reified Metaphor Catalog - Part 1
Core institutional metaphors: boundaries, intelligence, centralized, hierarchy

Part of Epistemological Matrix Framework
"""

from metaphor_core import LIBRARY, ReifiedMetaphor


# BOUNDARIES
LIBRARY.add_metaphor(ReifiedMetaphor(
    name="boundaries",
    reified_as="fixed separation",
    functional_form="permeability spectrum",
    value_range=[
        "fully_open",
        "contextually_permeable",
        "selectively_filtered",
        "temporarily_closed",
        "rigid_separation"
    ],
    dependencies=[
        "context",
        "relationship_type",
        "cultural_framework",
        "purpose",
        "trust_level"
    ],
    institutional_function="justifies rigid separation as natural/necessary, enables control through isolation",
    patterns=[
        r"\bboundaries\b",
        r"\bmaintain boundaries\b",
        r"\bprotective barriers\b",
        r"\bclear boundaries\b"
    ]
))


# INTELLIGENCE
LIBRARY.add_metaphor(ReifiedMetaphor(
    name="intelligence",
    reified_as="unitary measurable quantity",
    functional_form="architecture-problem fitness matrix",
    value_range=[
        "pattern_recognition",
        "adaptation_speed",
        "context_integration",
        "distributed_coordination",
        "specialized_optimization"
    ],
    dependencies=[
        "problem_structure",
        "information_availability",
        "architectural_type",
        "measurement_method",
        "cultural_framework"
    ],
    institutional_function="enables ranking/hierarchy claims, justifies concentration of power/resources",
    patterns=[
        r"\bintelligence\b",
        r"\bmore intelligent\b",
        r"\bAGI\b",
        r"\bgeneral intelligence\b",
        r"\bIQ\b"
    ]
))


# CENTRALIZED
LIBRARY.add_metaphor(ReifiedMetaphor(
    name="centralized",
    reified_as="inherently efficient/fast",
    functional_form="coordination pattern variable",
    value_range=[
        "distributed_peer",
        "temporary_coordination",
        "functional_specialization",
        "hierarchical_delegation",
        "rigid_command_chain"
    ],
    dependencies=[
        "information_distribution",
        "problem_complexity",
        "failure_tolerance",
        "scale",
        "coordination_cost"
    ],
    institutional_function="naturalizes hierarchical control, justifies concentration of decision-making power",
    patterns=[
        r"\bcentralized\b",
        r"\bhierarchy\b",
        r"\bchain of command\b",
        r"\btop-down\b"
    ]
))
