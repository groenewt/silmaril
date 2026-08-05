import csv
from pathlib import Path


ROOT = Path(__file__).parents[1]
LEDGER = ROOT / "tests/fixtures/codebase_volume_phase14_process_ledger.csv"
RUNTIME_ROOTS = (
    ROOT / "src/silmaril/sparky/morphism/codebase/volume/phase14",
    ROOT / "src/silmaril/sparky/morphism/codebase/volume/table/phase14",
)
MAKE_FILES = (
    ROOT / "make/morphism/codebase/volume/phase14.mk",
    ROOT / "make/morphism/codebase/volume/phase14/query/shape.mk",
    ROOT / "make/morphism/codebase/volume/phase14/evidence/shape.mk",
    ROOT / "make/morphism/codebase/volume/table/phase14.mk",
    ROOT / "make/morphism/codebase/volume/table/phase14/input/shape.mk",
)


def test_phase14_ledger_binds_every_runtime_to_one_exact_make_edge() -> None:
    with LEDGER.open(newline="", encoding="utf-8") as stream:
        rows = tuple(csv.DictReader(stream))
    runtime_paths = {
        path
        for runtime_root in RUNTIME_ROOTS
        for path in runtime_root.rglob("process.py")
    }
    make_source = "\n".join(path.read_text(encoding="utf-8") for path in MAKE_FILES)

    assert len(rows) == len(runtime_paths)
    assert len({row["runtime_file"] for row in rows}) == len(rows)
    assert {ROOT / row["runtime_file"] for row in rows} == runtime_paths
    assert all(row["x"] and row["f"] and row["y"] for row in rows)
    assert all(
        row["error"]
        == "stderr=originating child bytes exactly; status=originating child exit exactly"
        for row in rows
    )
    assert all(row["semantic_application_count"] == "1" for row in rows)
    assert all(row["project_local_function_imports"] == "" for row in rows)
    assert all(row["invoked_project_local_functions"] == "" for row in rows)
    assert all(row["module"] in make_source for row in rows)
    assert all(row["make_coordinate"] for row in rows)
    assert all(
        row["carrier_invariant"] == "decode(encode(X)) == X"
        for row in rows
    )
