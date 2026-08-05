from config.gate.external.python.morphism.codebase.volume.codec.library import DECODE
from config.gate.external.python.morphism.codebase.volume.lexical.value.library import VALUE
from config.gate.external.python.morphism.codebase.volume.lexical.vector.library import VECTOR
from config.gate.external.python.morphism.codebase.volume.verification.process_coverage.boundary.frame.library import FRAME
from config.gate.external.python.morphism.codebase.volume.verification.process_coverage.construct.accepted.state.library import STATE as ACCEPTED
from config.gate.external.python.morphism.codebase.volume.verification.process_coverage.construct.input.parse.state.library import STATE as PARSED
from config.gate.external.python.morphism.codebase.volume.verification.process_coverage.construct.materialized.state.library import STATE as MATERIALIZED
from config.gate.external.python.morphism.codebase.volume.verification.process_coverage.construct.receipt.render.library import RENDER
from config.gate.external.python.morphism.codebase.volume.verification.process_coverage.construct.validation.state.library import STATE as VALIDATED
from silmaril.sparky.morphism.codebase.volume.verification.process_coverage.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.verification.process_coverage.input.value import Value as Input


def PROJECT(value: Input) -> Frame:
    return FRAME(VECTOR(RENDER(VALIDATED(MATERIALIZED(ACCEPTED(PARSED(DECODE(VALUE(value)))))))))
