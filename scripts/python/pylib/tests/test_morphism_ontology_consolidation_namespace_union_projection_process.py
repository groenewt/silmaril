import ast
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).parents[1]
MODULE = "silmaril.sparky.morphism.ontology.consolidation.namespace.union.projection.process"
RUNTIME_FILE = (
    ROOT
    / "src/silmaril/sparky/morphism/ontology/consolidation/namespace/union/projection/process.py"
)
ENVIRONMENT = {
    **os.environ,
    "PYTHONDONTWRITEBYTECODE": "1",
    "PYTHONPATH": str(ROOT / "src"),
}


def test_union_process_merges_new_declarations_and_keeps_defaults(tmp_path: Path) -> None:
    (tmp_path / "alpha.ttl").write_text(
        "@prefix void: <http://rdfs.org/ns/void#> .\n"
        "@prefix silm: <urn:conflicting:redefinition#> .\n"
        "silm:a a silm:b .\n",
        encoding="utf-8",
    )
    (tmp_path / "beta.ttl").write_text("   \n\n", encoding="utf-8")
    (tmp_path / "gamma.ttl").write_text("@prefix aaa: <urn:aaa#> .\n", encoding="utf-8")

    completed = subprocess.run(
        (sys.executable, "-m", MODULE, str(tmp_path)),
        capture_output=True,
        check=False,
        env=ENVIRONMENT,
        input=b"alpha.ttl\nbeta.ttl\ngamma.ttl\n",
    )

    assert completed.returncode == 0
    assert completed.stderr == b""
    assert completed.stdout == (
        b"@prefix aaa: <urn:aaa#> .\n"
        b"@prefix cceo: <https://www.commoncoreontologies.org/cpo#> .\n"
        b"@prefix cco: <https://www.commoncoreontologies.org/> .\n"
        b"@prefix geo: <http://www.opengis.net/ont/geosparql#> .\n"
        b"@prefix owl: <http://www.w3.org/2002/07/owl#> .\n"
        b"@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n"
        b"@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
        b"@prefix sf: <http://www.opengis.net/ont/sf#> .\n"
        b"@prefix sh: <http://www.w3.org/ns/shacl#> .\n"
        b"@prefix silm: <urn:silmaril:entity#> .\n"
        b"@prefix void: <http://rdfs.org/ns/void#> .\n"
        b"@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n"
    )


def test_union_process_is_one_total_child_application() -> None:
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
