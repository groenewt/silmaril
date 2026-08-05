from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parents[1]
MODULE = "silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.process"


def test_name_segment_exclusion_matches_declared_names_at_every_depth(tmp_path: Path) -> None:
    (tmp_path / "keep").mkdir()
    (tmp_path / "keep/visible.txt").write_text("visible", encoding="utf-8")
    (tmp_path / "nested/node_modules/pkg").mkdir(parents=True)
    (tmp_path / "nested/node_modules/pkg/module.js").write_text("module", encoding="utf-8")
    (tmp_path / "nested/cache_like").mkdir(parents=True)
    (tmp_path / "nested/cache_like/value.txt").write_text("value", encoding="utf-8")
    (tmp_path / "__pycache__").mkdir()
    (tmp_path / "__pycache__/value.pyc").write_bytes(b"bytecode")
    completed = subprocess.run(
        (sys.executable, "-m", MODULE, str(tmp_path), "node_modules", "__pycache__"),
        input=b"keep/visible.txt\nnested/node_modules/pkg/module.js\nnested/cache_like/value.txt\n__pycache__/value.pyc\n",
        capture_output=True,
        check=False,
        cwd=ROOT,
    )

    assert completed.returncode == 0
    assert completed.stdout == b"__pycache__/value.pyc\nnested/node_modules/pkg/module.js\n"
    assert completed.stderr == b""
