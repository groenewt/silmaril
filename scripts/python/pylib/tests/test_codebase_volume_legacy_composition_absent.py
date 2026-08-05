import ast
from pathlib import Path


_ROOT = Path(__file__).parents[1]
_CONSTANT_ROOT = _ROOT / "src/config/constants/morphism/codebase/volume"
_GATE_ROOT = _ROOT / "src/config/gate/external/python/morphism/codebase/volume"
_RUNTIME_ROOT = _ROOT / "src/silmaril/sparky/morphism/codebase/volume"
_FORBIDDEN_TEXT = (
    ".apply import",
    "importlib",
    "INVALID",
    "PROJECT",
    "TRANSFORM",
)


def test_legacy_multi_application_composition_is_absent() -> None:
    runtime_paths = tuple(_RUNTIME_ROOT.rglob("*.py"))
    constant_paths = tuple(_CONSTANT_ROOT.rglob("*.py"))
    process_paths = tuple(_RUNTIME_ROOT.rglob("process.py"))

    assert not tuple(_GATE_ROOT.rglob("*.py"))
    assert not tuple(_RUNTIME_ROOT.rglob("apply.py"))
    assert not tuple(_RUNTIME_ROOT.rglob("*codec*"))
    assert not tuple(_RUNTIME_ROOT.rglob("*transition*"))
    assert not tuple(_RUNTIME_ROOT.rglob("*dispatch*"))
    assert not tuple(_CONSTANT_ROOT.rglob("*transition*"))

    for path in runtime_paths + constant_paths:
        source = path.read_text(encoding="utf-8")
        assert all(token not in source for token in _FORBIDDEN_TEXT), path

    for path in process_paths:
        tree = ast.parse(path.read_bytes(), filename=str(path))
        assert not any(isinstance(node, ast.ExceptHandler) for node in ast.walk(tree)), path
        assert not any(isinstance(node, ast.NamedExpr) for node in ast.walk(tree)), path
        subprocess_calls = tuple(
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "SUBPROCESS"
            and node.func.attr == "run"
        )
        assert len(subprocess_calls) <= 1, path
