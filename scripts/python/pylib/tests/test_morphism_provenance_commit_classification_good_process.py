import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parents[1]
MODULE = "silmaril.sparky.morphism.provenance.commit.classification.good.process"
F = b"\x1f"
LISTED = b"0123456789ABCDEF0123456789ABCDEF01234567"
SECOND = b"89ABCDEF0123456789ABCDEF0123456789ABCDEF"
UNLISTED = b"FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"
H1 = b"1" * 40
H2 = b"2" * 40
H3 = b"3" * 40
TAIL = (
    b"\x1d\n# comment line\n"
    + LISTED + b"  release  one.asc  One <one@example>\n"
    + SECOND + b"  agent  two.asc  Two <two@example>\n"
)
DOCUMENT = (
    H1 + F + b"pretty-good-privacy" + F + H1 + F + b"U" + F + b"KEYID" + F + LISTED + F + LISTED + F + b"primary subject\n"
    + H2 + F + b"pretty-good-privacy" + F + H2 + F + b"G" + F + b"KEYID" + F + b"" + F + SECOND + F + b"fallback subject\n"
    + H3 + F + b"pretty-good-privacy" + F + H3 + F + b"U" + F + b"KEYID" + F + UNLISTED + F + UNLISTED + F + b"unlisted subject\n"
    + TAIL
)


def test_good_classification_rewrites_only_manifest_listed_valid_records() -> None:
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
        b"GOOD" + F + H1 + F + b"release" + F + LISTED + F + b"primary subject\n"
        + b"GOOD" + F + H2 + F + b"agent" + F + SECOND + F + b"fallback subject\n"
        + H3 + F + b"pretty-good-privacy" + F + H3 + F + b"U" + F + b"KEYID" + F + UNLISTED + F + UNLISTED + F + b"unlisted subject\n"
        + TAIL
    )
