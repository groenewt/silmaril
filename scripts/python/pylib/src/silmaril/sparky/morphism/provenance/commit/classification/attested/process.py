from config.constants.morphism.provenance.commit.classification.attested.value import VALUE as _ATTESTED
from config.constants.morphism.provenance.commit.record.field.separator.value import VALUE as _FIELD
from config.constants.morphism.provenance.commit.signature.type.pretty.good.privacy.value import VALUE as _PRETTY_GOOD_PRIVACY
from config.gate.external.python.stdlib.re.library import DEPENDENCY as _REGEX
from config.gate.external.python.stdlib.sys.library import DEPENDENCY as _SYS

_UNAVAILABLE_KEY_RECORD = (
    rb"(?m)^([0-9a-f]{40})"
    + _FIELD
    + _PRETTY_GOOD_PRIVACY
    + _FIELD
    + rb"\1"
    + _FIELD
    + rb"E"
    + _FIELD
    + rb"[0-9A-F]*([0-9A-F]{16})"
    + _FIELD
    + rb"[^\x1f\n]*"
    + _FIELD
    + rb"[^\x1f\n]*"
    + _FIELD
    + rb"([^\n]*)$(?=[\s\S]*?\n([0-9A-F]{24}\2)[ \t]+([^ \t\n]+))"
)
_LINE = (
    _ATTESTED
    + _FIELD
    + b"\\1"
    + _FIELD
    + b"\\5"
    + _FIELD
    + b"\\4"
    + _FIELD
    + b"\\3"
)


def MAIN() -> int:
    _SYS.stdout.buffer.write(
        _REGEX.sub(
            _UNAVAILABLE_KEY_RECORD,
            _LINE,
            _SYS.stdin.buffer.read(),
        )
    )
    return 0


raise SystemExit(MAIN())
