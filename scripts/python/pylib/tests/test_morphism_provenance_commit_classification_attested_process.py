import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parents[1]
MODULE = "silmaril.sparky.morphism.provenance.commit.classification.attested.process"
F = b"\x1f"
LISTED = b"0123456789ABCDEF0123456789ABCDEF01234567"
H1 = b"1" * 40
H2 = b"2" * 40
TAIL = b"\x1d\n" + LISTED + b"  web-flow  one.asc  One <one@example>\n"
DOCUMENT = (
    H1 + F + b"pretty-good-privacy" + F + H1 + F + b"E" + F + LISTED[-16:] + F + b"" + F + b"" + F + b"attested subject\n"
    + H2 + F + b"pretty-good-privacy" + F + H2 + F + b"E" + F + b"FFFFFFFFFFFFFFFF" + F + b"" + F + b"" + F + b"stranger subject\n"
    + TAIL
)


def test_attested_classification_matches_key_identifier_suffix_against_manifest() -> None:
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
        b"ATTESTED" + F + H1 + F + b"web-flow" + F + LISTED + F + b"attested subject\n"
        + H2 + F + b"pretty-good-privacy" + F + H2 + F + b"E" + F + b"FFFFFFFFFFFFFFFF" + F + b"" + F + b"" + F + b"stranger subject\n"
        + TAIL
    )
