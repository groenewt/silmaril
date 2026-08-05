from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parents[1]
CSV_PATH = ROOT / "tests/fixtures/codebase_volume_make_process_inventory.csv"
HEADER = "coordinate,module,input_contract,output_contract,error_contract,make_safe_invocation,runtime_file,invoked_project_local_functions,semantic_application_count,external_application,project_local_function_imports"


def test_table_header_validation_returns_one_receipt_for_exact_contract(
    tmp_path: Path,
) -> None:
    output_root = tmp_path / "table-header"
    completed = subprocess.run(
        (
            "make",
            "-f",
            "make/morphism/codebase/volume/verification_table_header.mk",
            "volume-table-header",
            f"SILMARIL_PYTHON={sys.executable}",
            f"SILMARIL_PYLIB_SOURCE_ROOT={ROOT / 'src'}",
            f"VOLUME_TABLE_HEADER_CSV={CSV_PATH}",
            "VOLUME_TABLE_HEADER_INVENTORY_ID=process_inventory",
            f"VOLUME_TABLE_HEADER_EXPECTED={HEADER}",
            f"VOLUME_TABLE_HEADER_OUTPUT_ROOT={output_root}",
        ),
        capture_output=True,
        check=False,
        cwd=ROOT,
    )

    assert completed.returncode == 0
    assert (output_root / "table_header_receipt.csv").read_bytes() == (
        f"header_validated,process_inventory,{CSV_PATH}\n".encode()
    )
    assert completed.stderr == b""

    failed_root = tmp_path / "failed-table-header"
    failed = subprocess.run(
        (
            "make",
            "-f",
            "make/morphism/codebase/volume/verification_table_header.mk",
            "volume-table-header",
            f"SILMARIL_PYTHON={sys.executable}",
            f"SILMARIL_PYLIB_SOURCE_ROOT={ROOT / 'src'}",
            f"VOLUME_TABLE_HEADER_CSV={CSV_PATH}",
            "VOLUME_TABLE_HEADER_INVENTORY_ID=process_inventory",
            "VOLUME_TABLE_HEADER_EXPECTED=wrong_header",
            f"VOLUME_TABLE_HEADER_OUTPUT_ROOT={failed_root}",
        ),
        capture_output=True,
        check=False,
        cwd=ROOT,
    )
    child_error = (failed_root / "07-validated.carrier.error").read_bytes()

    assert failed.returncode != 0
    assert child_error in failed.stderr
    assert b"table_header_mismatch=process_inventory" in child_error
