import csv
import re
import subprocess
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).parents[1]
RUNTIME_ROOT = ROOT / "src/silmaril/sparky/morphism/codebase/volume/table"
LEDGER = ROOT / "tests/fixtures/codebase_volume_standard_table_constructor_process_ledger.csv"
BASE_LEDGER = ROOT / "tests/fixtures/codebase_volume_make_process_inventory.csv"
CONTEXTS = {
    "configuration",
    "dependencies",
    "documentation",
    "make_targets",
    "mix_tasks",
    "modules",
    "native_tree",
    "project_tasks",
    "provenance",
    "scripts",
    "tests",
}
MODULE_PATTERN = re.compile(
    r"-m (silmaril\.sparky\.morphism\.codebase\.volume\.table\."
    r"(?:configuration|dependencies|documentation|make_targets|mix_tasks|modules|"
    r"native_tree|project_tasks|provenance|scripts|tests)\.construct"
    r"(?:\.[A-Za-z0-9_]+)+\.process)"
)


def test_standard_table_constructors_are_one_to_one_make_visible_applications() -> None:
    runtime_modules = {
        "silmaril.sparky.morphism.codebase.volume.table."
        + path.relative_to(RUNTIME_ROOT).parent.as_posix().replace("/", ".")
        + ".process"
        for context in CONTEXTS
        for path in (RUNTIME_ROOT / context / "construct").rglob("process.py")
    }
    with LEDGER.open(newline="", encoding="utf-8") as stream:
        rows = tuple(csv.DictReader(stream))
    ledger_modules = {row["module"] for row in rows}
    make = subprocess.run(
        ("make", "-qp"),
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    make_occurrences = Counter(MODULE_PATTERN.findall(make.stdout))
    base_text = BASE_LEDGER.read_text(encoding="utf-8")

    assert make.returncode in {0, 1}
    assert make.stderr == ""
    assert len(rows) == len(runtime_modules) == len(make_occurrences) == 137
    assert runtime_modules == ledger_modules == set(make_occurrences)
    assert set(make_occurrences.values()) == {1}
    assert all(row["semantic_application_count"] == "1" for row in rows)
    assert all(row["invoked_project_local_functions"] == "" for row in rows)
    assert not any(f"table/{context}/construct," in base_text for context in CONTEXTS)
    assert not any(
        (RUNTIME_ROOT / context / "construct/presence/validation/process.py").exists()
        for context in CONTEXTS
    )
    assert not any(
        (RUNTIME_ROOT / context / "construct/uniqueness/validation/process.py").exists()
        for context in CONTEXTS
    )
    assert not (
        ROOT
        / "src/config/gate/external/python/morphism/codebase/volume/codec/library.py"
    ).exists()
