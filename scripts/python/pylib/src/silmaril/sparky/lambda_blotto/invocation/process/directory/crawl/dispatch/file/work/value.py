from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.value import Value as FileState
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    state: FileState
    evidence_class: ByteVector
