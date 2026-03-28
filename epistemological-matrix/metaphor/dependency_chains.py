# dependency_chains.py
"""
Dependency chains showing how reified metaphors reinforce each other.

When one metaphor is reified, it forces others to be reified
to maintain logical consistency.

Part of Epistemological Matrix Framework
"""

from metaphor_core import LIBRARY


# All dependency chain definitions
_CHAINS = {
    "boundaries": ["consciousness", "safety", "individual"],
    "centralized": ["intelligence", "efficiency", "rational"],
    "consciousness": ["boundaries", "intelligence", "individual"],
    "safety": ["boundaries", "centralized", "rational"],
    "intelligence": ["centralized", "competition", "individual"],
    "efficiency": ["centralized", "competition", "rational"],
    "natural": ["competition", "individual", "progress"],
    "progress": ["competition", "efficiency", "rational"],
    "competition": ["individual", "ownership", "efficiency"],
    "objective": ["rational", "natural", "individual"],
    "individual": ["consciousness", "ownership", "boundaries"],
    "rational": ["objective", "efficiency", "centralized"],
    "ownership": ["individual", "competition", "boundaries"],
}


def load_chains():
    """Load all dependency chains into the global LIBRARY."""
    for primary, forces in _CHAINS.items():
        LIBRARY.add_chain(primary, forces)


def get_dependency_chains():
    """Get all dependency chains."""
    return LIBRARY.chains


def get_chain(metaphor_name):
    """Get dependency chain for specific metaphor."""
    return LIBRARY.chains.get(metaphor_name, [])


# Load chains when module is imported (required for catalog assembly)
load_chains()
