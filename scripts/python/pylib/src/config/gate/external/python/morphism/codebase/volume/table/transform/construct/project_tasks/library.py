from config.constants.morphism.codebase.volume.table.make_targets.assignment.operator.value import VALUE as ASSIGNMENTS
from config.constants.morphism.codebase.volume.table.make_targets.grammar.value import VALUE as MAKE_GRAMMAR
from config.constants.morphism.codebase.volume.table.make_targets.pattern.wildcard.value import VALUE as WILDCARD
from config.constants.morphism.codebase.volume.table.mix_tasks.grammar.value import VALUE as MIX_GRAMMAR
from config.constants.morphism.codebase.volume.table.project_tasks.error.empty.value import VALUE as EMPTY
from config.constants.morphism.codebase.volume.table.project_tasks.header.value import VALUE as HEADER
from config.constants.morphism.codebase.volume.table.project_tasks.makefile.name.value import VALUE as MAKEFILE_NAME
from config.constants.morphism.codebase.volume.table.project_tasks.makefile.prefix.value import VALUE as MAKEFILE_PREFIX
from config.constants.morphism.codebase.volume.table.project_tasks.makefile.suffix.value import VALUE as MAKEFILE_SUFFIXES
from config.constants.morphism.codebase.volume.table.project_tasks.path.separator.value import VALUE as PATH_SEPARATOR
from config.gate.external.python.morphism.codebase.volume.lexical.chomp.library import CHOMP
from config.gate.external.python.morphism.codebase.volume.table.transform.construct.mix_tasks.library import TASK_NAME
from config.gate.external.python.stdlib.re.library import DEPENDENCY as REGEX

# A project task is declared in one of two dialects, so this table is the union
# of the two grammars that already name them: the Mix task module, and the Make
# rule.  The observer's second alternative -- `name:` at column zero -- is not a
# Make grammar at all, it is the shape of an English sentence, a YAML key and a
# JSON key, which is why the raw runs to a quarter of a million lines.  Only a
# file that IS a makefile can declare a Make target, so the Make half is held to
# `Makefile`, `Makefile.*` and `*.mk`; everything else the alternative dragged in
# is not a declaration and is dropped.  Within a makefile the make_targets rules
# apply unchanged: variable assignments are not targets, `%` pattern rules are
# templates rather than invocable tasks, and `.PHONY` cannot arrive because the
# name must open on an alphanumeric.
MIX_PATTERN = REGEX.compile(MIX_GRAMMAR)
MAKE_PATTERN = REGEX.compile(MAKE_GRAMMAR)
RELATIVE_PREFIX = "./"
BASENAME = -1
MIX_PATH_GROUP = 1
MIX_MODULE_GROUP = 3
MAKE_PATH_GROUP = 1
MAKE_NAME_GROUP = 3
MAKE_REMAINDER_GROUP = 4


def MAKEFILE(path: str) -> bool:
    basename = path.rpartition(PATH_SEPARATOR)[BASENAME]
    return basename == MAKEFILE_NAME or basename.startswith(MAKEFILE_PREFIX) or basename.endswith(MAKEFILE_SUFFIXES)


def RENDER(lines: list) -> list:
    rows = set()
    for line in lines:
        if not line:
            continue
        content = CHOMP(line)
        declaration = MIX_PATTERN.match(content)
        if declaration is not None:
            rows.add((TASK_NAME(declaration.group(MIX_MODULE_GROUP)), declaration.group(MIX_PATH_GROUP).removeprefix(RELATIVE_PREFIX)))
            continue
        rule = MAKE_PATTERN.match(content)
        if rule is None:
            continue
        declaration_path = rule.group(MAKE_PATH_GROUP).removeprefix(RELATIVE_PREFIX)
        if not MAKEFILE(declaration_path):
            continue
        target_name = rule.group(MAKE_NAME_GROUP)
        if WILDCARD in target_name:
            continue
        if rule.group(MAKE_REMAINDER_GROUP).startswith(ASSIGNMENTS):
            continue
        rows.add((target_name, declaration_path))
    if not rows:
        raise ValueError(EMPTY)
    return [list(HEADER)] + [list(row) for row in sorted(rows)]
