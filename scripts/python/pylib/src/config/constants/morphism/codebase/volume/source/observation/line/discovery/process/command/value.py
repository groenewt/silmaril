from config.constants.morphism.codebase.volume.executable.rg.value import VALUE as RG
from config.constants.morphism.codebase.volume.source.observation.discovery.ignore.argument.value import VALUE as IGNORE_ARGUMENTS


VALUE = (
    RG,
    "--encoding",
    "utf-8",
    "--line-number",
    "--no-heading",
    "--hidden",
    *IGNORE_ARGUMENTS,
    "^",
    ".",
)
