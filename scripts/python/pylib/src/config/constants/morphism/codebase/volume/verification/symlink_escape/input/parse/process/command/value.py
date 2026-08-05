from config.constants.morphism.codebase.volume.executable.jq.value import VALUE as JQ


VALUE = (JQ, "--null-input", "--compact-output", "$ARGS.positional", "--args")
