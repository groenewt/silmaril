from config.constants.morphism.provenance.commit.classification.bad.signature.value import VALUE as _BAD_SIGNATURE
from config.constants.morphism.provenance.commit.record.field.separator.value import VALUE as _FIELD
from config.constants.morphism.provenance.commit.signature.type.pretty.good.privacy.value import VALUE as _PRETTY_GOOD_PRIVACY
from config.gate.external.python.stdlib.re.library import DEPENDENCY as _REGEX
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as _SYS

_KEYED_RECORD = (
    rb"(?m)^([0-9a-f]{40})"
    + _FIELD
    + _PRETTY_GOOD_PRIVACY
    + _FIELD
    + rb"\1"
    + _FIELD
    + rb"B"
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
    + _PRETTY_GOOD_PRIVACY
    + _FIELD
    + rb"\1"
    + _FIELD
    + rb"B"
    + _FIELD
    + _FIELD
    + rb"[^\x1f\n]*"
    + _FIELD
    + rb"[^\x1f\n]*"
    + _FIELD
    + rb"([^\n]*)$"
)
_KEYED_LINE = (
    _BAD_SIGNATURE
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
    _BAD_SIGNATURE
    + _FIELD
    + b"\\1"
    + _FIELD
    + b"-"
    + _FIELD
    + b"?"
    + _FIELD
    + b"\\2"
)


def MAIN() -> int:
    _SYS.stdout.buffer.write(
        _REGEX.sub(
            _KEYLESS_RECORD,
            _KEYLESS_LINE,
            _REGEX.sub(
                _KEYED_RECORD,
                _KEYED_LINE,
                _SYS.stdin.buffer.read(),
            ),
        )
    )
    return 0


raise SystemExit(MAIN())
