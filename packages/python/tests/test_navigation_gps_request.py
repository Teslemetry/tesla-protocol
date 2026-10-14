import json
import unittest
from pathlib import Path

from tesla_protocol.command.car_server_pb2 import Action, NavigationGpsRequest

FIXTURE = json.loads(
    (
        Path(__file__).parents[3] / "fixtures" / "golden" / "navigation_gps_request.json"
    ).read_text()
)


class GoldenFixtureTests(unittest.TestCase):
    def test_outer_vehicle_action_wrapper_is_tag_2(self):
        self.assertEqual(FIXTURE["outer_field"]["tag"], 2)
        self.assertEqual(FIXTURE["outer_field"]["name"], "vehicleAction")

    def test_fixtures_round_trip_to_golden_bytes(self):
        for case in FIXTURE["cases"]:
            with self.subTest(case=case["name"]):
                self.assertEqual(case["vehicle_action_field"]["tag"], 53)
                action = Action(
                    vehicleAction={
                        "navigationGpsRequest": NavigationGpsRequest(
                            lat=case["payload"]["lat"],
                            lon=case["payload"]["lon"],
                            order=case["payload"]["order_number"],
                        )
                    }
                )

                encoded = action.SerializeToString()
                self.assertEqual(encoded.hex(), case["hex"])

                decoded = Action.FromString(encoded)
                request = decoded.vehicleAction.navigationGpsRequest
                self.assertEqual(request.lat, case["payload"]["lat"])
                self.assertEqual(request.lon, case["payload"]["lon"])
                self.assertEqual(request.order, case["payload"]["order_number"])


if __name__ == "__main__":
    unittest.main()
