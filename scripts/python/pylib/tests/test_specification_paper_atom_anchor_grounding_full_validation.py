import ast
import csv
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parents[1]
FAMILY = "morphism/specification/paper/atom/anchor/grounding/full/validation"
RUNTIME_ROOT = ROOT / "src/silmaril/sparky" / FAMILY
CONSTANT_ROOT = ROOT / "src/config/constants" / FAMILY
MAKE_FRAGMENT = ROOT / "make" / FAMILY / "../validation.mk"
PROCESS_LEDGER = ROOT / "tests/fixtures/specification_paper_atom_anchor_grounding_full_validation_process_ledger.csv"
DEPENDENCY_LEDGER = ROOT / "tests/fixtures/specification_paper_atom_anchor_grounding_full_validation_external_dependency_ledger.csv"
CLOSURE_STATUS = ROOT / "tests/fixtures/specification_paper_atom_anchor_grounding_full_validation_closure_status.json"
FIXTURE = ROOT / "tests/fixtures/specification_paper_atom_anchor_grounding_full_validation/papers"
LEGACY = Path("/home/tristan/Music/final/working/scripts/check-atom-anchor-grounding-full.py")
LEGACY_SHA256 = "6d49bbb3880c8ac21cd079e616f01674168aff5f36b51d7aed6db2710d570f55"
FORBIDDEN_RECIPE_TOKENS = (";", "&&", "||", "|", " set ", " rm ", " cp ", " mv ", " printf ", " cat ", " mkdir ")


def test_grounding_checker_transitional_graph_has_pinned_legacy_parity_without_claiming_frame_closure(tmp_path: Path) -> None:
    closure_status = json.loads(CLOSURE_STATUS.read_bytes())
    assert closure_status["status"] == "active_red_migration"
    assert len(closure_status["not_closure_authority"]) == 5
    with PROCESS_LEDGER.open(newline="", encoding="utf-8") as stream:
        ledger = tuple(csv.DictReader(stream))
    runtime_paths = tuple(sorted(RUNTIME_ROOT.rglob("process.py")))
    command_paths = tuple(sorted(CONSTANT_ROOT.rglob("process/command/value.py")))
    assert len(ledger) == 10
    assert {ROOT / row["runtime_file"] for row in ledger} == set(runtime_paths)
    assert {ROOT / row["command_file"] for row in ledger} == set(command_paths)
    assert not tuple(RUNTIME_ROOT.rglob("apply.py"))
    assert not tuple(RUNTIME_ROOT.rglob("project.py"))
    assert not tuple(RUNTIME_ROOT.rglob("launch.py"))
    assert not tuple(RUNTIME_ROOT.rglob("library.py"))

    for row in ledger:
        runtime = ROOT / row["runtime_file"]
        tree = ast.parse(runtime.read_bytes(), filename=str(runtime))
        functions = tuple(node for node in tree.body if isinstance(node, ast.FunctionDef))
        assert tuple(function.name for function in functions) == ("MAIN",)
        assert len(functions[0].body) == 1
        applications = tuple(
            node
            for node in ast.walk(functions[0])
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "SUBPROCESS"
            and node.func.attr == "run"
        )
        assert len(applications) == 1
        assert row["semantic_application_count"] == "1"
        assert row["carrier_invariant"]
        assert not any(isinstance(node, (ast.Try, ast.TryStar, ast.For, ast.While, ast.If)) for node in ast.walk(tree))

    for command in command_paths:
        tree = ast.parse(command.read_bytes(), filename=str(command))
        assert not tuple(node for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)))
        assignments = tuple(node for node in tree.body if isinstance(node, ast.Assign))
        assert len(assignments) == 1
        assert isinstance(assignments[0].targets[0], ast.Name)
        assert assignments[0].targets[0].id == "VALUE"
        imports = tuple(node for node in tree.body if isinstance(node, ast.ImportFrom))
        assert imports
        assert any("external.executable" in (node.module or "") for node in imports)

    make_source = MAKE_FRAGMENT.resolve().read_text(encoding="utf-8")
    recipes = tuple(line for line in make_source.splitlines() if line.startswith("\t"))
    assert len(recipes) == 10
    assert "define " not in make_source
    assert "$(shell" not in make_source
    assert all(line.count(" -m ") == 1 and ".process" in line for line in recipes)
    assert all(token not in line for line in recipes for token in FORBIDDEN_RECIPE_TOKENS)
    assert all(f'-m {row["module"]}' in make_source for row in ledger)

    with DEPENDENCY_LEDGER.open(newline="", encoding="utf-8") as stream:
        dependencies = tuple(csv.DictReader(stream))
    assert len(dependencies) == 5
    for dependency in dependencies:
        locus = Path(dependency["executable_locus"])
        assert locus.is_file()
        assert hashlib.sha256(locus.read_bytes()).hexdigest() == dependency["sha256"]

    assert hashlib.sha256(LEGACY.read_bytes()).hexdigest() == LEGACY_SHA256
    environment = os.environ | {"PYTHONDONTWRITEBYTECODE": "1"}
    legacy_json = subprocess.run(
        (sys.executable, str(LEGACY), "--papers-dir", str(FIXTURE), "--json"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=environment,
        check=False,
    )
    legacy_text = subprocess.run(
        (sys.executable, str(LEGACY), "--papers-dir", str(FIXTURE)),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=environment,
        check=False,
    )
    assert legacy_json.returncode == 1
    assert legacy_text.returncode == 1

    stage = tmp_path / "grounding-byte-frame"
    make_command = (
        "make",
        "--no-print-directory",
        "-f",
        str(MAKE_FRAGMENT.resolve()),
        f"ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_PYTHON={sys.executable}",
        f"ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_SOURCE_ROOT={ROOT / 'src'}",
        f"ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_PAPERS_DIRECTORY={FIXTURE}",
        f"ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_STAGE_ROOT={stage}",
    )
    observed_json_run = subprocess.run(
        (*make_command, "atom-anchor-grounding-full-json"),
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=environment,
        check=False,
    )
    observed_json = stage / "06-summary.json"
    assert observed_json_run.returncode != 0
    assert json.loads(observed_json.read_bytes()) == json.loads(legacy_json.stdout)

    validation = subprocess.run(
        (
            sys.executable,
            "-m",
            "silmaril.sparky.morphism.specification.paper.atom.anchor.grounding.full.validation.summary.completeness.validation.process",
        ),
        input=observed_json.read_bytes(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=environment | {"PYTHONPATH": str(ROOT / "src")},
        check=False,
    )
    assert validation.returncode == legacy_json.returncode == 1
    assert validation.stdout == b"false\n"
    assert validation.stderr == legacy_json.stderr == b""

    observed_text_run = subprocess.run(
        (*make_command, "atom-anchor-grounding-full-text"),
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=environment,
        check=False,
    )
    observed_text = stage / "07-summary.txt"
    assert observed_text_run.returncode != 0
    assert observed_text.read_bytes() == legacy_text.stdout

    missing_directory = subprocess.run(
        (
            sys.executable,
            "-m",
            "silmaril.sparky.morphism.specification.paper.atom.anchor.grounding.full.validation.papers.directory.presence.validation.process",
            str(tmp_path / "absent"),
        ),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=environment | {"PYTHONPATH": str(ROOT / "src")},
        check=False,
    )
    assert missing_directory.returncode == 2
    assert missing_directory.stdout == b""
    assert missing_directory.stderr == f"FAIL: not a directory: {tmp_path / 'absent'}\n".encode()
