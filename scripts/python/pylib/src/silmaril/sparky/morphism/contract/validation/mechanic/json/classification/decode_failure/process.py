from config.constants.morphism.contract.validation.classification.decode_failure.value import VALUE as _TOKEN
from config.gate.external.python.stdlib.re.library import DEPENDENCY as _REGEX
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as _SYS

_UNCLASSIFIED = rb"(?!(?:accepted|decode_failure|parse_failure|rejected)\Z)"
_JSON_STRING_CONTENT = rb'(?:\\(?:["\\/bfnrt]|u[0-9A-Fa-f]{4})|[\x20-\x21\x23-\x5b\x5d-\x7e])*'
_JSON_STRING = rb'\"' + _JSON_STRING_CONTENT + rb'\"'
_JSON_NUMBER = rb"-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?"
_JSON_SCALAR = rb"(?:" + _JSON_STRING + rb"|" + _JSON_NUMBER + rb"|true|false|null)"
_JSON_MEMBER = _JSON_STRING + rb"\s*:\s*" + _JSON_SCALAR
_JSON_OBJECT = rb"\{\s*(?:" + _JSON_MEMBER + rb"(?:\s*,\s*" + _JSON_MEMBER + rb")*)?\s*\}"
_JSON_ARRAY = rb"\[\s*(?:" + _JSON_SCALAR + rb"(?:\s*,\s*" + _JSON_SCALAR + rb")*)?\s*\]"
_JSON_DOCUMENT = rb"(?:" + _JSON_OBJECT + rb"|" + _JSON_ARRAY + rb"|" + _JSON_SCALAR + rb")"
_UNIQUE_OBJECT_KEYS = rb'(?![\x00-\xff]*\"(?P<accepted_key>' + _JSON_STRING_CONTENT + rb')\"\s*:[\x00-\xff]*\"(?P=accepted_key)\"\s*:)'
_DUPLICATE_OBJECT_KEY = rb'(?=[\x00-\xff]*\"(?P<duplicate_key>' + _JSON_STRING_CONTENT + rb')\"\s*:[\x00-\xff]*\"(?P=duplicate_key)\"\s*:)'
_PATTERN = rb"\A" + _UNCLASSIFIED + rb"[\x00-\xff]*[\x80-\xff][\x00-\xff]*\Z"


def MAIN() -> int:
    _SYS.stdout.buffer.write(
        _REGEX.sub(_PATTERN, _TOKEN, _SYS.stdin.buffer.read())
    )
    return 0


raise SystemExit(MAIN())
