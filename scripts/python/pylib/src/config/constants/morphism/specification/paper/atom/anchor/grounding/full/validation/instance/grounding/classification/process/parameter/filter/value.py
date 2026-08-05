from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.cardinality.zero.value import VALUE as ZERO_CARDINALITY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.external.evidence.property.common.core.ontology.grounding.internationalized.resource.identifier.value import VALUE as COMMON_CORE_ONTOLOGY_GROUNDING_IDENTIFIER_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.external.evidence.property.common.process.ontology.process.internationalized.resource.identifier.value import VALUE as COMMON_PROCESS_ONTOLOGY_PROCESS_IDENTIFIER_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.predicate.nonempty.whitespace.pattern.value import VALUE as WHITESPACE_PATTERN
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.fields.value import VALUE as FIELDS_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.grounded.value import VALUE as GROUNDED_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.serialization.text.empty.value import VALUE as EMPTY_TEXT
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.type.name.array.value import VALUE as ARRAY_TYPE
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.type.name.object.value import VALUE as OBJECT_TYPE
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.type.name.string.value import VALUE as STRING_TYPE

VALUE = f'''
def nonempty_grounding:
  type == "{STRING_TYPE}" and ((gsub("{WHITESPACE_PATTERN}"; "{EMPTY_TEXT}")) | length > {ZERO_CARDINALITY});
def has_grounding:
  ((.["{COMMON_CORE_ONTOLOGY_GROUNDING_IDENTIFIER_PROPERTY}"]? // null) | nonempty_grounding)
  or ((.["{COMMON_PROCESS_ONTOLOGY_PROCESS_IDENTIFIER_PROPERTY}"]? // null) | nonempty_grounding);
def grounded_fields:
  if type == "{OBJECT_TYPE}" then has_grounding
  elif type == "{ARRAY_TYPE}" then
    length > {ZERO_CARDINALITY} and all(.[]; type == "{OBJECT_TYPE}" and has_grounding)
  else false
  end;
. + {{"{GROUNDED_PROPERTY}": (.["{FIELDS_PROPERTY}"] | grounded_fields)}}
'''
