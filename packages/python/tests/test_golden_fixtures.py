import json
import unittest
from pathlib import Path

from tesla_protocol.command.car_server_pb2 import Action, AutoStwHeatAction, StwHeatLevelAction

FIXTURE = json.loads(
    (Path(__file__).parents[3] / "fixtures" / "golden" / "steering_wheel_heat.json").read_text()
)


class GoldenFixtureTests(unittest.TestCase):
    def test_outer_vehicle_action_wrapper_is_tag_2(self):
        self.assertEqual(FIXTURE["outer_field"]["tag"], 2)
        self.assertEqual(FIXTURE["outer_field"]["name"], "vehicleAction")

    def test_fixtures_round_trip_to_golden_bytes(self):
        for case in FIXTURE["cases"]:
            with self.subTest(case=case["name"]):
                field = case["vehicle_action_field"]["name"]
                if field == "autoStwHeatAction":
                    action = Action(
                        vehicleAction={
                            "autoStwHeatAction": AutoStwHeatAction(on=case["payload"]["on"])
                        }
                    )
                elif field == "stwHeatLevelAction":
                    action = Action(
                        vehicleAction={
                            "stwHeatLevelAction": StwHeatLevelAction(
                                stw_heat_level=case["payload"]["stw_heat_level_number"]
                            )
                        }
                    )
                else:
                    self.fail(f"unhandled fixture field: {field}")

                encoded = action.SerializeToString()
                self.assertEqual(encoded.hex(), case["hex"])

                decoded = Action.FromString(encoded)
                if field == "autoStwHeatAction":
                    self.assertEqual(decoded.vehicleAction.autoStwHeatAction.on, case["payload"]["on"])
                else:
                    self.assertEqual(
                        decoded.vehicleAction.stwHeatLevelAction.stw_heat_level,
                        case["payload"]["stw_heat_level_number"],
                    )


if __name__ == "__main__":
    unittest.main()
