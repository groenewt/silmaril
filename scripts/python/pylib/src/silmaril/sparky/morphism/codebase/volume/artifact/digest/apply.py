from config.gate.external.python.morphism.codebase.volume.artifact.digest.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.artifact.digest.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.artifact.digest.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
