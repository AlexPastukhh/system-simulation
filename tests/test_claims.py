import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from system_simulation.domain import ClaimBook, ClaimError, CurrencyAmount, Party


class ClaimBookTests(unittest.TestCase):
    def setUp(self):
        self.issuer = Party("issuer", "Issuer")
        self.alice = Party("alice", "Alice")
        self.bob = Party("bob", "Bob")
        self.book = ClaimBook()

    def test_issue_creates_equal_claim_asset_and_liability(self):
        self.book.issue(self.issuer, self.alice, CurrencyAmount.of(100))
        self.assertEqual(str(self.book.assets_of(self.alice)), "100.00 EUR")
        self.assertEqual(str(self.book.liabilities_of(self.issuer)), "100.00 EUR")
        self.assertEqual(self.book.total_assets(), self.book.total_liabilities())

    def test_transfer_changes_holder_not_total_claims(self):
        claim = self.book.issue(self.issuer, self.alice, CurrencyAmount.of(100))
        self.book.transfer(claim.id, from_holder=self.alice, to_holder=self.bob)
        self.assertEqual(str(self.book.assets_of(self.alice)), "0.00 EUR")
        self.assertEqual(str(self.book.assets_of(self.bob)), "100.00 EUR")
        self.assertEqual(str(self.book.liabilities_of(self.issuer)), "100.00 EUR")
        self.assertEqual(str(self.book.total_assets()), "100.00 EUR")

    def test_discharge_extinguishes_claim_asset_and_liability(self):
        claim = self.book.issue(self.issuer, self.alice, CurrencyAmount.of(100))
        self.book.transfer(claim.id, from_holder=self.alice, to_holder=self.bob)
        self.book.discharge(claim.id, issuer=self.issuer, holder=self.bob)
        self.assertEqual(str(self.book.total_assets()), "0.00 EUR")
        self.assertEqual(str(self.book.total_liabilities()), "0.00 EUR")
        self.assertEqual(len(self.book.claims), 0)

    def test_non_holder_cannot_transfer(self):
        claim = self.book.issue(self.issuer, self.alice, CurrencyAmount.of(100))
        with self.assertRaises(ClaimError):
            self.book.transfer(claim.id, from_holder=self.bob, to_holder=self.alice)

    def test_non_holder_cannot_discharge(self):
        claim = self.book.issue(self.issuer, self.alice, CurrencyAmount.of(100))
        with self.assertRaises(ClaimError):
            self.book.discharge(claim.id, issuer=self.issuer, holder=self.bob)

    def test_wrong_issuer_cannot_discharge(self):
        claim = self.book.issue(self.issuer, self.alice, CurrencyAmount.of(100))
        with self.assertRaises(ClaimError):
            self.book.discharge(claim.id, issuer=self.bob, holder=self.alice)

    def test_transfer_to_issuer_is_not_modeled_as_transfer(self):
        claim = self.book.issue(self.issuer, self.alice, CurrencyAmount.of(100))
        with self.assertRaisesRegex(ClaimError, "use discharge"):
            self.book.transfer(claim.id, from_holder=self.alice, to_holder=self.issuer)

    def test_second_currency_is_rejected(self):
        self.book.issue(self.issuer, self.alice, CurrencyAmount.of(100, "EUR"))
        with self.assertRaises(ClaimError):
            self.book.issue(self.issuer, self.bob, CurrencyAmount.of(10, "USD"))


class ClaimBookCurrencyContextTests(unittest.TestCase):
    def test_discharge_preserves_zero_balance_currency(self):
        issuer = Party("issuer", "Issuer")
        alice = Party("alice", "Alice")
        book = ClaimBook()
        claim = book.issue(issuer, alice, CurrencyAmount.of(100, "USD"))
        book.discharge(claim.id, issuer=issuer, holder=alice)
        self.assertEqual(str(book.total_assets()), "0.00 USD")
        self.assertEqual(str(book.total_liabilities()), "0.00 USD")

    def test_currency_cannot_change_after_full_discharge(self):
        issuer = Party("issuer", "Issuer")
        alice = Party("alice", "Alice")
        bob = Party("bob", "Bob")
        book = ClaimBook()
        claim = book.issue(issuer, alice, CurrencyAmount.of(100, "USD"))
        book.discharge(claim.id, issuer=issuer, holder=alice)

        with self.assertRaises(ClaimError):
            book.issue(issuer, bob, CurrencyAmount.of(10, "EUR"))


if __name__ == "__main__":
    unittest.main()
