from config.gate.external.python.stdlib.sys.argv.library import DEPENDENCY as ARGV

ARGUMENT_ORIGIN = 1


def READ() -> list:
    return ARGV[ARGUMENT_ORIGIN:]
