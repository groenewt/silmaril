"""Deterministic readback of the registered twin URI dispatch and evidence."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any


def errors(
    scene: dict[str, Any],
    repository: Path,
    configuration: dict[str, Any],
    scheme_dispatch: dict[str, tuple[str, set[str]]],
    adapter_identities: dict[str, str],
    relation_predicates: dict[str, str],
) -> list[str]:
    findings: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            findings.append(message)

    sources: dict[str, str] = {}
    try:
        for name, relative in configuration["files"].items():
            lexical = Path(relative)
            if lexical.is_absolute() or ".." in lexical.parts:
                raise ValueError(relative)
            sources[name] = (repository / lexical).read_text(encoding="utf-8")
    except OSError as error:
        return [f"twin readback unavailable: {error}"]
    except ValueError as error:
        return [f"twin readback path escapes repository: {error}"]

    extraction = configuration["dispatchExtraction"]
    dispatch = sources["schemeDispatch"]
    source_dispatch: dict[str, tuple[str, set[str]]] = {}
    for key in scheme_dispatch:
        pattern = extraction["blockPattern"].format(key=re.escape(key))
        match = re.search(pattern, dispatch)
        if not match:
            findings.append(f"twin readback: adapter block {key!r} is absent")
            continue
        block = match.group(1)
        primary_match = re.search(extraction["primaryPattern"], block)
        schemes_match = re.search(extraction["schemesPattern"], block)
        schemes = (
            set(re.findall(extraction["quotedValuePattern"], schemes_match.group(1)))
            if schemes_match
            else set()
        )
        source_dispatch[key] = (
            primary_match.group(1) if primary_match else "",
            schemes,
        )
    require(
        source_dispatch == scheme_dispatch,
        "twin readback: source scheme dispatch differs from the tracked contract",
    )

    for requirement in configuration["requiredSnippets"]:
        require(
            requirement["text"] in sources.get(requirement["source"], ""),
            f"twin readback: required source evidence {requirement!r} is absent",
        )
    relation_evidence = configuration["relationEvidence"]
    relation = sources.get(relation_evidence["source"], "")
    predicate = relation_predicates[relation_evidence["predicateKey"]]
    require(
        predicate in relation
        and relation_evidence["caseInsensitiveText"].lower() in relation.lower(),
        "twin readback: canonical locator relation evidence is absent",
    )

    registry = scene.get("locationRegistry", {})
    scene_dispatch = {
        key: (row.get("primaryScheme"), set(row.get("schemes", [])))
        for key, identity in adapter_identities.items()
        for row in registry.get("adapters", [])
        if isinstance(row, dict) and row.get("adapterIdentity") == identity
    }
    require(
        scene_dispatch == source_dispatch,
        "twin readback: scene registry does not equal the live twin registry",
    )
    observed_identities = {
        row.get("adapterIdentity")
        for row in registry.get("adapters", [])
        if isinstance(row, dict)
    }
    require(
        observed_identities == set(adapter_identities.values()),
        "twin readback: scene adapter identities differ from the validation profile",
    )
    return sorted(set(findings))
