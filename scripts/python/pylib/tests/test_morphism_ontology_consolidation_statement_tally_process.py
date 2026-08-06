import ast
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).parents[1]
REPOSITORY = Path(__file__).parents[4]
COMMITTED_CONSOLIDATED = REPOSITORY / "ontology/silmaril-consolidated.ttl"
MODULE = "silmaril.sparky.morphism.ontology.consolidation.statement.tally.process"
RUNTIME_FILE = (
    ROOT / "src/silmaril/sparky/morphism/ontology/consolidation/statement/tally/process.py"
)
ENVIRONMENT = {
    **os.environ,
    "PYTHONDONTWRITEBYTECODE": "1",
    "PYTHONPATH": str(ROOT / "src"),
}


def test_statement_tally_process_counts_terminated_statement_lines() -> None:
    completed = subprocess.run(
        (sys.executable, "-m", MODULE),
        capture_output=True,
        check=False,
        env=ENVIRONMENT,
        input=b"s .\n# t .\np ;\n\n@prefix q: <u> .\nplain\n  .  \n",
    )

    assert completed.returncode == 0
    assert completed.stderr == b""
    assert completed.stdout == b"3\n"


def test_statement_tally_process_matches_committed_manifest_estimate() -> None:
    completed = subprocess.run(
        (sys.executable, "-m", MODULE),
        capture_output=True,
        check=False,
        env=ENVIRONMENT,
        input=COMMITTED_CONSOLIDATED.read_bytes(),
    )

    assert completed.returncode == 0
    assert completed.stderr == b""
    assert completed.stdout == b"177683\n"


def test_statement_tally_process_is_one_total_child_application() -> None:
    tree = ast.parse(RUNTIME_FILE.read_bytes(), filename=str(RUNTIME_FILE))
    functions = tuple(node for node in tree.body if isinstance(node, ast.FunctionDef))
    assert tuple(node.name for node in functions) == ("MAIN",)
    assert len(functions[0].body) == 1
    child_applications = tuple(
        node
        for node in ast.walk(functions[0])
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id == "SUBPROCESS"
        and node.func.attr == "run"
    )
    assert len(child_applications) == 1
