from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.frame.effect.value import VALUE as EFFECT
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.frame.output.value import VALUE as OUTPUT
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.input.standard.value import VALUE as INPUT
from config.constants.morphism.specification.paper.atom.anchor.grounding.full.validation.summary.text.projection.process.command.value import VALUE as COMMAND
from config.gate.external.python.stdlib.subprocess.library import DEPENDENCY as SUBPROCESS


def MAIN() -> int:
    return SUBPROCESS.run(COMMAND, stdin=INPUT, stdout=OUTPUT, stderr=EFFECT).returncode


raise SystemExit(MAIN())
