from config.constants.morphism.codebase.volume.provenance.source_to_fragment.column.artifact.value import VALUE as ARTIFACT_COLUMN
from config.constants.morphism.codebase.volume.provenance.source_to_fragment.column.fragment.value import VALUE as FRAGMENT_COLUMN
from config.constants.morphism.codebase.volume.provenance.source_to_fragment.column.identity.value import VALUE as IDENTITY_COLUMN
from config.constants.morphism.codebase.volume.provenance.source_to_fragment.state.relation.key.value import VALUE as RELATION_KEY
from config.gate.external.python.morphism.codebase.volume.lexical.csv.rows.library import ROWS
from config.gate.external.python.morphism.codebase.volume.provenance.source_to_fragment.state.contract.library import CONTRACT
from config.gate.external.python.stdlib.os.path.lexists.library import DEPENDENCY as LEXISTS

ABSENCE_VIOLATION = "source_to_fragment_contract_missing="
BODY_ORIGIN = 1
COLUMN_VIOLATION = "source_to_fragment_contract_column_absent="
HEADER_ORIGIN = 0


def STATE(state: dict) -> dict:
    contract = CONTRACT(state)
    if not LEXISTS(contract):
        raise ValueError(ABSENCE_VIOLATION + contract)
    rows = ROWS(contract)
    header = rows[HEADER_ORIGIN]
    for column in (IDENTITY_COLUMN, ARTIFACT_COLUMN, FRAGMENT_COLUMN):
        if column not in header:
            raise ValueError(COLUMN_VIOLATION + column)
    identity = header.index(IDENTITY_COLUMN)
    artifact = header.index(ARTIFACT_COLUMN)
    fragment = header.index(FRAGMENT_COLUMN)
    relation = [[row[identity], row[artifact], row[fragment]] for row in rows[BODY_ORIGIN:]]
    return {**state, RELATION_KEY: sorted(relation)}
