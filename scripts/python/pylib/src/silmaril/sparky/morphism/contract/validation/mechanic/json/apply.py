from config.gate.external.python.morphism.contract.validation.mechanic.json.library import PROJECT
from silmaril.sparky.morphism.contract.validation.mechanic.json.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.mechanic.json.input.value import Value as Input

def apply(value: Input) -> Frame: return PROJECT(value)
