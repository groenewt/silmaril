from config.gate.external.python.stdlib.sys.stdout.library import DEPENDENCY as STDOUT


def WRITE(payload: bytes) -> int:
    return STDOUT.write(payload)
