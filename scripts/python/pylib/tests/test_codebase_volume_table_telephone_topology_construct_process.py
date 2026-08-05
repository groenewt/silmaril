import csv
import io
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parents[1]
SOURCE = b"lib/telephone/application.ex:1:defmodule Telephone.Application do\nlib/telephone/application.ex:2:  alias Telephone.Broker\nlib/telephone/application.ex:3:    {Broker, []},\nlib/research/render/telephone/switchboard/observation.ex:1:defmodule Research.Render.Telephone.Switchboard.Observation do\nlib/research/render/telephone/switchboard/observation.ex:2:  @rejected_event_key Commit.receipt([:keys, :rejected_event])\nlib/research/render/telephone/switchboard/observation.ex:3:  @rejected_handle_key Commit.receipt([:keys, :rejected_handle])\nlib/research/render/telephone/switchboard/observation.ex:4:  @absent_token Commit.receipt(:absent_token)\nconfig/constants/telephone/l1/switchboard.exs:1:group_batch_max: 512\nconfig/constants/telephone/l1/switchboard.exs:2:lag_max: 4_096\nconfig/constants/native/executor/io/uring.exs:1:queue_entries: 1\nnative/telephone/native/src/executor/iouring/executor.cpp:1:namespace telephone_native::executor::io_uring {\nnative/telephone/native/src/executor/iouring/executor.cpp:2:ring->active_submission.assign(chunks);\nnative/telephone/native/src/executor/iouring/executor.cpp:3:sqe->opcode = IORING_OP_WRITEV;\nnative/telephone/native/src/executor/iouring/executor.cpp:4:sqe->len = ring->active_submission.iovecs.size();\nconfig/constants/telephone/lambda/writer/format/structured/file/object/container/avro.exs:1:native_append_mode: :iouring\nconfig/constants/native/executor/io/uring.exs:2:fallback: :writev\n"


def test_telephone_topology_construct_preserves_ordered_source_evidence(
    tmp_path: Path,
) -> None:
    source = tmp_path / "telephone-topology-input.txt"
    source.write_bytes(SOURCE)
    build_root = tmp_path / "volume-build"
    completed = subprocess.run(
        (
            "make",
            "--no-print-directory",
            "morphism-codebase-volume-table-telephone-topology",
            f"SILMARIL_PYTHON={sys.executable}",
            f"VOLUME_40_BUILD_ROOT={build_root}",
            f"VOLUME_TABLE_TELEPHONE_TOPOLOGY_INPUT={source}",
        ),
        capture_output=True,
        check=False,
        cwd=ROOT,
        env=os.environ | {"PYTHONDONTWRITEBYTECODE": "1"},
    )
    output = (
        build_root
        / "operation/table/construct/telephone_topology/telephone_topology.csv"
    )

    assert completed.returncode == 0, completed.stderr
    rows = tuple(csv.DictReader(io.StringIO(output.read_text(encoding="utf-8"))))
    supervisor = next(row for row in rows if row["topology_layer"] == "Telephone.Application")
    layers = {row["topology_layer"] for row in rows}

    assert supervisor == {
        "topology_layer": "Telephone.Application",
        "module_name": "Telephone.Broker",
        "child_order": "1",
        "source_path": "lib/telephone/application.ex",
        "source_line": "3",
        "evidence": "    {Broker, []},",
    }
    assert layers >= {
        "backend_selection",
        "commit_group_bound",
        "commit_lag_bound",
        "grouped_sqe",
        "iouring_queue_bound",
        "overload_identity",
    }
    assert completed.stderr == b""


def test_telephone_topology_make_preserves_origin_error_and_status(
    tmp_path: Path,
) -> None:
    source = tmp_path / "invalid-telephone-topology-input.txt"
    source.write_bytes(b"not-a-source-record\n")
    build_root = tmp_path / "failed-volume-build"
    completed = subprocess.run(
        (
            "make",
            "--no-print-directory",
            "morphism-codebase-volume-table-telephone-topology",
            f"SILMARIL_PYTHON={sys.executable}",
            f"VOLUME_40_BUILD_ROOT={build_root}",
            f"VOLUME_TABLE_TELEPHONE_TOPOLOGY_INPUT={source}",
        ),
        capture_output=True,
        check=False,
        cwd=ROOT,
        env=os.environ | {"PYTHONDONTWRITEBYTECODE": "1"},
    )
    failed = (
        build_root
        / "operation/table/construct/telephone_topology/08e-source-presence.carrier"
    )
    raw_error = Path(f"{failed}.stderr").read_bytes()

    assert completed.returncode != 0
    assert raw_error
    assert completed.stderr.startswith(raw_error)
    assert Path(f"{failed}.status").read_bytes() == b"1\n"
    assert not failed.exists()
