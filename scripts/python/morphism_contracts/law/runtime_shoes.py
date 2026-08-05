"""Open-world runtime-shoe registry laws for a morphism scene."""

from __future__ import annotations

from typing import Any, Mapping

from morphism_contracts.law.common import require


def validate(
    profile: Mapping[str, Any], scene: Mapping[str, Any], errors: list[str]
) -> None:
    policy = profile["runtimeRegistryPolicy"]
    required = {
        row["canonicalName"]: (
            row["identity"],
            row["anchorMember"],
            row["capability"],
        )
        for row in profile["runtimeShoes"]
    }
    registry = scene.get("runtimeShoes", {})
    for coordinate, expected in policy["registry"].items():
        require(
            errors,
            registry.get(coordinate) == expected,
            f"scene: runtime registry coordinate {coordinate!r} differs from the validation profile",
            "scene.runtime.registry",
        )

    shoes_list = registry.get("shoes", [])
    shoes = {
        row.get("canonicalName"): row
        for row in shoes_list
        if isinstance(row, dict)
    }
    identities = [
        row.get("identity") for row in shoes_list if isinstance(row, dict)
    ]
    require(
        errors,
        len(shoes) == len(shoes_list),
        "scene: runtime shoe names are empty or duplicated",
    )
    require(
        errors,
        len(identities) == len(set(identities)),
        "scene: runtime shoe identities are duplicated",
    )
    require(
        errors,
        set(required) <= set(shoes),
        f"scene: named runtime shoes were erased {sorted(set(required) - set(shoes))}",
        "scene.runtime.required-shoes",
    )

    anchor_members = {
        row.get("identity"): row
        for row in scene.get("anchorModule", {}).get("members", [])
        if isinstance(row, dict)
    }
    for name, (identity, anchor_member, capability) in required.items():
        shoe = shoes.get(name, {})
        require(
            errors,
            shoe.get("identity") == identity,
            f"scene: {name} runtime shoe has the wrong identity",
        )
        require(
            errors,
            shoe.get("registration") == policy["registeredState"],
            f"scene: {name} runtime shoe is not registered",
        )
        require(
            errors,
            shoe.get("anchorMember") == anchor_member
            and anchor_member in anchor_members,
            f"scene: {name} runtime shoe has no explicit anchor member",
        )
        require(
            errors,
            capability
            in anchor_members.get(anchor_member, {}).get("capabilities", []),
            f"scene: {name} anchor member lacks its shoe capability",
        )

    provisional = [
        row
        for row in shoes_list
        if isinstance(row, dict)
        and row.get("registration") == policy["provisionalState"]
    ]
    require(
        errors,
        len(provisional) >= policy["minimumProvisional"],
        "scene: too few provisional future runtime shoes remain",
    )
    for shoe in provisional:
        anchor_member = shoe.get("anchorMember")
        require(
            errors,
            anchor_member in anchor_members,
            f"scene: provisional runtime shoe {shoe.get('identity')!r} has no anchor member",
        )
    for shoe in shoes_list:
        if isinstance(shoe, dict):
            require(
                errors,
                not (set(policy["forbiddenObservationFields"]) & set(shoe)),
                f"scene: runtime shoe {shoe.get('identity')!r} freezes per-observation availability",
                "scene.runtime.availability-separation",
            )
