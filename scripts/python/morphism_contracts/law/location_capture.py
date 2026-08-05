"""Scheme dispatch, source-root, and capture laws for a morphism scene."""

from __future__ import annotations

from typing import Any, Mapping

from morphism_contracts.law.common import require


def validate(
    profile: Mapping[str, Any], scene: Mapping[str, Any], errors: list[str]
) -> None:
    location_policy = profile["locationPolicy"]
    source_policy = profile["sourcePolicy"]
    capture_policy = profile["capturePolicy"]
    dispatch = {
        row["key"]: (row["primary"], set(row["schemes"]))
        for row in profile["twinSchemeDispatch"]
    }
    adapters = {
        row["key"]: row["adapterIdentity"]
        for row in profile["twinSchemeDispatch"]
    }
    expectations = {
        row["name"]: (
            row["role"],
            row["access"],
            row["literal"],
            row["normalizedUri"],
        )
        for row in profile["sourceExpectations"]
    }
    registry = scene.get("locationRegistry", {})
    for coordinate, expected in location_policy.items():
        require(
            errors,
            registry.get(coordinate) == expected,
            f"scene: location policy coordinate {coordinate!r} differs from the validation profile",
        )
    adapter_rows = registry.get("adapters", [])
    by_identity = {
        row.get("adapterIdentity"): row
        for row in adapter_rows
        if isinstance(row, dict)
    }
    require(
        errors,
        set(by_identity) == set(adapters.values()),
        "scene: scheme registry differs from the twin adapter set",
    )
    seen_schemes: set[str] = set()
    for key, (primary, schemes) in dispatch.items():
        adapter = by_identity.get(adapters[key], {})
        require(
            errors,
            adapter.get("primaryScheme") == primary,
            f"scene: adapter {key!r} has wrong primary scheme",
        )
        require(
            errors,
            set(adapter.get("schemes", [])) == schemes,
            f"scene: adapter {key!r} has wrong aliases",
        )
        overlap = seen_schemes & schemes
        require(
            errors,
            not overlap,
            f"scene: schemes have ambiguous adapter dispatch {sorted(overlap)}",
        )
        seen_schemes |= schemes

    sources = scene.get("locationSources", [])
    source_by_name = {
        row.get("name"): row for row in sources if isinstance(row, dict)
    }
    require(
        errors,
        set(source_by_name) == set(expectations),
        "scene: explicit source-root registry differs from its validation projection",
    )
    identities: list[Any] = []
    normalized: list[Any] = []
    for name, (role, access, literal, normalized_uri) in expectations.items():
        source = source_by_name.get(name, {})
        location = source.get("location", {})
        identities.append(source.get("sourceIdentity"))
        normalized.append(location.get("normalizedUri"))
        require(
            errors,
            source.get("role") == role and source.get("access") == access,
            f"scene: {name} has the wrong source role/access",
        )
        require(
            errors,
            source.get("aliasOf") == source_policy["aliasOf"],
            f"scene: {name} claims alias identity",
            "scene.location.source-alias",
        )
        require(
            errors,
            source.get("capture") == source_policy["capture"]
            and source.get("followLinks") == source_policy["followLinks"],
            f"scene: {name} is not an explicit non-following root",
        )
        require(
            errors,
            source.get("absorption") == source_policy["absorption"]
            and source.get("imports") == source_policy["imports"],
            f"scene: {name} permits source absorption/import",
        )
        require(
            errors,
            location.get("literal") == literal
            and location.get("normalizedUri") == normalized_uri,
            f"scene: {name} has the wrong literal/normalized URI",
        )
        require(
            errors,
            location.get("matchedScheme") == source_policy["matchedScheme"]
            and location.get("primaryScheme") == source_policy["primaryScheme"],
            f"scene: {name} lacks explicit file dispatch evidence",
        )
        require(
            errors,
            location.get("locatorPredicate") == source_policy["locatorPredicate"],
            f"scene: {name} lacks the canonical located-at relation",
        )
        require(
            errors,
            location.get("lineagePredicate") == source_policy["lineagePredicate"],
            f"scene: {name} lacks adapter lineage",
        )
        require(
            errors,
            source.get("sourceIdentity") != location.get("normalizedUri"),
            f"scene: {name} collapses source identity into locator",
        )
    require(
        errors,
        len(identities) == len(set(identities)),
        "scene: source identities are not distinct",
    )
    require(
        errors,
        len(normalized) == len(set(normalized)),
        "scene: distinct roots collapse onto one locator",
    )
    capture = scene.get("capture", {})
    for coordinate, expected in capture_policy.items():
        require(
            errors,
            capture.get(coordinate) == expected,
            f"scene: capture policy coordinate {coordinate!r} differs from the validation profile",
            "scene.capture.policy",
        )
