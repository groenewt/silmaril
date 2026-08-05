import os
from pathlib import Path
import subprocess
import sys

from config.constants.morphism.codebase.volume.source.ignore.name.value import VALUE as IGNORE_NAMES


_ROOT = Path(__file__).parents[1]
_MODULE = "silmaril.sparky.morphism.codebase.volume.inventory.source_files.process"


def test_source_files_observes_live_paths_with_configured_exclusions(tmp_path: Path) -> None:
    (tmp_path / "keep.txt").write_text("keep", encoding="utf-8")
    (tmp_path / "generated").mkdir()
    (tmp_path / "generated/output.txt").write_text("generated", encoding="utf-8")
    for name in IGNORE_NAMES:
        ignored = tmp_path / name
        ignored.mkdir()
        (ignored / "ignored.txt").write_text("ignored", encoding="utf-8")

    result = subprocess.run(
        (
            sys.executable,
            "-m",
            _MODULE,
            str(tmp_path),
            "--glob",
            "!generated/**",
            *(
                argument
                for name in IGNORE_NAMES
                for argument in ("--glob", f"!{name}/**")
            ),
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
    assert result.stdout == b"./keep.txt\n"
    assert result.stderr == b""
