from config.gate.external.python.morphism.contract.validation.mechanic.artifact.kind.library import PROJECT
from silmaril.sparky.morphism.contract.validation.mechanic.artifact.kind.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.mechanic.artifact.kind.input.value import Value as Input

def apply(value: Input) -> Frame: return PROJECT(value)
