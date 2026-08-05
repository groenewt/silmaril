from config.gate.external.python.stdlib.sys.argv.library import DEPENDENCY as ARGV

ROOT_POSITION = 1


def ROOT() -> str:
    return ARGV[ROOT_POSITION]
