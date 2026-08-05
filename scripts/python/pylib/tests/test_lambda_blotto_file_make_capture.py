import hashlib
from pathlib import Path
import subprocess
import tarfile


ROOT = Path(__file__).parents[1]


def test_file_capture_make_dag_materializes_durable_readback(tmp_path: Path) -> None:
    source = tmp_path / "artifact.txt"
    output = tmp_path / "capture"
    source.write_bytes(b"lambda-blotto-corpus")
    completed = subprocess.run(
        (
            "make",
            "--no-print-directory",
            "lambda-blotto-file-capture",
            f"LAMBDA_BLOTTO_FILE_SOURCE={source}",
            f"LAMBDA_BLOTTO_FILE_OUTPUT={output}",
            "LAMBDA_BLOTTO_FILE_MAXIMUM_BYTES=4096",
            "LAMBDA_BLOTTO_EVIDENCE_CLASS=observed",
        ),
        capture_output=True,
        check=False,
        cwd=ROOT,
    )

    receipt = output / "receipt.tar"
    assert completed.returncode == 0
    assert (output / "payload").read_bytes() == b"lambda-blotto-corpus"
    assert hashlib.sha256(receipt.read_bytes()).hexdigest() == (output / "receipt.sha256").read_text().split()[0]
    with tarfile.open(receipt) as archive:
        assert {"payload", "phoenix-disintegration-routing.json", "federated-computing-substrate-routing.json"}.issubset(archive.getnames())
    assert (output / "readback").read_text().endswith(": OK\n")
    assert completed.stderr == b""
