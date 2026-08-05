from config.constants.morphism.codebase.volume.projection.inventory.header.absent.message.value import VALUE as HEADER_ABSENT
from config.constants.morphism.codebase.volume.projection.inventory.lexical.empty.value import VALUE as EMPTY
from config.constants.substrate.byte.vector.lexical.encoding.host.python.value import VALUE as ENCODING
from config.gate.external.python.stdlib.csv.reader.library import DEPENDENCY as READER
from config.gate.external.python.stdlib.io.string_io.library import DEPENDENCY as StringIO

ERRORS = "surrogateescape"
HEADER_POSITION = 0
LEXICON = ENCODING.decode()
UNTRANSLATED = ""


def TABLE(payload: bytes) -> list:
    text = payload.decode(LEXICON, ERRORS)
    if text == EMPTY:
        raise ValueError(HEADER_ABSENT)
    rows = list(READER(StringIO(text, newline=UNTRANSLATED)))
    if not rows:
        raise ValueError(HEADER_ABSENT)
    return rows


def HEADER(rows: list) -> list:
    return rows[HEADER_POSITION]


def BODY(rows: list) -> list:
    return rows[HEADER_POSITION + 1:]
