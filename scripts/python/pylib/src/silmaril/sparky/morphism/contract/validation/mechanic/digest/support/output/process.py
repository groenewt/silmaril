from config.constants.morphism.contract.validation.classification.accepted.value import VALUE as _ACCEPTED_CLASS
from config.constants.morphism.contract.validation.classification.decode_failure.value import VALUE as _DECODE_FAILURE_CLASS
from config.constants.morphism.contract.validation.classification.parse_failure.value import VALUE as _PARSE_FAILURE_CLASS
from config.constants.morphism.contract.validation.classification.rejected.value import VALUE as _REJECTED_CLASS
from config.constants.morphism.contract.validation.truth.accepted.value import VALUE as _ACCEPTED
from config.constants.morphism.contract.validation.truth.rejected.value import VALUE as _REJECTED
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as _SYS

_OUTPUTS = {
    _ACCEPTED_CLASS: _ACCEPTED,
    _DECODE_FAILURE_CLASS: _REJECTED,
    _PARSE_FAILURE_CLASS: _REJECTED,
    _REJECTED_CLASS: _REJECTED,
}


def MAIN() -> int:
    _SYS.stdout.buffer.write(_OUTPUTS[_SYS.stdin.buffer.read()])
    return 0


raise SystemExit(MAIN())
