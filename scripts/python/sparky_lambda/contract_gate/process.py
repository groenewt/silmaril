"""Process and filesystem mechanics admitted only inside ContractGate."""

from __future__ import annotations

import os
from pathlib import Path
import stat
import subprocess

from ..artifact import Request, Response
from ..contract import Contract
from ..jvm import Process
from ..transport import CaptureGap, Execution, Failure, FileObservation
from .capture import CapturedFileDrifted, file
from .host.octet import Projection


def _gap(contract: Contract, response: Response, evidence: str) -> CaptureGap:
    return CaptureGap(
        identity=contract.contract_gate.capture.file_payload_not_captured_gap_identity,
        locator=response.locator,
        evidence=evidence,
    )


def _response_observation(
    contract: Contract,
    response: Response,
    projection: Projection,
) -> FileObservation | CaptureGap:
    try:
        captured = file(
            response.locator,
            projection.digest,
            contract.contract_gate,
        )
    except (OSError, ValueError) as issue:
        return _gap(
            contract,
            response,
            f"response payload not captured: {type(issue).__name__}: {issue}",
        )
    if isinstance(captured, CapturedFileDrifted):
        return CaptureGap(
            identity=captured.gap_identity,
            locator=response.locator,
            evidence=captured.gap_evidence,
        )
    return captured.observation


def invoke(
    contract: Contract,
    process: Process,
    request: Request,
    response: Response,
) -> Execution:
    if request.schema_identity != contract.artifact.request_schema_identity:
        raise ValueError("Lambda request schema differs from ContractGate")
    if response.schema_identity != contract.artifact.response_schema_identity:
        raise ValueError("Lambda response schema differs from ContractGate")
    if request.framing_identity != contract.artifact.framing_identity:
        raise ValueError("Lambda request framing differs from ContractGate")
    if response.framing_identity != contract.artifact.framing_identity:
        raise ValueError("Lambda response framing differs from ContractGate")
    if not process.command:
        raise ValueError("Lambda process projection requires a command")

    projection = Projection.registered(contract)
    request_capture = file(
        request.locator,
        projection.digest,
        contract.contract_gate,
    )
    if isinstance(request_capture, CapturedFileDrifted):
        raise ValueError(
            f"{request_capture.gap_identity}: {request_capture.gap_evidence}"
        )

    response_path = Path(response.locator.host_path.lexical)
    parent_metadata = os.stat(response_path.parent, follow_symlinks=False)
    if not stat.S_ISDIR(parent_metadata.st_mode):
        raise ValueError("Lambda response parent is not a directory")
    try:
        os.stat(response_path, follow_symlinks=False)
    except FileNotFoundError:
        pass
    else:
        raise ValueError(
            "Lambda response artifact already exists: "
            f"{response.locator.canonical.value}"
        )

    completed = subprocess.run(
        (
            *process.command,
            request.locator.host_path.lexical,
            response.locator.host_path.lexical,
        ),
        cwd=process.working_directory.host_path.lexical,
        check=False,
    )
    response_observation = _response_observation(
        contract,
        response,
        projection,
    )
    execution = Execution(
        capability=process.capability,
        runtime_shoe=process.runtime_shoe,
        request=request,
        response=response,
        exit_code=completed.returncode,
        evidence=process.evidence,
        request_observation=request_capture.observation,
        response_observation=response_observation,
    )
    if completed.returncode != 0:
        raise Failure(execution)
    if isinstance(response_observation, CaptureGap):
        raise RuntimeError(
            "registered Scala Lambda emitted no stable response artifact: "
            f"{response_observation.evidence}"
        )
    return execution
