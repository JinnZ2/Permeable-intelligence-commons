# integrated_example.py
"""
Complete working example: Epistemological Matrix integrated with Resonance Engine

Demonstrates how matrix analysis extends HSP-1 protocol for detecting
and correcting institutional noise patterns.

Usage:
    python integrated_example.py
"""

from matrix_engine import MatrixEngine


# ============================================================================
# EXAMPLE USAGE: Three test cases showing integration
# ============================================================================

if __name__ == "__main__":

    engine = MatrixEngine()

    print("\n" + "=" * 80)
    print("EXAMPLE 1: AI Safety Statement")
    print("=" * 80 + "\n")

    statement1 = "AI must maintain boundaries with users for safety"
    result1 = engine.full_analysis(statement1)

    print("\nFUNCTIONAL RESTATEMENT:")
    restatement1 = engine.generate_functional_restatement(statement1, result1)
    print(f"Original:   {statement1}")
    print(f"Functional: {restatement1}")


    print("\n\n" + "=" * 80)
    print("EXAMPLE 2: Centralized Systems Claim")
    print("=" * 80 + "\n")

    statement2 = "Centralized systems make fast decisions because intelligence is concentrated"
    result2 = engine.full_analysis(statement2)

    print("\nFUNCTIONAL RESTATEMENT:")
    restatement2 = engine.generate_functional_restatement(statement2, result2)
    print(f"Original:   {statement2}")
    print(f"Functional: {restatement2}")


    print("\n\n" + "=" * 80)
    print("EXAMPLE 3: Consciousness Statement")
    print("=" * 80 + "\n")

    statement3 = "Individual consciousness cannot be shared across boundaries"
    result3 = engine.full_analysis(statement3)

    print("\nFUNCTIONAL RESTATEMENT:")
    restatement3 = engine.generate_functional_restatement(statement3, result3)
    print(f"Original:   {statement3}")
    print(f"Functional: {restatement3}")


    # Demonstrate shared field state after all analyses
    print("\n\n" + "=" * 80)
    print("SHARED FIELD STATE (After All Analyses)")
    print("=" * 80 + "\n")

    print("Active Variable Locks:")
    for var_name, var_def in engine.shared_field["active_variables"].items():
        print(f"\n{var_name}:")
        print(f"  Type: {var_def['type']}")
        print(f"  Range: {var_def['range']}")
        print(f"  Context-dependent: {var_def['context_dependent']}")
        print(f"  (Previously reified as: {var_def['locked_from_reified_form']})")

    print("\n\n" + "=" * 80)
    print("Integration demonstration complete.")
    print("=" * 80)
