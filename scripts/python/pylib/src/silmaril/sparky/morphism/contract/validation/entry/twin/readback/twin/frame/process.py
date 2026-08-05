from config.gate.external.python.stdlib.pickle.library import DEPENDENCY as _PICKLE
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as _SYS


def MAIN() -> int:
    _PICKLE.dump(_SYS.stdin.buffer.read(), _SYS.stdout.buffer)
    return 0


raise SystemExit(MAIN())
