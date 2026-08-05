from config.constants.morphism.contract.validation.mechanic.artifact.kind.input.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.morphism.contract.validation.mechanic.artifact.kind.input.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.constants.morphism.contract.validation.mechanic.artifact.kind.input.state.identity.value import VALUE as STATE_IDENTITY
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    closed_enumeration: ByteVector
    registration_kind: ByteVector
    registration_identity: ByteVector
    registration_path: ByteVector
    registration_schema: ByteVector
    registration_status: ByteVector
    registration_source_evidence: ByteVector
    document_schema: ByteVector
    schema_document_schema: ByteVector
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
    state_identity = STATE_IDENTITY
