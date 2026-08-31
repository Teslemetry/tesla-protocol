---
"@teslemetry/tesla-protocol": minor
---

Support protobuf 7.x in the Python package.

The published gencode is stamped 6.31.1, and protobuf's only compatibility rule
is that the runtime must not be older than the gencode stamp - Python gencode
back to 3.20 is supported through at least 8.x. The `protobuf<7` cap was
therefore the only thing keeping 7.x users out, not any real incompatibility, so
it moves to `<8` (matching the cap `googleapis-common-protos` already declares).
One wheel now serves both 6.x consumers such as Home Assistant, which constrains
`protobuf==6.33.6`, and 7.x consumers.

CI gains a `python-runtime` matrix that imports every generated module and runs
the golden fixture suite against the declared floor (6.32.0), Home Assistant's
pin (6.33.6), and the newest major (7.x). No generated code or wire format
changed.
