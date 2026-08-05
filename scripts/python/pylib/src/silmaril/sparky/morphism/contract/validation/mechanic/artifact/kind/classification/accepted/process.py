from config.constants.morphism.contract.validation.classification.accepted.value import VALUE as _TOKEN
from config.gate.external.python.stdlib.re.library import DEPENDENCY as _REGEX
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as _SYS

_UNCLASSIFIED = rb"(?!(?:accepted|decode_failure|parse_failure|rejected)\Z)"
_NONEMPTY_FIELD = rb"[^\x00]+"
_FIELD = rb"[^\x00]*"
_KNOWN_KIND = rb"(?:code-property-language-topology|scene|lexicon|validation-profile|lambda-runtime-constants|lambda-runtime-gateway|source-continuation)"
_KNOWN_REGISTRATION = rb"(?:true|false)\x00" + _KNOWN_KIND + rb"\x00" + _NONEMPTY_FIELD + rb"\x00" + _NONEMPTY_FIELD + rb"\x00" + _FIELD + rb"\x00" + _FIELD + rb"\x00" + _FIELD + rb"\x00" + _FIELD + rb"\x00" + _FIELD
_OPEN_PROVISIONAL_REGISTRATION = rb"false\x00" + _NONEMPTY_FIELD + rb"\x00" + _NONEMPTY_FIELD + rb"\x00" + _NONEMPTY_FIELD + rb"\x00(?P<registration_schema>[^\x00]+)\x00provisional\x00" + _NONEMPTY_FIELD + rb"\x00(?P=registration_schema)\x00(?P=registration_schema)"
_PATTERN = rb"\A" + _UNCLASSIFIED + rb"(?:" + _KNOWN_REGISTRATION + rb"|" + _OPEN_PROVISIONAL_REGISTRATION + rb")\Z"


def MAIN() -> int:
    _SYS.stdout.buffer.write(
        _REGEX.sub(_PATTERN, _TOKEN, _SYS.stdin.buffer.read())
    )
    return 0


raise SystemExit(MAIN())
