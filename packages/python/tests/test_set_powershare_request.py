import json
import unittest
from pathlib import Path

from tesla_protocol.command.car_server_pb2 import Action, SetPowershareRequestAction

FIXTURE = json.loads(
    (Path(__file__).parents[3] / "fixtures" / "golden" / "set_powershare_request.json").read_text()
)


class GoldenFixtureTests(unittest.TestCase):
    def test_outer_vehicle_action_wrapper_is_tag_2(self):
        self.assertEqual(FIXTURE["outer_field"]["tag"], 2)
        self.assertEqual(FIXTURE["outer_field"]["name"], "vehicleAction")

    def test_fixtures_round_trip_to_golden_bytes(self):
        for case in FIXTURE["cases"]:
            with self.subTest(case=case["name"]):
                self.assertEqual(
                    SetPowershareRequestAction.PowershareRequest.Value(case["payload"]["powershare_request"]),
                    case["payload"]["powershare_request_number"],
                )

                action = Action(
                    vehicleAction={
                        "setPowershareRequestAction": SetPowershareRequestAction(
                            powershare_request=case["payload"]["powershare_request_number"]
                        )
                    }
                )

                encoded = action.SerializeToString()
                self.assertEqual(encoded.hex(), case["hex"])

                decoded = Action.FromString(encoded)
                self.assertEqual(
                    decoded.vehicleAction.setPowershareRequestAction.powershare_request,
                    case["payload"]["powershare_request_number"],
                )


if __name__ == "__main__":
    unittest.main()
