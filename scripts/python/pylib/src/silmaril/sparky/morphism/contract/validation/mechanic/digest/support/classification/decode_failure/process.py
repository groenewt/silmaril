from config.constants.morphism.contract.validation.classification.decode_failure.value import VALUE as _TOKEN
from config.gate.external.python.stdlib.re.library import DEPENDENCY as _REGEX
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as _SYS

_UNCLASSIFIED = rb"(?!(?:accepted|decode_failure|parse_failure|rejected)\Z)"
_PATTERN = rb"\A" + _UNCLASSIFIED + rb"[\x00-\xff]*[\x80-\xff][\x00-\xff]*\Z"


def MAIN() -> int:
    _SYS.stdout.buffer.write(
        _REGEX.sub(_PATTERN, _TOKEN, _SYS.stdin.buffer.read())
    )
    return 0


raise SystemExit(MAIN())
