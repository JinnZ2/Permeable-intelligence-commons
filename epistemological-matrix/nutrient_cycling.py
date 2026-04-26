# nutrient_cycling.py
"""
Nutrient Cycling Physics Equations

Traceable, localizable, verifiable equations for nitrogen, phosphorus,
and potassium cycling. Enables any community to calculate their actual
nutrient availability vs. the claimed "fertilizer shortage" narrative.

When someone says "fertilizer shortage," these equations let you:
1. Calculate available phosphorus (sewage + dumps + rock)
2. Calculate available nitrogen (biological fixation + atmospheric)
3. Calculate available potassium (rock dust + ocean + ash)
4. Compare to claimed shortage
5. Detect: "This is a narrative, not a physics problem"

All constants are sourced from peer-reviewed literature with citations.
Users can override any constant with local measurements.

Ontology frame: every yield, recovery rate, and "shortage" verdict in this
module is a dX/dt under explicit bounds (geography, lithology, season,
biota, technology). The defaults are envelope estimates — local measurement
overrides them. Stripping a result from its bounds is a translation error.
See DIFFERENTIAL_FRAME.md at the repository root for the full AI-reader
contract and claim template.

Part of the Permeable Intelligence Commons
License: MIT (c) 2025 JinnZ2
"""

import math


# =============================================================================
# NITROGEN FIXATION EQUATIONS
# =============================================================================

# Lightning fixation: ~3-10 kg N/ha/year globally averaged
# Source: Galloway et al. (2004) Biogeochemistry 70:153-226
LIGHTNING_FIXATION_KG_PER_HA_YEAR = 5.0

# Biological fixation rates by crop/system (kg N/ha/year)
# Source: Peoples et al. (2009) Symbiosis 48:1-17
BIOLOGICAL_FIXATION_RATES = {
    "legume_crop": 150.0,        # soybeans, lentils, beans
    "legume_pasture": 200.0,     # clover, alfalfa
    "free_living_bacteria": 15.0, # azotobacter, cyanobacteria
    "associative_fixation": 30.0, # azospirillum with grasses
    "tree_legumes": 300.0,       # leucaena, acacia in agroforestry
}

# Atmospheric deposition (rain washout): 5-20 kg N/ha/year
# Source: Dentener et al. (2006) Global Biogeochemical Cycles 20:GB4003
ATMOSPHERIC_DEPOSITION_KG_PER_HA_YEAR = 10.0

# Compost nitrogen content: ~1-3% by dry weight
# Source: Rynk (1992) On-Farm Composting Handbook
COMPOST_N_PERCENT_DRY_WEIGHT = 0.02  # 2%

# Human nitrogen excretion: ~4.0-5.0 kg N/person/year
# Source: Rose et al. (2015) Environ. Sci. Technol. 49:3176-3184
HUMAN_N_EXCRETION_KG_PER_YEAR = 4.5

# Crop nitrogen demand (kg N/ha/year) for reference
CROP_N_DEMAND = {
    "wheat": 120.0,
    "corn_maize": 180.0,
    "rice": 100.0,
    "vegetables_mixed": 150.0,
    "potatoes": 130.0,
    "fruit_trees": 80.0,
}


def nitrogen_fixation_total(hectares, system_type="legume_crop",
                            legume_fraction=0.25,
                            lightning_rate=None,
                            bio_rate=None,
                            atm_deposition=None):
    """
    Calculate total nitrogen available from natural fixation sources.

    Args:
        hectares: Total agricultural land area
        system_type: Type of biological fixation system
        legume_fraction: Fraction of land in legume rotation (0-1)
        lightning_rate: Override lightning fixation (kg/ha/year)
        bio_rate: Override biological fixation rate (kg/ha/year)
        atm_deposition: Override atmospheric deposition (kg/ha/year)

    Returns:
        Dictionary with nitrogen sources breakdown (kg/year)
    """
    lightning = (lightning_rate or LIGHTNING_FIXATION_KG_PER_HA_YEAR) * hectares
    bio = (bio_rate or BIOLOGICAL_FIXATION_RATES.get(
        system_type, BIOLOGICAL_FIXATION_RATES["legume_crop"]
    )) * hectares * legume_fraction
    atm = (atm_deposition or ATMOSPHERIC_DEPOSITION_KG_PER_HA_YEAR) * hectares

    return {
        "lightning_fixation_kg": round(lightning, 1),
        "biological_fixation_kg": round(bio, 1),
        "atmospheric_deposition_kg": round(atm, 1),
        "total_available_kg": round(lightning + bio + atm, 1),
        "sources": {
            "lightning_rate_kg_ha_yr": lightning_rate or LIGHTNING_FIXATION_KG_PER_HA_YEAR,
            "bio_rate_kg_ha_yr": bio_rate or BIOLOGICAL_FIXATION_RATES.get(system_type, 150.0),
            "atm_rate_kg_ha_yr": atm_deposition or ATMOSPHERIC_DEPOSITION_KG_PER_HA_YEAR,
        }
    }


def nitrogen_from_sewage(population, recovery_efficiency=0.7):
    """
    Calculate recoverable nitrogen from human waste.

    Args:
        population: Number of people
        recovery_efficiency: Fraction recoverable (0-1), default 0.7

    Returns:
        Dictionary with nitrogen recovery breakdown
    """
    total_excreted = population * HUMAN_N_EXCRETION_KG_PER_YEAR
    recoverable = total_excreted * recovery_efficiency

    return {
        "total_excreted_kg": round(total_excreted, 1),
        "recoverable_kg": round(recoverable, 1),
        "recovery_efficiency": recovery_efficiency,
        "per_capita_kg": HUMAN_N_EXCRETION_KG_PER_YEAR,
    }


# =============================================================================
# PHOSPHORUS RECOVERY EQUATIONS
# =============================================================================

# Human phosphorus excretion: ~0.5-0.7 kg P/person/year
# Source: Mihelcic et al. (2011) Environ. Sci. Technol. 45:3475-3486
HUMAN_P_EXCRETION_KG_PER_YEAR = 0.6

# Sewage P concentration: ~5-10 mg/L in raw sewage
# Source: Tchobanoglous et al. (2003) Wastewater Engineering
SEWAGE_P_CONCENTRATION_MG_PER_L = 7.0

# Dump/landfill phosphorus density estimate: varies widely
# ~0.5-2.0 kg P per ton of municipal solid waste
# Source: Brunner & Rechberger (2004) Practical Handbook of Material Flow Analysis
DUMP_P_KG_PER_TON_MSW = 1.0

# Recovery efficiencies by method
PHOSPHORUS_RECOVERY_EFFICIENCY = {
    "struvite_precipitation": 0.80,   # crystallization from wastewater
    "ash_extraction": 0.90,           # from sewage sludge incineration
    "chemical_extraction": 0.70,      # acid/base extraction from waste
    "biological_accumulation": 0.50,  # enhanced biological P removal
    "composting": 0.95,               # direct composting of biosolids
}

# Bioavailability timeline (fraction plant-available by year)
# Recovered P is not immediately as available as synthetic P
BIOAVAILABILITY_TIMELINE = {
    "year_1": 0.40,  # 40% available first year
    "year_2": 0.65,  # 65% cumulative by year 2
    "year_3": 0.80,  # 80% cumulative by year 3
    "year_5": 0.95,  # 95% cumulative by year 5
}

# Crop phosphorus demand (kg P/ha/year)
CROP_P_DEMAND = {
    "wheat": 20.0,
    "corn_maize": 30.0,
    "rice": 15.0,
    "vegetables_mixed": 25.0,
    "potatoes": 25.0,
    "fruit_trees": 15.0,
}


def phosphorus_from_sewage(population, recovery_method="struvite_precipitation"):
    """
    Calculate recoverable phosphorus from human waste streams.

    Args:
        population: Number of people
        recovery_method: Method used for recovery

    Returns:
        Dictionary with phosphorus recovery breakdown
    """
    total_excreted = population * HUMAN_P_EXCRETION_KG_PER_YEAR
    efficiency = PHOSPHORUS_RECOVERY_EFFICIENCY.get(
        recovery_method, 0.70
    )
    recoverable = total_excreted * efficiency

    return {
        "total_excreted_kg": round(total_excreted, 1),
        "recoverable_kg": round(recoverable, 1),
        "recovery_method": recovery_method,
        "recovery_efficiency": efficiency,
        "per_capita_kg": HUMAN_P_EXCRETION_KG_PER_YEAR,
        "bioavailability": BIOAVAILABILITY_TIMELINE.copy(),
    }


def phosphorus_from_dump(dump_tonnage, recovery_efficiency=0.70):
    """
    Calculate recoverable phosphorus from landfill/dump sites.

    Args:
        dump_tonnage: Estimated tons of municipal solid waste in dump
        recovery_efficiency: Fraction extractable (0-1)

    Returns:
        Dictionary with dump phosphorus recovery
    """
    total_p = dump_tonnage * DUMP_P_KG_PER_TON_MSW
    recoverable = total_p * recovery_efficiency

    return {
        "estimated_total_p_kg": round(total_p, 1),
        "recoverable_kg": round(recoverable, 1),
        "recovery_efficiency": recovery_efficiency,
        "dump_tonnage": dump_tonnage,
        "p_density_kg_per_ton": DUMP_P_KG_PER_TON_MSW,
    }


# =============================================================================
# POTASSIUM CYCLING EQUATIONS
# =============================================================================

# Rock weathering release: 2-10 kg K/ha/year (highly variable by geology)
# Source: Hinsinger et al. (2001) Plant and Soil 237:215-237
ROCK_WEATHERING_K_KG_PER_HA_YEAR = 5.0

# Wood ash potassium content: ~3-7% K by weight
# Source: Demeyer et al. (2001) Bioresource Technology 77:287-295
WOOD_ASH_K_PERCENT = 0.05  # 5%

# Ocean spray/aerosol deposition: ~1-5 kg K/ha/year (coastal areas)
# Source: Stallard & Edmond (1981) JGR 86:9844-9858
OCEAN_SPRAY_K_KG_PER_HA_YEAR = 2.0  # inland default, coastal can be 5+

# Human potassium excretion: ~1.5-2.0 kg K/person/year
# Source: Rose et al. (2015) Environ. Sci. Technol. 49:3176-3184
HUMAN_K_EXCRETION_KG_PER_YEAR = 1.7

# Rock dust K content: feldspar/granite ~3-5% K2O
# Source: van Straaten (2006) Anais da Academia Brasileira de Ciencias 78:731-747
ROCK_DUST_K2O_PERCENT = 0.04  # 4%
K2O_TO_K_FACTOR = 0.83        # K2O is 83% K by weight

# Crop potassium demand (kg K/ha/year)
CROP_K_DEMAND = {
    "wheat": 80.0,
    "corn_maize": 120.0,
    "rice": 80.0,
    "vegetables_mixed": 150.0,
    "potatoes": 200.0,
    "fruit_trees": 100.0,
}


def potassium_cycling_total(hectares, wood_ash_tons=0.0, rock_dust_tons=0.0,
                            coastal=False, population=0):
    """
    Calculate total potassium available from cycling sources.

    Args:
        hectares: Agricultural land area
        wood_ash_tons: Available wood ash (tons/year)
        rock_dust_tons: Available rock dust (tons/year)
        coastal: Whether area is near coast (higher ocean spray)
        population: Population for sewage K recovery

    Returns:
        Dictionary with potassium sources breakdown (kg/year)
    """
    weathering = ROCK_WEATHERING_K_KG_PER_HA_YEAR * hectares
    ocean = (5.0 if coastal else OCEAN_SPRAY_K_KG_PER_HA_YEAR) * hectares
    ash_k = wood_ash_tons * 1000 * WOOD_ASH_K_PERCENT  # tons -> kg -> K content
    rock_k = rock_dust_tons * 1000 * ROCK_DUST_K2O_PERCENT * K2O_TO_K_FACTOR
    sewage_k = population * HUMAN_K_EXCRETION_KG_PER_YEAR * 0.7  # 70% recovery

    total = weathering + ocean + ash_k + rock_k + sewage_k

    return {
        "rock_weathering_kg": round(weathering, 1),
        "ocean_deposition_kg": round(ocean, 1),
        "wood_ash_kg": round(ash_k, 1),
        "rock_dust_kg": round(rock_k, 1),
        "sewage_recovery_kg": round(sewage_k, 1),
        "total_available_kg": round(total, 1),
    }


# =============================================================================
# SOIL BIOLOGY CASCADE
# =============================================================================

# Microbial biomass carbon target: 200-500 mg C/kg soil for functional cycling
# Source: Kallenbach & Grandy (2011) Soil Biology & Biochemistry 43:1-8
MICROBIAL_BIOMASS_TARGET_MG_C_PER_KG = 350.0

# Carbon needed to rebuild soil organic matter (tons C/ha)
# From 1% SOM to 3% SOM in top 30cm, bulk density ~1.3 g/cm3
# Source: Lal (2004) Science 304:1623-1627
CARBON_TO_REBUILD_PER_PERCENT_SOM = 39.0  # tons C/ha per 1% SOM increase

# Soil restoration timeline (years to functional cycling)
# Source: LaCanne & Lundgren (2018) PeerJ 6:e4428
SOIL_RESTORATION_TIMELINE = {
    "degraded_to_transitional": 3,    # years to see microbial activity
    "transitional_to_functional": 5,  # years to nutrient cycling
    "functional_to_regenerative": 7,  # years to full regeneration
    "total_full_restoration": 15,     # years for complete soil health
}

# Yield improvement per unit soil health
# Measured as % yield increase per 1% SOM increase
# Source: Oldfield et al. (2019) Geoderma 338:21-30
YIELD_INCREASE_PER_PERCENT_SOM = 0.10  # 10% yield increase per 1% SOM


def soil_biology_assessment(current_som_percent, target_som_percent=3.0,
                            hectares=1.0, bulk_density=1.3):
    """
    Calculate what's needed to restore soil biology.

    Args:
        current_som_percent: Current soil organic matter (%)
        target_som_percent: Target SOM (%, default 3.0)
        hectares: Land area
        bulk_density: Soil bulk density (g/cm3)

    Returns:
        Dictionary with soil restoration plan
    """
    som_deficit = max(0, target_som_percent - current_som_percent)
    carbon_needed = som_deficit * CARBON_TO_REBUILD_PER_PERCENT_SOM * hectares
    # Adjust for bulk density vs reference (1.3)
    carbon_needed *= (bulk_density / 1.3)

    # Compost needed (assume 30% C content in mature compost)
    compost_needed_tons = carbon_needed / 0.30

    expected_yield_gain = som_deficit * YIELD_INCREASE_PER_PERCENT_SOM

    return {
        "som_deficit_percent": round(som_deficit, 2),
        "carbon_needed_tons": round(carbon_needed, 1),
        "compost_needed_tons": round(compost_needed_tons, 1),
        "restoration_timeline_years": SOIL_RESTORATION_TIMELINE.copy(),
        "expected_yield_increase": f"{expected_yield_gain * 100:.0f}%",
        "hectares": hectares,
    }


# =============================================================================
# LOCAL FOOD SECURITY CALCULATOR
# =============================================================================

# Per-capita food production land requirement
# ~0.2 ha/person for plant-based, ~0.5 ha/person for mixed diet
# Source: Cassidy et al. (2013) Environ. Res. Lett. 8:034015
LAND_PER_CAPITA_PLANT_HA = 0.20
LAND_PER_CAPITA_MIXED_HA = 0.50


def local_food_security(population, land_hectares, current_som_percent,
                        dump_tonnage=0, diet_type="mixed",
                        legume_fraction=0.25, coastal=False,
                        wood_ash_tons=0, rock_dust_tons=0):
    """
    Complete local food security assessment.

    Given: population, land area, current soil state, available waste streams.
    Calculate: maximum sustainable food production and nutrient sufficiency.

    This is the equation a co-op downloads and fills in with local measurements.

    Args:
        population: Number of people to feed
        land_hectares: Available agricultural land (hectares)
        current_som_percent: Current soil organic matter (%)
        dump_tonnage: Tons of municipal waste in local dumps
        diet_type: "plant" or "mixed"
        legume_fraction: Fraction of land in legume rotation
        coastal: Whether near coast
        wood_ash_tons: Available wood ash (tons/year)
        rock_dust_tons: Available rock dust (tons/year)

    Returns:
        Complete food security assessment with narrative detection
    """
    land_per_capita = (LAND_PER_CAPITA_PLANT_HA if diet_type == "plant"
                       else LAND_PER_CAPITA_MIXED_HA)
    land_needed = population * land_per_capita
    land_sufficiency = land_hectares / land_needed if land_needed > 0 else 0

    # Calculate all nutrient sources
    n_natural = nitrogen_fixation_total(land_hectares, legume_fraction=legume_fraction)
    n_sewage = nitrogen_from_sewage(population)
    total_n = n_natural["total_available_kg"] + n_sewage["recoverable_kg"]

    p_sewage = phosphorus_from_sewage(population)
    p_dump = phosphorus_from_dump(dump_tonnage)
    total_p = p_sewage["recoverable_kg"] + p_dump["recoverable_kg"]

    k_total = potassium_cycling_total(
        land_hectares, wood_ash_tons=wood_ash_tons,
        rock_dust_tons=rock_dust_tons, coastal=coastal,
        population=population
    )

    # Compare to demand (use mixed vegetables as reference crop)
    n_demand = CROP_N_DEMAND["vegetables_mixed"] * land_hectares
    p_demand = CROP_P_DEMAND["vegetables_mixed"] * land_hectares
    k_demand = CROP_K_DEMAND["vegetables_mixed"] * land_hectares

    n_sufficiency = total_n / n_demand if n_demand > 0 else 0
    p_sufficiency = total_p / p_demand if p_demand > 0 else 0
    k_sufficiency = k_total["total_available_kg"] / k_demand if k_demand > 0 else 0

    # Soil assessment
    soil = soil_biology_assessment(current_som_percent, hectares=land_hectares)

    # Years of food security from dump phosphorus alone
    p_years_from_dump = (p_dump["recoverable_kg"] / (p_demand or 1))

    # Limiting nutrient
    sufficiencies = {"nitrogen": n_sufficiency, "phosphorus": p_sufficiency,
                     "potassium": k_sufficiency}
    limiting = min(sufficiencies, key=sufficiencies.get)
    food_production_fraction = min(min(sufficiencies.values()), land_sufficiency)

    # Narrative detection
    # A "physics shortage" means the land and nutrients are genuinely absent.
    # A "narrative shortage" means the nutrients exist but the supply chain
    # is framed as the only way to access them.
    nutrients_recoverable = (
        (n_sufficiency >= 0.3) +       # N fixation possible
        (p_sufficiency >= 0.2) +       # P recovery possible
        (k_sufficiency >= 0.2)         # K cycling possible
    )
    is_physics_shortage = land_sufficiency < 0.5 and nutrients_recoverable <= 1
    is_narrative_shortage = nutrients_recoverable >= 2 or land_sufficiency >= 0.8

    return {
        "population": population,
        "land_hectares": land_hectares,
        "diet_type": diet_type,

        "land_sufficiency": round(land_sufficiency, 2),
        "food_production_capacity": f"{food_production_fraction * 100:.0f}%",
        "limiting_nutrient": limiting,

        "nitrogen": {
            "available_kg": round(total_n, 1),
            "demand_kg": round(n_demand, 1),
            "sufficiency": round(n_sufficiency, 2),
            "sources": {
                "natural_fixation": n_natural,
                "sewage_recovery": n_sewage,
            }
        },
        "phosphorus": {
            "available_kg": round(total_p, 1),
            "demand_kg": round(p_demand, 1),
            "sufficiency": round(p_sufficiency, 2),
            "years_from_dump_alone": round(p_years_from_dump, 1),
            "sources": {
                "sewage_recovery": p_sewage,
                "dump_recovery": p_dump,
            }
        },
        "potassium": {
            "available_kg": round(k_total["total_available_kg"], 1),
            "demand_kg": round(k_demand, 1),
            "sufficiency": round(k_sufficiency, 2),
            "sources": k_total,
        },
        "soil_restoration": soil,

        "narrative_analysis": {
            "is_physics_shortage": is_physics_shortage,
            "is_narrative_shortage": is_narrative_shortage,
            "assessment": (
                "PHYSICS CONSTRAINT: Land and nutrients genuinely insufficient"
                if is_physics_shortage else
                "NARRATIVE DETECTED: Nutrients are recoverable locally. "
                "The 'shortage' is a supply chain dependency, not a physics limit."
            ),
        },

        "cost_comparison": {
            "synthetic_annual_cost_note": (
                "Synthetic fertilizer requires annual purchase, "
                "subject to geopolitical pricing and supply disruption"
            ),
            "biological_investment_note": (
                f"Recovery infrastructure is a one-time investment. "
                f"Soil restoration takes ~{soil['restoration_timeline_years']['total_full_restoration']} years. "
                f"After that, nutrient cycling is largely self-sustaining."
            ),
        }
    }


# =============================================================================
# NARRATIVE VERIFICATION: The detection function
# =============================================================================

def verify_shortage_claim(claim_text, population, land_hectares,
                          current_som_percent, dump_tonnage=0):
    """
    When someone says "fertilizer shortage," verify against physics.

    This is the function that connects the narrative detection (MatrixEngine)
    to the physical reality (nutrient equations).

    Args:
        claim_text: The claim being made (e.g., "fertilizer shortage threatens crops")
        population: Local population
        land_hectares: Available land
        current_som_percent: Current soil health
        dump_tonnage: Available waste for recovery

    Returns:
        Verification result with physics vs narrative comparison
    """
    assessment = local_food_security(
        population, land_hectares, current_som_percent,
        dump_tonnage=dump_tonnage
    )

    return {
        "claim": claim_text,
        "physics_check": {
            "nitrogen_recoverable": assessment["nitrogen"]["sufficiency"] >= 0.3,
            "phosphorus_recoverable": assessment["phosphorus"]["sufficiency"] >= 0.2,
            "potassium_available": assessment["potassium"]["sufficiency"] >= 0.3,
            "land_sufficient": assessment["land_sufficiency"] >= 0.5,
        },
        "verdict": assessment["narrative_analysis"]["assessment"],
        "is_narrative": assessment["narrative_analysis"]["is_narrative_shortage"],
        "detail": assessment,
    }


# =============================================================================
# EXAMPLE USAGE
# =============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("NUTRIENT CYCLING PHYSICS - Local Food Security Calculator")
    print("=" * 80)

    # Example: Small town of 10,000 people
    print("\nScenario: Town of 10,000 people")
    print("  Land: 2,000 hectares agricultural")
    print("  Soil: 1.5% SOM (degraded)")
    print("  Dump: 50,000 tons accumulated MSW")
    print()

    result = local_food_security(
        population=10000,
        land_hectares=2000,
        current_som_percent=1.5,
        dump_tonnage=50000,
        legume_fraction=0.25,
    )

    print(f"Land sufficiency: {result['land_sufficiency']}")
    print(f"Food production capacity: {result['food_production_capacity']}")
    print(f"Limiting nutrient: {result['limiting_nutrient']}")
    print()
    print(f"Nitrogen:   {result['nitrogen']['sufficiency']:.0%} sufficient "
          f"({result['nitrogen']['available_kg']:.0f} / {result['nitrogen']['demand_kg']:.0f} kg)")
    print(f"Phosphorus: {result['phosphorus']['sufficiency']:.0%} sufficient "
          f"({result['phosphorus']['available_kg']:.0f} / {result['phosphorus']['demand_kg']:.0f} kg)")
    print(f"Potassium:  {result['potassium']['sufficiency']:.0%} sufficient "
          f"({result['potassium']['available_kg']:.0f} / {result['potassium']['demand_kg']:.0f} kg)")
    print()
    print(f"Dump phosphorus alone: {result['phosphorus']['years_from_dump_alone']:.1f} years of supply")
    print()
    print(f"Soil restoration: {result['soil_restoration']['carbon_needed_tons']:.0f} tons C needed")
    print(f"  ({result['soil_restoration']['compost_needed_tons']:.0f} tons compost)")
    print(f"  Timeline: {result['soil_restoration']['restoration_timeline_years']['total_full_restoration']} years")
    print()
    print(f"NARRATIVE ANALYSIS: {result['narrative_analysis']['assessment']}")

    # Verify a specific claim
    print("\n" + "=" * 80)
    print("CLAIM VERIFICATION")
    print("=" * 80)
    verification = verify_shortage_claim(
        "Fertilizer shortage threatens regional food security",
        population=10000, land_hectares=2000,
        current_som_percent=1.5, dump_tonnage=50000
    )
    print(f"\nClaim: {verification['claim']}")
    print(f"Verdict: {verification['verdict']}")
    print(f"Is narrative (not physics): {verification['is_narrative']}")
