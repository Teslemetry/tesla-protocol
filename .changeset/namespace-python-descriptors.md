---
"@teslemetry/tesla-protocol": major
---

Register every Python module under a `tesla_protocol` namespace in the protobuf descriptor pool. Each file is now registered as `tesla_protocol/<group>/<file>.proto` (for example `tesla_protocol/command/car_server.proto`) and each package as `tesla_protocol.<package>` (for example `tesla_protocol.CarServer`). Before this change, the bare file names and Tesla's generic package names (`CarServer`, `VCSEC`, `UniversalMessage`, ...) clashed with any other library that loads Tesla's protos into the same Python process: the import failed with `TypeError: Couldn't build proto file into descriptor pool`.

Python import paths do not change (`from tesla_protocol.command import car_server_pb2` still works), and the encoded bytes of every message do not change, except where a full type name is itself serialized: a `google.protobuf.Any` packed in Python now carries a `tesla_protocol.`-prefixed `type_url`. Code that uses descriptor full names does change: `DESCRIPTOR.full_name`, `descriptor_pool.FindMessageTypeByName("CarServer.Action")` and `google.protobuf.Any` type URLs now carry the `tesla_protocol.` prefix. The only `Any` field is `teslapower.Status.details`. The generated imports between modules are now absolute (`from tesla_protocol.command import ...`).

The TypeScript package is unchanged. It has no global descriptor registry, so it keeps upstream's package names; its major version moves only because the two packages release in lockstep.
