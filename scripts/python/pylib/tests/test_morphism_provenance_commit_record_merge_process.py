import os
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).parents[1]
MODULE = "silmaril.sparky.morphism.provenance.commit.record.merge.process"
FIELD = b"\x1f"
DOCUMENT = b"\x1d"


def test_record_merge_pairs_lines_and_appends_manifest_tail() -> None:
    scratch = Path(tempfile.mkdtemp(prefix="silmaril-merge.", dir=os.environ.get("TMPDIR", "/tmp")))
    types = scratch / "types"
    records = scratch / "records"
    manifest = scratch / "manifest"
    types.write_bytes(b"aaaa\x1fpretty-good-privacy\nbbbb\x1fabsent\n")
    records.write_bytes(b"aaaa\x1fU\x1fK\x1fP\x1fF\x1fone\nbbbb\x1fN\x1f\x1f\x1f\x1ftwo\n")
    manifest.write_bytes(b"# manifest comment\nAAAA  release  key.asc  comment\n")
    environment = dict(
        os.environ,
        PYTHONDONTWRITEBYTECODE="1",
        PYTHONPATH=str(ROOT / "src"),
    )
    completed = subprocess.run(
        (sys.executable, "-m", MODULE, str(types), str(records), str(manifest)),
        capture_output=True,
        check=False,
        cwd=ROOT,
        env=environment,
    )
    assert completed.returncode == 0
    assert completed.stderr == b""
    assert completed.stdout == (
        b"aaaa\x1fpretty-good-privacy\x1faaaa\x1fU\x1fK\x1fP\x1fF\x1fone\n"
        b"bbbb\x1fabsent\x1fbbbb\x1fN\x1f\x1f\x1f\x1ftwo\n"
        + DOCUMENT
        + b"\n# manifest comment\nAAAA  release  key.asc  comment\n"
    )
