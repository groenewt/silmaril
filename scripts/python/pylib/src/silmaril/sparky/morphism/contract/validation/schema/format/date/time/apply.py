from config.gate.external.python.morphism.contract.validation.schema.format.date.time.library import PROJECT
from silmaril.sparky.morphism.contract.validation.schema.format.date.time.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.schema.format.date.time.input.value import Value as Input

def apply(value: Input) -> Frame: return PROJECT(value)
