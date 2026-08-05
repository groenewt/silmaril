"""Profile-projected laws for morphism scenes, atlases, and lexicons.

The validator profile is the policy value. This module only interprets that
value through injected pure combinators; it owns no hidden project policy.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Mapping

from morphism_contracts.law import anchor_gateway, atlas, location_capture
from morphism_contracts.law import runtime_shoes, scene_contract, schema_lexicon
from morphism_contracts.law.common import Digest, diagnostic, require
from morphism_contracts.law.topology import registered_literals


def _diagnostic(rule_id: str, message: str) -> str:
    return diagnostic(rule_id, message)


def _require(
    errors: list[str], condition: bool, message: str, rule_id: str | None = None
) -> None:
    require(errors, condition, message, rule_id)


@dataclass(frozen=True, slots=True)
class SceneLaws:
    """An immutable scene-law projection over one validation profile."""

    profile: Mapping[str, Any]
    digest: Digest

    def _member_content(self, member: Mapping[str, Any]) -> dict[str, Any]:
        return anchor_gateway.member_content(self.profile, member)

    def _module_content(self, module: Mapping[str, Any]) -> dict[str, Any]:
        return anchor_gateway.module_content(self.profile, module)

    @staticmethod
    def _dependency_closure(
        identity: str, members: Mapping[str, Mapping[str, Any]]
    ) -> set[str]:
        return anchor_gateway.dependency_closure(identity, members)

    @staticmethod
    def _acyclic(members: Mapping[str, Mapping[str, Any]]) -> bool:
        return anchor_gateway.acyclic(members)

    def _validate_anchor_gateway(
        self, scene: Mapping[str, Any], errors: list[str]
    ) -> None:
        anchor_gateway.validate(self.profile, self.digest, scene, errors)

    def _validate_runtime_shoes(
        self, scene: Mapping[str, Any], errors: list[str]
    ) -> None:
        runtime_shoes.validate(self.profile, scene, errors)

    def _validate_location(
        self, scene: Mapping[str, Any], errors: list[str]
    ) -> None:
        location_capture.validate(self.profile, scene, errors)

    def _validate_atlas(
        self, scene: Mapping[str, Any], errors: list[str]
    ) -> None:
        atlas.validate(self.profile, scene, errors)

    def validate_scene(
        self,
        scene: Mapping[str, Any],
        lexicon: Mapping[str, Any],
        errors: list[str],
    ) -> None:
        scene_contract.validate(self.profile, self.digest, scene, lexicon, errors)

    def validate_schema(
        self, schema: Mapping[str, Any], errors: list[str]
    ) -> None:
        schema_lexicon.validate_schema(self.profile, schema, errors)

    def validate_lexicon(
        self, lexicon: Mapping[str, Any], errors: list[str]
    ) -> None:
        schema_lexicon.validate_lexicon(self.profile, lexicon, errors)
