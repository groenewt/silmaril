SEPARATOR = "/"
EMPTY_SEGMENT = ""


def SPLIT(text: str) -> list:
    segments = text.split(SEPARATOR)
    while segments and segments[-1] == EMPTY_SEGMENT:
        segments.pop()
    return segments
