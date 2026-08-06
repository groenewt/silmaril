from config.constants.morphism.ontology.consolidation.manifest.render.frame.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.morphism.ontology.consolidation.manifest.render.frame.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.morphism.ontology.consolidation.manifest.render.effect.value import Value as Effect
from silmaril.sparky.morphism.ontology.consolidation.manifest.render.output.value import Value as Output

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    output: Output
    effect: Effect
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
