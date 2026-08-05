from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.descriptor.occurrence.value import Value as Descriptor
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.locator.value import Value as Locator
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    descriptor: Descriptor
    locator: Locator
    attempt: ByteVector
