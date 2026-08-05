import ast
from pathlib import Path


ROOT = Path(__file__).parents[1]
PROCESS = (
    ROOT
    / "src/silmaril/sparky/morphism/codebase/volume/inventory/module/process.py"
)


def test_inventory_module_process_is_one_raw_total_arrow() -> None:
    source = PROCESS.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(PROCESS))
    functions = tuple(
        node for node in tree.body if isinstance(node, ast.FunctionDef)
    )

    assert tuple(node.name for node in functions) == ("MAIN",)
    assert ".apply import" not in source
    assert "json" not in source.lower()
    assert "base64" not in source.lower()
    assert "pickle" not in source.lower()
    assert "importlib" not in source.lower()
    assert not any(isinstance(node, ast.ExceptHandler) for node in ast.walk(tree))
    assert ".write(" not in source

    applications = tuple(
        node
        for node in ast.walk(functions[0])
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id == "SUBPROCESS"
        and node.func.attr == "run"
    )
    assert len(applications) == 1
