from config.constants.lambda_blotto.invocation.process.directory.crawl.child.dispatch.output.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.lambda_blotto.invocation.process.directory.crawl.child.dispatch.output.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.dispatch.directory.work.value import Value as DirectoryWork
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.dispatch.file.work.value import Value as FileWork
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.dispatch.none.value import Value as NoDispatch

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
    result: FileWork | DirectoryWork | NoDispatch
