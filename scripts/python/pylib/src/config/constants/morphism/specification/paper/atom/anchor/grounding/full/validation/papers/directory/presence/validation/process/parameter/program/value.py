from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.diagnostic.papers.directory.absent.prefix.value import VALUE as DIAGNOSTIC_PREFIX
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.papers.directory.presence.validation.process.parameter.argument.index.papers.directory.value import VALUE as PAPERS_DIRECTORY_ARGUMENT_INDEX
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.serialization.delimiter.line.value import VALUE as LINE_DELIMITER
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.cardinality.zero.value import VALUE as SUCCESS_STATUS
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.status.invalid.input.value import VALUE as INVALID_INPUT_STATUS

VALUE = f'''import os
import sys
directory = sys.argv[{PAPERS_DIRECTORY_ARGUMENT_INDEX}]
if os.path.isdir(directory):
    sys.exit({SUCCESS_STATUS})
sys.stderr.write("{DIAGNOSTIC_PREFIX}" + directory + "{LINE_DELIMITER}")
sys.exit({INVALID_INPUT_STATUS})
'''
