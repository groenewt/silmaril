from config.gate.external.python.morphism.codebase.volume.source.observation.name_segment_excluded.name.presence.validation.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
