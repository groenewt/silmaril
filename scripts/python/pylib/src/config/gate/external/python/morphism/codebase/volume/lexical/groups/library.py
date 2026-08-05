UNMATCHED = ()


def GROUPS(match: object) -> list:
    if match is None:
        return list(UNMATCHED)
    return list(match.groups())
