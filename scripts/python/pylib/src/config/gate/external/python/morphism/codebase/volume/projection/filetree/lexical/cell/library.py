import re

from config.constants.morphism.codebase.volume.projection.filetree.lexical.wrap.replacement.value import VALUE as WRAP_REPLACEMENT
from config.constants.morphism.codebase.volume.projection.filetree.lexical.wrap.rule.value import VALUE as WRAP_RULE_SOURCE
from config.constants.morphism.codebase.volume.projection.inventory.cell.limit.value import VALUE as LIMIT
from config.constants.morphism.codebase.volume.projection.inventory.cell.truncation.template.value import VALUE as TRUNCATION
from config.constants.substrate.byte.vector.lexical.encoding.host.python.value import VALUE as ENCODING
from config.gate.external.python.morphism.codebase.volume.lexical.digest.library import DIGEST
from config.gate.external.python.morphism.codebase.volume.projection.filetree.lexical.escape.library import ESCAPE

ERRORS = "surrogateescape"
EXCERPT_ERRORS = "replace"
LEXICON = ENCODING.decode()
ORIGIN = 0

WRAP_RULE = re.compile(WRAP_RULE_SOURCE)


def PAYLOAD(text: str) -> bytes:
    return text.encode(LEXICON, ERRORS)


def EXCERPT(payload: bytes) -> str:
    return payload[ORIGIN:LIMIT].decode(LEXICON, EXCERPT_ERRORS)


def BOUNDED(text: str) -> str:
    return TRUNCATION % (ESCAPE(EXCERPT(PAYLOAD(text))), LIMIT, len(PAYLOAD(text)), DIGEST(text))


WIDTH = {True: ESCAPE, False: BOUNDED}


def CELL(text: str) -> str:
    return WIDTH[len(PAYLOAD(text)) <= LIMIT](text)


def WRAP(rendered: str) -> str:
    return WRAP_RULE.sub(WRAP_REPLACEMENT, rendered)


def BREAKABLE(text: str) -> str:
    return WRAP(CELL(text))
