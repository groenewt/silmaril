import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).parents[1]
REPOSITORY = Path(__file__).parents[4]
CONSOLIDATED = REPOSITORY / "ontology/silmaril-consolidated.ttl"
MODULE = "silmaril.sparky.morphism.ontology.document.parse.process"
ENVIRONMENT = {
    **os.environ,
    "PYTHONDONTWRITEBYTECODE": "1",
    "PYTHONPATH": str(ROOT / "src"),
}


def test_parse_process_counts_consolidated_document_triples() -> None:
    completed = subprocess.run(
        (sys.executable, "-m", MODULE),
        capture_output=True,
        check=False,
        env=ENVIRONMENT,
        input=CONSOLIDATED.read_bytes(),
    )

    assert completed.returncode == 0
    assert completed.stderr == b""
    assert completed.stdout == b"triple-count=81526\n"
