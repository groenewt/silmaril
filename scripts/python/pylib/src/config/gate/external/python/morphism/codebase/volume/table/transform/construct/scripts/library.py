from config.constants.morphism.codebase.volume.table.scripts.error.empty.value import VALUE as EMPTY
from config.constants.morphism.codebase.volume.table.scripts.header.value import VALUE as HEADER
from config.gate.external.python.morphism.codebase.volume.lexical.chomp.library import CHOMP

# The observer runs `rg --files`, so this stream carries bare file paths -- no
# `path:line:` prefix and no match text -- and the whole line, minus the walk
# root that `rg .` stamps on every entry, IS the value.  A blank line carries no
# path, so it is not projected as one.
RELATIVE_PREFIX = "./"


def RENDER(lines: list) -> list:
    rows = set()
    for line in lines:
        relative_path = CHOMP(line).removeprefix(RELATIVE_PREFIX)
        if not relative_path:
            continue
        rows.add((relative_path,))
    if not rows:
        raise ValueError(EMPTY)
    return [list(HEADER)] + [list(row) for row in sorted(rows)]
