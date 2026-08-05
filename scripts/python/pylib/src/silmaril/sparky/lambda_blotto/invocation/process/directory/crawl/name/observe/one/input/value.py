from config.constants.lambda_blotto.invocation.process.directory.crawl.name.observe.one.input.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.lambda_blotto.invocation.process.directory.crawl.name.observe.one.input.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.constants.lambda_blotto.invocation.process.directory.crawl.name.observe.one.request.operation.identity.value import VALUE as OPERATION_IDENTITY
from config.constants.lambda_blotto.invocation.process.directory.crawl.source.evidence.value import VALUE as SOURCE_EVIDENCE
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.opened.directory.description.occurrence.value import Value as Opened
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.natural.value import Value as Natural

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
    opened: Opened
    ordinal: Natural
    operation_identity = OPERATION_IDENTITY
    source_evidence = SOURCE_EVIDENCE
