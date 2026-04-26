# yaml_loader.py
"""
YAML-based metaphor catalog loader.

Reads metaphors.yaml and dependency_chains.yaml and produces the same
dict structures (REIFIED_METAPHORS, DEPENDENCY_CHAINS) that MatrixEngine expects.

Part of the Permeable Intelligence Commons

Ontology frame: every metaphor entry loaded here is a dX/dt under bounds —
its detection patterns and confidence weights are valid only within the
context fields it declares. See DIFFERENTIAL_FRAME.md at the repository root
for the full AI-reader contract.
"""

import os
import re
import yaml

# Canonical keys every metaphor must have (basic set)
_CANONICAL_KEYS = {
    "reified_as", "functional_form", "value_range", "depends_on",
    "institutional_function", "detection_patterns"
}

# Extended keys including context-aware detection fields
_EXTENDED_KEYS = _CANONICAL_KEYS | {"reified_contexts", "functional_contexts"}

# Default paths relative to this module
_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
_DEFAULT_METAPHORS_PATH = os.path.join(_DATA_DIR, "metaphors.yaml")
_DEFAULT_CHAINS_PATH = os.path.join(_DATA_DIR, "dependency_chains.yaml")


def load_metaphor_catalog(yaml_path=None, include_contexts=False):
    """
    Load metaphor definitions from YAML file.

    Args:
        yaml_path: Path to metaphors.yaml. Defaults to data/metaphors.yaml
                   relative to this module.
        include_contexts: If True, include reified_contexts and functional_contexts
                         in the returned dicts. If False, return only the 6 canonical keys.

    Returns:
        Dict mapping metaphor names to their property dicts.
    """
    path = yaml_path or _DEFAULT_METAPHORS_PATH

    with open(path, 'r') as f:
        data = yaml.safe_load(f)

    metaphors = {}
    for name, props in data["metaphors"].items():
        if include_contexts:
            metaphors[name] = {k: props[k] for k in _EXTENDED_KEYS if k in props}
        else:
            metaphors[name] = {k: props[k] for k in _CANONICAL_KEYS if k in props}

    return metaphors


def load_dependency_chains(yaml_path=None):
    """
    Load dependency chains from YAML file.

    Args:
        yaml_path: Path to dependency_chains.yaml. Defaults to data/dependency_chains.yaml.

    Returns:
        Dict mapping primary metaphor name to list of forced metaphor names.
    """
    path = yaml_path or _DEFAULT_CHAINS_PATH

    with open(path, 'r') as f:
        data = yaml.safe_load(f)

    return dict(data["chains"])


def validate_catalog(metaphors, chains):
    """
    Validate that the catalog is internally consistent.

    Checks:
    - All metaphors have the 6 canonical keys
    - All detection_patterns are valid regex
    - All chain references point to defined metaphors
    - All reified_contexts/functional_contexts are valid regex (if present)

    Args:
        metaphors: Dict from load_metaphor_catalog()
        chains: Dict from load_dependency_chains()

    Returns:
        List of validation error strings (empty = valid).
    """
    errors = []

    for name, props in metaphors.items():
        # Check canonical keys
        missing = _CANONICAL_KEYS - set(props.keys())
        if missing:
            errors.append(f"Metaphor '{name}' missing keys: {missing}")

        # Validate regex patterns
        for field in ("detection_patterns", "reified_contexts", "functional_contexts"):
            for pattern in props.get(field, []):
                try:
                    re.compile(pattern)
                except re.error as e:
                    errors.append(f"Metaphor '{name}' has invalid regex in {field}: '{pattern}' ({e})")

    # Validate chain references
    for primary, forced_list in chains.items():
        if primary not in metaphors:
            errors.append(f"Chain primary '{primary}' not found in metaphors")
        for dep in forced_list:
            if dep not in metaphors:
                errors.append(f"Chain dependency '{dep}' (from '{primary}') not found in metaphors")

    return errors
