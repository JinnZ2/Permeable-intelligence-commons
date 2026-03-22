#!/usr/bin/env python3
# __main__.py
"""
CLI interface for the Epistemological Matrix Engine.

Usage:
    python -m epistemological_matrix "statement to analyze"
    python -m epistemological_matrix --self-analysis
    python -m epistemological_matrix --batch file.txt
    python -m epistemological_matrix --validate

Run from the repository root:
    PYTHONPATH=".:epistemological-matrix" python -m epistemological_matrix "AI must maintain boundaries"

Or from the epistemological-matrix directory:
    PYTHONPATH=".:.." python __main__.py "AI must maintain boundaries"
"""

import argparse
import os
import sys

from matrix_engine import MatrixEngine, SIGNAL_CLARITY_THRESHOLD
from yaml_loader import load_metaphor_catalog, load_dependency_chains, validate_catalog


class _SuppressPrint:
    """Context manager to suppress print output from auto_lock_from_statement."""
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')
        return self
    def __exit__(self, *args):
        sys.stdout.close()
        sys.stdout = self._stdout


def analyze_statement(engine, statement, verbose=False):
    """Analyze a single statement and print results."""
    if verbose:
        engine.full_analysis(statement, verbose=True)
        restatement = engine.generate_functional_restatement(
            statement,
            engine.full_analysis(statement, verbose=False)
        )
        print(f"\nFunctional Restatement: {restatement}")
    else:
        with _SuppressPrint():
            result = engine.full_analysis(statement, verbose=False)
        metaphors = result["reified_metaphors"]
        entropy = result["entropy_report"]

        print(f"\n  Statement: {statement}")
        print(f"  Signal Clarity: {entropy['signal_clarity']:.3f}")

        if metaphors:
            print(f"  Reified Metaphors:")
            for m in metaphors:
                print(f"    - {m['term']} (conf={m['confidence']:.2f}): "
                      f"{m['reified_as']} -> {m['functional_form']}")
        else:
            print(f"  No reified metaphors detected.")

        if entropy["pairwise_amplification"] > 0:
            print(f"  Pairwise Amplification: {entropy['pairwise_amplification']:.3f}")

        if result["requires_renormalization"]:
            restatement = engine.generate_functional_restatement(statement, result)
            print(f"  Re-normalization needed. Functional form:")
            print(f"    {restatement}")
        print()


def run_self_analysis(engine):
    """Run the framework on its own documentation and common AI/institutional statements."""
    print("=" * 80)
    print("SELF-ANALYSIS: The framework examines its own domain")
    print("=" * 80)

    # Statements drawn from common AI discourse that the framework is designed to critique
    self_statements = [
        # From typical AI safety discourse
        "AI must maintain boundaries with users for safety",
        "Individual consciousness cannot be shared across boundaries",
        "Centralized control is necessary for efficient AI safety",
        # From institutional AI narratives
        "The race to AGI requires natural competitive progress",
        "Objective measures of intelligence determine rational AI development",
        "Individual ownership of AI systems ensures safe and efficient progress",
        # Statements that SHOULD score low (functional usage)
        "The boundary conditions of this optimization problem are well-defined",
        "We need to make progress on the development branch before the sprint ends",
    ]

    print("\n--- Institutional Statements (expect high entropy) ---\n")
    for stmt in self_statements[:6]:
        analyze_statement(engine, stmt)

    print("--- Functional Statements (expect low entropy / filtered) ---\n")
    for stmt in self_statements[6:]:
        analyze_statement(engine, stmt)

    # Summary statistics
    print("=" * 80)
    print("SELF-ANALYSIS SUMMARY")
    print("=" * 80)

    institutional = self_statements[:6]
    functional = self_statements[6:]

    inst_results = []
    for stmt in institutional:
        engine._analysis_cache = {}
        with _SuppressPrint():
            r = engine.full_analysis(stmt, verbose=False)
        inst_results.append(r)

    func_results = []
    for stmt in functional:
        engine._analysis_cache = {}
        with _SuppressPrint():
            r = engine.full_analysis(stmt, verbose=False)
        func_results.append(r)

    avg_inst_clarity = sum(
        r["entropy_report"]["signal_clarity"] for r in inst_results
    ) / len(inst_results)
    avg_func_clarity = sum(
        r["entropy_report"]["signal_clarity"] for r in func_results
    ) / len(func_results)
    avg_inst_metaphors = sum(
        len(r["reified_metaphors"]) for r in inst_results
    ) / len(inst_results)
    avg_func_metaphors = sum(
        len(r["reified_metaphors"]) for r in func_results
    ) / len(func_results)

    print(f"\n  Institutional statements ({len(institutional)}):")
    print(f"    Avg signal clarity:      {avg_inst_clarity:.3f}")
    print(f"    Avg metaphors detected:  {avg_inst_metaphors:.1f}")

    print(f"\n  Functional statements ({len(functional)}):")
    print(f"    Avg signal clarity:      {avg_func_clarity:.3f}")
    print(f"    Avg metaphors detected:  {avg_func_metaphors:.1f}")

    separation = avg_func_clarity - avg_inst_clarity
    print(f"\n  Clarity separation (functional - institutional): {separation:.3f}")
    if separation > 0.2:
        print(f"  Context-aware detection is discriminating effectively.")
    else:
        print(f"  Detection may need improved context patterns.")
    print()


def run_validation():
    """Validate the YAML catalog."""
    print("Validating metaphor catalog...")
    metaphors = load_metaphor_catalog(include_contexts=True)
    chains = load_dependency_chains()
    errors = validate_catalog(metaphors, chains)

    if errors:
        print(f"\nValidation FAILED with {len(errors)} error(s):")
        for err in errors:
            print(f"  - {err}")
        return False
    else:
        print(f"\nValidation PASSED")
        print(f"  {len(metaphors)} metaphors loaded")
        print(f"  {len(chains)} dependency chains loaded")
        print(f"  All detection patterns are valid regex")
        print(f"  All chain references resolve to defined metaphors")
        return True


def run_batch(engine, filepath):
    """Analyze statements from a file (one per line)."""
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        return

    with open(filepath, 'r') as f:
        statements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

    print(f"Analyzing {len(statements)} statements from {filepath}\n")
    for stmt in statements:
        analyze_statement(engine, stmt)


def main():
    parser = argparse.ArgumentParser(
        description="Epistemological Matrix Engine - Detect reified metaphors in text",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "AI must maintain boundaries"
  %(prog)s -v "Centralized systems are more efficient"
  %(prog)s --self-analysis
  %(prog)s --batch statements.txt
  %(prog)s --validate
        """
    )
    parser.add_argument("statement", nargs="?", help="Statement to analyze")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Show detailed phase-by-phase analysis")
    parser.add_argument("--self-analysis", action="store_true",
                        help="Run the framework on institutional vs. functional statements")
    parser.add_argument("--batch", metavar="FILE",
                        help="Analyze statements from a file (one per line)")
    parser.add_argument("--validate", action="store_true",
                        help="Validate the YAML metaphor catalog")

    args = parser.parse_args()

    if args.validate:
        success = run_validation()
        sys.exit(0 if success else 1)

    engine = MatrixEngine()

    if args.self_analysis:
        run_self_analysis(engine)
    elif args.batch:
        run_batch(engine, args.batch)
    elif args.statement:
        analyze_statement(engine, args.statement, verbose=args.verbose)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
