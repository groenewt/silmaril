from config.gate.external.python.stdlib.re.library import DEPENDENCY as REGEX

GRAMMAR = REGEX.compile(r"\A(.+?):([0-9]+):(.*?)(?:\r?\n)?\Z", REGEX.DOTALL)
UNPARSED_PATH = ""
UNPARSED_NUMBER = "0"


def RECORD(raw: str) -> list:
    match = GRAMMAR.match(raw)
    if match is None:
        return [UNPARSED_PATH, UNPARSED_NUMBER, raw]
    return [match.group(1), match.group(2), match.group(3)]
