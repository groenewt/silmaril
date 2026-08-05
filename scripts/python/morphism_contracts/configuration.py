"""Bootstrap the data-declared morphism validator configuration."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from morphism_contracts.digest.policy import capability_errors
from morphism_contracts.json.document import read_json_file, unique_by_errors
from morphism_contracts.law.lambda_projection import errors as lambda_projection_errors


@dataclass(frozen=True, slots=True)
class Configuration:
    repo: Path
    contract_root: Path
    index_path: Path
    bootstrap_index: dict[str, Any]
    profile_path: Path
    profile: dict[str, Any]

    @classmethod
    def load(cls, repo: Path) -> "Configuration":
        contract_root = repo / "contracts" / "morphisms"
        index_path = contract_root / "contract-set.json"
        bootstrap_index = read_json_file(index_path, repo)
        if not isinstance(bootstrap_index, dict):
            raise ValueError("[contract-set.type] contract set must be an object")

        registrations = [
            row
            for row in bootstrap_index.get("artifacts", [])
            if isinstance(row, dict) and row.get("kind") == "validation-profile"
        ]
        if len(registrations) != 1:
            raise ValueError(
                "[profile.registration.cardinality] contract set must register exactly one "
                f"validation-profile; found {len(registrations)}"
            )
        relative = registrations[0].get("path")
        if not isinstance(relative, str):
            raise ValueError(
                "[profile.registration.path] registered validation profile path is absent"
            )
        profile_path = (contract_root / relative).resolve()
        try:
            profile_path.relative_to(contract_root.resolve())
        except ValueError as error:
            raise ValueError(
                "[profile.registration.path] registered validation profile escapes the contract root"
            ) from error

        profile = read_json_file(profile_path, repo)
        if not isinstance(profile, dict):
            raise ValueError(
                "[profile.bootstrap.type] validation profile must be an object"
            )
        errors = capability_errors(profile.get("digestPolicy"))
        errors.extend(
            unique_by_errors(
                {
                    "contract-set": bootstrap_index,
                    "validation-profile": profile,
                },
                profile.get("uniqueBy"),
            )
        )
        errors.extend(lambda_projection_errors(profile))
        if errors:
            raise ValueError("; ".join(errors))
        return cls(
            repo=repo,
            contract_root=contract_root,
            index_path=index_path,
            bootstrap_index=bootstrap_index,
            profile_path=profile_path,
            profile=profile,
        )
