import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parents[1]
MODULE = "silmaril.sparky.morphism.codebase.volume.inventory.telephone.process"


def test_telephone_observer_emits_dynamic_overload_and_iouring_evidence() -> None:
    repository = Path(os.environ["SILMARIL_REPO_ROOT"])
    completed = subprocess.run(
        (sys.executable, "-m", MODULE, str(repository)),
        capture_output=True,
        check=False,
        cwd=ROOT,
    )

    assert completed.returncode == 0
    assert b"rejected_event" in completed.stdout
    assert b"rejected_handle" in completed.stdout
    assert b"group_batch_max" in completed.stdout
    assert b"lag_max" in completed.stdout
    assert b"queue_entries" in completed.stdout
    assert b"IORING_OP_WRITEV" in completed.stdout
    assert b"active_submission.assign(chunks)" in completed.stdout
    assert b"sqe->len" in completed.stdout
    assert completed.stderr == b""
