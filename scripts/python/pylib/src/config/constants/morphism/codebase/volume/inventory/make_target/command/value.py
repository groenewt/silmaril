from config.constants.morphism.codebase.volume.executable.rg.value import VALUE as RG


VALUE = (RG, "--sort", "path", "--hidden", "--line-number", "--glob", "!.git/**", "--glob", "Makefile", "--glob", "*.mk", "^[A-Za-z0-9][A-Za-z0-9_.%/-]*:", ".")
