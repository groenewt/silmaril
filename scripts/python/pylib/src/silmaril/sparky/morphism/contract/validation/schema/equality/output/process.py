from config.constants.morphism.contract.validation.truth.accepted.value import VALUE as _ACCEPTED
from config.constants.morphism.contract.validation.truth.rejected.value import VALUE as _REJECTED
from config.gate.external.python.stdlib.pickle.library import DEPENDENCY as _PICKLE
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as _SYS


def MAIN() -> int:
    left = _PICKLE.load(_SYS.stdin.buffer)
    right = _PICKLE.load(_SYS.stdin.buffer)
    _SYS.stdout.buffer.write(_ACCEPTED if left == right else _REJECTED)
    return 0


raise SystemExit(MAIN())
