from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.diagnostic.yaml.parse.error.prefix.value import VALUE as YAML_PARSE_ERROR_PREFIX
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.instance.label.collection.prefix.value import VALUE as COLLECTION_LABEL_PREFIX
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.instance.label.collection.suffix.value import VALUE as COLLECTION_LABEL_SUFFIX
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.instance.label.entity.value import VALUE as ENTITY_LABEL
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.path.paper.slug.segment.index.value import VALUE as PAPER_SLUG_SEGMENT_INDEX
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.entity.value import VALUE as ENTITY_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.fields.value import VALUE as FIELDS_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.instance.label.value import VALUE as INSTANCE_LABEL_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.instances.value import VALUE as INSTANCES_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.paper.slug.value import VALUE as PAPER_SLUG_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.specification.path.value import VALUE as SPECIFICATION_PATH_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.serialization.delimiter.line.value import VALUE as LINE_DELIMITER
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.serialization.delimiter.record.null.value import VALUE as RECORD_DELIMITER
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.specification.document.instance.relation.parsing.process.parameter.argument.index.papers.directory.value import VALUE as PAPERS_DIRECTORY_ARGUMENT_INDEX
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.status.invalid.input.value import VALUE as INVALID_INPUT_STATUS

VALUE = f'''import json
import os
import sys
import yaml

root = sys.argv[{PAPERS_DIRECTORY_ARGUMENT_INDEX}]
prefix = root if root.endswith(os.sep) else root + os.sep
records = []
for path in sys.stdin.read().split("{RECORD_DELIMITER}"):
    if not path:
        continue
    try:
        with open(path) as handle:
            document = yaml.safe_load(handle)
    except yaml.YAMLError as error:
        sys.stderr.write("{YAML_PARSE_ERROR_PREFIX}" + path + ": " + str(error) + "{LINE_DELIMITER}")
        sys.exit({INVALID_INPUT_STATUS})
    if isinstance(document, dict) and isinstance(document.get("{ENTITY_PROPERTY}"), dict):
        instances = [(document["{ENTITY_PROPERTY}"], "{ENTITY_LABEL}")]
    elif isinstance(document, dict) and isinstance(document.get("{INSTANCES_PROPERTY}"), list):
        instances = [(instance, "{COLLECTION_LABEL_PREFIX}" + str(index) + "{COLLECTION_LABEL_SUFFIX}") for index, instance in enumerate(document["{INSTANCES_PROPERTY}"]) if isinstance(instance, dict)]
    else:
        instances = []
    relative = path[len(prefix):] if path.startswith(prefix) else path
    slug = relative.split(os.sep)[{PAPER_SLUG_SEGMENT_INDEX}]
    for instance, label in instances:
        records.append({{"{SPECIFICATION_PATH_PROPERTY}": path, "{PAPER_SLUG_PROPERTY}": slug, "{INSTANCE_LABEL_PROPERTY}": label, "{FIELDS_PROPERTY}": instance.get("{FIELDS_PROPERTY}")}})
sys.stdout.write("{LINE_DELIMITER}".join(json.dumps(record) for record in records))
if records:
    sys.stdout.write("{LINE_DELIMITER}")
'''
