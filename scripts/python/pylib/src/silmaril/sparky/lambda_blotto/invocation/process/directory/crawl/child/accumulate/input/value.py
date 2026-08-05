from config.constants.lambda_blotto.invocation.process.directory.crawl.child.accumulate.input.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.lambda_blotto.invocation.process.directory.crawl.child.accumulate.input.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.constants.lambda_blotto.invocation.process.directory.crawl.child.accumulate.request.operation.identity.value import VALUE as OPERATION_IDENTITY
from config.constants.lambda_blotto.invocation.process.directory.crawl.source.evidence.value import VALUE as SOURCE_EVIDENCE
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.child.classification.value import Value as Classification
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.dispatch.directory.work.value import Value as DirectoryWork
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.dispatch.file.work.value import Value as FileWork
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.dispatch.none.value import Value as NoDispatch
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.frame.accumulator.value import Value as Accumulator
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.hidden.decision.value import Value as Hidden
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.name.observation.value import Value as Name
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.metadata.observation.value import Value as Metadata

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
    accumulator: Accumulator
    name: Name
    metadata: Metadata
    classification: Classification
    hidden: Hidden
    dispatch: FileWork | DirectoryWork | NoDispatch
    operation_identity = OPERATION_IDENTITY
    source_evidence = SOURCE_EVIDENCE
