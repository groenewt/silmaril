from config.constants.morphism.provenance.commit.classification.unknown.value import VALUE as _UNKNOWN
from config.constants.morphism.provenance.commit.record.document.separator.value import VALUE as _DOCUMENT
from config.constants.morphism.provenance.commit.record.field.separator.value import VALUE as _FIELD
from config.gate.external.python.stdlib.re.library import DEPENDENCY as _REGEX
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as _SYS

_KEYED_RECORD = (
    rb"(?m)^([0-9a-f]{40})"
    + _FIELD
    + rb"[^\x1f\n]*"
    + _FIELD
    + rb"[0-9a-f]{40}"
    + _FIELD
    + rb"[^\x1f\n]*"
    + _FIELD
    + rb"([^\x1f\n]+)"
    + _FIELD
    + rb"[^\x1f\n]*"
    + _FIELD
    + rb"[^\x1f\n]*"
    + _FIELD
    + rb"([^\n]*)$"
)
_KEYLESS_RECORD = (
    rb"(?m)^([0-9a-f]{40})"
    + _FIELD
    + rb"[^\x1f\n]*"
    + _FIELD
    + rb"[0-9a-f]{40}"
    + _FIELD
    + rb"[^\x1f\n]*"
    + _FIELD
    + _FIELD
    + rb"[^\x1f\n]*"
    + _FIELD
    + rb"[^\x1f\n]*"
    + _FIELD
    + rb"([^\n]*)$"
)
_KEYED_LINE = (
    _UNKNOWN
    + _FIELD
    + b"\\1"
    + _FIELD
    + b"-"
    + _FIELD
    + b"\\2"
    + _FIELD
    + b"\\3"
)
_KEYLESS_LINE = (
    _UNKNOWN
    + _FIELD
    + b"\\1"
    + _FIELD
    + b"-"
    + _FIELD
    + b"?"
    + _FIELD
    + b"\\2"
)
_TAIL = rb"(?s)" + _DOCUMENT + rb"\n.*\Z"


def MAIN() -> int:
    _SYS.stdout.buffer.write(
        _REGEX.sub(
            _TAIL,
            b"",
            _REGEX.sub(
                _KEYLESS_RECORD,
                _KEYLESS_LINE,
                _REGEX.sub(
                    _KEYED_RECORD,
                    _KEYED_LINE,
                    _SYS.stdin.buffer.read(),
                ),
            ),
        )
    )
    return 0


raise SystemExit(MAIN())
