LINE_FEED = "\n"
CARRIAGE_RETURN = "\r"


def CHOMP(text: str) -> str:
    return text.removesuffix(LINE_FEED).removesuffix(CARRIAGE_RETURN)
