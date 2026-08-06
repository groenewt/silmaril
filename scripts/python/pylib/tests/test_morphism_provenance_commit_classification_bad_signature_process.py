import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parents[1]
MODULE = "silmaril.sparky.morphism.provenance.commit.classification.bad.signature.process"
F = b"\x1f"
H1 = b"1" * 40
H2 = b"2" * 40
TAIL = b"\x1d\nmanifest tail\n"
DOCUMENT = (
    H1 + F + b"pretty-good-privacy" + F + H1 + F + b"B" + F + b"BADKEYID12345678" + F + b"" + F + b"" + F + b"tampered subject\n"
    + H2 + F + b"pretty-good-privacy" + F + H2 + F + b"B" + F + b"" + F + b"" + F + b"" + F + b"keyless tamper subject\n"
    + TAIL
)


def test_bad_signature_classification_is_never_advisory() -> None:
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
        b"BADSIG" + F + H1 + F + b"-" + F + b"BADKEYID12345678" + F + b"tampered subject\n"
        + b"BADSIG" + F + H2 + F + b"-" + F + b"?" + F + b"keyless tamper subject\n"
        + TAIL
    )
