from config.constants.morphism.codebase.volume.executable.rg.value import VALUE as RG


VALUE = (RG, "--sort", "path", "--hidden", "--line-number", "--glob", "!.git/**", "(defmodule[[:space:]]+Mix[.]Tasks[.]|^[A-Za-z0-9][A-Za-z0-9_.%/-]*:)", ".")
