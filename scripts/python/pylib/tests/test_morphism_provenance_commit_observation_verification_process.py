import os
from pathlib import Path
import stat
import subprocess
import sys
import tempfile


ROOT = Path(__file__).parents[1]
REPOSITORY = Path(os.environ.get("SILMARIL_REPO_ROOT", ROOT.parents[2]))
KEYRING_MODULE = "silmaril.sparky.morphism.provenance.commit.keyring.construction.process"
MODULE = "silmaril.sparky.morphism.provenance.commit.observation.verification.process"
FIELD = b"\x1f"


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


def _populated_home():
    home = Path(tempfile.mkdtemp(prefix="silmaril-gnupg.", dir=os.environ.get("TMPDIR", "/tmp")))
    home.chmod(stat.S_IRWXU)
    keys = REPOSITORY / "keys"
    imported = _run(
        KEYRING_MODULE,
        (str(keys / "herodotus.asc"), str(keys / "github-web-flow.asc"), str(keys / "claude.asc")),
        home,
    )
    assert imported.returncode == 0
    return home


def test_verification_observation_emits_one_record_per_commit() -> None:
    home = _populated_home()
    completed = _run(MODULE, (str(REPOSITORY), "HEAD"), home)
    assert completed.returncode == 0
    assert completed.stderr == b""
    lines = completed.stdout.splitlines()
    assert lines
    for line in lines:
        fields = line.split(FIELD)
        assert len(fields) == 6
        assert len(fields[0]) == 40
        assert fields[1] in (b"G", b"U")
    subprocess.run(("gpgconf", "--homedir", str(home), "--kill", "all"), capture_output=True, check=False)


def test_verification_observation_hard_fails_on_unknown_revision() -> None:
    home = _populated_home()
    completed = _run(MODULE, (str(REPOSITORY), "no-such-revision-name"), home)
    assert completed.returncode != 0
    subprocess.run(("gpgconf", "--homedir", str(home), "--kill", "all"), capture_output=True, check=False)


def test_verification_observation_hard_fails_on_incompatible_signature_payload() -> None:
    scratch = Path(tempfile.mkdtemp(prefix="silmaril-repo.", dir=os.environ.get("TMPDIR", "/tmp")))
    subprocess.run(("git", "init", "-q", str(scratch)), check=True, capture_output=True)
    fabricated = (
        b"tree 4b825dc642cb6eb9a060e54bf8d69288fbee4904\n"
        b"author T <t@t> 1700000000 +0000\n"
        b"committer T <t@t> 1700000000 +0000\n"
        b"gpgsig -----BEGIN WEIRD BLOB-----\n"
        b" xxxx\n"
        b" -----END WEIRD BLOB-----\n"
        b"\n"
        b"incompatible payload subject\n"
    )
    written = subprocess.run(
        ("git", "-C", str(scratch), "hash-object", "-w", "-t", "commit", "--literally", "--stdin"),
        input=fabricated,
        capture_output=True,
        check=True,
    )
    commit = written.stdout.strip().decode()
    subprocess.run(
        ("git", "-C", str(scratch), "update-ref", "refs/heads/weird", commit),
        check=True,
        capture_output=True,
    )
    home = _populated_home()
    completed = _run(MODULE, (str(scratch), "weird"), home)
    assert completed.returncode != 0
    subprocess.run(("gpgconf", "--homedir", str(home), "--kill", "all"), capture_output=True, check=False)
