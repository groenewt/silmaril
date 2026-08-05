import csv
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parents[1]


def test_catalog_quality_flags_preserves_canonical_flag_ids(tmp_path: Path) -> None:
    repository = tmp_path / "repository"
    table_root = repository / "library_cache/tables"
    table_root.mkdir(parents=True)
    rows = [
      {
        "flag_id": "flag_id-0-b",
        "doc_id": "doc_id-1-b",
        "flag": "flag-2-b",
        "severity": "severity-3-b",
        "reason": "reason-4-b",
      },
      {
        "flag_id": "flag_id-0-a",
        "doc_id": "doc_id-1-a",
        "flag": "flag-2-a",
        "severity": "severity-3-a",
        "reason": "reason-4-a",
      },
    ]
    rows[0]["doc_id"] = "b-0"
    rows[0]["flag"] = "b-1"
    rows[0]["flag_id"] = "b-2"
    rows[1]["doc_id"] = "a-0"
    rows[1]["flag"] = "a-1"
    rows[1]["flag_id"] = "a-2"
    source = table_root / "quality_flags.csv"
    with source.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=tuple(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    output_root = tmp_path / "output"
    completed = subprocess.run(
        (
            "make",
            "-f",
            "make/morphism/codebase/volume/inventory_catalog_quality_flags.mk",
            "volume-inventory-catalog-quality-flags",
            f"SILMARIL_PYTHON={sys.executable}",
            f"SILMARIL_PYLIB_SOURCE_ROOT={ROOT / 'src'}",
            f"VOLUME_REPOSITORY={repository}",
            f"VOLUME_INVENTORY_CATALOG_QUALITY_FLAGS_OUTPUT_ROOT={output_root}",
        ),
        capture_output=True,
        check=False,
        cwd=ROOT,
    )
    with (output_root / "catalog_quality_flags.csv").open(
        encoding="utf-8", newline=""
    ) as stream:
        projected_rows = tuple(csv.DictReader(stream))

    assert completed.returncode == 0, completed.stderr
    assert completed.stderr == b""
    assert projected_rows == tuple(
        sorted(rows, key=lambda row: (row["doc_id"], row["flag"], row["flag_id"]))
    )
    assert (output_root / "relation.duckdb").is_file()
    assert (output_root / "projection.receipt").is_file()
    assert (output_root / "canonical-order.receipt").is_file()
