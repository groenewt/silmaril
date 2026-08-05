"""Load and content-address one registered morphism contract bundle."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

from morphism_contracts.configuration import Configuration
from morphism_contracts.json.document import read_json_file, unique_by_errors


Digest = Callable[[Any], str]


@dataclass(frozen=True, slots=True)
class Bundle:
    index: dict[str, Any]
    documents: dict[str, Any]

    @classmethod
    def load(cls, configuration: Configuration) -> "Bundle":
        index = read_json_file(configuration.index_path, configuration.repo)
        if not isinstance(index, dict):
            raise ValueError("[contract-set.type] contract set must be an object")
        uniqueness = unique_by_errors(
            {
                "contract-set": index,
                "validation-profile": configuration.profile,
            },
            configuration.profile["uniqueBy"],
        )
        if uniqueness:
            raise ValueError("; ".join(uniqueness))

        documents: dict[str, Any] = {}
        seen_paths: set[str] = set()
        for artifact in index.get("artifacts", []):
            if not isinstance(artifact, dict):
                raise ValueError(
                    "[contract-set.artifact.type] contract registration must be an object"
                )
            relative = artifact.get("path", "")
            candidate = (configuration.contract_root / relative).resolve()
            try:
                candidate.relative_to(configuration.contract_root.resolve())
            except ValueError as error:
                raise ValueError(f"contract path escapes root: {relative}") from error
            if relative in seen_paths:
                raise ValueError(f"duplicate contract path: {relative}")
            seen_paths.add(relative)
            identity = artifact.get("id")
            if identity in documents:
                raise ValueError(f"duplicate contract id: {identity}")
            documents[identity] = read_json_file(candidate, configuration.repo)
        return cls(index=index, documents=documents)

    def digest(self, profile: dict[str, Any], digest: Digest) -> str:
        registrations = {
            row["id"]: row for row in self.index.get("artifacts", [])
        }
        policy = profile["digestPolicy"]
        identities = (
            sorted(self.documents)
            if policy["artifactOrder"] == "identity"
            else list(self.documents)
        )
        return digest(
            {
                "contractSet": self.index.get("schema"),
                "artifacts": [
                    {
                        "document": self.documents[identity],
                        "identity": identity,
                        "registration": registrations.get(identity),
                    }
                    for identity in identities
                ],
            }
        )

    def artifact_for(
        self, selector: dict[str, Any], profile: dict[str, Any]
    ) -> str | None:
        if selector.get("contractSet") is True:
            return None
        if "schemaKey" in selector:
            return profile["artifactIds"][selector["schemaKey"]]
        matches = [
            row["id"]
            for row in self.index.get("artifacts", [])
            if row.get("kind") == selector.get("kind")
        ]
        if len(matches) != 1:
            raise ValueError(
                f"artifact selector {selector!r} resolved {len(matches)} values"
            )
        return matches[0]
