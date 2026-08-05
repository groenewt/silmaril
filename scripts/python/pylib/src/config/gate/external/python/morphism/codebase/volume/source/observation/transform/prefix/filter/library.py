from config.constants.morphism.codebase.volume.source.observation.state.indices.key.value import VALUE as INDICES_KEY
from config.gate.external.python.morphism.codebase.volume.lexical.covered.library import COVERED
from config.gate.external.python.morphism.codebase.volume.lexical.split.library import SPLIT
from config.gate.external.python.morphism.codebase.volume.source.observation.state.paths.library import PATHS
from config.gate.external.python.morphism.codebase.volume.source.observation.state.prefixes.library import PREFIXES


def STATE(state: dict) -> dict:
    prefixes = [SPLIT(prefix) for prefix in PREFIXES(state)]
    return {**state, INDICES_KEY: [index for index, path in enumerate(PATHS(state)) if any(COVERED([SPLIT(path), prefix]) for prefix in prefixes)]}
