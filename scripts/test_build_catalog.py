#!/usr/bin/env python3
"""Tests for build_catalog.py.

Run with `.venv/bin/python -m unittest scripts/test_build_catalog.py -v` (or
just `.venv/bin/python scripts/test_build_catalog.py`). Requires grpcio-tools,
same as the script under test.
"""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_catalog  # noqa: E402


class DescriptorWalkTests(unittest.TestCase):
    """Fixture-based checks: nested symbols, oneofs, reservations, imports."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="catalog-fixture-"))
        (self.tmp / "base.proto").write_text(
            "syntax = \"proto3\";\n"
            "package fixture;\n"
            "message Base {\n"
            "  int32 id = 1;\n"
            "}\n"
        )
        (self.tmp / "main.proto").write_text(
            "syntax = \"proto3\";\n"
            "package fixture;\n"
            "import \"base.proto\";\n"
            "message Outer {\n"
            "  reserved 2, 5 to 7;\n"
            "  reserved \"old_field\";\n"
            "  message Inner {\n"
            "    enum Color { COLOR_UNSPECIFIED = 0; RED = 1; }\n"
            "    Color color = 1;\n"
            "  }\n"
            "  oneof payload {\n"
            "    Base base = 1;\n"
            "    string text = 3;\n"
            "  }\n"
            "  Inner inner = 4;\n"
            "}\n"
        )

    def _walk_main(self) -> dict:
        fds = build_catalog.compile_descriptor_set(
            self.tmp, [self.tmp / "main.proto"]
        )
        fd = next(f for f in fds.file if f.name == "main.proto")
        return build_catalog.walk_file(fd)

    def test_imports_captured(self):
        file_entry = self._walk_main()
        self.assertEqual(file_entry["imports"], ["base.proto"])

    def test_nested_message_and_enum(self):
        file_entry = self._walk_main()
        outer = next(m for m in file_entry["messages"] if m["name"] == "Outer")
        self.assertEqual(outer["fqn"], ".fixture.Outer")
        inner = next(m for m in outer["nested_messages"] if m["name"] == "Inner")
        self.assertEqual(inner["fqn"], ".fixture.Outer.Inner")
        color = next(e for e in inner["nested_enums"] if e["name"] == "Color")
        self.assertEqual(color["fqn"], ".fixture.Outer.Inner.Color")
        self.assertEqual(
            {v["name"]: v["number"] for v in color["values"]},
            {"COLOR_UNSPECIFIED": 0, "RED": 1},
        )

    def test_oneof_membership(self):
        file_entry = self._walk_main()
        outer = next(m for m in file_entry["messages"] if m["name"] == "Outer")
        self.assertEqual(outer["oneofs"], ["payload"])
        by_name = {f["name"]: f for f in outer["fields"]}
        self.assertEqual(by_name["base"]["oneof"], "payload")
        self.assertEqual(by_name["text"]["oneof"], "payload")
        self.assertIsNone(by_name["inner"]["oneof"])

    def test_reservations(self):
        file_entry = self._walk_main()
        outer = next(m for m in file_entry["messages"] if m["name"] == "Outer")
        # end is exclusive on the wire (5 to 7 -> range object end=8); stored inclusive.
        self.assertEqual(outer["reserved_ranges"], [[2, 2], [5, 7]])
        self.assertEqual(outer["reserved_names"], ["old_field"])

    def test_field_type_and_type_name(self):
        file_entry = self._walk_main()
        outer = next(m for m in file_entry["messages"] if m["name"] == "Outer")
        by_name = {f["name"]: f for f in outer["fields"]}
        self.assertEqual(by_name["base"]["type"], "TYPE_MESSAGE")
        self.assertEqual(by_name["base"]["type_name"], ".fixture.Base")
        self.assertEqual(by_name["text"]["type"], "TYPE_STRING")
        self.assertIsNone(by_name["text"]["type_name"])

    def test_counts(self):
        file_entry = self._walk_main()
        self.assertEqual(build_catalog.count_messages(file_entry["messages"]), 2)  # Outer, Inner
        self.assertEqual(
            len(file_entry["enums"]) + build_catalog.count_nested_enums(file_entry["messages"]), 1
        )
        # Outer.base, Outer.text, Outer.inner, plus Inner.color (fields count recursively).
        self.assertEqual(build_catalog.count_fields(file_entry["messages"]), 4)


class DeterministicOrderingTests(unittest.TestCase):
    """Filesystem iteration order must not leak into catalog output."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="catalog-order-"))
        # Names chosen so directory-listing order is unlikely to already be sorted.
        for name, content in [
            ("zeta.proto", 'syntax = "proto3";\npackage order;\nmessage Z { int32 z = 1; }\n'),
            ("alpha.proto", 'syntax = "proto3";\npackage order;\nmessage A { int32 a = 1; }\n'),
            ("mid.proto", 'syntax = "proto3";\npackage order;\nmessage M { int32 m = 1; }\n'),
        ]:
            (self.tmp / name).write_text(content)

    def test_compiled_top_level_files_sorted(self):
        orig_proto_root = build_catalog.PROTO_ROOT
        try:
            build_catalog.PROTO_ROOT = self.tmp.parent
            group = self.tmp.name
            files = build_catalog.compiled_top_level_files(group)
            self.assertEqual([f.name for f in files], ["alpha.proto", "mid.proto", "zeta.proto"])
        finally:
            build_catalog.PROTO_ROOT = orig_proto_root

    def test_repeated_build_is_byte_identical(self):
        fds1 = build_catalog.compile_descriptor_set(
            self.tmp, sorted(self.tmp.glob("*.proto"))
        )
        fds2 = build_catalog.compile_descriptor_set(
            self.tmp, sorted(self.tmp.glob("*.proto"))
        )
        entries1 = [build_catalog.walk_file(fd) for fd in fds1.file]
        entries2 = [build_catalog.walk_file(fd) for fd in fds2.file]
        self.assertEqual(
            json.dumps(entries1, sort_keys=True), json.dumps(entries2, sort_keys=True)
        )


class RepoIntegrationTests(unittest.TestCase):
    """Exercises the tool against this repo's actual proto/ tree."""

    @classmethod
    def setUpClass(cls):
        cls.catalog = build_catalog.build_catalog()

    def test_group_registration_is_consistent(self):
        self.assertTrue(
            self.catalog["registration"]["consistent"],
            self.catalog["registration"]["problems"],
        )

    def test_every_group_maps_to_both_generated_packages(self):
        for group in self.catalog["groups"]:
            targets = group["generated_targets"]
            self.assertTrue((build_catalog.REPO_ROOT / targets["typescript"]).is_dir())
            self.assertTrue((build_catalog.REPO_ROOT / targets["python"]).is_dir())

    def test_status_proto_import_only_is_excluded_from_totals_but_catalogued(self):
        energy_device = next(g for g in self.catalog["groups"] if g["name"] == "energy_device")
        self.assertEqual(energy_device["source_files"], 19)
        self.assertEqual(energy_device["compiled_top_level_inputs"], 18)
        import_only = [f for f in energy_device["files"] if not f["compiled_top_level_input"]]
        self.assertEqual(len(import_only), 1)
        self.assertEqual(import_only[0]["path"], "proto/energy_device/google/rpc/status.proto")
        self.assertEqual(import_only[0]["messages"], [])

    def test_files_within_each_group_are_sorted_by_path(self):
        for group in self.catalog["groups"]:
            paths = [f["path"] for f in group["files"]]
            self.assertEqual(paths, sorted(paths))

    def test_baseline_totals(self):
        # proto/ is authoritative: these document the current surface size so an
        # unintended change shows up, they don't freeze it. Update on purpose.
        totals = self.catalog["totals"]
        self.assertEqual(totals["source_files"], 38)
        self.assertEqual(totals["groups"], 7)
        self.assertEqual(totals["messages"], 868)
        self.assertEqual(totals["enums"], 237)
        self.assertEqual(totals["fields"], 2805)

    def test_rebuild_is_deterministic(self):
        second = build_catalog.build_catalog()
        self.assertEqual(
            json.dumps(self.catalog, sort_keys=True), json.dumps(second, sort_keys=True)
        )


class CliIdempotencyTests(unittest.TestCase):
    """The committed contract: run once, run again, no diff."""

    def test_main_writes_identical_bytes_on_second_run(self):
        orig_dir = build_catalog.CATALOG_DIR
        tmp = Path(tempfile.mkdtemp(prefix="catalog-out-"))
        try:
            build_catalog.CATALOG_DIR = tmp
            build_catalog.main()
            first_json = (tmp / "catalog.json").read_bytes()
            first_md = (tmp / "SUMMARY.md").read_bytes()
            build_catalog.main()
            second_json = (tmp / "catalog.json").read_bytes()
            second_md = (tmp / "SUMMARY.md").read_bytes()
            self.assertEqual(first_json, second_json)
            self.assertEqual(first_md, second_md)
        finally:
            build_catalog.CATALOG_DIR = orig_dir


if __name__ == "__main__":
    unittest.main()
