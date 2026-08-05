from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parents[1]
MODULE = "silmaril.sparky.morphism.codebase.volume.source.observation.unreadable.process"


def test_unreadable_observation_selects_only_unreadable_regular_files(tmp_path: Path) -> None:
    (tmp_path / "readable.txt").write_text("readable", encoding="utf-8")
    unreadable = tmp_path / "unreadable.txt"
    unreadable.write_text("unreadable", encoding="utf-8")
    unreadable.chmod(0o000)
    completed = subprocess.run(
        (sys.executable, "-m", MODULE, str(tmp_path)),
        input=b"readable.txt\nunreadable.txt\n",
        capture_output=True,
        check=False,
        cwd=ROOT,
    )

    assert completed.returncode == 0
    assert completed.stdout == b"unreadable.txt\n"
    assert completed.stderr == b""
