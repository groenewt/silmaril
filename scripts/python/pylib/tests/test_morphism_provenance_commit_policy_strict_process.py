import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parents[1]
MODULE = "silmaril.sparky.morphism.provenance.commit.policy.strict.process"
F = b"\x1f"
H = b"1" * 40
GOOD = b"GOOD" + F + H + F + b"release" + F + b"A" * 40 + F + b"s\n"
ATTESTED = b"ATTESTED" + F + H + F + b"agent" + F + b"B" * 40 + F + b"s\n"
SSH = b"SSH" + F + H + F + b"-" + F + b"-" + F + b"s\n"
UNSIGNED = b"UNSIGNED" + F + H + F + b"-" + F + b"-" + F + b"s\n"


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


def test_strict_policy_passes_only_good() -> None:
    completed = _run(GOOD + GOOD)
    assert completed.returncode == 0
    assert completed.stdout == GOOD + GOOD
    assert completed.stderr == b""


def test_strict_policy_fails_every_non_good_class() -> None:
    assert _run(GOOD + ATTESTED).returncode == 1
    assert _run(GOOD + SSH).returncode == 1
    assert _run(GOOD + UNSIGNED).returncode == 1
