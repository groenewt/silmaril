from config.gate.external.python.morphism.codebase.volume.shared.anchor.global_architecture.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.shared.anchor.global_architecture.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.shared.anchor.global_architecture.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
