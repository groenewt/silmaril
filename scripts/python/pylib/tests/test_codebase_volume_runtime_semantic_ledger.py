import ast
import csv
from pathlib import Path


ROOT = Path(__file__).parents[1]
RUNTIME_ROOT = ROOT / "src/silmaril/sparky/morphism/codebase/volume"
CONSTANT_ROOT = ROOT / "src/config/constants/morphism/codebase/volume"
VOLUME_GATE_ROOT = ROOT / "src/config/gate/external/python/morphism/codebase/volume"
FIXTURE_ROOT = ROOT / "tests/fixtures"
LEDGERS = (
    FIXTURE_ROOT / "codebase_volume_make_process_inventory.csv",
    *sorted(FIXTURE_ROOT.glob("codebase_volume_*_process_ledger.csv")),
)
STDLIB_GATE_PREFIX = "config.gate.external.python.stdlib."
PROJECT_PREFIXES = (
    "silmaril.",
    "config.gate.external.project.",
    "config.gate.external.python.",
)


def test_every_volume_runtime_is_one_transitively_closed_semantic_arrow() -> None:
    rows = []
    for ledger in LEDGERS:
        with ledger.open(newline="", encoding="utf-8") as stream:
            rows.extend(csv.DictReader(stream))
    paths = tuple(sorted(RUNTIME_ROOT.rglob("process.py")))

    assert len(rows) == len(paths)
    assert {ROOT / row["runtime_file"] for row in rows} == set(paths)
    assert not tuple(VOLUME_GATE_ROOT.rglob("library.py"))
    assert not (VOLUME_GATE_ROOT / "codec/library.py").exists()
    assert not (VOLUME_GATE_ROOT / "source/observation/path/library.py").exists()

    reachable_libraries = set()
    for row in rows:
        path = ROOT / row["runtime_file"]
        tree = ast.parse(path.read_bytes(), filename=str(path))
        functions = tuple(node for node in tree.body if isinstance(node, ast.FunctionDef))
        imports = {
            alias.asname or alias.name: node.module
            for node in tree.body
            if isinstance(node, ast.ImportFrom)
            for alias in node.names
        }
        project_function_imports = {
            name
            for name, module in imports.items()
            if module
            and module.startswith(PROJECT_PREFIXES)
            and not module.startswith(STDLIB_GATE_PREFIX)
            and name not in {"COMMAND", "CONTAINED", "ESCAPED", "EXPECTED"}
        }
        invoked_project_functions = {
            node.func.id
            for node in ast.walk(functions[0])
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id in project_function_imports
        }
        subprocess_calls = tuple(
            node
            for node in ast.walk(functions[0])
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "SUBPROCESS"
            and node.func.attr == "run"
        )

        assert tuple(node.name for node in functions) == ("MAIN",), path
        assert row.get("input_contract") or row.get("x"), path
        assert row.get("output_contract") or row.get("y"), path
        assert row.get("error_contract") or row.get("error"), path
        assert row["semantic_application_count"] == "1", path
        assert row["invoked_project_local_functions"] == "", path
        assert invoked_project_functions == set(), path
        assert row.get("external_application") or row.get("f")
        assert len(subprocess_calls) == 1

        reachable_libraries.update(
            ROOT / "src" / Path(module.replace(".", "/") + ".py")
            for module in imports.values()
            if module and module.startswith(STDLIB_GATE_PREFIX)
        )

    assert reachable_libraries == {
        ROOT / "src/config/gate/external/python/stdlib/subprocess/library.py",
        ROOT / "src/config/gate/external/python/stdlib/sys/library.py",
    }
    for path in reachable_libraries:
        tree = ast.parse(path.read_bytes(), filename=str(path))
        assert not tuple(node for node in tree.body if isinstance(node, ast.FunctionDef)), path
        assert not tuple(node for node in ast.walk(tree) if isinstance(node, ast.Call)), path

    for path in CONSTANT_ROOT.rglob("*.py"):
        tree = ast.parse(path.read_bytes(), filename=str(path))
        assert not tuple(node for node in tree.body if isinstance(node, ast.FunctionDef)), path
        assert not any(
            isinstance(node, ast.ImportFrom)
            and node.module
            and node.module.startswith(PROJECT_PREFIXES)
            and any(alias.name not in {"VALUE"} for alias in node.names)
            for node in tree.body
        ), path
