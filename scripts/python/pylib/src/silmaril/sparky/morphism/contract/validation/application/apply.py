from config.gate.external.python.morphism.contract.validation.application.library import PROJECT
from silmaril.sparky.morphism.contract.validation.application.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.application.input.value import Value as Input

def apply(value: Input) -> Frame: return PROJECT(value)
