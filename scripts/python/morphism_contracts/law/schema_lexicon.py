"""Scene-schema and naming-lexicon laws."""

from __future__ import annotations

from typing import Any, Mapping

from morphism_contracts.law.common import require
from morphism_contracts.law.topology import registered_literals


def validate_schema(
    profile: Mapping[str, Any], schema: Mapping[str, Any], errors: list[str]
) -> None:
    policy = profile["scenePolicy"]
    required = set(schema.get("required", []))
    require(
        errors,
        schema.get("title") == profile["schemaTitles"]["scene"],
        "scene schema: title differs from the validation profile",
    )
    require(
        errors,
        set(policy["sceneSchemaRequired"]) <= required,
        "scene schema: registered cross-substrate contracts must be required",
    )
    literals = {value.lower() for value in registered_literals(schema)}
    for row in profile["runtimeShoes"]:
        runtime_name = row["canonicalName"]
        require(
            errors,
            runtime_name.lower() not in literals,
            f"scene schema: runtime shoe {runtime_name!r} is frozen as a universal chart",
        )
    location = (
        schema.get("$defs", {})
        .get(policy["locationSourceDefinition"], {})
        .get("properties", {})
        .get(policy["locationCoordinate"], {})
    )
    expected = (
        f"{profile['artifactIds']['topology']}#{policy['locationSchemaAnchor']}"
    )
    require(
        errors,
        location.get("$ref") == expected,
        "scene schema: roots do not use the scheme-dispatched location substrate",
    )


def validate_lexicon(
    profile: Mapping[str, Any], lexicon: Mapping[str, Any], errors: list[str]
) -> None:
    policy = profile["lexiconPolicy"]
    lexeme_classes = set(profile["lexemeClasses"])
    required_canonical = set(profile["requiredCanonicalNames"])
    required_literals = set(profile["requiredToolLiterals"])
    classes = lexicon.get("classes", [])
    require(
        errors,
        set(classes) == lexeme_classes and len(classes) == len(lexeme_classes),
        "lexicon: classes must be the nine registered classes",
    )
    require(
        errors,
        lexicon.get("unknown") == policy["unknown"],
        "lexicon: unknown meanings differ from the validation profile",
    )
    require(
        errors,
        lexicon.get("normalization") == policy["normalization"],
        "lexicon: normalization policy differs from the validation profile",
    )
    entries = lexicon.get("entries", [])
    by_spelling = {
        row.get("spelling"): row for row in entries if isinstance(row, dict)
    }
    require(
        errors,
        len(by_spelling) == len(entries),
        "lexicon: duplicate spelling registration",
    )
    require(
        errors,
        required_canonical <= set(by_spelling),
        "lexicon: required canonical names are missing",
    )
    require(
        errors,
        required_literals <= set(by_spelling),
        "lexicon: required tool literals are missing",
    )
    for spelling, expected in profile["requiredSemanticExpansions"].items():
        row = by_spelling.get(spelling, {})
        projection = row.get("semanticProjection", {})
        observed = {
            "canonical": row.get("canonical"),
            "class": row.get("class"),
            "contexts": row.get("contexts"),
            "identity": projection.get("identity"),
            "kind": projection.get("kind"),
            "scalaCoordinate": projection.get("scalaCoordinate"),
            "segments": projection.get("segments"),
        }
        require(
            errors,
            observed == expected
            and row.get("rewriteEligible") is True
            and row.get("canonical") == ".".join(projection.get("segments", [])),
            f"lexicon: semantic expansion {spelling!r} differs from its registered component chain",
        )
    for spelling in required_canonical:
        canonical_value = by_spelling.get(spelling, {}).get("canonical")
        if policy["requiredCanonicalTransform"] == "identity":
            require(
                errors,
                canonical_value == spelling,
                f"lexicon: {spelling} must preserve exact spelling",
            )
        else:
            require(
                errors,
                canonical_value == spelling.lower(),
                f"lexicon: {spelling} does not apply the registered transform",
            )
    for spelling in required_literals:
        row = by_spelling.get(spelling, {})
        tool_class = policy["requiredToolClass"]
        rule = policy["classRules"][tool_class]
        require(
            errors,
            row.get("class") == tool_class,
            f"lexicon: {spelling} has the wrong registered tool class",
        )
        if "rewriteEligible" in rule:
            require(
                errors,
                row.get("rewriteEligible") == rule["rewriteEligible"],
                f"lexicon: {spelling} has the wrong rewrite eligibility",
            )
        if rule.get("canonicalTransform") == "identity":
            require(
                errors,
                row.get("canonical") == spelling,
                f"lexicon: {spelling} must preserve exact spelling",
            )
    for row in entries:
        spelling = row.get("spelling")
        lexical_class = row.get("class")
        require(
            errors,
            lexical_class in lexeme_classes,
            f"lexicon: {spelling!r} has unknown class",
        )
        require(
            errors,
            len(row.get("contexts", [])) >= policy["contextsMinimum"],
            f"lexicon: {spelling!r} has too few contexts",
        )
        rule = policy["classRules"].get(lexical_class, {})
        if rule.get("canonicalTransform") == "lowercase":
            canonical_spelling = row.get("canonical", "")
            require(
                errors,
                canonical_spelling == canonical_spelling.lower(),
                f"lexicon: common noun {spelling!r} is not lowercase",
            )
        elif rule.get("canonicalTransform") == "identity":
            require(
                errors,
                row.get("canonical") == spelling,
                f"lexicon: {lexical_class} name {spelling!r} does not preserve identity spelling",
            )
        if "rewriteEligible" in rule:
            require(
                errors,
                row.get("rewriteEligible") == rule["rewriteEligible"],
                f"lexicon: {lexical_class} name {spelling!r} has the wrong rewrite eligibility",
            )
