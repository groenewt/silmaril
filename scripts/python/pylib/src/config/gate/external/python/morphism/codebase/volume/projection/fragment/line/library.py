from config.constants.morphism.codebase.volume.projection.fragment.line.absent.message.value import VALUE as ABSENT_MESSAGE
from config.constants.morphism.codebase.volume.projection.fragment.line.blank.message.value import VALUE as BLANK_MESSAGE
from config.constants.morphism.codebase.volume.projection.fragment.line.empty.value import VALUE as EMPTY
from config.constants.morphism.codebase.volume.projection.fragment.line.separator.value import VALUE as SEPARATOR
from config.constants.morphism.codebase.volume.projection.fragment.line.unterminated.message.value import VALUE as UNTERMINATED_MESSAGE
from config.constants.substrate.byte.vector.lexical.encoding.host.python.value import VALUE as ENCODING


def LINES(payload: bytes) -> tuple:
    text = payload.decode(ENCODING.decode())
    parts = text.split(SEPARATOR)
    if parts[-1] != EMPTY:
        raise ValueError(UNTERMINATED_MESSAGE % text)
    entries = tuple(parts[:-1])
    if not entries:
        raise ValueError(ABSENT_MESSAGE % text)
    for entry in entries:
        if entry == EMPTY:
            raise ValueError(BLANK_MESSAGE % text)
    return entries
