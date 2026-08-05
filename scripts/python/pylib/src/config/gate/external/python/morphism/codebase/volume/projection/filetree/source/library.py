from config.constants.substrate.byte.vector.lexical.encoding.host.python.value import VALUE as ENCODING
from config.gate.external.python.stdlib.builtins.next.library import DEPENDENCY as NEXT
from config.gate.external.python.stdlib.builtins.open.library import DEPENDENCY as OPEN
from config.gate.external.python.stdlib.csv.reader.library import DEPENDENCY as READER

ERRORS = "surrogateescape"
LEXICON = ENCODING.decode()
MODE = "r"
UNTRANSLATED = ""


def HANDLE(locus: str) -> object:
    return OPEN(locus, MODE, encoding=LEXICON, errors=ERRORS, newline=UNTRANSLATED)


def SCAN(locus: str) -> object:
    return READER(HANDLE(locus))


def HEADER(reader: object) -> tuple:
    return tuple(NEXT(reader))
