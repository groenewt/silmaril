import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parents[1]
REPOSITORY = Path(os.environ.get("SILMARIL_REPO_ROOT", ROOT.parents[2]))
MODULE = "silmaril.sparky.morphism.provenance.commit.observation.header.process"


def _run(arguments):
    environment = dict(
        os.environ,
        PYTHONDONTWRITEBYTECODE="1",
        PYTHONPATH=str(ROOT / "src"),
    )
    return subprocess.run(
        (sys.executable, "-m", MODULE, *arguments),
        capture_output=True,
        check=False,
        cwd=ROOT,
        env=environment,
    )


def test_header_observation_emits_raw_commit_headers() -> None:
    head = subprocess.run(
        ("git", "-C", str(REPOSITORY), "rev-parse", "HEAD"),
        capture_output=True,
        check=True,
    ).stdout.strip()
    completed = _run((str(REPOSITORY), "HEAD"))
    assert completed.returncode == 0
    assert completed.stderr == b""
    assert completed.stdout.startswith(b"commit " + head + b"\n")
    assert b"\ngpgsig -----BEGIN PGP SIGNATURE-----\n" in completed.stdout


def test_header_observation_hard_fails_on_unknown_revision() -> None:
    completed = _run((str(REPOSITORY), "no-such-revision-name"))
    assert completed.returncode != 0
