"""Strict JSON decoding and registered-coordinate uniqueness checks."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class DuplicateObjectKey(ValueError):
    """Raised before a JSON object can collapse two lexical coordinates."""


def object_without_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateObjectKey(
                f"[json.object-key.unique] duplicate JSON object key {key!r}"
            )
        result[key] = value
    return result


def decode_json(text: str, label: str) -> Any:
    try:
        return json.loads(text, object_pairs_hook=object_without_duplicate_keys)
    except (DuplicateObjectKey, json.JSONDecodeError) as error:
        raise ValueError(f"cannot read JSON {label}: {error}") from error


def read_json_file(path: Path, repository: Path) -> Any:
    try:
        return decode_json(path.read_text(encoding="utf-8"), str(path.relative_to(repository)))
    except OSError as error:
        raise ValueError(f"cannot read JSON {path.relative_to(repository)}: {error}") from error


def registered_path(root: Any, path: Any) -> Any:
    current = root
    if not isinstance(path, list) or not path:
        raise ValueError("uniqueBy path must be a non-empty array")
    for coordinate in path:
        if (
            not isinstance(coordinate, str)
            or not isinstance(current, dict)
            or coordinate not in current
        ):
            raise ValueError(f"uniqueBy path coordinate {coordinate!r} is absent")
        current = current[coordinate]
    return current


def unique_by_errors(targets: dict[str, Any], rules: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(rules, dict) or not rules:
        return ["[profile.unique-by.registry] uniqueBy must be a non-empty registered table"]
    for rule_id in sorted(rules):
        rule = rules[rule_id]
        if not isinstance(rule, dict):
            errors.append(f"[{rule_id}] uniqueBy rule must be an object")
            continue
        target_name = rule.get("target")
        fields = rule.get("fields")
        try:
            values = registered_path(targets.get(target_name), rule.get("path"))
        except ValueError as error:
            errors.append(f"[{rule_id}] {error}")
            continue
        if (
            not isinstance(values, list)
            or not isinstance(fields, list)
            or not fields
            or not all(isinstance(field, str) for field in fields)
        ):
            errors.append(
                f"[{rule_id}] uniqueBy requires an array target and non-empty string fields"
            )
            continue
        seen: set[tuple[Any, ...]] = set()
        for offset, value in enumerate(values):
            if not isinstance(value, dict):
                errors.append(f"[{rule_id}] uniqueBy row {offset} is not an object")
                continue
            key = tuple(value.get(field) for field in fields)
            if any(component is None for component in key):
                errors.append(f"[{rule_id}] uniqueBy row {offset} omits one of {fields!r}")
            elif key in seen:
                errors.append(f"[{rule_id}] duplicate uniqueBy coordinates {key!r}")
            else:
                seen.add(key)
    return errors
