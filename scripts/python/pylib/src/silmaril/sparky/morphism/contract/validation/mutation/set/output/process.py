from config.gate.external.python.stdlib.pickle.library import DEPENDENCY as _PICKLE
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as _SYS


def MAIN() -> int:
    replacement = _PICKLE.load(_SYS.stdin.buffer)
    _SYS.stdout.buffer.write(replacement)
    return 0


raise SystemExit(MAIN())
