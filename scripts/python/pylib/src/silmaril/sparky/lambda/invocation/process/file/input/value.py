from config.gate.external.project.sparky.invocation.process.file.input.library import BINDING_IDENTITY, Effect, LINEAGE_IDENTITY, OBJECT_IDENTITY, OPERATION_IDENTITY, Output, PREDICATE_IDENTITY, SCHEMA_IDENTITY, SOURCE_EVIDENCE, STAGE_IDENTITY, SUBJECT_IDENTITY, VECTOR_IDENTITY
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    output: Output
    effect: Effect
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
    binding_identity = BINDING_IDENTITY
    operation_identity = OPERATION_IDENTITY
    vector_identity = VECTOR_IDENTITY
    subject_identity = SUBJECT_IDENTITY
    object_identity = OBJECT_IDENTITY
    predicate_identity = PREDICATE_IDENTITY
    source_evidence = SOURCE_EVIDENCE
    stage_identity = STAGE_IDENTITY
