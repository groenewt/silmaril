import os
from pathlib import Path
import subprocess
import sys


_ROOT = Path(__file__).parents[1]
_MODULE = "silmaril.sparky.morphism.codebase.volume.source.observation.symlink.process"


def test_symlink_observation_includes_broken_and_escaping_loci(tmp_path: Path) -> None:
    (tmp_path / "broken").symlink_to("missing")
    (tmp_path / "escaping").symlink_to(tmp_path.parent)
    (tmp_path / "_build").mkdir()
    (tmp_path / "_build/ignored").symlink_to("missing")
    (tmp_path / "generated").mkdir()
    (tmp_path / "generated/ignored").symlink_to("missing")

    result = subprocess.run(
        (
            sys.executable,
            "-m",
            _MODULE,
            str(tmp_path),
            "-not",
            "-path",
            "./generated/*",
        ),
        capture_output=True,
        cwd=_ROOT,
        env=os.environ | {
            "PYTHONDONTWRITEBYTECODE": "1",
            "PYTHONPATH": str(_ROOT / "src"),
        },
        check=False,
    )

    assert result.returncode == 0
    assert set(result.stdout.splitlines()) == {b"./broken", b"./escaping"}
    assert result.stderr == b""
