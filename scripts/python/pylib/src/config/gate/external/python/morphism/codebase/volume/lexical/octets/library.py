from config.constants.substrate.byte.vector.lexical.encoding.host.python.value import VALUE as ENCODING

ERRORS = "surrogateescape"
LEXICON = ENCODING.decode()


def OCTETS(text: str) -> bytes:
    return text.encode(LEXICON, ERRORS)
