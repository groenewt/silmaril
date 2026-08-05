"""Anchor-member DAG and delivery-gateway laws for a morphism scene."""

from __future__ import annotations

from typing import Any, Mapping

from morphism_contracts.law.common import Digest, require


def member_content(
    profile: Mapping[str, Any], member: Mapping[str, Any]
) -> dict[str, Any]:
    coordinates = profile["anchorPolicy"]["memberDigestCoordinates"]
    return {key: member.get(key) for key in coordinates}


def module_content(
    profile: Mapping[str, Any], module: Mapping[str, Any]
) -> dict[str, Any]:
    coordinates = profile["anchorPolicy"]["moduleDigestCoordinates"]
    return {key: module.get(key) for key in coordinates}


def dependency_closure(
    identity: str, members: Mapping[str, Mapping[str, Any]]
) -> set[str]:
    result: set[str] = set()
    stack = list(members.get(identity, {}).get("dependsOn", []))
    while stack:
        item = stack.pop()
        if item in result:
            continue
        result.add(item)
        stack.extend(members.get(item, {}).get("dependsOn", []))
    return result


def acyclic(members: Mapping[str, Mapping[str, Any]]) -> bool:
    temporary: set[str] = set()
    permanent: set[str] = set()

    def visit(identity: str) -> bool:
        if identity in permanent:
            return True
        if identity in temporary:
            return False
        temporary.add(identity)
        for dependency in members.get(identity, {}).get("dependsOn", []):
            if dependency in members and not visit(dependency):
                return False
        temporary.remove(identity)
        permanent.add(identity)
        return True

    return all(visit(identity) for identity in members)


def validate(
    profile: Mapping[str, Any],
    digest: Digest,
    scene: Mapping[str, Any],
    errors: list[str],
) -> None:
    policy = profile["anchorPolicy"]
    delivery_capabilities = {
        row["id"]: row["capability"] for row in profile["deliveries"]
    }
    module = scene.get("anchorModule", {})
    members_list = module.get("members", [])
    members = {
        row.get("identity"): row for row in members_list if isinstance(row, dict)
    }
    require(
        errors,
        len(members) == len(members_list) and bool(members),
        "scene: anchor member identities must be nonempty and unique",
    )
    for identity, member in members.items():
        require(
            errors,
            member.get("revisionDigest") == digest(member_content(profile, member)),
            f"scene: anchor member {identity!r} is not content-addressed",
            "scene.anchor.member-digest",
        )
        unknown = set(member.get("dependsOn", [])) - set(members)
        require(
            errors,
            not unknown,
            f"scene: anchor member {identity!r} has undeclared dependencies {sorted(unknown)}",
        )
    require(
        errors,
        acyclic(members),
        "scene: anchor member graph has an undeclared cycle",
    )
    require(
        errors,
        module.get("moduleRevisionDigest") == digest(module_content(profile, module)),
        "scene: anchor module revision does not bind the member DAG",
    )
    require(
        errors,
        module.get("declaredExternalDependencies")
        == policy["declaredExternalDependencies"],
        "scene: unexpected external dependency entered the anchor module",
    )

    plans = scene.get("gatewayPlans", [])
    plan_by_capability = {
        row.get("capability"): row for row in plans if isinstance(row, dict)
    }
    require(
        errors,
        set(plan_by_capability) == set(delivery_capabilities.values()),
        "scene: gateway plans do not cover the registered delivery capabilities",
    )
    for capability, plan in plan_by_capability.items():
        renderer = plan.get("renderer")
        member = members.get(renderer, {})
        require(
            errors,
            plan.get("anchorModule") == module.get("identity"),
            f"scene: gateway plan {capability!r} selects another anchor module",
        )
        require(
            errors,
            renderer in members,
            f"scene: gateway plan {capability!r} selects a hidden renderer",
        )
        require(
            errors,
            capability in member.get("capabilities", []),
            f"scene: renderer {renderer!r} does not declare capability {capability!r}",
        )
        require(
            errors,
            plan.get("rendererRevisionDigest") == member.get("revisionDigest"),
            f"scene: gateway plan {capability!r} does not bind renderer revision",
        )
        order = plan.get("dependencyOrder", [])
        required = dependency_closure(renderer, members) | {renderer}
        require(
            errors,
            set(order) == required and len(order) == len(required),
            f"scene: gateway plan {capability!r} has an incomplete dependency order",
        )
        positions = {identity: index for index, identity in enumerate(order)}
        ordered = all(
            positions[dependency] < positions[identity]
            for identity in order
            for dependency in members.get(identity, {}).get("dependsOn", [])
        )
        require(
            errors,
            ordered,
            f"scene: gateway plan {capability!r} is not dependency ordered",
        )
        require(
            errors,
            plan.get("hiddenDiscovery") == policy["hiddenDiscovery"],
            f"scene: gateway plan {capability!r} differs from the registered discovery boundary",
            "scene.gateway.discovery",
        )
