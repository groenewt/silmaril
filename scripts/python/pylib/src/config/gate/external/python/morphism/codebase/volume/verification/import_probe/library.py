from config.gate.external.python.morphism.codebase.volume.codec.library import DECODE
from config.gate.external.python.morphism.codebase.volume.lexical.value.library import VALUE
from config.gate.external.python.morphism.codebase.volume.lexical.vector.library import VECTOR
from config.gate.external.python.morphism.codebase.volume.verification.import_probe.boundary.frame.library import FRAME
from config.gate.external.python.morphism.codebase.volume.verification.import_probe.construct.declared.state.library import STATE as DECLARED
from config.gate.external.python.morphism.codebase.volume.verification.import_probe.construct.input.parse.state.library import STATE as PARSED
from config.gate.external.python.morphism.codebase.volume.verification.import_probe.construct.probe.state.library import STATE as PROBED
from config.gate.external.python.morphism.codebase.volume.verification.import_probe.construct.receipt.render.library import RENDER
from config.gate.external.python.morphism.codebase.volume.verification.import_probe.construct.registry.state.library import STATE as REGISTERED
from config.gate.external.python.morphism.codebase.volume.verification.import_probe.construct.validation.state.library import STATE as VALIDATED
from silmaril.sparky.morphism.codebase.volume.verification.import_probe.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.verification.import_probe.input.value import Value as Input


def PROJECT(value: Input) -> Frame:
    return FRAME(VECTOR(RENDER(VALIDATED(PROBED(DECLARED(REGISTERED(PARSED(DECODE(VALUE(value))))))))))
