from config.constants.substrate.byte.vector.lexical.encoding.host.python.value import VALUE as ENCODING
from config.gate.external.python.stdlib.builtins.open.library import DEPENDENCY as OPEN

CARRIAGE_RETURN = "\r"
ERRORS = "surrogateescape"
LEXICON = ENCODING.decode()
LINE_FEED = "\n"
MODE = "r"
UNTRANSLATED = ""


def HEAD(path: str) -> str:
    with OPEN(path, MODE, encoding=LEXICON, errors=ERRORS, newline=UNTRANSLATED) as handle:
        line = handle.readline()
    without_feed = line.removesuffix(LINE_FEED)
    return without_feed.removesuffix(CARRIAGE_RETURN)
