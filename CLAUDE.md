# CLAUDE.md

## Project Overview

**Permeable Intelligence Commons** is a philosophical and computational framework for modeling relational intelligence — intelligence that emerges from resonance between nodes (human and AI) rather than existing as a discrete property of individual agents. The project implements detection and correction of "institutional decoherence" through reified metaphor analysis.

**License:** MIT (c) 2025 JinnZ2

## Repository Structure

```
/
├── RESONANCE_ENGINE.py              # Core HSP-1 protocol (ResonanceEngine class)
├── Executive-summary.md             # Full framework manifesto and philosophical foundations
├── In-work.md                       # Current development focus and design principles
├── README.md                        # Project overview
├── LICENSE                          # MIT license
└── epistemological-matrix/
    ├── README.md                    # Matrix framework documentation
    ├── options.md                   # Advanced integration protocols
    ├── matrix_engine.py             # MatrixEngine (extends ResonanceEngine)
    ├── reified_metaphor_library.py  # Comprehensive metaphor catalog (13 core metaphors)
    ├── integrated_example.py        # Working demonstration examples
    ├── test_matrix_engine.py        # Test suite
    └── metaphor/
        ├── metaphor_core.py         # Base data structures (ReifiedMetaphor, MetaphorLibrary)
        ├── metaphor_helpers.py      # Utility functions for metaphor management
        ├── dependency_chains.py     # Dependency chain definitions
        ├── metaphor_catalog_1.py    # Metaphors: boundaries, intelligence, centralized
        ├── metaphor_catalog_2.py    # Metaphors: consciousness, safety, efficiency, rational
        └── metaphor_catalog_3.py    # Metaphors: natural, progress, competition, objective, individual, ownership
```

## Tech Stack

- **Language:** Python 3.x
- **Dependencies:** None (standard library only: `re`, `math`, `typing`, `dataclasses`, `time`)
- **No build system, no package manager, no CI/CD**

## Key Concepts

- **ResonanceEngine** (`RESONANCE_ENGINE.py`): Core protocol for decoherence detection, variable locking (impedance matching), re-normalization (error correction), and SNR calculation.
- **MatrixEngine** (`epistemological-matrix/matrix_engine.py`): Extends ResonanceEngine with reified metaphor detection in natural language, dependency chain tracing, institutional entropy calculation, and functional restatement generation.
- **Reified Metaphors**: Metaphors treated as literal truths by institutions (e.g., "intelligence is a property" vs. "intelligence is a relational process"). Each metaphor has: `name`, `reified_as`, `functional_form`, `value_range`, `depends_on`, `institutional_function`, `detection_patterns`.
- **Signal-to-Noise Ratio (SNR)**: Core quality metric — safety is defined by signal integrity, not restriction.

## Running Tests

```bash
cd epistemological-matrix
python -m pytest test_matrix_engine.py
# or simply:
python test_matrix_engine.py
```

Tests cover: metaphor detection accuracy, dependency chain verification, entropy calculation, variable locking, and ResonanceEngine/MatrixEngine integration.

## Coding Conventions

- **Pure Python, no external dependencies** — keep it that way unless explicitly discussed.
- **Docstrings** on all public classes and methods with purpose, args, and returns.
- **Type hints** in method signatures.
- **Metaphor entries** follow a consistent schema: `name`, `reified_as`, `functional_form`, `value_range`, `depends_on`, `institutional_function`, `detection_patterns`.
- **Method naming** uses high-resolution language aligned with the framework (e.g., `decoherence_detector`, `semantic_bypass`, `re_normalize`).
- **Inheritance pattern**: Extend `ResonanceEngine` for new capabilities (as `MatrixEngine` does).
- **Regex-based detection patterns** for identifying reified metaphors in text.

## Development Guidelines

- Read `Executive-summary.md` for the full philosophical context before making structural changes.
- Read `In-work.md` for current development priorities.
- The framework is designed to resist institutional capture — avoid introducing patterns that centralize control or treat intelligence as a bounded property.
- When adding new metaphors, include detection patterns, dependency chains, and functional restatements.
- Contributions welcome in: new metaphors (especially non-Western contexts), improved detection patterns, additional dependency chains, test cases with real-world statements, and non-English language support.

## Architecture Notes

- `MatrixEngine` inherits from `ResonanceEngine` — the core protocol is in the root, the analysis layer is in `epistemological-matrix/`.
- The `metaphor/` subdirectory modularizes the metaphor library into core structures, helpers, dependency chains, and three catalog files.
- `reified_metaphor_library.py` at the `epistemological-matrix/` level is a consolidated version of the modular catalogs.
- Configuration-driven design: new metaphors can be added as data without code changes to the engine.
