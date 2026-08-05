from config.gate.external.python.morphism.codebase.volume.source.observation.state.loci.library import LOCI
from config.gate.external.python.morphism.codebase.volume.source.observation.strict.library import STRICT
from config.gate.external.python.stdlib.os.path.lexists.library import DEPENDENCY as LEXISTS

VIOLATION = "observation_path_missing="


def STATE(state: dict) -> dict:
    vanished = [locus for locus in LOCI(state) if not LEXISTS(locus)]
    if vanished and STRICT():
        raise ValueError(VIOLATION + vanished[0])
    return state
