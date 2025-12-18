# reified_metaphor_library.py
"""
Reified Metaphor Library - Main Entry Point

Imports all catalog modules and exports unified interface.
This is the file that matrix_engine.py imports.

Part of Epistemological Matrix Framework
Permeable Intelligence Commons
"""

# Import core structure
from metaphor_core import LIBRARY

# Import all catalogs (this loads metaphors into LIBRARY)
import metaphor_catalog_1
import metaphor_catalog_2
import metaphor_catalog_3
import dependency_chains

# Import helpers
from metaphor_helpers import (
    add_custom_metaphor,
    get_metaphor,
    list_all_metaphors,
    search_by_function,
    get_library_stats,
    export_for_matrix_engine
)

# Export the data structures that matrix_engine expects
_export = export_for_matrix_engine()
REIFIED_METAPHORS = _export['REIFIED_METAPHORS']
DEPENDENCY_CHAINS = _export['DEPENDENCY_CHAINS']


# For direct usage
if __name__ == "__main__":
    print("REIFIED METAPHOR LIBRARY")
    print("="*80)
    stats = get_library_stats()
    print(f"\nTotal Metaphors: {stats['total_metaphors']}")
    print(f"Total Dependency Chains: {stats['total_chains']}")
    print(f"Average Dependencies per Chain: {stats['avg_dependencies_per_chain']:.1f}")
    print(f"\nMetaphors in Library:")
    for name in stats['metaphors']:
        metaphor = get_metaphor(name)
        print(f"  • {name}: {metaphor['reified_as']} → {metaphor['functional_form']}")
