import csv
from pathlib import Path


ROOT = Path(__file__).parents[1]
ARROW_ROOT = ROOT / "src/silmaril/sparky/morphism/codebase/volume"
FIXTURE_ROOT = ROOT / "tests/fixtures"
INVENTORIES = (
    FIXTURE_ROOT / "codebase_volume_make_process_inventory.csv",
    *sorted(FIXTURE_ROOT.glob("codebase_volume_*_process_ledger.csv")),
)
EXCLUDED = ROOT / "tests/fixtures/codebase_volume_make_process_exclusions.csv"
_MAKE_OWNED_COORDINATES = {
    "application/step",
    "cli/exit/status",
    "cli/stderr/write",
    "cli/stdin/read",
    "cli/stdout/write",
    "request/capture",
}


def test_make_process_inventory_covers_every_non_control_arrow() -> None:
    rows = []
    for inventory in INVENTORIES:
        with inventory.open(newline="", encoding="utf-8") as stream:
            rows.extend(csv.DictReader(stream))
    with EXCLUDED.open(newline="", encoding="utf-8") as stream:
        exclusions = tuple(csv.DictReader(stream))

    process_coordinates = {
        path.relative_to(ARROW_ROOT).parent.as_posix()
        for path in ARROW_ROOT.rglob("process.py")
    }
    excluded_coordinates = {row["coordinate"] for row in exclusions}

    coordinates = {
        Path(row["runtime_file"]).relative_to(
            "src/silmaril/sparky/morphism/codebase/volume"
        ).parent.as_posix()
        for row in rows
    }

    assert len(rows) == len(coordinates)
    assert coordinates == process_coordinates
    assert excluded_coordinates == _MAKE_OWNED_COORDINATES
    assert not process_coordinates & excluded_coordinates
    assert all(
        row["module"]
        == "silmaril.sparky.morphism.codebase.volume."
        + Path(row["runtime_file"]).relative_to(
            "src/silmaril/sparky/morphism/codebase/volume"
        ).parent.as_posix().replace("/", ".")
        + ".process"
        for row in rows
    )
    generic_rows = tuple(row for row in rows if row.get("make_safe_invocation"))
    exact_rows = tuple(row for row in rows if row.get("make_coordinate"))
    assert all("$$TEMP_OUTPUT" in row["make_safe_invocation"] for row in generic_rows)
    assert all("$$ERROR_OUTPUT" in row["make_safe_invocation"] for row in generic_rows)
    assert all(
        'PYTHONPATH="$$SILMARIL_PYLIB_SOURCE_ROOT"'
        in row["make_safe_invocation"]
        for row in generic_rows
    )
    assert all(
        '"$$SILMARIL_PYTHON" -m ' in row["make_safe_invocation"]
        for row in generic_rows
    )
    assert all(
        row["make_safe_invocation"].startswith("set +e; ")
        for row in generic_rows
    )
    assert all(
        "; STATUS=$$?; set -e; " in row["make_safe_invocation"]
        for row in generic_rows
    )
    assert all(
        'cat "$$ERROR_OUTPUT" >&2; exit "$$STATUS"; fi'
        in row["make_safe_invocation"]
        for row in generic_rows
    )
    assert all(row["x"] and row["f"] and row["y"] and row["error"] for row in exact_rows)
    assert all(row["make_coordinate"] for row in exact_rows)
    assert all(row["carrier_invariant"] for row in exact_rows)
