import os
from pathlib import Path
import stat
import subprocess
import sys
import tempfile


ROOT = Path(__file__).parents[1]
REPOSITORY = Path(os.environ.get("SILMARIL_REPO_ROOT", ROOT.parents[2]))
FAMILY = "silmaril.sparky.morphism.provenance.commit"
FIELD = b"\x1f"
ANCHOR = "1a8ae666f5a4b49b3e2ebc647bb6561b22f33df7"
EXPECTED_POLICY = {
    b"1a8ae666f5a4b49b3e2ebc647bb6561b22f33df7": b"agent",
    b"7d3becf760d4f547ba4f701e3b9f90de6ccb4b1a": b"release",
    b"ca3c97fbc23a6a231fd6503c4b4ae3d3001b56b1": b"release",
    b"ab3ff47b52945d006d6241d0bb0d87a444cb645f": b"web-flow",
    b"270fa68750ffc17f7376d99d6c5664cce47560dc": b"release",
}


def _run(module, arguments=(), stdin=b"", home=None):
    environment = dict(
        os.environ,
        PYTHONDONTWRITEBYTECODE="1",
        PYTHONPATH=str(ROOT / "src"),
    )
    if home is not None:
        environment["GNUPGHOME"] = str(home)
    return subprocess.run(
        (sys.executable, "-m", module, *arguments),
        input=stdin,
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
        FAMILY + ".keyring.construction.process",
        (str(keys / "herodotus.asc"), str(keys / "github-web-flow.asc"), str(keys / "claude.asc")),
        home=home,
    )
    assert imported.returncode == 0
    return home


def _classify(repository, revision, home):
    scratch = Path(tempfile.mkdtemp(prefix="silmaril-pipeline.", dir=os.environ.get("TMPDIR", "/tmp")))
    verification = _run(
        FAMILY + ".observation.verification.process", (str(repository), revision), home=home
    )
    assert verification.returncode == 0
    header = _run(
        FAMILY + ".observation.header.process", (str(repository), revision), home=home
    )
    assert header.returncode == 0
    types = _run(FAMILY + ".classification.signature.type.process", stdin=header.stdout)
    assert types.returncode == 0
    (scratch / "types").write_bytes(types.stdout)
    (scratch / "verification").write_bytes(verification.stdout)
    merged = _run(
        FAMILY + ".record.merge.process",
        (
            str(scratch / "types"),
            str(scratch / "verification"),
            str(REPOSITORY / "keys" / "trust-manifest.txt"),
        ),
    )
    assert merged.returncode == 0
    document = merged.stdout
    for stage in (
        ".classification.good.process",
        ".classification.attested.process",
        ".classification.bad.signature.process",
        ".classification.secure.shell.process",
        ".classification.unsigned.process",
        ".classification.unknown.process",
    ):
        classified = _run(FAMILY + stage, stdin=document)
        assert classified.returncode == 0
        assert classified.stderr == b""
        document = classified.stdout
    return document


def _verdicts(document):
    verdicts = {}
    for mode in ("default", "strict", "report"):
        completed = _run(FAMILY + ".policy." + mode + ".process", stdin=document)
        assert completed.stdout == document
        assert completed.stderr == b""
        verdicts[mode] = completed.returncode
    return verdicts


def test_pinned_real_history_matches_rejected_reference_classes_and_exits() -> None:
    home = _populated_home()
    document = _classify(REPOSITORY, ANCHOR, home)
    lines = document.splitlines()
    assert len(lines) == 6
    observed = {}
    for line in lines:
        fields = line.split(FIELD)
        assert fields[0] == b"GOOD"
        observed[fields[1]] = fields[2]
    for commit, policy in EXPECTED_POLICY.items():
        assert observed[commit] == policy
    assert _verdicts(document) == {"default": 0, "strict": 0, "report": 0}
    subprocess.run(("gpgconf", "--homedir", str(home), "--kill", "all"), capture_output=True, check=False)


def test_tampered_commit_fails_every_policy_mode() -> None:
    tampered = Path(tempfile.mkdtemp(prefix="silmaril-tampered.", dir=os.environ.get("TMPDIR", "/tmp")))
    subprocess.run(("git", "init", "-q", str(tampered)), check=True, capture_output=True)
    raw = subprocess.run(
        ("git", "-C", str(REPOSITORY), "cat-file", "commit", ANCHOR),
        capture_output=True,
        check=True,
    ).stdout
    rootless = b"\n".join(
        line for line in raw.split(b"\n") if not line.startswith(b"parent ")
    )
    fabricated = rootless + b"tampered payload\n"
    written = subprocess.run(
        ("git", "-C", str(tampered), "hash-object", "-w", "-t", "commit", "--literally", "--stdin"),
        input=fabricated,
        capture_output=True,
        check=True,
    )
    commit = written.stdout.strip().decode()
    subprocess.run(
        ("git", "-C", str(tampered), "update-ref", "refs/heads/tampered", commit),
        check=True,
        capture_output=True,
    )
    home = _populated_home()
    document = _classify(tampered, "tampered", home)
    lines = document.splitlines()
    assert len(lines) == 1
    assert lines[0].split(FIELD)[0] == b"BADSIG"
    assert _verdicts(document) == {"default": 1, "strict": 1, "report": 1}
    subprocess.run(("gpgconf", "--homedir", str(home), "--kill", "all"), capture_output=True, check=False)


def test_unsigned_and_secure_shell_commits_warn_by_class_not_by_crash() -> None:
    scratch = Path(tempfile.mkdtemp(prefix="silmaril-edge.", dir=os.environ.get("TMPDIR", "/tmp")))
    subprocess.run(("git", "init", "-q", str(scratch)), check=True, capture_output=True)
    subprocess.run(
        (
            "git", "-C", str(scratch),
            "-c", "user.name=T", "-c", "user.email=t@t", "-c", "commit.gpgsign=false",
            "commit", "-q", "--allow-empty", "-m", "plain unsigned subject",
        ),
        check=True,
        capture_output=True,
    )
    unsigned = subprocess.run(
        ("git", "-C", str(scratch), "rev-parse", "HEAD"),
        capture_output=True,
        check=True,
    ).stdout.strip().decode()
    fabricated = (
        b"tree 4b825dc642cb6eb9a060e54bf8d69288fbee4904\n"
        b"parent " + unsigned.encode() + b"\n"
        b"author T <t@t> 1700000000 +0000\n"
        b"committer T <t@t> 1700000000 +0000\n"
        b"gpgsig -----BEGIN SSH SIGNATURE-----\n"
        b" U1NIU0lHfake\n"
        b" -----END SSH SIGNATURE-----\n"
        b"\n"
        b"secure shell subject\n"
    )
    written = subprocess.run(
        ("git", "-C", str(scratch), "hash-object", "-w", "-t", "commit", "--literally", "--stdin"),
        input=fabricated,
        capture_output=True,
        check=True,
    )
    tip = written.stdout.strip().decode()
    subprocess.run(
        ("git", "-C", str(scratch), "update-ref", "refs/heads/edge", tip),
        check=True,
        capture_output=True,
    )
    home = _populated_home()
    document = _classify(scratch, "edge", home)
    classes = tuple(line.split(FIELD)[0] for line in document.splitlines())
    assert classes == (b"SSH", b"UNSIGNED")
    assert _verdicts(document) == {"default": 0, "strict": 1, "report": 0}
    subprocess.run(("gpgconf", "--homedir", str(home), "--kill", "all"), capture_output=True, check=False)
