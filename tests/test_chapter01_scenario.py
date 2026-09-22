import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from system_simulation.curriculum.finance.ch01 import FinancialClaimsScenario, SCENARIO_GUIDES


class Chapter01ScenarioTests(unittest.TestCase):
    def test_complete_scenario_has_expected_events_and_final_state(self):
        scenario = FinancialClaimsScenario()
        scenario.run_complete(100)
        self.assertEqual(
            [frame.event for frame in scenario.trace.frames],
            ["InitialState", "ClaimIssued", "ClaimTransferred", "ClaimDischarged"],
        )
        final = scenario.snapshot()
        self.assertEqual(final["active_claims"], 0)
        self.assertEqual(final["total_claim_assets"], "0.00 EUR")
        self.assertEqual(final["total_claim_liabilities"], "0.00 EUR")

    def test_learning_steps_follow_issue_transfer_discharge(self):
        scenario = FinancialClaimsScenario()
        self.assertEqual(scenario.current_learning_step(), "issue")
        scenario.issue_claim(100)
        self.assertEqual(scenario.current_learning_step(), "transfer")
        scenario.transfer_to_bob()
        self.assertEqual(scenario.current_learning_step(), "discharge")
        scenario.discharge_with_bob()
        self.assertIsNone(scenario.current_learning_step())

    def test_transfer_trace_exposes_holder_change_without_liability_change(self):
        scenario = FinancialClaimsScenario()
        scenario.issue_claim(100)
        frame = scenario.transfer_to_bob()
        changed = {c.path: (c.before, c.after) for c in frame.changes}
        self.assertEqual(changed["claim.holder"], ("Alice", "Bob"))
        self.assertNotIn("issuer.liabilities", changed)
        self.assertNotIn("total_claim_liabilities", changed)

    def test_discharge_trace_exposes_both_sides_disappearing(self):
        scenario = FinancialClaimsScenario()
        scenario.issue_claim(100)
        scenario.transfer_to_bob()
        frame = scenario.discharge_with_bob()
        changed = {c.path: (c.before, c.after) for c in frame.changes}
        self.assertEqual(changed["bob.assets"], ("100.00 EUR", "0.00 EUR"))
        self.assertEqual(changed["issuer.liabilities"], ("100.00 EUR", "0.00 EUR"))
        self.assertEqual(changed["active_claims"], (1, 0))

    def test_scenario_guides_cover_all_core_learning_experiments(self):
        self.assertEqual(set(SCENARIO_GUIDES), {"issue", "transfer", "discharge"})
        for guide in SCENARIO_GUIDES.values():
            self.assertTrue(guide.prediction)
            self.assertTrue(guide.observable)
            self.assertTrue(guide.learning_payoff)
            self.assertTrue(guide.variation)


if __name__ == "__main__":
    unittest.main()
