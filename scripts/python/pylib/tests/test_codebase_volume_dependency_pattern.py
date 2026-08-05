import re

from config.constants.morphism.codebase.volume.source.observation.classification.dependency.pattern.value import VALUE as DEPENDENCY_PATTERN


def test_dependency_pattern_preserves_source_boundary() -> None:
    pattern = re.compile(DEPENDENCY_PATTERN)

    assert pattern.search("alias Research.Render").group(1) == "Research.Render"
    assert pattern.search("#include <sys/io_uring.h>").group(2) == "sys/io_uring.h"
    assert pattern.search("module Research.Render") is None
