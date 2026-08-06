import ast
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).parents[1]
REPOSITORY = Path(__file__).parents[4]
COMMITTED_MANIFEST = REPOSITORY / "ontology/manifest.ttl"
MODULE = "silmaril.sparky.morphism.ontology.consolidation.manifest.render.process"
RUNTIME_FILE = (
    ROOT / "src/silmaril/sparky/morphism/ontology/consolidation/manifest/render/process.py"
)
ENVIRONMENT = {
    **os.environ,
    "PYTHONDONTWRITEBYTECODE": "1",
    "PYTHONPATH": str(ROOT / "src"),
}


def test_manifest_render_process_reproduces_committed_manifest_bytes(
    tmp_path: Path,
) -> None:
    corpus_tally = tmp_path / "corpus-tally"
    corpus_tally.write_bytes(b"30084\n")
    statement_tally = tmp_path / "statement-tally"
    statement_tally.write_bytes(b"177683\n")
    entity_tally = tmp_path / "entity-tally"
    entity_tally.write_bytes(b"59794\n")

    completed = subprocess.run(
        (
            sys.executable,
            "-m",
            MODULE,
            str(corpus_tally),
            str(statement_tally),
            str(entity_tally),
        ),
        capture_output=True,
        check=False,
        env=ENVIRONMENT,
    )

    assert completed.returncode == 0
    assert completed.stderr == b""
    assert completed.stdout == COMMITTED_MANIFEST.read_bytes()


def test_manifest_render_process_is_one_total_child_application() -> None:
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
