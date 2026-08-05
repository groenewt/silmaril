"""Shared diagnostic combinators for profile-projected contract laws."""

from __future__ import annotations

from typing import Any, Callable


Digest = Callable[[Any], str]


def diagnostic(rule_id: str, message: str) -> str:
    return f"[{rule_id}] {message}"


def require(
    errors: list[str], condition: bool, message: str, rule_id: str | None = None
) -> None:
    if not condition:
        errors.append(diagnostic(rule_id, message) if rule_id else message)
