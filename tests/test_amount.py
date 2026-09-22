import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from system_simulation.domain import CurrencyAmount


class CurrencyAmountTests(unittest.TestCase):
    def test_amount_quantizes_to_cents(self):
        self.assertEqual(str(CurrencyAmount.of("10.126")), "10.13 EUR")

    def test_negative_amount_is_rejected(self):
        with self.assertRaises(ValueError):
            CurrencyAmount.of("-1")

    def test_currency_code_is_normalized(self):
        self.assertEqual(str(CurrencyAmount.of(10, "usd")), "10.00 USD")

    def test_currency_code_must_be_three_letters(self):
        with self.assertRaises(ValueError):
            CurrencyAmount.of(10, "EU")
        with self.assertRaises(ValueError):
            CurrencyAmount.of(10, "E1R")


if __name__ == "__main__":
    unittest.main()
