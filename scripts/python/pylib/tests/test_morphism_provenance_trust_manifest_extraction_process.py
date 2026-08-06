import ast
import json
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).parents[1]
REPOSITORY = Path(__file__).parents[4]
TRUST_MODEL = REPOSITORY / "basicttl/commit_signing_trust.ttl"
MODULE = "silmaril.sparky.morphism.provenance.trust.manifest.extraction.process"
RUNTIME_FILE = ROOT / "src/silmaril/sparky/morphism/provenance/trust/manifest/extraction/process.py"
COMMAND_FILE = (
    ROOT
    / "src/config/constants/morphism/provenance/trust/manifest/extraction/process/command/value.py"
)
ENVIRONMENT = {
    **os.environ,
    "PYTHONDONTWRITEBYTECODE": "1",
    "PYTHONPATH": str(ROOT / "src"),
}
MULTI_KEY_TRUST_MODEL = b"""\
@prefix silm: <urn:silmaril:entity#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

silm:signing_identity_alpha a owl:NamedIndividual, silm:signingidentity ;
    rdfs:label "Alpha" ;
    silm:hasEmail "alpha@example.internal" ;
    silm:signsWith silm:signing_key_alpha_one , silm:signing_key_alpha_two .

silm:signing_identity_beta a owl:NamedIndividual, silm:signingidentity ;
    rdfs:label "Beta" ;
    silm:hasEmail "beta@example.internal" ;
    silm:signsWith silm:signing_key_beta_one ;
    silm:signsWith silm:signing_key_beta_two .

silm:signing_key_alpha_one a owl:NamedIndividual, silm:signingkey ;
    rdfs:label "AlphaKeyOne" ;
    silm:hasFingerprint "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" ;
    silm:hasKeyAlgorithm "ed25519" ;
    silm:hasKeyFile "alpha-one.asc" ;
    silm:hasPolicyClass silm:trust_policy_release .

silm:signing_key_alpha_two a owl:NamedIndividual, silm:signingkey ;
    rdfs:label "AlphaKeyTwo" ;
    silm:hasFingerprint "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB" ;
    silm:hasKeyAlgorithm "ed25519" ;
    silm:hasKeyFile "alpha-two.asc" ;
    silm:hasPolicyClass silm:trust_policy_release .

silm:signing_key_beta_one a owl:NamedIndividual, silm:signingkey ;
    rdfs:label "BetaKeyOne" ;
    silm:hasFingerprint "CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC" ;
    silm:hasKeyAlgorithm "ed25519" ;
    silm:hasKeyFile "beta-one.asc" ;
    silm:hasPolicyClass silm:trust_policy_agent .

silm:signing_key_beta_two a owl:NamedIndividual, silm:signingkey ;
    rdfs:label "BetaKeyTwo" ;
    silm:hasFingerprint "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD" ;
    silm:hasKeyAlgorithm "rsa4096" ;
    silm:hasKeyFile "beta-two.asc" ;
    silm:hasPolicyClass silm:trust_policy_web_flow .
"""


def test_extraction_process_emits_committed_trust_model_rows() -> None:
    completed = subprocess.run(
        (sys.executable, "-m", MODULE),
        capture_output=True,
        check=False,
        env=ENVIRONMENT,
        input=TRUST_MODEL.read_bytes(),
    )

    assert completed.returncode == 0
    assert completed.stderr == b""
    rows = tuple(json.loads(line) for line in completed.stdout.splitlines())
    assert rows == (
        [
            "77481DD960B9CBE52BEC60CFC998590FAEA8530A",
            "release",
            "herodotus.asc",
            "Herodotus",
            "herodotus@silmaril.internal",
        ],
        [
            "968479A1AFF927E37D1A566BB5690EEEBB952194",
            "web-flow",
            "github-web-flow.asc",
            "GitHub",
            "noreply@github.com",
        ],
        [
            "27044DC503CD3A5EE470CE4E15B79D364040C858",
            "agent",
            "claude.asc",
            "Claude",
            "claude@silmaril.internal",
        ],
    )


def test_extraction_process_resolves_comma_list_and_repeated_signs_with() -> None:
    completed = subprocess.run(
        (sys.executable, "-m", MODULE),
        capture_output=True,
        check=False,
        env=ENVIRONMENT,
        input=MULTI_KEY_TRUST_MODEL,
    )

    assert completed.returncode == 0
    assert completed.stderr == b""
    rows = tuple(json.loads(line) for line in completed.stdout.splitlines())
    assert rows == (
        [
            "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
            "release",
            "alpha-one.asc",
            "Alpha",
            "alpha@example.internal",
        ],
        [
            "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
            "release",
            "alpha-two.asc",
            "Alpha",
            "alpha@example.internal",
        ],
        [
            "CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC",
            "agent",
            "beta-one.asc",
            "Beta",
            "beta@example.internal",
        ],
        [
            "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
            "web-flow",
            "beta-two.asc",
            "Beta",
            "beta@example.internal",
        ],
    )


def test_extraction_process_is_one_total_child_application() -> None:
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
