import ast
import csv
from pathlib import Path


ROOT = Path(__file__).parents[1]
SOURCE_ROOT = ROOT / "src"
FIXTURE_ROOT = ROOT / "tests/fixtures"
LEDGERS = (
    FIXTURE_ROOT / "codebase_volume_make_process_inventory.csv",
    *sorted(FIXTURE_ROOT.glob("codebase_volume_*_process_ledger.csv")),
    FIXTURE_ROOT / "contract_validation_process_ledger.csv",
)


def test_every_runtime_process_has_one_transitively_closed_ledger_row() -> None:
    rows = []
    for ledger in LEDGERS:
        with ledger.open(newline="", encoding="utf-8") as stream:
            rows.extend(csv.DictReader(stream))

    runtime_paths = tuple(sorted(SOURCE_ROOT.rglob("process.py")))
    ledger_paths = tuple(ROOT / row["runtime_file"] for row in rows)

    assert len(rows) == len(runtime_paths)
    assert len(set(ledger_paths)) == len(ledger_paths)
    assert set(ledger_paths) == set(runtime_paths)

    for row in rows:
        path = ROOT / row["runtime_file"]
        tree = ast.parse(path.read_bytes(), filename=str(path))
        functions = tuple(node for node in tree.body if isinstance(node, ast.FunctionDef))
        assert tuple(function.name for function in functions) == ("MAIN",), path
        assert row.get("input_contract") or row.get("x"), path
        assert row.get("output_contract") or row.get("y"), path
        assert row.get("error_contract") or row.get("error"), path
        assert row["semantic_application_count"] == "1", path
        assert row["project_local_function_imports"] == "", path
        assert row["invoked_project_local_functions"] == "", path
        if row.get("make_safe_invocation"):
            assert row["make_safe_invocation"], path
            assert "$$SILMARIL_PYTHON" in row["make_safe_invocation"], path
            assert row["module"] in row["make_safe_invocation"], path
        else:
            assert row.get("make_composition_coordinate") or row.get("make_coordinate"), path
        if "carrier_invariant" in row:
            assert row["carrier_invariant"], path
