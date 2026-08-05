from config.gate.external.python.morphism.codebase.volume.shared.component.title_metadata.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.shared.component.title_metadata.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.shared.component.title_metadata.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
