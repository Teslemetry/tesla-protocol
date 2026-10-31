import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

import { MessageEnvelope } from "../dist/energy_device/transport.mjs";
import { TEGAPIScheduleManualBackupEventRequest } from "../dist/energy_device/teg_api.mjs";

const fixturePath = fileURLToPath(
  new URL("../../../fixtures/golden/energy_v1r_envelopes.json", import.meta.url),
);
const fixture = JSON.parse(readFileSync(fixturePath, "utf8"));

const MAX_UINT64 = "18446744073709551615";

function hex(bytes: Uint8Array): string {
  return Buffer.from(bytes).toString("hex");
}

function camel(name: string): string {
  return name.replace(/_([a-z])/g, (_, c: string) => c.toUpperCase());
}

for (const c of fixture.cases) {
  test(`golden fixture: ${c.name}`, () => {
    for (const [i, m] of c.messages.entries()) {
      const decoded = MessageEnvelope.decode(Buffer.from(m.hex, "hex"));

      const [outer, inner] = m.payload_case.split(".").map(camel);
      const payload = (decoded as any)[outer]?.[inner];
      assert.ok(payload, `${c.name}[${i}]: ${m.payload_case} is set`);

      const encoded = MessageEnvelope.encode(decoded).finish();
      assert.equal(hex(encoded), m.canonical_hex ?? m.hex, `${c.name}[${i}]: re-encode mismatch`);

      if (m.scheduling_info) {
        const info =
          payload.schedulingInfo ?? payload.manualBackupEvent?.schedulingInfo;
        assert.ok(info, `${c.name}[${i}]: schedulingInfo is set`);
        assert.equal(info.startTime?.getTime(), m.scheduling_info.start_time_seconds * 1000);
        assert.equal(info.durationSeconds, m.scheduling_info.duration_seconds);
        assert.equal(typeof info.priority, "string");
        assert.equal(info.priority, m.scheduling_info.priority);
      }
    }
  });
}

test("ControlEventSchedulingInfo.priority encodes and decodes 2^64 - 1 as a string", () => {
  const reply = fixture.cases.find((c: any) => c.name === "get_backup_events_reply_max_priority");
  const decoded = MessageEnvelope.decode(Buffer.from(reply.messages[0].hex, "hex"));
  assert.equal(
    decoded.teg?.getBackupEventsResponse?.manualBackupEvent?.schedulingInfo?.priority,
    MAX_UINT64,
  );

  const schedule = fixture.cases.find((c: any) => c.name === "schedule_max_backup_7200");
  const expected = MessageEnvelope.decode(Buffer.from(schedule.messages[1].hex, "hex"));
  const built = MessageEnvelope.fromPartial({
    ...expected,
    teg: {
      scheduleManualBackupEventRequest: TEGAPIScheduleManualBackupEventRequest.fromPartial({
        schedulingInfo: {
          startTime: new Date(1800000000 * 1000),
          durationSeconds: 7200,
          priority: MAX_UINT64,
        },
      }),
    },
  });
  assert.equal(hex(MessageEnvelope.encode(built).finish()), schedule.messages[1].hex);

  const json = MessageEnvelope.toJSON(decoded) as any;
  assert.equal(json.teg.getBackupEventsResponse.manualBackupEvent.schedulingInfo.priority, MAX_UINT64);
});
