from config.gate.external.python.stdlib.sys.argv.library import DEPENDENCY as ARGV

ARGUMENTS_START = 2


def ARGUMENTS() -> list:
    return list(ARGV[ARGUMENTS_START:])
