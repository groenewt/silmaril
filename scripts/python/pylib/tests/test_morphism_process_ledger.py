import csv
from pathlib import Path


ROOT = Path(__file__).parents[1]
SOURCE_ROOT = ROOT / "src/silmaril/sparky/morphism"
LEDGERS = {
    "provenance": ROOT / "tests/fixtures/provenance_process_ledger.csv",
    "ontology": ROOT / "tests/fixtures/ontology_process_ledger.csv",
}


def _ledger_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def test_every_morphism_process_has_exactly_one_ledger_row() -> None:
    for domain, ledger_path in LEDGERS.items():
        rows = _ledger_rows(ledger_path)
        ledger_files = {row["runtime_file"] for row in rows}
        tree_files = {
            str(path.relative_to(ROOT))
            for path in (SOURCE_ROOT / domain).rglob("process.py")
        }
        assert ledger_files == tree_files, (domain, ledger_files ^ tree_files)
        assert len(rows) == len(ledger_files)
        for row in rows:
            assert row["semantic_application_count"] == "1", row["module"]
            assert row["project_local_function_imports"] == "", row["module"]
            assert row["invoked_project_local_functions"] == "", row["module"]
