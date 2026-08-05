from config.constants.lambda_blotto.invocation.process.file.capture.effect.provisional.identity.value import VALUE as PROVISIONAL
from config.gate.external.python.stdlib.hashlib.sha256.value import VALUE as SHA256
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.encoding.field.project import PROJECT as FIELD
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.progress.plan.value import Value as Plan
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.progress.receipt.value import Value as Receipt
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.progress.seal.effect.value import Value as Effect
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.progress.seal.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.progress.seal.input.value import Value as Input
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.progress.seal.output.value import Value as Output
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

def PROJECT(value: Input) -> Frame:
    completed = ByteVector(value.completed.value.to_bytes(16, "big", signed=False))
    total = ByteVector(value.total.value.to_bytes(16, "big", signed=False))
    fields = (ByteVector(b"lambda-blotto-file-capture-progress-v1"), value.scan_identity, value.stage, completed, total, value.locator.value, value.previous_digest)
    serialized = ByteVector(b"".join(FIELD(field).payload for field in fields))
    receipt = Receipt(serialized, ByteVector(SHA256(serialized.payload).digest()))
    plan = Plan(ByteVector(b"hook_file_capture_progress"), serialized)
    return Frame(Output(receipt, plan), Effect(ByteVector(PROVISIONAL)))
