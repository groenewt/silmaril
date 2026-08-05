from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.publication.routing.occurrence.value import Value as Occurrence

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    claim_key: ByteVector
    volume_route: ByteVector
    chapter_route: ByteVector
    appendix_route: ByteVector
    occurrences: tuple[Occurrence, ...]
