from config.constants.selection.mode.value import VALUE as MODE
from config.constants.selection.archetype.value import VALUE as ARCHETYPE
from config.constants.selection.federation.value import VALUE as FEDERATION
from config.constants.selection.filesystem.value import VALUE as FILESYSTEM
from config.constants.selection.volatility.value import VALUE as VOLATILITY
from config.constants.selection.yggdrasil.configuration.value import VALUE as YGGDRASIL_CONFIGURATION
from config.constants.selection.yggdrasil.format.value import VALUE as YGGDRASIL_FORMAT

def build(frame): return frame.bind_mode(MODE).bind_archetype(ARCHETYPE).bind_federation(FEDERATION).bind_filesystem(FILESYSTEM).bind_volatility(VOLATILITY).bind_yggdrasil_configuration(YGGDRASIL_CONFIGURATION).bind_yggdrasil_format(YGGDRASIL_FORMAT)
