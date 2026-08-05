import csv
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parents[1]
INVENTORY = ROOT / "tests/fixtures/codebase_volume_make_process_inventory.csv"
ERROR_BIN = ROOT / "tests/fixtures/volume_process_error"


def test_table_constructor_make_process_preserves_original_child_error(tmp_path: Path) -> None:
    with INVENTORY.open(newline="", encoding="utf-8") as stream:
        row = next(row for row in csv.DictReader(stream) if row["coordinate"] == "table/modules/construct")
    completed = subprocess.run(
        ("/bin/sh", "-c", row["make_safe_invocation"].replace("$$", "$")),
        input=b"lib/a.ex:1:defmodule A do\n",
        capture_output=True,
        check=False,
        cwd=ROOT,
        env=os.environ | {
            "ERROR_OUTPUT": str(tmp_path / "error"),
            "INPUT": str(ROOT / "tests/fixtures/volume_inventory/README.md"),
            "PATH": f"{ERROR_BIN}:{os.environ['PATH']}",
            "SILMARIL_PYLIB_SOURCE_ROOT": str(ROOT / "src"),
            "SILMARIL_PYTHON": sys.executable,
            "TEMP_OUTPUT": str(tmp_path / "output"),
        },
    )

    assert completed.returncode == 73
    assert completed.stdout == b""
    assert completed.stderr == b"original-domain-error\n"
