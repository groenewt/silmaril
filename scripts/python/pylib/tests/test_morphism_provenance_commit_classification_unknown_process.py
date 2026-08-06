import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parents[1]
MODULE = "silmaril.sparky.morphism.provenance.commit.classification.unknown.process"
F = b"\x1f"
H1 = b"1" * 40
H2 = b"2" * 40
H3 = b"3" * 40
TAIL = b"\x1d\nmanifest tail\n"
DOCUMENT = (
    b"GOOD" + F + H1 + F + b"release" + F + b"0123456789ABCDEF0123456789ABCDEF01234567" + F + b"good subject\n"
    + H2 + F + b"pretty-good-privacy" + F + H2 + F + b"X" + F + b"EXPIREDKEY123456" + F + b"" + F + b"" + F + b"expired subject\n"
    + H3 + F + b"other" + F + H3 + F + b"N" + F + b"" + F + b"" + F + b"" + F + b"odd payload subject\n"
    + TAIL
)


def test_unknown_classification_sweeps_residual_records_and_strips_manifest_tail() -> None:
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
        b"GOOD" + F + H1 + F + b"release" + F + b"0123456789ABCDEF0123456789ABCDEF01234567" + F + b"good subject\n"
        + b"UNKNOWN" + F + H2 + F + b"-" + F + b"EXPIREDKEY123456" + F + b"expired subject\n"
        + b"UNKNOWN" + F + H3 + F + b"-" + F + b"?" + F + b"odd payload subject\n"
    )
