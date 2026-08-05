from config.constants.morphism.codebase.volume.artifact.hash_manifest.state.payloads.key.value import VALUE as PAYLOADS_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.hash_manifest.state.sources.library import SOURCES
from config.gate.external.python.morphism.codebase.volume.boundary.file.bytes.library import BYTES
from config.gate.external.python.morphism.codebase.volume.boundary.file.path.library import PATH
from config.gate.external.python.morphism.codebase.volume.lexical.text.library import TEXT


def STATE(state: dict) -> dict:
    return {**state, PAYLOADS_KEY: [TEXT(BYTES(PATH(source))) for source in SOURCES(state)]}
