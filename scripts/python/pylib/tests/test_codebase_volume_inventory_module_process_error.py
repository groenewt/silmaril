import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).parents[1]
FIXTURE = ROOT / "tests/fixtures/volume_inventory"
ERROR_BIN = ROOT / "tests/fixtures/volume_process_error"
MODULE = "silmaril.sparky.morphism.codebase.volume.inventory.module.process"


def test_inventory_module_process_preserves_original_command_error() -> None:
    environment = dict(os.environ)
    environment["PATH"] = str(ERROR_BIN)

    completed = subprocess.run(
        (sys.executable, "-m", MODULE, str(FIXTURE)),
        capture_output=True,
        check=False,
        cwd=ROOT,
        env=environment,
    )

    assert completed.returncode == 73
    assert completed.stdout == b""
    assert completed.stderr == b"original-domain-error\n"
