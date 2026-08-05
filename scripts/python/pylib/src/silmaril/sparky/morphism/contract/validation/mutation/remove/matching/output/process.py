from config.constants.morphism.contract.validation.mutation.remove.matching.mechanic.translation.table.value import VALUE as _TRANSLATION_TABLE
from config.gate.external.python.stdlib.pickle.library import DEPENDENCY as _PICKLE
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as _SYS


def MAIN() -> int:
    target = _PICKLE.load(_SYS.stdin.buffer)
    matching = _PICKLE.load(_SYS.stdin.buffer)
    _SYS.stdout.buffer.write(target.translate(_TRANSLATION_TABLE, matching))
    return 0


raise SystemExit(MAIN())
