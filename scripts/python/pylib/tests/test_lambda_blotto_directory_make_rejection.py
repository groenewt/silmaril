from pathlib import Path
import subprocess


ROOT = Path(__file__).parents[1]


def test_directory_capture_make_dag_rejects_entry_bound_overflow(tmp_path: Path) -> None:
    source = tmp_path / "root"
    source.mkdir()
    (source / "a").write_bytes(b"a")
    (source / "b").write_bytes(b"b")
    completed = subprocess.run(
        (
            "make",
            "--no-print-directory",
            "lambda-blotto-directory-capture",
            f"LAMBDA_BLOTTO_DIRECTORY_SOURCE={source}",
            f"LAMBDA_BLOTTO_DIRECTORY_OUTPUT={tmp_path / 'capture'}",
            "LAMBDA_BLOTTO_DIRECTORY_MAXIMUM_ENTRIES=1",
            "LAMBDA_BLOTTO_EVIDENCE_CLASS=observed",
        ),
        capture_output=True,
        check=False,
        cwd=ROOT,
    )

    assert completed.returncode != 0
    assert b"directory_capture_maximum_entries_exceeded" in completed.stderr
