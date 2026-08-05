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

def test_semantic_operation_tokens_are_confined_to_their_declared_edges() -> None:
    rows = _ledger_rows()
    allowed = {
        "CSV.read": {"parse"},
        "CSV.generate_line": {"csv/encode"},
        ".flatten(": {"group/aggregate"},
        ".uniq": {"required/set/uniqueness/projection"},
        ".sort_by": {"order/projection"},
        ".to_i": {"order/numeric/normalization"},
        ".values_at": {"uniqueness/identity/projection"},
    }
    map_edges = {
        "parse",
        "source/annotation/projection",
        "required/key/projection",
        "uniqueness/identity/projection",
        "row/projection",
        "order/numeric/normalization",
        "order/key/projection",
        "order/result/projection",
    }
    validation_edges = {
        "shape/validation",
        "required/set/validation",
        "uniqueness/validation",
    }

    for row in rows:
        constant_path = _ROOT / (
            "src/config/constants/morphism/codebase/volume/table/"
            + row["family"]
            + "/aggregate/"
            + row["edge"]
            + "/process/command/value.py"
        )
        source = constant_path.read_text(encoding="utf-8")
        for token, edges in allowed.items():
            if token in source:
                assert row["edge"] in edges, (constant_path, token)
        if ".map" in source:
            assert row["edge"] in map_edges, constant_path
        if "raise " in source:
            assert row["edge"] in validation_edges, constant_path
        if '"-rcsv"' in source:
            assert row["edge"] in {"parse", "csv/encode"}, constant_path
        assert "rescue" not in source, constant_path
        assert "JSON" not in source, constant_path
        assert ".select" not in source, constant_path
        assert ".filter" not in source, constant_path
        assert ".reject" not in source, constant_path
