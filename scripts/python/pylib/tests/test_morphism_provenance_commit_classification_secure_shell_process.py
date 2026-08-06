import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parents[1]
MODULE = "silmaril.sparky.morphism.provenance.commit.classification.secure.shell.process"
F = b"\x1f"
H1 = b"1" * 40
H2 = b"2" * 40
TAIL = b"\x1d\nmanifest tail\n"
DOCUMENT = (
    H1 + F + b"secure-shell" + F + H1 + F + b"N" + F + b"" + F + b"" + F + b"" + F + b"ssh subject\n"
    + H2 + F + b"pretty-good-privacy" + F + H2 + F + b"U" + F + b"K" + F + b"" + F + b"" + F + b"pgp subject\n"
    + TAIL
)


def test_secure_shell_classification_rewrites_only_secure_shell_records() -> None:
    environment = dict(
        os.environ,
        PYTHONDONTWRITEBYTECODE="1",
        PYTHONPATH=str(ROOT / "src"),
    )
    completed = subprocess.run(
        (sys.executable, "-m", MODULE),
        input=DOCUMENT,
        capture_output=True,
        check=False,
        cwd=ROOT,
        env=environment,
    )
    assert completed.returncode == 0
    assert completed.stderr == b""
    assert completed.stdout == (
        b"SSH" + F + H1 + F + b"-" + F + b"-" + F + b"ssh subject\n"
        + H2 + F + b"pretty-good-privacy" + F + H2 + F + b"U" + F + b"K" + F + b"" + F + b"" + F + b"pgp subject\n"
        + TAIL
    )
