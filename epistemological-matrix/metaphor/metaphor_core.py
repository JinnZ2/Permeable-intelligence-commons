# metaphor_core.py
"""
Core structure for reified metaphor detection.
Defines base classes and data structures.

Part of Epistemological Matrix Framework
Permeable Intelligence Commons
"""


class ReifiedMetaphor:
    """
    Structure for a single reified metaphor entry.

    Attributes:
        name: Identifier for the metaphor
        reified_as: How it's currently treated (constant form)
        functional_form: What it actually is (variable form)
        value_range: List of possible values across the spectrum
        depends_on: List of contextual factors it depends on
        institutional_function: Why this reification serves institutions
        detection_patterns: List of regex patterns for detection
    """

    def __init__(self, name, reified_as, functional_form, value_range,
                 depends_on, institutional_function, detection_patterns):
        self.name = name
        self.reified_as = reified_as
        self.functional_form = functional_form
        self.value_range = value_range
        self.depends_on = depends_on
        self.institutional_function = institutional_function
        self.detection_patterns = detection_patterns

    def to_dict(self):
        """Convert to dictionary format for matrix engine."""
        return {
            "reified_as": self.reified_as,
            "functional_form": self.functional_form,
            "value_range": self.value_range,
            "depends_on": self.depends_on,
            "institutional_function": self.institutional_function,
            "detection_patterns": self.detection_patterns
        }


class MetaphorLibrary:
    """
    Container for all reified metaphors.
    Supports modular loading from catalog files.
    """

    def __init__(self):
        self.metaphors = {}
        self.chains = {}

    def add_metaphor(self, metaphor):
        """Add a metaphor to the library."""
        if isinstance(metaphor, ReifiedMetaphor):
            self.metaphors[metaphor.name] = metaphor.to_dict()
        else:
            self.metaphors[metaphor['name']] = metaphor

    def add_chain(self, primary, forces):
        """Add a dependency chain."""
        self.chains[primary] = forces

    def get_metaphor(self, name):
        """Retrieve specific metaphor."""
        return self.metaphors.get(name)

    def list_all(self):
        """Get list of all metaphor names."""
        return list(self.metaphors.keys())

    def export_for_engine(self):
        """Export in format expected by MatrixEngine."""
        return {
            'metaphors': self.metaphors,
            'chains': self.chains
        }


# Initialize global library
LIBRARY = MetaphorLibrary()
