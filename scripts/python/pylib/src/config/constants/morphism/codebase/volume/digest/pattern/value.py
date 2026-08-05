from config.constants.morphism.codebase.volume.digest.separator.value import VALUE as SEPARATOR

HEXADECIMAL = "^([0-9a-f]{64})"
RELATIVE_PATH = "(.+)$"

VALUE = HEXADECIMAL + SEPARATOR + RELATIVE_PATH
