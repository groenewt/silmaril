import os
from pathlib import Path
import subprocess
import sys


_ROOT = Path(__file__).parents[1]
_MODULE = "silmaril.sparky.morphism.codebase.volume.projection.chapter.process"
_ERROR_EXECUTABLES = _ROOT / "tests/fixtures/volume_process_error"


def test_projection_chapter_preserves_original_child_error() -> None:
    result = subprocess.run(
        (sys.executable, "-m", _MODULE, "Architecture"),
        input=b"body",
        capture_output=True,
        cwd=_ROOT,
        env=os.environ | {
            "PATH": f"{_ERROR_EXECUTABLES}:{os.environ['PATH']}",
            "PYTHONDONTWRITEBYTECODE": "1",
            "PYTHONPATH": str(_ROOT / "src"),
        },
        check=False,
    )

    assert result.returncode == 73
    assert result.stdout == b""
    assert result.stderr == b"original-domain-error\n"
