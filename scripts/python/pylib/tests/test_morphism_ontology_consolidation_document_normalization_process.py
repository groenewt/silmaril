import ast
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).parents[1]
MODULE = "silmaril.sparky.morphism.ontology.consolidation.document.normalization.process"
RUNTIME_FILE = (
    ROOT
    / "src/silmaril/sparky/morphism/ontology/consolidation/document/normalization/process.py"
)
ENVIRONMENT = {
    **os.environ,
    "PYTHONDONTWRITEBYTECODE": "1",
    "PYTHONPATH": str(ROOT / "src"),
}


def test_normalization_process_encodes_tokens_and_assembles_source_blocks(
    tmp_path: Path,
) -> None:
    (tmp_path / "alpha.ttl").write_text(
        "@prefix silm: <urn:silmaril:entity#> .\n"
        "# comment line\n"
        "silm:anchor#one a owl:NamedIndividual ;\n"
        '    rdfs:label "kept # \\" raw" ;\n'
        "    silm:link silm:path%2Fkept%2 .\n",
        encoding="utf-8",
    )
    (tmp_path / "beta.ttl").write_text("   \n\n", encoding="utf-8")
    (tmp_path / "delta.ttl").write_text("(silm:x> a silm:y .\n", encoding="utf-8")
    (tmp_path / "gamma.ttl").write_text(
        "@prefix owl: <http://www.w3.org/2002/07/owl#> .\n", encoding="utf-8"
    )

    completed = subprocess.run(
        (sys.executable, "-m", MODULE, str(tmp_path)),
        capture_output=True,
        check=False,
        env=ENVIRONMENT,
        input=b"alpha.ttl\nbeta.ttl\ndelta.ttl\ngamma.ttl\n",
    )

    assert completed.returncode == 0
    assert completed.stderr == b""
    assert completed.stdout == (
        b"\n# Source: alpha.ttl\n"
        b"silm:anchor%23one a owl:NamedIndividual ;\n"
        b'    rdfs:label "kept # \\" raw" ;\n'
        b"    silm:link silm:path%2Fkept%252 .\n"
        b"\n"
        b"\n# Source: delta.ttl\n"
        b"(silm:x%3E a silm:y .\n"
    )


def test_normalization_process_is_one_total_child_application() -> None:
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
