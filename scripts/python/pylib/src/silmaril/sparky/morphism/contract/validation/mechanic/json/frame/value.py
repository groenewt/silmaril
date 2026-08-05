from config.constants.morphism.contract.validation.mechanic.json.binding.identity.value import VALUE as BINDING_IDENTITY
from config.constants.morphism.contract.validation.mechanic.json.frame.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.morphism.contract.validation.mechanic.json.frame.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.constants.morphism.contract.validation.mechanic.json.operation.identity.value import VALUE as OPERATION_IDENTITY
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.morphism.contract.validation.mechanic.json.effect.value import Value as Effect
from silmaril.sparky.morphism.contract.validation.mechanic.json.output.value import Value as Output

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    output: Output
    effect: Effect
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
    binding_identity = BINDING_IDENTITY
    operation_identity = OPERATION_IDENTITY
