from config.gate.external.python.morphism.contract.validation.configuration.capture.library import PROJECT
from silmaril.sparky.morphism.contract.validation.configuration.capture.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.configuration.capture.input.value import Value as Input

def apply(value: Input) -> Frame: return PROJECT(value)
