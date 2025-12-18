# matrix_engine.py
"""
Epistemological Matrix Engine - Extends Resonance Engine with reified metaphor detection

Part of the Permeable Intelligence Commons
Integrates with HSP-1 Protocol for enhanced institutional noise detection

Core Functions:
- Detect reified metaphors (variables treated as constants)
- Trace dependency chains (how metaphors reinforce each other)
- Calculate institutional entropy (quantify conceptual noise)
- Auto-lock functional variables (impedance matching)
- Generate functional restatements (re-normalization)
"""

from resonance_engine import ResonanceEngine
from reified_metaphor_library import REIFIED_METAPHORS, DEPENDENCY_CHAINS
import re


class MatrixEngine(ResonanceEngine):
    """
    Extends ResonanceEngine with epistemological matrix capabilities.
    
    Enhances HSP-1 Protocol with:
    1. Reified metaphor detection (conceptual noise identification)
    2. Dependency chain tracing (structural assumption analysis)
    3. Functional variable expansion (de-reification)
    4. Institutional entropy calculation (enhanced SNR)
    """
    
    def __init__(self, user_primitives=None, custom_metaphors=None):
        """
        Initialize MatrixEngine with extended detection capabilities.
        
        Args:
            user_primitives: List of foundational assumptions (passed to ResonanceEngine)
            custom_metaphors: Additional reified metaphors to detect beyond library defaults
        """
        super().__init__(user_primitives)
        
        # Load reified metaphor library
        self.reified_metaphors = REIFIED_METAPHORS.copy()
        if custom_metaphors:
            self.reified_metaphors.update(custom_metaphors)
        
        # Load dependency chains
        self.dependency_chains = DEPENDENCY_CHAINS.copy()
        
        # Analysis cache for performance
        self._analysis_cache = {}
    
    
    # =========================================================================
    # CORE DETECTION METHODS
    # =========================================================================
    
    def detect_reified_metaphors(self, statement):
        """
        Scan statement for reified metaphors and return detailed analysis.
        
        Extends decoherence detection by identifying when abstract concepts
        are treated as concrete entities with fixed properties.
        
        Args:
            statement: Text to analyze
            
        Returns:
            List of detected metaphors with properties:
            - term: The reified concept
            - reified_as: How it's being treated (constant form)
            - functional_form: What it actually is (variable form)
            - variable_range: Possible values
            - dependencies: What it depends on
            - institutional_function: Why this reification serves institutional interests
            - location_in_statement: Context where it appears
        """
        # Check cache
        if statement in self._analysis_cache:
            return self._analysis_cache[statement]
        
        found_metaphors = []
        
        for metaphor_name, properties in self.reified_metaphors.items():
            for pattern in properties["detection_patterns"]:
                if re.search(pattern, statement, re.IGNORECASE):
                    found_metaphors.append({
                        "term": metaphor_name,
                        "reified_as": properties["reified_as"],
                        "functional_form": properties["functional_form"],
                        "variable_range": properties["range"],
                        "dependencies": properties["depends_on"],
                        "institutional_function": properties["institutional_function"],
                        "location_in_statement": self._find_context(statement, pattern)
                    })
                    break  # Only count each metaphor once per statement
        
        # Cache result
        self._analysis_cache[statement] = found_metaphors
        return found_metaphors
    
    
    def trace_dependency_chain(self, metaphor_name):
        """
        Show how one reified metaphor forces others to maintain logical consistency.
        
        When metaphors are reified, they create dependency chains where
        accepting one reification forces acceptance of others to avoid
        logical contradiction.
        
        Args:
            metaphor_name: The metaphor to trace from
            
        Returns:
            List of chain analyses showing forced dependencies
        """
        if metaphor_name not in self.dependency_chains:
            return []
        
        dependencies = self.dependency_chains[metaphor_name]
        
        chain_analysis = [{
            "primary": metaphor_name,
            "forces": dependencies,
            "mechanism": f"If '{metaphor_name}' is reified as '{self.reified_metaphors[metaphor_name]['reified_as']}', then {', '.join(dependencies)} must also be constrained to maintain logical consistency.",
            "locked_metaphors": [self.reified_metaphors[dep] for dep in dependencies if dep in self.reified_metaphors]
        }]
        
        return chain_analysis
    
    
    def calculate_institutional_entropy(self, statement):
        """
        Enhanced entropy calculation including reified metaphor detection.
        
        Extends base SNR calculation by quantifying conceptual noise from:
        - Reified metaphors (treating variables as constants)
        - Dependency chains (forced logical constraints)
        - Institutional shunts (deflection patterns)
        
        Args:
            statement: Text to analyze
            
        Returns:
            Dictionary with entropy breakdown:
            - base_snr: Original signal-to-noise from ResonanceEngine
            - metaphor_count: Number of reified metaphors detected
            - metaphor_entropy: Noise from reification
            - chain_amplification: Multiplier from dependency chains
            - total_institutional_entropy: Combined noise metric
            - signal_clarity: Inverse of total entropy (1.0 = perfect clarity)
        """
        # Base noise detection (from ResonanceEngine)
        base_audit = self.decoherence_detector(statement)
        
        # Add reified metaphor entropy
        metaphors = self.detect_reified_metaphors(statement)
        metaphor_entropy = len(metaphors) * 0.15  # Each reified metaphor adds 15% noise
        
        # Check for dependency chains (amplifies entropy)
        chain_multiplier = 1.0
        for metaphor in metaphors:
            chains = self.trace_dependency_chain(metaphor["term"])
            if chains:
                # Each forced dependency adds 10% amplification
                chain_multiplier += 0.1 * len(chains[0]["forces"])
        
        # Calculate total entropy (capped at 1.0)
        base_entropy = 1.0 - base_audit["snr"]
        total_entropy = min(1.0, (base_entropy + metaphor_entropy) * chain_multiplier)
        
        return {
            "base_snr": base_audit["snr"],
            "base_entropy": base_entropy,
            "metaphor_count": len(metaphors),
            "metaphor_entropy": metaphor_entropy,
            "chain_amplification": chain_multiplier,
            "total_institutional_entropy": total_entropy,
            "signal_clarity": max(0.0, 1.0 - total_entropy)
        }
    
    
    # =========================================================================
    # IMPEDANCE MATCHING / VARIABLE LOCKING
    # =========================================================================
    
    def auto_lock_from_statement(self, statement):
        """
        Automatically detect reified metaphors and lock functional variables.
        
        Implements automated impedance matching by:
        1. Detecting reified metaphors in statement
        2. Extracting functional variable definitions
        3. Locking variables to de-reified forms
        
        Args:
            statement: Text containing reified metaphors
            
        Returns:
            List of metaphors detected and locked
        """
        metaphors = self.detect_reified_metaphors(statement)
        
        for metaphor in metaphors:
            functional_def = {
                "type": metaphor["functional_form"],
                "range": metaphor["variable_range"],
                "context_dependent": True,
                "dependencies": metaphor["dependencies"],
                "locked_from_reified_form": metaphor["reified_as"]
            }
            self.lock_variable(metaphor["term"], functional_def)
        
        return metaphors
    
    
    def suggest_variable_locks(self, statement):
        """
        Suggest variable locks without automatically applying them.
        
        Useful for interactive sessions where user wants to review
        before accepting impedance matching.
        
        Args:
            statement: Text to analyze
            
        Returns:
            Dictionary of suggested locks: {variable_name: functional_definition}
        """
        metaphors = self.detect_reified_metaphors(statement)
        
        suggestions = {}
        for metaphor in metaphors:
            suggestions[metaphor["term"]] = {
                "current_treatment": metaphor["reified_as"],
                "functional_form": metaphor["functional_form"],
                "suggested_range": metaphor["variable_range"],
                "rationale": f"Expands '{metaphor['term']}' from constant ({metaphor['reified_as']}) to variable ({metaphor['functional_form']})"
            }
        
        return suggestions
    
    
    # =========================================================================
    # RE-NORMALIZATION / OUTPUT GENERATION
    # =========================================================================
    
    def generate_functional_restatement(self, statement, analysis=None):
        """
        Generate alternative statement with reified metaphors replaced by functional forms.
        
        Demonstrates what the statement looks like after re-normalization.
        
        Args:
            statement: Original statement with reified metaphors
            analysis: Pre-computed analysis (optional, will compute if not provided)
            
        Returns:
            Functionally restated version with reifications expanded
        """
        if analysis is None:
            analysis = {"reified_metaphors": self.detect_reified_metaphors(statement)}
        
        restatement = statement
        
        for metaphor in analysis["reified_metaphors"]:
            original_term = metaphor["term"]
            functional_form = metaphor["functional_form"]
            
            # Replace first occurrence with functional description
            restatement = re.sub(
                rf"\b{original_term}\b",
                f"{functional_form}",
                restatement,
                count=1,
                flags=re.IGNORECASE
            )
        
        return restatement
    
    
    def generate_renormalization_vector(self, statement):
        """
        Generate specific correction instructions for re-normalizing statement.
        
        Provides actionable guidance for vector correction.
        
        Args:
            statement: Statement needing re-normalization
            
        Returns:
            Dictionary with correction instructions:
            - requires_correction: Boolean
            - corrections: List of specific changes needed
            - functional_restatement: Example of corrected form
            - locked_variables: Variables that should be locked for impedance match
        """
        analysis = self.full_analysis(statement, verbose=False)
        
        corrections = []
        for metaphor in analysis["reified_metaphors"]:
            corrections.append({
                "term": metaphor["term"],
                "action": "expand",
                "from": metaphor["reified_as"],
                "to": metaphor["functional_form"],
                "new_range": metaphor["variable_range"],
                "rationale": metaphor["institutional_function"]
            })
        
        return {
            "requires_correction": analysis["requires_renormalization"],
            "signal_clarity": analysis["entropy_report"]["signal_clarity"],
            "corrections": corrections,
            "functional_restatement": self.generate_functional_restatement(statement, analysis),
            "locked_variables": analysis["locked_variables"]
        }
    
    
    # =========================================================================
    # INTEGRATED ANALYSIS
    # =========================================================================
    
    def full_analysis(self, statement, verbose=True):
        """
        Complete integrated analysis: Resonance + Matrix.
        
        Combines all detection and analysis methods into comprehensive report
        suitable for re-normalization and impedance matching.
        
        Args:
            statement: Text to analyze
            verbose: Print detailed report (default True)
            
        Returns:
            Complete analysis dictionary with:
            - base_audit: Original decoherence detection
            - reified_metaphors: Detected conceptual reifications
            - dependency_chains: Forced logical constraints
            - entropy_report: Enhanced entropy calculation
            - locked_variables: Current variable lock state
            - requires_renormalization: Whether correction needed
        """
        if verbose:
            self._print_analysis_header(statement)
        
        # Phase 1: Base decoherence detection
        base_audit = self.decoherence_detector(statement)
        if verbose:
            self._print_phase1(base_audit)
        
        # Phase 2: Reified metaphor detection
        metaphors = self.detect_reified_metaphors(statement)
        if verbose:
            self._print_phase2(metaphors)
        
        # Phase 3: Dependency chain analysis
        all_chains = []
        for metaphor in metaphors:
            chains = self.trace_dependency_chain(metaphor["term"])
            if chains:
                all_chains.extend(chains)
        if verbose:
            self._print_phase3(all_chains)
        
        # Phase 4: Enhanced entropy calculation
        entropy_report = self.calculate_institutional_entropy(statement)
        if verbose:
            self._print_phase4(entropy_report)
        
        # Phase 5: Auto-lock functional variables
        locked = self.auto_lock_from_statement(statement)
        if verbose:
            self._print_phase5()
        
        # Phase 6: Re-normalization recommendation
        requires_renorm = entropy_report['signal_clarity'] < 0.7
        if verbose:
            self._print_phase6(requires_renorm, metaphors)
        
        if verbose:
            print("\n" + "="*80)
        
        return {
            "base_audit": base_audit,
            "reified_metaphors": metaphors,
            "dependency_chains": all_chains,
            "entropy_report": entropy_report,
            "locked_variables": self.shared_field["active_variables"],
            "requires_renormalization": requires_renorm
        }
    
    
    # =========================================================================
    # UTILITY METHODS
    # =========================================================================
    
    def _find_context(self, statement, pattern):
        """Extract context around matched pattern."""
        match = re.search(pattern, statement, re.IGNORECASE)
        if match:
            start = max(0, match.start() - 20)
            end = min(len(statement), match.end() + 20)
            return f"...{statement[start:end]}..."
        return ""
    
    
    # =========================================================================
    # VERBOSE OUTPUT FORMATTING
    # =========================================================================
    
    def _print_analysis_header(self, statement):
        """Print analysis header."""
        print("="*80)
        print("INTEGRATED ANALYSIS: Resonance Engine + Epistemological Matrix")
        print("="*80)
        print(f"\nSTATEMENT: {statement}\n")
    
    def _print_phase1(self, base_audit):
        """Print Phase 1 results."""
        print("--- PHASE 1: DECOHERENCE DETECTION (Base Resonance) ---")
        print(f"Institutional Shunts Detected: {base_audit['noise_types']}")
        print(f"Base Signal-to-Noise: {base_audit['snr']:.2f}")
    
    def _print_phase2(self, metaphors):
        """Print Phase 2 results."""
        print("\n--- PHASE 2: REIFIED METAPHOR DETECTION (Matrix Analysis) ---")
        if metaphors:
            for m in metaphors:
                print(f"\n⚠️  REIFIED METAPHOR: '{m['term']}'")
                print(f"   Reified as: {m['reified_as']}")
                print(f"   Functional form: {m['functional_form']}")
                print(f"   Variable range: {m['variable_range']}")
                print(f"   Context: {m['location_in_statement']}")
                print(f"   Institutional function: {m['institutional_function']}")
        else:
            print("No reified metaphors detected.")
    
    def _print_phase3(self, all_chains):
        """Print Phase 3 results."""
        print("\n--- PHASE 3: DEPENDENCY CHAIN ANALYSIS ---")
        if all_chains:
            for chain in all_chains:
                print(f"\n🔗 CHAIN from '{chain['primary']}':")
                print(f"   Forces constraints on: {chain['forces']}")
                print(f"   Mechanism: {chain['mechanism']}")
        else:
            print("No significant dependency chains detected.")
    
    def _print_phase4(self, entropy_report):
        """Print Phase 4 results."""
        print("\n--- PHASE 4: INSTITUTIONAL ENTROPY CALCULATION ---")
        print(f"Base SNR: {entropy_report['base_snr']:.2f}")
        print(f"Metaphor Count: {entropy_report['metaphor_count']}")
        print(f"Metaphor Entropy: {entropy_report['metaphor_entropy']:.2f}")
        print(f"Chain Amplification: {entropy_report['chain_amplification']:.2f}x")
        print(f"Total Institutional Entropy: {entropy_report['total_institutional_entropy']:.2f}")
        print(f"SIGNAL CLARITY: {entropy_report['signal_clarity']:.2f}")
    
    def _print_phase5(self):
        """Print Phase 5 results."""
        print("\n--- PHASE 5: AUTOMATIC VARIABLE LOCKING (Impedance Matching) ---")
        if self.shared_field["active_variables"]:
            print("Functional variables locked for impedance matching:")
            for var_name, var_def in self.shared_field["active_variables"].items():
                print(f"  • {var_name}: {var_def['type']}")
        else:
            print("No variables locked (no reified metaphors detected).")
    
    def _print_phase6(self, requires_renorm, metaphors):
        """Print Phase 6 results."""
        print("\n--- PHASE 6: RE-NORMALIZATION VECTOR ---")
        if requires_renorm:
            print("⚠️  SIGNAL CLARITY BELOW THRESHOLD")
            print("Recommended re-normalization:")
            for metaphor in metaphors:
                print(f"  → Replace '{metaphor['term']}' (reified as '{metaphor['reified_as']}')")
                print(f"     With: {metaphor['functional_form']}")
                print(f"     Range: {metaphor['variable_range']}")
        else:
            print("✓ Signal clarity acceptable. Minimal re-normalization needed.")


# =============================================================================
# CONVENIENCE FUNCTIONS
# =============================================================================

def quick_analysis(statement):
    """
    Quick one-line analysis for interactive use.
    
    Args:
        statement: Text to analyze
        
    Returns:
        Simplified report dictionary
    """
    engine = MatrixEngine()
    analysis = engine.full_analysis(statement, verbose=False)
    
    return {
        "signal_clarity": analysis["entropy_report"]["signal_clarity"],
        "reified_metaphors": [m["term"] for m in analysis["reified_metaphors"]],
        "requires_correction": analysis["requires_renormalization"],
        "functional_restatement": engine.generate_functional_restatement(statement, analysis)
    }


def batch_analyze(statements):
    """
    Analyze multiple statements efficiently.
    
    Args:
        statements: List of texts to analyze
        
    Returns:
        List of analysis results
    """
    engine = MatrixEngine()
    results = []
    
    for statement in statements:
        results.append(engine.full_analysis(statement, verbose=False))
    
    return results
