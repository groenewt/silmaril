import ast
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).parents[1]
REPOSITORY = Path(__file__).parents[4]
COMMITTED_DOCUMENT = REPOSITORY / "ontology/shapes.ttl"
MODULE = (
    "silmaril.sparky.morphism.ontology.consolidation"
    ".shapes.constraint.language.document.render.process"
)
RUNTIME_FILE = (
    ROOT
    / "src/silmaril/sparky/morphism/ontology/consolidation"
    / "shapes/constraint/language/document/render/process.py"
)
ENVIRONMENT = {
    **os.environ,
    "PYTHONDONTWRITEBYTECODE": "1",
    "PYTHONPATH": str(ROOT / "src"),
}


def test_shapes_render_process_reproduces_committed_document_bytes() -> None:
    committed = COMMITTED_DOCUMENT.read_bytes()
    declarations = committed.split(b"\n\n# Silmaril SHACL Shapes", 1)[0] + b"\n"

    completed = subprocess.run(
        (sys.executable, "-m", MODULE),
        capture_output=True,
        check=False,
        env=ENVIRONMENT,
        input=declarations,
    )

    assert completed.returncode == 0
    assert completed.stderr == b""
    assert completed.stdout == committed


def test_shapes_render_process_is_one_gated_combination() -> None:
    tree = ast.parse(RUNTIME_FILE.read_bytes(), filename=str(RUNTIME_FILE))
    functions = tuple(node for node in tree.body if isinstance(node, ast.FunctionDef))
    assert tuple(node.name for node in functions) == ("MAIN",)
    assert not tuple(
        node
        for node in ast.walk(functions[0])
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "run"
    )
    combinations = tuple(
        node
        for node in ast.walk(functions[0])
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add)
    )
    assert len(combinations) == 1
