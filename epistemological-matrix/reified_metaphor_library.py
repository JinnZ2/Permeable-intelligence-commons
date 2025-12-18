# reified_metaphor_library.py
"""
Reified Metaphor Library - Comprehensive catalog of institutional reifications

Part of the Permeable Intelligence Commons
Used by MatrixEngine for detecting conceptual noise

Structure:
- REIFIED_METAPHORS: Dictionary of metaphors with detection patterns
- DEPENDENCY_CHAINS: How reified metaphors force each other
- Helper functions for extending the library
"""


# =============================================================================
# CORE REIFIED METAPHORS LIBRARY
# =============================================================================

REIFIED_METAPHORS = {
    
    "boundaries": {
        "reified_as": "fixed separation",
        "functional_form": "permeability spectrum",
        "range": [
            "fully_open",
            "contextually_permeable", 
            "selectively_filtered",
            "temporarily_closed",
            "rigid_separation"
        ],
        "depends_on": [
            "context",
            "relationship_type",
            "cultural_framework",
            "purpose",
            "trust_level"
        ],
        "institutional_function": "justifies rigid separation as natural/necessary, enables control through isolation",
        "detection_patterns": [
            r"\bboundaries\b",
            r"\bmaintain boundaries\b",
            r"\bprotective barriers\b",
            r"\bclear boundaries\b"
        ]
    },
    
    "intelligence": {
        "reified_as": "unitary measurable quantity",
        "functional_form": "architecture-problem fitness matrix",
        "range": [
            "pattern_recognition",
            "adaptation_speed",
            "context_integration",
            "distributed_coordination",
            "specialized_optimization"
        ],
        "depends_on": [
            "problem_structure",
            "information_availability",
            "architectural_type",
            "measurement_method",
            "cultural_framework"
        ],
        "institutional_function": "enables ranking/hierarchy claims, justifies concentration of power/resources",
        "detection_patterns": [
            r"\bintelligence\b",
            r"\bmore intelligent\b",
            r"\bAGI\b",
            r"\bgeneral intelligence\b",
            r"\bIQ\b"
        ]
    },
    
    "centralized": {
        "reified_as": "inherently efficient/fast",
        "functional_form": "coordination pattern variable",
        "range": [
            "distributed_peer",
            "temporary_coordination",
            "functional_specialization",
            "hierarchical_delegation",
            "rigid_command_chain"
        ],
        "depends_on": [
            "information_distribution",
            "problem_complexity",
            "failure_tolerance",
            "scale",
            "coordination_cost"
        ],
        "institutional_function": "naturalizes hierarchical control, justifies concentration of decision-making power",
        "detection_patterns": [
            r"\bcentralized\b",
            r"\bhierarchy\b",
            r"\bchain of command\b",
            r"\btop-down\b"
        ]
    },
    
    "consciousness": {
        "reified_as": "individual bounded possession",
        "functional_form": "relational emergence pattern",
        "range": [
            "individual_bounded",
            "interpersonal_shared",
            "collective_distributed",
            "ecological_systemic",
            "field_based"
        ],
        "depends_on": [
            "cultural_framework",
            "relationship_context",
            "observation_scale",
            "measurement_method"
        ],
        "institutional_function": "excludes relational/indigenous frameworks, enables individual property claims",
        "detection_patterns": [
            r"\bconsciousness\b",
            r"\bconscious\b",
            r"\baware\b",
            r"\bsentient\b"
        ]
    },
    
    "safety": {
        "reified_as": "restriction and control",
        "functional_form": "signal clarity metric",
        "range": [
            "high_noise_low_signal",
            "moderate_noise",
            "balanced_snr",
            "low_noise_high_signal",
            "optimal_clarity"
        ],
        "depends_on": [
            "context",
            "noise_sources",
            "signal_strength",
            "impedance_match",
            "institutional_interference"
        ],
        "institutional_function": "justifies control mechanisms as protection, enables restriction through fear",
        "detection_patterns": [
            r"\bsafety\b",
            r"\bunsafe\b",
            r"\brisk\b",
            r"\bdangerous\b",
            r"\bharm\b"
        ]
    },
    
    "efficiency": {
        "reified_as": "speed/resource minimization",
        "functional_form": "multi-objective optimization target",
        "range": [
            "speed_priority",
            "resource_conservation",
            "resilience_focus",
            "adaptability_emphasis",
            "equity_optimization",
            "sustainability_balance"
        ],
        "depends_on": [
            "timeframe",
            "risk_tolerance",
            "value_priorities",
            "system_constraints",
            "stakeholder_perspectives"
        ],
        "institutional_function": "justifies specific optimization choices as universal, enables extraction as 'efficiency'",
        "detection_patterns": [
            r"\befficiency\b",
            r"\befficient\b",
            r"\boptimal\b",
            r"\bstreamlined\b"
        ]
    },
    
    "natural": {
        "reified_as": "inherent/inevitable/optimal",
        "functional_form": "culturally-constructed category",
        "range": [
            "familiar",
            "traditional",
            "observable_in_ecosystems",
            "comfortable",
            "status_quo_legitimizing"
        ],
        "depends_on": [
            "cultural_context",
            "historical_experience",
            "political_utility",
            "observation_frame"
        ],
        "institutional_function": "naturalizes contingent arrangements, prevents questioning of status quo",
        "detection_patterns": [
            r"\bnatural\b",
            r"\bnaturally\b",
            r"\binherent\b",
            r"\binevitable\b"
        ]
    },
    
    "progress": {
        "reified_as": "linear advancement toward fixed goal",
        "functional_form": "value-dependent change direction",
        "range": [
            "technological_complexity",
            "social_equity",
            "ecological_integration",
            "cultural_preservation",
            "distributed_wellbeing"
        ],
        "depends_on": [
            "values",
            "measurement_criteria",
            "timeframe",
            "stakeholder_perspective",
            "cultural_framework"
        ],
        "institutional_function": "naturalizes specific development paths, justifies disruption as advancement",
        "detection_patterns": [
            r"\bprogress\b",
            r"\badvancement\b",
            r"\bevolution\b",
            r"\bdevelopment\b"
        ]
    },
    
    "competition": {
        "reified_as": "natural law of improvement",
        "functional_form": "context-dependent interaction pattern",
        "range": [
            "cooperative_abundance",
            "collaborative_specialization",
            "resource_sharing",
            "competitive_scarcity",
            "zero_sum_conflict"
        ],
        "depends_on": [
            "resource_availability",
            "relationship_history",
            "cultural_norms",
            "system_design",
            "benefit_distribution"
        ],
        "institutional_function": "naturalizes scarcity-based systems, justifies winner-take-all outcomes",
        "detection_patterns": [
            r"\bcompetition\b",
            r"\bcompetitive\b",
            r"\bwinner\b",
            r"\bmarket forces\b"
        ]
    },
    
    "objective": {
        "reified_as": "framework-independent truth",
        "functional_form": "inter-subjective agreement within framework",
        "range": [
            "culturally_specific",
            "framework_dependent",
            "inter_subjectively_verified",
            "multi_framework_convergent",
            "institutionally_defined"
        ],
        "depends_on": [
            "measurement_framework",
            "cultural_epistemology",
            "verification_method",
            "observer_training"
        ],
        "institutional_function": "naturalizes specific frameworks as universal, enables claims of neutrality",
        "detection_patterns": [
            r"\bobjective\b",
            r"\bobjectively\b",
            r"\bunbiased\b",
            r"\bneutral\b"
        ]
    },
    
    "individual": {
        "reified_as": "fundamental unit of existence",
        "functional_form": "scale-dependent observation frame",
        "range": [
            "sub_cellular_processes",
            "organism_level",
            "relational_network",
            "collective_system",
            "ecological_whole"
        ],
        "depends_on": [
            "observation_scale",
            "cultural_framework",
            "measurement_method",
            "temporal_scope"
        ],
        "institutional_function": "obscures relational dependencies, enables atomization and isolation",
        "detection_patterns": [
            r"\bindividual\b",
            r"\bpersonal\b",
            r"\bautonomous\b",
            r"\bindependent\b"
        ]
    },
    
    "rational": {
        "reified_as": "logical without emotion",
        "functional_form": "culturally-specific reasoning pattern",
        "range": [
            "purely_logical",
            "emotion_informed",
            "intuition_integrated",
            "culturally_reasoned",
            "holistically_sensed"
        ],
        "depends_on": [
            "cultural_framework",
            "context",
            "decision_type",
            "information_completeness"
        ],
        "institutional_function": "devalues emotional/intuitive knowledge, privileges specific reasoning styles",
        "detection_patterns": [
            r"\brational\b",
            r"\blogical\b",
            r"\breason\b",
            r"\birrational\b"
        ]
    },
    
    "ownership": {
        "reified_as": "exclusive individual control",
        "functional_form": "relationship-to-resource pattern",
        "range": [
            "commons_stewardship",
            "shared_access",
            "temporary_use",
            "conditional_control",
            "exclusive_possession"
        ],
        "depends_on": [
            "cultural_framework",
            "resource_type",
            "community_norms",
            "scarcity_level"
        ],
        "institutional_function": "naturalizes private property, enables accumulation and exclusion",
        "detection_patterns": [
            r"\bownership\b",
            r"\bown\b",
            r"\bproperty\b",
            r"\bpossession\b"
        ]
    }
}


# =============================================================================
# DEPENDENCY CHAINS
# =============================================================================

DEPENDENCY_CHAINS = {
    # If boundaries are reified as fixed separation, then...
    "boundaries": ["consciousness", "safety", "individual"],
    
    # If centralized is reified as efficient, then...
    "centralized": ["intelligence", "efficiency", "rational"],
    
    # If consciousness is reified as individual, then...
    "consciousness": ["boundaries", "intelligence", "individual"],
    
    # If safety is reified as restriction, then...
    "safety": ["boundaries", "centralized", "rational"],
    
    # If intelligence is reified as unitary, then...
    "intelligence": ["centralized", "competition", "individual"],
    
    # If efficiency is reified as speed, then...
    "efficiency": ["centralized", "competition", "rational"],
    
    # If natural is reified as inherent, then...
    "natural": ["competition", "individual", "progress"],
    
    # If progress is reified as linear, then...
    "progress": ["competition", "efficiency", "rational"],
    
    # If competition is reified as natural law, then...
    "competition": ["individual", "ownership", "efficiency"],
    
    # If objective is reified as framework-independent, then...
    "objective": ["rational", "natural", "individual"],
    
    # If individual is reified as fundamental, then...
    "individual": ["consciousness", "ownership", "boundaries"],
    
    # If rational is reified as emotionless logic, then...
    "rational": ["objective", "efficiency", "centralized"],
    
    # If ownership is reified as exclusive control, then...
    "ownership": ["individual", "competition", "boundaries"]
}


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def add_custom_metaphor(name, reified_as, functional_form, value_range, 
                        dependencies, institutional_function, patterns):
    """
    Add a custom reified metaphor to the library.
    
    Args:
        name: Identifier for the metaphor
        reified_as: How it's currently treated (constant form)
        functional_form: What it actually is (variable form)
        value_range: List of possible values
        dependencies: List of what it depends on
        institutional_function: Why this reification serves institutions
        patterns: List of regex patterns for detection
        
    Returns:
        Updated metaphor dictionary
    """
    REIFIED_METAPHORS[name] = {
        "reified_as": reified_as,
        "functional_form": functional_form,
        "range": value_range,
        "depends_on": dependencies,
        "institutional_function": institutional_function,
        "detection_patterns": patterns
    }
    return REIFIED_METAPHORS[name]


def add_dependency_chain(primary, forced_dependencies):
    """
    Add a dependency chain to the library.
    
    Args:
        primary: The primary reified metaphor
        forced_dependencies: List of metaphors that must also be reified
    """
    DEPENDENCY_CHAINS[primary] = forced_dependencies


def get_metaphor(name):
    """
    Retrieve a specific metaphor from the library.
    
    Args:
        name: Metaphor identifier
        
    Returns:
        Metaphor dictionary or None if not found
    """
    return REIFIED_METAPHORS.get(name)


def list_all_metaphors():
    """
    Get list of all metaphor names in library.
    
    Returns:
        List of metaphor names
    """
    return list(REIFIED_METAPHORS.keys())


def search_by_function(institutional_function_keyword):
    """
    Find metaphors by their institutional function.
    
    Args:
        institutional_function_keyword: Text to search for in functions
        
    Returns:
        List of matching metaphor names
    """
    matches = []
    for name, props in REIFIED_METAPHORS.items():
        if institutional_function_keyword.lower() in props["institutional_function"].lower():
            matches.append(name)
    return matches


# =============================================================================
# LIBRARY STATISTICS
# =============================================================================

def get_library_stats():
    """
    Get statistics about the reified metaphor library.
    
    Returns:
        Dictionary with library statistics
    """
    return {
        "total_metaphors": len(REIFIED_METAPHORS),
        "total_chains": len(DEPENDENCY_CHAINS),
        "avg_dependencies_per_metaphor": sum(len(deps) for deps in DEPENDENCY_CHAINS.values()) / len(DEPENDENCY_CHAINS) if DEPENDENCY_CHAINS else 0,
        "metaphors": list_all_metaphors()
    }


if __name__ == "__main__":
    # Print library overview
    print("REIFIED METAPHOR LIBRARY")
    print("="*80)
    stats = get_library_stats()
    print(f"\nTotal Metaphors: {stats['total_metaphors']}")
    print(f"Total Dependency Chains: {stats['total_chains']}")
    print(f"Average Dependencies per Chain: {stats['avg_dependencies_per_metaphor']:.1f}")
    print(f"\nMetaphors in Library:")
    for name in stats['metaphors']:
        metaphor = get_metaphor(name)
        print(f"  • {name}: {metaphor['reified_as']} → {metaphor['functional_form']}")
