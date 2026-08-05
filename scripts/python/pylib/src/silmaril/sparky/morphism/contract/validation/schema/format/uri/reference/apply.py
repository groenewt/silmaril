from config.gate.external.python.morphism.contract.validation.schema.format.uri.reference.library import PROJECT
from silmaril.sparky.morphism.contract.validation.schema.format.uri.reference.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.schema.format.uri.reference.input.value import Value as Input

def apply(value: Input) -> Frame: return PROJECT(value)
