import csv
import os
from pathlib import Path
import subprocess
import sys


_ROOT = Path(__file__).parents[1]
_LEDGER = _ROOT / "tests/fixtures/contract_validation_process_ledger.csv"
_MAKE_ROOT = _ROOT / "make/morphism/contract/validation"


def test_make_is_the_only_named_contract_validation_compositor(tmp_path: Path) -> None:
    with _LEDGER.open(newline="", encoding="utf-8") as stream:
        rows = tuple(csv.DictReader(stream))

    make_sources = "".join(
        path.read_text(encoding="utf-8") for path in sorted(_MAKE_ROOT.glob("*.mk"))
    )
    coordinates = {row["make_composition_coordinate"] for row in rows}

    assert len(coordinates) == 21
    assert "include make/morphism/contract/validation/directory.mk" in (
        _ROOT / "Makefile"
    ).read_text(encoding="utf-8")
    assert "define " not in make_sources
    assert "%:" not in make_sources
    for coordinate in coordinates:
        assert f".PHONY: {coordinate}" in make_sources
    for row in rows:
        assert f'-m {row["module"]}' in make_sources
    assert make_sources.count('>"$@.stderr"') == len(rows)
    assert make_sources.count('>"$@.status"') == len(rows)
    assert make_sources.count('exit "$$STATUS"') == len(rows)

    application_input = tmp_path / "application-input.bin"
    application_input.write_bytes(b"  exact application bytes  ")
    application_root = tmp_path / "application-artifacts"
    environment = os.environ | {"PYTHONDONTWRITEBYTECODE": "1"}

    application = subprocess.run(
        (
            "make",
            "--no-print-directory",
            "morphism-contract-validation-application",
            f"SILMARIL_PYTHON={sys.executable}",
            f"MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT={application_root}",
            f"MCV_APPLICATION_FRAME={application_input}",
        ),
        cwd=_ROOT,
        env=environment,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    assert application.returncode == 0, application.stderr
    application_edge = application_root / "application"
    assert (application_edge / "output.bin").read_bytes() == application_input.read_bytes()
    assert (application_edge / "output.bin.stderr").read_bytes() == b""
    assert (application_edge / "output.bin.status").read_bytes() == b"0\n"
    assert (application_edge / "effect.bin").read_bytes()
    assert (application_edge / "effect.bin.stderr").read_bytes() == b""
    assert (application_edge / "effect.bin.status").read_bytes() == b"0\n"

    json_input = tmp_path / "json-input.bin"
    json_input.write_bytes(b'{"one":"thing"}')
    json_root = tmp_path / "json-artifacts"
    json_result = subprocess.run(
        (
            "make",
            "--no-print-directory",
            "morphism-contract-validation-mechanic-json",
            f"SILMARIL_PYTHON={sys.executable}",
            f"MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT={json_root}",
            f"MCV_JSON_VALUE={json_input}",
        ),
        cwd=_ROOT,
        env=environment,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    assert json_result.returncode == 0, json_result.stderr
    json_edge = json_root / "mechanic/json"
    assert (json_edge / "classification.bin").read_bytes() == b"accepted"
    assert (json_edge / "output.bin").read_bytes() == b"true"
    assert (json_edge / "effect.bin").read_bytes()
    for lane in ("classification", "output", "effect"):
        assert (json_edge / f"{lane}.bin.stderr").read_bytes() == b""
        assert (json_edge / f"{lane}.bin.status").read_bytes() == b"0\n"
