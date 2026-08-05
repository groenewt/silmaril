from config.gate.external.python.morphism.contract.validation.mutation.set.library import PROJECT
from silmaril.sparky.morphism.contract.validation.mutation.set.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.mutation.set.input.value import Value as Input

def apply(value: Input) -> Frame: return PROJECT(value)
