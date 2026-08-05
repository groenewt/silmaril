from config.constants.morphism.codebase.volume.table.tests.error.empty.value import VALUE as EMPTY
from config.constants.morphism.codebase.volume.table.tests.grammar.value import VALUE as GRAMMAR
from config.constants.morphism.codebase.volume.table.tests.header.value import VALUE as HEADER
from config.gate.external.python.morphism.codebase.volume.lexical.chomp.library import CHOMP
from config.gate.external.python.stdlib.re.library import DEPENDENCY as REGEX

# The observer's rg pattern stops at the declaring keyword; this grammar is the
# authority on what a test is and on where its name ends.  A quoted description
# (`test`/`it`/`describe`) is read as a source string literal -- `\\.` consumes an
# escaped delimiter so a description embedding its own quote is captured whole
# rather than truncated -- and the delimiter is back-referenced so single- and
# double-quoted forms are both admitted without the one leaking into the other.
# A Python declaration has no description, so its name is the `test_` identifier
# itself.  The keyword must be followed by whitespace or an opening parenthesis,
# which is what separates a declaration from an identifier that merely starts
# with the same letters.
PATTERN = REGEX.compile(GRAMMAR)
RELATIVE_PREFIX = "./"
PATH_GROUP = 1
NUMBER_GROUP = 2
DESCRIPTION_GROUP = 4
IDENTIFIER_GROUP = 5


def RENDER(lines: list) -> list:
    rows = set()
    for line in lines:
        if not line:
            continue
        match = PATTERN.match(CHOMP(line))
        if match is None:
            continue
        test_name = match.group(DESCRIPTION_GROUP)
        if test_name is None:
            test_name = match.group(IDENTIFIER_GROUP)
        if not test_name:
            continue
        relative_path = match.group(PATH_GROUP).removeprefix(RELATIVE_PREFIX)
        rows.add((relative_path, test_name, int(match.group(NUMBER_GROUP))))
    if not rows:
        raise ValueError(EMPTY)
    return [list(HEADER)] + [list(row) for row in sorted(rows)]
