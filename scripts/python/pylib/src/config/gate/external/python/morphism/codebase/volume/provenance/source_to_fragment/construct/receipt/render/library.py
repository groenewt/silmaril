from config.constants.morphism.codebase.volume.provenance.source_to_fragment.column.artifact.value import VALUE as ARTIFACT_COLUMN
from config.constants.morphism.codebase.volume.provenance.source_to_fragment.column.fragment.value import VALUE as FRAGMENT_COLUMN
from config.constants.morphism.codebase.volume.provenance.source_to_fragment.column.identity.value import VALUE as IDENTITY_COLUMN
from config.gate.external.python.morphism.codebase.volume.lexical.csv.materialize.library import MATERIALIZE
from config.gate.external.python.morphism.codebase.volume.provenance.source_to_fragment.state.relation.library import RELATION

HEADER = [IDENTITY_COLUMN, ARTIFACT_COLUMN, FRAGMENT_COLUMN]


def RENDER(state: dict) -> str:
    return MATERIALIZE([HEADER, *RELATION(state)])
