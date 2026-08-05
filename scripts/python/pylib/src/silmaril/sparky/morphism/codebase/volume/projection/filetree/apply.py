from config.gate.external.python.morphism.codebase.volume.projection.filetree.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.projection.filetree.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.projection.filetree.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
