from config.constants.substrate.byte.vector.lexical.encoding.host.python.value import VALUE as ENCODING
from config.gate.external.python.stdlib.hashlib.library import DEPENDENCY as HASHLIB

ERRORS = "surrogateescape"
LEXICON = ENCODING.decode()


def DIGEST(text: str) -> str:
    return HASHLIB.sha256(text.encode(LEXICON, ERRORS)).hexdigest()
