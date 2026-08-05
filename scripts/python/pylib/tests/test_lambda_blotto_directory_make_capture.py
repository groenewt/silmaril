from pathlib import Path
import subprocess
import tarfile


ROOT = Path(__file__).parents[1]


def test_directory_capture_make_dag_includes_hidden_and_records_symlink(tmp_path: Path) -> None:
    source = tmp_path / "root"
    output = tmp_path / "capture"
    source.mkdir()
    (source / "visible.txt").write_bytes(b"visible")
    (source / ".hidden-map").write_bytes(b"hidden")
    (source / "target").mkdir()
    (source / "target/inside.txt").write_bytes(b"inside")
    (source / "link-to-directory").symlink_to(source / "target", target_is_directory=True)
    completed = subprocess.run(
        (
            "make",
            "--no-print-directory",
            "lambda-blotto-directory-capture",
            f"LAMBDA_BLOTTO_DIRECTORY_SOURCE={source}",
            f"LAMBDA_BLOTTO_DIRECTORY_OUTPUT={output}",
            "LAMBDA_BLOTTO_DIRECTORY_MAXIMUM_ENTRIES=10",
            "LAMBDA_BLOTTO_EVIDENCE_CLASS=observed",
        ),
        capture_output=True,
        check=False,
        cwd=ROOT,
    )

    assert completed.returncode == 0
    assert (output / "names.sorted").read_bytes().split(b"\0")[:-1] == [b".hidden-map", b"link-to-directory", b"target", b"visible.txt"]
    with tarfile.open(output / "payload.tar") as archive:
        link = archive.getmember("root/link-to-directory")
        assert link.issym()
        assert link.linkname.endswith("/target")
    assert (output / "readback").read_text().endswith(": OK\n")
    assert completed.stderr == b""
