import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parents[1]
MODULE = "silmaril.sparky.morphism.provenance.commit.policy.report.process"
F = b"\x1f"
H = b"1" * 40
GOOD = b"GOOD" + F + H + F + b"release" + F + b"A" * 40 + F + b"s\n"
UNKNOWN = b"UNKNOWN" + F + H + F + b"-" + F + b"?" + F + b"s\n"
UNSIGNED = b"UNSIGNED" + F + H + F + b"-" + F + b"-" + F + b"s\n"
BADSIG = b"BADSIG" + F + H + F + b"-" + F + b"?" + F + b"s\n"


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


def test_report_policy_passes_everything_except_bad_signature() -> None:
    completed = _run(GOOD + UNKNOWN + UNSIGNED)
    assert completed.returncode == 0
    assert completed.stdout == GOOD + UNKNOWN + UNSIGNED
    assert completed.stderr == b""


def test_report_policy_fails_bad_signature() -> None:
    completed = _run(GOOD + BADSIG)
    assert completed.returncode == 1
    assert completed.stdout == GOOD + BADSIG
