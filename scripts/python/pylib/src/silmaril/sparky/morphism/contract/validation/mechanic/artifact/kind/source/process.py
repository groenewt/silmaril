from config.gate.external.python.stdlib.pickle.library import DEPENDENCY as _PICKLE
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as _SYS

_SEPARATOR = b"\x00"


def MAIN() -> int:
    values = [_PICKLE.load(_SYS.stdin.buffer) for _index in range(9)]
    _SYS.stdout.buffer.write(_SEPARATOR.join(values))
    return 0


raise SystemExit(MAIN())
