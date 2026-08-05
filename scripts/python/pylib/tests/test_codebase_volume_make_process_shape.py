import ast
from pathlib import Path


ROOT = Path(__file__).parents[1]
ARROW_ROOT = ROOT / "src/silmaril/sparky/morphism/codebase/volume"
FORBIDDEN_NODES = (
    ast.AsyncFor,
    ast.DictComp,
    ast.For,
    ast.GeneratorExp,
    ast.Lambda,
    ast.ListComp,
    ast.NamedExpr,
    ast.SetComp,
    ast.While,
)


def test_every_make_process_is_one_raw_total_arrow() -> None:
    process_paths = tuple(sorted(ARROW_ROOT.rglob("process.py")))
    assert process_paths

    for path in process_paths:
        source = path.read_text(encoding="utf-8")
        tree = ast.parse(source, filename=str(path))
        functions = tuple(
            node for node in tree.body if isinstance(node, ast.FunctionDef)
        )
        import_roots = {
            alias.name.split(".")[0]
            for node in tree.body
            if isinstance(node, ast.Import)
            for alias in node.names
        } | {
            node.module.split(".")[0]
            for node in tree.body
            if isinstance(node, ast.ImportFrom) and node.module
        }

        assert tuple(node.name for node in functions) == ("MAIN",), path
        assert ".apply import" not in source, path
        assert not import_roots & {"base64", "importlib", "json", "pickle"}, path
        assert ".write(" not in source, path
        assert not any(isinstance(node, ast.ExceptHandler) for node in ast.walk(tree)), path
        assert not any(isinstance(node, FORBIDDEN_NODES) for node in ast.walk(tree)), path

        command_applications = tuple(
            node
            for node in ast.walk(functions[0])
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "SUBPROCESS"
            and node.func.attr == "run"
        )
        assert len(command_applications) == 1, path
