from config.constants.morphism.codebase.volume.table.public_apis.arity.nullary.value import VALUE as NULLARY
from config.constants.morphism.codebase.volume.table.public_apis.delimiter.close.value import VALUE as CLOSE
from config.constants.morphism.codebase.volume.table.public_apis.delimiter.open.value import VALUE as OPEN
from config.constants.morphism.codebase.volume.table.public_apis.delimiter.parameter.open.value import VALUE as PARAMETER_OPEN
from config.constants.morphism.codebase.volume.table.public_apis.delimiter.parameter.separator.value import VALUE as SEPARATOR
from config.constants.morphism.codebase.volume.table.public_apis.error.empty.value import VALUE as EMPTY
from config.constants.morphism.codebase.volume.table.public_apis.error.unclosed.value import VALUE as UNCLOSED
from config.constants.morphism.codebase.volume.table.public_apis.grammar.module.value import VALUE as MODULE_GRAMMAR
from config.constants.morphism.codebase.volume.table.public_apis.grammar.public.value import VALUE as PUBLIC_GRAMMAR
from config.constants.morphism.codebase.volume.table.public_apis.grammar.record.value import VALUE as RECORD_GRAMMAR
from config.constants.morphism.codebase.volume.table.public_apis.header.value import VALUE as HEADER
from config.gate.external.python.morphism.codebase.volume.lexical.chomp.library import CHOMP
from config.gate.external.python.stdlib.re.library import DEPENDENCY as REGEX

# The observer emits every line of every .ex/.exs file, so the grammars below --
# not the observer -- decide what a public API is.  `def[^\S\r\n]+` cannot match
# `defp`, `defmacro` or `defmodule`, so private functions are excluded by
# construction rather than by a subtractive filter.
RECORD_PATTERN = REGEX.compile(RECORD_GRAMMAR)
MODULE_PATTERN = REGEX.compile(MODULE_GRAMMAR)
PUBLIC_PATTERN = REGEX.compile(PUBLIC_GRAMMAR)
RELATIVE_PREFIX = "./"
JOIN = " "
PATH_GROUP = 1
LINE_GROUP = 2
BODY_GROUP = 3
MODULE_NAME_GROUP = 1
API_NAME_GROUP = 1
PARAMETER_GROUP = 2
NEXT = 1
UNBALANCED = None


def SCAN(text: str):
    # Count only top-level commas and stop at the paren closing the parameter
    # list, so nested tuples/maps/lists, default arguments (`\\`) and trailing
    # `when` guards never inflate the arity.  Returns None while the parameter
    # list is still open, i.e. the declaration spans further lines.
    depth = 0
    separators = 0
    occupied = False
    for character in text:
        if character in OPEN:
            depth += 1
        elif character in CLOSE:
            depth -= 1
            if depth == 0:
                return separators + NEXT if occupied else NULLARY
        elif depth == 1 and character == SEPARATOR:
            separators += 1
            occupied = True
        elif not character.isspace():
            occupied = True
    return UNBALANCED


def ARITY(records: list, index: int, source_path: str, parameters: str) -> int:
    if not parameters.startswith(PARAMETER_OPEN):
        return NULLARY
    text = parameters
    cursor = index
    while True:
        arity = SCAN(text)
        if arity is not UNBALANCED:
            return arity
        # The observer sorts by path, so the remainder of a multi-line parameter
        # list is the next record of the same file.
        cursor += NEXT
        if cursor >= len(records):
            raise ValueError(UNCLOSED)
        path, _line, body = records[cursor]
        if path != source_path:
            raise ValueError(UNCLOSED)
        text = text + JOIN + body.strip()


def PARSE(lines: list) -> list:
    records = []
    for line in lines:
        if not line:
            continue
        match = RECORD_PATTERN.match(CHOMP(line))
        if match is None:
            continue
        records.append(
            (
                match.group(PATH_GROUP).removeprefix(RELATIVE_PREFIX),
                int(match.group(LINE_GROUP)),
                match.group(BODY_GROUP),
            )
        )
    return records


def RENDER(lines: list) -> list:
    records = PARSE(lines)
    rows = set()
    owner = None
    module = None
    for index, (source_path, source_line, body) in enumerate(records):
        declaration = MODULE_PATTERN.match(body)
        if declaration is not None:
            owner, module = source_path, declaration.group(MODULE_NAME_GROUP)
            continue
        definition = PUBLIC_PATTERN.match(body)
        if definition is None:
            continue
        # A `def` reached before its own file declared a module has no owner to
        # attribute the API to, so it is not projected.
        if module is None or owner != source_path:
            continue
        rows.add(
            (
                module,
                definition.group(API_NAME_GROUP),
                ARITY(records, index, source_path, definition.group(PARAMETER_GROUP)),
                source_path,
                source_line,
            )
        )
    if not rows:
        raise ValueError(EMPTY)
    return [list(HEADER)] + [list(row) for row in sorted(rows)]
