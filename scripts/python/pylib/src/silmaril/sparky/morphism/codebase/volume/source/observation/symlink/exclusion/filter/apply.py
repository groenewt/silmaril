from config.gate.external.python.morphism.codebase.volume.source.observation.symlink.exclusion.filter.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.source.observation.symlink.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.source.observation.symlink.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
