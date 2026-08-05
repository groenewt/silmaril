import ast
import csv
from pathlib import Path


_ROOT = Path(__file__).parents[1]
_RUNTIME_ROOT = _ROOT / "src/silmaril/sparky/morphism/contract/validation"
_OWNED_ROOTS = (
    _ROOT / "src/config/constants/morphism/contract/validation",
    _ROOT / "src/config/gate/external/project/sparky/morphism/contract/validation",
    _ROOT / "src/config/gate/external/python/morphism/contract/validation",
    _RUNTIME_ROOT,
)
_LEDGER = _ROOT / "tests/fixtures/contract_validation_process_ledger.csv"
_PROJECT_PREFIXES = ("config.", "silmaril.")
_ALLOWED_PROJECT_IMPORTS = {"VALUE", "DEPENDENCY"}


def test_contract_validation_files_are_single_total_applications() -> None:
    with _LEDGER.open(newline="", encoding="utf-8") as stream:
        rows = tuple(csv.DictReader(stream))

    expected_header = (
        "edge",
        "module",
        "runtime_file",
        "input_contract",
        "semantic_application",
        "output_contract",
        "error_contract",
        "semantic_application_count",
        "project_local_function_imports",
        "invoked_project_local_functions",
        "make_composition_coordinate",
    )
    process_paths = tuple(sorted(_RUNTIME_ROOT.rglob("process.py")))
    owned_paths = tuple(
        sorted(path for root in _OWNED_ROOTS for path in root.rglob("*.py"))
    )

    assert tuple(rows[0]) == expected_header
    assert len(rows) == len(process_paths)
    assert len({row["edge"] for row in rows}) == len(rows)
    assert {(_ROOT / row["runtime_file"]) for row in rows} == set(process_paths)
    assert not tuple(_RUNTIME_ROOT.rglob("apply.py"))

    for row in rows:
        assert row["input_contract"]
        assert row["semantic_application"]
        assert row["output_contract"]
        assert row["error_contract"]
        assert row["semantic_application_count"] == "1"
        assert row["project_local_function_imports"] == ""
        assert row["invoked_project_local_functions"] == ""
        assert row["make_composition_coordinate"].startswith(
            "morphism-contract-validation-"
        )

    for path in owned_paths:
        tree = ast.parse(path.read_bytes(), filename=str(path))
        assert not tuple(node for node in ast.walk(tree) if isinstance(node, ast.Try)), path
        assert not tuple(
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id in {"eval", "exec", "__import__"}
        ), path
        assert not tuple(
            node
            for node in tree.body
            if isinstance(node, ast.Import)
            and any(alias.name == "importlib" for alias in node.names)
        ), path

        project_imports = tuple(
            alias
            for node in tree.body
            if isinstance(node, ast.ImportFrom)
            and node.module
            and node.module.startswith(_PROJECT_PREFIXES)
            for alias in node.names
        )
        project_local_function_imports = tuple(
            alias.name
            for alias in project_imports
            if alias.name not in _ALLOWED_PROJECT_IMPORTS
        )
        assert project_local_function_imports == (), path

        public = []
        for node in tree.body:
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                public.extend(
                    alias.asname or alias.name
                    for alias in node.names
                    if not (alias.asname or alias.name).startswith("_")
                )
            if isinstance(node, (ast.ClassDef, ast.FunctionDef)) and not node.name.startswith("_"):
                public.append(node.name)
            if isinstance(node, ast.Assign):
                public.extend(
                    target.id
                    for target in node.targets
                    if isinstance(target, ast.Name) and not target.id.startswith("_")
                )
            if isinstance(node, ast.AnnAssign):
                target = node.target
                if isinstance(target, ast.Name) and not target.id.startswith("_"):
                    public.append(target.id)

        if path.name == "process.py":
            runtime_relative = path.relative_to(_RUNTIME_ROOT).as_posix()
            row = next(
                item for item in rows if item["runtime_file"].endswith(runtime_relative)
            )
            semantic_calls = tuple(
                node
                for node in ast.walk(tree)
                if isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and (
                    (
                        "/classification/" in row["edge"]
                        and node.func.attr == "sub"
                    )
                    or (
                        row["edge"].endswith("/source")
                        and node.func.attr == "join"
                    )
                )
            )
            if "/classification/" in row["edge"] or row["edge"].endswith("/source"):
                assert len(semantic_calls) == 1, (path, semantic_calls)

            functions = tuple(
                node for node in tree.body if isinstance(node, ast.FunctionDef)
            )
            assert tuple(node.name for node in functions) == ("MAIN",), path
            assert public == ["MAIN"], path
            assert not tuple(node for node in tree.body if isinstance(node, ast.ClassDef)), path
        elif path.name == "value.py":
            assert public == ["VALUE"], (path, public)
            assert not tuple(node for node in tree.body if isinstance(node, ast.FunctionDef)), path
            assert not tuple(node for node in ast.walk(tree) if isinstance(node, ast.Call)), path
        elif path.name == "library.py":
            assert public == ["DEPENDENCY"], (path, public)
            assert not tuple(node for node in tree.body if isinstance(node, ast.FunctionDef)), path
            assert not tuple(node for node in ast.walk(tree) if isinstance(node, ast.Call)), path
        else:
            raise AssertionError(path)
