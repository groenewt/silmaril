from config.constants.lambda_blotto.invocation.process.file.capture.progress.seal.input.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.lambda_blotto.invocation.process.file.capture.progress.seal.input.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.constants.lambda_blotto.invocation.process.file.capture.progress.seal.request.operation.identity.value import VALUE as OPERATION_IDENTITY
from config.constants.lambda_blotto.invocation.process.file.capture.source.evidence.value import VALUE as SOURCE_EVIDENCE
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.locator.value import Value as Locator
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.natural.value import Value as Natural
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
    scan_identity: ByteVector
    stage: ByteVector
    completed: Natural
    total: Natural
    locator: Locator
    previous_digest: ByteVector
    operation_identity = OPERATION_IDENTITY
    source_evidence = SOURCE_EVIDENCE
