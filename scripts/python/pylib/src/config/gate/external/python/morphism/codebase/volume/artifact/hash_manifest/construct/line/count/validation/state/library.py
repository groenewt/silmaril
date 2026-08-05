from config.gate.external.python.morphism.codebase.volume.artifact.hash_manifest.state.counts.library import COUNTS
from config.gate.external.python.morphism.codebase.volume.artifact.hash_manifest.state.sources.library import SOURCES
from config.gate.external.python.morphism.codebase.volume.artifact.strict.library import STRICT

VIOLATION = "hash_manifest_line_count_not_one="
EXPECTED = 1


def STATE(state: dict) -> dict:
    divergent = [source for source, count in zip(SOURCES(state), COUNTS(state)) if count != EXPECTED]
    if divergent and STRICT():
        raise ValueError(VIOLATION + divergent[0])
    return state
