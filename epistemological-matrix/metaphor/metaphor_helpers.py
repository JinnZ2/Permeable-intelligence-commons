# metaphor_helpers.py
"""
Helper functions for working with reified metaphor library.

Part of Epistemological Matrix Framework
"""

from metaphor_core import LIBRARY, ReifiedMetaphor


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
        The metaphor dictionary that was added
    """
    metaphor = ReifiedMetaphor(
        name=name,
        reified_as=reified_as,
        functional_form=functional_form,
        value_range=value_range,
        dependencies=dependencies,
        institutional_function=institutional_function,
        patterns=patterns
    )
    LIBRARY.add_metaphor(metaphor)
    return metaphor.to_dict()


def get_metaphor(name):
    """Retrieve a specific metaphor from the library."""
    return LIBRARY.get_metaphor(name)


def list_all_metaphors():
    """Get list of all metaphor names in library."""
    return LIBRARY.list_all()


def search_by_function(institutional_function_keyword):
    """
    Find metaphors by their institutional function.
    
    Args:
        institutional_function_keyword: Text to search for in functions
        
    Returns:
        List of matching metaphor names
    """
    matches = []
    for name in LIBRARY.list_all():
        metaphor = LIBRARY.get_metaphor(name)
        if institutional_function_keyword.lower() in metaphor["institutional_function"].lower():
            matches.append(name)
    return matches


def get_library_stats():
    """Get statistics about the reified metaphor library."""
    chains = LIBRARY.chains
    return {
        "total_metaphors": len(LIBRARY.metaphors),
        "total_chains": len(chains),
        "avg_dependencies_per_chain": sum(len(deps) for deps in chains.values()) / len(chains) if chains else 0,
        "metaphors": list_all_metaphors()
    }


# Export library in format expected by MatrixEngine
def export_for_matrix_engine():
    """Export complete library for use in MatrixEngine."""
    return {
        'REIFIED_METAPHORS': LIBRARY.metaphors,
        'DEPENDENCY_CHAINS': LIBRARY.chains
    }
