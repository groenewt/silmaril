"""Local-chart, transition, obstruction, and seam laws for an Atlas."""

from __future__ import annotations

from typing import Any, Mapping

from morphism_contracts.law.common import require


def validate(
    profile: Mapping[str, Any], scene: Mapping[str, Any], errors: list[str]
) -> None:
    policy = profile["atlasPolicy"]
    atlas = scene.get("atlas", {})
    for coordinate, expected in policy["root"].items():
        require(
            errors,
            atlas.get(coordinate) == expected,
            f"scene: Atlas policy coordinate {coordinate!r} differs from the validation profile",
            "scene.atlas.root",
        )
    chart_rows = atlas.get("charts", [])
    charts = {
        row.get("identity"): row for row in chart_rows if isinstance(row, dict)
    }
    require(
        errors,
        len(charts) == len(chart_rows)
        and len(charts) >= policy["chart"]["minimum"],
        "scene: Atlas charts must be distinct local scenes",
    )
    for identity, chart in charts.items():
        require(
            errors,
            chart.get("localOnly") == policy["chart"]["localOnly"],
            f"scene: chart {identity!r} claims global completeness",
        )
        require(
            errors,
            not (set(policy["chart"]["forbiddenCoordinates"]) & set(chart)),
            f"scene: chart {identity!r} contains a forbidden universal coordinate",
        )
        missing = [
            coordinate
            for coordinate in policy["chart"]["requiredNonempty"]
            if not chart.get(coordinate)
        ]
        require(
            errors,
            not missing,
            f"scene: chart {identity!r} lacks registered nonempty coordinates {missing}",
        )

    transition_rows = atlas.get("transitions", [])
    transitions = {
        row.get("identity"): row
        for row in transition_rows
        if isinstance(row, dict)
    }
    require(
        errors,
        len(transitions) == len(transition_rows) and bool(transitions),
        "scene: transition map identities must be unique",
    )
    for identity, transition in transitions.items():
        source = transition.get("sourceChart")
        target = transition.get("targetChart")
        inverse = transitions.get(transition.get("inverse"), {})
        require(
            errors,
            source in charts and target in charts and source != target,
            f"scene: transition {identity!r} has invalid chart endpoints",
        )
        if policy["transition"]["inverseExact"]:
            require(
                errors,
                inverse.get("inverse") == identity
                and inverse.get("sourceChart") == target
                and inverse.get("targetChart") == source,
                f"scene: transition {identity!r} has no exact return map",
            )
        if policy["transition"]["roundTripAgreement"]:
            require(
                errors,
                inverse.get("roundTrip") == transition.get("roundTrip"),
                f"scene: transition {identity!r} disagrees with inverse round-trip law",
            )

    obstruction_pairs = {
        (row.get("sourceTransition"), row.get("returnTransition"))
        for row in atlas.get("obstructions", [])
        if isinstance(row, dict)
    }
    for identity, transition in transitions.items():
        pair = (identity, transition.get("inverse"))
        reverse = (transition.get("inverse"), identity)
        if (
            transition.get("roundTrip")
            == policy["transition"]["obstructionRequired"]
        ):
            require(
                errors,
                pair in obstruction_pairs or reverse in obstruction_pairs,
                f"scene: transition {identity!r} promises an obstruction but emits none",
                "scene.atlas.obstruction",
            )
        else:
            require(
                errors,
                transition.get("roundTrip")
                == policy["transition"]["roundTripCommutes"],
                f"scene: transition {identity!r} has an unknown round-trip verdict",
            )
    for seam in atlas.get("seams", []):
        if policy["transition"]["seamReferenceRequired"]:
            require(
                errors,
                seam.get("transition") in transitions,
                f"scene: seam {seam.get('identity')!r} references no transition",
            )
