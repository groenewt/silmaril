from config.constants.morphism.codebase.volume.artifact.manifest.artifact.bytes.key.value import VALUE as BYTES_KEY
from config.constants.morphism.codebase.volume.artifact.manifest.artifact.path.key.value import VALUE as PATH_KEY
from config.constants.morphism.codebase.volume.artifact.manifest.artifact.sha256.key.value import VALUE as SHA256_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.bytes.library import ARTIFACT_BYTES
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.digests.library import ARTIFACT_DIGESTS

VIOLATION = "manifest_artifact_digest_absent="


def ARTIFACTS(state: dict) -> list:
    sizes = ARTIFACT_BYTES(state)
    digests = ARTIFACT_DIGESTS(state)
    missing = [path for path in sizes if path not in digests]
    if missing:
        raise ValueError(VIOLATION + ",".join(sorted(missing)))
    return [
        {BYTES_KEY: sizes[path], PATH_KEY: path, SHA256_KEY: digests[path]}
        for path in sorted(sizes)
    ]
