import ast
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).parents[1]
MODULE = "silmaril.sparky.morphism.ontology.consolidation.consolidated.render.process"
RUNTIME_FILE = (
    ROOT
    / "src/silmaril/sparky/morphism/ontology/consolidation/consolidated/render/process.py"
)
ENVIRONMENT = {
    **os.environ,
    "PYTHONDONTWRITEBYTECODE": "1",
    "PYTHONPATH": str(ROOT / "src"),
}


def test_consolidated_render_process_frames_header_declarations_and_blocks(
    tmp_path: Path,
) -> None:
    tally = tmp_path / "corpus-tally"
    tally.write_bytes(b"3\n")
    declarations = tmp_path / "namespace-declarations"
    declarations.write_bytes(b"@prefix a: <urn:a#> .\n@prefix b: <urn:b#> .\n")

    completed = subprocess.run(
        (sys.executable, "-m", MODULE, str(tally), str(declarations)),
        capture_output=True,
        check=False,
        env=ENVIRONMENT,
        input=b"\n# Source: x.ttl\nbody .\n",
    )

    assert completed.returncode == 0
    assert completed.stderr == b""
    assert completed.stdout == (
        b"# Silmaril Consolidated Ontology\n"
        b"# Generated from 3 TTL files\n"
        b"# This file is machine-generated; edit the source files in basicttl/\n"
        b"\n"
        b"@prefix a: <urn:a#> .\n"
        b"@prefix b: <urn:b#> .\n"
        b"\n# Source: x.ttl\nbody .\n"
    )


def test_consolidated_render_process_is_one_total_child_application() -> None:
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
