import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parents[1]
MODULE = "silmaril.sparky.morphism.provenance.commit.policy.default.process"
F = b"\x1f"
H = b"1" * 40
GOOD = b"GOOD" + F + H + F + b"release" + F + b"A" * 40 + F + b"s\n"
WARN = b"ATTESTED" + F + H + F + b"agent" + F + b"B" * 40 + F + b"s\n" + b"SSH" + F + H + F + b"-" + F + b"-" + F + b"s\n" + b"UNSIGNED" + F + H + F + b"-" + F + b"-" + F + b"s\n"
UNKNOWN = b"UNKNOWN" + F + H + F + b"-" + F + b"?" + F + b"s\n"
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


def test_default_policy_passes_good_and_warn_classes() -> None:
    completed = _run(GOOD + WARN)
    assert completed.returncode == 0
    assert completed.stdout == GOOD + WARN
    assert completed.stderr == b""


def test_default_policy_fails_unknown() -> None:
    completed = _run(GOOD + UNKNOWN)
    assert completed.returncode == 1
    assert completed.stdout == GOOD + UNKNOWN


def test_default_policy_fails_bad_signature() -> None:
    completed = _run(GOOD + BADSIG)
    assert completed.returncode == 1
    assert completed.stdout == GOOD + BADSIG
