from config.constants.morphism.codebase.volume.artifact.hash_manifest.state.matches.key.value import VALUE as MATCHES_KEY
from config.constants.morphism.codebase.volume.digest.pattern.value import VALUE as EXPRESSION
from config.gate.external.python.morphism.codebase.volume.artifact.hash_manifest.state.lines.library import LINES_OF
from config.gate.external.python.morphism.codebase.volume.lexical.groups.library import GROUPS
from config.gate.external.python.morphism.codebase.volume.lexical.match.library import MATCH
from config.gate.external.python.morphism.codebase.volume.lexical.pattern.library import PATTERN


def STATE(state: dict) -> dict:
    pattern = PATTERN(EXPRESSION)
    return {**state, MATCHES_KEY: [GROUPS(MATCH([pattern, line])) for line in LINES_OF(state)]}
