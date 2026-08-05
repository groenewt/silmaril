import re

from config.constants.morphism.codebase.volume.source.observation.classification.relation.pattern.value import VALUE as RELATION_PATTERN


def test_relation_pattern_preserves_source_boundary() -> None:
    pattern = re.compile(RELATION_PATTERN)

    assert pattern.search(r"\input{src/shared/preamble}").group(3) == "src/shared/preamble"
    assert pattern.search("ordinary prose without a relation") is None
