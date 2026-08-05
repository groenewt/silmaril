import ast
from pathlib import Path


ROOT = Path(__file__).parents[1]
VOLUME_ROOTS = (
    ROOT / "src/config/constants/morphism/codebase/volume",
    ROOT / "src/silmaril/sparky/morphism/codebase/volume",
)
def test_every_audited_python_file_declares_one_total_application() -> None:
    source_paths = {
        path
        for volume_root in VOLUME_ROOTS
        for path in volume_root.rglob("*.py")
    }
    expected_paths = source_paths | set(
        (ROOT / "tests").glob("test_codebase_volume_*.py")
    )

    assert expected_paths

    for path in expected_paths:
        tree = ast.parse(path.read_bytes(), filename=str(path))
        symbols = []
        for node in tree.body:
            if isinstance(node, (ast.ClassDef, ast.FunctionDef)) and not node.name.startswith("_"):
                symbols.append(node.name)
            if isinstance(node, ast.Assign):
                symbols.extend(
                    target.id
                    for target in node.targets
                    if isinstance(target, ast.Name) and not target.id.startswith("_")
                )
            if isinstance(node, ast.AnnAssign):
                target = node.target
                if isinstance(target, ast.Name) and not target.id.startswith("_"):
                    symbols.append(target.id)
        if path.name == "process.py":
            assert tuple(symbols) == ("MAIN",), path
        elif path.name.startswith("test_codebase_volume_"):
            tests = tuple(
                node.name
                for node in tree.body
                if isinstance(node, ast.FunctionDef) and node.name.startswith("test_")
            )
            assert len(tests) == 1, path
        else:
            assert tuple(symbols) == ("VALUE",), (path, symbols)
