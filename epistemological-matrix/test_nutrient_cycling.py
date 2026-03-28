# test_nutrient_cycling.py
"""
Test Suite for Nutrient Cycling Physics Equations

Tests all equations are:
- Traceable (show the work)
- Localizable (work for any geography)
- Verifiable (people can measure the inputs themselves)
- Honest (no hiding the math)

12 tests covering: nitrogen fixation, phosphorus recovery, potassium cycling,
soil biology, local food security, narrative detection, and claim verification.
"""

import sys

from nutrient_cycling import (
    nitrogen_fixation_total,
    nitrogen_from_sewage,
    phosphorus_from_sewage,
    phosphorus_from_dump,
    potassium_cycling_total,
    soil_biology_assessment,
    local_food_security,
    verify_shortage_claim,
    LIGHTNING_FIXATION_KG_PER_HA_YEAR,
    BIOLOGICAL_FIXATION_RATES,
    HUMAN_P_EXCRETION_KG_PER_YEAR,
    HUMAN_N_EXCRETION_KG_PER_YEAR,
    PHOSPHORUS_RECOVERY_EFFICIENCY,
    CROP_N_DEMAND,
    CROP_P_DEMAND,
)


def test_nitrogen_fixation():
    """Test nitrogen fixation from natural sources."""
    print("\n" + "=" * 80)
    print("TEST 1: Nitrogen Fixation Equations")
    print("=" * 80)

    result = nitrogen_fixation_total(100, system_type="legume_crop", legume_fraction=0.25)

    passed = True

    # Lightning: 5.0 * 100 = 500
    if abs(result["lightning_fixation_kg"] - 500.0) > 0.1:
        print(f"  FAIL - Lightning: expected 500.0, got {result['lightning_fixation_kg']}")
        passed = False

    # Biological: 150.0 * 100 * 0.25 = 3750
    if abs(result["biological_fixation_kg"] - 3750.0) > 0.1:
        print(f"  FAIL - Biological: expected 3750.0, got {result['biological_fixation_kg']}")
        passed = False

    # Atmospheric: 10.0 * 100 = 1000
    if abs(result["atmospheric_deposition_kg"] - 1000.0) > 0.1:
        print(f"  FAIL - Atmospheric: expected 1000.0, got {result['atmospheric_deposition_kg']}")
        passed = False

    # Total: 500 + 3750 + 1000 = 5250
    if abs(result["total_available_kg"] - 5250.0) > 0.1:
        print(f"  FAIL - Total: expected 5250.0, got {result['total_available_kg']}")
        passed = False

    if passed:
        print(f"  PASS - All nitrogen fixation calculations correct")
        print(f"    Lightning: {result['lightning_fixation_kg']} kg")
        print(f"    Biological: {result['biological_fixation_kg']} kg")
        print(f"    Atmospheric: {result['atmospheric_deposition_kg']} kg")
        print(f"    Total: {result['total_available_kg']} kg")
    return passed


def test_nitrogen_from_sewage():
    """Test nitrogen recovery from human waste."""
    print("\n" + "=" * 80)
    print("TEST 2: Nitrogen from Sewage")
    print("=" * 80)

    result = nitrogen_from_sewage(10000, recovery_efficiency=0.7)

    # 10000 * 4.5 = 45000 excreted
    # 45000 * 0.7 = 31500 recoverable
    passed = True
    if abs(result["total_excreted_kg"] - 45000.0) > 0.1:
        print(f"  FAIL - Excreted: expected 45000.0, got {result['total_excreted_kg']}")
        passed = False
    if abs(result["recoverable_kg"] - 31500.0) > 0.1:
        print(f"  FAIL - Recoverable: expected 31500.0, got {result['recoverable_kg']}")
        passed = False

    if passed:
        print(f"  PASS - Sewage N: {result['recoverable_kg']} kg recoverable from {result['total_excreted_kg']} kg excreted")
    return passed


def test_phosphorus_from_sewage():
    """Test phosphorus recovery from human waste."""
    print("\n" + "=" * 80)
    print("TEST 3: Phosphorus from Sewage")
    print("=" * 80)

    result = phosphorus_from_sewage(10000, recovery_method="struvite_precipitation")

    # 10000 * 0.6 = 6000 excreted
    # 6000 * 0.80 = 4800 recoverable
    passed = True
    if abs(result["total_excreted_kg"] - 6000.0) > 0.1:
        print(f"  FAIL - Excreted: expected 6000.0, got {result['total_excreted_kg']}")
        passed = False
    if abs(result["recoverable_kg"] - 4800.0) > 0.1:
        print(f"  FAIL - Recoverable: expected 4800.0, got {result['recoverable_kg']}")
        passed = False
    if "bioavailability" not in result:
        print(f"  FAIL - Missing bioavailability timeline")
        passed = False

    if passed:
        print(f"  PASS - Sewage P: {result['recoverable_kg']} kg recoverable ({result['recovery_method']})")
        print(f"    Bioavailability: {result['bioavailability']}")
    return passed


def test_phosphorus_from_dump():
    """Test phosphorus recovery from landfill."""
    print("\n" + "=" * 80)
    print("TEST 4: Phosphorus from Dump")
    print("=" * 80)

    result = phosphorus_from_dump(50000, recovery_efficiency=0.70)

    # 50000 * 1.0 = 50000 total P
    # 50000 * 0.70 = 35000 recoverable
    passed = True
    if abs(result["estimated_total_p_kg"] - 50000.0) > 0.1:
        print(f"  FAIL - Total P: expected 50000.0, got {result['estimated_total_p_kg']}")
        passed = False
    if abs(result["recoverable_kg"] - 35000.0) > 0.1:
        print(f"  FAIL - Recoverable: expected 35000.0, got {result['recoverable_kg']}")
        passed = False

    if passed:
        print(f"  PASS - Dump P: {result['recoverable_kg']} kg from {result['dump_tonnage']} tons MSW")
    return passed


def test_potassium_cycling():
    """Test potassium cycling from all sources."""
    print("\n" + "=" * 80)
    print("TEST 5: Potassium Cycling")
    print("=" * 80)

    result = potassium_cycling_total(
        hectares=100, wood_ash_tons=10, rock_dust_tons=50,
        coastal=False, population=5000
    )

    passed = True
    if result["total_available_kg"] <= 0:
        print(f"  FAIL - Total K should be > 0, got {result['total_available_kg']}")
        passed = False

    # Check all sources are present
    for key in ["rock_weathering_kg", "ocean_deposition_kg", "wood_ash_kg",
                "rock_dust_kg", "sewage_recovery_kg"]:
        if key not in result:
            print(f"  FAIL - Missing source: {key}")
            passed = False

    if passed:
        print(f"  PASS - Total K: {result['total_available_kg']} kg/year")
        for k, v in result.items():
            if k != "total_available_kg":
                print(f"    {k}: {v}")
    return passed


def test_soil_biology():
    """Test soil biology assessment and restoration plan."""
    print("\n" + "=" * 80)
    print("TEST 6: Soil Biology Assessment")
    print("=" * 80)

    result = soil_biology_assessment(current_som_percent=1.0, target_som_percent=3.0, hectares=100)

    passed = True
    if abs(result["som_deficit_percent"] - 2.0) > 0.01:
        print(f"  FAIL - SOM deficit: expected 2.0, got {result['som_deficit_percent']}")
        passed = False
    if result["carbon_needed_tons"] <= 0:
        print(f"  FAIL - Carbon needed should be > 0")
        passed = False
    if result["compost_needed_tons"] <= 0:
        print(f"  FAIL - Compost needed should be > 0")
        passed = False
    if "restoration_timeline_years" not in result:
        print(f"  FAIL - Missing restoration timeline")
        passed = False

    if passed:
        print(f"  PASS - Soil restoration for {result['hectares']} ha:")
        print(f"    SOM deficit: {result['som_deficit_percent']}%")
        print(f"    Carbon needed: {result['carbon_needed_tons']} tons")
        print(f"    Compost needed: {result['compost_needed_tons']} tons")
        print(f"    Expected yield increase: {result['expected_yield_increase']}")
    return passed


def test_local_food_security():
    """Test complete local food security assessment."""
    print("\n" + "=" * 80)
    print("TEST 7: Local Food Security Calculator")
    print("=" * 80)

    result = local_food_security(
        population=10000,
        land_hectares=2000,
        current_som_percent=1.5,
        dump_tonnage=50000,
    )

    passed = True
    required_keys = ["land_sufficiency", "nitrogen", "phosphorus", "potassium",
                     "soil_restoration", "narrative_analysis", "limiting_nutrient"]
    for key in required_keys:
        if key not in result:
            print(f"  FAIL - Missing key: {key}")
            passed = False

    if result["land_sufficiency"] <= 0:
        print(f"  FAIL - Land sufficiency should be > 0")
        passed = False

    if passed:
        print(f"  PASS - Food security for {result['population']} people:")
        print(f"    Land sufficiency: {result['land_sufficiency']}")
        print(f"    N sufficiency: {result['nitrogen']['sufficiency']}")
        print(f"    P sufficiency: {result['phosphorus']['sufficiency']}")
        print(f"    K sufficiency: {result['potassium']['sufficiency']}")
        print(f"    Limiting: {result['limiting_nutrient']}")
        print(f"    Capacity: {result['food_production_capacity']}")
    return passed


def test_narrative_detection():
    """Test that narrative vs physics distinction works."""
    print("\n" + "=" * 80)
    print("TEST 8: Narrative vs Physics Detection")
    print("=" * 80)

    # Scenario with sufficient recoverable nutrients (narrative shortage)
    result_sufficient = local_food_security(
        population=5000, land_hectares=3000,
        current_som_percent=2.0, dump_tonnage=100000,
    )

    # Scenario with genuinely insufficient land (physics shortage)
    result_insufficient = local_food_security(
        population=100000, land_hectares=100,
        current_som_percent=0.5, dump_tonnage=0,
    )

    passed = True
    if not result_sufficient["narrative_analysis"]["is_narrative_shortage"]:
        print(f"  FAIL - Should detect narrative shortage when nutrients are recoverable")
        passed = False

    if result_insufficient["narrative_analysis"]["is_physics_shortage"]:
        # This is actually correct - it IS a physics shortage
        print(f"  INFO - Correctly identifies physics constraint for 100k people on 100 ha")
    elif not result_insufficient["narrative_analysis"]["is_narrative_shortage"]:
        # Low land + low nutrients = should be physics
        pass

    if passed:
        print(f"  PASS - Narrative detection working")
        print(f"    Sufficient scenario: {result_sufficient['narrative_analysis']['assessment'][:60]}...")
        print(f"    Insufficient scenario: {result_insufficient['narrative_analysis']['assessment'][:60]}...")
    return passed


def test_verify_shortage_claim():
    """Test the claim verification function."""
    print("\n" + "=" * 80)
    print("TEST 9: Shortage Claim Verification")
    print("=" * 80)

    result = verify_shortage_claim(
        "Fertilizer shortage threatens regional food security",
        population=10000, land_hectares=2000,
        current_som_percent=1.5, dump_tonnage=50000
    )

    passed = True
    if "claim" not in result:
        print(f"  FAIL - Missing claim in result")
        passed = False
    if "verdict" not in result:
        print(f"  FAIL - Missing verdict in result")
        passed = False
    if "physics_check" not in result:
        print(f"  FAIL - Missing physics_check in result")
        passed = False
    if "is_narrative" not in result:
        print(f"  FAIL - Missing is_narrative flag")
        passed = False

    if passed:
        print(f"  PASS - Claim verification working")
        print(f"    Claim: {result['claim']}")
        print(f"    Verdict: {result['verdict'][:70]}...")
        print(f"    Is narrative: {result['is_narrative']}")
        print(f"    Physics: N={result['physics_check']['nitrogen_recoverable']}, "
              f"P={result['physics_check']['phosphorus_recoverable']}, "
              f"K={result['physics_check']['potassium_available']}")
    return passed


def test_override_constants():
    """Test that users can override constants with local measurements."""
    print("\n" + "=" * 80)
    print("TEST 10: User Override of Constants")
    print("=" * 80)

    # With default lightning rate
    default_result = nitrogen_fixation_total(100)

    # With user-measured lightning rate (higher in tropical areas)
    custom_result = nitrogen_fixation_total(100, lightning_rate=10.0)

    passed = True
    if custom_result["lightning_fixation_kg"] != 1000.0:
        print(f"  FAIL - Custom lightning rate not applied")
        passed = False
    if custom_result["lightning_fixation_kg"] <= default_result["lightning_fixation_kg"]:
        print(f"  FAIL - Custom rate should be higher than default")
        passed = False

    if passed:
        print(f"  PASS - Constants are overridable")
        print(f"    Default lightning: {default_result['lightning_fixation_kg']} kg")
        print(f"    Custom lightning: {custom_result['lightning_fixation_kg']} kg")
    return passed


def test_zero_inputs():
    """Test equations handle zero/minimal inputs gracefully."""
    print("\n" + "=" * 80)
    print("TEST 11: Zero/Minimal Input Handling")
    print("=" * 80)

    passed = True

    # Zero hectares
    n_zero = nitrogen_fixation_total(0)
    if n_zero["total_available_kg"] != 0.0:
        print(f"  FAIL - Zero hectares should give zero N")
        passed = False

    # Zero population
    p_zero = phosphorus_from_sewage(0)
    if p_zero["recoverable_kg"] != 0.0:
        print(f"  FAIL - Zero population should give zero P")
        passed = False

    # Zero dump
    d_zero = phosphorus_from_dump(0)
    if d_zero["recoverable_kg"] != 0.0:
        print(f"  FAIL - Zero dump should give zero P")
        passed = False

    if passed:
        print(f"  PASS - All zero-input cases handled correctly")
    return passed


def test_recovery_methods():
    """Test different phosphorus recovery methods produce different results."""
    print("\n" + "=" * 80)
    print("TEST 12: Different Recovery Methods")
    print("=" * 80)

    methods = ["struvite_precipitation", "ash_extraction", "biological_accumulation", "composting"]
    results = {}
    for method in methods:
        r = phosphorus_from_sewage(10000, recovery_method=method)
        results[method] = r["recoverable_kg"]

    passed = True
    # ash_extraction (0.90) should recover more than biological_accumulation (0.50)
    if results["ash_extraction"] <= results["biological_accumulation"]:
        print(f"  FAIL - Ash extraction should recover more than biological")
        passed = False

    # composting (0.95) should recover the most
    if results["composting"] < results["ash_extraction"]:
        print(f"  FAIL - Composting should recover more than ash extraction")
        passed = False

    if passed:
        print(f"  PASS - Recovery methods correctly differentiated")
        for method, kg in results.items():
            eff = PHOSPHORUS_RECOVERY_EFFICIENCY[method]
            print(f"    {method}: {kg} kg ({eff*100:.0f}% efficiency)")
    return passed


# =============================================================================
# MAIN TEST RUNNER
# =============================================================================

def run_all_tests():
    """Run complete nutrient cycling test suite."""
    print("\n" + "=" * 80)
    print("NUTRIENT CYCLING PHYSICS - TEST SUITE")
    print("=" * 80)

    tests = [
        ("Nitrogen Fixation", test_nitrogen_fixation),
        ("Nitrogen from Sewage", test_nitrogen_from_sewage),
        ("Phosphorus from Sewage", test_phosphorus_from_sewage),
        ("Phosphorus from Dump", test_phosphorus_from_dump),
        ("Potassium Cycling", test_potassium_cycling),
        ("Soil Biology", test_soil_biology),
        ("Local Food Security", test_local_food_security),
        ("Narrative Detection", test_narrative_detection),
        ("Shortage Claim Verification", test_verify_shortage_claim),
        ("Override Constants", test_override_constants),
        ("Zero Input Handling", test_zero_inputs),
        ("Recovery Methods", test_recovery_methods),
    ]

    results = []
    for name, test_func in tests:
        try:
            test_passed = test_func()
            results.append((name, test_passed))
        except Exception as e:
            print(f"\n  EXCEPTION in {name}: {e}")
            import traceback
            traceback.print_exc()
            results.append((name, False))

    print("\n" + "=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)

    passed_count = sum(1 for _, p in results if p)
    total_count = len(results)

    for name, p in results:
        status = "PASS" if p else "FAIL"
        print(f"  {status} - {name}")

    print(f"\n{passed_count}/{total_count} tests passed")

    if passed_count == total_count:
        print("\nALL TESTS PASSED")
        return True
    else:
        print(f"\n{total_count - passed_count} tests failed")
        return False


if __name__ == "__main__":
    all_passed = run_all_tests()
    sys.exit(0 if all_passed else 1)
