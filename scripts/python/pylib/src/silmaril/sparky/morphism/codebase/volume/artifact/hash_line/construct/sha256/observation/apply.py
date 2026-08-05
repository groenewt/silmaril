from config.gate.external.python.morphism.codebase.volume.artifact.hash_line.construct.sha256.observation.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.artifact.hash_line.construct.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.artifact.hash_line.construct.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
