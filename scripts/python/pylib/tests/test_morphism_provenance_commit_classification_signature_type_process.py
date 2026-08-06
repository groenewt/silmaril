import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parents[1]
MODULE = "silmaril.sparky.morphism.provenance.commit.classification.signature.type.process"
FIELD = b"\x1f"
PGP_HASH = b"a" * 40
SSH_HASH = b"b" * 40
OTHER_HASH = b"c" * 40
ABSENT_HASH = b"d" * 40
RAW = (
    b"commit " + PGP_HASH + b"\n"
    b"tree 4b825dc642cb6eb9a060e54bf8d69288fbee4904\n"
    b"author T <t@t> 1700000000 +0000\n"
    b"committer T <t@t> 1700000000 +0000\n"
    b"gpgsig -----BEGIN PGP SIGNATURE-----\n"
    b" abcdef\n"
    b" -----END PGP SIGNATURE-----\n"
    b"\n"
    b"    pgp subject\n"
    b"\n"
    b"commit " + SSH_HASH + b"\n"
    b"tree 4b825dc642cb6eb9a060e54bf8d69288fbee4904\n"
    b"committer T <t@t> 1700000000 +0000\n"
    b"gpgsig -----BEGIN SSH SIGNATURE-----\n"
    b" abcdef\n"
    b" -----END SSH SIGNATURE-----\n"
    b"\n"
    b"    ssh subject\n"
    b"\n"
    b"commit " + OTHER_HASH + b"\n"
    b"tree 4b825dc642cb6eb9a060e54bf8d69288fbee4904\n"
    b"committer T <t@t> 1700000000 +0000\n"
    b"gpgsig -----BEGIN WEIRD BLOB-----\n"
    b" abcdef\n"
    b"\n"
    b"    other subject\n"
    b"\n"
    b"commit " + ABSENT_HASH + b"\n"
    b"tree 4b825dc642cb6eb9a060e54bf8d69288fbee4904\n"
    b"committer T <t@t> 1700000000 +0000\n"
    b"\n"
    b"    unsigned subject quoting a signature block:\n"
    b"    gpgsig -----BEGIN PGP SIGNATURE-----\n"
    b"    -----END PGP SIGNATURE-----\n"
)


def _run(stdin):
    environment = dict(
        os.environ,
        PYTHONDONTWRITEBYTECODE="1",
        PYTHONPATH=str(ROOT / "src"),
    )
    return subprocess.run(
        (sys.executable, "-m", MODULE),
        input=stdin,
        capture_output=True,
        check=False,
        cwd=ROOT,
        env=environment,
    )


def test_signature_type_classification_is_header_block_only() -> None:
    completed = _run(RAW)
    assert completed.returncode == 0
    assert completed.stderr == b""
    assert completed.stdout == (
        PGP_HASH + FIELD + b"pretty-good-privacy\n"
        + SSH_HASH + FIELD + b"secure-shell\n"
        + OTHER_HASH + FIELD + b"other\n"
        + ABSENT_HASH + FIELD + b"absent\n"
    )


def test_signature_type_classification_of_empty_observation_is_empty() -> None:
    completed = _run(b"")
    assert completed.returncode == 0
    assert completed.stdout == b""
