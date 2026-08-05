from config.gate.external.python.morphism.codebase.volume.codec.library import DECODE
from config.gate.external.python.morphism.codebase.volume.lexical.value.library import VALUE
from config.gate.external.python.morphism.codebase.volume.lexical.vector.library import VECTOR
from config.gate.external.python.morphism.codebase.volume.verification.table_header.boundary.frame.library import FRAME
from config.gate.external.python.morphism.codebase.volume.verification.table_header.construct.input.parse.state.library import STATE as PARSED
from config.gate.external.python.morphism.codebase.volume.verification.table_header.construct.observation.state.library import STATE as OBSERVED
from config.gate.external.python.morphism.codebase.volume.verification.table_header.construct.receipt.render.library import RENDER
from config.gate.external.python.morphism.codebase.volume.verification.table_header.construct.validation.state.library import STATE as VALIDATED
from silmaril.sparky.morphism.codebase.volume.verification.table_header.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.verification.table_header.input.value import Value as Input


def PROJECT(value: Input) -> Frame:
    return FRAME(VECTOR(RENDER(VALIDATED(OBSERVED(PARSED(DECODE(VALUE(value))))))))
