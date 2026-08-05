from config.gate.external.python.morphism.codebase.volume.projection.section.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.projection.section.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.projection.section.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
