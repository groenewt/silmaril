from config.gate.external.python.morphism.codebase.volume.artifact.manifest.input.frame.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.artifact.manifest.frame.value import Value as Frame


def apply(arguments: list) -> Frame:
    return PROJECT(arguments)
