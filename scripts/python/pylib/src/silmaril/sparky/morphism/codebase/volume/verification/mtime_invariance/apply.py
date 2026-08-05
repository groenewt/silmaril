from config.gate.external.python.morphism.codebase.volume.verification.mtime_invariance.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.verification.mtime_invariance.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.verification.mtime_invariance.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
