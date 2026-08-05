from config.gate.external.python.morphism.codebase.volume.shared.anchor.cross_volume.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.shared.anchor.cross_volume.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.shared.anchor.cross_volume.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
