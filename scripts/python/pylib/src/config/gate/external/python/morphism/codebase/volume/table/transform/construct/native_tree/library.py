from config.constants.morphism.codebase.volume.table.native_tree.comment.prefix.value import VALUE as COMMENT_PREFIX
from config.constants.morphism.codebase.volume.table.native_tree.error.empty.value import VALUE as EMPTY
from config.constants.morphism.codebase.volume.table.native_tree.header.value import VALUE as HEADER
from config.constants.morphism.codebase.volume.table.native_tree.native.control.keyword.value import VALUE as CONTROL_KEYWORDS
from config.constants.morphism.codebase.volume.table.native_tree.native.extension.value import VALUE as NATIVE_EXTENSIONS
from config.constants.morphism.codebase.volume.table.native_tree.native.function.grammar.value import VALUE as NATIVE_FUNCTION_GRAMMAR
from config.constants.morphism.codebase.volume.table.native_tree.native.type.grammar.value import VALUE as NATIVE_TYPE_GRAMMAR
from config.constants.morphism.codebase.volume.table.native_tree.rust.declaration.grammar.value import VALUE as RUST_DECLARATION_GRAMMAR
from config.constants.morphism.codebase.volume.table.native_tree.rust.extension.value import VALUE as RUST_EXTENSIONS
from config.constants.morphism.codebase.volume.table.native_tree.rust.implementation.grammar.value import VALUE as RUST_IMPLEMENTATION_GRAMMAR
from config.constants.morphism.codebase.volume.table.native_tree.source.grammar.value import VALUE as SOURCE_GRAMMAR
from config.gate.external.python.morphism.codebase.volume.lexical.chomp.library import CHOMP
from config.gate.external.python.stdlib.re.library import DEPENDENCY as REGEX

# The observer's rg pattern is `^`, so this stream carries every line of every
# C, C++ and Rust source in the tree; these grammars are the authority on which
# of those lines DECLARES a symbol.  The declaring form is language-specific, so
# the file extension selects the grammar: a `.rs` line is read as Rust, a
# `.c`/`.cc`/`.cpp`/`.cxx`/`.h`/`.hpp` line as C or C++.
#
# A declaration is stated at the head of its own line, so every grammar is
# anchored at the start of the text and a line opening with a comment or
# preprocessor marker is not read at all -- that is what keeps prose, `#define`
# and `#[derive(...)]` out, and it is also what keeps a keyword embedded in a
# string literal out, since such a keyword can never be the first token.
#
# C and C++ TYPES are `namespace`/`struct`/`class`/`union`/`enum` (optionally
# `typedef`-ed or templated) followed by the declared name and then `{`, `;` or
# a `:` base clause.  Requiring that closer is what separates the declaration
# `struct Value {` from the USE `struct stat parent_before, parent_after;`,
# where a second identifier follows the type name.
#
# C and C++ FUNCTIONS are a return type, then the (optionally class-qualified)
# name, then a parenthesised argument list that closes on the same line, then
# only qualifiers, and then the opening brace of the body.  The return type must
# be present, which is what rejects `if (`, `for (`, `while (`, `switch (`,
# `return` and every bare call; `if constexpr (` slips a qualifier into the
# return-type slot, so a control keyword is rejected wherever it appears.  The
# argument list may not itself contain parentheses and the head may not contain
# `.`, `=`, `[` or a quote, so a call whose argument is a lambda or a member
# expression cannot be read as a definition.
#
# A C `typedef` names its type on the line that CLOSES the braced body, not on
# the line that opens it, so a line-oriented reading reaches the struct tag it
# is built from -- `typedef struct word_desc {` declares `word_desc` -- and not
# the alias.  The corpus states ten typedefs: eight open an anonymous body whose
# alias is stated on the closing line, two carry a tag that is projected, and
# one is a function-type alias whose name stands ahead of a parameter list.  The
# alias itself is therefore not projected.
#
# Rust DECLARATIONS are `fn`/`struct`/`enum`/`trait`/`mod` behind the usual
# visibility and effect qualifiers.  An `impl` names no new symbol of its own --
# it names the type it implements FOR -- so the target is read from behind the
# `for` keyword when there is one and from directly behind `impl` when there is
# not.
#
# Precision is preferred to recall.  Excluded by construction: a definition
# whose head is split across lines; a constructor carrying an initialiser list;
# a function PROTOTYPE, which declares no body and so is not a definition; a
# Rust `type` alias, which is not one of the declaring forms named above; and a
# macro, which declares its symbol to the preprocessor rather than the language.
SOURCE = REGEX.compile(SOURCE_GRAMMAR)
NATIVE_TYPE = REGEX.compile(NATIVE_TYPE_GRAMMAR)
NATIVE_FUNCTION = REGEX.compile(NATIVE_FUNCTION_GRAMMAR)
RUST_DECLARATION = REGEX.compile(RUST_DECLARATION_GRAMMAR)
RUST_IMPLEMENTATION = REGEX.compile(RUST_IMPLEMENTATION_GRAMMAR)
RELATIVE_PREFIX = "./"
QUALIFIER_SEPARATOR = "::"
UNDECLARED = None
PATH_GROUP = 1
NUMBER_GROUP = 2
TEXT_GROUP = 3
TYPE_NAME_GROUP = 1
FUNCTION_HEAD_GROUP = 1
FUNCTION_NAME_GROUP = 2
DECLARATION_NAME_GROUP = 1
IMPLEMENTATION_NAME_GROUP = 1
LEADING_TOKEN = 0
TRAILING_QUALIFIER = -1


def NATIVE_SYMBOL(text: str) -> str:
    match = NATIVE_TYPE.match(text)
    if match is not None:
        return match.group(TYPE_NAME_GROUP)
    match = NATIVE_FUNCTION.match(text)
    if match is None:
        return UNDECLARED
    name = match.group(FUNCTION_NAME_GROUP)
    if name.split(QUALIFIER_SEPARATOR)[TRAILING_QUALIFIER] in CONTROL_KEYWORDS:
        return UNDECLARED
    if match.group(FUNCTION_HEAD_GROUP).split()[LEADING_TOKEN] in CONTROL_KEYWORDS:
        return UNDECLARED
    return name


def RUST_SYMBOL(text: str) -> str:
    match = RUST_DECLARATION.match(text)
    if match is not None:
        return match.group(DECLARATION_NAME_GROUP)
    match = RUST_IMPLEMENTATION.match(text)
    if match is None:
        return UNDECLARED
    return match.group(IMPLEMENTATION_NAME_GROUP)


def RENDER(lines: list) -> list:
    rows = set()
    for line in lines:
        if not line:
            continue
        record = SOURCE.match(CHOMP(line))
        if record is None:
            continue
        relative_path = record.group(PATH_GROUP).removeprefix(RELATIVE_PREFIX)
        text = record.group(TEXT_GROUP)
        if text.lstrip().startswith(COMMENT_PREFIX):
            continue
        if relative_path.endswith(RUST_EXTENSIONS):
            symbol = RUST_SYMBOL(text)
        elif relative_path.endswith(NATIVE_EXTENSIONS):
            symbol = NATIVE_SYMBOL(text)
        else:
            continue
        if not symbol:
            continue
        rows.add((relative_path, symbol, int(record.group(NUMBER_GROUP))))
    if not rows:
        raise ValueError(EMPTY)
    return [list(HEADER)] + [list(row) for row in sorted(rows)]
