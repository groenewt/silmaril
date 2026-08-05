from config.gate.external.project.sparky.invocation.process.file.output.library import LINEAGE_IDENTITY, REPOSITORY_COORDINATE_IDENTITY, REQUEST_COORDINATE_IDENTITY, RESPONSE_COORDINATE_IDENTITY, SCHEMA_IDENTITY, STAGE_IDENTITY, TRANSITION_IDENTITY
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from .....substrate.byte.vector.value import Value as ByteVector

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    repository: ByteVector
    request: ByteVector
    response: ByteVector
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
    repository_coordinate_identity = REPOSITORY_COORDINATE_IDENTITY
    request_coordinate_identity = REQUEST_COORDINATE_IDENTITY
    response_coordinate_identity = RESPONSE_COORDINATE_IDENTITY
    stage_identity = STAGE_IDENTITY
    transition_identity = TRANSITION_IDENTITY
