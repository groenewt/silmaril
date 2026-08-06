import os
from pathlib import Path
import stat
import subprocess
import sys
import tempfile


ROOT = Path(__file__).parents[1]
REPOSITORY = Path(os.environ.get("SILMARIL_REPO_ROOT", ROOT.parents[2]))
MODULE = "silmaril.sparky.morphism.provenance.commit.keyring.construction.process"


def _run(module, arguments, home):
    environment = dict(
        os.environ,
        PYTHONDONTWRITEBYTECODE="1",
        PYTHONPATH=str(ROOT / "src"),
        GNUPGHOME=str(home),
    )
    return subprocess.run(
        (sys.executable, "-m", module, *arguments),
        capture_output=True,
        check=False,
        cwd=ROOT,
        env=environment,
    )


def test_keyring_construction_imports_manifest_keys_into_ephemeral_home() -> None:
    home = Path(tempfile.mkdtemp(prefix="silmaril-gnupg.", dir=os.environ.get("TMPDIR", "/tmp")))
    home.chmod(stat.S_IRWXU)
    keys = REPOSITORY / "keys"
    completed = _run(
        MODULE,
        (str(keys / "herodotus.asc"), str(keys / "github-web-flow.asc"), str(keys / "claude.asc")),
        home,
    )
    assert completed.returncode == 0
    listing = subprocess.run(
        ("gpg", "--batch", "--with-colons", "--list-keys"),
        capture_output=True,
        check=False,
        env=dict(os.environ, GNUPGHOME=str(home)),
    )
    primaries = tuple(
        line for line in listing.stdout.splitlines() if line.startswith(b"pub:")
    )
    assert len(primaries) == 3
    subprocess.run(
        ("gpgconf", "--homedir", str(home), "--kill", "all"),
        capture_output=True,
        check=False,
    )


def test_keyring_construction_fails_on_absent_key_file() -> None:
    home = Path(tempfile.mkdtemp(prefix="silmaril-gnupg.", dir=os.environ.get("TMPDIR", "/tmp")))
    home.chmod(stat.S_IRWXU)
    completed = _run(MODULE, (str(home / "missing.asc"),), home)
    assert completed.returncode != 0
    subprocess.run(
        ("gpgconf", "--homedir", str(home), "--kill", "all"),
        capture_output=True,
        check=False,
    )
