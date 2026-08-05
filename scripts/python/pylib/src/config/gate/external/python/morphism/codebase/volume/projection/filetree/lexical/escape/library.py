from config.constants.morphism.codebase.volume.projection.inventory.lexical.escape.map.value import VALUE as ESCAPE_MAP
from config.constants.morphism.codebase.volume.projection.inventory.lexical.space.value import VALUE as SPACE

CONTROL_LIMIT = 32
DELETE_ORDINAL = 127

CONTROL = {ordinal: SPACE for ordinal in range(CONTROL_LIMIT)}
DELETE = {DELETE_ORDINAL: SPACE}
RESERVED = {ord(source): target for source, target in ESCAPE_MAP}
TABLE = CONTROL | DELETE | RESERVED


def ESCAPE(text: str) -> str:
    return text.translate(TABLE)
