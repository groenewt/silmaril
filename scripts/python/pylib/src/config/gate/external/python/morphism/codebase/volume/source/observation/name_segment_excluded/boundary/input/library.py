from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector
from silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.input.value import Value as Input


def INPUT(payload: bytes) -> Input:
    return Input(ByteVector(payload))
