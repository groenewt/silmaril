from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parents[1]
MODULE = "silmaril.sparky.morphism.codebase.volume.source.observation.excluded.process"


def test_excluded_observation_selects_only_declared_existing_prefixes(tmp_path: Path) -> None:
    (tmp_path / "keep.txt").write_text("keep", encoding="utf-8")
    (tmp_path / "generated").mkdir()
    (tmp_path / "generated/output.txt").write_text("generated", encoding="utf-8")
    completed = subprocess.run(
        (sys.executable, "-m", MODULE, str(tmp_path), "generated"),
        input=b"keep.txt\ngenerated/output.txt\n",
        capture_output=True,
        check=False,
        cwd=ROOT,
    )

    assert completed.returncode == 0
    assert completed.stdout == b"generated/output.txt\n"
    assert completed.stderr == b""
