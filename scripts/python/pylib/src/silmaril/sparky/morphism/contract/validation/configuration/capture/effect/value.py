from config.constants.morphism.contract.validation.configuration.capture.effect.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.morphism.contract.validation.configuration.capture.effect.provisional.evidence.value import VALUE as PROVISIONAL_EVIDENCE
from config.constants.morphism.contract.validation.configuration.capture.effect.provisional.identity.value import VALUE as PROVISIONAL_IDENTITY
from config.constants.morphism.contract.validation.configuration.capture.effect.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.constants.morphism.contract.validation.configuration.capture.request.gap.identity.value import VALUE as GAP_IDENTITY
from config.gate.external.project.sparky.morphism.contract.validation.request.binding.state.provisional.identity.library import DEPENDENCY as BINDING_STATE_IDENTITY
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    frame: ByteVector
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
    identity = PROVISIONAL_IDENTITY
    evidence = PROVISIONAL_EVIDENCE
    binding_state_identity = BINDING_STATE_IDENTITY
    gap_identity = GAP_IDENTITY
