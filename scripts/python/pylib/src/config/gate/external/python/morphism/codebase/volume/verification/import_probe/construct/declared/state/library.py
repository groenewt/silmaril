from config.constants.morphism.codebase.volume.verification.import_probe.state.declared.key.value import VALUE as DECLARED_KEY
from config.constants.morphism.codebase.volume.verification.import_probe.state.inline.key.value import VALUE as INLINE_KEY
from config.gate.external.python.morphism.codebase.volume.verification.import_probe.state.prefix.library import PREFIX
from config.gate.external.python.morphism.codebase.volume.verification.import_probe.state.registered.library import REGISTERED

MODULE_ORIGIN = 1
PREFIX_VIOLATION = "import_probe_module_prefix_empty="
VACUOUS_VIOLATION = "import_probe_no_declared_module_carries_prefix="


def STATE(state: dict) -> dict:
    prefix = PREFIX(state)
    if not prefix:
        raise ValueError(PREFIX_VIOLATION + prefix)
    registered = REGISTERED(state)
    declared = [entry for entry in registered if entry[MODULE_ORIGIN].startswith(prefix)]
    inline = [entry for entry in registered if not entry[MODULE_ORIGIN].startswith(prefix)]
    if not declared:
        raise ValueError(VACUOUS_VIOLATION + prefix)
    return {**state, DECLARED_KEY: declared, INLINE_KEY: inline}
