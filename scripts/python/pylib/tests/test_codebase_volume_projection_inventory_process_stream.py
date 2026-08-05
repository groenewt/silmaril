import os
from pathlib import Path
import subprocess
import sys


_ROOT = Path(__file__).parents[1]
_MODULE = "silmaril.sparky.morphism.codebase.volume.projection.inventory.process"
_TITLE = "Modules"
_LAYOUT = "keyed"
_GROUP = "module"
_HEADER = b"module,name\n"
_ROW = b"alpha,beta\n"
_ROW_COUNT = 200_000
_BODY = _HEADER + _ROW * _ROW_COUNT
_TABLE_HEADING = b"\\subsection{Modules}\n"
_GROUP_HEADING = b"\\subsubsection*{\\texttt{alpha}}\n"
_RECORD_HEADING = b"\\noindent\\textbf{\\texttt{beta}}\\par\n"


def test_projection_inventory_streams_a_body_larger_than_arg_max() -> None:
    result = subprocess.run(
        (sys.executable, "-m", _MODULE, _TITLE, _LAYOUT, _GROUP),
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
    assert result.stdout == (
        _TABLE_HEADING + _GROUP_HEADING + _RECORD_HEADING * _ROW_COUNT
    )
    assert result.stderr == b""
