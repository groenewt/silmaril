from config.gate.external.python.morphism.contract.validation.schema.diagnostic.library import PROJECT
from silmaril.sparky.morphism.contract.validation.schema.diagnostic.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.schema.diagnostic.input.value import Value as Input

def apply(value: Input) -> Frame: return PROJECT(value)
