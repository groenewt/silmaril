import os
from pathlib import Path
import subprocess
import sys


_ROOT = Path(__file__).parents[1]
_MODULE = "silmaril.sparky.morphism.codebase.volume.projection.provenance.process"
_BODY = (b"subject,predicate,object\n" * 200_000)


def test_projection_provenance_streams_a_body_larger_than_arg_max() -> None:
    result = subprocess.run(
        (sys.executable, "-m", _MODULE),
        input=_BODY,
        capture_output=True,
        cwd=_ROOT,
        env=os.environ | {
            "PYTHONDONTWRITEBYTECODE": "1",
            "PYTHONPATH": str(_ROOT / "src"),
        },
        check=False,
    )

    assert result.returncode == 0
    assert result.stdout == b"\\section{Provenance and gaps}\n" + _BODY + b"\n"
    assert result.stderr == b""
