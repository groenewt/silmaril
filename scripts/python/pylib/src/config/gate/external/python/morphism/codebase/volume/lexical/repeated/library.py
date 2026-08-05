from config.constants.morphism.codebase.volume.lexical.repeated.threshold.value import VALUE as THRESHOLD
from config.gate.external.python.morphism.codebase.volume.lexical.pairs.library import PAIRS
from config.gate.external.python.morphism.codebase.volume.lexical.tallies.library import TALLIES


def REPEATED(values: list) -> list:
    return [value for value, tally in PAIRS(TALLIES(values)) if tally > THRESHOLD]
