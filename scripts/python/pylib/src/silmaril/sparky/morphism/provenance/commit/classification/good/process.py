from config.constants.morphism.provenance.commit.classification.good.value import VALUE as _GOOD
from config.constants.morphism.provenance.commit.record.field.separator.value import VALUE as _FIELD
from config.constants.morphism.provenance.commit.signature.type.pretty.good.privacy.value import VALUE as _PRETTY_GOOD_PRIVACY
from config.gate.external.python.stdlib.re.library import DEPENDENCY as _REGEX
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as _SYS

_PRIMARY_RECORD = (
    rb"(?m)^([0-9a-f]{40})"
    + _FIELD
    + _PRETTY_GOOD_PRIVACY
    + _FIELD
    + rb"\1"
    + _FIELD
    + rb"[GU]"
    + _FIELD
    + rb"[^\x1f\n]*"
    + _FIELD
    + rb"([0-9A-F]{40})"
    + _FIELD
    + rb"[^\x1f\n]*"
    + _FIELD
    + rb"([^\n]*)$(?=[\s\S]*?\n\2[ \t]+([^ \t\n]+))"
)
_FALLBACK_RECORD = (
    rb"(?m)^([0-9a-f]{40})"
    + _FIELD
    + _PRETTY_GOOD_PRIVACY
    + _FIELD
    + rb"\1"
    + _FIELD
    + rb"[GU]"
    + _FIELD
    + rb"[^\x1f\n]*"
    + _FIELD
    + _FIELD
    + rb"([0-9A-F]{40})"
    + _FIELD
    + rb"([^\n]*)$(?=[\s\S]*?\n\2[ \t]+([^ \t\n]+))"
)
_LINE = (
    _GOOD
    + _FIELD
    + b"\\1"
    + _FIELD
    + b"\\4"
    + _FIELD
    + b"\\2"
    + _FIELD
    + b"\\3"
)


def MAIN() -> int:
    _SYS.stdout.buffer.write(
        _REGEX.sub(
            _FALLBACK_RECORD,
            _LINE,
            _REGEX.sub(
                _PRIMARY_RECORD,
                _LINE,
                _SYS.stdin.buffer.read(),
            ),
        )
    )
    return 0


raise SystemExit(MAIN())
