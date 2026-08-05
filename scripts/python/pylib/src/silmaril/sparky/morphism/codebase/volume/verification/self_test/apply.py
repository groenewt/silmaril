from config.gate.external.python.morphism.codebase.volume.verification.self_test.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.verification.self_test.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.verification.self_test.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
