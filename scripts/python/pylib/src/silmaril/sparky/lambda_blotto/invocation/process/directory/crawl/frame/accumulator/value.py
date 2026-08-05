from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.child.frame.value import Value as Child
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.frontier.value import Value as Frontier
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.natural.value import Value as Natural
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    children: tuple[Child, ...]
    serialized_children: ByteVector
    frontier: Frontier
    next_ordinal: Natural
    expected_total: Natural
    initialized_identity: ByteVector
    drift_identity: ByteVector
