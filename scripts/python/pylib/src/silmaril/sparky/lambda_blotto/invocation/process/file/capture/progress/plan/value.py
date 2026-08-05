from config.constants.lambda_blotto.invocation.process.file.capture.gap.progress.emission.value import VALUE as EMISSION_GAP
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    event: ByteVector
    payload: ByteVector
    emission_gap = EMISSION_GAP
