from config.constants.morphism.codebase.volume.table.dependencies.ecosystem.name.c.value import VALUE as C
from config.constants.morphism.codebase.volume.table.dependencies.ecosystem.name.cpp.value import VALUE as CPP
from config.constants.morphism.codebase.volume.table.dependencies.ecosystem.name.elixir.value import VALUE as ELIXIR
from config.constants.morphism.codebase.volume.table.dependencies.ecosystem.name.haskell.value import VALUE as HASKELL
from config.constants.morphism.codebase.volume.table.dependencies.ecosystem.name.javascript.value import VALUE as JAVASCRIPT
from config.constants.morphism.codebase.volume.table.dependencies.ecosystem.name.python.value import VALUE as PYTHON
from config.constants.morphism.codebase.volume.table.dependencies.ecosystem.name.rust.value import VALUE as RUST
from config.constants.morphism.codebase.volume.table.dependencies.ecosystem.name.scala.value import VALUE as SCALA

# The closed vocabulary: a (file extension, declaration keyword) pair names the
# language whose dependency grammar the line is read with.  A pair absent from
# this map is not a dependency observation -- prose in .md/.txt/.yaml, CSV data
# rows, vendored snapshots (.vendor), Perl git-hook samples (.sample), and shell
# heredocs (.sh, which carry both Python and Haskell imports and so cannot be
# classified from the host extension) all fall out here rather than being
# guessed at.  `require` in .scala is Scala's precondition function, not a
# dependency, and is likewise absent.
VALUE = {
    (".ex", "alias"): ELIXIR,
    (".ex", "import"): ELIXIR,
    (".ex", "require"): ELIXIR,
    (".ex", "use"): ELIXIR,
    (".exs", "alias"): ELIXIR,
    (".exs", "import"): ELIXIR,
    (".exs", "require"): ELIXIR,
    (".exs", "use"): ELIXIR,
    (".scala", "import"): SCALA,
    (".sc", "import"): SCALA,
    (".py", "import"): PYTHON,
    (".rs", "use"): RUST,
    (".hs", "import"): HASKELL,
    (".js", "import"): JAVASCRIPT,
    (".mjs", "import"): JAVASCRIPT,
    (".c", "#include"): C,
    (".cpp", "#include"): CPP,
    (".hpp", "#include"): CPP,
}
