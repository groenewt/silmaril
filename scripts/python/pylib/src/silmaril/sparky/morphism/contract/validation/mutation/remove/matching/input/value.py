from config.constants.morphism.contract.validation.mutation.remove.matching.input.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.morphism.contract.validation.mutation.remove.matching.input.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.constants.morphism.contract.validation.mutation.remove.matching.request.binding.identity.value import VALUE as BINDING_IDENTITY
from config.constants.morphism.contract.validation.mutation.remove.matching.request.operation.identity.value import VALUE as OPERATION_IDENTITY
from config.constants.morphism.contract.validation.mutation.remove.matching.request.role.object.identity.value import VALUE as OBJECT_IDENTITY
from config.constants.morphism.contract.validation.mutation.remove.matching.request.role.predicate.identity.value import VALUE as PREDICATE_IDENTITY
from config.constants.morphism.contract.validation.mutation.remove.matching.request.role.subject.identity.value import VALUE as SUBJECT_IDENTITY
from config.constants.morphism.contract.validation.mutation.remove.matching.request.source.evidence.value import VALUE as SOURCE_EVIDENCE
from config.constants.morphism.contract.validation.mutation.remove.matching.request.vector.identity.value import VALUE as VECTOR_IDENTITY
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    target: ByteVector
    matching: ByteVector
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
    binding_identity = BINDING_IDENTITY
    operation_identity = OPERATION_IDENTITY
    vector_identity = VECTOR_IDENTITY
    subject_identity = SUBJECT_IDENTITY
    object_identity = OBJECT_IDENTITY
    predicate_identity = PREDICATE_IDENTITY
    source_evidence = SOURCE_EVIDENCE
