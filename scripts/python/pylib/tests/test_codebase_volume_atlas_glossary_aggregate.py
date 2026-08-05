import ast
import csv
import os
from pathlib import Path
import subprocess
import sys


_ROOT = Path(__file__).parents[1]
_RUNTIME_ROOT = (
    _ROOT
    / "src/silmaril/sparky/morphism/codebase/volume/atlas/glossary/aggregate"
)
_LEDGER = _ROOT / "tests/fixtures/codebase_volume_atlas_glossary_process_ledger.csv"
_MAKE = _ROOT / "make/morphism/codebase/volume/atlas/glossary/aggregate.mk"
_FIXTURE = _ROOT / "tests/fixtures/atlas_glossary"


def _source_roots() -> str:
    local = _ROOT / "src"
    dependency = Path("/data/src/scripts/pylib/src")
    return str(local) if (local / "config/gate/external/python/stdlib/subprocess/library.py").is_file() else f"{local}:{dependency}"


def test_atlas_glossary_is_one_physical_application_per_frame_and_matches_legacy_bytes(tmp_path: Path) -> None:
    with _LEDGER.open(newline="", encoding="utf-8") as stream:
        ledger = tuple(csv.DictReader(stream))
    runtime_paths = tuple(sorted(_RUNTIME_ROOT.rglob("process.py")))
    make_source = _MAKE.read_text(encoding="utf-8")
    recipes = tuple(line for line in make_source.splitlines() if line.startswith("\t"))

    assert len(ledger) == 16
    assert {(_ROOT / row["runtime_file"]) for row in ledger} == set(runtime_paths)
    assert len(recipes) == 16
    assert "define " not in make_source
    assert all(line.count(" -m ") == 1 for line in recipes)
    assert all(token not in "\n".join(recipes) for token in (";", "&&", "||", " set ", " rm ", " cp ", " mv ", " printf ", " cat "))

    for row in ledger:
        path = _ROOT / row["runtime_file"]
        tree = ast.parse(path.read_bytes(), filename=str(path))
        functions = tuple(node for node in tree.body if isinstance(node, ast.FunctionDef))
        applications = tuple(
            node
            for node in ast.walk(functions[0])
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "SUBPROCESS"
            and node.func.attr == "run"
        )
        assert tuple(function.name for function in functions) == ("MAIN",)
        assert len(applications) == 1
        assert row["semantic_application_count"] == "1"
        assert row["project_local_function_imports"] == ""
        assert row["invoked_project_local_functions"] == ""
        assert not any(isinstance(node, (ast.Try, ast.TryStar, ast.For, ast.While)) for node in ast.walk(tree))
        assert f'-m {row["module"]}' in make_source

    output = tmp_path / "observed.csv"
    command = (
        "make",
        "--no-print-directory",
        "-f",
        str(_MAKE),
        "atlas-glossary-aggregate",
        f"ATLAS_GLOSSARY_PYTHON={sys.executable}",
        f"ATLAS_GLOSSARY_PYLIB_SOURCE_ROOT={_source_roots()}",
        f"ATLAS_GLOSSARY_ROW_SOURCE_DIRECTORY={_FIXTURE / 'rows'}",
        f"ATLAS_GLOSSARY_HEADER_TEMPLATE={_FIXTURE / 'header.csv.template'}",
        f"ATLAS_GLOSSARY_OUTPUT={output}",
    )
    result = subprocess.run(
        command,
        cwd=_ROOT,
        env=os.environ | {"PYTHONDONTWRITEBYTECODE": "1"},
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert output.read_bytes() == (_FIXTURE / "expected.csv").read_bytes()
    assert all(path.read_bytes() == b"" for path in tmp_path.rglob("*.stderr"))

    empty_rows = tmp_path / "empty-rows"
    empty_rows.mkdir()
    rejected = subprocess.run(
        (
            *command[:-3],
            f"ATLAS_GLOSSARY_ROW_SOURCE_DIRECTORY={empty_rows}",
            command[-2],
            f"ATLAS_GLOSSARY_OUTPUT={tmp_path / 'rejected.csv'}",
        ),
        cwd=_ROOT,
        env=os.environ | {"PYTHONDONTWRITEBYTECODE": "1"},
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    assert rejected.returncode != 0
    assert not (tmp_path / "rejected.csv").exists()

