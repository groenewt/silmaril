from config.gate.external.python.morphism.codebase.volume.artifact.atomic_delivery.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.artifact.atomic_delivery.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.artifact.atomic_delivery.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
