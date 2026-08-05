from config.constants.morphism.codebase.volume.executable.rg.value import VALUE as RG
from config.constants.morphism.codebase.volume.shared.component.bibliography.token.value import VALUE as TOKENS


VALUE = (
    RG,
    "--fixed-strings",
    "-e",
    TOKENS[0],
    "-e",
    TOKENS[1],
    "-",
)
