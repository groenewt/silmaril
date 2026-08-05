import ast
import csv
import os
from pathlib import Path
import shutil
import subprocess
import sys


_ROOT = Path(__file__).parents[1]
_LEDGER = _ROOT / "tests/fixtures/codebase_volume_five_aggregate_process_ledger.csv"
_RUNTIME_TABLE_ROOT = (
    _ROOT / "src/silmaril/sparky/morphism/codebase/volume/table"
)
_FAMILIES = (
    "source_files",
    "gdb_evidence",
    "ring_families",
    "shared_components",
    "shared_anchors",
)
_MAKE_ROOT = _ROOT / "make/morphism/codebase/volume/table/aggregate"
_HASH = "a" * 64


def _ledger_rows() -> tuple[dict[str, str], ...]:
    with _LEDGER.open(newline="", encoding="utf-8") as stream:
        return tuple(csv.DictReader(stream))


def _runtime_paths() -> tuple[Path, ...]:
    return tuple(
        sorted(
            path
            for family in _FAMILIES
            for path in (_RUNTIME_TABLE_ROOT / family / "aggregate").rglob(
                "process.py"
            )
        )
    )


def _write_rows(path: Path, rows: tuple[tuple[str, ...], ...]) -> None:
    with path.open("w", newline="", encoding="utf-8") as stream:
        csv.writer(stream).writerows(rows)


def _valid_inputs(root: Path) -> dict[str, Path]:
    inputs = {family: root / f"{family}.csv" for family in _FAMILIES}
    _write_rows(
        inputs["source_files"],
        (
            ("root", "zeta", "/zeta", "observed", ""),
            ("root", "alpha", "/alpha", "observed", ""),
        ),
    )
    _write_rows(
        inputs["gdb_evidence"],
        tuple(
            (kind, f"{kind}.md", str(index + 1), _HASH, f"evidence {kind}")
            for index, kind in enumerate(
                reversed(("hash", "readback", "source_frame", "transcript", "verifier"))
            )
        ),
    )
    _write_rows(
        inputs["ring_families"],
        tuple(
            (str(index), family, f"{family}.md", str(index + 1), f"evidence {family}")
            for index, family in enumerate(
                reversed(
                    (
                        "dunbar_inner_5",
                        "dunbar_15",
                        "dunbar_50",
                        "dunbar_150",
                        "l0",
                        "l1",
                        "l2",
                        "l3",
                        "l3_5",
                        "native_pool",
                        "trust_protection",
                    )
                )
            )
        ),
    )
    _write_rows(
        inputs["shared_components"],
        tuple(
            (kind, f"{kind}.tex", str(index + 1), f"evidence {kind}")
            for index, kind in enumerate(
                reversed(
                    (
                        "bibliography",
                        "build_wrapper",
                        "diagram",
                        "glossary",
                        "index",
                        "macro",
                        "preamble",
                        "projection_wrapper",
                        "table",
                        "title_metadata",
                    )
                )
            )
        ),
    )
    _write_rows(
        inputs["shared_anchors"],
        tuple(
            (kind, f"label:{kind}", f"{kind}.tex", str(index + 1), f"evidence {kind}")
            for index, kind in enumerate(
                reversed(
                    (
                        "cross_volume",
                        "global_architecture",
                        "label",
                        "validation_build",
                        "validation_include",
                        "validation_label",
                        "validation_projection",
                    )
                )
            )
        ),
    )
    return inputs

def test_each_runtime_file_declares_one_exact_semantic_edge() -> None:
    rows = _ledger_rows()
    runtime_paths = _runtime_paths()
    expected_header = (
        "family",
        "edge",
        "module",
        "runtime_file",
        "x",
        "f",
        "y",
        "error",
        "make_coordinate",
        "semantic_application_count",
        "project_local_function_imports",
        "invoked_project_local_functions",
        "carrier_invariant",
    )

    assert tuple(rows[0]) == expected_header
    assert len(rows) == 93
    assert len({(row["family"], row["edge"]) for row in rows}) == len(rows)
    assert {_ROOT / row["runtime_file"] for row in rows} == set(runtime_paths)
    assert not (
        _ROOT / "src/config/gate/external/python/morphism/codebase/volume/codec/library.py"
    ).exists()

    for row in rows:
        runtime = _ROOT / row["runtime_file"]
        tree = ast.parse(runtime.read_bytes(), filename=str(runtime))
        functions = tuple(
            node for node in tree.body if isinstance(node, ast.FunctionDef)
        )
        calls = tuple(
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "run"
        )
        forbidden_imports = tuple(
            alias.name
            for node in tree.body
            if isinstance(node, ast.ImportFrom)
            and node.module
            and node.module.startswith(("config.", "silmaril."))
            for alias in node.names
            if alias.name not in {"VALUE", "DEPENDENCY"}
        )
        constant_path = _ROOT / (
            "src/config/constants/morphism/codebase/volume/table/"
            + row["family"]
            + "/aggregate/"
            + row["edge"]
            + "/process/command/value.py"
        )

        assert tuple(node.name for node in functions) == ("MAIN",), runtime
        assert len(calls) == 1, runtime
        assert not tuple(node for node in ast.walk(tree) if isinstance(node, ast.Try)), runtime
        assert forbidden_imports == (), runtime
        assert constant_path.is_file(), constant_path
        assert row["x"] and row["f"] and row["y"] and row["error"]
        assert row["semantic_application_count"] == "1"
        assert row["project_local_function_imports"] == ""
        assert row["invoked_project_local_functions"] == ""
        assert "round-trip" in row["carrier_invariant"] or "== X" in row["carrier_invariant"]
