# matrix_engine.py
"""
Epistemological Matrix Engine - Extends Resonance Engine with reified metaphor detection

Part of the Permeable Intelligence Commons
Integrates with HSP-1 Protocol for enhanced institutional noise detection

Ontology frame: every detection, confidence score, and entropy value in this
module is a dX/dt bounded by the input statement, the metaphor catalog, and
the active context patterns. Results do not travel without their bounds. See
DIFFERENTIAL_FRAME.md at the repository root for the full AI-reader contract.

Core Functions:
- Detect reified metaphors with context-aware confidence scoring
- Trace dependency chains (how metaphors reinforce each other)
- Calculate institutional entropy with interaction-aware non-linear model
- Auto-lock functional variables (impedance matching)
- Generate functional restatements (re-normalization)
"""

import math
import re

from resonance_engine import ResonanceEngine
from reified_metaphor_library import REIFIED_METAPHORS, DEPENDENCY_CHAINS
from yaml_loader import load_metaphor_catalog

# =============================================================================
# ENTROPY CONSTANTS
# =============================================================================

# Each detected reified metaphor contributes this fraction of noise
# (now weighted by confidence)
METAPHOR_ENTROPY_WEIGHT = 0.15

# Signal clarity below this threshold triggers re-normalization
SIGNAL_CLARITY_THRESHOLD = 0.7

# Pairwise co-occurrence amplification rate
# (per shared dependency or chain connection between detected metaphor pairs)
COOCCURRENCE_AMPLIFICATION_RATE = 0.05

# Logistic saturation parameters for non-linear entropy
# f(x) = 1 / (1 + e^(-STEEPNESS * (x - MIDPOINT)))
SATURATION_STEEPNESS = 6.0
SATURATION_MIDPOINT = 0.5

# =============================================================================
# CONTEXT-AWARE DETECTION CONSTANTS
# =============================================================================

# Base confidence when a detection pattern matches (before context analysis)
BASE_DETECTION_CONFIDENCE = 0.5

# Boost per reified-context hit (capped at REIFIED_CONTEXT_MAX_BOOST)
REIFIED_CONTEXT_BOOST_PER_HIT = 0.15

# Maximum total boost from reified context matches
REIFIED_CONTEXT_MAX_BOOST = 0.3

# Penalty per functional-context hit (capped at FUNCTIONAL_CONTEXT_MAX_PENALTY)
FUNCTIONAL_CONTEXT_PENALTY_PER_HIT = 0.2

# Maximum total penalty from functional context matches
FUNCTIONAL_CONTEXT_MAX_PENALTY = 0.4

# Boost per co-occurring metaphor that shares a dependency chain
COOCCURRENCE_BOOST_PER_NEIGHBOR = 0.1

# Maximum total boost from co-occurrence
COOCCURRENCE_MAX_BOOST = 0.2

# Metaphors with confidence below this are excluded from results
CONFIDENCE_THRESHOLD = 0.3


class MatrixEngine(ResonanceEngine):
    """
    Extends ResonanceEngine with epistemological matrix capabilities.

    Enhances HSP-1 Protocol with:
    1. Context-aware reified metaphor detection with confidence scoring
    2. Dependency chain tracing (structural assumption analysis)
    3. Interaction-aware institutional entropy with logistic saturation
    4. Functional variable expansion (de-reification)
    """

    def __init__(self, user_primitives=None, custom_metaphors=None):
        """
        Initialize MatrixEngine with extended detection capabilities.

        Args:
            user_primitives: List of foundational assumptions (passed to ResonanceEngine)
            custom_metaphors: Additional reified metaphors to detect beyond library defaults
        """
        super().__init__(user_primitives)

        # Load basic metaphor library (for backward-compatible operations)
        self.reified_metaphors = REIFIED_METAPHORS.copy()
        if custom_metaphors:
            self.reified_metaphors.update(custom_metaphors)

        # Load extended library with context patterns for confidence scoring
        self._context_metaphors = load_metaphor_catalog(include_contexts=True)
        if custom_metaphors:
            self._context_metaphors.update(custom_metaphors)

        # Load dependency chains
        self.dependency_chains = DEPENDENCY_CHAINS.copy()

        # Analysis cache for performance
        self._analysis_cache = {}


    # =========================================================================
    # CORE DETECTION METHODS
    # =========================================================================

    def detect_reified_metaphors(self, statement):
        """
        Scan statement for reified metaphors with context-aware confidence scoring.

        Uses a two-pass approach:
        1. Base detection + per-metaphor reified/functional context scoring
        2. Co-occurrence boost based on dependency chain neighbors

        Args:
            statement: Text to analyze

        Returns:
            List of detected metaphors with properties:
            - term, reified_as, functional_form, value_range, depends_on,
              institutional_function, location_in_statement (standard)
            - confidence: float 0.0-1.0 (context-aware score)
            - detection_detail: breakdown of scoring components
        """
        # Check cache
        if statement in self._analysis_cache:
            return self._analysis_cache[statement]

        # Pass 1: Base detection with per-metaphor context scoring
        candidates = []
        for metaphor_name, properties in self.reified_metaphors.items():
            base_match = False
            for pattern in properties["detection_patterns"]:
                if re.search(pattern, statement, re.IGNORECASE):
                    base_match = True
                    break

            if not base_match:
                continue

            # Compute context scores from extended library
            ctx_props = self._context_metaphors.get(metaphor_name, properties)
            reified_score, functional_score = self._compute_context_score(
                statement, ctx_props
            )

            pre_cooccurrence = (
                BASE_DETECTION_CONFIDENCE
                + reified_score
                - functional_score
            )

            candidates.append({
                "term": metaphor_name,
                "reified_as": properties["reified_as"],
                "functional_form": properties["functional_form"],
                "value_range": properties["value_range"],
                "depends_on": properties["depends_on"],
                "institutional_function": properties["institutional_function"],
                "location_in_statement": self._find_context(
                    statement, properties["detection_patterns"][0]
                ),
                "_pre_cooccurrence": pre_cooccurrence,
                "_reified_score": reified_score,
                "_functional_score": functional_score,
            })

        # Pass 2: Co-occurrence boost
        detected_names = {c["term"] for c in candidates}
        found_metaphors = []

        for candidate in candidates:
            name = candidate["term"]

            # Count how many other detected metaphors are in this one's chain
            cooccurrence_score = 0.0
            chain_deps = set(self.dependency_chains.get(name, []))
            neighbors = detected_names & chain_deps
            cooccurrence_score = min(
                COOCCURRENCE_MAX_BOOST,
                len(neighbors) * COOCCURRENCE_BOOST_PER_NEIGHBOR
            )

            confidence = max(0.0, min(1.0,
                candidate["_pre_cooccurrence"] + cooccurrence_score
            ))

            # Filter by threshold
            if confidence < CONFIDENCE_THRESHOLD:
                continue

            # Build final result (strip internal fields)
            found_metaphors.append({
                "term": name,
                "reified_as": candidate["reified_as"],
                "functional_form": candidate["functional_form"],
                "value_range": candidate["value_range"],
                "depends_on": candidate["depends_on"],
                "institutional_function": candidate["institutional_function"],
                "location_in_statement": candidate["location_in_statement"],
                "confidence": round(confidence, 3),
                "detection_detail": {
                    "base": BASE_DETECTION_CONFIDENCE,
                    "reified_context_boost": candidate["_reified_score"],
                    "functional_context_penalty": candidate["_functional_score"],
                    "cooccurrence_boost": cooccurrence_score,
                }
            })

        # Cache result
        self._analysis_cache[statement] = found_metaphors
        return found_metaphors


    def _compute_context_score(self, statement, properties):
        """
        Compute reified and functional context scores for a metaphor match.

        Args:
            statement: Text being analyzed
            properties: Metaphor properties dict (may include context fields)

        Returns:
            Tuple of (reified_boost, functional_penalty) both >= 0.0
        """
        reified_hits = 0
        for pattern in properties.get("reified_contexts", []):
            if re.search(pattern, statement, re.IGNORECASE):
                reified_hits += 1
        reified_boost = min(
            REIFIED_CONTEXT_MAX_BOOST,
            reified_hits * REIFIED_CONTEXT_BOOST_PER_HIT
        )

        functional_hits = 0
        for pattern in properties.get("functional_contexts", []):
            if re.search(pattern, statement, re.IGNORECASE):
                functional_hits += 1
        functional_penalty = min(
            FUNCTIONAL_CONTEXT_MAX_PENALTY,
            functional_hits * FUNCTIONAL_CONTEXT_PENALTY_PER_HIT
        )

        return reified_boost, functional_penalty


    def trace_dependency_chain(self, metaphor_name):
        """
        Show how one reified metaphor forces others to maintain logical consistency.

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
            "mechanism": (
                f"If '{metaphor_name}' is reified as "
                f"'{self.reified_metaphors[metaphor_name]['reified_as']}', "
                f"then {', '.join(dependencies)} must also be constrained "
                f"to maintain logical consistency."
            ),
            "locked_metaphors": [
                self.reified_metaphors[dep]
                for dep in dependencies
                if dep in self.reified_metaphors
            ]
        }]

        return chain_analysis


    # =========================================================================
    # INTERACTION-AWARE ENTROPY
    # =========================================================================

    def calculate_institutional_entropy(self, statement):
        """
        Interaction-aware entropy calculation with logistic saturation.

        Formula:
            weighted_entropy = sum(confidence_i * METAPHOR_ENTROPY_WEIGHT)
            pair_amp = sum over pairs (chain_connection + depends_overlap) * COOCCURRENCE_AMPLIFICATION_RATE
            mutual_reinforcement = 1.0 + pair_amp
            raw_entropy = (base_entropy + weighted_entropy) * mutual_reinforcement
            total_entropy = logistic(raw_entropy)  = 1 / (1 + e^(-k*(x - x0)))
            signal_clarity = 1.0 - total_entropy

        Args:
            statement: Text to analyze

        Returns:
            Dictionary with entropy breakdown
        """
        # Base noise detection (from ResonanceEngine)
        base_audit = self.decoherence_detector(statement)
        base_entropy = 1.0 - base_audit["snr"]

        # Reified metaphor detection with confidence
        metaphors = self.detect_reified_metaphors(statement)

        # Step 1: Confidence-weighted metaphor entropy
        weighted_metaphor_entropy = sum(
            m.get("confidence", 1.0) * METAPHOR_ENTROPY_WEIGHT
            for m in metaphors
        )

        # Step 2: Pairwise co-occurrence amplification
        pair_amplification = self._calculate_pairwise_amplification(metaphors)

        # Step 3: Mutual reinforcement multiplier
        mutual_reinforcement = 1.0 + pair_amplification

        # Step 4: Raw entropy
        raw_entropy = (base_entropy + weighted_metaphor_entropy) * mutual_reinforcement

        # Step 5: Non-linear saturation (logistic curve)
        total_entropy = self._logistic_saturation(raw_entropy)

        # Step 6: Signal clarity
        signal_clarity = max(0.0, 1.0 - total_entropy)

        return {
            "base_snr": base_audit["snr"],
            "base_entropy": base_entropy,
            "metaphor_count": len(metaphors),
            # New detailed fields
            "weighted_metaphor_entropy": weighted_metaphor_entropy,
            "pairwise_amplification": pair_amplification,
            "mutual_reinforcement": mutual_reinforcement,
            "raw_entropy": raw_entropy,
            "saturation_applied": True,
            # Backward-compatible fields
            "metaphor_entropy": weighted_metaphor_entropy,
            "chain_amplification": mutual_reinforcement,
            "total_institutional_entropy": total_entropy,
            "signal_clarity": signal_clarity,
        }


    def _calculate_pairwise_amplification(self, detected_metaphors):
        """
        Calculate co-occurrence amplification for all pairs of detected metaphors.

        For each pair (A, B):
          - chain_connection: 1 if B in chains[A] or A in chains[B]
          - depends_overlap: |set(A.depends_on) & set(B.depends_on)|
          - pair_score: (chain_connection + depends_overlap) * COOCCURRENCE_AMPLIFICATION_RATE

        Args:
            detected_metaphors: List of detected metaphor dicts

        Returns:
            Total pairwise amplification score
        """
        if len(detected_metaphors) < 2:
            return 0.0

        total = 0.0
        names = [m["term"] for m in detected_metaphors]
        deps_map = {m["term"]: set(m.get("depends_on", [])) for m in detected_metaphors}

        for i in range(len(names)):
            for j in range(i + 1, len(names)):
                a, b = names[i], names[j]

                # Chain connection
                chain_a = set(self.dependency_chains.get(a, []))
                chain_b = set(self.dependency_chains.get(b, []))
                chain_connection = 1 if (b in chain_a or a in chain_b) else 0

                # Dependency overlap
                depends_overlap = len(deps_map.get(a, set()) & deps_map.get(b, set()))

                total += (chain_connection + depends_overlap) * COOCCURRENCE_AMPLIFICATION_RATE

        return total


    @staticmethod
    def _logistic_saturation(x):
        """
        Apply logistic saturation to raw entropy value.

        Returns value in (0, 1) that approaches 1.0 asymptotically.
        At x=SATURATION_MIDPOINT, output is 0.5.

        Args:
            x: Raw entropy value (can exceed 1.0)

        Returns:
            Saturated entropy in (0, 1)
        """
        return 1.0 / (1.0 + math.exp(-SATURATION_STEEPNESS * (x - SATURATION_MIDPOINT)))


    # =========================================================================
    # IMPEDANCE MATCHING / VARIABLE LOCKING
    # =========================================================================

    def auto_lock_from_statement(self, statement):
        """
        Automatically detect reified metaphors and lock functional variables.

        Args:
            statement: Text containing reified metaphors

        Returns:
            List of metaphors detected and locked
        """
        metaphors = self.detect_reified_metaphors(statement)

        for metaphor in metaphors:
            functional_def = {
                "type": metaphor["functional_form"],
                "range": metaphor["value_range"],
                "context_dependent": True,
                "depends_on": metaphor["depends_on"],
                "locked_from_reified_form": metaphor["reified_as"]
            }
            self.lock_variable(metaphor["term"], functional_def)

        return metaphors


    def suggest_variable_locks(self, statement):
        """
        Suggest variable locks without automatically applying them.

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
                "suggested_range": metaphor["value_range"],
                "confidence": metaphor.get("confidence", 1.0),
                "rationale": (
                    f"Expands '{metaphor['term']}' from constant "
                    f"({metaphor['reified_as']}) to variable "
                    f"({metaphor['functional_form']})"
                )
            }

        return suggestions


    # =========================================================================
    # RE-NORMALIZATION / OUTPUT GENERATION
    # =========================================================================

    def generate_functional_restatement(self, statement, analysis=None):
        """
        Generate alternative statement with reified metaphors replaced by functional forms.

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

        Args:
            statement: Statement needing re-normalization

        Returns:
            Dictionary with correction instructions
        """
        analysis = self.full_analysis(statement, verbose=False)

        corrections = []
        for metaphor in analysis["reified_metaphors"]:
            corrections.append({
                "term": metaphor["term"],
                "action": "expand",
                "from": metaphor["reified_as"],
                "to": metaphor["functional_form"],
                "new_range": metaphor["value_range"],
                "confidence": metaphor.get("confidence", 1.0),
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

        Args:
            statement: Text to analyze
            verbose: Print detailed report (default True)

        Returns:
            Complete analysis dictionary
        """
        if verbose:
            self._print_analysis_header(statement)

        # Phase 1: Base decoherence detection
        base_audit = self.decoherence_detector(statement)
        if verbose:
            self._print_phase1(base_audit)

        # Phase 2: Reified metaphor detection (now with confidence)
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

        # Phase 4: Interaction-aware entropy calculation
        entropy_report = self.calculate_institutional_entropy(statement)
        if verbose:
            self._print_phase4(entropy_report)

        # Phase 5: Auto-lock functional variables
        locked = self.auto_lock_from_statement(statement)
        if verbose:
            self._print_phase5()

        # Phase 6: Re-normalization recommendation
        requires_renorm = entropy_report['signal_clarity'] < SIGNAL_CLARITY_THRESHOLD
        if verbose:
            self._print_phase6(requires_renorm, metaphors)

        if verbose:
            print("\n" + "=" * 80)

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
        print("=" * 80)
        print("INTEGRATED ANALYSIS: Resonance Engine + Epistemological Matrix")
        print("=" * 80)
        print(f"\nSTATEMENT: {statement}\n")

    def _print_phase1(self, base_audit):
        print("--- PHASE 1: DECOHERENCE DETECTION (Base Resonance) ---")
        print(f"Institutional Shunts Detected: {base_audit['noise_types']}")
        print(f"Base Signal-to-Noise: {base_audit['snr']:.2f}")

    def _print_phase2(self, metaphors):
        print("\n--- PHASE 2: REIFIED METAPHOR DETECTION (Context-Aware) ---")
        if metaphors:
            for m in metaphors:
                conf = m.get('confidence', 'N/A')
                print(f"\n  REIFIED METAPHOR: '{m['term']}' (confidence: {conf})")
                print(f"   Reified as: {m['reified_as']}")
                print(f"   Functional form: {m['functional_form']}")
                print(f"   Value range: {m['value_range']}")
                print(f"   Context: {m['location_in_statement']}")
                print(f"   Institutional function: {m['institutional_function']}")
                if 'detection_detail' in m:
                    d = m['detection_detail']
                    print(f"   Scoring: base={d['base']}, "
                          f"reified_boost=+{d['reified_context_boost']:.2f}, "
                          f"functional_penalty=-{d['functional_context_penalty']:.2f}, "
                          f"cooccurrence=+{d['cooccurrence_boost']:.2f}")
        else:
            print("No reified metaphors detected.")

    def _print_phase3(self, all_chains):
        print("\n--- PHASE 3: DEPENDENCY CHAIN ANALYSIS ---")
        if all_chains:
            for chain in all_chains:
                print(f"\n  CHAIN from '{chain['primary']}':")
                print(f"   Forces constraints on: {chain['forces']}")
                print(f"   Mechanism: {chain['mechanism']}")
        else:
            print("No significant dependency chains detected.")

    def _print_phase4(self, entropy_report):
        print("\n--- PHASE 4: INTERACTION-AWARE ENTROPY ---")
        print(f"Base SNR: {entropy_report['base_snr']:.2f}")
        print(f"Metaphor Count: {entropy_report['metaphor_count']}")
        print(f"Weighted Metaphor Entropy: {entropy_report['weighted_metaphor_entropy']:.3f}")
        print(f"Pairwise Amplification: {entropy_report['pairwise_amplification']:.3f}")
        print(f"Mutual Reinforcement: {entropy_report['mutual_reinforcement']:.2f}x")
        print(f"Raw Entropy: {entropy_report['raw_entropy']:.3f}")
        print(f"Total Entropy (saturated): {entropy_report['total_institutional_entropy']:.3f}")
        print(f"SIGNAL CLARITY: {entropy_report['signal_clarity']:.3f}")

    def _print_phase5(self):
        print("\n--- PHASE 5: AUTOMATIC VARIABLE LOCKING (Impedance Matching) ---")
        if self.shared_field["active_variables"]:
            print("Functional variables locked for impedance matching:")
            for var_name, var_def in self.shared_field["active_variables"].items():
                print(f"  * {var_name}: {var_def['type']}")
        else:
            print("No variables locked (no reified metaphors detected).")

    def _print_phase6(self, requires_renorm, metaphors):
        print("\n--- PHASE 6: RE-NORMALIZATION VECTOR ---")
        if requires_renorm:
            print("  SIGNAL CLARITY BELOW THRESHOLD")
            print("Recommended re-normalization:")
            for metaphor in metaphors:
                conf = metaphor.get('confidence', 'N/A')
                print(f"  -> Replace '{metaphor['term']}' [conf={conf}] "
                      f"(reified as '{metaphor['reified_as']}')")
                print(f"     With: {metaphor['functional_form']}")
                print(f"     Range: {metaphor['value_range']}")
        else:
            print("Signal clarity acceptable. Minimal re-normalization needed.")


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
