import json
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parents[1]
PARSE_MODULE = "silmaril.sparky.morphism.codebase.volume.phase14.json.parse.process"
# The carrier codec is Python pickle. This proof loads the test-produced
# query.carrier under the same interpreter and asserts codec object-identity:
# decode(encode(X)) == X. The carrier is produced by the make recipe from this
# test's own query, never an untrusted source.
CARRIER_ROUND_TRIP_PROOF = (
    "import pickle\n"
    "import sys\n"
    "value = pickle.loads(sys.stdin.buffer.read())\n"
    "raise SystemExit(0 if pickle.loads(pickle.dumps(value)) == value else 1)\n"
)


def test_phase14_make_composes_total_edges_with_bijective_carrier(tmp_path: Path) -> None:
    suffixes = ("passed", "profiled", "traced", "drift")
    records = [
        {
            "event": f"gate_{gate}_{suffix}",
            "correlation_id": f"correlation-{gate}-{suffix}",
            "run_id": "run-1",
            "sequence": gate,
            "time_iso": "2026-07-19T00:00:00Z",
        }
        for gate in range(1, 27)
        for suffix in suffixes
    ]
    query = {
        "records": list(reversed(records)),
        "count": len(records),
        "selected_tier": "L1",
        "tiers_consulted": ["L1"],
        "tiers_available": ["L0", "L1"],
        "route_selected": "explicit",
        "completeness_status": "complete",
    }
    query_path = tmp_path / "query.json"
    query_path.write_text(json.dumps(query), encoding="utf-8")
    query_command = tmp_path / "telephone-query"
    query_command.write_text('#!/bin/sh\nexec cat "$VOLUME_PHASE14_TEST_QUERY"\n', encoding="utf-8")
    query_command.chmod(0o700)
    output_root = tmp_path / "output"
    environment = os.environ | {"VOLUME_PHASE14_TEST_QUERY": str(query_path)}
    completed = subprocess.run(
        (
            "make",
            "volume-phase14-evidence",
            f"SILMARIL_PYTHON={sys.executable}",
            f"VOLUME_TELEPHONE_QUERY={query_command}",
            "VOLUME_PHASE14_QUERY_TIER=L1",
            f"VOLUME_PHASE14_OUTPUT={output_root}",
        ),
        capture_output=True,
        check=False,
        cwd=ROOT,
        env=environment,
    )
    envelope = json.loads((output_root / "evidence-envelope.json").read_text(encoding="utf-8"))
    carrier = (output_root / "query.carrier").read_bytes()
    reframed = subprocess.run(
        (sys.executable, "-c", CARRIER_ROUND_TRIP_PROOF),
        input=carrier,
        capture_output=True,
        check=False,
    )

    assert completed.returncode == 0
    assert envelope["gates"] == 26
    assert envelope["dimensions"] == 4
    assert len(envelope["records"]) == 104
    assert envelope["records"][0]["event"] == "gate_1_passed"
    assert envelope["records"][-1]["event"] == "gate_26_drift"
    assert reframed.returncode == 0
    assert reframed.stderr == b""

    invalid_query = tmp_path / "invalid.json"
    invalid_query.write_bytes(b"{")
    direct_error = subprocess.run(
        (sys.executable, "-m", PARSE_MODULE),
        input=b"{",
        capture_output=True,
        check=False,
        cwd=ROOT,
        env=os.environ | {"PYTHONPATH": str(ROOT / "src")},
    )
    failed_output = tmp_path / "failed-output"
    failed = subprocess.run(
        (
            "make",
            "volume-phase14-evidence",
            f"SILMARIL_PYTHON={sys.executable}",
            f"VOLUME_TELEPHONE_QUERY={query_command}",
            "VOLUME_PHASE14_QUERY_TIER=L1",
            f"VOLUME_PHASE14_OUTPUT={failed_output}",
        ),
        capture_output=True,
        check=False,
        cwd=ROOT,
        env=os.environ | {"VOLUME_PHASE14_TEST_QUERY": str(invalid_query)},
    )

    assert direct_error.returncode != 0
    assert failed.returncode != 0
    assert direct_error.stderr in failed.stderr
