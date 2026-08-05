from config.constants.lambda_blotto.invocation.process.directory.crawl.receipt.seal.input.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.lambda_blotto.invocation.process.directory.crawl.receipt.seal.input.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.constants.lambda_blotto.invocation.process.directory.crawl.receipt.seal.request.operation.identity.value import VALUE as OPERATION_IDENTITY
from config.constants.lambda_blotto.invocation.process.directory.crawl.source.evidence.value import VALUE as SOURCE_EVIDENCE
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.frame.value import Value as DirectoryFrame
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.revision.value import Value as Revision

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
    frame: DirectoryFrame
    revision: Revision
    operation_identity = OPERATION_IDENTITY
    source_evidence = SOURCE_EVIDENCE
