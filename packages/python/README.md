# tesla-protocol

Python protobuf bindings (`_pb2` modules with `.pyi` stubs) for Tesla's
vehicle-command, fleet-telemetry and energy device protocols.

```sh
pip install tesla-protocol
```

```python
from tesla_protocol.command import car_server_pb2
from tesla_protocol.telemetry import vehicle_data_pb2
```

Versioned in lockstep with the npm package `@teslemetry/tesla-protocol` from
the same repository. See the
[repository README](https://github.com/Teslemetry/tesla-protocol) for the
release model.
