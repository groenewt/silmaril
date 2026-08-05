from config.gate.external.python.stdlib.hashlib.library import DEPENDENCY as _HASH
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as _SYS


def MAIN() -> int:
    _SYS.stdout.buffer.write(_HASH.sha256(_SYS.stdin.buffer.read()).digest())
    return 0


raise SystemExit(MAIN())
