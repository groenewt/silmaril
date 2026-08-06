from config.constants.morphism.ontology.shapes.conformance.effect.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.morphism.ontology.shapes.conformance.effect.provisional.evidence.value import VALUE as PROVISIONAL_EVIDENCE
from config.constants.morphism.ontology.shapes.conformance.effect.provisional.identity.value import VALUE as PROVISIONAL_IDENTITY
from config.constants.morphism.ontology.shapes.conformance.effect.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    frame: ByteVector
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
    identity = PROVISIONAL_IDENTITY
    evidence = PROVISIONAL_EVIDENCE
