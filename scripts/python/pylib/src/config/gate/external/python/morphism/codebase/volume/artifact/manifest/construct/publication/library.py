from config.constants.morphism.codebase.volume.artifact.generated.readback.name.value import VALUE as READBACK_NAMES
from config.constants.morphism.codebase.volume.artifact.manifest.publication.artifacts.key.value import VALUE as ARTIFACTS_KEY
from config.constants.morphism.codebase.volume.artifact.manifest.publication.count.key.value import VALUE as COUNT_KEY
from config.constants.morphism.codebase.volume.artifact.manifest.publication.excluded.suffix.value import VALUE as EXCLUDED_SUFFIX
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.artifact.library import MANIFEST_ARTIFACTS


def PUBLICATION(state: dict) -> dict:
    published = [path for path in MANIFEST_ARTIFACTS(state) if not path.endswith(EXCLUDED_SUFFIX)]
    delivered = sorted(set(published) | set(READBACK_NAMES))
    return {COUNT_KEY: len(delivered), ARTIFACTS_KEY: delivered}
