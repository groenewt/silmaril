from config.gate.external.python.morphism.codebase.volume.artifact.hash_manifest.construct.line.count.validation.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.artifact.hash_manifest.construct.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.artifact.hash_manifest.construct.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
