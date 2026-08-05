"""Test-only host mechanics kept inside ContractGate."""

from __future__ import annotations

from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
import tempfile

from ..locator import Locator
from .location import admit, repository as repository_locator


@dataclass(frozen=True, slots=True)
class ResponsePair:
    first: Locator
    second: Locator


def repository(module_file: str) -> Locator:
    root = Path(module_file).resolve().parents[2]
    return repository_locator(str(root))


@contextmanager
def responses(repository: Locator, prefix: str):
    with tempfile.TemporaryDirectory(prefix=prefix) as directory:
        policy = repository.host_path.registration
        yield ResponsePair(
            first=admit(str(Path(directory) / "first.json"), policy),
            second=admit(str(Path(directory) / "second.json"), policy),
        )


@contextmanager
def symbolic_link(repository: Locator, target: Locator):
    with tempfile.TemporaryDirectory(prefix="sparky-lambda-link-") as directory:
        path = Path(directory) / "link.json"
        path.symlink_to(target.host_path.lexical)
        yield admit(str(path), repository.host_path.registration)
