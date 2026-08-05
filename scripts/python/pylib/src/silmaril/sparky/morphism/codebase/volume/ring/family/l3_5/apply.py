from config.gate.external.python.morphism.codebase.volume.ring.family.l3_5.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.ring.family.l3_5.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.ring.family.l3_5.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
