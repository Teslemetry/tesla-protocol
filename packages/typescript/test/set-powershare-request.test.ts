import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

import { Action, SetPowershareRequestAction_PowershareRequest } from "../dist/command/car_server.mjs";

const fixturePath = fileURLToPath(
  new URL("../../../fixtures/golden/set_powershare_request.json", import.meta.url),
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
      SetPowershareRequestAction_PowershareRequest[c.payload.powershare_request as keyof typeof SetPowershareRequestAction_PowershareRequest],
      c.payload.powershare_request_number,
      `enum value mismatch for ${c.payload.powershare_request}`,
    );

    const action = Action.fromJSON({
      vehicleAction: {
        setPowershareRequestAction: { powershareRequest: c.payload.powershare_request_number },
      },
    });

    const encoded = Action.encode(action).finish();
    assert.equal(hex(encoded), c.hex, `encode mismatch for ${c.name}`);

    const decoded = Action.decode(encoded);
    assert.equal(
      decoded.vehicleAction?.setPowershareRequestAction?.powershareRequest ?? 0,
      c.payload.powershare_request_number,
    );
  });
}
