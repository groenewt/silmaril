from config.gate.external.python.morphism.contract.validation.mechanic.digest.support.library import PROJECT
from silmaril.sparky.morphism.contract.validation.mechanic.digest.support.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.mechanic.digest.support.input.value import Value as Input

def apply(value: Input) -> Frame: return PROJECT(value)
