from config.gate.external.python.morphism.codebase.volume.verification.absent_anchor.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.verification.absent_anchor.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.verification.absent_anchor.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
