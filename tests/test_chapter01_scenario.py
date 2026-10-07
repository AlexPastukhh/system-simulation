import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from system_simulation.curriculum.finance.ch01 import ClaimsChapterScenario


class Chapter01ScenarioTests(unittest.TestCase):
    def test_complete_scenario_has_expected_events_and_final_state(self):
        scenario = ClaimsChapterScenario()
        scenario.run_complete(100)
        self.assertEqual(
            [frame.event for frame in scenario.trace.frames],
            ["InitialState", "ClaimIssued", "ClaimTransferred", "ClaimSettled"],
        )
        final = scenario.snapshot()
        self.assertEqual(final["active_claims"], 0)
        self.assertEqual(final["total_claim_assets"], "0.00 EUR")
        self.assertEqual(final["total_claim_liabilities"], "0.00 EUR")

    def test_transfer_trace_exposes_holder_change(self):
        scenario = ClaimsChapterScenario()
        scenario.issue_claim(100)
        frame = scenario.transfer_to_bob()
        changed = {c.path: (c.before, c.after) for c in frame.changes}
        self.assertEqual(changed["claim.holder"], ("Alice", "Bob"))
