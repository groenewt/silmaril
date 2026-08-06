import ast
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).parents[1]
REPOSITORY = Path(__file__).parents[4]
TRUST_MODEL = REPOSITORY / "basicttl/commit_signing_trust.ttl"
COMMITTED_MANIFEST = REPOSITORY / "keys/trust-manifest.txt"
EXTRACTION_MODULE = "silmaril.sparky.morphism.provenance.trust.manifest.extraction.process"
RENDER_MODULE = "silmaril.sparky.morphism.provenance.trust.manifest.render.process"
RUNTIME_FILE = ROOT / "src/silmaril/sparky/morphism/provenance/trust/manifest/render/process.py"
COMMAND_FILE = (
    ROOT
    / "src/config/constants/morphism/provenance/trust/manifest/render/process/command/value.py"
)
ENVIRONMENT = {
    **os.environ,
    "PYTHONDONTWRITEBYTECODE": "1",
    "PYTHONPATH": str(ROOT / "src"),
}


def test_render_process_reproduces_committed_manifest_bytes() -> None:
    extracted = subprocess.run(
        (sys.executable, "-m", EXTRACTION_MODULE),
        capture_output=True,
        check=False,
        env=ENVIRONMENT,
        input=TRUST_MODEL.read_bytes(),
    )
    assert extracted.returncode == 0
    assert extracted.stderr == b""

    rendered = subprocess.run(
        (sys.executable, "-m", RENDER_MODULE),
        capture_output=True,
        check=False,
        env=ENVIRONMENT,
        input=extracted.stdout,
    )
    assert rendered.returncode == 0
    assert rendered.stderr == b""
    assert rendered.stdout == COMMITTED_MANIFEST.read_bytes()


def test_render_process_is_one_total_child_application() -> None:
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

    command_tree = ast.parse(COMMAND_FILE.read_bytes(), filename=str(COMMAND_FILE))
    assignments = tuple(node for node in command_tree.body if isinstance(node, ast.Assign))
    assert len(assignments) == 1
    assert assignments[0].targets[0].id == "VALUE"
    command = ast.literal_eval(assignments[0].value)
    assert command[0] == "python3"
    assert command[1] == "-c"
