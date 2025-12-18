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
    """
    def __init__(self, name, reified_as, functional_form, value_range, 
                 dependencies, institutional_function, patterns):
        self.name = name
        self.reified_as = reified_as
        self.functional_form = functional_form
        self.range = value_range
        self.depends_on = dependencies
        self.institutional_function = institutional_function
        self.detection_patterns = patterns
    
    def to_dict(self):
        """Convert to dictionary format for matrix engine."""
        return {
            "reified_as": self.reified_as,
            "functional_form": self.functional_form,
            "range": self.range,
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
