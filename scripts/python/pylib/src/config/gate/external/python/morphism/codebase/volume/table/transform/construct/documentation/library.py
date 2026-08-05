from config.constants.morphism.codebase.volume.table.documentation.closer.grammar.value import VALUE as CLOSER_GRAMMAR
from config.constants.morphism.codebase.volume.table.documentation.error.empty.value import VALUE as EMPTY
from config.constants.morphism.codebase.volume.table.documentation.grammar.value import VALUE as GRAMMAR
from config.constants.morphism.codebase.volume.table.documentation.header.value import VALUE as HEADER
from config.gate.external.python.morphism.codebase.volume.lexical.chomp.library import CHOMP
from config.gate.external.python.stdlib.re.library import DEPENDENCY as REGEX

# The observer's rg pattern surfaces the marker; this grammar is the authority
# on the title carried behind it.  Markdown states the title inline, LaTeX
# states it as the braced argument of a sectioning command, and reStructuredText
# states it as the label of an anchor -- three markers, one heading each.  An ATX
# heading may be closed by a run of `#`, which is decoration rather than title,
# so the closing run and any trailing blanks are removed; a marker left carrying
# no title names nothing and is not projected as a heading.
PATTERN = REGEX.compile(GRAMMAR)
CLOSER = REGEX.compile(CLOSER_GRAMMAR)
STRIPPED = ""
RELATIVE_PREFIX = "./"
PATH_GROUP = 1
NUMBER_GROUP = 2
TITLE_GROUP = 3
BRACED_GROUP = 4
LABEL_GROUP = 5


def RENDER(lines: list) -> list:
    rows = set()
    for line in lines:
        if not line:
            continue
        match = PATTERN.match(CHOMP(line))
        if match is None:
            continue
        heading = match.group(TITLE_GROUP)
        if heading is None:
            heading = match.group(BRACED_GROUP)
        else:
            heading = CLOSER.sub(STRIPPED, heading)
        if heading is None:
            heading = match.group(LABEL_GROUP)
        if not heading:
            continue
        relative_path = match.group(PATH_GROUP).removeprefix(RELATIVE_PREFIX)
        rows.add((relative_path, heading, int(match.group(NUMBER_GROUP))))
    if not rows:
        raise ValueError(EMPTY)
    return [list(HEADER)] + [list(row) for row in sorted(rows)]
