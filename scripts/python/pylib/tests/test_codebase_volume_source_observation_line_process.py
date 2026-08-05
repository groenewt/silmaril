from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parents[1]
FIXTURE = ROOT / "tests/fixtures/volume_inventory"
MODULE = "silmaril.sparky.morphism.codebase.volume.source.observation.line.process"


def test_source_line_observation_emits_sorted_source_located_text() -> None:
    completed = subprocess.run(
        (sys.executable, "-m", MODULE, str(FIXTURE), "--glob", "!README.md"),
        capture_output=True,
        check=False,
        cwd=ROOT,
    )

    assert completed.returncode == 0
    assert completed.stdout.startswith(b"./Makefile:1:build:\n")
    assert b"./config/runtime.exs:2:config :telephone, :ring_pool, 64\n" in completed.stdout
    assert completed.stderr == b""
