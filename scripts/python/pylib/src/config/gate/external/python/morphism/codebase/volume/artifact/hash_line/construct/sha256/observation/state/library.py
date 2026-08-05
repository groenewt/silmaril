from config.constants.morphism.codebase.volume.artifact.hash_line.state.digest.key.value import VALUE as DIGEST_KEY
from config.constants.morphism.codebase.volume.digest.process.command.value import VALUE as COMMAND
from config.gate.external.python.morphism.codebase.volume.artifact.hash_line.state.artifact.library import ARTIFACT
from config.gate.external.python.morphism.codebase.volume.digest.process.library import PROCESS
from config.gate.external.python.morphism.codebase.volume.digest.standard.output.library import STANDARD_OUTPUT
from config.gate.external.python.morphism.codebase.volume.lexical.text.library import TEXT


def STATE(state: dict) -> dict:
    return {**state, DIGEST_KEY: TEXT(STANDARD_OUTPUT(PROCESS((*COMMAND, ARTIFACT(state)))))}
