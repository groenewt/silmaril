import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).parents[1]
FIXTURE = ROOT / "tests/fixtures/volume_inventory"
MODULE = "silmaril.sparky.morphism.codebase.volume.inventory.module.process"


def test_inventory_module_process_emits_raw_output() -> None:
    completed = subprocess.run(
        (sys.executable, "-m", MODULE, str(FIXTURE)),
        capture_output=True,
        check=False,
        cwd=ROOT,
    )

    assert completed.returncode == 0
    assert b"sample.exs:1:defmodule Mix.Tasks.Volume.Sample do" in completed.stdout
    assert completed.stderr == b""
