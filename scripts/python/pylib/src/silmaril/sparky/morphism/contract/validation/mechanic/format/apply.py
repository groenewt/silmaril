from config.gate.external.python.morphism.contract.validation.mechanic.format.library import PROJECT
from silmaril.sparky.morphism.contract.validation.mechanic.format.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.mechanic.format.input.value import Value as Input

def apply(value: Input) -> Frame: return PROJECT(value)
