from config.constants.morphism.codebase.volume.artifact.atomic_delivery.process.command.value import VALUE as COMMAND
from config.constants.morphism.codebase.volume.executable.mv.value import VALUE as MV


def test_atomic_delivery_is_one_fail_closed_directory_rename() -> None:
    assert COMMAND == (MV, "--no-copy", "-T", "--")
