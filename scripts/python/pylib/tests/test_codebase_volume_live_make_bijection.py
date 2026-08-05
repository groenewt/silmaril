import csv
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).parents[1]
RUNTIME_ROOT = ROOT / "src/silmaril/sparky/morphism/codebase/volume"
FIXTURE_ROOT = ROOT / "tests/fixtures"
BASE_LEDGER = FIXTURE_ROOT / "codebase_volume_make_process_inventory.csv"
MODULE_PATTERN = re.compile(
    r"-m (silmaril\.sparky\.morphism\.codebase\.volume(?:\.[A-Za-z0-9_]+)+\.process)"
)


def test_runtime_ledger_and_live_make_module_sets_are_identical() -> None:
    ledgers = (BASE_LEDGER, *sorted(FIXTURE_ROOT.glob("codebase_volume_*_process_ledger.csv")))
    rows = []
    for ledger in ledgers:
        with ledger.open(newline="", encoding="utf-8") as stream:
            rows.extend(csv.DictReader(stream))

    runtime_modules = {
        "silmaril.sparky.morphism.codebase.volume."
        + path.relative_to(RUNTIME_ROOT).parent.as_posix().replace("/", ".")
        + ".process"
        for path in RUNTIME_ROOT.rglob("process.py")
    }
    ledger_modules = {row["module"] for row in rows}

    make = subprocess.run(
        ("make", "-qp"),
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert make.returncode in {0, 1}
    assert make.stderr == ""
    recipe_text = "\n".join(
        line for line in make.stdout.splitlines() if line.startswith("\t")
    )
    make_modules = set(MODULE_PATTERN.findall(recipe_text))

    assert len(rows) == len(ledger_modules)
    assert runtime_modules == ledger_modules == make_modules
