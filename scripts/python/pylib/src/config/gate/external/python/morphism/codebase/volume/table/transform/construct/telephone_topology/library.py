from config.constants.morphism.codebase.volume.table.telephone_topology.alias.grammar.value import VALUE as ALIAS_GRAMMAR
from config.constants.morphism.codebase.volume.table.telephone_topology.child.grammar.value import VALUE as CHILD_GRAMMAR
from config.constants.morphism.codebase.volume.table.telephone_topology.elixir.module.grammar.value import VALUE as MODULE_GRAMMAR
from config.constants.morphism.codebase.volume.table.telephone_topology.error.duplicate.value import VALUE as DUPLICATE
from config.constants.morphism.codebase.volume.table.telephone_topology.error.empty.value import VALUE as EMPTY
from config.constants.morphism.codebase.volume.table.telephone_topology.error.evidence.absent.value import VALUE as ABSENT
from config.constants.morphism.codebase.volume.table.telephone_topology.error.source.invalid.value import VALUE as INVALID
from config.constants.morphism.codebase.volume.table.telephone_topology.evidence.token.value import VALUE as EVIDENCE_TOKENS
from config.constants.morphism.codebase.volume.table.telephone_topology.header.value import VALUE as HEADER
from config.constants.morphism.codebase.volume.table.telephone_topology.native.namespace.grammar.value import VALUE as NAMESPACE_GRAMMAR
from config.constants.morphism.codebase.volume.table.telephone_topology.source.grammar.value import VALUE as SOURCE_GRAMMAR
from config.gate.external.python.morphism.codebase.volume.lexical.chomp.library import CHOMP
from config.gate.external.python.stdlib.re.library import DEPENDENCY as REGEX

# The observer globs the supervision spine -- the application and kernel
# supervisors, the switchboard, the L1 avro writer and the io_uring executor --
# and matches `^`, so this stream carries every line of those sources.  The
# table states that spine twice over.
#
# The SUPERVISOR half reads the declaring module of each file (`defmodule` in
# Elixir, `namespace` in C++) as a topology layer and the capitalised head of
# each child entry -- a `{Child, arg}` tuple or a bare `Child,` in a child list
# -- as one child of that layer, in the order the source states them.  A child
# stated by its last segment is resolved through the file's own `alias`
# declarations, so the row carries the module the runtime will start rather than
# the shorthand the source spells; a layer is never its own child.
#
# The EVIDENCE half carries the declared token pairs: each pair names a topology
# layer and a token whose presence in the source is the evidence for it.  Every
# line containing a token is projected under that layer, ordered within the
# layer, and attributed to the module that declares the file.  A token that the
# corpus does not state anywhere is a broken claim, not an empty result, so the
# absent tokens are named and the construction fails.
#
# A line the observer emitted that does not carry a `path:line:` prefix is a
# corrupt observation rather than an uninteresting one, so it fails the
# construction too, and two identical rows would mean one supervision fact
# counted twice, so the rows are held distinct.
SOURCE = REGEX.compile(SOURCE_GRAMMAR)
MODULE = REGEX.compile(MODULE_GRAMMAR)
NAMESPACE = REGEX.compile(NAMESPACE_GRAMMAR)
ALIAS = REGEX.compile(ALIAS_GRAMMAR)
CHILD = REGEX.compile(CHILD_GRAMMAR)
RELATIVE_PREFIX = "./"
MODULE_SEPARATOR = "."
TOKEN_SEPARATOR = ","
DETAIL_SEPARATOR = "="
PAIR_STRIDE = 2
LAYER_OFFSET = 0
TOKEN_OFFSET = 1
ORDER_ORIGIN = 1
PATH_GROUP = 1
NUMBER_GROUP = 2
TEXT_GROUP = 3
NAME_GROUP = 1
TRAILING_SEGMENT = -1
EVIDENCE_PAIRS = tuple(
    zip(EVIDENCE_TOKENS[LAYER_OFFSET::PAIR_STRIDE], EVIDENCE_TOKENS[TOKEN_OFFSET::PAIR_STRIDE])
)


def DECLARED(text: str) -> str:
    match = MODULE.match(text)
    if match is None:
        match = NAMESPACE.match(text)
    if match is None:
        return None
    return match.group(NAME_GROUP)


def RESOLVED(child: str, aliases: dict) -> str:
    if MODULE_SEPARATOR in child:
        return child
    return aliases.get(child, child)


def RENDER(lines: list) -> list:
    sources = []
    modules = {}
    aliases = {}
    children = {}
    for line in lines:
        if not line:
            continue
        record = SOURCE.match(CHOMP(line))
        if record is None:
            raise ValueError(INVALID + DETAIL_SEPARATOR + CHOMP(line))
        source_path = record.group(PATH_GROUP).removeprefix(RELATIVE_PREFIX)
        source_line = int(record.group(NUMBER_GROUP))
        text = record.group(TEXT_GROUP)
        declared = DECLARED(text)
        if declared is not None:
            modules[source_path] = declared
        entry = ALIAS.match(text)
        if entry is not None:
            name = entry.group(NAME_GROUP)
            aliases.setdefault(source_path, {})[name.split(MODULE_SEPARATOR)[TRAILING_SEGMENT]] = name
        sources.append((source_path, source_line, text))
        if source_path not in modules:
            continue
        child = CHILD.match(text)
        if child is None:
            continue
        resolved = RESOLVED(child.group(NAME_GROUP), aliases.get(source_path, {}))
        if resolved == modules[source_path]:
            continue
        children.setdefault(modules[source_path], []).append(
            (resolved, source_path, source_line, text)
        )
    supervisor_rows = []
    for layer, entries in children.items():
        for order, entry in enumerate(entries, ORDER_ORIGIN):
            supervisor_rows.append([layer, entry[0], order, entry[1], entry[2], entry[3]])
    matched = set()
    grouped = {}
    for source_path, source_line, text in sources:
        for layer, token in EVIDENCE_PAIRS:
            if token not in text:
                continue
            matched.add(token)
            grouped.setdefault(layer, []).append(
                (modules.get(source_path, source_path), source_path, source_line, text)
            )
    missing = [token for layer, token in EVIDENCE_PAIRS if token not in matched]
    if missing:
        raise ValueError(ABSENT + DETAIL_SEPARATOR + TOKEN_SEPARATOR.join(missing))
    evidence_rows = []
    for layer, entries in grouped.items():
        for order, entry in enumerate(sorted(entries), ORDER_ORIGIN):
            evidence_rows.append([layer, entry[0], order, entry[1], entry[2], entry[3]])
    rows = supervisor_rows + evidence_rows
    if not rows:
        raise ValueError(EMPTY)
    if len({tuple(row) for row in rows}) != len(rows):
        raise ValueError(DUPLICATE)
    return [list(HEADER)] + sorted(rows)
