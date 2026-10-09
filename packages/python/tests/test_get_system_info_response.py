import json
import unittest
from pathlib import Path

from tesla_protocol.energy_device import common_api_pb2, device_pb2, transport_pb2

FIXTURE = json.loads(
    (Path(__file__).parents[3] / "fixtures" / "golden" / "get_system_info_response.json").read_text()
)


def build_envelope():
    envelope = FIXTURE["envelope"]
    payload = FIXTURE["payload"]
    msg = transport_pb2.MessageEnvelope(delivery_channel=envelope["delivery_channel_number"])
    msg.sender.din = envelope["sender_din"]
    msg.recipient.local = envelope["recipient_local_number"]
    info = msg.common.get_system_info_response
    info.device_id.part_number = payload["device_id"]["part_number"]
    info.device_id.serial_number = payload["device_id"]["serial_number"]
    info.din = payload["din"]
    info.firmware_version.version = payload["firmware_version"]["version"]
    info.firmware_version.githash = bytes.fromhex(payload["firmware_version"]["githash_hex"])
    info.system_update.update_status = payload["system_update"]["update_status"]
    info.device_type = payload["device_type_number"]
    for radio in payload["compliance_information"]:
        entry = info.compliance_information.radio_legal_information.add()
        entry.manufacturer.value = radio["manufacturer"]
        entry.model.value = radio["model"]
        entry.fcc_id.value = radio["fcc_id"]
        entry.ic_id.value = radio["ic_id"]
    return msg


class GetSystemInfoResponseFixtureTests(unittest.TestCase):
    def test_wrapper_tags(self):
        fields = transport_pb2.MessageEnvelope.DESCRIPTOR.fields_by_name
        self.assertEqual(fields["common"].number, FIXTURE["outer_field"]["tag"])
        fields = common_api_pb2.CommonMessages.DESCRIPTOR.fields_by_name
        self.assertEqual(fields["get_system_info_response"].number, FIXTURE["message_field"]["tag"])

    def test_decodes_device_reply(self):
        envelope = FIXTURE["envelope"]
        payload = FIXTURE["payload"]
        msg = transport_pb2.MessageEnvelope.FromString(bytes.fromhex(FIXTURE["device_reply_hex"]))
        self.assertEqual(msg.delivery_channel, envelope["delivery_channel_number"])
        self.assertEqual(msg.sender.din, envelope["sender_din"])
        self.assertEqual(msg.recipient.local, envelope["recipient_local_number"])
        self.assertEqual(msg.common.WhichOneof("message"), "get_system_info_response")

        info = msg.common.get_system_info_response
        self.assertEqual(info.device_id.part_number, payload["device_id"]["part_number"])
        self.assertEqual(info.device_id.serial_number, payload["device_id"]["serial_number"])
        self.assertEqual(info.din, payload["din"])
        self.assertEqual(info.firmware_version.version, payload["firmware_version"]["version"])
        self.assertEqual(info.firmware_version.githash.hex(), payload["firmware_version"]["githash_hex"])
        self.assertEqual(info.system_update.update_status, payload["system_update"]["update_status"])
        self.assertEqual(device_pb2.DeviceType.Value(payload["device_type"]), payload["device_type_number"])
        self.assertEqual(info.device_type, payload["device_type_number"])
        self.assertEqual(
            [
                {
                    "manufacturer": r.manufacturer.value,
                    "model": r.model.value,
                    "fcc_id": r.fcc_id.value,
                    "ic_id": r.ic_id.value,
                }
                for r in info.compliance_information.radio_legal_information
            ],
            payload["compliance_information"],
        )

    def test_encodes_modelled_fields_to_golden_bytes(self):
        self.assertEqual(build_envelope().SerializeToString().hex(), FIXTURE["modelled_hex"])


if __name__ == "__main__":
    unittest.main()
