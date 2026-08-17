# legacy/metaphor/__init__.py
"""
Modular reified metaphor library. SUPERSEDED — kept as record, not as API.

Falsified and replaced by epistemological-matrix/data/metaphors.yaml and
data/dependency_chains.yaml (loaded by yaml_loader.py) in commit d86a861.
See ../README.md and ledger entry E-001 in ../../METHOD.md for why.

This package does not import: its submodules use flat imports
(`from metaphor_core import LIBRARY`) that only resolve when this directory is
itself on sys.path. That failure is part of what falsified E-001 and is
preserved deliberately. Do not repair it — read it.

Ontology frame: every metaphor here is a dX/dt under bounds whose scope was
exited, not zeroed. See ../../DIFFERENTIAL_FRAME.md for the AI-reader contract.
"""

import warnings
warnings.warn(
    "legacy.metaphor is superseded and kept only as a record. "
    "Metaphor definitions live in epistemological-matrix/data/metaphors.yaml; "
    "import from epistemological-matrix/reified_metaphor_library instead. "
    "See METHOD.md entry E-001.",
    DeprecationWarning,
    stacklevel=2,
)
