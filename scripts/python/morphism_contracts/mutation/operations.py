"""Pure data-declared mutation operations for adversarial contract probes."""

from __future__ import annotations

import copy
from collections.abc import Callable
from typing import Any


Equal = Callable[[Any, Any], bool]


def select_component(value: Any, component: Any, equal: Equal) -> Any:
    if isinstance(component, str):
        if not isinstance(value, dict) or component not in value:
            raise ValueError(f"path coordinate {component!r} is absent")
        return value[component]
    if not isinstance(value, list) or not isinstance(component, dict):
        raise ValueError(f"selector {component!r} requires an array")
    if "present" in component:
        matches = [
            row
            for row in value
            if isinstance(row, dict) and component["present"] in row
        ]
    else:
        matches = [
            row
            for row in value
            if isinstance(row, dict)
            and equal(row.get(component["field"]), component["equals"])
        ]
    if len(matches) != 1:
        raise ValueError(f"path selector {component!r} resolved {len(matches)} values")
    return matches[0]


def resolve_path(value: Any, path: list[Any], equal: Equal) -> Any:
    current = value
    for component in path:
        current = select_component(current, component, equal)
    return current


def assign_path(value: Any, path: list[Any], replacement: Any, equal: Equal) -> None:
    parent = resolve_path(value, path[:-1], equal) if len(path) > 1 else value
    leaf = path[-1]
    if not isinstance(parent, dict) or not isinstance(leaf, str):
        raise ValueError("set/fill mutation requires a final object coordinate")
    parent[leaf] = replacement


def set_value(document: dict[str, Any], test: dict[str, Any], equal: Equal) -> None:
    operation = test["operation"]
    assign_path(document, test["path"], copy.deepcopy(operation["value"]), equal)


def fill_preserving_length(
    document: dict[str, Any], test: dict[str, Any], equal: Equal
) -> None:
    operation = test["operation"]
    current = resolve_path(document, test["path"], equal)
    if not isinstance(current, str):
        raise ValueError("fill-preserving-length requires a string target")
    assign_path(
        document,
        test["path"],
        operation["fill"] * len(current),
        equal,
    )


def remove_matching(
    document: dict[str, Any], test: dict[str, Any], equal: Equal
) -> None:
    operation = test["operation"]
    current = resolve_path(document, test["path"], equal)
    if not isinstance(current, list):
        raise ValueError("remove-matching requires an array target")
    retained = [
        row
        for row in current
        if not (
            isinstance(row, dict)
            and equal(row.get(operation["field"]), operation["equals"])
        )
    ]
    if len(retained) == len(current):
        raise ValueError("remove-matching selected no values")
    current[:] = retained


def append_copy(
    document: dict[str, Any], test: dict[str, Any], equal: Equal
) -> None:
    operation = test["operation"]
    current = resolve_path(document, test["path"], equal)
    if not isinstance(current, list):
        raise ValueError("append-copy requires an array target")
    matches = [
        row
        for row in current
        if isinstance(row, dict)
        and equal(row.get(operation["field"]), operation["equals"])
    ]
    if len(matches) != 1:
        raise ValueError(f"append-copy selector resolved {len(matches)} values")
    appended = copy.deepcopy(matches[0])
    appended.update(copy.deepcopy(operation["overrides"]))
    current.append(appended)
