from config.gate.external.python.morphism.codebase.volume.verification.twin_readback.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.verification.twin_readback.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.verification.twin_readback.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
