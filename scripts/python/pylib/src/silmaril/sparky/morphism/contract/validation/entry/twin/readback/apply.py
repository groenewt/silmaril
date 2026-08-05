from config.gate.external.python.morphism.contract.validation.entry.twin.readback.library import PROJECT
from silmaril.sparky.morphism.contract.validation.entry.twin.readback.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.entry.twin.readback.input.value import Value as Input

def apply(value: Input) -> Frame: return PROJECT(value)
