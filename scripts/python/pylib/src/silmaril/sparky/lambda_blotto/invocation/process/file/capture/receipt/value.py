from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.artifact.provenance.value import Value as Provenance
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.revision.value import Value as Revision
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    serialized: ByteVector
    digest: ByteVector
    revision: Revision
    attempt: ByteVector
    provenance: Provenance
