"""Descriptor-bound physical capture for every Python ContractGate read."""

from __future__ import annotations

import fcntl
import hashlib
from itertools import count
import os
import stat
from dataclasses import dataclass
from pathlib import Path

from ..contract import ContractGateRegistration
from ..kind import (
    DescriptorClosedAfterCapture,
    DescriptorClosedAfterEnumeration,
    DirectoryEnumerationDrifted,
    DirectoryEnumerationStable,
    FileCaptureDrifted,
    FileCaptureStable,
    Provisional,
)
from ..locator import Locator
from .location import admit, child as child_locator
from ..transport import (
    CaptureAttempt,
    CaptureGap,
    DescriptorOpenedDescriptionAssociation,
    DescriptorObservation,
    DigestBinding,
    DirectoryFrame,
    DirectoryInode,
    FileObservation,
    Metadata,
    OpenedDescriptionInodeAssociation,
    OpenedFileDescriptionContext,
    OpenedFileDescriptionIdentityEvidence,
    OpenedFileDescriptionOccurrence,
    RegularInode,
    SpecialInode,
    SymbolicLinkInode,
)


@dataclass(frozen=True, slots=True)
class CapturedFileStable:
    observation: FileObservation
    payload: bytes


@dataclass(frozen=True, slots=True)
class CapturedFileDrifted:
    observation: FileObservation
    payload: bytes
    gap_identity: str
    gap_evidence: str


@dataclass(frozen=True, slots=True)
class DirectoryCapture:
    files: tuple[FileObservation, ...]
    directories: tuple[DirectoryFrame, ...]
    gaps: tuple[CaptureGap, ...]


@dataclass(slots=True)
class _DirectoryCursor:
    locator: Locator
    descriptor: int
    capture_attempt: CaptureAttempt
    entry_pre: Metadata
    pre: Metadata
    names: tuple[str, ...]
    index: int
    offset_pre: int
    status_flags: int


_ATTEMPT_SEQUENCE = count()


def _lexical(locator: Locator) -> Path:
    return Path(os.path.abspath(locator.host_path.lexical))


def _capture_attempt(gate: ContractGateRegistration) -> CaptureAttempt:
    return CaptureAttempt(
        identity=(
            f"{gate.capture.attempt_lineage_identity}:"
            f"process-local:{next(_ATTEMPT_SEQUENCE)}"
        ),
        lineage_identity=gate.capture.attempt_lineage_identity,
    )


def _inode(value: os.stat_result):
    if stat.S_ISREG(value.st_mode):
        return RegularInode(device=value.st_dev, number=value.st_ino)
    if stat.S_ISDIR(value.st_mode):
        return DirectoryInode(device=value.st_dev, number=value.st_ino)
    if stat.S_ISLNK(value.st_mode):
        return SymbolicLinkInode(device=value.st_dev, number=value.st_ino)
    return SpecialInode(device=value.st_dev, number=value.st_ino)


def _metadata(value: os.stat_result) -> Metadata:
    return Metadata(
        inode=_inode(value),
        size=value.st_size,
        modified_ns=value.st_mtime_ns,
        changed_ns=value.st_ctime_ns,
        link_count=value.st_nlink,
        mode=value.st_mode,
    )


def _file_state(
    entry_pre: Metadata,
    pre: Metadata,
    post: Metadata,
    payload_size: int,
    gate: ContractGateRegistration,
) -> FileCaptureStable | FileCaptureDrifted:
    if entry_pre == pre == post and payload_size == pre.size:
        return gate.states.file_capture_stable
    return gate.states.file_capture_drifted


def _directory_state(
    entry_pre: Metadata,
    pre: Metadata,
    post: Metadata,
    gate: ContractGateRegistration,
) -> DirectoryEnumerationStable | DirectoryEnumerationDrifted:
    if entry_pre == pre == post:
        return gate.states.directory_enumeration_stable
    return gate.states.directory_enumeration_drifted


def _new_digest(binding: DigestBinding):
    host_spelling = hashlib.sha256().name
    provider_coordinate = f"{hashlib.__name__}.{host_spelling}"
    if binding.provider_coordinate != provider_coordinate:
        raise ValueError(
            "ContractGate digest provider differs from the registered projection: "
            f"registered={binding.provider_coordinate} host={provider_coordinate}"
        )
    if binding.host_spelling != host_spelling:
        raise ValueError(
            "ContractGate digest spelling differs from the registered projection: "
            f"registered={binding.host_spelling} host={host_spelling}"
        )
    return hashlib.sha256()


def _opened_description(
    locator: Locator,
    descriptor: DescriptorObservation,
    offset_pre: int,
    offset_post: int,
    status_flags: int,
    gate: ContractGateRegistration,
) -> OpenedFileDescriptionOccurrence:
    context = OpenedFileDescriptionContext(
        capture_attempt=descriptor.capture_attempt,
        locator=locator,
        descriptor_process_local_number=descriptor.process_local_number,
        evidence_state=gate.states.provisional,
    )
    return OpenedFileDescriptionOccurrence(
        context=context,
        identity_evidence=OpenedFileDescriptionIdentityEvidence(
            context=context,
            gap_identity=gate.capture.opened_description_kernel_identity_gap_identity,
            evidence=(
                "Python exposes an FD occurrence and description properties, "
                "not a stable kernel file-table identity"
            ),
        ),
        offset_pre=offset_pre,
        offset_post=offset_post,
        status_flags=status_flags,
    )


def _capture_descriptor(
    locator: Locator,
    descriptor: int,
    capture_attempt: CaptureAttempt,
    entry_pre: Metadata,
    digest_binding: DigestBinding,
    gate: ContractGateRegistration,
) -> CapturedFileStable | CapturedFileDrifted:
    pre = _metadata(os.fstat(descriptor))
    if not stat.S_ISREG(pre.mode):
        raise ValueError(
            "ContractGate capture requires a regular file: "
            f"{locator.host_path.lexical}"
        )
    descriptor_observation = DescriptorObservation(
        capture_attempt=capture_attempt,
        process_local_number=descriptor,
        lifecycle=gate.states.descriptor_closed_after_capture,
    )
    offset_pre = os.lseek(descriptor, 0, os.SEEK_CUR)
    status_flags = fcntl.fcntl(descriptor, fcntl.F_GETFL)
    remaining = pre.size + 1
    chunks: list[bytes] = []
    digest = _new_digest(digest_binding)
    observed = 0
    while remaining > 0:
        chunk = os.read(descriptor, min(65536, remaining))
        if not chunk:
            break
        chunks.append(chunk)
        digest.update(chunk)
        observed += len(chunk)
        remaining -= len(chunk)
    offset_post = os.lseek(descriptor, 0, os.SEEK_CUR)
    post = _metadata(os.fstat(descriptor))
    payload = b"".join(chunks)
    state = _file_state(entry_pre, pre, post, observed, gate)
    opened_description = _opened_description(
        locator,
        descriptor_observation,
        offset_pre,
        offset_post,
        status_flags,
        gate,
    )
    observation = FileObservation(
        locator=locator,
        descriptor=descriptor_observation,
        opened_description=opened_description,
        descriptor_opened_description=DescriptorOpenedDescriptionAssociation(
            relation_identity=gate.capture.descriptor_opened_description_relation_identity,
            descriptor=descriptor_observation,
            opened_description=opened_description,
        ),
        opened_description_inode=OpenedDescriptionInodeAssociation(
            relation_identity=gate.capture.opened_description_inode_relation_identity,
            opened_description=opened_description,
            inode=pre.inode,
        ),
        entry_pre=entry_pre,
        pre=pre,
        post=post,
        host_octet_count=observed,
        digest=digest_binding,
        payload_digest=digest.hexdigest(),
        state=state,
    )
    if isinstance(state, FileCaptureStable):
        return CapturedFileStable(observation=observation, payload=payload)
    return CapturedFileDrifted(
        observation=observation,
        payload=payload,
        gap_identity=gate.capture.file_drift_gap_identity,
        gap_evidence=(
            "directory-entry, descriptor pre/post metadata, or bounded payload "
            "length changed"
        ),
    )


def file(
    locator: Locator,
    digest_binding: DigestBinding,
    gate: ContractGateRegistration,
) -> CapturedFileStable | CapturedFileDrifted:
    path = _lexical(locator)
    physical_locator = admit(str(path), locator.host_path.registration)
    entry_pre = _metadata(os.stat(path, follow_symlinks=False))
    descriptor = os.open(path, os.O_RDONLY | os.O_CLOEXEC | os.O_NOFOLLOW)
    try:
        return _capture_descriptor(
            physical_locator,
            descriptor,
            _capture_attempt(gate),
            entry_pre,
            digest_binding,
            gate,
        )
    finally:
        os.close(descriptor)


def _file_at(
    parent_descriptor: int,
    name: str,
    locator: Locator,
    entry_pre: Metadata,
    digest_binding: DigestBinding,
    gate: ContractGateRegistration,
) -> CapturedFileStable | CapturedFileDrifted:
    descriptor = os.open(
        name,
        os.O_RDONLY | os.O_CLOEXEC | os.O_NOFOLLOW,
        dir_fd=parent_descriptor,
    )
    try:
        return _capture_descriptor(
            locator,
            descriptor,
            _capture_attempt(gate),
            entry_pre,
            digest_binding,
            gate,
        )
    finally:
        os.close(descriptor)


def _cursor(
    locator: Locator,
    descriptor: int,
    capture_attempt: CaptureAttempt,
    entry_pre: Metadata,
) -> _DirectoryCursor:
    pre = _metadata(os.fstat(descriptor))
    if not stat.S_ISDIR(pre.mode):
        raise ValueError(
            "ContractGate tree capture requires a directory: "
            f"{locator.host_path.lexical}"
        )
    offset_pre = os.lseek(descriptor, 0, os.SEEK_CUR)
    status_flags = fcntl.fcntl(descriptor, fcntl.F_GETFL)
    names = tuple(sorted(os.listdir(descriptor)))
    return _DirectoryCursor(
        locator=locator,
        descriptor=descriptor,
        capture_attempt=capture_attempt,
        entry_pre=entry_pre,
        pre=pre,
        names=names,
        index=0,
        offset_pre=offset_pre,
        status_flags=status_flags,
    )


def _root_cursor(
    locator: Locator,
    gate: ContractGateRegistration,
) -> _DirectoryCursor:
    path = _lexical(locator)
    physical_locator = admit(str(path), locator.host_path.registration)
    entry_pre = _metadata(os.stat(path, follow_symlinks=False))
    descriptor = os.open(
        path,
        os.O_RDONLY | os.O_CLOEXEC | os.O_NOFOLLOW | os.O_DIRECTORY,
    )
    try:
        return _cursor(
            physical_locator,
            descriptor,
            _capture_attempt(gate),
            entry_pre,
        )
    except Exception:
        os.close(descriptor)
        raise


def _child_cursor(
    parent: _DirectoryCursor,
    name: str,
    locator: Locator,
    entry_pre: Metadata,
    gate: ContractGateRegistration,
) -> _DirectoryCursor:
    descriptor = os.open(
        name,
        os.O_RDONLY | os.O_CLOEXEC | os.O_NOFOLLOW | os.O_DIRECTORY,
        dir_fd=parent.descriptor,
    )
    try:
        return _cursor(locator, descriptor, _capture_attempt(gate), entry_pre)
    except Exception:
        os.close(descriptor)
        raise


def _gap(identity: str, locator: Locator, evidence: str) -> CaptureGap:
    return CaptureGap(
        identity=identity,
        locator=locator,
        evidence=evidence,
    )


def tree(
    locator: Locator,
    digest_binding: DigestBinding,
    gate: ContractGateRegistration,
) -> DirectoryCapture:
    """Iteratively capture children through retained directory descriptors."""

    root = admit(str(_lexical(locator)), locator.host_path.registration)
    stack = [_root_cursor(root, gate)]
    files: list[FileObservation] = []
    frames: list[DirectoryFrame] = []
    gaps: list[CaptureGap] = [
        _gap(
            gate.capture.non_atomic_snapshot_gap_identity,
            root,
            "descriptor-relative frames do not constitute an atomic whole-tree snapshot",
        )
    ]
    try:
        while stack:
            current = stack[-1]
            if current.index < len(current.names):
                name = current.names[current.index]
                current.index += 1
                child = child_locator(current.locator, name)
                try:
                    entry_pre = _metadata(
                        os.stat(
                            name,
                            dir_fd=current.descriptor,
                            follow_symlinks=False,
                        )
                    )
                except OSError as issue:
                    gaps.append(
                        _gap(
                            gate.capture.entry_stat_unavailable_gap_identity,
                            child,
                            f"entry observed in frame but stat failed: {type(issue).__name__}: {issue}",
                        )
                    )
                    continue
                if stat.S_ISLNK(entry_pre.mode):
                    gaps.append(
                        _gap(
                            gate.capture.symbolic_link_payload_not_captured_gap_identity,
                            child,
                            "symbolic-link entry observed; link and target payload were not captured",
                        )
                    )
                    continue
                if stat.S_ISDIR(entry_pre.mode):
                    try:
                        stack.append(_child_cursor(current, name, child, entry_pre, gate))
                    except (OSError, ValueError) as issue:
                        gaps.append(
                            _gap(
                                gate.capture.directory_payload_not_captured_gap_identity,
                                child,
                                f"directory entry observed but open failed: {type(issue).__name__}: {issue}",
                            )
                        )
                    continue
                if stat.S_ISREG(entry_pre.mode):
                    try:
                        captured = _file_at(
                            current.descriptor,
                            name,
                            child,
                            entry_pre,
                            digest_binding,
                            gate,
                        )
                    except (OSError, ValueError) as issue:
                        gaps.append(
                            _gap(
                                gate.capture.file_payload_not_captured_gap_identity,
                                child,
                                f"regular-file entry observed but payload open failed: {type(issue).__name__}: {issue}",
                            )
                        )
                        continue
                    files.append(captured.observation)
                    if isinstance(captured, CapturedFileDrifted):
                        gaps.append(
                            _gap(captured.gap_identity, child, captured.gap_evidence)
                        )
                    continue
                gaps.append(
                    _gap(
                        gate.capture.special_payload_not_captured_gap_identity,
                        child,
                        f"special entry observed; payload not captured; mode={entry_pre.mode}",
                    )
                )
                continue

            offset_post = os.lseek(current.descriptor, 0, os.SEEK_CUR)
            post = _metadata(os.fstat(current.descriptor))
            state = _directory_state(current.entry_pre, current.pre, post, gate)
            descriptor_observation = DescriptorObservation(
                capture_attempt=current.capture_attempt,
                process_local_number=current.descriptor,
                lifecycle=gate.states.descriptor_closed_after_enumeration,
            )
            opened_description = _opened_description(
                current.locator,
                descriptor_observation,
                current.offset_pre,
                offset_post,
                current.status_flags,
                gate,
            )
            frames.append(
                DirectoryFrame(
                    locator=current.locator,
                    descriptor=descriptor_observation,
                    opened_description=opened_description,
                    descriptor_opened_description=DescriptorOpenedDescriptionAssociation(
                        relation_identity=gate.capture.descriptor_opened_description_relation_identity,
                        descriptor=descriptor_observation,
                        opened_description=opened_description,
                    ),
                    opened_description_inode=OpenedDescriptionInodeAssociation(
                        relation_identity=gate.capture.opened_description_inode_relation_identity,
                        opened_description=opened_description,
                        inode=current.pre.inode,
                    ),
                    entry_pre=current.entry_pre,
                    pre=current.pre,
                    post=post,
                    entry_count=len(current.names),
                    state=state,
                )
            )
            if isinstance(state, DirectoryEnumerationDrifted):
                gaps.append(
                    _gap(
                        gate.capture.directory_drift_gap_identity,
                        current.locator,
                        "directory-entry or descriptor pre/post metadata changed",
                    )
                )
            finished = stack.pop()
            os.close(finished.descriptor)
    finally:
        while stack:
            cursor = stack.pop()
            try:
                os.close(cursor.descriptor)
            except OSError:
                pass
    return DirectoryCapture(
        files=tuple(sorted(files, key=lambda item: item.locator.canonical.value)),
        directories=tuple(
            sorted(frames, key=lambda item: item.locator.canonical.value)
        ),
        gaps=tuple(gaps),
    )
