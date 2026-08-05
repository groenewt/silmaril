from config.constants.lambda_blotto.invocation.process.directory.crawl.scheduler.transition.input.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.lambda_blotto.invocation.process.directory.crawl.scheduler.transition.input.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.constants.lambda_blotto.invocation.process.directory.crawl.scheduler.transition.request.operation.identity.value import VALUE as OPERATION_IDENTITY
from config.constants.lambda_blotto.invocation.process.directory.crawl.source.evidence.value import VALUE as SOURCE_EVIDENCE
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.value import Value as State
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
    state: State
    evidence_class: ByteVector
    transition_identity: ByteVector
    scan_identity: ByteVector
    attempt: ByteVector
    operation_identity = OPERATION_IDENTITY
    source_evidence = SOURCE_EVIDENCE
