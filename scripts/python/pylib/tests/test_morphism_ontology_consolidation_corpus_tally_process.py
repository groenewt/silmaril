import ast
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).parents[1]
MODULE = "silmaril.sparky.morphism.ontology.consolidation.corpus.tally.process"
RUNTIME_FILE = (
    ROOT / "src/silmaril/sparky/morphism/ontology/consolidation/corpus/tally/process.py"
)
ENVIRONMENT = {
    **os.environ,
    "PYTHONDONTWRITEBYTECODE": "1",
    "PYTHONPATH": str(ROOT / "src"),
}


def test_corpus_tally_process_counts_only_non_empty_documents(tmp_path: Path) -> None:
    (tmp_path / "alpha.ttl").write_text("x .\n", encoding="utf-8")
    (tmp_path / "beta.ttl").write_text("  \n\n", encoding="utf-8")
    (tmp_path / "gamma.ttl").write_text("y\n", encoding="utf-8")

    completed = subprocess.run(
        (sys.executable, "-m", MODULE, str(tmp_path)),
        capture_output=True,
        check=False,
        env=ENVIRONMENT,
        input=b"alpha.ttl\nbeta.ttl\ngamma.ttl\n",
    )

    assert completed.returncode == 0
    assert completed.stderr == b""
    assert completed.stdout == b"2\n"


def test_corpus_tally_process_is_one_total_child_application() -> None:
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
