from config.constants.morphism.codebase.volume.table.modules.declaration.elixir.extension.value import VALUE as ELIXIR_EXTENSIONS
from config.constants.morphism.codebase.volume.table.modules.declaration.elixir.keyword.value import VALUE as ELIXIR_KEYWORDS
from config.constants.morphism.codebase.volume.table.modules.error.empty.value import VALUE as EMPTY
from config.constants.morphism.codebase.volume.table.modules.grammar.value import VALUE as GRAMMAR
from config.constants.morphism.codebase.volume.table.modules.header.value import VALUE as HEADER
from config.gate.external.python.morphism.codebase.volume.lexical.chomp.library import CHOMP
from config.gate.external.python.stdlib.re.library import DEPENDENCY as REGEX

# The observer's rg pattern is prose-permissive: `^\s*module\s+` also matches
# English sentences.  This grammar is the authority on what a declaration is --
# a keyword followed by an identifier -- and Elixir sources are further held to
# `defmodule`, the only module-declaring form in that language, so prose such as
# "module owns ..." in a .ex file is not projected as a module.
PATTERN = REGEX.compile(GRAMMAR)
RELATIVE_PREFIX = "./"
PATH_GROUP = 1
KEYWORD_GROUP = 3
NAME_GROUP = 4


def RENDER(lines: list) -> list:
    rows = set()
    for line in lines:
        if not line:
            continue
        match = PATTERN.match(CHOMP(line))
        if match is None:
            continue
        source_path = match.group(PATH_GROUP).removeprefix(RELATIVE_PREFIX)
        if source_path.endswith(ELIXIR_EXTENSIONS) and match.group(KEYWORD_GROUP) not in ELIXIR_KEYWORDS:
            continue
        rows.add((match.group(NAME_GROUP), source_path))
    if not rows:
        raise ValueError(EMPTY)
    return [list(HEADER)] + [list(row) for row in sorted(rows)]
