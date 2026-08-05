from config.gate.external.python.morphism.codebase.volume.codec.library import ENCODE
from silmaril.sparky.morphism.codebase.volume.artifact.hash_manifest.construct.input.value import Value as Input


def INPUT(arguments: list) -> Input:
    return Input(ENCODE(arguments))
