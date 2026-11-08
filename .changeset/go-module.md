---
"@teslemetry/tesla-protocol": minor
---

Publish the protos as a Go module, `github.com/Teslemetry/tesla-protocol/go/v6`, versioned in lockstep with the npm and PyPI packages: one package per proto group (`telemetry`, `energy_device`, ...), and one per proto package under `command` (`command/carserver`, `command/vcsec`, ...). Like the Python package, the Go descriptors are registered under the `tesla_protocol.` namespace so they load alongside another copy of Tesla's protos.
