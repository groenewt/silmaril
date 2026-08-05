"""JVM build and filesystem discovery admitted only inside ContractGate."""

from __future__ import annotations

import json
import os
from pathlib import Path

from .host.octet import Projection
from .location import admit
from .registration import _loads
from .revision import observe, observe_coordinates
from ..contract import Contract
from ..jvm import Process, Unavailable
from ..kind import (
    ExternalProductObserved,
    TimestampCurrentUnverified,
    TimestampStale,
)
from ..locator import Locator
from ..transport import (
    ExternalDependencyRevision,
    OwnedDependencyRevision,
    RuntimeEvidence,
)


def _object(path: Path) -> dict[str, object]:
    value = _loads(path.read_text(encoding="utf-8"), path)
    if not isinstance(value, dict):
        raise ValueError(f"registered JVM evidence is not an object: {path}")
    return value


def _string(value: object, coordinate: str) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError(f"registered JVM coordinate is not text: {coordinate}")
    return value


def _sequence(value: object, coordinate: str) -> tuple[object, ...]:
    if not isinstance(value, list):
        raise ValueError(f"registered JVM coordinate is not a sequence: {coordinate}")
    return tuple(value)


def _module(source: Path, repository: Path) -> Path:
    modules = repository / "modules"
    for coordinate in source.parents:
        if coordinate.parent == modules:
            return coordinate
    raise ValueError(f"Scala Lambda main is outside a module: {source}")


def _inside(path: Path, boundary: Path, coordinate: str) -> Path:
    resolved = path.resolve()
    resolved.relative_to(boundary.resolve())
    if not resolved.exists():
        raise ValueError(f"registered JVM {coordinate} does not exist: {resolved}")
    return resolved


def _flag_path(arguments: tuple[object, ...], flag: str, repository: Path) -> Path:
    matches = [index for index, value in enumerate(arguments) if value == flag]
    if len(matches) != 1 or matches[0] + 1 >= len(arguments):
        raise ValueError(f"Scala CLI BSP registration must expose one {flag}")
    value = _string(arguments[matches[0] + 1], flag)
    return _inside(Path(value), repository, flag)


def discover(repository: Locator, contract: Contract | None = None) -> Process | Unavailable:
    root = Path(os.path.abspath(repository.host_path.lexical))
    gateway = contract if contract is not None else Contract.discover(repository)
    registration = gateway.process_file
    projection = Projection.registered(gateway)
    digest_binding = projection.digest

    try:
        main_class = gateway.implementation.main_class
        main_relative = Path(*main_class.split(".")).with_suffix(".scala")
        main_candidates = tuple(
            sorted(root.glob(f"modules/*/src/main/scala/{main_relative.as_posix()}"))
        )
        if len(main_candidates) != 1:
            raise ValueError(
                "registered Scala Lambda main must resolve to one source; "
                f"observed={len(main_candidates)}"
            )
        main_source = _inside(main_candidates[0], root, "main source")
        invocation_root = main_source.parents[2]
        source_coordinates = tuple(
            sorted(
                source.resolve()
                for source in invocation_root.rglob("*.scala")
                if ".scala-build" not in source.parts
            )
        )
        if not source_coordinates:
            raise ValueError("Scala Lambda invocation source closure is empty")

        bsp_candidates = tuple(
            sorted(
                path
                for path in invocation_root.rglob(".bsp/scala-cli.json")
                if ".scala-build" not in path.parts
            )
        )
        if not bsp_candidates:
            raise ValueError("Scala Lambda invocation exposes no BSP registrations")
        matching_registrations: list[tuple[Path, tuple[object, ...], Path]] = []
        for bsp_coordinate in bsp_candidates:
            candidate = _object(bsp_coordinate)
            candidate_arguments = _sequence(candidate.get("argv"), "bsp.argv")
            candidate_options = _flag_path(candidate_arguments, "--json-options", root)
            candidate_inputs = _object(candidate_options.with_name("ide-inputs.json"))
            candidate_input_arguments = _sequence(
                candidate_inputs.get("args"), "ide-inputs.args"
            )
            candidate_input_coordinates = tuple(
                sorted(
                    _inside(
                        Path(_string(value, "ide-inputs.args[]")),
                        root,
                        "source input",
                    )
                    for value in candidate_input_arguments
                )
            )
            if candidate_input_coordinates == source_coordinates:
                matching_registrations.append(
                    (bsp_coordinate.resolve(), candidate_arguments, candidate_options)
                )
        if len(matching_registrations) != 1:
            raise ValueError(
                "Scala Lambda source closure must resolve one exact BSP registration; "
                f"candidates={len(bsp_candidates)} exact={len(matching_registrations)}"
            )
        bsp_registration, arguments, options_path = matching_registrations[0]
        executable = _inside(
            Path(_string(arguments[0], "bsp.argv[0]")),
            Path("/"),
            "Scala CLI executable",
        )
        if not os.access(executable, os.X_OK):
            raise ValueError(f"Scala CLI executable is not executable: {executable}")

        options = _object(options_path)
        scala_version = _string(options.get("scalaVersion"), "scalaVersion")
        module = _module(main_source, root)
        dependency_export = _inside(
            module / "target/streams/compile/dependencyClasspath/_global/streams/export",
            root,
            "SBT dependency classpath",
        )
        dependency_values = tuple(
            value
            for value in dependency_export.read_text(encoding="utf-8").strip().split(os.pathsep)
            if value
        )
        dependencies = tuple(
            _inside(Path(value), Path("/"), "SBT dependency")
            for value in dependency_values
        )
        if not dependencies:
            raise ValueError("SBT dependency classpath is empty")
        scala_library = f"scala3-library_3-{scala_version}.jar"
        if sum(path.name == scala_library for path in dependencies) != 1:
            raise ValueError("SBT dependency classpath does not certify Scala CLI version")

        owned_dependencies: list[OwnedDependencyRevision] = []
        external_dependencies: list[ExternalDependencyRevision] = []
        for dependency in dependencies:
            dependency_locator = admit(
                str(dependency),
                repository.host_path.registration,
            )
            try:
                relative = dependency.relative_to(root)
            except ValueError:
                external_dependencies.append(
                    ExternalDependencyRevision(
                        product=observe(
                            dependency_locator,
                            digest_binding,
                            gateway.contract_gate,
                        ),
                        state=gateway.contract_gate.states.external_product_observed,
                    )
                )
                continue
            if len(relative.parts) < 2 or relative.parts[0] != "modules":
                raise ValueError(f"owned dependency has no module lineage: {dependency}")
            source_root = root / "modules" / relative.parts[1] / "src" / "main"
            source_revision = observe(
                admit(str(source_root), repository.host_path.registration),
                digest_binding,
                gateway.contract_gate,
            )
            product_revision = observe(
                dependency_locator,
                digest_binding,
                gateway.contract_gate,
            )
            dependency_state = (
                gateway.contract_gate.states.timestamp_stale
                if source_revision.latest_modified_ns > product_revision.latest_modified_ns
                else gateway.contract_gate.states.timestamp_current_unverified
            )
            owned_dependencies.append(
                OwnedDependencyRevision(
                    source=source_revision,
                    product=product_revision,
                    state=dependency_state,
                )
            )

        evidence = RuntimeEvidence(
            state=registration.operation_state,
            gap_identities=registration.gap_identities,
            bsp=observe(
                admit(str(bsp_registration), repository.host_path.registration),
                digest_binding,
                gateway.contract_gate,
            ),
            invocation_sources=observe_coordinates(
                admit(str(invocation_root), repository.host_path.registration),
                tuple(
                    admit(str(path), repository.host_path.registration)
                    for path in source_coordinates
                ),
                digest_binding,
                gateway.contract_gate,
            ),
            owned_dependencies=tuple(owned_dependencies),
            external_dependencies=tuple(external_dependencies),
        )
        command = (
            str(executable),
            "run",
            *(str(path) for path in source_coordinates),
            "--scala",
            scala_version,
            "--server=false",
            "--classpath",
            os.pathsep.join(str(path) for path in dependencies),
            "--main-class",
            main_class,
            "--",
        )
        return Process(
            capability=registration.capability,
            runtime_shoe=registration.runtime_shoe,
            working_directory=repository,
            main_class=main_class,
            scala_version=scala_version,
            bsp_registration=admit(
                str(bsp_registration),
                repository.host_path.registration,
            ),
            bsp_registrations=tuple(
                admit(str(path), repository.host_path.registration)
                for path in bsp_candidates
            ),
            sources=tuple(
                admit(str(path), repository.host_path.registration)
                for path in source_coordinates
            ),
            dependencies=tuple(
                admit(str(path), repository.host_path.registration)
                for path in dependencies
            ),
            evidence=evidence,
            command=command,
        )
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as issue:
        return Unavailable(
            capability=registration.capability,
            runtime_shoe=registration.runtime_shoe,
            observations=(f"{type(issue).__name__}: {issue}",),
        )
