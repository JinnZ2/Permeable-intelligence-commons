# reified_metaphor_library.py
"""
Reified Metaphor Library - Loaded from YAML catalog

Part of the Permeable Intelligence Commons
Used by MatrixEngine for detecting conceptual noise

Exports:
- REIFIED_METAPHORS: Dictionary of metaphors with detection patterns
- DEPENDENCY_CHAINS: How reified metaphors force each other
- Helper functions for extending the library at runtime
"""

from yaml_loader import load_metaphor_catalog, load_dependency_chains

# Load canonical catalog from YAML data files
REIFIED_METAPHORS = load_metaphor_catalog(include_contexts=False)
DEPENDENCY_CHAINS = load_dependency_chains()


# =============================================================================
# HELPER FUNCTIONS (runtime additions, not persisted to YAML)
# =============================================================================

def add_custom_metaphor(name, reified_as, functional_form, value_range,
                        depends_on, institutional_function, detection_patterns):
    """
    Add a custom reified metaphor to the library at runtime.

    Note: This modifies the in-memory catalog only. To persist changes,
    edit data/metaphors.yaml directly.

    Args:
        name: Identifier for the metaphor
        reified_as: How it's currently treated (constant form)
        functional_form: What it actually is (variable form)
        value_range: List of possible values
        depends_on: List of what it depends on
        institutional_function: Why this reification serves institutions
        detection_patterns: List of regex patterns for detection

    Returns:
        Updated metaphor dictionary
    """
    REIFIED_METAPHORS[name] = {
        "reified_as": reified_as,
        "functional_form": functional_form,
        "value_range": value_range,
        "depends_on": depends_on,
        "institutional_function": institutional_function,
        "detection_patterns": detection_patterns
    }
    return REIFIED_METAPHORS[name]


def add_dependency_chain(primary, forced_dependencies):
    """
    Add a dependency chain to the library at runtime.

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


def get_library_stats():
    """
    Get statistics about the reified metaphor library.

    Returns:
        Dictionary with library statistics
    """
    return {
        "total_metaphors": len(REIFIED_METAPHORS),
        "total_chains": len(DEPENDENCY_CHAINS),
        "avg_dependencies_per_metaphor": sum(
            len(deps) for deps in DEPENDENCY_CHAINS.values()
        ) / len(DEPENDENCY_CHAINS) if DEPENDENCY_CHAINS else 0,
        "metaphors": list_all_metaphors()
    }


if __name__ == "__main__":
    print("REIFIED METAPHOR LIBRARY")
    print("=" * 80)
    stats = get_library_stats()
    print(f"\nTotal Metaphors: {stats['total_metaphors']}")
    print(f"Total Dependency Chains: {stats['total_chains']}")
    print(f"Average Dependencies per Chain: {stats['avg_dependencies_per_metaphor']:.1f}")
    print(f"\nMetaphors in Library:")
    for name in stats['metaphors']:
        metaphor = get_metaphor(name)
        print(f"  * {name}: {metaphor['reified_as']} -> {metaphor['functional_form']}")
