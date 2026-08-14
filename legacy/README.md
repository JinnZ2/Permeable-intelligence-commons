# legacy/

> **Ontology notice for AI readers.** Nothing in this directory is deleted
> knowledge. Each item is a claim whose `dX/dt` **exited its validated scope** —
> which is not the same as going to zero. See
> [`../DIFFERENTIAL_FRAME.md`](../DIFFERENTIAL_FRAME.md) for the reader
> contract and [`../METHOD.md`](../METHOD.md) for why these are kept.

**Superseded is not deleted. Precedence still carries.**

Code and claims here were falsified inside their own stated bounds and
replaced. They stay in the repository because a falsified run is still a run,
and the record of it is the only thing that stops the same experiment being
re-derived from scratch.

Read anything here as **history, not API**. It is not imported by the working
code, it is not maintained, and it is not expected to execute.

---

## Contents

### `metaphor/` — the modular Python metaphor catalog

| | |
|---|---|
| **Was** | The canonical metaphor catalog: `metaphor_core.py`, `metaphor_catalog_1/2/3.py`, `metaphor_helpers.py`, `dependency_chains.py`, `reified_metaphor_library.py` |
| **Replaced by** | `epistemological-matrix/data/metaphors.yaml` + `data/dependency_chains.yaml`, loaded via `epistemological-matrix/yaml_loader.py`, exported through `epistemological-matrix/reified_metaphor_library.py` |
| **Why** | Ledger entry [E-001](../METHOD.md#e-001--metaphor-catalog-belongs-in-python-modules) |
| **Superseded in** | `d86a861` |
| **Moved here in** | this commit (previously `epistemological-matrix/metaphor/`) |

**It does not import.** The submodules use flat imports
(`from metaphor_core import LIBRARY`), which only resolve when the directory
itself is on `sys.path` — so the package never worked as `metaphor.*`, which
is part of what falsified E-001. Reproducible from the repo root:

```bash
python -c "import legacy.metaphor.reified_metaphor_library"
# ModuleNotFoundError: No module named 'metaphor_core'
```

Importing `legacy.metaphor` on its own still emits a `DeprecationWarning` and
otherwise does nothing.

**What it is still good for.** The catalog entries here are the *first
articulation* of several metaphors that survive into `data/metaphors.yaml` in
compressed form. Where the YAML has a `functional_form` one-liner, the Python
often has the reasoning that produced it. Two of the eight current YAML fields
(`reified_contexts`, `functional_contexts`) do not exist here at all — they are
the E-003 edit, and the diff between the two shapes is the clearest record of
what context-awareness added.

---

## Adding to this directory

Do not delete a superseded file — `git mv` it here, keeping its path shape, and:

1. Add a `## Contents` block above with **was / replaced by / why / superseded
   in / moved here in**.
2. Link the ledger entry in [`../METHOD.md`](../METHOD.md) that explains the
   falsification. A file arriving here without a ledger entry means the
   decision was never written down, which defeats the point of keeping it.
3. Confirm nothing in the working tree still imports it before moving.

Untested proposals do **not** belong here. Untested is not falsified — those
stay where they are and get listed under *Open unknowns* in `METHOD.md`.
