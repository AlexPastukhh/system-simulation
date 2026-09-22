import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from system_simulation.domain import Money


class MoneyTests(unittest.TestCase):
    def test_money_quantizes_to_cents(self):
        self.assertEqual(str(Money.of("10.126")), "10.13 EUR")

    def test_negative_money_is_rejected(self):
        with self.assertRaises(ValueError):
            Money.of("-1")
