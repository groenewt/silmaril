from config.gate.external.python.morphism.codebase.volume.ring.family.native_pool.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.ring.family.native_pool.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.ring.family.native_pool.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
