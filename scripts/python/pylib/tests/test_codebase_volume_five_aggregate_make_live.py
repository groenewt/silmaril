import ast
import csv
import os
from pathlib import Path
import subprocess
import sys


_ROOT = Path(__file__).parents[1]
# The carrier codec is Python pickle. This proof loads each test-produced
# .carrier artifact under the same interpreter and asserts the codec round-trip
# is object-identity: decode(encode(X)) == X. The artifacts are produced by the
# make recipe from this test's own inputs, never an untrusted source.
_CARRIER_ROUND_TRIP_PROOF = (
    "import pickle\n"
    "import sys\n"
    "value = pickle.loads(sys.stdin.buffer.read())\n"
    "raise SystemExit(0 if pickle.loads(pickle.dumps(value)) == value else 1)\n"
)
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

def test_make_exposes_and_preserves_every_semantic_edge(tmp_path: Path) -> None:
    rows = _ledger_rows()
    make_sources = "".join(
        path.read_text(encoding="utf-8") for path in sorted(_MAKE_ROOT.glob("*.mk"))
    )
    inputs = _valid_inputs(tmp_path)
    artifact_root = tmp_path / "artifacts"
    environment = os.environ | {"PYTHONDONTWRITEBYTECODE": "1"}
    command = (
        "make",
        "--no-print-directory",
        "morphism-codebase-volume-table-aggregates",
        f"SILMARIL_PYTHON={sys.executable}",
        f"MORPHISM_CODEBASE_VOLUME_TABLE_ARTIFACT_ROOT={artifact_root}",
        f"VOLUME_SOURCE_FILES_ROW_FILES={inputs['source_files']}",
        f"VOLUME_GDB_EVIDENCE_ROW_FILES={inputs['gdb_evidence']}",
        f"VOLUME_RING_FAMILIES_ROW_FILES={inputs['ring_families']}",
        f"VOLUME_SHARED_COMPONENTS_ROW_FILES={inputs['shared_components']}",
        f"VOLUME_SHARED_ANCHORS_ROW_FILES={inputs['shared_anchors']}",
    )

    assert "include make/morphism/codebase/volume/table/aggregate/directory.mk" in (
        _ROOT / "Makefile"
    ).read_text(encoding="utf-8")
    for row in rows:
        assert make_sources.count(row["module"]) == 1, row["module"]

    result = subprocess.run(
        command,
        cwd=_ROOT,
        env=environment,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    assert result.returncode == 0, result.stderr

    statuses = tuple(sorted(artifact_root.rglob("*.status")))
    standard_errors = tuple(sorted(artifact_root.rglob("*.stderr")))
    carrier_artifacts = tuple(sorted(artifact_root.rglob("*.carrier")))
    assert len(statuses) == len(rows)
    assert len(standard_errors) == len(rows)
    assert all(path.read_bytes() == b"0\n" for path in statuses)
    assert all(path.read_bytes() == b"" for path in standard_errors)

    assert carrier_artifacts
    for artifact in carrier_artifacts:
        proof = subprocess.run(
            (sys.executable, "-c", _CARRIER_ROUND_TRIP_PROOF),
            input=artifact.read_bytes(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        assert proof.returncode == 0, (artifact, proof.stderr)

    expected_headers = {
        "source_files": ["root_id", "relative_path", "absolute_path", "observation_status", "gap_reason"],
        "gdb_evidence": ["evidence_kind", "relative_path", "source_line", "evidence_sha256", "evidence"],
        "ring_families": ["ring_order", "family", "source_path", "source_line", "evidence"],
        "shared_components": ["component_kind", "relative_path", "source_line", "evidence"],
        "shared_anchors": ["anchor_kind", "label", "relative_path", "source_line", "evidence"],
    }
    for family, header in expected_headers.items():
        output = artifact_root / family / "aggregate" / f"{family}.csv"
        with output.open(newline="", encoding="utf-8") as stream:
            table = tuple(csv.reader(stream))
        assert table[0] == header
        assert table[1:] == tuple(sorted(table[1:], key=lambda row: _expected_key(family, row)))


def _expected_key(family: str, row: list[str]) -> tuple[object, ...]:
    if family == "source_files":
        return (row[0], row[1])
    if family == "gdb_evidence":
        return (row[0], row[1], int(row[2]), row[3])
    if family == "ring_families":
        return (int(row[0]), row[1], row[2], int(row[3]), row[4])
    if family == "shared_components":
        return (row[0], row[1], int(row[2]), row[3])
    if family == "shared_anchors":
        return (row[0], row[1], row[2], int(row[3]), row[4])
    raise AssertionError(family)
