#!/usr/bin/env python3
"""Reply-coverage gate for `CarServer.Response.response_msg`.

`scripts/upstream_coverage.py` only enforces upstream (subset) ours - it never
looks at server-to-app reply payloads, since neither side's public repo
declares them. That blind spot let `GetChargeOnSolarFeatureResponse` (field
15) sit unmodelled with no CI failure.

This gate closes that hole for the reply oneof specifically: every field
number in KNOWN_REPLY_FIELDS must be either present in `oneof response_msg`
or `reserved` with a trailing reason comment. It fails if a known field
number is neither, and it fails if a `reserved` entry has no comment (a
reservation with no reason is as silent as an omission).

KNOWN_REPLY_FIELDS is a fixed, hand-maintained set. It does not discover new
Tesla-added reply fields on its own - whoever adds one must add its number
here (modelled or reserved) as a conscious decision. That is the point: this
gate cannot regress on the fields it already knows about.

Requires grpcio-tools (bundled protoc) in the running interpreter.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

from google.protobuf import descriptor_pb2

REPO_ROOT = Path(__file__).resolve().parent.parent
PROTO_DIR = REPO_ROOT / "proto" / "command"
PROTO_FILE = "car_server.proto"
MESSAGE_FQN = ".CarServer.Response"
ONEOF_NAME = "response_msg"

# Field numbers known to exist in CarServer.Response.response_msg, from the
# app-side completeness audit. Every one of these must be modelled or
# reserved-with-reason below; see PROVENANCE.md / CLAUDE.md for the field
# 12/17/19 exclusion rationale.
KNOWN_REPLY_FIELDS = {
    2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 24, 25,
}


def compile_descriptor_set(out: Path) -> descriptor_pb2.FileDescriptorSet:
    args = [
        sys.executable,
        "-m",
        "grpc_tools.protoc",
        f"-I{PROTO_DIR}",
        f"--descriptor_set_out={out}",
        "--include_source_info",
        PROTO_FILE,
    ]
    proc = subprocess.run(args, capture_output=True, text=True)
    if proc.returncode != 0:
        sys.exit(f"protoc failed:\n{proc.stderr}")
    fds = descriptor_pb2.FileDescriptorSet()
    fds.ParseFromString(out.read_bytes())
    return fds


def find_message(fds: descriptor_pb2.FileDescriptorSet, fqn: str):
    for fd in fds.file:
        if fd.name != PROTO_FILE:
            continue
        prefix = f".{fd.package}" if fd.package else ""
        for i, msg in enumerate(fd.message_type):
            if f"{prefix}.{msg.name}" == fqn:
                return fd, msg, (4, i)
    sys.exit(f"message `{fqn}` not found in {PROTO_FILE}")


def reserved_range_comments(fd, msg_path: tuple) -> dict[int, str | None]:
    """Map each reserved_range index to its statement's comment, if any.

    protoc attaches a `reserved N, M;` statement's comment to the bare
    `(..., 9)` path (once per statement, not per number); the per-range
    `(..., 9, i)` locations that follow it in source order share that
    comment until the next bare `(..., 9)` location resets it.
    """
    group_path = msg_path + (9,)
    comments: dict[int, str | None] = {}
    current: str | None = None
    for loc in fd.source_code_info.location:
        path = tuple(loc.path)
        if path == group_path:
            current = (loc.leading_comments or loc.trailing_comments).strip() or None
        elif len(path) == len(group_path) + 1 and path[:-1] == group_path:
            comments[path[-1]] = current
    return comments


def main() -> int:
    tmp = Path(tempfile.mkdtemp(prefix="reply-coverage-"))
    fds = compile_descriptor_set(tmp / "response.pb")

    fd, msg, msg_path = find_message(fds, MESSAGE_FQN)

    oneof_index = None
    for i, oneof in enumerate(msg.oneof_decl):
        if oneof.name == ONEOF_NAME:
            oneof_index = i
            break
    if oneof_index is None:
        sys.exit(f"oneof `{ONEOF_NAME}` not found on {MESSAGE_FQN}")

    modelled = {
        f.number for f in msg.field
        if f.HasField("oneof_index") and f.oneof_index == oneof_index
    }

    # reserved_range end is exclusive, matching proto's own "reserved N to M" semantics.
    range_comments = reserved_range_comments(fd, msg_path)
    reserved: dict[int, str | None] = {}
    for i, rr in enumerate(msg.reserved_range):
        comment = range_comments.get(i)
        for number in range(rr.start, rr.end):
            reserved[number] = comment

    problems: list[str] = []
    for number in sorted(KNOWN_REPLY_FIELDS):
        if number in modelled:
            continue
        if number in reserved:
            if not reserved[number]:
                problems.append(
                    f"field {number} is `reserved` in {MESSAGE_FQN} but has no reason "
                    "comment - add one explaining why it's excluded"
                )
            continue
        problems.append(
            f"field {number} is neither modelled in `oneof {ONEOF_NAME}` nor `reserved` "
            f"in {MESSAGE_FQN} - it needs a conscious model-or-reserve decision"
        )

    if problems:
        print("Reply coverage gate failed:", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1

    print(
        f"Reply coverage OK: {len(KNOWN_REPLY_FIELDS)} known {MESSAGE_FQN} reply "
        f"fields all modelled or reserved-with-reason."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
