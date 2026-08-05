from config.gate.external.python.morphism.contract.validation.determinism.reverse.library import PROJECT
from silmaril.sparky.morphism.contract.validation.determinism.reverse.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.determinism.reverse.input.value import Value as Input

def apply(value: Input) -> Frame: return PROJECT(value)
