from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.cardinality.zero.value import VALUE as ZERO_CARDINALITY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.diagnostic.json.parse.error.prefix.value import VALUE as JSON_PARSE_ERROR_PREFIX
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.percentage.precision.value import VALUE as PERCENTAGE_PRECISION
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.percentage.scale.value import VALUE as PERCENTAGE_SCALE
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.coverage.percentage.value import VALUE as COVERAGE_PERCENTAGE_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.missing.value import VALUE as MISSING_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.papers.directory.value import VALUE as PAPERS_DIRECTORY_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.per.slug.value import VALUE as PER_SLUG_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.total.instances.value import VALUE as TOTAL_INSTANCES_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.total.missing.value import VALUE as TOTAL_MISSING_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.total.value import VALUE as TOTAL_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.serialization.delimiter.line.value import VALUE as LINE_DELIMITER
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.status.invalid.input.value import VALUE as INVALID_INPUT_STATUS
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.summary.json.construction.process.parameter.argument.index.papers.directory.value import VALUE as PAPERS_DIRECTORY_ARGUMENT_INDEX

VALUE = f'''import json
import sys

papers_directory = sys.argv[{PAPERS_DIRECTORY_ARGUMENT_INDEX}]
try:
    per_slug = json.loads(sys.stdin.read())
except json.JSONDecodeError as error:
    sys.stderr.write("{JSON_PARSE_ERROR_PREFIX}" + str(error) + "{LINE_DELIMITER}")
    sys.exit({INVALID_INPUT_STATUS})
total_instances = sum(entry["{TOTAL_PROPERTY}"] for entry in per_slug.values())
total_missing = sum(entry["{MISSING_PROPERTY}"] for entry in per_slug.values())
coverage = {ZERO_CARDINALITY} if total_instances == {ZERO_CARDINALITY} else round((total_instances - total_missing) * {PERCENTAGE_SCALE} / total_instances, {PERCENTAGE_PRECISION})
summary = {{
    "{PAPERS_DIRECTORY_PROPERTY}": papers_directory,
    "{TOTAL_INSTANCES_PROPERTY}": total_instances,
    "{TOTAL_MISSING_PROPERTY}": total_missing,
    "{COVERAGE_PERCENTAGE_PROPERTY}": coverage,
    "{PER_SLUG_PROPERTY}": per_slug,
}}
sys.stdout.write(json.dumps(summary))
sys.stdout.write("{LINE_DELIMITER}")
'''
