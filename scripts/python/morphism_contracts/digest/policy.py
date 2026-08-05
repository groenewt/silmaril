"""Host-capability preflight for a schema-owned digest policy."""

from __future__ import annotations

import hashlib
import re
from typing import Any


def capability_errors(policy: Any) -> list[str]:
    """Report realization gaps without choosing campaign policy in Python."""
    errors: list[str] = []
    if not isinstance(policy, dict):
        return ["[digest.policy] digestPolicy must be an object"]
    algorithm = policy.get("algorithm")
    encoding = policy.get("encoding")
    try:
        if not isinstance(algorithm, str) or not algorithm:
            raise ValueError(algorithm)
        hashlib.new(algorithm).hexdigest()
    except (TypeError, ValueError):
        errors.append(
            f"[digest.algorithm.supported] unsupported digest algorithm {algorithm!r}"
        )
    try:
        if not isinstance(encoding, str) or not encoding:
            raise LookupError(encoding)
        "".encode(encoding)
    except (LookupError, TypeError):
        errors.append(
            f"[digest.encoding.supported] unsupported digest encoding {encoding!r}"
        )
    canonical_policy = policy.get("canonicalJson")
    separators = (
        canonical_policy.get("separators") if isinstance(canonical_policy, dict) else None
    )
    if not (
        isinstance(canonical_policy, dict)
        and isinstance(canonical_policy.get("ensureAscii"), bool)
        and isinstance(canonical_policy.get("objectKeyOrder"), str)
        and bool(canonical_policy.get("objectKeyOrder"))
        and isinstance(separators, list)
        and len(separators) == 2
        and all(isinstance(separator, str) for separator in separators)
    ):
        errors.append(
            "[digest.canonical-json.supported] unsupported canonical JSON policy"
        )
    if not isinstance(policy.get("artifactOrder"), str) or not isinstance(
        policy.get("preimage"), str
    ):
        errors.append(
            "[digest.preimage.supported] digest preimage/order policy must be registered strings"
        )
    pattern = policy.get("hexPattern")
    try:
        if not isinstance(pattern, str) or not pattern:
            raise re.error("empty pattern")
        re.compile(pattern)
    except re.error:
        errors.append("[digest.output.pattern] unsupported digest output pattern")
    return errors
