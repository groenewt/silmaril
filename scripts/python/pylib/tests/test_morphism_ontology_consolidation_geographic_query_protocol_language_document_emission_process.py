import ast
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).parents[1]
REPOSITORY = Path(__file__).parents[4]
COMMITTED_DOCUMENT = REPOSITORY / "ontology/geosparql.sparql"
MODULE = (
    "silmaril.sparky.morphism.ontology.consolidation"
    ".geographic.query.protocol.language.document.emission.process"
)
RUNTIME_FILE = (
    ROOT
    / "src/silmaril/sparky/morphism/ontology/consolidation"
    / "geographic/query/protocol/language/document/emission/process.py"
)
ENVIRONMENT = {
    **os.environ,
    "PYTHONDONTWRITEBYTECODE": "1",
    "PYTHONPATH": str(ROOT / "src"),
}


def test_geographic_query_document_emission_reproduces_committed_document_bytes() -> None:
    completed = subprocess.run(
        (sys.executable, "-m", MODULE),
        capture_output=True,
        check=False,
        env=ENVIRONMENT,
        input=b"",
    )

    assert completed.returncode == 0
    assert completed.stderr == b""
    assert completed.stdout == COMMITTED_DOCUMENT.read_bytes()


def test_geographic_query_document_emission_is_one_gated_projection() -> None:
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
    emissions = tuple(
        node
        for node in ast.walk(functions[0])
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "write"
    )
    assert len(emissions) == 1
