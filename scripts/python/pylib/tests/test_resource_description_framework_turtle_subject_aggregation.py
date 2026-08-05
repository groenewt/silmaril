import ast
import csv
import hashlib
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).parents[1]
FIXTURE = ROOT / "tests/fixtures/resource_description_framework_turtle_subject_aggregation"
LEDGER = ROOT / "tests/fixtures/resource_description_framework_turtle_subject_aggregation_process_ledger.csv"
DEPENDENCY_LEDGER = ROOT / "tests/fixtures/resource_description_framework_turtle_subject_aggregation_external_dependency_ledger.csv"
RUNTIME_ROOT = ROOT / "src/silmaril/sparky/morphism/resource/description/framework/turtle/document/subject/aggregation"
COMMAND_ROOT = ROOT / "src/config/constants/morphism/resource/description/framework/turtle/document/subject/aggregation"
MAKE_FRAGMENT = ROOT / "make/morphism/resource/description/framework/turtle/document/subject/aggregation.mk"
SOURCE_PATH = os.pathsep.join((str(ROOT / "src"), "/data/src/scripts/pylib/src"))
SEMANTIC_CATEGORIES = {
    "encoding": re.compile(r"(?:JSON)\.(?:generate|dump)"),
    "filtering": re.compile(r"\.(?:select|reject|filter|compact)\b"),
    "grouping": re.compile(r"\.(?:group_by|flat_map|flatten|each_slice|transpose)\b"),
    "normalization": re.compile(r"\.(?:strip|sub|gsub|delete_prefix|delete_suffix|downcase|upcase|to_i|to_s|cleanpath)\b"),
    "ordering": re.compile(r"\.(?:sort|sort_by)\b"),
    "parsing": re.compile(r"(?:JSON)\.(?:read|parse)"),
    "pattern": re.compile(r"\.match\?|=~|\.scan\b|\.split\b|\.each_line\b"),
    "uniqueness": re.compile(r"\.uniq\b"),
}


class ResourceDescriptionFrameworkTurtleSubjectAggregationTest(unittest.TestCase):
    def test_every_runtime_coordinate_is_one_process_and_one_child_application(self) -> None:
        with LEDGER.open(newline="", encoding="utf-8") as stream:
            rows = tuple(csv.DictReader(stream))
        process_paths = tuple(sorted(RUNTIME_ROOT.rglob("process.py")))
        self.assertEqual(15, len(rows))
        self.assertEqual({ROOT / row["runtime_file"] for row in rows}, set(process_paths))
        self.assertFalse(tuple(RUNTIME_ROOT.rglob("apply.py")))
        self.assertFalse(tuple(RUNTIME_ROOT.rglob("project.py")))
        self.assertFalse(tuple(RUNTIME_ROOT.rglob("launch.py")))
        for row in rows:
            self.assertEqual("1", row["semantic_application_count"])
            self.assertEqual("", row["project_local_function_imports"])
            self.assertEqual("", row["invoked_project_local_functions"])
            self.assertEqual("one_process_coordinate_one_child_application", row["carrier_invariant"])
            tree = ast.parse((ROOT / row["runtime_file"]).read_bytes())
            functions = tuple(node for node in tree.body if isinstance(node, ast.FunctionDef))
            self.assertEqual(("MAIN",), tuple(node.name for node in functions))
            self.assertEqual(1, len(functions[0].body))
            child_applications = tuple(
                node for node in ast.walk(functions[0])
                if isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and isinstance(node.func.value, ast.Name)
                and node.func.value.id == "SUBPROCESS"
                and node.func.attr == "run"
            )
            self.assertEqual(1, len(child_applications))

    def test_command_carriers_are_values_without_callable_facades(self) -> None:
        command_paths = tuple(sorted(COMMAND_ROOT.rglob("process/command/value.py")))
        self.assertEqual(15, len(command_paths))
        for path in command_paths:
            tree = ast.parse(path.read_bytes())
            functions = tuple(node for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)))
            self.assertEqual((), functions)
            assignments = tuple(node for node in tree.body if isinstance(node, ast.Assign))
            self.assertEqual(1, len(assignments))
            self.assertEqual("VALUE", assignments[0].targets[0].id)
            command = ast.literal_eval(assignments[0].value)
            for index, argument in enumerate(command[:-1]):
                if argument not in {"-c", "-e"}:
                    continue
                body = command[index + 1]
                categories = tuple(name for name, pattern in SEMANTIC_CATEGORIES.items() if pattern.search(body))
                self.assertLessEqual(len(categories), 1, (str(path), categories))

    def test_make_composition_reproduces_the_inspected_predecessor_fixture(self) -> None:
        with tempfile.TemporaryDirectory(prefix="turtle-subject-aggregation-") as directory:
            temporary = Path(directory)
            output = temporary / "output/aggregate.ttl"
            environment = dict(os.environ)
            environment["PYTHONDONTWRITEBYTECODE"] = "1"
            result = subprocess.run(
                (
                    "make", "-f", str(MAKE_FRAGMENT), "resource-description-framework-turtle-subject-aggregation",
                    f"SILMARIL_PYTHON={sys.executable}",
                    f"RESOURCE_DESCRIPTION_FRAMEWORK_TURTLE_SUBJECT_AGGREGATION_SOURCE_ROOT={SOURCE_PATH}",
                    f"RESOURCE_DESCRIPTION_FRAMEWORK_TURTLE_SUBJECT_AGGREGATION_BUILD_ROOT={temporary / 'build'}",
                    f"RESOURCE_DESCRIPTION_FRAMEWORK_TURTLE_SUBJECT_AGGREGATION_SOURCE_DIRECTORY={FIXTURE / 'source'}",
                    f"RESOURCE_DESCRIPTION_FRAMEWORK_TURTLE_SUBJECT_AGGREGATION_ANCHOR_DOCUMENT={FIXTURE / 'universal_anchors.spec.yaml'}",
                    f"RESOURCE_DESCRIPTION_FRAMEWORK_TURTLE_SUBJECT_AGGREGATION_OUTPUT_DOCUMENT={output}",
                ),
                cwd=ROOT,
                env=environment,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )
            self.assertEqual(0, result.returncode, result.stderr.decode("utf-8", errors="replace"))
            observed = output.read_bytes()
            expected = (FIXTURE / "expected.ttl").read_bytes() + b"\n"
            self.assertEqual(expected, observed)
            self.assertEqual("abf22a74934d6c314c251a1d6446922bf78ed6d75d1aa2b49067e576c14f243a", hashlib.sha256(observed).hexdigest())

    def test_unknown_external_namespace_preserves_child_error_and_status(self) -> None:
        environment = dict(os.environ)
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        environment["PYTHONPATH"] = SOURCE_PATH
        result = subprocess.run(
            (sys.executable, "-m", "silmaril.sparky.morphism.resource.description.framework.turtle.document.subject.aggregation.namespace.identifier.validation.process"),
            input=b"absent\n",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=environment,
            check=False,
        )
        self.assertEqual(2, result.returncode)
        self.assertEqual(b"", result.stdout)
        self.assertEqual(b"namespace-identifier-absent:absent\n", result.stderr)

    def test_external_executables_are_registered_as_external_evidence(self) -> None:
        with DEPENDENCY_LEDGER.open(newline="", encoding="utf-8") as stream:
            rows = tuple(csv.DictReader(stream))
        self.assertEqual(6, len(rows))
        for row in rows:
            self.assertEqual("external_command_spelling_is_evidence_only", row["authority_boundary"])
            self.assertTrue(Path(row["executable_locus"]).is_file())

    def test_make_graph_names_every_edge_and_never_writes_volume_forty(self) -> None:
        text = MAKE_FRAGMENT.read_text(encoding="utf-8")
        with LEDGER.open(newline="", encoding="utf-8") as stream:
            rows = tuple(csv.DictReader(stream))
        for row in rows:
            suffix = row["module"].split("aggregation.", 1)[1]
            self.assertIn(suffix, text)
        self.assertNotIn("volume/40", text.lower())
        self.assertNotIn("volume.40", text.lower())


if __name__ == "__main__":
    unittest.main()
