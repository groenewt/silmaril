CURRENT_DIRECTORY_PREFIX = "./"


def RELATIVE(text: str) -> str:
    return text.removeprefix(CURRENT_DIRECTORY_PREFIX)
