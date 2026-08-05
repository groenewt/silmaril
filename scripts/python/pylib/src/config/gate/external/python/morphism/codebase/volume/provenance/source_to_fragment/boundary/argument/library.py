from config.gate.external.python.morphism.codebase.volume.codec.library import ENCODE
from silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.construct.input.value import Value as Input


def INPUT(arguments: list) -> Input:
    return Input(ENCODE(arguments))
