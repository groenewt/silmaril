from config.constants.substrate.byte.vector.lexical.encoding.host.python.value import VALUE as ENCODING

ERRORS = "surrogateescape"
LEXICON = ENCODING.decode()


def TEXT(payload: bytes) -> str:
    return payload.decode(LEXICON, ERRORS)
