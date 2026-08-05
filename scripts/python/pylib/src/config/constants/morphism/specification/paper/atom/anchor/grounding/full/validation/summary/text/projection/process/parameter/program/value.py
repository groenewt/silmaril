from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.cardinality.zero.value import VALUE as ZERO_CARDINALITY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.percentage.scale.value import VALUE as PERCENTAGE_SCALE
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.coverage.percentage.value import VALUE as COVERAGE_PERCENTAGE_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.missing.paths.value import VALUE as MISSING_PATHS_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.missing.value import VALUE as MISSING_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.per.slug.value import VALUE as PER_SLUG_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.total.instances.value import VALUE as TOTAL_INSTANCES_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.total.missing.value import VALUE as TOTAL_MISSING_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.total.value import VALUE as TOTAL_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.serialization.delimiter.line.value import VALUE as LINE_DELIMITER
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.summary.text.format.coverage.percentage.value import VALUE as COVERAGE_PERCENTAGE_FORMAT
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.summary.text.format.header.value import VALUE as HEADER_FORMAT
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.summary.text.format.offending.path.value import VALUE as OFFENDING_PATH_FORMAT
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.summary.text.format.row.value import VALUE as ROW_FORMAT
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.summary.text.format.slug.heading.value import VALUE as SLUG_HEADING_FORMAT
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.summary.text.format.total.instances.value import VALUE as TOTAL_INSTANCES_FORMAT
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.summary.text.format.total.missing.value import VALUE as TOTAL_MISSING_FORMAT
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.summary.text.label.missing.value import VALUE as MISSING_LABEL
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.summary.text.label.percentage.value import VALUE as PERCENTAGE_LABEL
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.summary.text.label.slug.value import VALUE as SLUG_LABEL
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.summary.text.label.total.value import VALUE as TOTAL_LABEL
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.summary.text.offending.heading.value import VALUE as OFFENDING_HEADING

VALUE = f'''import json
import sys

summary = json.loads(sys.stdin.read())
sys.stdout.write("{TOTAL_INSTANCES_FORMAT}" % summary["{TOTAL_INSTANCES_PROPERTY}"])
sys.stdout.write("{TOTAL_MISSING_FORMAT}" % summary["{TOTAL_MISSING_PROPERTY}"])
sys.stdout.write("{COVERAGE_PERCENTAGE_FORMAT}" % summary["{COVERAGE_PERCENTAGE_PROPERTY}"])
sys.stdout.write("{LINE_DELIMITER}")
sys.stdout.write("{HEADER_FORMAT}" % ("{SLUG_LABEL}", "{TOTAL_LABEL}", "{MISSING_LABEL}", "{PERCENTAGE_LABEL}"))
for slug, entry in summary["{PER_SLUG_PROPERTY}"].items():
    total = entry["{TOTAL_PROPERTY}"]
    missing = entry["{MISSING_PROPERTY}"]
    percentage = float({ZERO_CARDINALITY}) if total == {ZERO_CARDINALITY} else (total - missing) * {PERCENTAGE_SCALE} / total
    sys.stdout.write("{ROW_FORMAT}" % (slug, total, missing, percentage))
if summary["{TOTAL_MISSING_PROPERTY}"] > {ZERO_CARDINALITY}:
    sys.stdout.write("{LINE_DELIMITER}")
    sys.stdout.write("{OFFENDING_HEADING}" + "{LINE_DELIMITER}")
    for slug, entry in summary["{PER_SLUG_PROPERTY}"].items():
        if entry["{MISSING_PROPERTY}"] > {ZERO_CARDINALITY}:
            sys.stdout.write("{SLUG_HEADING_FORMAT}" % slug + "{LINE_DELIMITER}")
            for path in entry["{MISSING_PATHS_PROPERTY}"]:
                sys.stdout.write("{OFFENDING_PATH_FORMAT}" % path + "{LINE_DELIMITER}")
'''
