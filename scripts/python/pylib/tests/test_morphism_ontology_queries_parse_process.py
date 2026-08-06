import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).parents[1]
REPOSITORY = Path(__file__).parents[4]
MODULE = "silmaril.sparky.morphism.ontology.queries.parse.process"
ENVIRONMENT = {
    **os.environ,
    "PYTHONDONTWRITEBYTECODE": "1",
    "PYTHONPATH": str(ROOT / "src"),
}


def test_parse_process_prepares_every_query_block() -> None:
    completed = subprocess.run(
        (sys.executable, "-m", MODULE, str(REPOSITORY)),
        capture_output=True,
        check=False,
        env=ENVIRONMENT,
    )

    assert completed.returncode == 0
    assert completed.stderr == b""
    for header in (b"Q1", b"Q2", b"Q3", b"Q4", b"Q5", b"GQ1", b"GQ2"):
        assert b"parse-verdict " + header + b" ok" in completed.stdout
