"""Provisional revisions derived from descriptor-bound ContractGate frames."""

from __future__ import annotations

import os
import stat
from pathlib import Path

from .capture import CapturedFileDrifted, _lexical, _new_digest, file, tree
from .location import admit
from ..contract import ContractGateRegistration
from ..kind import (
    DirectoryEnumerationDrifted,
    FileCaptureDrifted,
    RevisionProvisionalCaptured,
    RevisionProvisionalDrifted,
    RevisionProvisionalIncomplete,
)
from ..locator import Locator
from ..transport import (
    CaptureGap,
    DigestBinding,
    DirectoryFrame,
    FileObservation,
    Revision,
)


def _revision(
    root: Locator,
    digest_binding: DigestBinding,
    files: tuple[FileObservation, ...],
    directories: tuple[DirectoryFrame, ...],
    gaps: tuple[CaptureGap, ...],
    gate: ContractGateRegistration,
) -> Revision:
    if not files and not directories:
        raise ValueError(
            "revision observation has no frame evidence: "
            f"{root.host_path.lexical}"
        )
    root_path = Path(root.host_path.lexical)
    digest = _new_digest(digest_binding)
    for observation in files:
        if observation.digest != digest_binding:
            raise ValueError(
                "revision file digest binding differs from its frame: "
                f"{observation.locator.canonical.value}"
            )
        observation_path = Path(observation.locator.host_path.lexical)
        relative = (
            observation_path.name
            if observation.locator == root
            else observation_path.relative_to(root_path).as_posix()
        )
        digest.update(relative.encode("utf-8"))
        digest.update(b"\x00")
        digest.update(observation.payload_digest.encode("ascii"))
        digest.update(b"\x00")
        digest.update(str(observation.host_octet_count).encode("ascii"))
        digest.update(b"\x00")
    for frame in directories:
        frame_path = Path(frame.locator.host_path.lexical)
        relative = (
            "."
            if frame.locator == root
            else frame_path.relative_to(root_path).as_posix()
        )
        digest.update(relative.encode("utf-8"))
        digest.update(b"\x00")
        digest.update(str(frame.pre.inode.device).encode("ascii"))
        digest.update(b":")
        digest.update(str(frame.pre.inode.number).encode("ascii"))
        digest.update(b":")
        digest.update(str(frame.entry_count).encode("ascii"))
        digest.update(b"\x00")
    drifted = any(isinstance(item.state, FileCaptureDrifted) for item in files) or any(
        isinstance(item.state, DirectoryEnumerationDrifted)
        for item in directories
    )
    incomplete = any(
        gap.identity != gate.capture.non_atomic_snapshot_gap_identity
        for gap in gaps
    )
    modified = tuple(item.post.modified_ns for item in files) + tuple(
        item.post.modified_ns for item in directories
    )
    state = (
        gate.states.revision_provisional_drifted
        if drifted
        else gate.states.revision_provisional_incomplete
        if incomplete
        else gate.states.revision_provisional_captured
    )
    return Revision(
        locator=root,
        digest=digest_binding,
        revision_digest=digest.hexdigest(),
        latest_modified_ns=max(modified),
        entry_count=len(files),
        state=state,
        files=files,
        directories=directories,
        gaps=gaps,
    )


def _drift_gap(
    observation: FileObservation,
    gate: ContractGateRegistration,
) -> CaptureGap:
    return CaptureGap(
        identity=gate.capture.file_revision_drift_gap_identity,
        locator=observation.locator,
        evidence="directory-entry, descriptor metadata, or bounded payload changed",
    )


def observe(
    locator: Locator,
    digest_binding: DigestBinding,
    gate: ContractGateRegistration,
) -> Revision:
    root_path = _lexical(locator)
    root = admit(str(root_path), locator.host_path.registration)
    entry = os.stat(root_path, follow_symlinks=False)
    if stat.S_ISLNK(entry.st_mode):
        raise ValueError(
            "revision capture does not follow a symbolic-link root: "
            f"{root.host_path.lexical}"
        )
    if stat.S_ISREG(entry.st_mode):
        captured = file(root, digest_binding, gate)
        gaps = (
            (_drift_gap(captured.observation, gate),)
            if isinstance(captured, CapturedFileDrifted)
            else ()
        )
        return _revision(
            root,
            digest_binding,
            (captured.observation,),
            (),
            gaps,
            gate,
        )
    if not stat.S_ISDIR(entry.st_mode):
        raise ValueError(
            "revision locator is not a regular file or directory: "
            f"{root.host_path.lexical}"
        )
    captured_tree = tree(root, digest_binding, gate)
    return _revision(
        root,
        digest_binding,
        captured_tree.files,
        captured_tree.directories,
        captured_tree.gaps,
        gate,
    )


def observe_coordinates(
    locator: Locator,
    coordinates: tuple[Locator, ...],
    digest_binding: DigestBinding,
    gate: ContractGateRegistration,
) -> Revision:
    root = admit(str(_lexical(locator)), locator.host_path.registration)
    root_path = Path(root.host_path.lexical)
    entries = tuple(
        sorted(
            (
                admit(str(_lexical(path)), path.host_path.registration)
                for path in coordinates
            ),
            key=lambda value: value.canonical.value,
        )
    )
    if not entries:
        raise ValueError(
            f"revision observation has no entries: {root.host_path.lexical}"
        )
    observations: list[FileObservation] = []
    gaps: list[CaptureGap] = []
    for entry in entries:
        Path(entry.host_path.lexical).relative_to(root_path)
        captured = file(entry, digest_binding, gate)
        observations.append(captured.observation)
        if isinstance(captured, CapturedFileDrifted):
            gaps.append(_drift_gap(captured.observation, gate))
    return _revision(
        root,
        digest_binding,
        tuple(observations),
        (),
        tuple(gaps),
        gate,
    )
