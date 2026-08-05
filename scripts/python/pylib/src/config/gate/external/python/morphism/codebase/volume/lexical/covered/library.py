def COVERED(pair: list) -> bool:
    segments, prefix = pair
    return segments[: len(prefix)] == prefix
