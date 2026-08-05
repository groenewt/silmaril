from config.gate.external.python.stdlib.re.library import DEPENDENCY as RE


def PATTERN(expression: str) -> object:
    return RE.compile(expression)
