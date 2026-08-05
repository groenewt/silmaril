from config.gate.external.python.morphism.codebase.volume.ring.family.dunbar_inner_5.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.ring.family.dunbar_inner_5.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.ring.family.dunbar_inner_5.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
