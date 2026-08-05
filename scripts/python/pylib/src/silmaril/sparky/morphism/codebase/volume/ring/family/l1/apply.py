from config.gate.external.python.morphism.codebase.volume.ring.family.l1.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.ring.family.l1.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.ring.family.l1.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
