import csv
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parents[1]


def test_catalog_documents_projects_canonical_rows_without_reextraction(tmp_path: Path) -> None:
    repository = tmp_path / "repository"
    table_root = repository / "library_cache/tables"
    table_root.mkdir(parents=True)
    rows = [
      {
        "doc_id": "doc_id-0-b",
        "abs_path": "abs_path-1-b",
        "rel_path": "rel_path-2-b",
        "filename": "filename-3-b",
        "dir1": "dir1-4-b",
        "dir2": "dir2-5-b",
        "extension": "extension-6-b",
        "size_bytes": "size_bytes-7-b",
        "mtime_ns": "mtime_ns-8-b",
        "sha256": "sha256-9-b",
        "hash_status": "hash_status-10-b",
        "source_label": "source_label-11-b",
        "canonical_status": "canonical_status-12-b",
        "ingest_status": "ingest_status-13-b",
        "text_cache_path": "text_cache_path-14-b",
        "title": "title-15-b",
        "detected_title": "detected_title-16-b",
        "pdf_pages": "pdf_pages-17-b",
        "word_count": "word_count-18-b",
        "line_count": "line_count-19-b",
        "file_kind": "file_kind-20-b",
        "parse_status": "parse_status-21-b",
        "parse_error": "parse_error-22-b",
      },
      {
        "doc_id": "doc_id-0-a",
        "abs_path": "abs_path-1-a",
        "rel_path": "rel_path-2-a",
        "filename": "filename-3-a",
        "dir1": "dir1-4-a",
        "dir2": "dir2-5-a",
        "extension": "extension-6-a",
        "size_bytes": "size_bytes-7-a",
        "mtime_ns": "mtime_ns-8-a",
        "sha256": "sha256-9-a",
        "hash_status": "hash_status-10-a",
        "source_label": "source_label-11-a",
        "canonical_status": "canonical_status-12-a",
        "ingest_status": "ingest_status-13-a",
        "text_cache_path": "text_cache_path-14-a",
        "title": "title-15-a",
        "detected_title": "detected_title-16-a",
        "pdf_pages": "pdf_pages-17-a",
        "word_count": "word_count-18-a",
        "line_count": "line_count-19-a",
        "file_kind": "file_kind-20-a",
        "parse_status": "parse_status-21-a",
        "parse_error": "parse_error-22-a",
      },
    ]
    rows[0]["rel_path"] = "b-0"
    rows[0]["doc_id"] = "b-1"
    rows[1]["rel_path"] = "a-0"
    rows[1]["doc_id"] = "a-1"
    source = table_root / "documents.csv"
    with source.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=tuple(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    output_root = tmp_path / "output"
    completed = subprocess.run(
        (
            "make",
            "-f",
            "make/morphism/codebase/volume/inventory_catalog_documents.mk",
            "volume-inventory-catalog-documents",
            f"SILMARIL_PYTHON={sys.executable}",
            f"SILMARIL_PYLIB_SOURCE_ROOT={ROOT / 'src'}",
            f"VOLUME_REPOSITORY={repository}",
            f"VOLUME_INVENTORY_CATALOG_DOCUMENTS_OUTPUT_ROOT={output_root}",
        ),
        capture_output=True,
        check=False,
        cwd=ROOT,
    )
    with (output_root / "catalog_documents.csv").open(
        encoding="utf-8", newline=""
    ) as stream:
        projected_rows = tuple(csv.DictReader(stream))

    assert completed.returncode == 0, completed.stderr
    assert completed.stderr == b""
    assert projected_rows == tuple(
        sorted(rows, key=lambda row: (row["rel_path"], row["doc_id"]))
    )
    assert (output_root / "relation.duckdb").is_file()
    assert (output_root / "projection.receipt").is_file()
    assert (output_root / "canonical-order.receipt").is_file()
