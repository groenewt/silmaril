import csv
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parents[1]


def test_catalog_gaps_preserves_canonical_gap_and_document_ids(tmp_path: Path) -> None:
    repository = tmp_path / "repository"
    table_root = repository / "library_cache/tables"
    table_root.mkdir(parents=True)
    rows = [
      {
        "gap_id": "gap_id-0-b",
        "doc_id": "doc_id-1-b",
        "category": "category-2-b",
        "severity": "severity-3-b",
        "gap_text": "gap_text-4-b",
        "source_locator": "source_locator-5-b",
        "matched_terms": "matched_terms-6-b",
      },
      {
        "gap_id": "gap_id-0-a",
        "doc_id": "doc_id-1-a",
        "category": "category-2-a",
        "severity": "severity-3-a",
        "gap_text": "gap_text-4-a",
        "source_locator": "source_locator-5-a",
        "matched_terms": "matched_terms-6-a",
      },
    ]
    rows[0]["doc_id"] = "b-0"
    rows[0]["gap_id"] = "b-1"
    rows[1]["doc_id"] = "a-0"
    rows[1]["gap_id"] = "a-1"
    source = table_root / "gaps.csv"
    with source.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=tuple(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    output_root = tmp_path / "output"
    completed = subprocess.run(
        (
            "make",
            "-f",
            "make/morphism/codebase/volume/inventory_catalog_gaps.mk",
            "volume-inventory-catalog-gaps",
            f"SILMARIL_PYTHON={sys.executable}",
            f"SILMARIL_PYLIB_SOURCE_ROOT={ROOT / 'src'}",
            f"VOLUME_REPOSITORY={repository}",
            f"VOLUME_INVENTORY_CATALOG_GAPS_OUTPUT_ROOT={output_root}",
        ),
        capture_output=True,
        check=False,
        cwd=ROOT,
    )
    with (output_root / "catalog_gaps.csv").open(
        encoding="utf-8", newline=""
    ) as stream:
        projected_rows = tuple(csv.DictReader(stream))

    assert completed.returncode == 0, completed.stderr
    assert completed.stderr == b""
    assert projected_rows == tuple(
        sorted(rows, key=lambda row: (row["doc_id"], row["gap_id"]))
    )
    assert (output_root / "relation.duckdb").is_file()
    assert (output_root / "projection.receipt").is_file()
    assert (output_root / "canonical-order.receipt").is_file()
