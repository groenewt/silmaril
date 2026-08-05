from config.constants.lambda_.invocation.output.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.lambda_.invocation.output.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.constants.lambda_.invocation.process.file.input.coordinate.repository.identity.value import VALUE as REPOSITORY_COORDINATE_IDENTITY
from config.constants.lambda_.invocation.process.file.input.coordinate.request.identity.value import VALUE as REQUEST_COORDINATE_IDENTITY
from config.constants.lambda_.invocation.process.file.input.coordinate.response.identity.value import VALUE as RESPONSE_COORDINATE_IDENTITY
from config.constants.lambda_.invocation.process.file.stage.output.state.continuation.host.client.readback.identity.value import VALUE as STAGE_IDENTITY
from config.constants.lambda_.invocation.process.file.stage.transition.identity.value import VALUE as TRANSITION_IDENTITY
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
