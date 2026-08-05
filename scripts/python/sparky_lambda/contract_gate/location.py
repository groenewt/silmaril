"""Registered file-IRI to host-path projection inside ContractGate."""

from __future__ import annotations

import json
import os
from pathlib import Path

from ..locator import (
    CanonicalIri,
    FileLocationRegistration,
    LexicalHostPathProjection,
    Locator,
)


def _read(path: Path):
    def unique(pairs):
        value = {}
        for key, item in pairs:
            if key in value:
                raise ValueError(f"duplicate JSON coordinate {key!r} in {path}")
            value[key] = item
        return value

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique)


def _row(rows, key: str, value: str, coordinate: str):
    matches = tuple(row for row in rows if isinstance(row, dict) and row.get(key) == value)
    if len(matches) != 1:
        raise ValueError(f"{coordinate} must resolve exactly one {key}={value!r}")
    return matches[0]


def _text(value, coordinate: str) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError(f"{coordinate} is not registered text")
    return value


def registration(repository_host_path: str) -> FileLocationRegistration:
    root = Path(os.path.abspath(repository_host_path)) / "contracts" / "morphisms"
    contract_set = _read(root / "contract-set.json")
    artifacts = contract_set.get("artifacts")
    if not isinstance(artifacts, list):
        raise ValueError("contract-set artifacts are not a sequence")
    scene_row = _row(artifacts, "kind", "scene", "contract-set scene")
    profile_row = _row(
        artifacts,
        "kind",
        "validation-profile",
        "contract-set validation profile",
    )
    scene = _read(root / _text(scene_row.get("path"), "scene.path"))
    profile = _read(root / _text(profile_row.get("path"), "profile.path"))
    registry = scene.get("locationRegistry")
    if not isinstance(registry, dict):
        raise ValueError("scene location registry is not an object")
    adapters = registry.get("adapters")
    if not isinstance(adapters, list):
        raise ValueError("scene location adapters are not a sequence")
    adapter = _row(adapters, "primaryScheme", "file", "scene file adapter")
    sources = scene.get("locationSources")
    if not isinstance(sources, list):
        raise ValueError("scene location sources are not a sequence")
    repository_source = _row(sources, "name", "repository", "repository source")
    location = repository_source.get("location")
    if not isinstance(location, dict):
        raise ValueError("repository source location is not an object")
    source_policy = profile.get("sourcePolicy")
    if not isinstance(source_policy, dict):
        raise ValueError("profile source policy is not an object")
    dispatch = profile.get("twinSchemeDispatch")
    if not isinstance(dispatch, list):
        raise ValueError("profile twin scheme dispatch is not a sequence")
    file_dispatch = _row(dispatch, "key", "file", "profile file dispatch")

    adapter_identity = _text(adapter.get("adapterIdentity"), "adapter.identity")
    if adapter_identity != _text(location.get("adapterIdentity"), "location.adapter"):
        raise ValueError("scene file adapter differs from repository location")
    if adapter_identity != _text(file_dispatch.get("adapterIdentity"), "dispatch.adapter"):
        raise ValueError("scene file adapter differs from twin file dispatch")
    primary_scheme = _text(adapter.get("primaryScheme"), "adapter.primaryScheme")
    if primary_scheme != _text(location.get("primaryScheme"), "location.primaryScheme"):
        raise ValueError("repository location primary scheme differs from adapter")
    if primary_scheme != _text(source_policy.get("primaryScheme"), "sourcePolicy.primaryScheme"):
        raise ValueError("source policy primary scheme differs from adapter")
    schemes = file_dispatch.get("schemes")
    if schemes != [primary_scheme]:
        raise ValueError("twin file dispatch is not the exact singleton file scheme")
    lineage_predicate = _text(location.get("lineagePredicate"), "location.lineagePredicate")
    locator_predicate = _text(location.get("locatorPredicate"), "location.locatorPredicate")
    if lineage_predicate != _text(source_policy.get("lineagePredicate"), "sourcePolicy.lineagePredicate"):
        raise ValueError("source location lineage predicate differs from policy")
    if locator_predicate != _text(source_policy.get("locatorPredicate"), "sourcePolicy.locatorPredicate"):
        raise ValueError("source locator predicate differs from policy")
    substrate_identity = _text(adapter.get("substrateIdentity"), "adapter.substrateIdentity")
    if substrate_identity != _text(location.get("substrateIdentity"), "location.substrateIdentity"):
        raise ValueError("repository substrate differs from file adapter")
    return FileLocationRegistration(
        adapter_identity=adapter_identity,
        atlas_type_identity=_text(adapter.get("atlasType"), "adapter.atlasType"),
        substrate_identity=substrate_identity,
        lineage_predicate=lineage_predicate,
        locator_predicate=locator_predicate,
        matched_scheme=_text(location.get("matchedScheme"), "location.matchedScheme"),
        primary_scheme=primary_scheme,
        proof_status=_text(location.get("proofStatus"), "location.proofStatus"),
    )


def admit(host_path: str, policy: FileLocationRegistration) -> Locator:
    path = Path(os.path.abspath(host_path))
    canonical = CanonicalIri(
        value=path.as_uri(),
        atlas_type_identity=policy.atlas_type_identity,
    )
    if not canonical.value.startswith(f"{policy.primary_scheme}://"):
        raise ValueError("canonical host locator does not use the registered file scheme")
    return Locator(
        canonical=canonical,
        host_path=LexicalHostPathProjection(
            lexical=str(path),
            source=canonical,
            registration=policy,
        ),
    )


def repository(host_path: str) -> Locator:
    return admit(host_path, registration(host_path))


def child(parent: Locator, name: str) -> Locator:
    return admit(
        str(Path(parent.host_path.lexical) / name),
        parent.host_path.registration,
    )
