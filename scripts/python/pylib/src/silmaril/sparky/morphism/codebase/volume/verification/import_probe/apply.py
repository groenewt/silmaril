from config.gate.external.python.morphism.codebase.volume.verification.import_probe.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.verification.import_probe.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.verification.import_probe.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
