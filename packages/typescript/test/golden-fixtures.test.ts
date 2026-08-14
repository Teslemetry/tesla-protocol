import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

import { Action } from "../dist/command/car_server.mjs";
import { StwHeatLevel } from "../dist/command/common.mjs";

const fixturePath = fileURLToPath(
  new URL("../../../fixtures/golden/steering_wheel_heat.json", import.meta.url),
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
    let action;
    if (c.vehicle_action_field.name === "autoStwHeatAction") {
      action = Action.fromJSON({
        vehicleAction: { autoStwHeatAction: { on: c.payload.on } },
      });
    } else if (c.vehicle_action_field.name === "stwHeatLevelAction") {
      action = Action.fromJSON({
        vehicleAction: {
          stwHeatLevelAction: { stwHeatLevel: c.payload.stw_heat_level_number },
        },
      });
    } else {
      throw new Error(`unhandled fixture field: ${c.vehicle_action_field.name}`);
    }

    const encoded = Action.encode(action).finish();
    assert.equal(hex(encoded), c.hex, `encode mismatch for ${c.name}`);

    const decoded = Action.decode(encoded);
    if (c.vehicle_action_field.name === "autoStwHeatAction") {
      assert.equal(decoded.vehicleAction?.autoStwHeatAction?.on ?? false, c.payload.on);
    } else {
      assert.equal(
        decoded.vehicleAction?.stwHeatLevelAction?.stwHeatLevel ?? StwHeatLevel.StwHeatLevel_Unknown,
        c.payload.stw_heat_level_number,
      );
    }
  });
}
