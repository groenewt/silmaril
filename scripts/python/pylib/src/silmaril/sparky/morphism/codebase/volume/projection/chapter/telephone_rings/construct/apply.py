from config.gate.external.python.morphism.codebase.volume.projection.chapter.telephone_rings.construct.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.projection.fragment.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.projection.fragment.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
