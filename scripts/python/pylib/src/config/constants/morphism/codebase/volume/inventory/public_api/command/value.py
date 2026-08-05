from config.constants.morphism.codebase.volume.executable.rg.value import VALUE as RG


VALUE = (RG, "--sort", "path", "--hidden", "--line-number", "--glob", "!.git/**", "--glob", "*.ex", "--glob", "*.exs", "^", ".")
