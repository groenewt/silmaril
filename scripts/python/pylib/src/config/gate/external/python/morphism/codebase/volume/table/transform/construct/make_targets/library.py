from config.constants.morphism.codebase.volume.table.make_targets.assignment.operator.value import VALUE as ASSIGNMENTS
from config.constants.morphism.codebase.volume.table.make_targets.error.empty.value import VALUE as EMPTY
from config.constants.morphism.codebase.volume.table.make_targets.grammar.value import VALUE as GRAMMAR
from config.constants.morphism.codebase.volume.table.make_targets.header.value import VALUE as HEADER
from config.constants.morphism.codebase.volume.table.make_targets.pattern.wildcard.value import VALUE as WILDCARD
from config.gate.external.python.morphism.codebase.volume.lexical.chomp.library import CHOMP
from config.gate.external.python.stdlib.re.library import DEPENDENCY as REGEX

# The observer's globs already hold the walk to makefiles, but `name:` at column
# zero is also how Make opens a variable assignment -- `name:=value` and
# `name::=value` -- so this grammar splits the name off the first colon and lets
# the remainder decide: a rule is what a colon opens that is not an `=`.
# Double-colon rules (`name:: recipe`) ARE rules and are kept; pattern rules
# (`%.o: %.c`) are rule TEMPLATES rather than invocable targets, so a `%` in the
# name is dropped.  Special targets such as `.PHONY` never arrive here -- the
# grammar, like the observer, requires the name to open on an alphanumeric.
PATTERN = REGEX.compile(GRAMMAR)
RELATIVE_PREFIX = "./"
PATH_GROUP = 1
LINE_GROUP = 2
NAME_GROUP = 3
REMAINDER_GROUP = 4


def RENDER(lines: list) -> list:
    rows = set()
    for line in lines:
        if not line:
            continue
        match = PATTERN.match(CHOMP(line))
        if match is None:
            continue
        target_name = match.group(NAME_GROUP)
        if WILDCARD in target_name:
            continue
        if match.group(REMAINDER_GROUP).startswith(ASSIGNMENTS):
            continue
        source_path = match.group(PATH_GROUP).removeprefix(RELATIVE_PREFIX)
        rows.add((target_name, source_path, match.group(LINE_GROUP)))
    if not rows:
        raise ValueError(EMPTY)
    return [list(HEADER)] + [list(row) for row in sorted(rows)]
