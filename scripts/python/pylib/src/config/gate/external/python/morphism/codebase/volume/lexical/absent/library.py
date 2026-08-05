from config.gate.external.python.morphism.codebase.volume.lexical.keyed.library import KEYED


def ABSENT(candidates: list, reference: list) -> list:
    return [value for value in candidates if value not in KEYED(reference)]
