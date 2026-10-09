import os
import subprocess
import sys
import textwrap
import unittest
from pathlib import Path

PACKAGE_PARENT = Path(__file__).parents[1]
PACKAGE_ROOT = PACKAGE_PARENT / "tesla_protocol"
MODULES = sorted(
    ".".join(path.relative_to(PACKAGE_PARENT).with_suffix("").parts)
    for path in PACKAGE_ROOT.rglob("*_pb2.py")
)

# Registers protos the way another library compiling Tesla's protos would: bare
# file names and Tesla's own packages, with conflicting definitions of symbols
# tesla_protocol also defines. Python protobuf has one default descriptor pool
# per process, so a shared file name or full symbol name raises TypeError.
FOREIGN = textwrap.dedent(
    """
    from google.protobuf import descriptor_pb2, descriptor_pool

    def register(name, package, message):
        proto = descriptor_pb2.FileDescriptorProto(name=name, package=package, syntax="proto3")
        proto.message_type.add(name=message).field.add(
            name="foreign", number=1,
            type=descriptor_pb2.FieldDescriptorProto.TYPE_STRING,
            label=descriptor_pb2.FieldDescriptorProto.LABEL_OPTIONAL,
        )
        descriptor_pool.Default().AddSerializedFile(proto.SerializeToString())

    register("car_server.proto", "CarServer", "Action")
    register("vcsec.proto", "VCSEC", "UnsignedMessage")
    register("universal_message.proto", "UniversalMessage", "RoutableMessage")
    register("vehicle_data.proto", "telemetry.vehicle_data", "Payload")
    register("tedapi.proto", "tedapi", "Message")
    """
)


def run_isolated(script: str) -> subprocess.CompletedProcess:
    # A fresh interpreter gets a fresh default pool, independent of whatever the
    # other tests in this process have already imported.
    env = dict(os.environ, PYTHONPATH=str(PACKAGE_PARENT))
    return subprocess.run([sys.executable, "-c", script], capture_output=True, text=True, env=env)


class DescriptorNamespaceTests(unittest.TestCase):
    def test_every_file_and_package_is_namespaced(self):
        import importlib

        for name in MODULES:
            with self.subTest(module=name):
                descriptor = importlib.import_module(name).DESCRIPTOR
                group = name.split(".")[1]
                self.assertTrue(descriptor.name.startswith(f"tesla_protocol/{group}/"), descriptor.name)
                self.assertTrue(descriptor.package.startswith("tesla_protocol."), descriptor.package)

    def test_loads_alongside_foreign_tesla_protos(self):
        imports = "\n".join(f"import {name}" for name in MODULES)
        for order, script in (
            ("foreign first", FOREIGN + imports),
            ("tesla_protocol first", imports + "\n" + FOREIGN),
        ):
            with self.subTest(order=order):
                result = run_isolated(script)
                self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
