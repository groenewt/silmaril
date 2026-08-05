from config.constants.morphism.contract.validation.mutation.fill.preserving.length.mechanic.translation.table.value import VALUE as _TRANSLATION_TABLE
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as _SYS


def MAIN() -> int:
    _SYS.stdout.buffer.write(_SYS.stdin.buffer.read().translate(_TRANSLATION_TABLE))
    return 0


raise SystemExit(MAIN())
