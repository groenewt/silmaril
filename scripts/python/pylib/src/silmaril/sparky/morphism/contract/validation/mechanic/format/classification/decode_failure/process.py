from config.gate.external.python.morphism.contract.validation.schema.format.date.time.pattern.value import VALUE as _DATE_TIME
from config.gate.external.python.morphism.contract.validation.schema.format.uri.pattern.value import VALUE as _URI
from config.gate.external.python.morphism.contract.validation.schema.format.uri.reference.pattern.value import VALUE as _URI_REFERENCE
from config.constants.morphism.contract.validation.classification.decode_failure.value import VALUE as _TOKEN
from config.gate.external.python.stdlib.re.library import DEPENDENCY as _REGEX
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as _SYS

_UNCLASSIFIED = rb"(?!(?:accepted|decode_failure|parse_failure|rejected)\Z)"
_ACCEPTED_FORMAT = rb"(?:uri\x00" + _URI + rb"|uri-reference\x00" + _URI_REFERENCE + rb"|date-time\x00" + _DATE_TIME + rb")"
_PATTERN = rb"\A" + _UNCLASSIFIED + rb"[\x00-\xff]*[\x80-\xff][\x00-\xff]*\Z"


def MAIN() -> int:
    _SYS.stdout.buffer.write(
        _REGEX.sub(_PATTERN, _TOKEN, _SYS.stdin.buffer.read())
    )
    return 0


raise SystemExit(MAIN())
