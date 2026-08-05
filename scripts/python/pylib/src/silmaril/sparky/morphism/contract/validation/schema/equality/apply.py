from config.gate.external.python.morphism.contract.validation.schema.equality.library import PROJECT
from silmaril.sparky.morphism.contract.validation.schema.equality.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.schema.equality.input.value import Value as Input

def apply(value: Input) -> Frame: return PROJECT(value)
