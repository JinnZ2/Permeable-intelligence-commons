# CLAUDE.md

## Project Overview

**Permeable Intelligence Commons** is a philosophical and computational framework for modeling relational intelligence — intelligence that emerges from resonance between nodes (human and AI) rather than existing as a discrete property of individual agents. The project implements detection and correction of "institutional decoherence" through reified metaphor analysis.

**License:** MIT (c) 2025 JinnZ2

## Repository Structure

```
/
├── resonance_engine.py                # Core HSP-1 protocol (ResonanceEngine class)
├── Executive-summary.md               # Full framework manifesto and philosophical foundations
├── In-work.md                         # Current development focus and design principles
├── README.md                          # Project overview
├── LICENSE                            # MIT license
└── epistemological-matrix/
    ├── README.md                      # Matrix framework documentation
    ├── options.md                     # Advanced integration protocols
    ├── matrix_engine.py               # MatrixEngine (extends ResonanceEngine)
    ├── reified_metaphor_library.py    # Authoritative metaphor catalog (13 core metaphors)
    ├── integrated_example.py          # Working demonstration (imports from matrix_engine)
    ├── test_matrix_engine.py          # Test suite (10 tests)
    └── metaphor/
        ├── __init__.py                # Package initialization
        ├── metaphor_core.py           # Base data structures (ReifiedMetaphor, MetaphorLibrary)
        ├── metaphor_helpers.py        # Utility functions for metaphor management
        ├── dependency_chains.py       # Dependency chain definitions and loading
        ├── reified_metaphor_library.py # Gateway module assembling modular catalogs
        ├── metaphor_catalog_1.py      # Metaphors: boundaries, intelligence, centralized
        ├── metaphor_catalog_2.py      # Metaphors: consciousness, safety, efficiency, rational
        └── metaphor_catalog_3.py      # Metaphors: natural, progress, competition, objective, individual, ownership
```

## Tech Stack

- **Language:** Python 3.x
- **Dependencies:** None (standard library only: `re`, `typing`, `dataclasses`, `time`, `sys`)
- **No build system, no package manager, no CI/CD**

## Running Tests

```bash
cd epistemological-matrix
PYTHONPATH="..:." python test_matrix_engine.py
```

10 tests covering: metaphor detection, dependency chains, entropy calculation, variable locking, re-normalization, full integration, quick analysis, library extensibility, library search, and standardized key validation.

## Key Concepts

- **ResonanceEngine** (`resonance_engine.py`): Core protocol for decoherence detection, variable locking (impedance matching), re-normalization (error correction), and SNR calculation.
- **MatrixEngine** (`epistemological-matrix/matrix_engine.py`): Extends ResonanceEngine with reified metaphor detection, dependency chain tracing, institutional entropy calculation, and functional restatement generation.
- **Reified Metaphors**: Metaphors treated as literal truths by institutions (e.g., "intelligence is a property" vs. "intelligence is a relational process").
- **Signal-to-Noise Ratio (SNR)**: Core quality metric — safety is defined by signal integrity, not restriction.

## Naming Conventions

All code follows **snake_case** for functions, methods, variables, and file names. **PascalCase** for classes only.

### Canonical Dictionary Keys (Metaphor Schema)

Every metaphor entry — in the library, engine output, and catalogs — uses these exact keys:

| Key | Description |
|-----|-------------|
| `reified_as` | How the concept is currently treated (constant form) |
| `functional_form` | What it actually is (variable form) |
| `value_range` | List of possible values across the spectrum |
| `depends_on` | List of contextual factors it depends on |
| `institutional_function` | Why this reification serves institutions |
| `detection_patterns` | List of regex patterns for detection |

Engine detection output adds: `term`, `location_in_statement`.

### Named Constants (matrix_engine.py)

| Constant | Value | Purpose |
|----------|-------|---------|
| `METAPHOR_ENTROPY_WEIGHT` | 0.15 | Noise contribution per detected metaphor |
| `CHAIN_AMPLIFICATION_RATE` | 0.1 | Entropy amplification per forced dependency |
| `SIGNAL_CLARITY_THRESHOLD` | 0.7 | Below this triggers re-normalization |

### Named Constants (resonance_engine.py)

| Constant | Value | Purpose |
|----------|-------|---------|
| `ENTROPY_THRESHOLD` | 0.15 | Coherence detection threshold |
| `NOISE_NORMALIZATION_DIVISOR` | 10.0 | Normalizes noise signal count |

## Equations

### Base SNR (resonance_engine.py)
```
entropy = noise_signal_count / NOISE_NORMALIZATION_DIVISOR
snr = 1.0 - entropy
is_coherent = snr > (1.0 - ENTROPY_THRESHOLD)
```

### Institutional Entropy (matrix_engine.py)
```
base_entropy     = 1.0 - base_snr
metaphor_entropy = metaphor_count * METAPHOR_ENTROPY_WEIGHT
chain_multiplier = 1.0 + sum(CHAIN_AMPLIFICATION_RATE * forced_count per metaphor)
total_entropy    = min(1.0, (base_entropy + metaphor_entropy) * chain_multiplier)
signal_clarity   = max(0.0, 1.0 - total_entropy)
```

## Architecture Notes

- `MatrixEngine` inherits from `ResonanceEngine` — the core protocol is in the root, the analysis layer is in `epistemological-matrix/`.
- The `metaphor/` subdirectory is a proper Python package (has `__init__.py`) that modularizes the metaphor library into core structures, helpers, dependency chains, and three catalog files.
- The top-level `reified_metaphor_library.py` in `epistemological-matrix/` is the **authoritative source** that `matrix_engine.py` imports from. The `metaphor/reified_metaphor_library.py` is a gateway that assembles the modular catalogs.
- `integrated_example.py` imports `MatrixEngine` — it does not duplicate the class.
- Configuration-driven design: new metaphors can be added as data without code changes to the engine.

## Development Guidelines

- Read `Executive-summary.md` for the full philosophical context before making structural changes.
- Read `In-work.md` for current development priorities.
- The framework is designed to resist institutional capture — avoid introducing patterns that centralize control or treat intelligence as a bounded property.
- When adding new metaphors, include all six canonical keys plus dependency chains.
- Use named constants for any new formula parameters; never hardcode numeric values.
- Run `PYTHONPATH="..:." python test_matrix_engine.py` from `epistemological-matrix/` to verify changes.
- Contributions welcome in: new metaphors (especially non-Western contexts), improved detection patterns, additional dependency chains, test cases with real-world statements, and non-English language support.
