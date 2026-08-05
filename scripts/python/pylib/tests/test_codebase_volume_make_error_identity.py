import csv
import os
from pathlib import Path
import subprocess
import sys


_ROOT = Path(__file__).parents[1]
_INVENTORY = _ROOT / "tests/fixtures/codebase_volume_make_process_inventory.csv"
_ERROR_EXECUTABLES = _ROOT / "tests/fixtures/volume_process_error"


def test_make_recipe_replays_original_error_and_exit_status(tmp_path: Path) -> None:
    with _INVENTORY.open(newline="", encoding="utf-8") as stream:
        row = next(
            row
            for row in csv.DictReader(stream)
            if row["coordinate"] == "inventory/module"
        )

    temp_output = tmp_path / "accepted-output"
    error_output = tmp_path / "original-error"
    result = subprocess.run(
        ("/bin/sh", "-c", row["make_safe_invocation"].replace("$$", "$")),
        capture_output=True,
        cwd=_ROOT,
        env=os.environ | {
            "ERROR_OUTPUT": str(error_output),
            "PATH": f"{_ERROR_EXECUTABLES}:{os.environ['PATH']}",
            "SILMARIL_PYLIB_SOURCE_ROOT": str(_ROOT / "src"),
            "SILMARIL_PYTHON": sys.executable,
            "TEMP_OUTPUT": str(temp_output),
            "VOLUME_REPOSITORY": str(_ROOT),
        },
        check=False,
    )

    assert result.returncode == 73
    assert result.stdout == b""
    assert result.stderr == b"original-domain-error\n"
    assert error_output.read_bytes() == result.stderr
    assert temp_output.read_bytes() == b""
