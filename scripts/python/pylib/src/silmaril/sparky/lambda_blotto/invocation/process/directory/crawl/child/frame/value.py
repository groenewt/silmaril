from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.child.classification.value import Value as Classification
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.dispatch.directory.work.value import Value as DirectoryWork
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.dispatch.file.work.value import Value as FileWork
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.dispatch.none.value import Value as NoDispatch
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.hidden.decision.value import Value as HiddenDecision
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.name.observation.value import Value as Name
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.metadata.observation.value import Value as Metadata

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    name: Name
    metadata: Metadata
    classification: Classification
    hidden: HiddenDecision
    dispatch: FileWork | DirectoryWork | NoDispatch
