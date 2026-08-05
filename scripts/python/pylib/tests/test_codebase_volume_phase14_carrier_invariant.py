import subprocess
import sys


# The carrier codec is Python pickle. Both programs below run under the same
# interpreter over test-authored, in-process data (never an untrusted source),
# proving the carrier is byte-identical after a load-then-dump reification.
_ORIGINAL_CARRIER_PROGRAM = (
    "import pickle\n"
    "import sys\n"
    'sys.stdout.buffer.write(pickle.dumps({"records": [{"event": "gate_1_passed", "sequence": 7}], "absent": None, "boolean": True}))\n'
)
_REFRAME_CARRIER_PROGRAM = (
    "import pickle\n"
    "import sys\n"
    "value = pickle.load(sys.stdin.buffer)\n"
    "sys.stdout.buffer.write(pickle.dumps(value))\n"
)


def test_phase14_carrier_is_byte_identical_after_reification() -> None:
    original = subprocess.run(
        (sys.executable, "-c", _ORIGINAL_CARRIER_PROGRAM),
        capture_output=True,
        check=False,
    )
    reframed = subprocess.run(
        (sys.executable, "-c", _REFRAME_CARRIER_PROGRAM),
        input=original.stdout,
        capture_output=True,
        check=False,
    )

    assert original.returncode == 0
    assert original.stderr == b""
    assert reframed.returncode == 0
    assert reframed.stderr == b""
    assert reframed.stdout == original.stdout
