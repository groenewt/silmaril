from config.gate.external.python.morphism.codebase.volume.phase14.evidence.shape.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.phase14.evidence.shape.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.phase14.evidence.shape.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
