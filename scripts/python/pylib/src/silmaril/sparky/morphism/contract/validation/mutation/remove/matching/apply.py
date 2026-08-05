from config.gate.external.python.morphism.contract.validation.mutation.remove.matching.library import PROJECT
from silmaril.sparky.morphism.contract.validation.mutation.remove.matching.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.mutation.remove.matching.input.value import Value as Input

def apply(value: Input) -> Frame: return PROJECT(value)
