from config.constants.morphism.codebase.volume.digest.alphabet.value import VALUE as ALPHABET
from config.constants.morphism.codebase.volume.digest.encoding.value import VALUE as ENCODING
from config.constants.morphism.codebase.volume.digest.length.value import VALUE as LENGTH
from config.constants.morphism.codebase.volume.digest.process.command.value import VALUE as COMMAND
from config.gate.external.python.morphism.codebase.volume.digest.output.library import OUTPUT
from config.gate.external.python.morphism.codebase.volume.digest.process.library import PROCESS

VIOLATION = "artifact_digest_malformed="
DELIMITER = "="


def DIGEST(path: str) -> str:
    text = OUTPUT(PROCESS(COMMAND + (path,))).decode(ENCODING)
    unexpected = [character for character in text if character not in ALPHABET]
    if unexpected or len(text) != LENGTH:
        raise ValueError(VIOLATION + path + DELIMITER + text)
    return text
