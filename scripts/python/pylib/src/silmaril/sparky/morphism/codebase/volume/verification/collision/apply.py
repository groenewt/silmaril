from config.gate.external.python.morphism.codebase.volume.verification.collision.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.verification.collision.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.verification.collision.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
