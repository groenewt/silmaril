from config.constants.morphism.ontology.consolidation.source.discovery.frame.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.morphism.ontology.consolidation.source.discovery.frame.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.morphism.ontology.consolidation.source.discovery.effect.value import Value as Effect
from silmaril.sparky.morphism.ontology.consolidation.source.discovery.output.value import Value as Output

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    output: Output
    effect: Effect
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
