from config.constants.substrate.byte.vector.lexical.encoding.host.python.value import VALUE as ENCODING
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

ERRORS = "surrogateescape"
LEXICON = ENCODING.decode()


def VECTOR(text: str) -> ByteVector:
    return ByteVector(text.encode(LEXICON, ERRORS))
