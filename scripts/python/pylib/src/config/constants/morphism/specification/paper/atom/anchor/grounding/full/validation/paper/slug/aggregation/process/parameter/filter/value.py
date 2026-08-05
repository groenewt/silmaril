from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.cardinality.offending.path.limit.value import VALUE as OFFENDING_PATH_LIMIT
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.cardinality.one.value import VALUE as ONE_CARDINALITY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.cardinality.zero.value import VALUE as ZERO_CARDINALITY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.grounded.value import VALUE as GROUNDED_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.instance.label.value import VALUE as INSTANCE_LABEL_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.key.value import VALUE as KEY_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.missing.paths.value import VALUE as MISSING_PATHS_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.missing.value import VALUE as MISSING_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.paper.slug.value import VALUE as PAPER_SLUG_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.specification.path.value import VALUE as SPECIFICATION_PATH_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.schema.property.total.value import VALUE as TOTAL_PROPERTY
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.serialization.delimiter.path.label.value import VALUE as PATH_LABEL_DELIMITER

VALUE = f'''
reduce .[] as $row ({{}};
  .[$row["{PAPER_SLUG_PROPERTY}"]] = (
    (.[$row["{PAPER_SLUG_PROPERTY}"]] // {{"{TOTAL_PROPERTY}": {ZERO_CARDINALITY}, "{MISSING_PROPERTY}": {ZERO_CARDINALITY}, "{MISSING_PATHS_PROPERTY}": []}}) as $state
    | {{
        "{TOTAL_PROPERTY}": ($state["{TOTAL_PROPERTY}"] + {ONE_CARDINALITY}),
        "{MISSING_PROPERTY}": ($state["{MISSING_PROPERTY}"] + (if $row["{GROUNDED_PROPERTY}"] then {ZERO_CARDINALITY} else {ONE_CARDINALITY} end)),
        "{MISSING_PATHS_PROPERTY}": (
          if ($row["{GROUNDED_PROPERTY}"] | not) and (($state["{MISSING_PATHS_PROPERTY}"] | length) < {OFFENDING_PATH_LIMIT})
          then $state["{MISSING_PATHS_PROPERTY}"] + ["\\($row[\"{SPECIFICATION_PATH_PROPERTY}\"]){PATH_LABEL_DELIMITER}\\($row[\"{INSTANCE_LABEL_PROPERTY}\"])"]
          else $state["{MISSING_PATHS_PROPERTY}"]
          end
        )
      }}
  )
)
| to_entries
| sort_by(.["{KEY_PROPERTY}"])
| from_entries
'''
