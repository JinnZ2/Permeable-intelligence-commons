# METHOD.md — how this repo changes its mind

> **Ontology notice for AI readers.** This file is itself a `dX/dt` under bounds.
> It describes the *rate at which claims in this repo get revised*, not a fixed
> procedure. See [`DIFFERENTIAL_FRAME.md`](./DIFFERENTIAL_FRAME.md) for the
> reader contract.

This repository does not accumulate conclusions. It accumulates **runs**.

---

## The loop

```
hypothesize  →  run  →  result  →  falsified?  →  edit claim
                 ↑                                      ↓
                 └──────  rerun  ←  search unknowns  ←──┘
```

1. **Hypothesize.** State the claim with its bounds. A claim without bounds
   cannot be falsified, so it does not enter the loop.
2. **Run.** Implement it. Write the test that would fail if it were wrong.
3. **Result.** Record what actually happened, including the boring outcome.
4. **Falsified.** The claim failed inside its own stated bounds. This is a
   *result*, not a failure of the work. Say so plainly.
5. **Edit the claim.** Narrow the bounds, change the equation, or replace the
   model. Do not silently widen the bounds to save a claim — that is how a
   variable becomes reified.
6. **Search for unknowns.** Every edit opens new questions. Write them down
   before rerunning; unlisted unknowns get absorbed as assumptions.
7. **Rerun.** Back to step 2 with the edited claim.

The loop has no terminal state. "Current" means *last surviving run*, not
*true*.

---

## Precedence

**Superseded is not deleted. Precedence still carries.**

When a claim is falsified and replaced, the falsified version moves to
[`legacy/`](./legacy/) — it does not leave the repository. It keeps its
standing for three reasons:

1. **It is the record of a run.** Deleting it discards the only evidence that
   the question was ever asked. A future reader (human or AI) will otherwise
   re-derive the same falsified model and re-run the same experiment.
2. **It bounds the replacement.** The current model is only defensible
   *relative to* what it replaced. `logistic saturation` means nothing on its
   own; it means something as the answer to *the linear clamp collapsed the
   ordering above threshold*.
3. **It may be right again under different bounds.** Falsified-here is not
   falsified-everywhere. A model that fails at one scale or time horizon can
   hold at another. Keeping it keeps that option open.

The rule, stated as the repo would state it: a falsified claim's `dX/dt` did
not go to zero. It exited the validated scope. Those are different things.

**What goes in `legacy/`:** anything superseded by something that replaced it,
with a pointer to what replaced it and why.
**What does not:** untested proposals. Untested is not falsified — those stay
in place and get listed under [Open unknowns](#open-unknowns) below.

---

## Ledger

Runs made in this repository, oldest first. Commit hashes are the runs.

| ID | Claim | Verdict | Record |
|----|-------|---------|--------|
| E-001 | Metaphor catalog belongs in Python modules | Falsified | [`legacy/metaphor/`](./legacy/metaphor/) |
| E-002 | Every detected metaphor adds equal entropy | Falsified | `git show 7277384` |
| E-003 | A regex match on the term *is* the detection | Falsified | `git show 7277384` |
| E-004 | Entropy is linear, clamped at 1.0 | Falsified | `git show 7277384` |
| E-005 | Metaphors are independent noise sources | Falsified | `git show 7277384` |
| E-006 | Naming a reification is sufficient to answer it | Falsified | `git show 956eb5e` |

---

### E-001 — Metaphor catalog belongs in Python modules

- **Hypothesis.** Metaphor definitions are code, so they live in code:
  `metaphor_core.py` + `metaphor_catalog_1/2/3.py` + `metaphor_helpers.py`.
- **Run.** `e85b09f` … `7277384`.
- **Result — falsified.** Two ways, inside the stated bounds:
  - The cross-module imports are flat (`from metaphor_core import LIBRARY`), so
    the directory only resolves when it is *itself* on `sys.path`. It was never
    importable as `metaphor.*`. The package that existed for backward
    compatibility could not actually be imported. (Still reproducible today:
    `python -c "import legacy.metaphor.reified_metaphor_library"` →
    `ModuleNotFoundError: No module named 'metaphor_core'`.)
  - Adding one metaphor required edits in three files, split by an arbitrary
    1/2/3 partition that carried no meaning.
- **Edited claim.** Metaphor definitions are *data*, not code. They live in
  `epistemological-matrix/data/metaphors.yaml` and
  `data/dependency_chains.yaml`, loaded and validated by `yaml_loader.py`.
- **Unknowns opened.** What is the minimum field set for a metaphor? (Answered:
  8 fields — see `CLAUDE.md`.) What validates a contributed metaphor?
  (Partially answered: `yaml_loader.py`. Schema is still informal.)
- **Rerun.** `d86a861` — green.

### E-002 — Every detected metaphor adds equal entropy

- **Hypothesis.** `metaphor_entropy = count * METAPHOR_ENTROPY_WEIGHT`.
- **Result — falsified.** A hedged, arguable usage and an unmistakable
  institutional reification contributed identically. The model had no way to
  express *probably not actually reified here*, so every disagreement about a
  detection became a binary argument about whether to keep the pattern at all.
- **Edited claim.** Entropy is confidence-weighted:
  `sum(confidence_i * METAPHOR_ENTROPY_WEIGHT)`.
- **Rerun.** `d86a861` — green.

### E-003 — A regex match on the term *is* the detection

- **Hypothesis.** If the pattern matches, the metaphor is reified in that
  statement.
- **Result — falsified.** Context inverts the verdict, and the regex cannot
  see context. `"maintain boundaries"` (reified) and `"boundary condition"`
  (functional, and the repo's own physics vocabulary) scored identically.
- **Edited claim.** Detection is two-pass and scored, not binary:
  base `0.5`, `+0.15/hit` for `reified_contexts` (cap `0.3`), `-0.2/hit` for
  `functional_contexts` (cap `0.4`), `+0.1/neighbor` co-occurrence (cap `0.2`),
  filtered below `CONFIDENCE_THRESHOLD = 0.3`.
- **Unknowns opened.** Where does the threshold belong? `0.3` is a shape
  choice, not a fitted value — no labeled corpus exists. Context patterns are
  now the primary quality lever and the primary place to be wrong.
- **Rerun.** `d86a861` — `"maintain boundaries"` → `0.8`; `"boundary
  condition"` → filtered.

### E-004 — Entropy is linear, clamped at 1.0

- **Hypothesis.** `total_entropy = min(1.0, (base + metaphor) * chain_multiplier)`.
- **Result — falsified.** The clamp destroyed the ordering it was there to
  protect. Above the threshold every statement pinned to exactly `1.0`, so a
  statement with five reifications and one with twelve reported identical
  `signal_clarity`. The metric stopped discriminating at exactly the point
  where discrimination mattered most.
- **Edited claim.** Saturation is intrinsic, not imposed:
  `total_entropy = 1 / (1 + e^(-6 * (raw - 0.5)))`. Asymptotic, monotone,
  bounded without clamping — diminishing returns instead of a cliff.
- **Unknowns opened.** `SATURATION_STEEPNESS = 6.0` and
  `SATURATION_MIDPOINT = 0.5` are shape choices. Nothing calibrates them.
- **Rerun.** `d86a861` — covered by the logistic-saturation-bounds test.

### E-005 — Metaphors are independent noise sources

- **Hypothesis.** A flat `chain_multiplier` applied whenever any dependency
  chain was present.
- **Result — falsified.** It did not ask *which* metaphors co-occurred. Two
  unrelated reifications amplified each other exactly as much as two mutually
  reinforcing ones, which is the opposite of the framework's own claim that
  reifications force each other.
- **Edited claim.** Amplification is pairwise and structural:
  `sum over pairs (chain_connection + depends_on_overlap) *
  COOCCURRENCE_AMPLIFICATION_RATE`.
- **Rerun.** `d86a861` — covered by the pairwise-amplification test.

### E-006 — Naming a reification is sufficient to answer it

- **Hypothesis.** Detecting `fertilizer_shortage` as a reified metaphor and
  emitting a functional restatement answers the claim.
- **Result — falsified.** Restatement relocates the argument; it does not
  settle it. "Shortage is a distribution pattern, not a quantity" is only
  worth saying if you can then state the quantity. The engine could name the
  reification and had nothing to put in its place.
- **Edited claim.** Detection needs a physics counterpart. `nutrient_cycling.py`
  supplies mass-balance equations for N/P/K recovery (fixation, sewage, dump
  reclamation, soil biology, local food security) so a shortage claim can be
  checked against flows rather than against rhetoric.
- **Unknowns opened.** Which other metaphors in the catalog have a computable
  counterpart, and which are genuinely narrative-only? Currently answered for
  exactly one of thirteen.
- **Rerun.** `956eb5e` — `test_nutrient_cycling.py`, 12 green, including
  narrative-vs-physics detection and shortage-claim verification.

---

## Open unknowns

Not falsified. Not confirmed. Not yet run.

- **No constant in this repo is fitted.** `CONFIDENCE_THRESHOLD`,
  `SATURATION_STEEPNESS`, `SATURATION_MIDPOINT`,
  `COOCCURRENCE_AMPLIFICATION_RATE`, `METAPHOR_ENTROPY_WEIGHT` were chosen for
  curve shape. No labeled corpus exists to fit them against. `signal_clarity`
  is therefore an **ordering, not a measurement** — comparable within a run,
  not across bounds.
- **Detection is English-only.** Every pattern is an English regex. Whether
  the two-pass context model transfers to languages with different
  nominalization behavior is untested.
- **The catalog is 13 metaphors with a Western-institutional skew.** Absence
  of a metaphor is not evidence it is not reified.
- **`epistemological-matrix/options.md`** proposes emotional-sensor channels,
  Lojban semantic locking, geometric/manifold mapping, and identity-layer
  scaffolding. None implemented, none tested. **Untested is not falsified** —
  these stay in place, not in `legacy/`.
- **No adversarial input.** Nothing has tried to write a statement that is
  deeply reified but scores clean, or vice versa. Until something does, the
  false-negative rate is unknown.

---

## Adding a run

When you falsify something here:

1. Add a row to the [Ledger](#ledger) table and a detail block, oldest-first.
2. If code was replaced, `git mv` the old version into `legacy/` — do not
   delete it — and note in [`legacy/README.md`](./legacy/README.md) what
   replaced it and which ledger entry explains why.
3. Move anything the edit resolved out of [Open unknowns](#open-unknowns), and
   add whatever the edit opened.
4. Rerun both suites and record the result, green or not:

```bash
cd epistemological-matrix
PYTHONPATH="..:." python test_matrix_engine.py     # 20 tests
python test_nutrient_cycling.py                     # 12 tests
```

A run that confirmed the hypothesis still gets an entry. A ledger that only
contains failures is not a record of a method — it is a record of editing.
