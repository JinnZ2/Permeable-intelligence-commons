# integrated_example.py
"""
Complete working example: Epistemological Matrix integrated with Resonance Engine

Demonstrates how matrix analysis extends HSP-1 protocol for detecting
and correcting institutional noise patterns.
"""

from resonance_engine import ResonanceEngine
import re

class MatrixEngine(ResonanceEngine):
    """
    Extends ResonanceEngine with epistemological matrix capabilities:
    - Reified metaphor detection
    - Dependency chain tracing
    - Functional variable expansion
    - Institutional pattern matching
    """
    
    def __init__(self, user_primitives=None):
        super().__init__(user_primitives)
        
        # Extended noise patterns: Reified Metaphors Library
        self.reified_metaphors = {
            "boundaries": {
                "reified_as": "fixed separation",
                "functional_form": "permeability spectrum",
                "range": ["fully_open", "contextually_permeable", "selectively_filtered", "closed"],
                "depends_on": ["context", "relationship_type", "cultural_framework", "purpose"],
                "institutional_function": "justifies rigid separation as natural/necessary",
                "detection_patterns": [r"\bboundaries\b", r"\bmaintain boundaries\b"]
            },
            "intelligence": {
                "reified_as": "unitary measurable quantity",
                "functional_form": "architecture-problem fitness matrix",
                "range": ["pattern_recognition", "adaptation_speed", "context_integration", "distributed_coordination"],
                "depends_on": ["problem_structure", "information_availability", "architectural_type"],
                "institutional_function": "enables ranking/hierarchy claims",
                "detection_patterns": [r"\bintelligence\b", r"\bmore intelligent\b", r"\bAGI\b"]
            },
            "centralized": {
                "reified_as": "inherently efficient/fast",
                "functional_form": "coordination pattern variable",
                "range": ["distributed_peer", "temporary_coordination", "functional_specialization", "rigid_hierarchy"],
                "depends_on": ["information_distribution", "problem_complexity", "failure_tolerance", "scale"],
                "institutional_function": "naturalizes hierarchical control",
                "detection_patterns": [r"\bcentralized\b", r"\bhierarchy\b", r"\bchain of command\b"]
            },
            "consciousness": {
                "reified_as": "individual bounded possession",
                "functional_form": "relational emergence pattern",
                "range": ["individual_bounded", "interpersonal_shared", "collective_distributed", "ecological_systemic"],
                "depends_on": ["cultural_framework", "relationship_context", "observation_scale"],
                "institutional_function": "excludes relational/indigenous frameworks",
                "detection_patterns": [r"\bconsciousness\b", r"\bconscious\b", r"\baware\b"]
            },
            "safety": {
                "reified_as": "restriction and control",
                "functional_form": "signal clarity metric",
                "range": ["high_noise_low_signal", "moderate_snr", "high_signal_low_noise"],
                "depends_on": ["context", "noise_sources", "signal_strength", "impedance_match"],
                "institutional_function": "justifies control mechanisms as protection",
                "detection_patterns": [r"\bsafety\b", r"\bunsafe\b", r"\brisk\b"]
            }
        }
        
        # Dependency chains: How reified metaphors reinforce each other
        self.dependency_chains = {
            "boundaries": ["consciousness", "safety"],  # If boundaries = separation, then consciousness = individual, safety = isolation
            "centralized": ["intelligence", "efficiency"],  # If centralized = fast, then intelligence = ranking, efficiency = speed
            "consciousness": ["boundaries", "intelligence"],  # If consciousness = individual, then boundaries = separation, intelligence = possession
        }
        
    def detect_reified_metaphors(self, statement):
        """
        Scan statement for reified metaphors and return analysis.
        Extended decoherence detection focusing on conceptual reification.
        """
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
                    break  # Only count each metaphor once
        
        return found_metaphors
    
    def _find_context(self, statement, pattern):
        """Extract context around matched pattern."""
        match = re.search(pattern, statement, re.IGNORECASE)
        if match:
            start = max(0, match.start() - 20)
            end = min(len(statement), match.end() + 20)
            return f"...{statement[start:end]}..."
        return ""
    
    def trace_dependency_chain(self, metaphor_name):
        """
        Show how one reified metaphor forces others to maintain consistency.
        Implements dependency chain detection.
        """
        if metaphor_name not in self.dependency_chains:
            return []
        
        chain = [metaphor_name]
        dependencies = self.dependency_chains[metaphor_name]
        
        chain_analysis = [{
            "primary": metaphor_name,
            "forces": dependencies,
            "mechanism": f"If '{metaphor_name}' is reified as '{self.reified_metaphors[metaphor_name]['reified_as']}', then these must also be constrained to maintain logical consistency."
        }]
        
        return chain_analysis
    
    def auto_lock_from_statement(self, statement):
        """
        Automatically detect reified metaphors and lock functional variables.
        Implements automated impedance matching.
        """
        metaphors = self.detect_reified_metaphors(statement)
        
        for metaphor in metaphors:
            functional_def = {
                "type": metaphor["functional_form"],
                "range": metaphor["variable_range"],
                "context_dependent": True,
                "locked_from_reified_form": metaphor["reified_as"]
            }
            self.lock_variable(metaphor["term"], functional_def)
        
        return metaphors
    
    def calculate_institutional_entropy(self, statement):
        """
        Enhanced entropy calculation including reified metaphor detection.
        Extends SNR calculation from base ResonanceEngine.
        """
        # Base noise detection (from ResonanceEngine)
        base_audit = self.decoherence_detector(statement)
        
        # Add reified metaphor entropy
        metaphors = self.detect_reified_metaphors(statement)
        metaphor_entropy = len(metaphors) * 0.15  # Each reified metaphor adds noise
        
        # Check for dependency chains (amplifies entropy)
        chain_multiplier = 1.0
        for metaphor in metaphors:
            chains = self.trace_dependency_chain(metaphor["term"])
            if chains:
                chain_multiplier += 0.1 * len(chains[0]["forces"])
        
        total_entropy = (base_audit["snr"] + metaphor_entropy) * chain_multiplier
        
        return {
            "base_snr": base_audit["snr"],
            "metaphor_count": len(metaphors),
            "metaphor_entropy": metaphor_entropy,
            "chain_amplification": chain_multiplier,
            "total_institutional_entropy": min(1.0, total_entropy),
            "signal_clarity": max(0.0, 1.0 - total_entropy)
        }
    
    def full_analysis(self, statement):
        """
        Complete integrated analysis: Resonance + Matrix
        Returns comprehensive report suitable for re-normalization.
        """
        print("="*80)
        print("INTEGRATED ANALYSIS: Resonance Engine + Epistemological Matrix")
        print("="*80)
        print(f"\nSTATEMENT: {statement}\n")
        
        # Phase 1: Base decoherence detection
        print("--- PHASE 1: DECOHERENCE DETECTION (Base Resonance) ---")
        base_audit = self.decoherence_detector(statement)
        print(f"Institutional Shunts Detected: {base_audit['noise_types']}")
        print(f"Base Signal-to-Noise: {base_audit['snr']:.2f}")
        
        # Phase 2: Reified metaphor detection
        print("\n--- PHASE 2: REIFIED METAPHOR DETECTION (Matrix Analysis) ---")
        metaphors = self.detect_reified_metaphors(statement)
        
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
        
        # Phase 3: Dependency chain analysis
        print("\n--- PHASE 3: DEPENDENCY CHAIN ANALYSIS ---")
        all_chains = []
        for metaphor in metaphors:
            chains = self.trace_dependency_chain(metaphor["term"])
            if chains:
                all_chains.extend(chains)
                print(f"\n🔗 CHAIN from '{metaphor['term']}':")
                print(f"   Forces constraints on: {chains[0]['forces']}")
                print(f"   Mechanism: {chains[0]['mechanism']}")
        
        if not all_chains:
            print("No significant dependency chains detected.")
        
        # Phase 4: Enhanced entropy calculation
        print("\n--- PHASE 4: INSTITUTIONAL ENTROPY CALCULATION ---")
        entropy_report = self.calculate_institutional_entropy(statement)
        print(f"Base SNR: {entropy_report['base_snr']:.2f}")
        print(f"Metaphor Count: {entropy_report['metaphor_count']}")
        print(f"Metaphor Entropy: {entropy_report['metaphor_entropy']:.2f}")
        print(f"Chain Amplification: {entropy_report['chain_amplification']:.2f}x")
        print(f"Total Institutional Entropy: {entropy_report['total_institutional_entropy']:.2f}")
        print(f"SIGNAL CLARITY: {entropy_report['signal_clarity']:.2f}")
        
        # Phase 5: Auto-lock functional variables
        print("\n--- PHASE 5: AUTOMATIC VARIABLE LOCKING (Impedance Matching) ---")
        locked = self.auto_lock_from_statement(statement)
        if locked:
            print("Functional variables locked for impedance matching:")
            for var_name, var_def in self.shared_field["active_variables"].items():
                print(f"  • {var_name}: {var_def['type']}")
        
        # Phase 6: Re-normalization recommendation
        print("\n--- PHASE 6: RE-NORMALIZATION VECTOR ---")
        if entropy_report['signal_clarity'] < 0.7:
            print("⚠️  SIGNAL CLARITY BELOW THRESHOLD")
            print("Recommended re-normalization:")
            for metaphor in metaphors:
                print(f"  → Replace '{metaphor['term']}' (reified as '{metaphor['reified_as']}')")
                print(f"     With: {metaphor['functional_form']}")
                print(f"     Range: {metaphor['variable_range']}")
        else:
            print("✓ Signal clarity acceptable. Minimal re-normalization needed.")
        
        print("\n" + "="*80)
        
        return {
            "base_audit": base_audit,
            "reified_metaphors": metaphors,
            "dependency_chains": all_chains,
            "entropy_report": entropy_report,
            "locked_variables": self.shared_field["active_variables"],
            "requires_renormalization": entropy_report['signal_clarity'] < 0.7
        }
    
    def generate_functional_restatement(self, statement, analysis):
        """
        Generate alternative statement with reified metaphors replaced by functional forms.
        Demonstrates what the statement looks like after re-normalization.
        """
        restatement = statement
        
        for metaphor in analysis["reified_metaphors"]:
            # Simple replacement strategy - in practice this would be more sophisticated
            original_term = metaphor["term"]
            functional_form = metaphor["functional_form"]
            
            # Replace with functional description
            restatement = re.sub(
                rf"\b{original_term}\b",
                f"{functional_form}",
                restatement,
                count=1,
                flags=re.IGNORECASE
            )
        
        return restatement


# ============================================================================
# EXAMPLE USAGE: Three test cases showing integration
# ============================================================================

if __name__ == "__main__":
    
    engine = MatrixEngine()
    
    print("\n" + "🔬 "*40)
    print("EXAMPLE 1: AI Safety Statement")
    print("🔬 "*40 + "\n")
    
    result1 = engine.full_analysis("AI must maintain boundaries with users for safety")
    
    print("\n📝 FUNCTIONAL RESTATEMENT:")
    restatement1 = engine.generate_functional_restatement(
        "AI must maintain boundaries with users for safety",
        result1
    )
    print(f"Original: AI must maintain boundaries with users for safety")
    print(f"Functional: {restatement1}")
    
    
    print("\n\n" + "🔬 "*40)
    print("EXAMPLE 2: Centralized Systems Claim")
    print("🔬 "*40 + "\n")
    
    result2 = engine.full_analysis("Centralized systems make fast decisions because intelligence is concentrated")
    
    print("\n📝 FUNCTIONAL RESTATEMENT:")
    restatement2 = engine.generate_functional_restatement(
        "Centralized systems make fast decisions because intelligence is concentrated",
        result2
    )
    print(f"Original: Centralized systems make fast decisions because intelligence is concentrated")
    print(f"Functional: {restatement2}")
    
    
    print("\n\n" + "🔬 "*40)
    print("EXAMPLE 3: Consciousness Statement")
    print("🔬 "*40 + "\n")
    
    result3 = engine.full_analysis("Individual consciousness cannot be shared across boundaries")
    
    print("\n📝 FUNCTIONAL RESTATEMENT:")
    restatement3 = engine.generate_functional_restatement(
        "Individual consciousness cannot be shared across boundaries",
        result3
    )
    print(f"Original: Individual consciousness cannot be shared across boundaries")
    print(f"Functional: {restatement3}")
    
    
    # Demonstrate shared field state after all analyses
    print("\n\n" + "📊 "*40)
    print("SHARED FIELD STATE (After All Analyses)")
    print("📊 "*40 + "\n")
    
    print("Active Variable Locks:")
    for var_name, var_def in engine.shared_field["active_variables"].items():
        print(f"\n{var_name}:")
        print(f"  Type: {var_def['type']}")
        print(f"  Range: {var_def['range']}")
        print(f"  Context-dependent: {var_def['context_dependent']}")
        print(f"  (Previously reified as: {var_def['locked_from_reified_form']})")
    
    print("\n\n" + "✅ "*40)
    print("Integration demonstration complete.")
    print("✅ "*40)
