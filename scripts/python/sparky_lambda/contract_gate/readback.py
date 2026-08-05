"""Immutable artifact readback materialized only inside ContractGate."""

from __future__ import annotations

from .. import artifact
from ..contract import Contract
from ..transport import ReceiptReadback
from .capture import CapturedFileDrifted, file
from .host.octet import Projection


def readback(contract: Contract) -> ReceiptReadback:
    registration = contract.receipt_readback
    projection = Projection.registered(contract)
    request = artifact.request(contract, registration.request_locator)
    response = artifact.response(contract, registration.response_locator)
    request_capture = file(
        request.locator,
        projection.digest,
        contract.contract_gate,
    )
    response_capture = file(
        response.locator,
        projection.digest,
        contract.contract_gate,
    )
    if isinstance(request_capture, CapturedFileDrifted):
        raise ValueError(
            f"{request_capture.gap_identity}: {request_capture.gap_evidence}"
        )
    if isinstance(response_capture, CapturedFileDrifted):
        raise ValueError(
            f"{response_capture.gap_identity}: {response_capture.gap_evidence}"
        )
    return ReceiptReadback(
        capability=registration.capability,
        state=registration.state,
        request=request,
        response=response,
        request_observation=request_capture.observation,
        response_observation=response_capture.observation,
    )
