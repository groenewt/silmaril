from config.gate.external.python.morphism.codebase.volume.verification.reverse_discovery.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.verification.reverse_discovery.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.verification.reverse_discovery.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
