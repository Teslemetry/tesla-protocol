#!/usr/bin/env python3
"""Tests for upstream_coverage.py.

Run with `.venv/bin/python -m unittest scripts/test_upstream_coverage.py -v`
(or just `.venv/bin/python scripts/test_upstream_coverage.py`). Requires
grpcio-tools, same as the script under test. Exercises the comparison,
marker, overlap and delta-classification logic directly against small proto
fixtures - no network access, unlike a real `--mode head` run.
"""

from __future__ import annotations

import hashlib
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import upstream_coverage as uc  # noqa: E402


def compile_symbols(base: Path, filenames: list[str], source_info: bool) -> uc.Symbols:
    out = Path(tempfile.mkstemp(suffix=".pb")[1])
    try:
        uc.run_protoc(base, [base / f for f in filenames], out, source_info=source_info)
        return uc.index_set(uc.load_descriptor_set(out))
    finally:
        out.unlink()


def write_proto(directory: Path, name: str, content: str) -> None:
    (directory / name).write_text(content)


class MissingSymbolTests(unittest.TestCase):
    """Fixture: upstream field/message ours never modeled - coverage_gap."""

    def test_missing_field_is_coverage_gap(self):
        upstream_dir = Path(tempfile.mkdtemp(prefix="uc-upstream-"))
        ours_dir = Path(tempfile.mkdtemp(prefix="uc-ours-"))
        proto = (
            'syntax = "proto3";\npackage fixture;\n'
            "message M {\n  int32 a = 1;\n  int32 b = 2;\n}\n"
        )
        write_proto(upstream_dir, "m.proto", proto)
        write_proto(
            ours_dir, "m.proto",
            'syntax = "proto3";\npackage fixture;\nmessage M {\n  int32 a = 1;\n}\n',
        )
        upstream = compile_symbols(upstream_dir, ["m.proto"], source_info=False)
        ours = compile_symbols(ours_dir, ["m.proto"], source_info=True)

        findings, void_masked = uc.compare(upstream, ours)

        self.assertEqual(void_masked, [])
        gaps = [f for f in findings if f.outcome_class == "coverage_gap"]
        self.assertEqual(len(gaps), 1)
        self.assertIn(".fixture.M.b", gaps[0].detail)

    def test_missing_message_is_coverage_gap(self):
        upstream_dir = Path(tempfile.mkdtemp(prefix="uc-upstream-"))
        ours_dir = Path(tempfile.mkdtemp(prefix="uc-ours-"))
        write_proto(
            upstream_dir, "m.proto",
            'syntax = "proto3";\npackage fixture;\n'
            "message M {\n  int32 a = 1;\n}\nmessage N {\n  int32 x = 1;\n}\n",
        )
        write_proto(
            ours_dir, "m.proto",
            'syntax = "proto3";\npackage fixture;\nmessage M {\n  int32 a = 1;\n}\n',
        )
        upstream = compile_symbols(upstream_dir, ["m.proto"], source_info=False)
        ours = compile_symbols(ours_dir, ["m.proto"], source_info=True)

        findings, _ = uc.compare(upstream, ours)

        gaps = [f for f in findings if f.outcome_class == "coverage_gap"]
        self.assertTrue(any(".fixture.N" in f.detail for f in gaps))


class NewProtoFileTests(unittest.TestCase):
    """Fixture: a whole new upstream file, not yet mirrored locally."""

    def test_new_file_is_reported_missing(self):
        upstream_dir = Path(tempfile.mkdtemp(prefix="uc-upstream-"))
        ours_dir = Path(tempfile.mkdtemp(prefix="uc-ours-"))
        for d in (upstream_dir, ours_dir):
            write_proto(d, "a.proto", 'syntax = "proto3";\npackage fixture;\nmessage A {}\n')
        write_proto(upstream_dir, "b.proto", 'syntax = "proto3";\npackage fixture;\nmessage B {}\n')

        missing = uc.missing_files(
            sorted(upstream_dir.glob("*.proto")), sorted(ours_dir.glob("*.proto"))
        )

        self.assertEqual(missing, {"b.proto"})


class WireConflictTests(unittest.TestCase):
    """Fixture: rename and type/tag conflicts - upstream wins names."""

    def test_rename_is_wire_conflict(self):
        upstream_dir = Path(tempfile.mkdtemp(prefix="uc-upstream-"))
        ours_dir = Path(tempfile.mkdtemp(prefix="uc-ours-"))
        write_proto(
            upstream_dir, "m.proto",
            'syntax = "proto3";\npackage fixture;\nmessage M {\n  int32 a = 1;\n}\n',
        )
        write_proto(
            ours_dir, "m.proto",
            'syntax = "proto3";\npackage fixture;\nmessage M {\n  int32 renamed_a = 1;\n}\n',
        )
        upstream = compile_symbols(upstream_dir, ["m.proto"], source_info=False)
        ours = compile_symbols(ours_dir, ["m.proto"], source_info=True)

        findings, void_masked = uc.compare(upstream, ours)

        self.assertEqual(void_masked, [])
        conflicts = [f for f in findings if f.outcome_class == "wire_conflict"]
        self.assertEqual(len(conflicts), 1)
        self.assertIn("renamed_a", conflicts[0].detail)
        self.assertIn("upstream wins names", conflicts[0].detail)

    def test_type_mismatch_is_wire_conflict(self):
        upstream_dir = Path(tempfile.mkdtemp(prefix="uc-upstream-"))
        ours_dir = Path(tempfile.mkdtemp(prefix="uc-ours-"))
        write_proto(
            upstream_dir, "m.proto",
            'syntax = "proto3";\npackage fixture;\nmessage M {\n  int32 a = 1;\n}\n',
        )
        write_proto(
            ours_dir, "m.proto",
            'syntax = "proto3";\npackage fixture;\nmessage M {\n  string a = 1;\n}\n',
        )
        upstream = compile_symbols(upstream_dir, ["m.proto"], source_info=False)
        ours = compile_symbols(ours_dir, ["m.proto"], source_info=True)

        findings, void_masked = uc.compare(upstream, ours)

        self.assertEqual(void_masked, [])
        conflicts = [f for f in findings if f.outcome_class == "wire_conflict"]
        self.assertEqual(len(conflicts), 1)
        self.assertIn(".fixture.M.a", conflicts[0].detail)


class NoMovementTests(unittest.TestCase):
    """Fixture: upstream and pin are byte-identical, ours already covers it."""

    def test_identical_state_needs_no_reconcile(self):
        content = 'syntax = "proto3";\npackage fixture;\nmessage M {\n  int32 a = 1;\n}\n'
        upstream_dir = Path(tempfile.mkdtemp(prefix="uc-upstream-"))
        ours_dir = Path(tempfile.mkdtemp(prefix="uc-ours-"))
        write_proto(upstream_dir, "m.proto", content)
        write_proto(ours_dir, "m.proto", content)
        upstream = compile_symbols(upstream_dir, ["m.proto"], source_info=False)
        ours = compile_symbols(ours_dir, ["m.proto"], source_info=True)

        findings, void_masked = uc.compare(upstream, ours)
        marker_cache: dict = {}
        marker_findings = uc.check_markers(
            upstream, ours, ours_dir, {"m.proto"}, marker_cache
        )
        overlap_findings = uc.check_overlaps(
            upstream, ours, ours_dir, {"m.proto"}, marker_cache
        )

        self.assertEqual(findings + marker_findings + overlap_findings, [])
        self.assertEqual(void_masked, [])

        sha = hashlib.sha256(content.encode()).hexdigest()
        file_diff = uc.diff_files({"m.proto": sha}, {"m.proto": sha})
        self.assertEqual(file_diff, {"added": [], "removed": [], "changed": [], "unchanged": ["m.proto"]})

        by_class, outcome_classes, reconcile_needed = uc.classify(
            findings + marker_findings + overlap_findings, proto_bytes_changed=False
        )
        self.assertEqual(by_class, {})
        self.assertEqual(outcome_classes, [])
        self.assertFalse(reconcile_needed)


class UpstreamOverlapTests(unittest.TestCase):
    """Fixture: upstream now republishes a symbol we already carry as a
    TESLEMETRY-EXT local extension - the case that used to report "No drift"
    even though the pin was stale."""

    def setUp(self):
        self.ours_dir = Path(tempfile.mkdtemp(prefix="uc-ours-"))
        write_proto(
            self.ours_dir, "m.proto",
            'syntax = "proto3";\npackage fixture;\n'
            "message M {\n"
            "  int32 a = 1;\n"
            "  int32 ext_field = 2; // TESLEMETRY-EXT\n"
            "}\n",
        )
        self.old_upstream_content = (
            'syntax = "proto3";\npackage fixture;\nmessage M {\n  int32 a = 1;\n}\n'
        )
        self.new_upstream_content = (
            'syntax = "proto3";\npackage fixture;\n'
            "message M {\n  int32 a = 1;\n  int32 ext_field = 2;\n}\n"
        )

    def test_overlap_is_not_a_coverage_finding(self):
        upstream_dir = Path(tempfile.mkdtemp(prefix="uc-upstream-"))
        write_proto(upstream_dir, "m.proto", self.new_upstream_content)
        upstream = compile_symbols(upstream_dir, ["m.proto"], source_info=False)
        ours = compile_symbols(self.ours_dir, ["m.proto"], source_info=True)

        findings, void_masked = uc.compare(upstream, ours)

        self.assertEqual(findings, [])
        self.assertEqual(void_masked, [])

    def test_overlap_is_flagged_as_upstream_overlap(self):
        upstream_dir = Path(tempfile.mkdtemp(prefix="uc-upstream-"))
        write_proto(upstream_dir, "m.proto", self.new_upstream_content)
        upstream = compile_symbols(upstream_dir, ["m.proto"], source_info=False)
        ours = compile_symbols(self.ours_dir, ["m.proto"], source_info=True)

        overlap_findings = uc.check_overlaps(upstream, ours, self.ours_dir, {"m.proto"}, {})

        self.assertEqual(len(overlap_findings), 1)
        self.assertEqual(overlap_findings[0].outcome_class, "upstream_overlap")
        self.assertIn("ext_field", overlap_findings[0].detail)

    def test_reconcile_advances_instead_of_no_drift(self):
        upstream_dir = Path(tempfile.mkdtemp(prefix="uc-upstream-"))
        write_proto(upstream_dir, "m.proto", self.new_upstream_content)
        upstream = compile_symbols(upstream_dir, ["m.proto"], source_info=False)
        ours = compile_symbols(self.ours_dir, ["m.proto"], source_info=True)

        findings, _ = uc.compare(upstream, ours)
        marker_cache: dict = {}
        marker_findings = uc.check_markers(upstream, ours, self.ours_dir, {"m.proto"}, marker_cache)
        overlap_findings = uc.check_overlaps(upstream, ours, self.ours_dir, {"m.proto"}, marker_cache)

        # Old behavior: zero coverage findings -> reported "No drift."
        self.assertEqual(findings + marker_findings, [])

        pinned = {"m.proto": hashlib.sha256(self.old_upstream_content.encode()).hexdigest()}
        observed = {"m.proto": hashlib.sha256(self.new_upstream_content.encode()).hexdigest()}
        file_diff = uc.diff_files(pinned, observed)
        proto_bytes_changed = bool(file_diff["added"] or file_diff["removed"] or file_diff["changed"])
        self.assertTrue(proto_bytes_changed)
        self.assertEqual(file_diff["changed"], ["m.proto"])

        by_class, outcome_classes, reconcile_needed = uc.classify(
            findings + marker_findings + overlap_findings, proto_bytes_changed
        )

        self.assertEqual(outcome_classes, ["upstream_overlap"])
        self.assertTrue(reconcile_needed)


class VoidMaskingTests(unittest.TestCase):
    """Fixture: a Tesla-published placeholder (empty message type) at the
    same number as a concretely-defined local field. A void never replaces
    a concrete definition."""

    def test_concrete_local_field_suppresses_the_conflict(self):
        upstream_dir = Path(tempfile.mkdtemp(prefix="uc-upstream-"))
        ours_dir = Path(tempfile.mkdtemp(prefix="uc-ours-"))
        write_proto(
            upstream_dir, "m.proto",
            'syntax = "proto3";\npackage fixture;\n'
            "message Void {}\nmessage M {\n  Void raw = 5;\n}\n",
        )
        write_proto(
            ours_dir, "m.proto",
            'syntax = "proto3";\npackage fixture;\n'
            "message Void {}\nmessage M {\n  int32 concrete_field = 5;\n}\n",
        )
        upstream = compile_symbols(upstream_dir, ["m.proto"], source_info=False)
        ours = compile_symbols(ours_dir, ["m.proto"], source_info=True)

        self.assertIn(".fixture.Void", upstream.empty_messages)

        findings, void_masked = uc.compare(upstream, ours)

        self.assertEqual(findings, [])
        self.assertEqual(len(void_masked), 1)
        self.assertIn("concrete_field", void_masked[0])

    def test_upstream_concrete_field_still_conflicts_normally(self):
        # Sanity check: without a void type on the upstream side, the
        # existing rename-conflict behavior (upstream wins) is unaffected.
        upstream_dir = Path(tempfile.mkdtemp(prefix="uc-upstream-"))
        ours_dir = Path(tempfile.mkdtemp(prefix="uc-ours-"))
        write_proto(
            upstream_dir, "m.proto",
            'syntax = "proto3";\npackage fixture;\nmessage M {\n  int32 raw = 5;\n}\n',
        )
        write_proto(
            ours_dir, "m.proto",
            'syntax = "proto3";\npackage fixture;\nmessage M {\n  int32 concrete_field = 5;\n}\n',
        )
        upstream = compile_symbols(upstream_dir, ["m.proto"], source_info=False)
        ours = compile_symbols(ours_dir, ["m.proto"], source_info=True)

        findings, void_masked = uc.compare(upstream, ours)

        self.assertEqual(void_masked, [])
        conflicts = [f for f in findings if f.outcome_class == "wire_conflict"]
        self.assertEqual(len(conflicts), 1)


class EmptyMessageIndexingTests(unittest.TestCase):
    def test_empty_message_is_tracked(self):
        d = Path(tempfile.mkdtemp(prefix="uc-empty-"))
        write_proto(
            d, "m.proto",
            'syntax = "proto3";\npackage fixture;\n'
            "message Empty {}\nmessage NotEmpty {\n  int32 a = 1;\n}\n",
        )
        syms = compile_symbols(d, ["m.proto"], source_info=False)
        self.assertIn(".fixture.Empty", syms.empty_messages)
        self.assertNotIn(".fixture.NotEmpty", syms.empty_messages)


class DiffFilesTests(unittest.TestCase):
    def test_added_removed_changed_unchanged(self):
        pinned = {"a.proto": "h1", "b.proto": "h2", "c.proto": "h3"}
        observed = {"a.proto": "h1", "b.proto": "changed", "d.proto": "h4"}

        result = uc.diff_files(pinned, observed)

        self.assertEqual(result["added"], ["d.proto"])
        self.assertEqual(result["removed"], ["c.proto"])
        self.assertEqual(result["changed"], ["b.proto"])
        self.assertEqual(result["unchanged"], ["a.proto"])


class ClassifyTests(unittest.TestCase):
    def test_no_findings_no_byte_change_is_clean(self):
        by_class, outcome_classes, reconcile_needed = uc.classify([], proto_bytes_changed=False)
        self.assertEqual(by_class, {})
        self.assertEqual(outcome_classes, [])
        self.assertFalse(reconcile_needed)

    def test_byte_change_alone_triggers_reconcile(self):
        _, outcome_classes, reconcile_needed = uc.classify([], proto_bytes_changed=True)
        self.assertEqual(outcome_classes, [])
        self.assertTrue(reconcile_needed)

    def test_unmarked_extension_alone_does_not_trigger_reconcile(self):
        findings = [uc.Finding("unmarked_extension", "field `.fixture.M.x` is not in upstream")]
        _, outcome_classes, reconcile_needed = uc.classify(findings, proto_bytes_changed=False)
        self.assertEqual(outcome_classes, [])
        self.assertFalse(reconcile_needed)

    def test_coverage_gap_triggers_reconcile(self):
        findings = [uc.Finding("coverage_gap", "field `.fixture.M.x` missing from ours")]
        by_class, outcome_classes, reconcile_needed = uc.classify(findings, proto_bytes_changed=False)
        self.assertEqual(outcome_classes, ["coverage_gap"])
        self.assertTrue(reconcile_needed)
        self.assertEqual(by_class["coverage_gap"], ["field `.fixture.M.x` missing from ours"])


if __name__ == "__main__":
    unittest.main()
