PATTERN_POSITION = 0
TEXT_POSITION = 1


def MATCH(pair: list) -> object:
    return pair[PATTERN_POSITION].match(pair[TEXT_POSITION])
