from config.constants.morphism.codebase.volume.table.aggregate.state.groups.key.value import VALUE as GROUPS_KEY
from config.gate.external.python.morphism.codebase.volume.boundary.arguments.library import ARGUMENTS
from config.gate.external.python.morphism.codebase.volume.boundary.root.library import ROOT
from config.gate.external.python.stdlib.csv.reader.library import DEPENDENCY as READER


def STATE(unused: list) -> dict:
    sources = [ROOT()] + ARGUMENTS()
    return {GROUPS_KEY: [[source, [row for row in READER(open(source, newline=''))]] for source in sources]}
