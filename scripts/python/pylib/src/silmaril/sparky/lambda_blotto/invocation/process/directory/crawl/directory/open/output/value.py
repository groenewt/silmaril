from config.constants.lambda_blotto.invocation.process.directory.crawl.directory.open.output.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.lambda_blotto.invocation.process.directory.crawl.directory.open.output.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.opened.directory.description.occurrence.value import Value as Opened
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.issue.value import Value as Issue

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
    result: Opened | Issue
