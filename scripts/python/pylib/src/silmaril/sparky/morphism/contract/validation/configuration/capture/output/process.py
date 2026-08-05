from config.gate.external.python.stdlib.sys.library import DEPENDENCY as _SYS


def MAIN() -> int:
    _SYS.stdout.buffer.write(_SYS.stdin.buffer.read())
    return 0


raise SystemExit(MAIN())
