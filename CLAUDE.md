# CLAUDE.md

## Project Overview

**Permeable Intelligence Commons** is a philosophical and computational framework for modeling relational intelligence — intelligence that emerges from resonance between nodes (human and AI) rather than existing as a discrete property of individual agents. The project implements detection and correction of "institutional decoherence" through reified metaphor analysis with context-aware confidence scoring and interaction-aware entropy modeling.

**License:** MIT (c) 2025 JinnZ2

## Repository Structure

```
/
├── resonance_engine.py                # Core HSP-1 protocol (ResonanceEngine class)
├── requirements.txt                   # Python dependencies (pyyaml)
├── Executive-summary.md               # Full framework manifesto and philosophical foundations
├── In-work.md                         # Current development focus and design principles
├── README.md                          # Project overview
├── LICENSE                            # MIT license
└── epistemological-matrix/
    ├── data/
    │   ├── metaphors.yaml             # Canonical metaphor catalog (13 metaphors, YAML)
    │   └── dependency_chains.yaml     # Dependency chain definitions (YAML)
    ├── yaml_loader.py                 # YAML loading and validation
    ├── matrix_engine.py               # MatrixEngine (extends ResonanceEngine)
    ├── reified_metaphor_library.py    # Library interface (loads from YAML)
    ├── integrated_example.py          # Working demonstration
    ├── test_matrix_engine.py          # Test suite (17 tests)
    └── metaphor/                      # DEPRECATED - kept for backward compat
        ├── __init__.py                # Deprecation warning
        └── ...                        # Legacy modular catalog files
```

## Tech Stack

- **Language:** Python 3.x
- **Dependencies:** `pyyaml>=6.0` (see `requirements.txt`)
- **Install:** `pip install -r requirements.txt`

## Running Tests

```bash
cd epistemological-matrix
PYTHONPATH="..:." python test_matrix_engine.py
```

17 tests covering: metaphor detection, dependency chains, entropy calculation, variable locking, re-normalization, full integration, quick analysis, library extensibility, library search, standardized keys, reified/functional context scoring, co-occurrence boosting, confidence ranges, interaction-aware entropy fields, logistic saturation bounds, and pairwise amplification.

## Key Concepts

- **ResonanceEngine** (`resonance_engine.py`): Core protocol for decoherence detection, variable locking (impedance matching), re-normalization, and SNR calculation.
- **MatrixEngine** (`epistemological-matrix/matrix_engine.py`): Extends ResonanceEngine with context-aware metaphor detection, interaction-aware entropy, and functional restatement generation.
- **Reified Metaphors**: Metaphors treated as literal truths by institutions. Defined in `data/metaphors.yaml`.
- **Confidence Scoring**: Two-pass detection — base regex match + context analysis (reified boost, functional penalty, co-occurrence boost) produces a 0.0-1.0 confidence score per detection.
- **Logistic Entropy**: Non-linear saturation model replaces linear entropy. Accounts for pairwise metaphor interaction and diminishing returns.

## YAML Metaphor Schema

Metaphors are defined in `data/metaphors.yaml` with 8 fields:

| Field | Description |
|-------|-------------|
| `reified_as` | How the concept is currently treated (constant form) |
| `functional_form` | What it actually is (variable form) |
| `value_range` | List of possible values across the spectrum |
| `depends_on` | List of contextual factors it depends on |
| `institutional_function` | Why this reification serves institutions |
| `detection_patterns` | Regex patterns for base detection |
| `reified_contexts` | Regex patterns where the term IS reified (boosts confidence) |
| `functional_contexts` | Regex patterns where the term is used functionally (reduces confidence) |

To add a new metaphor, edit `data/metaphors.yaml` and add its dependency chain to `data/dependency_chains.yaml`.

## Named Constants

### Context-Aware Detection (matrix_engine.py)

| Constant | Value | Purpose |
|----------|-------|---------|
| `BASE_DETECTION_CONFIDENCE` | 0.5 | Starting confidence when base regex matches |
| `REIFIED_CONTEXT_BOOST_PER_HIT` | 0.15 | Boost per reified-context match |
| `REIFIED_CONTEXT_MAX_BOOST` | 0.3 | Cap on total reified boost |
| `FUNCTIONAL_CONTEXT_PENALTY_PER_HIT` | 0.2 | Penalty per functional-context match |
| `FUNCTIONAL_CONTEXT_MAX_PENALTY` | 0.4 | Cap on total functional penalty |
| `COOCCURRENCE_BOOST_PER_NEIGHBOR` | 0.1 | Boost per chain neighbor co-occurrence |
| `COOCCURRENCE_MAX_BOOST` | 0.2 | Cap on co-occurrence boost |
| `CONFIDENCE_THRESHOLD` | 0.3 | Below this, detection is filtered out |

### Entropy Model (matrix_engine.py)

| Constant | Value | Purpose |
|----------|-------|---------|
| `METAPHOR_ENTROPY_WEIGHT` | 0.15 | Noise contribution per metaphor (weighted by confidence) |
| `COOCCURRENCE_AMPLIFICATION_RATE` | 0.05 | Per chain-connection or depends_on overlap |
| `SATURATION_STEEPNESS` | 6.0 | Logistic curve steepness (k) |
| `SATURATION_MIDPOINT` | 0.5 | Logistic curve midpoint (x0) |
| `SIGNAL_CLARITY_THRESHOLD` | 0.7 | Below this triggers re-normalization |

### Base Engine (resonance_engine.py)

| Constant | Value | Purpose |
|----------|-------|---------|
| `ENTROPY_THRESHOLD` | 0.15 | Coherence detection threshold |
| `NOISE_NORMALIZATION_DIVISOR` | 10.0 | Normalizes noise signal count |

## Equations

### Confidence Scoring (per metaphor)
```
confidence = BASE (0.5)
           + min(0.3, reified_context_hits * 0.15)     # reified boost
           - min(0.4, functional_context_hits * 0.2)    # functional penalty
           + min(0.2, chain_neighbor_count * 0.1)       # co-occurrence boost
confidence = clamp(confidence, 0.0, 1.0)
if confidence < CONFIDENCE_THRESHOLD: filtered out
```

### Interaction-Aware Entropy
```
base_entropy           = 1.0 - base_snr
weighted_metaphor_ent  = sum(confidence_i * METAPHOR_ENTROPY_WEIGHT)
pair_amplification     = sum over pairs (chain_connection + depends_overlap) * 0.05
mutual_reinforcement   = 1.0 + pair_amplification
raw_entropy            = (base_entropy + weighted_metaphor_ent) * mutual_reinforcement
total_entropy          = 1 / (1 + e^(-6 * (raw_entropy - 0.5)))    # logistic saturation
signal_clarity         = 1.0 - total_entropy
```

### Base SNR (resonance_engine.py)
```
entropy     = noise_signal_count / 10.0
snr         = 1.0 - entropy
is_coherent = snr > (1.0 - 0.15)
```

## Architecture Notes

- `MatrixEngine` inherits from `ResonanceEngine`.
- Metaphor data lives in YAML (`data/`), loaded by `yaml_loader.py`, exported through `reified_metaphor_library.py`.
- `integrated_example.py` imports `MatrixEngine` — it does not duplicate the class.
- The `metaphor/` package is deprecated. It still works but emits a `DeprecationWarning`.
- Detection uses a two-pass algorithm: Pass 1 scores each metaphor individually, Pass 2 adds co-occurrence boosts.
- Entropy uses a logistic saturation curve ensuring asymptotic bounds without `min(1.0, ...)` clamping.

## Development Guidelines

- Read `Executive-summary.md` for philosophical context before structural changes.
- When adding metaphors, edit `data/metaphors.yaml` — include all 8 fields plus the dependency chain in `data/dependency_chains.yaml`.
- Use named constants for any formula parameters.
- Run `PYTHONPATH="..:." python test_matrix_engine.py` to verify changes (17 tests).
- Context patterns (`reified_contexts`, `functional_contexts`) are the primary lever for improving detection quality.
- Contributions welcome in: new metaphors (especially non-Western contexts), improved context patterns, additional dependency chains, and non-English language support.
