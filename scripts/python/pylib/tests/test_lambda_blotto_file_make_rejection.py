from pathlib import Path
import subprocess


ROOT = Path(__file__).parents[1]


def test_file_capture_make_dag_rejects_non_observed_evidence(tmp_path: Path) -> None:
    source = tmp_path / "artifact.txt"
    source.write_bytes(b"counterfactual-input")
    completed = subprocess.run(
        (
            "make",
            "--no-print-directory",
            "lambda-blotto-file-capture",
            f"LAMBDA_BLOTTO_FILE_SOURCE={source}",
            f"LAMBDA_BLOTTO_FILE_OUTPUT={tmp_path / 'capture'}",
            "LAMBDA_BLOTTO_FILE_MAXIMUM_BYTES=4096",
            "LAMBDA_BLOTTO_EVIDENCE_CLASS=counterfactual",
        ),
        capture_output=True,
        check=False,
        cwd=ROOT,
    )

    assert completed.returncode != 0
    assert b"non_observed_file_capture_rejected" in completed.stderr
