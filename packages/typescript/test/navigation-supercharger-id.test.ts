import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

import { Action } from "../dist/command/car_server.mjs";

const fixturePath = fileURLToPath(
  new URL("../../../fixtures/golden/navigation_supercharger_id.json", import.meta.url),
);
const fixture = JSON.parse(readFileSync(fixturePath, "utf8"));

function hex(bytes: Uint8Array): string {
  return Buffer.from(bytes).toString("hex");
}

test("Action.vehicleAction outer wrapper is tag 2", () => {
  assert.equal(fixture.outer_field.tag, 2);
  assert.equal(fixture.outer_field.name, "vehicleAction");
});

for (const c of fixture.cases) {
  test(`golden fixture: ${c.name}`, () => {
    const action = Action.fromJSON({
      vehicleAction: {
        navigationSuperchargerRequest: {
          id: c.payload.id,
          remoteNavTripOrder: c.payload.remote_nav_trip_order_number,
        },
      },
    });

    const encoded = Action.encode(action).finish();
    assert.equal(hex(encoded), c.hex, `encode mismatch for ${c.name}`);

    const decoded = Action.decode(encoded);
    assert.equal(
      decoded.vehicleAction?.navigationSuperchargerRequest?.id ?? 0,
      c.payload.id,
    );
    assert.equal(
      decoded.vehicleAction?.navigationSuperchargerRequest?.remoteNavTripOrder ?? 0,
      c.payload.remote_nav_trip_order_number,
    );
  });
}
