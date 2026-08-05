from config.gate.external.python.stdlib.sys.stdin.library import DEPENDENCY as STDIN


def READ() -> bytes:
    return STDIN.read()
