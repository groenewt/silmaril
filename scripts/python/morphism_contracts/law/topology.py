"""Topology-schema laws kept separate from JSON-Schema mechanics."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any


Equal = Callable[[Any, Any], bool]


def require(
    errors: list[str], condition: bool, message: str, rule_id: str | None = None
) -> None:
    if not condition:
        errors.append(f"[{rule_id}] {message}" if rule_id else message)


def collection_refs(definition: dict[str, Any]) -> dict[str, str]:
    result: dict[str, str] = {}
    for name, schema in definition.get("properties", {}).items():
        reference = (
            schema.get("items", {}).get("$ref", "")
            if isinstance(schema, dict)
            else ""
        )
        result[name] = reference.rsplit("/", 1)[-1]
    return result


def role_order(schema: dict[str, Any]) -> list[Any]:
    return [
        row.get("const")
        for row in schema.get("prefixItems", [])
        if isinstance(row, dict)
    ]


def relation_predicate(definition: dict[str, Any]) -> Any:
    for row in definition.get("allOf", []):
        value = (
            row.get("properties", {}).get("predicate", {}).get("const")
            if isinstance(row, dict)
            else None
        )
        if value is not None:
            return value
    return None


def composed_properties(definition: dict[str, Any]) -> dict[str, Any]:
    result = dict(definition.get("properties", {}))
    for row in definition.get("allOf", []):
        if isinstance(row, dict) and isinstance(row.get("properties"), dict):
            result.update(row["properties"])
    return result


def composed_required(definition: dict[str, Any]) -> set[str]:
    result = set(definition.get("required", []))
    for row in definition.get("allOf", []):
        if isinstance(row, dict) and isinstance(row.get("required"), list):
            result.update(row["required"])
    return result


def property_names(definition: Any) -> set[str]:
    if not isinstance(definition, dict):
        return set()
    result = set(definition.get("properties", {}))
    for component in definition.get("allOf", []):
        result |= property_names(component)
    return result


def registered_literals(value: Any) -> set[str]:
    result: set[str] = set()
    if isinstance(value, dict):
        constant = value.get("const")
        if isinstance(constant, str):
            result.add(constant)
        for candidate in value.get("enum", []):
            if isinstance(candidate, str):
                result.add(candidate)
        for child in value.values():
            result |= registered_literals(child)
    elif isinstance(value, list):
        for child in value:
            result |= registered_literals(child)
    return result


def composed_property_conflicts(
    definition: dict[str, Any], equal: Equal
) -> set[str]:
    seen: dict[str, Any] = {}
    conflicts: set[str] = set()
    components = [definition, *definition.get("allOf", [])]
    for component in components:
        if not isinstance(component, dict):
            continue
        for name, value in component.get("properties", {}).items():
            if name in seen and not equal(seen[name], value):
                conflicts.add(name)
            seen[name] = value
    return conflicts


def validate(
    schema: dict[str, Any],
    errors: list[str],
    profile: dict[str, Any],
    equal: Equal,
) -> None:
    policy = profile["topologyPolicy"]
    runtime_registry = profile["runtimeRegistryPolicy"]
    schema_titles = profile["schemaTitles"]
    role_sequence = profile["roleOrder"]
    projection_collections = profile["projectionCollections"]
    relation_collections = profile["relationCollections"]
    predicates_by_definition = profile["relationPredicates"]

    definitions = schema.get("$defs", {})
    properties = schema.get("properties", {})
    names = policy["definitions"]
    structural = policy["structuralCoordinates"]
    require(
        errors,
        schema.get("title") == schema_titles["topology"],
        "topology schema: title differs from the validation profile",
    )
    require(
        errors,
        not (set(policy["forbiddenRootCollections"]) & set(properties)),
        "topology schema: generic root collections are forbidden",
        "topology.root.generic",
    )
    require(
        errors,
        not (set(policy["forbiddenDefinitions"]) & set(definitions)),
        "topology schema: generic definitions are forbidden",
    )
    require(
        errors,
        properties.get(structural["lambdaRoot"], {}).get("$ref")
        == f"#/$defs/{names['closedCarrier']}",
        "topology schema: closed Lambda carrier is not authoritative",
    )
    require(
        errors,
        set(policy["rootRequired"]) <= set(schema.get("required", [])),
        "topology schema: required root coordinates are missing",
    )
    for name, definition in definitions.items():
        if isinstance(definition, dict) and definition.get("allOf"):
            require(
                errors,
                not composed_property_conflicts(definition, equal),
                f"topology schema: {name} has conflicting composed property definitions",
            )

    closed = definitions.get(names["closedCarrier"], {})
    require(
        errors,
        closed.get("properties", {})
        .get(structural["closedFlag"], {})
        .get("const")
        == policy["closedCarrier"],
        "topology schema: Lambda carrier is not closed",
    )
    rank = (
        definitions.get(names["lambdaVector"], {})
        .get("properties", {})
        .get(structural["vectorBidegree"], {})
        .get("properties", {})
        .get(structural["vectorRank"], {})
    )
    require(
        errors,
        rank.get("const") == policy["closedRank"],
        "topology schema: Lambda vector rank is not closed",
    )
    coordinates = definitions.get(names["lambdaCoordinates"], {}).get("oneOf", [])
    selector = policy["relationCoordinate"]
    relation_coordinate = next(
        (
            row
            for row in coordinates
            if row.get("properties", {})
            .get(selector["formCoordinate"], {})
            .get("const")
            == selector["formValue"]
        ),
        {},
    )
    coordinate_order = role_order(
        relation_coordinate.get("properties", {}).get(
            selector["roleOrderCoordinate"], {}
        )
    )
    require(
        errors,
        coordinate_order == role_sequence,
        "topology schema: relation coordinates must retain role-labelled S:O:P order",
    )

    projection_refs = collection_refs(definitions.get(names["projections"], {}))
    require(
        errors,
        projection_refs == projection_collections,
        "topology schema: projection families are missing or collapsed",
    )
    require(
        errors,
        set(definitions.get(names["projections"], {}).get("required", []))
        == set(projection_collections),
        "topology schema: every typed projection family must be present",
    )
    for required in projection_collections.values():
        require(
            errors,
            required in definitions,
            f"topology schema: missing projection definition {required}",
        )
    carrier_required = set(
        definitions.get(names["projectionCarrier"], {}).get("required", [])
    )
    require(
        errors,
        carrier_required == set(policy["projectionCarrierRequired"]),
        "topology schema: projection carrier collapses locator or semantic identity",
    )
    require(
        errors,
        not (
            set(policy["physicalEntryForbidden"])
            & property_names(definitions.get(names["physicalEntry"], {}))
        ),
        "topology schema: physical entry directly absorbs a forbidden coordinate",
    )
    regular_properties = composed_properties(definitions.get(names["regularFile"], {}))
    require(
        errors,
        set(policy["regularFileRequired"]) <= set(regular_properties),
        "topology schema: regular file omits entry/revision separation",
    )
    gap_required = composed_required(definitions.get(names["gap"], {}))
    require(
        errors,
        set(policy["gapRequired"]) <= gap_required,
        "topology schema: provisional gap omits registered evidence coordinates",
    )
    shoe = definitions.get(names["runtimeShoe"], {})
    shoe_properties = property_names(shoe)
    require(
        errors,
        composed_required(shoe) == set(policy["runtimeShoeRequired"]),
        "topology schema: runtime shoe identity/registration/anchor coordinates are incomplete",
    )
    require(
        errors,
        not (set(runtime_registry["forbiddenObservationFields"]) & shoe_properties),
        "topology schema: static runtime shoe freezes handler availability",
        "topology.runtime.availability-separation",
    )
    availability = definitions.get(names["availabilityObservation"], {})
    require(
        errors,
        composed_required(availability) == set(policy["availabilityObservationRequired"]),
        "topology schema: runtime availability observation omits fresh attempt/shoe/handler/state/evidence coordinates",
    )
    availability_properties = composed_properties(availability)
    require(
        errors,
        availability_properties.get(structural["availabilityTime"], {}).get("format")
        == policy["availabilityTimeFormat"],
        "topology schema: runtime availability observation has no explicit time",
    )

    relation_refs = collection_refs(definitions.get(names["relations"], {}))
    require(
        errors,
        relation_refs == relation_collections,
        "topology schema: relation families are missing or collapsed",
    )
    require(
        errors,
        set(definitions.get(names["relations"], {}).get("required", []))
        == set(relation_collections),
        "topology schema: every typed relation family must be present",
    )
    relation_order = role_order(
        definitions.get(names["relationCarrier"], {})
        .get("properties", {})
        .get(selector["roleOrderCoordinate"], {})
    )
    require(
        errors,
        relation_order == role_sequence,
        "topology schema: typed relations must retain role-labelled S:O:P order",
    )
    for definition, predicate in predicates_by_definition.items():
        require(
            errors,
            relation_predicate(definitions.get(definition, {})) == predicate,
            f"topology schema: {definition} lacks its canonical predicate",
        )
    predicates = [
        relation_predicate(definitions.get(name, {}))
        for name in predicates_by_definition
    ]
    require(
        errors,
        len(predicates) == len(set(predicates)),
        "topology schema: distinct arrow families share a predicate identity",
    )

    location = definitions.get(names["location"], {})
    require(
        errors,
        set(location.get("required", [])) == set(policy["locationRequired"]),
        "topology schema: location substrate does not preserve twin fields plus located-at",
    )
    normalized = location.get("properties", {}).get(
        structural["normalizedLocation"], {}
    )
    require(
        errors,
        normalized.get("format") == policy["normalizedLocationFormat"]
        and "pattern" not in normalized,
        "topology schema: normalized location is constrained to one scheme",
        "topology.location.uri",
    )
    locator_predicate = predicates_by_definition[policy["locationPredicateRelation"]]
    require(
        errors,
        location.get("properties", {})
        .get(structural["locatorPredicate"], {})
        .get("const")
        == locator_predicate,
        "topology schema: canonical located-at predicate is missing",
    )

    physical = definitions.get(names["physicalIdentity"], {})
    require(
        errors,
        set(physical.get("required", [])) == set(policy["physicalIdentityRequired"]),
        "topology schema: FD/inode identity is not scoped physical evidence",
    )
    require(
        errors,
        not (
            set(policy["physicalIdentityForbidden"])
            & set(physical.get("properties", {}))
        ),
        "topology schema: transient observation coordinate escaped as identity",
    )
    revision = definitions.get(names["contentRevision"], {})
    revision_properties = revision.get("properties", {})
    observation = revision_properties.get(
        structural["revisionObservation"], {}
    ).get("properties", {})
    require(
        errors,
        revision_properties.get(structural["revisionComplete"], {}).get("const")
        == policy["revisionComplete"],
        "topology schema: incomplete digest can certify a revision",
        "topology.revision.complete",
    )
    for coordinate, expected in policy["revisionObservation"].items():
        require(
            errors,
            observation.get(coordinate, {}).get("const") == expected,
            f"topology schema: revision observation coordinate {coordinate!r} differs from the profile",
        )
