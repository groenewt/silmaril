import re

from config.constants.morphism.codebase.volume.projection.inventory.lexical.escape.map.value import VALUE as ESCAPE_MAP
from config.constants.morphism.codebase.volume.projection.inventory.lexical.space.value import VALUE as SPACE
from config.constants.morphism.codebase.volume.projection.inventory.lexical.wrap.span.value import VALUE as SPAN
from config.constants.morphism.codebase.volume.projection.inventory.lexical.wrap.token.value import VALUE as WRAP

CONTROL_LIMIT = 32
DELETE_ORDINAL = 127

TABLE = {ordinal: SPACE for ordinal in range(CONTROL_LIMIT)}
TABLE[DELETE_ORDINAL] = SPACE
for SOURCE, TARGET in ESCAPE_MAP:
    TABLE[ord(SOURCE)] = TARGET

WRAP_RULE = re.compile(r"((?:\\[A-Za-z]+\{\}|\\[^A-Za-z]|[^\\]){%d})" % SPAN)
WRAP_REPLACEMENT = r"\g<1>" + WRAP.replace("\\", r"\\")


def ESCAPE(text: str) -> str:
    return WRAP_RULE.sub(WRAP_REPLACEMENT, text.translate(TABLE))
