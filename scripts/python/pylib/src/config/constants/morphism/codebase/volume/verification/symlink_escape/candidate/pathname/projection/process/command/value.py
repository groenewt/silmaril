from config.constants.morphism.codebase.volume.executable.jq.value import VALUE as JQ


VALUE = (JQ, "--compact-output", '.[0] |= sub("/+$"; "")')
