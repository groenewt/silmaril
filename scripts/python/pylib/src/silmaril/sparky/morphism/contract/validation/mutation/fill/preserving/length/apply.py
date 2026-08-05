from config.gate.external.python.morphism.contract.validation.mutation.fill.preserving.length.library import PROJECT
from silmaril.sparky.morphism.contract.validation.mutation.fill.preserving.length.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.mutation.fill.preserving.length.input.value import Value as Input

def apply(value: Input) -> Frame: return PROJECT(value)
