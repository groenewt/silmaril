from config.gate.external.python.morphism.contract.validation.entry.self.test.library import PROJECT
from silmaril.sparky.morphism.contract.validation.entry.self.test.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.entry.self.test.input.value import Value as Input

def apply(value: Input) -> Frame: return PROJECT(value)
