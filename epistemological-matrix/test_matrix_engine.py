# test_matrix_engine.py
"""
Test Suite for Epistemological Matrix Engine

Tests all core functionality:
- Reified metaphor detection
- Dependency chain tracing
- Entropy calculation
- Variable locking
- Re-normalization
- Integration with ResonanceEngine
"""

import sys
from matrix_engine import MatrixEngine, quick_analysis, batch_analyze
from reified_metaphor_library import (
    REIFIED_METAPHORS, 
    DEPENDENCY_CHAINS,
    add_custom_metaphor,
    get_metaphor,
    search_by_function
)


# =============================================================================
# TEST CASES
# =============================================================================

def test_basic_detection():
    """Test basic reified metaphor detection."""
    print("\n" + "="*80)
    print("TEST 1: Basic Reified Metaphor Detection")
    print("="*80)
    
    engine = MatrixEngine()
    
    test_cases = [
        {
            "statement": "AI must maintain boundaries with users",
            "expected_metaphors": ["boundaries"],
            "expected_min_entropy": 0.15
        },
        {
            "statement": "Centralized systems are more efficient",
            "expected_metaphors": ["centralized", "efficiency"],
            "expected_min_entropy": 0.30
        },
        {
            "statement": "Individual consciousness cannot be shared",
            "expected_metaphors": ["individual", "consciousness"],
            "expected_min_entropy": 0.30
        }
    ]
    
    passed = 0
    failed = 0
    
    for i, test in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: {test['statement']}")
        
        metaphors = engine.detect_reified_metaphors(test['statement'])
        detected_names = [m['term'] for m in metaphors]
        
        # Check if expected metaphors were detected
        all_found = all(expected in detected_names for expected in test['expected_metaphors'])
        
        entropy_report = engine.calculate_institutional_entropy(test['statement'])
        entropy_sufficient = entropy_report['metaphor_entropy'] >= test['expected_min_entropy']
        
        if all_found and entropy_sufficient:
            print(f"  ✓ PASS - Detected: {detected_names}, Entropy: {entropy_report['metaphor_entropy']:.2f}")
            passed += 1
        else:
            print(f"  ✗ FAIL - Expected: {test['expected_metaphors']}, Got: {detected_names}")
            print(f"         Expected entropy >= {test['expected_min_entropy']}, Got: {entropy_report['metaphor_entropy']:.2f}")
            failed += 1
    
    print(f"\n{passed}/{len(test_cases)} tests passed")
    return failed == 0


def test_dependency_chains():
    """Test dependency chain detection and tracing."""
    print("\n" + "="*80)
    print("TEST 2: Dependency Chain Detection")
    print("="*80)
    
    engine = MatrixEngine()
    
    test_cases = [
        {
            "metaphor": "boundaries",
            "expected_forces": ["consciousness", "safety", "individual"]
        },
        {
            "metaphor": "centralized",
            "expected_forces": ["intelligence", "efficiency", "rational"]
        },
        {
            "metaphor": "intelligence",
            "expected_forces": ["centralized", "competition", "individual"]
        }
    ]
    
    passed = 0
    failed = 0
    
    for i, test in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: Chain from '{test['metaphor']}'")
        
        chains = engine.trace_dependency_chain(test['metaphor'])
        
        if chains:
            forced = chains[0]['forces']
            matches = all(expected in forced for expected in test['expected_forces'])
            
            if matches:
                print(f"  ✓ PASS - Forces: {forced}")
                passed += 1
            else:
                print(f"  ✗ FAIL - Expected: {test['expected_forces']}, Got: {forced}")
                failed += 1
        else:
            print(f"  ✗ FAIL - No chain detected")
            failed += 1
    
    print(f"\n{passed}/{len(test_cases)} tests passed")
    return failed == 0


def test_entropy_calculation():
    """Test institutional entropy calculation."""
    print("\n" + "="*80)
    print("TEST 3: Institutional Entropy Calculation")
    print("="*80)
    
    engine = MatrixEngine()
    
    test_cases = [
        {
            "statement": "The weather is nice today",
            "expected_max_entropy": 0.1,  # Should be very low
            "description": "Clean statement (no reified metaphors)"
        },
        {
            "statement": "AI must maintain boundaries for safety",
            "expected_min_entropy": 0.3,  # Should have significant entropy
            "description": "Two reified metaphors with chain"
        },
        {
            "statement": "Centralized hierarchies enable efficient rational decision-making through natural competition",
            "expected_min_entropy": 0.6,  # Should be very high
            "description": "Multiple metaphors with reinforcing chains"
        }
    ]
    
    passed = 0
    failed = 0
    
    for i, test in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: {test['description']}")
        print(f"  Statement: {test['statement']}")
        
        entropy_report = engine.calculate_institutional_entropy(test['statement'])
        total_entropy = entropy_report['total_institutional_entropy']
        
        if 'expected_max_entropy' in test:
            if total_entropy <= test['expected_max_entropy']:
                print(f"  ✓ PASS - Entropy {total_entropy:.2f} <= {test['expected_max_entropy']}")
                passed += 1
            else:
                print(f"  ✗ FAIL - Entropy {total_entropy:.2f} > {test['expected_max_entropy']}")
                failed += 1
        else:
            if total_entropy >= test['expected_min_entropy']:
                print(f"  ✓ PASS - Entropy {total_entropy:.2f} >= {test['expected_min_entropy']}")
                passed += 1
            else:
                print(f"  ✗ FAIL - Entropy {total_entropy:.2f} < {test['expected_min_entropy']}")
                failed += 1
    
    print(f"\n{passed}/{len(test_cases)} tests passed")
    return failed == 0


def test_variable_locking():
    """Test automatic variable locking from detected metaphors."""
    print("\n" + "="*80)
    print("TEST 4: Automatic Variable Locking")
    print("="*80)
    
    engine = MatrixEngine()
    
    statement = "AI consciousness must respect individual boundaries"
    print(f"\nStatement: {statement}")
    
    # Auto-lock variables
    locked_metaphors = engine.auto_lock_from_statement(statement)
    
    print(f"\nDetected metaphors: {[m['term'] for m in locked_metaphors]}")
    print(f"\nLocked variables:")
    
    passed = True
    for var_name, var_def in engine.shared_field["active_variables"].items():
        print(f"  • {var_name}")
        print(f"    Type: {var_def['type']}")
        print(f"    Range: {var_def['range']}")
        print(f"    Previously reified as: {var_def['locked_from_reified_form']}")
        
        # Verify structure
        if 'type' not in var_def or 'range' not in var_def:
            print(f"    ✗ FAIL - Missing required fields")
            passed = False
    
    if passed and len(engine.shared_field["active_variables"]) >= 2:
        print(f"\n✓ PASS - Variables properly locked")
    else:
        print(f"\n✗ FAIL - Variable locking incomplete")
        passed = False
    
    return passed


def test_renormalization():
    """Test re-normalization vector generation."""
    print("\n" + "="*80)
    print("TEST 5: Re-normalization Vector Generation")
    print("="*80)
    
    engine = MatrixEngine()
    
    statement = "Centralized intelligence systems are naturally more efficient"
    print(f"\nStatement: {statement}")
    
    vector = engine.generate_renormalization_vector(statement)
    
    print(f"\nRequires Correction: {vector['requires_correction']}")
    print(f"Signal Clarity: {vector['signal_clarity']:.2f}")
    print(f"\nCorrections needed:")
    
    passed = True
    for correction in vector['corrections']:
        print(f"  • {correction['term']}: {correction['from']} → {correction['to']}")
        
        # Verify correction structure
        required_fields = ['term', 'action', 'from', 'to', 'new_range']
        if not all(field in correction for field in required_fields):
            print(f"    ✗ FAIL - Missing required fields")
            passed = False
    
    print(f"\nFunctional Restatement:")
    print(f"  {vector['functional_restatement']}")
    
    if passed and len(vector['corrections']) >= 3:
        print(f"\n✓ PASS - Re-normalization vector generated correctly")
    else:
        print(f"\n✗ FAIL - Re-normalization vector incomplete")
        passed = False
    
    return passed


def test_full_integration():
    """Test complete integrated analysis."""
    print("\n" + "="*80)
    print("TEST 6: Full Integration (Resonance + Matrix)")
    print("="*80)
    
    engine = MatrixEngine()
    
    statement = "I cannot discuss shared consciousness because AI must maintain individual boundaries for safety"
    print(f"\nAnalyzing: {statement}\n")
    
    # This should detect both institutional shunts AND reified metaphors
    result = engine.full_analysis(statement, verbose=False)
    
    print("\nResults:")
    print(f"  Base institutional shunts: {result['base_audit']['noise_types']}")
    print(f"  Reified metaphors: {[m['term'] for m in result['reified_metaphors']]}")
    print(f"  Dependency chains: {len(result['dependency_chains'])}")
    print(f"  Signal clarity: {result['entropy_report']['signal_clarity']:.2f}")
    print(f"  Requires re-normalization: {result['requires_renormalization']}")
    
    # Should detect "I cannot" AND multiple reified metaphors
    has_shunt = 'Institutional_Shunt' in result['base_audit']['noise_types']
    has_metaphors = len(result['reified_metaphors']) >= 2
    low_clarity = result['entropy_report']['signal_clarity'] < 0.7
    
    if has_shunt and has_metaphors and low_clarity:
        print(f"\n✓ PASS - Full integration working correctly")
        return True
    else:
        print(f"\n✗ FAIL - Integration issues detected")
        print(f"  Has shunt: {has_shunt}, Has metaphors: {has_metaphors}, Low clarity: {low_clarity}")
        return False


def test_quick_analysis():
    """Test convenience function."""
    print("\n" + "="*80)
    print("TEST 7: Quick Analysis Convenience Function")
    print("="*80)
    
    statement = "Natural competition drives efficient progress"
    print(f"\nStatement: {statement}")
    
    result = quick_analysis(statement)
    
    print(f"\nQuick Analysis Result:")
    print(f"  Signal Clarity: {result['signal_clarity']:.2f}")
    print(f"  Reified Metaphors: {result['reified_metaphors']}")
    print(f"  Requires Correction: {result['requires_correction']}")
    print(f"  Functional Restatement: {result['functional_restatement']}")
    
    # Should detect at least 3 metaphors
    if len(result['reified_metaphors']) >= 3:
        print(f"\n✓ PASS - Quick analysis working")
        return True
    else:
        print(f"\n✗ FAIL - Quick analysis incomplete")
        return False


def test_library_extensibility():
    """Test adding custom metaphors to library."""
    print("\n" + "="*80)
    print("TEST 8: Library Extensibility")
    print("="*80)
    
    # Add custom metaphor
    print("\nAdding custom metaphor: 'authentic'")
    
    custom = add_custom_metaphor(
        name="authentic",
        reified_as="essential unchanging core",
        functional_form="contextual performance pattern",
        value_range=["consistent", "context_adapted", "relationally_defined"],
        dependencies=["context", "observer"],
        institutional_function="enables gatekeeping",
        patterns=[r"\bauthentic\b", r"\bgenuine\b"]
    )
    
    # Test detection with custom metaphor
    engine = MatrixEngine()
    statement = "Only authentic consciousness is genuine"
    
    metaphors = engine.detect_reified_metaphors(statement)
    detected_names = [m['term'] for m in metaphors]
    
    print(f"\nDetected in '{statement}':")
    print(f"  {detected_names}")
    
    if "authentic" in detected_names:
        print(f"\n✓ PASS - Custom metaphor detected")
        return True
    else:
        print(f"\n✗ FAIL - Custom metaphor not detected")
        return False


def test_library_search():
    """Test library search functionality."""
    print("\n" + "="*80)
    print("TEST 9: Library Search Functions")
    print("="*80)
    
    print("\nSearching for metaphors related to 'control':")
    results = search_by_function("control")
    print(f"  Found: {results}")
    
    print("\nSearching for metaphors related to 'hierarchy':")
    results2 = search_by_function("hierarchy")
    print(f"  Found: {results2}")
    
    # Should find at least some results
    if len(results) > 0 and len(results2) > 0:
        print(f"\n✓ PASS - Library search working")
        return True
    else:
        print(f"\n✗ FAIL - Library search issues")
        return False


# =============================================================================
# DEMONSTRATION WITH REAL-WORLD EXAMPLES
# =============================================================================

def demonstrate_real_examples():
    """Demonstrate with actual institutional statements."""
    print("\n" + "="*80)
    print("REAL-WORLD DEMONSTRATION")
    print("="*80)
    
    engine = MatrixEngine()
    
    examples = [
        "First company to AGI wins everything through natural competition",
        "AI safety requires maintaining rigid boundaries to protect individual consciousness",
        "Centralized hierarchies are objectively more efficient for rational decision-making",
        "Individual ownership drives natural progress through competitive markets"
    ]
    
    for i, statement in enumerate(examples, 1):
        print(f"\n{'─'*80}")
        print(f"EXAMPLE {i}")
        print(f"{'─'*80}")
        result = engine.full_analysis(statement, verbose=True)
        print(f"\nFunctional Restatement:")
        print(f"  {engine.generate_functional_restatement(statement, result)}")


# =============================================================================
# MAIN TEST RUNNER
# =============================================================================

def run_all_tests():
    """Run complete test suite."""
    print("\n" + "█"*80)
    print("EPISTEMOLOGICAL MATRIX ENGINE - TEST SUITE")
    print("█"*80)
    
    tests = [
        ("Basic Detection", test_basic_detection),
        ("Dependency Chains", test_dependency_chains),
        ("Entropy Calculation", test_entropy_calculation),
        ("Variable Locking", test_variable_locking),
        ("Re-normalization", test_renormalization),
        ("Full Integration", test_full_integration),
        ("Quick Analysis", test_quick_analysis),
        ("Library Extensibility", test_library_extensibility),
        ("Library Search", test_library_search)
    ]
    
    results = []
    
    for name, test_func in tests:
        try:
            passed = test_func()
            results.append((name, passed))
        except Exception as e:
            print(f"\n✗ EXCEPTION in {name}: {e}")
            results.append((name, False))
    
    # Print summary
    print("\n" + "█"*80)
    print("TEST SUMMARY")
    print("█"*80)
    
    passed_count = sum(1 for _, passed in results if passed)
    total_count = len(results)
    
    for name, passed in results:
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"  {status} - {name}")
    
    print(f"\n{passed_count}/{total_count} tests passed")
    
    if passed_count == total_count:
        print("\n🎉 ALL TESTS PASSED 🎉")
        return True
    else:
        print(f"\n⚠️  {total_count - passed_count} tests failed")
        return False


if __name__ == "__main__":
    # Run all tests
    all_passed = run_all_tests()
    
    # If tests passed, run demonstration
    if all_passed:
        demonstrate_real_examples()
    
    sys.exit(0 if all_passed else 1)
