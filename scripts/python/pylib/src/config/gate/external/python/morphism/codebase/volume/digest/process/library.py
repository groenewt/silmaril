from config.gate.external.python.stdlib.subprocess.library import DEPENDENCY as SUBPROCESS

CAPTURE = True
CHECK = True


def PROCESS(command: tuple) -> object:
    return SUBPROCESS.run(command, capture_output=CAPTURE, check=CHECK)
