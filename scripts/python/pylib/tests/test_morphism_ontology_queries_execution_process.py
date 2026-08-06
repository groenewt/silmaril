import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).parents[1]
REPOSITORY = Path(__file__).parents[4]
MODULE = "silmaril.sparky.morphism.ontology.queries.execution.process"
ENVIRONMENT = {
    **os.environ,
    "PYTHONDONTWRITEBYTECODE": "1",
    "PYTHONPATH": str(ROOT / "src"),
}


def test_execution_process_reports_expected_row_counts() -> None:
    completed = subprocess.run(
        (sys.executable, "-m", MODULE, str(REPOSITORY)),
        capture_output=True,
        check=False,
        env=ENVIRONMENT,
    )

    assert completed.returncode == 0
    assert completed.stderr == b""
    assert b"execution-verdict Q1 rows=35595" in completed.stdout
    assert b"execution-verdict Q3 rows=21" in completed.stdout
    assert b"execution-verdict Q5 rows=4807" in completed.stdout
