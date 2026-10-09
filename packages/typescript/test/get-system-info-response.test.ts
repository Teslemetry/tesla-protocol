import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

import { MessageEnvelope } from "../dist/energy_device/transport.mjs";
import { DeviceType } from "../dist/energy_device/device.mjs";

const fixturePath = fileURLToPath(
  new URL("../../../fixtures/golden/get_system_info_response.json", import.meta.url),
);
const fixture = JSON.parse(readFileSync(fixturePath, "utf8"));

function hex(bytes: Uint8Array): string {
  return Buffer.from(bytes).toString("hex");
}

test("golden fixture: decodes the device reply", () => {
  const { envelope, payload } = fixture;
  const msg = MessageEnvelope.decode(Buffer.from(fixture.device_reply_hex, "hex"));
  assert.equal(msg.deliveryChannel, envelope.delivery_channel_number);
  assert.equal(msg.sender?.din, envelope.sender_din);
  assert.equal(msg.recipient?.local, envelope.recipient_local_number);

  const info = msg.common?.getSystemInfoResponse;
  assert.ok(info, "common.getSystemInfoResponse is set");
  assert.deepEqual(
    { partNumber: info.deviceId?.partNumber, serialNumber: info.deviceId?.serialNumber },
    { partNumber: payload.device_id.part_number, serialNumber: payload.device_id.serial_number },
  );
  assert.equal(info.din, payload.din);
  assert.equal(info.firmwareVersion?.version, payload.firmware_version.version);
  assert.equal(hex(info.firmwareVersion?.githash ?? new Uint8Array()), payload.firmware_version.githash_hex);
  assert.equal(info.systemUpdate?.updateStatus, payload.system_update.update_status);
  assert.equal(DeviceType[payload.device_type as keyof typeof DeviceType], payload.device_type_number);
  assert.equal(info.deviceType, payload.device_type_number);
  assert.deepEqual(
    (info.complianceInformation?.radioLegalInformation ?? []).map((r) => ({
      manufacturer: r.manufacturer,
      model: r.model,
      fcc_id: r.fccId,
      ic_id: r.icId,
    })),
    payload.compliance_information,
  );
});

test("golden fixture: encodes the modelled fields to golden bytes", () => {
  const { envelope, payload } = fixture;
  const msg = MessageEnvelope.fromPartial({
    deliveryChannel: envelope.delivery_channel_number,
    sender: { din: envelope.sender_din },
    recipient: { local: envelope.recipient_local_number },
    common: {
      getSystemInfoResponse: {
        deviceId: {
          partNumber: payload.device_id.part_number,
          serialNumber: payload.device_id.serial_number,
        },
        din: payload.din,
        firmwareVersion: {
          version: payload.firmware_version.version,
          githash: Buffer.from(payload.firmware_version.githash_hex, "hex"),
        },
        systemUpdate: { updateStatus: payload.system_update.update_status },
        deviceType: payload.device_type_number,
        complianceInformation: {
          radioLegalInformation: payload.compliance_information.map(
            (r: { manufacturer: string; model: string; fcc_id: string; ic_id: string }) => ({
              manufacturer: r.manufacturer,
              model: r.model,
              fccId: r.fcc_id,
              icId: r.ic_id,
            }),
          ),
        },
      },
    },
  });
  assert.equal(hex(MessageEnvelope.encode(msg).finish()), fixture.modelled_hex);
});
