from config.constants.morphism.codebase.volume.table.dependencies.ecosystem.name.c.value import VALUE as C
from config.constants.morphism.codebase.volume.table.dependencies.ecosystem.name.cpp.value import VALUE as CPP
from config.constants.morphism.codebase.volume.table.dependencies.ecosystem.name.elixir.value import VALUE as ELIXIR
from config.constants.morphism.codebase.volume.table.dependencies.ecosystem.name.haskell.value import VALUE as HASKELL
from config.constants.morphism.codebase.volume.table.dependencies.ecosystem.name.javascript.value import VALUE as JAVASCRIPT
from config.constants.morphism.codebase.volume.table.dependencies.ecosystem.name.python.value import VALUE as PYTHON
from config.constants.morphism.codebase.volume.table.dependencies.ecosystem.name.rust.value import VALUE as RUST
from config.constants.morphism.codebase.volume.table.dependencies.ecosystem.name.scala.value import VALUE as SCALA
from config.constants.morphism.codebase.volume.table.dependencies.ecosystem.value import VALUE as ECOSYSTEM
from config.constants.morphism.codebase.volume.table.dependencies.error.empty.value import VALUE as EMPTY
from config.constants.morphism.codebase.volume.table.dependencies.grammar.elixir.member.value import VALUE as ELIXIR_MEMBER_GRAMMAR
from config.constants.morphism.codebase.volume.table.dependencies.grammar.elixir.root.value import VALUE as ELIXIR_ROOT_GRAMMAR
from config.constants.morphism.codebase.volume.table.dependencies.grammar.haskell.root.value import VALUE as HASKELL_ROOT_GRAMMAR
from config.constants.morphism.codebase.volume.table.dependencies.grammar.include.keyword.value import VALUE as INCLUDE_GRAMMAR
from config.constants.morphism.codebase.volume.table.dependencies.grammar.include.target.value import VALUE as INCLUDE_TARGET_GRAMMAR
from config.constants.morphism.codebase.volume.table.dependencies.grammar.javascript.specifier.value import VALUE as JAVASCRIPT_GRAMMAR
from config.constants.morphism.codebase.volume.table.dependencies.grammar.keyword.value import VALUE as KEYWORD_GRAMMAR
from config.constants.morphism.codebase.volume.table.dependencies.grammar.python.member.value import VALUE as PYTHON_MEMBER_GRAMMAR
from config.constants.morphism.codebase.volume.table.dependencies.grammar.record.value import VALUE as RECORD_GRAMMAR
from config.constants.morphism.codebase.volume.table.dependencies.grammar.rust.member.value import VALUE as RUST_MEMBER_GRAMMAR
from config.constants.morphism.codebase.volume.table.dependencies.grammar.rust.root.value import VALUE as RUST_ROOT_GRAMMAR
from config.constants.morphism.codebase.volume.table.dependencies.grammar.scala.member.value import VALUE as SCALA_MEMBER_GRAMMAR
from config.constants.morphism.codebase.volume.table.dependencies.grammar.scala.root.value import VALUE as SCALA_ROOT_GRAMMAR
from config.constants.morphism.codebase.volume.table.dependencies.group.close.value import VALUE as GROUP_CLOSE
from config.constants.morphism.codebase.volume.table.dependencies.group.open.value import VALUE as GROUP_OPEN
from config.constants.morphism.codebase.volume.table.dependencies.group.prefix.elixir.value import VALUE as ELIXIR_PREFIX
from config.constants.morphism.codebase.volume.table.dependencies.group.prefix.rust.value import VALUE as RUST_PREFIX
from config.constants.morphism.codebase.volume.table.dependencies.group.prefix.scala.value import VALUE as SCALA_PREFIX
from config.constants.morphism.codebase.volume.table.dependencies.group.separator.value import VALUE as GROUP_SEPARATOR
from config.constants.morphism.codebase.volume.table.dependencies.header.value import VALUE as HEADER
from config.gate.external.python.morphism.codebase.volume.lexical.chomp.library import CHOMP
from config.gate.external.python.stdlib.re.library import DEPENDENCY as REGEX

# The observer's rg pattern is prose-permissive and language-blind: it matches
# English ("use the following"), Elixir variables named `import`, and Scala's
# `require(...)` precondition function.  Two gates narrow it.  First, the
# keyword must be followed by whitespace, which drops `require(`, `import:` and
# `import = ...`.  Second, the (extension, keyword) pair must appear in the
# ECOSYSTEM vocabulary, which is what excludes prose-bearing .md/.txt/.yaml and
# language-ambiguous .sh heredocs.  The surviving line is then read with the
# dependency grammar of its own language.
RECORD_PATTERN = REGEX.compile(RECORD_GRAMMAR)
KEYWORD_PATTERN = REGEX.compile(KEYWORD_GRAMMAR)
INCLUDE_PATTERN = REGEX.compile(INCLUDE_GRAMMAR)
ELIXIR_ROOT_PATTERN = REGEX.compile(ELIXIR_ROOT_GRAMMAR)
ELIXIR_MEMBER_PATTERN = REGEX.compile(ELIXIR_MEMBER_GRAMMAR)
SCALA_ROOT_PATTERN = REGEX.compile(SCALA_ROOT_GRAMMAR)
SCALA_MEMBER_PATTERN = REGEX.compile(SCALA_MEMBER_GRAMMAR)
RUST_ROOT_PATTERN = REGEX.compile(RUST_ROOT_GRAMMAR)
RUST_MEMBER_PATTERN = REGEX.compile(RUST_MEMBER_GRAMMAR)
PYTHON_MEMBER_PATTERN = REGEX.compile(PYTHON_MEMBER_GRAMMAR)
HASKELL_ROOT_PATTERN = REGEX.compile(HASKELL_ROOT_GRAMMAR)
JAVASCRIPT_PATTERN = REGEX.compile(JAVASCRIPT_GRAMMAR)
INCLUDE_TARGET_PATTERN = REGEX.compile(INCLUDE_TARGET_GRAMMAR)
RELATIVE_PREFIX = "./"
PATH_SEPARATOR = "/"
EXTENSION_SEPARATOR = "."
NO_EXTENSION = ""
PATH_GROUP = 1
LINE_GROUP = 2
BODY_GROUP = 3
KEYWORD_GROUP = 1
DECLARATION_GROUP = 2
NAME_GROUP = 1
LAST = -1
NONE = []


def EXTENSION(source_path: str) -> str:
    base = source_path.rsplit(PATH_SEPARATOR, 1)[LAST]
    if EXTENSION_SEPARATOR not in base:
        return NO_EXTENSION
    return EXTENSION_SEPARATOR + base.rsplit(EXTENSION_SEPARATOR, 1)[LAST]


def GROUP(declaration: str, root: str, prefix: str, member: object) -> list:
    # `alias Foo.{Bar, Baz}` / `import java.util.{X, Y}` / `use std::ffi::{A, B}`
    # each name several dependencies at once.  The observer captured only lines
    # matching its keyword pattern, so a group left open at end of line has its
    # members on lines that are absent from this input and is not projectable.
    tail = declaration[len(root) :]
    if not tail.startswith(prefix + GROUP_OPEN):
        return [root]
    inner = tail[len(prefix) + len(GROUP_OPEN) :]
    if GROUP_CLOSE not in inner:
        return NONE
    names = []
    for candidate in inner.split(GROUP_CLOSE)[0].split(GROUP_SEPARATOR):
        match = member.match(candidate.strip())
        if match is not None:
            names.append(root + prefix + match.group(NAME_GROUP))
    return names


def ROOTED(declaration: str, root_pattern: object, prefix: str, member_pattern: object) -> list:
    match = root_pattern.match(declaration)
    if match is None:
        return NONE
    return GROUP(declaration, match.group(NAME_GROUP), prefix, member_pattern)


def ELIXIR_NAMES(declaration: str) -> list:
    return ROOTED(declaration, ELIXIR_ROOT_PATTERN, ELIXIR_PREFIX, ELIXIR_MEMBER_PATTERN)


def SCALA_NAMES(declaration: str) -> list:
    return ROOTED(declaration, SCALA_ROOT_PATTERN, SCALA_PREFIX, SCALA_MEMBER_PATTERN)


def RUST_NAMES(declaration: str) -> list:
    return ROOTED(declaration, RUST_ROOT_PATTERN, RUST_PREFIX, RUST_MEMBER_PATTERN)


def SINGLE(declaration: str, pattern: object) -> list:
    match = pattern.match(declaration)
    if match is None:
        return NONE
    return [match.group(NAME_GROUP)]


def HASKELL_NAMES(declaration: str) -> list:
    return SINGLE(declaration, HASKELL_ROOT_PATTERN)


def INCLUDE_NAMES(declaration: str) -> list:
    return SINGLE(declaration, INCLUDE_TARGET_PATTERN)


def PYTHON_NAMES(declaration: str) -> list:
    # `import os, sys` and `import pyarrow.parquet as pq` are both plain lists of
    # module paths; the `as` binding is a local name, not a dependency.
    names = []
    for candidate in declaration.split(GROUP_SEPARATOR):
        match = PYTHON_MEMBER_PATTERN.match(candidate.strip())
        if match is not None:
            names.append(match.group(NAME_GROUP))
    return names


def JAVASCRIPT_NAMES(declaration: str) -> list:
    # The dependency is the module specifier, never the imported bindings.
    match = JAVASCRIPT_PATTERN.search(declaration)
    if match is None:
        return NONE
    return [match.group(NAME_GROUP)]


EXTRACT = {
    ELIXIR: ELIXIR_NAMES,
    SCALA: SCALA_NAMES,
    RUST: RUST_NAMES,
    PYTHON: PYTHON_NAMES,
    HASKELL: HASKELL_NAMES,
    JAVASCRIPT: JAVASCRIPT_NAMES,
    C: INCLUDE_NAMES,
    CPP: INCLUDE_NAMES,
}


def DECLARATION(body: str):
    match = KEYWORD_PATTERN.match(body)
    if match is None:
        match = INCLUDE_PATTERN.match(body)
    if match is None:
        return None
    return match.group(KEYWORD_GROUP), match.group(DECLARATION_GROUP)


def RENDER(lines: list) -> list:
    rows = set()
    for line in lines:
        if not line:
            continue
        record = RECORD_PATTERN.match(CHOMP(line))
        if record is None:
            continue
        declaration = DECLARATION(record.group(BODY_GROUP))
        if declaration is None:
            continue
        keyword, body = declaration
        source_path = record.group(PATH_GROUP).removeprefix(RELATIVE_PREFIX)
        ecosystem = ECOSYSTEM.get((EXTENSION(source_path), keyword))
        if ecosystem is None:
            continue
        source_line = int(record.group(LINE_GROUP))
        for name in EXTRACT[ecosystem](body):
            rows.add((ecosystem, name, source_path, source_line))
    if not rows:
        raise ValueError(EMPTY)
    return [list(HEADER)] + [list(row) for row in sorted(rows)]
