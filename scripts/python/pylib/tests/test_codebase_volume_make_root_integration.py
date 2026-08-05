import subprocess
from pathlib import Path


ROOT = Path(__file__).parents[1]


def test_root_make_exposes_every_modular_volume_pipeline() -> None:
    completed = subprocess.run(
        ("make", "-n", "morphism-codebase-volume"),
        capture_output=True,
        check=False,
        cwd=ROOT,
        text=True,
    )

    assert completed.returncode == 0
    assert "volume.artifact.manifest" in completed.stdout
    assert "volume.provenance.source_to_fragment" in completed.stdout
    assert "volume.verification.process_coverage" in completed.stdout
    assert "volume.phase14" in completed.stdout
    assert "volume.table.phase14" in completed.stdout
    assert "volume.table.source_files.aggregate" in completed.stdout
