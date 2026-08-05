from config.gate.external.python.morphism.contract.validation.schema.format.uri.pattern.value import VALUE as _FORMAT
from config.constants.morphism.contract.validation.classification.accepted.value import VALUE as _TOKEN
from config.gate.external.python.stdlib.re.library import DEPENDENCY as _REGEX
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as _SYS

_UNCLASSIFIED = rb"(?!(?:accepted|decode_failure|parse_failure|rejected)\Z)"
_PATTERN = rb"\A" + _UNCLASSIFIED + _FORMAT + rb"\Z"


def MAIN() -> int:
    _SYS.stdout.buffer.write(
        _REGEX.sub(_PATTERN, _TOKEN, _SYS.stdin.buffer.read())
    )
    return 0


raise SystemExit(MAIN())
