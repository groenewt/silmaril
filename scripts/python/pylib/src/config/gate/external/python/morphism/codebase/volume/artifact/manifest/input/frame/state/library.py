from config.constants.morphism.codebase.volume.artifact.manifest.state.artifact.key.value import VALUE as ARTIFACT_KEY
from config.constants.morphism.codebase.volume.artifact.manifest.state.contract.path.key.value import VALUE as CONTRACT_PATH_KEY
from config.constants.morphism.codebase.volume.artifact.manifest.state.csv_artifact.entry.key.value import VALUE as CSV_ARTIFACT_KEY
from config.gate.external.python.morphism.codebase.volume.boundary.root.library import ROOT
from config.gate.external.python.morphism.codebase.volume.lexical.integer.library import INTEGER

COUNT_POSITION = 0
LIST_START = 1
VIOLATION = "manifest_frame_csv_artifact_count_exceeds_arguments="


def STATE(arguments: list) -> dict:
    count = INTEGER(arguments[COUNT_POSITION])
    boundary = LIST_START + count
    if boundary > len(arguments):
        raise ValueError(VIOLATION + str(count))
    return {
        CONTRACT_PATH_KEY: ROOT(),
        CSV_ARTIFACT_KEY: arguments[LIST_START:boundary],
        ARTIFACT_KEY: arguments[boundary:],
    }
