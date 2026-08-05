from config.constants.morphism.contract.validation.classification.accepted.value import VALUE as _ACCEPTED_CLASS
from config.constants.morphism.contract.validation.classification.decode_failure.value import VALUE as _DECODE_FAILURE_CLASS
from config.constants.morphism.contract.validation.classification.parse_failure.value import VALUE as _PARSE_FAILURE_CLASS
from config.constants.morphism.contract.validation.classification.rejected.value import VALUE as _REJECTED_CLASS
from config.constants.morphism.contract.validation.mechanic.format.effect.applied.identity.value import VALUE as _ACCEPTED_EFFECT
from config.constants.morphism.contract.validation.mechanic.format.effect.decode.failure.identity.value import VALUE as _DECODE_FAILURE_EFFECT
from config.constants.morphism.contract.validation.mechanic.format.effect.parse.failure.identity.value import VALUE as _PARSE_FAILURE_EFFECT
from config.constants.morphism.contract.validation.mechanic.format.effect.rejected.identity.value import VALUE as _REJECTED_EFFECT
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as _SYS

_EFFECTS = {
    _ACCEPTED_CLASS: _ACCEPTED_EFFECT,
    _DECODE_FAILURE_CLASS: _DECODE_FAILURE_EFFECT,
    _PARSE_FAILURE_CLASS: _PARSE_FAILURE_EFFECT,
    _REJECTED_CLASS: _REJECTED_EFFECT,
}


def MAIN() -> int:
    _SYS.stdout.buffer.write(_EFFECTS[_SYS.stdin.buffer.read()])
    return 0


raise SystemExit(MAIN())
