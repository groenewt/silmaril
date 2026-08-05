from config.gate.external.python.morphism.contract.validation.schema.canonicalize.library import PROJECT
from silmaril.sparky.morphism.contract.validation.schema.canonicalize.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.schema.canonicalize.input.value import Value as Input

def apply(value: Input) -> Frame: return PROJECT(value)
