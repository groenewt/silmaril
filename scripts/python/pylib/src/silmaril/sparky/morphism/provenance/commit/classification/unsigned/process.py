from config.constants.morphism.provenance.commit.classification.unsigned.value import VALUE as _UNSIGNED
from config.constants.morphism.provenance.commit.record.field.separator.value import VALUE as _FIELD
from config.constants.morphism.provenance.commit.signature.type.absent.value import VALUE as _ABSENT
from config.gate.external.python.stdlib.re.library import DEPENDENCY as _REGEX
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as _SYS

_RECORD = (
    rb"(?m)^([0-9a-f]{40})"
    + _FIELD
    + _ABSENT
    + _FIELD
    + rb"\1"
    + _FIELD
    + rb"[^\x1f\n]*"
    + _FIELD
    + rb"[^\x1f\n]*"
    + _FIELD
    + rb"[^\x1f\n]*"
    + _FIELD
    + rb"[^\x1f\n]*"
    + _FIELD
    + rb"([^\n]*)$"
)
_LINE = (
    _UNSIGNED
    + _FIELD
    + b"\\1"
    + _FIELD
    + b"-"
    + _FIELD
    + b"-"
    + _FIELD
    + b"\\2"
)


def MAIN() -> int:
    _SYS.stdout.buffer.write(
        _REGEX.sub(
            _RECORD,
            _LINE,
            _SYS.stdin.buffer.read(),
        )
    )
    return 0


raise SystemExit(MAIN())
