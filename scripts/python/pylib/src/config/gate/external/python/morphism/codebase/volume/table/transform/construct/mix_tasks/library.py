from config.constants.morphism.codebase.volume.table.mix_tasks.error.empty.value import VALUE as EMPTY
from config.constants.morphism.codebase.volume.table.mix_tasks.grammar.value import VALUE as GRAMMAR
from config.constants.morphism.codebase.volume.table.mix_tasks.header.value import VALUE as HEADER
from config.constants.morphism.codebase.volume.table.mix_tasks.task.namespace.value import VALUE as NAMESPACE
from config.constants.morphism.codebase.volume.table.mix_tasks.task.segment.separator.value import VALUE as SEGMENT_SEPARATOR
from config.constants.morphism.codebase.volume.table.mix_tasks.task.word.separator.value import VALUE as WORD_SEPARATOR
from config.gate.external.python.morphism.codebase.volume.lexical.chomp.library import CHOMP
from config.gate.external.python.stdlib.re.library import DEPENDENCY as REGEX

# The observer's rg pattern finds `defmodule Mix.Tasks.` anywhere on a line, so
# prose and markdown that merely quote a task module are matched too.  This
# grammar is the authority on what a declaration is: the line content must OPEN
# with the `defmodule` keyword, and the alias that follows must be a well-formed
# module whose every segment starts with a capital.
PATTERN = REGEX.compile(GRAMMAR)
RELATIVE_PREFIX = "./"
PATH_GROUP = 1
MODULE_GROUP = 3
STEP = 1
NOTHING = ""
WORD_OPENERS = (SEGMENT_SEPARATOR, WORD_SEPARATOR)


def UNDERSCORE(segment: str) -> str:
    # Port of Elixir's `Macro.underscore/1` narrowed to one dot-free alias
    # segment.  A capital opens a new word when the character after it is not a
    # capital (`HTTPServer` -> `http_server`, `A1B2` -> `a1_b2`) or when the
    # character before it was itself neither a capital nor a separator
    # (`Foo2Bar` -> `foo2_bar`); a run of capitals therefore stays one word
    # (`Gate24` -> `gate24`, `B0` -> `b0`).  The original's hyphen and dot
    # clauses are unreachable here -- the grammar admits only `[A-Za-z0-9_]`
    # inside a segment.
    tail = segment[STEP:]
    characters = []
    previous = NOTHING
    for index, current in enumerate(segment):
        following = tail[index:index + STEP]
        opens_word = current.isupper() and (
            (following and not following.isupper() and following not in WORD_OPENERS)
            or (not previous.isupper() and previous != WORD_SEPARATOR)
        )
        if previous and opens_word:
            characters.append(WORD_SEPARATOR)
        characters.append(current.lower())
        previous = current
    return NOTHING.join(characters)


def TASK_NAME(module: str) -> str:
    # `mix foo.bar` is `Mix.Tasks.Foo.Bar`: drop the namespace, underscore every
    # remaining alias segment on its own, and rejoin on the dot.  So
    # `Mix.Tasks.Research.MasterProduce` is `research.master_produce` while
    # `Mix.Tasks.Research.Master.Produce` is `research.master.produce`.
    return SEGMENT_SEPARATOR.join(
        UNDERSCORE(segment)
        for segment in module.removeprefix(NAMESPACE).split(SEGMENT_SEPARATOR)
    )


def RENDER(lines: list) -> list:
    rows = set()
    for line in lines:
        if not line:
            continue
        match = PATTERN.match(CHOMP(line))
        if match is None:
            continue
        module_name = match.group(MODULE_GROUP)
        source_path = match.group(PATH_GROUP).removeprefix(RELATIVE_PREFIX)
        rows.add((TASK_NAME(module_name), module_name, source_path))
    if not rows:
        raise ValueError(EMPTY)
    return [list(HEADER)] + [list(row) for row in sorted(rows)]
