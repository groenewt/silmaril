import csv
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parents[1]
def test_phase14_construct_preserves_authoritative_26_by_4_statuses(tmp_path: Path) -> None:
    envelope = {"records": [{"event": "gate_1_passed", "detail": "status=failed", "sequence": 7}]}
    input_path = tmp_path / "input.json"
    output_root = tmp_path / "output"
    input_path.write_text(json.dumps(envelope), encoding="utf-8")
    completed = subprocess.run(
        (
            "make",
            "volume-phase14-table",
            f"SILMARIL_PYTHON={sys.executable}",
            f"VOLUME_PHASE14_TABLE_INPUT={input_path}",
            f"VOLUME_PHASE14_TABLE_OUTPUT={output_root}",
        ),
        capture_output=True,
        check=False,
        cwd=ROOT,
    )
    with (output_root / "phase14.csv").open(newline="", encoding="utf-8") as stream:
        rows = tuple(csv.DictReader(stream))

    assert completed.returncode == 0
    assert len(rows) == 104
    assert rows[0] == {
        "gate_order": "1",
        "gate_id": "gate_1",
        "dimension_order": "1",
        "dimension": "pass",
        "status": "fail",
        "evidence_ref": '{"sequence":7}',
    }
    assert rows[1]["status"] == "pending"
    assert completed.stderr == b""
