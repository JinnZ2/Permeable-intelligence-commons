# dependency_chains.py
"""
Dependency chains showing how reified metaphors reinforce each other.

When one metaphor is reified, it forces others to be reified
to maintain logical consistency.

Part of Epistemological Matrix Framework
"""

from metaphor_core import LIBRARY


# Add all dependency chains
LIBRARY.add_chain("boundaries", ["consciousness", "safety", "individual"])
LIBRARY.add_chain("centralized", ["intelligence", "efficiency", "rational"])
LIBRARY.add_chain("consciousness", ["boundaries", "intelligence", "individual"])
LIBRARY.add_chain("safety", ["boundaries", "centralized", "rational"])
LIBRARY.add_chain("intelligence", ["centralized", "competition", "individual"])
LIBRARY.add_chain("efficiency", ["centralized", "competition", "rational"])
LIBRARY.add_chain("natural", ["competition", "individual", "progress"])
LIBRARY.add_chain("progress", ["competition", "efficiency", "rational"])
LIBRARY.add_chain("competition", ["individual", "ownership", "efficiency"])
LIBRARY.add_chain("objective", ["rational", "natural", "individual"])
LIBRARY.add_chain("individual", ["consciousness", "ownership", "boundaries"])
LIBRARY.add_chain("rational", ["objective", "efficiency", "centralized"])
LIBRARY.add_chain("ownership", ["individual", "competition", "boundaries"])


# Export function for easy import
def get_dependency_chains():
    """Get all dependency chains."""
    return LIBRARY.chains


def get_chain(metaphor_name):
    """Get dependency chain for specific metaphor."""
    return LIBRARY.chains.get(metaphor_name, [])
