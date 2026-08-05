"""Deterministic JSON-Schema, RFC 3986, and RFC 3339 combinators."""

from __future__ import annotations

import datetime
import hashlib
import json
import re
from typing import Any, Callable
from urllib.parse import urlsplit


def diagnostic(rule_id: str, message: str) -> str:
    return f"[{rule_id}] {message}"


def json_type_matches(value: Any, expected: str) -> bool:
    if expected == "null":
        return value is None
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "string":
        return isinstance(value, str)
    if expected == "array":
        return isinstance(value, list)
    if expected == "object":
        return isinstance(value, dict)
    return False


URI_SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*$")
INVALID_PERCENT_ESCAPE = re.compile(r"%(?![0-9A-Fa-f]{2})")
URI_AUTHORITY = re.compile(
    r"^(?:[A-Za-z0-9._~!$&'()*+,;=:@\[\]-]|%[0-9A-Fa-f]{2})*$"
)
URI_PATH = re.compile(r"^(?:[A-Za-z0-9._~!$&'()*+,;=:@/\-]|%[0-9A-Fa-f]{2})*$")
URI_QUERY_OR_FRAGMENT = re.compile(
    r"^(?:[A-Za-z0-9._~!$&'()*+,;=:@/?\-]|%[0-9A-Fa-f]{2})*$"
)
RFC3339_DATE_TIME = re.compile(
    r"^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})"
    r"(?:\.(\d+))?(Z|([+-])(\d{2}):(\d{2}))$"
)


def valid_uri_reference(value: str, absolute: bool) -> bool:
    """Focused RFC 3986 URI-reference check, including strict percent triplets."""
    try:
        value.encode("ascii")
        parsed = urlsplit(value)
    except (UnicodeEncodeError, ValueError):
        return False
    if INVALID_PERCENT_ESCAPE.search(value) or re.search(r'[\x00-\x20<>"{}|\\^`]', value):
        return False
    if parsed.scheme and URI_SCHEME.fullmatch(parsed.scheme) is None:
        return False
    if absolute and not parsed.scheme:
        return False
    if not parsed.scheme and value.startswith("//") and not parsed.netloc:
        return False
    if (
        URI_AUTHORITY.fullmatch(parsed.netloc) is None
        or URI_PATH.fullmatch(parsed.path) is None
        or URI_QUERY_OR_FRAGMENT.fullmatch(parsed.query) is None
        or URI_QUERY_OR_FRAGMENT.fullmatch(parsed.fragment) is None
    ):
        return False
    return True


def valid_rfc3339_date_time(value: str) -> bool:
    """Validate the RFC 3339 date-time production, including leap seconds."""
    match = RFC3339_DATE_TIME.fullmatch(value)
    if match is None:
        return False
    year, month, day, hour, minute, second = (
        int(match.group(index)) for index in range(1, 7)
    )
    offset_hour = int(match.group(10)) if match.group(10) is not None else 0
    offset_minute = int(match.group(11)) if match.group(11) is not None else 0
    if (
        year == 0
        or hour > 23
        or minute > 59
        or second > 60
        or (second == 60 and minute != 59)
        or offset_hour > 23
        or offset_minute > 59
    ):
        return False
    try:
        datetime.datetime(year, month, day, hour, minute, min(second, 59))
    except ValueError:
        return False
    return True


def uri_error(value: str) -> str | None:
    if not valid_uri_reference(value, absolute=True):
        return diagnostic("schema.format.uri", "is not an RFC 3986 absolute URI")
    return None


def uri_reference_error(value: str) -> str | None:
    if not valid_uri_reference(value, absolute=False):
        return diagnostic("schema.format.uri-reference", "is not an RFC 3986 URI reference")
    return None


def date_time_error(value: str) -> str | None:
    if not valid_rfc3339_date_time(value):
        return diagnostic("schema.format.date-time", "is not an RFC 3339 date-time")
    return None


def pointer(root: Any, fragment: str) -> Any:
    current = root
    if not fragment:
        return current
    if not fragment.startswith("/"):
        raise KeyError(fragment)
    for raw in fragment[1:].split("/"):
        token = raw.replace("~1", "/").replace("~0", "~")
        current = current[int(token)] if isinstance(current, list) else current[token]
    return current


def anchor(root: Any, name: str) -> Any:
    if isinstance(root, dict):
        if root.get("$anchor") == name:
            return root
        for value in root.values():
            try:
                return anchor(value, name)
            except KeyError:
                pass
    elif isinstance(root, list):
        for value in root:
            try:
                return anchor(value, name)
            except KeyError:
                pass
    raise KeyError(name)


def resolve_reference(
    reference: str,
    root: dict[str, Any],
    registry: dict[str, dict[str, Any]],
) -> tuple[dict[str, Any], dict[str, Any]]:
    identity, separator, fragment = reference.partition("#")
    target_root = root if not identity else registry[identity]
    if not separator or not fragment:
        return target_root, target_root
    target = pointer(target_root, fragment) if fragment.startswith("/") else anchor(
        target_root, fragment
    )
    return target, target_root


def evaluated_properties(
    schema: Any,
    registry: dict[str, dict[str, Any]],
    root: dict[str, Any],
    seen: set[tuple[int, str]] | None = None,
) -> set[str]:
    if not isinstance(schema, dict):
        return set()
    visited = seen if seen is not None else set()
    marker = (id(root), str(schema.get("$ref", id(schema))))
    if marker in visited:
        return set()
    visited.add(marker)
    result = set(schema.get("properties", {}))
    reference = schema.get("$ref")
    if isinstance(reference, str):
        try:
            target, target_root = resolve_reference(reference, root, registry)
            result |= evaluated_properties(target, registry, target_root, visited)
        except (KeyError, TypeError, ValueError):
            pass
    for candidate in schema.get("allOf", []):
        result |= evaluated_properties(candidate, registry, root, visited)
    return result


class Combinators:
    """Pure schema projections closed over one registered digest policy."""

    def __init__(
        self,
        digest_policy: dict[str, Any],
        format_projection: Callable[[str, str], str | None],
    ) -> None:
        self.digest_policy = digest_policy
        self.format_projection = format_projection

    def canonical(self, value: Any) -> bytes:
        policy = self.digest_policy["canonicalJson"]
        return json.dumps(
            value,
            ensure_ascii=policy["ensureAscii"],
            separators=tuple(policy["separators"]),
            sort_keys=policy["objectKeyOrder"] == "lexicographic",
        ).encode(self.digest_policy["encoding"])

    def digest(self, value: Any) -> str:
        observed = hashlib.new(
            self.digest_policy["algorithm"], self.canonical(value)
        ).hexdigest()
        if re.fullmatch(self.digest_policy["hexPattern"], observed) is None:
            raise ValueError(
                "[digest.output.pattern] digest output differs from the registered pattern"
            )
        return observed

    def exact_equal(self, left: Any, right: Any) -> bool:
        return self.canonical(left) == self.canonical(right)

    def errors(
        self,
        value: Any,
        schema: Any,
        registry: dict[str, dict[str, Any]],
        root: dict[str, Any],
        location: str,
    ) -> list[str]:
        if schema is True:
            return []
        if schema is False:
            return [f"{location}: forbidden by schema"]
        if not isinstance(schema, dict):
            return [f"{location}: invalid schema projection"]

        errors: list[str] = []
        reference = schema.get("$ref")
        if isinstance(reference, str):
            try:
                target, target_root = resolve_reference(reference, root, registry)
            except (KeyError, TypeError, ValueError):
                return [f"{location}: unresolved schema reference {reference!r}"]
            errors.extend(self.errors(value, target, registry, target_root, location))

        for candidate in schema.get("allOf", []):
            errors.extend(self.errors(value, candidate, registry, root, location))

        alternatives = schema.get("oneOf")
        if isinstance(alternatives, list):
            accepted = sum(
                not self.errors(value, candidate, registry, root, location)
                for candidate in alternatives
            )
            if accepted != 1:
                errors.append(
                    f"{location}: expected exactly one schema alternative, accepted {accepted}"
                )

        if "const" in schema and not self.exact_equal(value, schema["const"]):
            errors.append(
                diagnostic("schema.const", f"{location}: differs from registered const")
            )
        if "enum" in schema and not any(
            self.exact_equal(value, candidate) for candidate in schema["enum"]
        ):
            errors.append(f"{location}: is outside registered enum")

        declared_type = schema.get("type")
        expected_types = (
            declared_type
            if isinstance(declared_type, list)
            else [declared_type]
            if declared_type
            else []
        )
        if expected_types and not any(
            json_type_matches(value, expected) for expected in expected_types
        ):
            return errors + [
                f"{location}: expected JSON type {'|'.join(expected_types)}"
            ]

        if isinstance(value, dict):
            for name in schema.get("required", []):
                if name not in value:
                    errors.append(f"{location}: missing required coordinate {name!r}")
            properties = schema.get("properties", {})
            for name, child in value.items():
                if name in properties:
                    errors.extend(
                        self.errors(
                            child, properties[name], registry, root, f"{location}/{name}"
                        )
                    )
                elif schema.get("additionalProperties") is False:
                    errors.append(f"{location}: unregistered coordinate {name!r}")
                elif isinstance(schema.get("additionalProperties"), dict):
                    errors.extend(
                        self.errors(
                            child,
                            schema["additionalProperties"],
                            registry,
                            root,
                            f"{location}/{name}",
                        )
                    )
            minimum_properties = schema.get("minProperties")
            if isinstance(minimum_properties, int) and len(value) < minimum_properties:
                errors.append(
                    f"{location}: has fewer than {minimum_properties} coordinates"
                )
            if schema.get("unevaluatedProperties") is False:
                unregistered = set(value) - evaluated_properties(schema, registry, root)
                for name in sorted(unregistered):
                    errors.append(f"{location}: unevaluated coordinate {name!r}")

        if isinstance(value, list):
            minimum_items = schema.get("minItems")
            maximum_items = schema.get("maxItems")
            if isinstance(minimum_items, int) and len(value) < minimum_items:
                errors.append(f"{location}: has fewer than {minimum_items} values")
            if isinstance(maximum_items, int) and len(value) > maximum_items:
                errors.append(f"{location}: has more than {maximum_items} values")
            if schema.get("uniqueItems") is True:
                encoded = [self.canonical(item) for item in value]
                if len(encoded) != len(set(encoded)):
                    errors.append(f"{location}: contains duplicate values")
            prefixes = schema.get("prefixItems", [])
            for index, child_schema in enumerate(prefixes):
                if index < len(value):
                    errors.extend(
                        self.errors(
                            value[index],
                            child_schema,
                            registry,
                            root,
                            f"{location}/{index}",
                        )
                    )
            item_schema = schema.get("items")
            if item_schema is not None:
                start = len(prefixes) if prefixes else 0
                for index, child in enumerate(value[start:], start=start):
                    errors.extend(
                        self.errors(
                            child, item_schema, registry, root, f"{location}/{index}"
                        )
                    )

        if isinstance(value, str):
            minimum_length = schema.get("minLength")
            if isinstance(minimum_length, int) and len(value) < minimum_length:
                errors.append(f"{location}: is shorter than {minimum_length}")
            pattern = schema.get("pattern")
            if isinstance(pattern, str) and re.search(pattern, value) is None:
                errors.append(f"{location}: does not match registered pattern")
            declared_format = schema.get("format")
            if isinstance(declared_format, str):
                failure = self.format_projection(declared_format, value)
                if failure:
                    errors.append(f"{failure}: {location}")

        minimum = schema.get("minimum")
        if (
            isinstance(minimum, (int, float))
            and isinstance(value, (int, float))
            and not isinstance(value, bool)
            and value < minimum
        ):
            errors.append(f"{location}: is below registered minimum")
        return errors
