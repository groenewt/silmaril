import csv
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parents[1]


def test_csv_artifacts_are_composed_as_make_visible_total_edges(tmp_path: Path) -> None:
    generated_root = tmp_path / "generated"
    contract_path = tmp_path / "inventory-contract.csv"
    rows = [
        {
            "inventory_id": f"inventory_{index:02d}",
            "output_artifact": f"inventories/inventory_{index:02d}.csv",
            "downstream_fragment": f"sections/inventory_{index:02d}.tex",
        }
        for index in range(23)
    ]
    generated_root.mkdir()
    with contract_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=tuple(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    for row in rows:
        source = generated_root / row["output_artifact"]
        projection = generated_root / f"tables/{row['inventory_id']}.tex"
        fragment = generated_root / row["downstream_fragment"]
        source.parent.mkdir(parents=True, exist_ok=True)
        projection.parent.mkdir(parents=True, exist_ok=True)
        fragment.parent.mkdir(parents=True, exist_ok=True)
        source.write_text("coordinate\nedge\n", encoding="utf-8")
        projection.write_text("projection\n", encoding="utf-8")
        fragment.write_text("fragment\n", encoding="utf-8")
    (generated_root / "body.tex").write_text("body\n", encoding="utf-8")

    csv_artifacts = tuple(row["output_artifact"] for row in rows)
    all_artifacts = csv_artifacts + tuple(
        f"tables/{row['inventory_id']}.tex" for row in rows
    ) + tuple(row["downstream_fragment"] for row in rows) + ("body.tex",)
    manifest_root = tmp_path / "manifest-output"
    manifest = subprocess.run(
        (
            "make",
            "-f",
            "make/morphism/codebase/volume/artifact_manifest.mk",
            "volume-artifact-manifest",
            f"SILMARIL_PYTHON={sys.executable}",
            f"SILMARIL_PYLIB_SOURCE_ROOT={ROOT / 'src'}",
            f"VOLUME_INVENTORY_CONTRACT={contract_path}",
            f"VOLUME_MANIFEST_CSV_ARTIFACTS={' '.join(csv_artifacts)}",
            f"VOLUME_MANIFEST_ARTIFACTS={' '.join(all_artifacts)}",
            f"VOLUME_ARTIFACT_MANIFEST_GENERATED_ROOT={generated_root}",
            f"VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT={manifest_root}",
        ),
        capture_output=True,
        check=False,
        cwd=ROOT,
    )
    manifest_document = json.loads(
        (manifest_root / "manifest.json").read_text(encoding="utf-8")
    )

    source_root = tmp_path / "source-output"
    source_to_fragment = subprocess.run(
        (
            "make",
            "-f",
            "make/morphism/codebase/volume/provenance_source_to_fragment.mk",
            "volume-source-to-fragment",
            f"SILMARIL_PYTHON={sys.executable}",
            f"SILMARIL_PYLIB_SOURCE_ROOT={ROOT / 'src'}",
            f"VOLUME_INVENTORY_CONTRACT={contract_path}",
            f"VOLUME_SOURCE_TO_FRAGMENT_GENERATED_ROOT={generated_root}",
            f"VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT={source_root}",
        ),
        capture_output=True,
        check=False,
        cwd=ROOT,
    )
    with (source_root / "source_to_fragment.csv").open(
        encoding="utf-8", newline=""
    ) as stream:
        source_rows = tuple(csv.reader(stream))

    accepted_path = tmp_path / "accepted.csv"
    materialized_path = tmp_path / "materialized.csv"
    accepted_path.write_text("coordinate\nedge_a\nedge_b\n", encoding="utf-8")
    materialized_path.write_text("coordinate\nedge_b\nedge_a\n", encoding="utf-8")
    coverage_root = tmp_path / "coverage-output"
    coverage = subprocess.run(
        (
            "make",
            "-f",
            "make/morphism/codebase/volume/verification_process_coverage.mk",
            "volume-process-coverage",
            f"SILMARIL_PYTHON={sys.executable}",
            f"SILMARIL_PYLIB_SOURCE_ROOT={ROOT / 'src'}",
            f"VOLUME_ACCEPTED_PROCESS_INVENTORY={accepted_path}",
            f"VOLUME_MATERIALIZED_PROCESS_COORDINATES={materialized_path}",
            f"VOLUME_PROCESS_COVERAGE_OUTPUT_ROOT={coverage_root}",
        ),
        capture_output=True,
        check=False,
        cwd=ROOT,
    )

    assert manifest.returncode == 0, manifest.stderr
    assert len(manifest_document["artifacts"]) == 70
    assert len(manifest_document["inventories"]) == 23
    assert manifest_document["gaps"] == []
    assert len(tuple(manifest_root.glob("*.carrier"))) == 49
    assert source_to_fragment.returncode == 0, source_to_fragment.stderr
    assert source_rows[0] == [
        "inventory_id",
        "source_artifact",
        "projection_artifact",
        "downstream_fragment",
        "row_count",
        "sha256",
    ]
    assert len(source_rows) == 24
    assert len(tuple(source_root.glob("*.carrier"))) == 41
    assert coverage.returncode == 0, coverage.stderr
    assert (coverage_root / "process_coverage.csv").read_text(encoding="utf-8") == (
        "process_coverage_validated,2\n"
    )
    assert len(tuple(coverage_root.glob("*.carrier"))) == 20

    materialized_path.write_text("coordinate\nedge_c\n", encoding="utf-8")
    failed_root = tmp_path / "failed-coverage-output"
    failed = subprocess.run(
        (
            "make",
            "-f",
            "make/morphism/codebase/volume/verification_process_coverage.mk",
            "volume-process-coverage",
            f"SILMARIL_PYTHON={sys.executable}",
            f"SILMARIL_PYLIB_SOURCE_ROOT={ROOT / 'src'}",
            f"VOLUME_ACCEPTED_PROCESS_INVENTORY={accepted_path}",
            f"VOLUME_MATERIALIZED_PROCESS_COORDINATES={materialized_path}",
            f"VOLUME_PROCESS_COVERAGE_OUTPUT_ROOT={failed_root}",
        ),
        capture_output=True,
        check=False,
        cwd=ROOT,
    )
    child_error = (failed_root / "17-matched.carrier.error").read_bytes()

    assert failed.returncode != 0
    assert child_error in failed.stderr
    assert b"process_coverage_mismatch" in child_error
