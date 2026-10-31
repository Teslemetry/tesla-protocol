import json
import unittest
from pathlib import Path

from tesla_protocol.energy_device.transport_pb2 import MessageEnvelope

FIXTURE = json.loads(
    (Path(__file__).parents[3] / "fixtures" / "golden" / "energy_v1r_envelopes.json").read_text()
)

MAX_UINT64 = 2**64 - 1


class EnergyV1rEnvelopeTests(unittest.TestCase):
    def test_fixtures_round_trip_to_golden_bytes(self):
        for case in FIXTURE["cases"]:
            for i, message in enumerate(case["messages"]):
                with self.subTest(case=case["name"], message=i):
                    decoded = MessageEnvelope.FromString(bytes.fromhex(message["hex"]))

                    outer, inner = message["payload_case"].split(".")
                    self.assertEqual(decoded.WhichOneof("payload"), outer)
                    group = getattr(decoded, outer)
                    self.assertTrue(group.HasField(inner))
                    payload = getattr(group, inner)

                    self.assertEqual(
                        decoded.SerializeToString().hex(),
                        message.get("canonical_hex", message["hex"]),
                    )

                    expected = message.get("scheduling_info")
                    if expected:
                        info = (
                            payload.scheduling_info
                            if "scheduling_info" in payload.DESCRIPTOR.fields_by_name
                            else payload.manual_backup_event.scheduling_info
                        )
                        self.assertEqual(info.start_time.seconds, expected["start_time_seconds"])
                        self.assertEqual(info.duration_seconds, expected["duration_seconds"])
                        self.assertEqual(str(info.priority), expected["priority"])

    def test_max_priority_reply_decodes(self):
        reply = next(c for c in FIXTURE["cases"] if c["name"] == "get_backup_events_reply_max_priority")
        decoded = MessageEnvelope.FromString(bytes.fromhex(reply["messages"][0]["hex"]))
        self.assertEqual(
            decoded.teg.get_backup_events_response.manual_backup_event.scheduling_info.priority,
            MAX_UINT64,
        )


if __name__ == "__main__":
    unittest.main()
