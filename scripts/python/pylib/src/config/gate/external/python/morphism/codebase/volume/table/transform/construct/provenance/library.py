from config.constants.morphism.codebase.volume.table.provenance.behaviour.grammar.value import VALUE as BEHAVIOUR_GRAMMAR
from config.constants.morphism.codebase.volume.table.provenance.delegate.grammar.value import VALUE as DELEGATE_GRAMMAR
from config.constants.morphism.codebase.volume.table.provenance.error.empty.value import VALUE as EMPTY
from config.constants.morphism.codebase.volume.table.provenance.error.predicate.unknown.value import VALUE as UNKNOWN
from config.constants.morphism.codebase.volume.table.provenance.header.value import VALUE as HEADER
from config.constants.morphism.codebase.volume.table.provenance.module.grammar.value import VALUE as MODULE_GRAMMAR
from config.constants.morphism.codebase.volume.table.provenance.predicate.alias.value import VALUE as ALIAS
from config.constants.morphism.codebase.volume.table.provenance.predicate.behaviour.value import VALUE as BEHAVIOUR
from config.constants.morphism.codebase.volume.table.provenance.predicate.delegate.value import VALUE as DELEGATE
from config.constants.morphism.codebase.volume.table.provenance.predicate.vocabulary.value import VALUE as VOCABULARY
from config.constants.morphism.codebase.volume.table.provenance.relation.grammar.value import VALUE as RELATION_GRAMMAR
from config.constants.morphism.codebase.volume.table.provenance.relation.multiple.grammar.value import VALUE as MULTIPLE_GRAMMAR
from config.constants.morphism.codebase.volume.table.provenance.relation.multiple.member.grammar.value import VALUE as MEMBER_GRAMMAR
from config.constants.morphism.codebase.volume.table.provenance.source.grammar.value import VALUE as SOURCE_GRAMMAR
from config.gate.external.python.morphism.codebase.volume.lexical.chomp.library import CHOMP
from config.gate.external.python.stdlib.re.library import DEPENDENCY as REGEX

# The observer's rg pattern is `^`, so this stream carries every line of every
# Elixir source in the tree.  A provenance row is a TRIPLE, and these grammars
# are the authority on which lines state one: the structural relations a module
# declares about other modules.  The vocabulary is closed -- `alias`, `use`,
# `import`, `require`, `behaviour` and `delegate` -- and every predicate emitted
# is held to it, so the grammar and the vocabulary cannot drift apart.
#
# The SUBJECT is the enclosing module: the most recent `defmodule` stated in the
# same file, which is what makes a nested declaration belong to the module that
# encloses it.  A relation stated before any `defmodule` -- `import Config` at
# the head of a config script -- has no module to be the subject of, so it is
# not projected as a triple.
#
# The OBJECT is the module named by the declaration and must be capitalised,
# which is what keeps the foreign `import` of a heredoc-quoted Haskell, Java or
# Python source out of an Elixir relation, and what keeps `@behaviour
# __MODULE__` -- a self-reference, naming nothing new -- out too.  A declaration
# must end at the object, at a comma opening its options, or at a comment, so
# `import Data.List (intercalate)`, whose parenthesised import list no Elixir
# declaration can carry, is not read as one.  `alias Base.{A, B}` states one
# relation per member, each qualified by the base, and `defdelegate f(x), to: B`
# states the delegation target behind its `to:` option.
#
# Excluded by construction, precision being preferred to recall: the multi-line
# form of `alias Base.{` , whose members a line-oriented reading cannot close;
# and a target built by metaprogramming (`to: target`, `__MODULE__.Urn`), which
# names no module until the macro is expanded.
SOURCE = REGEX.compile(SOURCE_GRAMMAR)
MODULE = REGEX.compile(MODULE_GRAMMAR)
RELATION = REGEX.compile(RELATION_GRAMMAR)
MULTIPLE = REGEX.compile(MULTIPLE_GRAMMAR)
MEMBER = REGEX.compile(MEMBER_GRAMMAR)
BEHAVIOUR_DECLARATION = REGEX.compile(BEHAVIOUR_GRAMMAR)
DELEGATE_DECLARATION = REGEX.compile(DELEGATE_GRAMMAR)
RELATIVE_PREFIX = "./"
MODULE_SEPARATOR = "."
MEMBER_SEPARATOR = ","
DETAIL_SEPARATOR = "="
PATH_GROUP = 1
NUMBER_GROUP = 2
TEXT_GROUP = 3
NAME_GROUP = 1
PREDICATE_GROUP = 1
OBJECT_GROUP = 2
BASE_GROUP = 1
MEMBERS_GROUP = 2


def RELATIONS(text: str) -> list:
    match = MULTIPLE.match(text)
    if match is not None:
        base = match.group(BASE_GROUP)
        relations = []
        for member in match.group(MEMBERS_GROUP).split(MEMBER_SEPARATOR):
            named = MEMBER.match(member.strip())
            if named is None:
                continue
            relations.append((ALIAS, base + MODULE_SEPARATOR + named.group(NAME_GROUP)))
        return relations
    match = RELATION.match(text)
    if match is not None:
        return [(match.group(PREDICATE_GROUP), match.group(OBJECT_GROUP))]
    match = BEHAVIOUR_DECLARATION.match(text)
    if match is not None:
        return [(BEHAVIOUR, match.group(NAME_GROUP))]
    match = DELEGATE_DECLARATION.match(text)
    if match is not None:
        return [(DELEGATE, match.group(NAME_GROUP))]
    return []


def RENDER(lines: list) -> list:
    rows = set()
    subjects = {}
    for line in lines:
        if not line:
            continue
        record = SOURCE.match(CHOMP(line))
        if record is None:
            continue
        source_path = record.group(PATH_GROUP).removeprefix(RELATIVE_PREFIX)
        text = record.group(TEXT_GROUP)
        declaration = MODULE.match(text)
        if declaration is not None:
            subjects[source_path] = declaration.group(NAME_GROUP)
        if source_path not in subjects:
            continue
        for predicate, target in RELATIONS(text):
            if predicate not in VOCABULARY:
                raise ValueError(UNKNOWN + DETAIL_SEPARATOR + predicate)
            rows.add(
                (
                    subjects[source_path],
                    predicate,
                    target,
                    source_path,
                    int(record.group(NUMBER_GROUP)),
                )
            )
    if not rows:
        raise ValueError(EMPTY)
    return [list(HEADER)] + [list(row) for row in sorted(rows)]
