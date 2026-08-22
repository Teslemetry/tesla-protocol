import json
import unittest
from pathlib import Path

from tesla_protocol.command.car_server_pb2 import Action, NavigationSuperchargerRequest

FIXTURE = json.loads(
    (
        Path(__file__).parents[3] / "fixtures" / "golden" / "navigation_supercharger_id.json"
    ).read_text()
)


class GoldenFixtureTests(unittest.TestCase):
    def test_outer_vehicle_action_wrapper_is_tag_2(self):
        self.assertEqual(FIXTURE["outer_field"]["tag"], 2)
        self.assertEqual(FIXTURE["outer_field"]["name"], "vehicleAction")

    def test_fixtures_round_trip_to_golden_bytes(self):
        for case in FIXTURE["cases"]:
            with self.subTest(case=case["name"]):
                action = Action(
                    vehicleAction={
                        "navigationSuperchargerRequest": NavigationSuperchargerRequest(
                            id=case["payload"]["id"],
                            remote_nav_trip_order=case["payload"][
                                "remote_nav_trip_order_number"
                            ],
                        )
                    }
                )

                encoded = action.SerializeToString()
                self.assertEqual(encoded.hex(), case["hex"])

                decoded = Action.FromString(encoded)
                self.assertEqual(
                    decoded.vehicleAction.navigationSuperchargerRequest.id,
                    case["payload"]["id"],
                )
                self.assertEqual(
                    decoded.vehicleAction.navigationSuperchargerRequest.remote_nav_trip_order,
                    case["payload"]["remote_nav_trip_order_number"],
                )


if __name__ == "__main__":
    unittest.main()
