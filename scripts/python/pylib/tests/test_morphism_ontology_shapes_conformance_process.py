import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).parents[1]
REPOSITORY = Path(__file__).parents[4]
CONSOLIDATED = REPOSITORY / "ontology/silmaril-consolidated.ttl"
SHAPES = REPOSITORY / "ontology/shapes.ttl"
MODULE = "silmaril.sparky.morphism.ontology.shapes.conformance.process"
ENVIRONMENT = {
    **os.environ,
    "PYTHONDONTWRITEBYTECODE": "1",
    "PYTHONPATH": str(ROOT / "src"),
}


def test_conformance_process_accepts_committed_artifacts() -> None:
    completed = subprocess.run(
        (sys.executable, "-m", MODULE, str(SHAPES)),
        capture_output=True,
        check=False,
        env=ENVIRONMENT,
        input=CONSOLIDATED.read_bytes(),
    )

    assert completed.returncode == 0
    assert completed.stderr == b""
    assert b"Conforms: True" in completed.stdout


def test_conformance_process_rejects_a_corrupted_fingerprint() -> None:
    corrupted = CONSOLIDATED.read_bytes().replace(
        b'"77481DD960B9CBE52BEC60CFC998590FAEA8530A"', b'"77481DD960B9CBE"', 1
    )
    completed = subprocess.run(
        (sys.executable, "-m", MODULE, str(SHAPES)),
        capture_output=True,
        check=False,
        env=ENVIRONMENT,
        input=corrupted,
    )

    assert completed.returncode == 1
    assert b"Conforms: False" in completed.stdout
