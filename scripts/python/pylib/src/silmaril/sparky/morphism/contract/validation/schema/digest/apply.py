from config.gate.external.python.morphism.contract.validation.schema.digest.library import PROJECT
from silmaril.sparky.morphism.contract.validation.schema.digest.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.schema.digest.input.value import Value as Input

def apply(value: Input) -> Frame: return PROJECT(value)
