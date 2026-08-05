from config.constants.morphism.codebase.volume.table.configuration.application.prefix.value import VALUE as APPLICATION_PREFIX
from config.constants.morphism.codebase.volume.table.configuration.error.empty.value import VALUE as EMPTY
from config.constants.morphism.codebase.volume.table.configuration.grammar.directive.value import VALUE as DIRECTIVE_GRAMMAR
from config.constants.morphism.codebase.volume.table.configuration.grammar.keyword.value import VALUE as KEYWORD_GRAMMAR
from config.constants.morphism.codebase.volume.table.configuration.grammar.record.value import VALUE as RECORD_GRAMMAR
from config.constants.morphism.codebase.volume.table.configuration.grammar.shell.value import VALUE as SHELL_GRAMMAR
from config.constants.morphism.codebase.volume.table.configuration.grammar.target.atom.value import VALUE as ATOM_GRAMMAR
from config.constants.morphism.codebase.volume.table.configuration.grammar.target.module.value import VALUE as MODULE_GRAMMAR
from config.constants.morphism.codebase.volume.table.configuration.grammar.toml.pair.value import VALUE as TOML_PAIR_GRAMMAR
from config.constants.morphism.codebase.volume.table.configuration.grammar.toml.section.value import VALUE as TOML_SECTION_GRAMMAR
from config.constants.morphism.codebase.volume.table.configuration.header.value import VALUE as HEADER
from config.constants.morphism.codebase.volume.table.configuration.qualifier.separator.value import VALUE as QUALIFIER
from config.constants.morphism.codebase.volume.table.configuration.scope.elixir.extension.value import VALUE as ELIXIR_EXTENSION
from config.constants.morphism.codebase.volume.table.configuration.scope.shell.value import VALUE as SHELL_SCOPE
from config.constants.morphism.codebase.volume.table.configuration.scope.toml.extension.value import VALUE as TOML_EXTENSION
from config.gate.external.python.morphism.codebase.volume.lexical.chomp.library import CHOMP
from config.gate.external.python.stdlib.re.library import DEPENDENCY as REGEX

# The observer emits every line of config/**, *.exs, .codex/** and scripts/env/**,
# so almost all of its output is not configuration at all.  Three form grammars
# decide what is: an Elixir `config` directive plus the first-level keys of the
# keyword list it opens, a shell assignment inside scripts/env/**, and a TOML
# pair or section header inside a .toml file.  Anchoring the Elixir directive at
# column zero is what separates it from prose and from local variables named
# `config` (`config = Config.load(...)`, `config dependency, or wire emission`),
# which are always indented inside a function body.
RECORD_PATTERN = REGEX.compile(RECORD_GRAMMAR)
DIRECTIVE_PATTERN = REGEX.compile(DIRECTIVE_GRAMMAR)
ATOM_PATTERN = REGEX.compile(ATOM_GRAMMAR)
MODULE_PATTERN = REGEX.compile(MODULE_GRAMMAR)
KEYWORD_PATTERN = REGEX.compile(KEYWORD_GRAMMAR)
SHELL_PATTERN = REGEX.compile(SHELL_GRAMMAR)
TOML_SECTION_PATTERN = REGEX.compile(TOML_SECTION_GRAMMAR)
TOML_PAIR_PATTERN = REGEX.compile(TOML_PAIR_GRAMMAR)
RELATIVE_PREFIX = "./"
PATH_SEPARATOR = "/"
EXTENSION_SEPARATOR = "."
NO_EXTENSION = ""
INDENT = (" ", "\t")
PATH_GROUP = 1
LINE_GROUP = 2
BODY_GROUP = 3
APPLICATION_GROUP = 1
TARGET_GROUP = 2
NAME_GROUP = 1
LAST = -1


def EXTENSION(source_path: str) -> str:
    base = source_path.rsplit(PATH_SEPARATOR, 1)[LAST]
    if EXTENSION_SEPARATOR not in base:
        return NO_EXTENSION
    return EXTENSION_SEPARATOR + base.rsplit(EXTENSION_SEPARATOR, 1)[LAST]


def QUALIFY(owner: str, name: str) -> str:
    if owner is None:
        return name
    return owner + QUALIFIER + name


def DIRECTIVE(body: str):
    # `config :app, Module,` / `config :app, :key, value` / `config :app,` all
    # address a configuration root; the second argument, when present, is the
    # leaf the directive writes and belongs in the key.
    match = DIRECTIVE_PATTERN.match(body)
    if match is None:
        return None
    application = match.group(APPLICATION_GROUP).removeprefix(APPLICATION_PREFIX)
    target = match.group(TARGET_GROUP)
    atom = ATOM_PATTERN.match(target)
    if atom is not None:
        return QUALIFY(application, atom.group(NAME_GROUP))
    module = MODULE_PATTERN.match(target)
    if module is not None:
        return QUALIFY(application, module.group(NAME_GROUP))
    return application


def ELIXIR(body: str, directive: str, rows: set, source_path: str, source_line: int):
    # Returns the directive still in force after this line.  A block opened by a
    # directive runs until the next line that starts back at column zero; the
    # keys written by that block are its keyword entries one level in.
    opened = DIRECTIVE(body)
    if opened is not None:
        rows.add((opened, source_path, source_line))
        return opened
    if directive is None or not body:
        return directive
    if not body.startswith(INDENT):
        return None
    keyword = KEYWORD_PATTERN.match(body)
    if keyword is not None:
        rows.add((QUALIFY(directive, keyword.group(NAME_GROUP)), source_path, source_line))
    return directive


def TOML(body: str, section: str, rows: set, source_path: str, source_line: int):
    heading = TOML_SECTION_PATTERN.match(body)
    if heading is not None:
        rows.add((heading.group(NAME_GROUP), source_path, source_line))
        return heading.group(NAME_GROUP)
    pair = TOML_PAIR_PATTERN.match(body)
    if pair is not None:
        rows.add((QUALIFY(section, pair.group(NAME_GROUP)), source_path, source_line))
    return section


def SHELL(body: str, rows: set, source_path: str, source_line: int):
    match = SHELL_PATTERN.match(body)
    if match is not None:
        rows.add((match.group(NAME_GROUP), source_path, source_line))


def RENDER(lines: list) -> list:
    rows = set()
    owner = None
    directive = None
    section = None
    for line in lines:
        if not line:
            continue
        record = RECORD_PATTERN.match(CHOMP(line))
        if record is None:
            continue
        source_path = record.group(PATH_GROUP).removeprefix(RELATIVE_PREFIX)
        body = record.group(BODY_GROUP)
        source_line = int(record.group(LINE_GROUP))
        if source_path != owner:
            owner, directive, section = source_path, None, None
        extension = EXTENSION(source_path)
        if extension == ELIXIR_EXTENSION:
            directive = ELIXIR(body, directive, rows, source_path, source_line)
        elif extension == TOML_EXTENSION:
            section = TOML(body, section, rows, source_path, source_line)
        elif source_path.startswith(SHELL_SCOPE):
            SHELL(body, rows, source_path, source_line)
    if not rows:
        raise ValueError(EMPTY)
    return [list(HEADER)] + [list(row) for row in sorted(rows)]
