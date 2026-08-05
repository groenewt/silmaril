from config.constants.morphism.contract.validation.application.output.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.morphism.contract.validation.application.output.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.gate.external.project.sparky.morphism.contract.validation.application.stage.output.state.continuation.readback.identity.library import DEPENDENCY as STAGE_IDENTITY
from config.constants.morphism.contract.validation.application.stage.transition.identity.value import VALUE as TRANSITION_IDENTITY
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    frame: ByteVector
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
    stage_identity = STAGE_IDENTITY
    transition_identity = TRANSITION_IDENTITY
