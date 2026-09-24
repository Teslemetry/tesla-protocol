import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

import { Action, SetOutletsOnOffAction_OutletRequest } from "../dist/command/car_server.mjs";

const fixturePath = fileURLToPath(
  new URL("../../../fixtures/golden/set_outlets_on_off.json", import.meta.url),
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
    assert.equal(
      SetOutletsOnOffAction_OutletRequest[c.payload.outlet_request as keyof typeof SetOutletsOnOffAction_OutletRequest],
      c.payload.outlet_request_number,
      `enum value mismatch for ${c.payload.outlet_request}`,
    );

    const action = Action.fromJSON({
      vehicleAction: {
        setOutletsOnOffAction: { outletRequest: c.payload.outlet_request_number },
      },
    });

    const encoded = Action.encode(action).finish();
    assert.equal(hex(encoded), c.hex, `encode mismatch for ${c.name}`);

    const decoded = Action.decode(encoded);
    assert.equal(
      decoded.vehicleAction?.setOutletsOnOffAction?.outletRequest ?? 0,
      c.payload.outlet_request_number,
    );
  });
}
