from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parents[1]
PATHS = b"tables/source_files.tex\ntables/modules.tex\ntables/public_apis.tex\ntables/dependencies.tex\n"


def test_architecture_chapter_construct_accepts_only_its_ordered_include_domain(tmp_path: Path) -> None:
    input_path = tmp_path / "architecture.paths"
    output_root = tmp_path / "output"
    input_path.write_bytes(PATHS)
    completed = subprocess.run(
        (
            "make",
            "volume-projection-chapter-architecture",
            f"SILMARIL_PYTHON={sys.executable}",
            f"VOLUME_PROJECTION_ARCHITECTURE_INPUT={input_path}",
            f"VOLUME_PROJECTION_OUTPUT_ROOT={output_root}",
        ),
        capture_output=True,
        check=False,
        cwd=ROOT,
    )

    assert completed.returncode == 0
    assert (output_root / "00_architecture.tex").read_bytes() == b"\\chapter{Architecture and Source Surface}\n\\input{tables/source_files.tex}\n\\input{tables/modules.tex}\n\\input{tables/public_apis.tex}\n\\input{tables/dependencies.tex}\n"
