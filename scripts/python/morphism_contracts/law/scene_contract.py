"""Cross-substrate orchestration laws for one morphism scene."""

from __future__ import annotations

from typing import Any, Mapping

from morphism_contracts.law import anchor_gateway, atlas, location_capture
from morphism_contracts.law import runtime_shoes
from morphism_contracts.law.common import Digest, require


def validate(
    profile: Mapping[str, Any],
    digest: Digest,
    scene: Mapping[str, Any],
    lexicon: Mapping[str, Any],
    errors: list[str],
) -> None:
    policy = profile["scenePolicy"]
    schema_ids = profile["artifactIds"]
    required_shoes = {row["canonicalName"] for row in profile["runtimeShoes"]}
    deliveries = {row["id"] for row in profile["deliveries"]}
    delivery_expectations = {row["id"]: row for row in profile["deliveries"]}
    migrations = {
        row["id"]: (row["functor"], row["realization"])
        for row in profile["migrations"]
    }
    require(
        errors,
        scene.get("defaultMigration") == policy["defaultMigration"],
        "scene: default migration differs from the validation profile",
    )
    require(
        errors,
        scene.get("lexicon") == lexicon.get("lexicon"),
        "scene: lexicon reference does not resolve",
    )
    require(
        errors,
        scene.get("inputSchema")
        == f"{schema_ids['topology']}#{policy['inputAnchor']}",
        "scene: wrong input schema",
    )
    require(
        errors,
        scene.get("outputSchema")
        == f"{schema_ids['topology']}#{policy['outputAnchor']}",
        "scene: wrong output schema",
    )
    require(
        errors,
        scene.get("identity", {}).get("successor") == profile["successor"],
        "scene: successor identity is not canonical GraphAtlas sparky",
    )
    require(
        errors,
        scene.get("openWorld") == profile["openWorld"],
        "scene: open-world provisional discovery law differs from the validation profile",
        "scene.open-world",
    )
    for row in scene.get("identity", {}).get("predecessorEvidence", []):
        require(
            errors,
            row.get("evidenceOnly") == policy["predecessorEvidenceOnly"]
            and row.get("activeInSuccessor") == policy["predecessorActive"],
            f"scene: predecessor {row.get('value')!r} is active",
        )

    invariants = set(scene.get("invariants", []))
    required_invariants = set(profile["requiredInvariants"])
    require(
        errors,
        required_invariants <= invariants,
        f"scene: required invariants missing {sorted(required_invariants - invariants)}",
    )
    require(
        errors,
        not ({name.lower() for name in required_shoes} & invariants),
        "scene: runtime shoe names became universal invariants",
    )

    realized_deliveries = {
        row.get("id"): row
        for row in scene.get("deliveries", [])
        if isinstance(row, dict)
    }
    require(
        errors,
        set(realized_deliveries) == deliveries,
        "scene: delivery set differs from the registered profile",
    )
    for name, expectation in delivery_expectations.items():
        delivery = realized_deliveries.get(name, {})
        require(
            errors,
            delivery.get("outputCapability") == expectation["capability"],
            f"scene: {name} has wrong output capability",
        )
        for coordinate in policy["deliveryComparedCoordinates"]:
            require(
                errors,
                delivery.get(coordinate) == expectation[coordinate],
                f"scene: {name} coordinate {coordinate!r} differs from the validation profile",
            )
        require(
            errors,
            delivery.get("topologyDigest") == policy["topologyDigest"],
            f"scene: {name} does not bind topology digest",
            "scene.delivery.topology-digest",
        )

    realized_migrations = {
        row.get("id"): row
        for row in scene.get("migrations", [])
        if isinstance(row, dict)
    }
    require(
        errors,
        set(realized_migrations) == set(migrations),
        "scene: migration set differs from the registered profile",
    )
    for name, (functor, realization) in migrations.items():
        migration = realized_migrations.get(name, {})
        require(
            errors,
            migration.get("functor") == functor
            and migration.get("realization") == realization,
            f"scene: {name} has the wrong categorical mode",
        )
        missing_coordinates = [
            coordinate
            for coordinate in policy["migrationRequiredCoordinates"]
            if not migration.get(coordinate)
        ]
        require(
            errors,
            not missing_coordinates,
            f"scene: {name} omits registered coordinates {missing_coordinates}",
        )
        require(
            errors,
            bool(migration.get("deliveries"))
            and set(migration.get("deliveries", [])) <= deliveries,
            f"scene: {name} has invalid deliveries",
        )
    composite = realized_migrations.get(policy["defaultMigration"], {})
    require(
        errors,
        set(composite.get("deliveries", [])) == deliveries
        and policy["deliveryEquivalenceInvariant"]
        in composite.get("invariants", []),
        "scene: default composite does not require delivery digest equivalence",
    )
    require(
        errors,
        scene.get("proofPolicy") == profile["proofPolicy"],
        "scene: proof policy differs from the validation profile",
    )
    require(
        errors,
        scene.get("completion") == profile["completionPolicy"],
        "scene: completion policy differs from the validation profile",
    )

    grounding = profile["grounding"]
    citations = {
        row.get("citation")
        for row in scene.get("grounding", [])
        if isinstance(row, dict)
    }
    required_citations = set(grounding["requiredCitations"])
    require(
        errors,
        required_citations <= citations,
        f"scene: direct grounding missing {sorted(required_citations - citations)}",
    )
    prairie_rows = [
        row
        for row in scene.get("grounding", [])
        if row.get("citation") == grounding["prairieCitation"]
    ]
    require(
        errors,
        len(prairie_rows) == 1
        and prairie_rows[0].get("sourceDigest") == grounding["prairieDigest"],
        "scene: canonical Prairie-Dog source/digest grounding is missing or ambiguous",
    )
    direct_prefixes = tuple(grounding["directSourcePrefixes"])
    for row in scene.get("grounding", []):
        citation = row.get("citation", "")
        direct_source = (
            citation.startswith(direct_prefixes)
            or citation == grounding["prairieCitation"]
        )
        line_is_explicit = citation.rsplit(":", 1)[-1].isdigit()
        require(
            errors,
            direct_source
            and (line_is_explicit or not grounding["lineRequired"]),
            f"scene: invalid direct source citation {citation!r}",
        )

    location_capture.validate(profile, scene, errors)
    anchor_gateway.validate(profile, digest, scene, errors)
    runtime_shoes.validate(profile, scene, errors)
    atlas.validate(profile, scene, errors)

    waves = scene.get("waves", [])
    orders = [row.get("order") for row in waves]
    origin = policy["waveOrderOrigin"]
    require(
        errors,
        orders == list(range(origin, origin + len(waves))),
        "scene: waves must have contiguous deterministic order",
    )
    seen: set[str] = set()
    for wave in waves:
        require(
            errors,
            set(wave.get("requires", [])) <= seen,
            f"scene: wave {wave.get('id')!r} requires a later or missing wave",
        )
        if wave.get("id"):
            seen.add(wave["id"])
