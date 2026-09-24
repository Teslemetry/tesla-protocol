import json
import unittest
from pathlib import Path

from tesla_protocol.command.car_server_pb2 import Action, SetOutletsOnOffAction

FIXTURE = json.loads(
    (Path(__file__).parents[3] / "fixtures" / "golden" / "set_outlets_on_off.json").read_text()
)


class GoldenFixtureTests(unittest.TestCase):
    def test_outer_vehicle_action_wrapper_is_tag_2(self):
        self.assertEqual(FIXTURE["outer_field"]["tag"], 2)
        self.assertEqual(FIXTURE["outer_field"]["name"], "vehicleAction")

    def test_fixtures_round_trip_to_golden_bytes(self):
        for case in FIXTURE["cases"]:
            with self.subTest(case=case["name"]):
                self.assertEqual(
                    SetOutletsOnOffAction.OutletRequest.Value(case["payload"]["outlet_request"]),
                    case["payload"]["outlet_request_number"],
                )

                action = Action(
                    vehicleAction={
                        "setOutletsOnOffAction": SetOutletsOnOffAction(
                            outlet_request=case["payload"]["outlet_request_number"]
                        )
                    }
                )

                encoded = action.SerializeToString()
                self.assertEqual(encoded.hex(), case["hex"])

                decoded = Action.FromString(encoded)
                self.assertEqual(
                    decoded.vehicleAction.setOutletsOnOffAction.outlet_request,
                    case["payload"]["outlet_request_number"],
                )


if __name__ == "__main__":
    unittest.main()
