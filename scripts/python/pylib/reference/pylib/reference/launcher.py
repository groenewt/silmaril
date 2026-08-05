from config.gate.external.project.bootstrap.library import DEPENDENCY as BOOTSTRAP
from config.gate.external.project.config.registry.library import DEPENDENCY as REGISTRY

def launch(frame): return BOOTSTRAP.resolve(REGISTRY.build(frame))
