from config.constants.morphism.codebase.volume.projection.filetree.lead.value import VALUE as LEAD
from config.constants.morphism.codebase.volume.projection.filetree.toc.restore.value import VALUE as RESTORE
from config.constants.morphism.codebase.volume.projection.filetree.toc.template.value import VALUE as TOC
from config.constants.morphism.codebase.volume.projection.filetree.toc.tree.value import VALUE as TREE_DEPTH
from config.constants.morphism.codebase.volume.projection.inventory.lexical.empty.value import VALUE as EMPTY
from config.gate.external.python.morphism.codebase.volume.projection.filetree.census.library import CENSUS
from config.gate.external.python.morphism.codebase.volume.projection.filetree.relation.library import CONTRIBUTIONS
from config.gate.external.python.morphism.codebase.volume.projection.filetree.relation.library import CORPUS
from config.gate.external.python.morphism.codebase.volume.projection.filetree.tree.library import TREE


def FOREST(records: tuple) -> str:
    return TREE(CONTRIBUTIONS(CORPUS(records)))


def RENDER(records: tuple) -> str:
    return EMPTY.join((TOC % TREE_DEPTH, LEAD, CENSUS(records), FOREST(records), TOC % RESTORE))
