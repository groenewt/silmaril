from config.constants.morphism.codebase.volume.projection.inventory.cell.limit.value import VALUE as LIMIT
from config.constants.morphism.codebase.volume.projection.inventory.cell.truncation.template.value import VALUE as TRUNCATION
from config.constants.morphism.codebase.volume.projection.inventory.lexical.empty.value import VALUE as EMPTY
from config.constants.substrate.byte.vector.lexical.encoding.host.python.value import VALUE as ENCODING
from config.gate.external.python.morphism.codebase.volume.lexical.digest.library import DIGEST
from config.gate.external.python.morphism.codebase.volume.projection.inventory.lexical.escape.library import ESCAPE

ERRORS = "surrogateescape"
EXCERPT_ERRORS = "replace"
LEXICON = ENCODING.decode()


def CELL(text: str) -> str:
    payload = text.encode(LEXICON, ERRORS)
    if len(payload) <= LIMIT:
        return ESCAPE(text)
    excerpt = payload[:LIMIT].decode(LEXICON, EXCERPT_ERRORS)
    return TRUNCATION % (ESCAPE(excerpt), LIMIT, len(payload), DIGEST(text))


def FIELD(row: list, index: int) -> str:
    return row[index] if index < len(row) else EMPTY
