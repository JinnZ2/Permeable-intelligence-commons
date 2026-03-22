# epistemological-matrix/metaphor/__init__.py
"""
Modular reified metaphor library.

DEPRECATED: Metaphor definitions have moved to YAML data files in ../data/.
This package is kept for backward compatibility and will be removed in a
future version. Use yaml_loader.py or import from reified_metaphor_library
instead.
"""

import warnings
warnings.warn(
    "The metaphor/ package is deprecated. "
    "Metaphor definitions are now in data/metaphors.yaml. "
    "Import from reified_metaphor_library instead.",
    DeprecationWarning,
    stacklevel=2,
)
