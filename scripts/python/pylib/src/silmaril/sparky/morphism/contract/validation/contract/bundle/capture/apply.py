from config.gate.external.python.morphism.contract.validation.contract.bundle.capture.library import PROJECT
from silmaril.sparky.morphism.contract.validation.contract.bundle.capture.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.contract.bundle.capture.input.value import Value as Input

def apply(value: Input) -> Frame: return PROJECT(value)
