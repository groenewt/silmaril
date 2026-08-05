from config.gate.external.python.morphism.codebase.volume.ring.family.dunbar_150.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.ring.family.dunbar_150.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.ring.family.dunbar_150.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
