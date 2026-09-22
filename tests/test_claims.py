import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from system_simulation.domain import ClaimBook, ClaimError, Money, Party


class ClaimBookTests(unittest.TestCase):
    def setUp(self):
        self.issuer = Party("issuer", "Issuer")
        self.alice = Party("alice", "Alice")
        self.bob = Party("bob", "Bob")
        self.book = ClaimBook()

    def test_issue_creates_equal_asset_and_liability(self):
        self.book.issue(self.issuer, self.alice, Money.of(100))
        self.assertEqual(str(self.book.assets_of(self.alice)), "100.00 EUR")
        self.assertEqual(str(self.book.liabilities_of(self.issuer)), "100.00 EUR")
        self.assertEqual(self.book.total_assets(), self.book.total_liabilities())

    def test_transfer_changes_holder_not_total_claims(self):
        claim = self.book.issue(self.issuer, self.alice, Money.of(100))
        self.book.transfer(claim.id, from_holder=self.alice, to_holder=self.bob)
        self.assertEqual(str(self.book.assets_of(self.alice)), "0.00 EUR")
        self.assertEqual(str(self.book.assets_of(self.bob)), "100.00 EUR")
        self.assertEqual(str(self.book.liabilities_of(self.issuer)), "100.00 EUR")
        self.assertEqual(str(self.book.total_assets()), "100.00 EUR")

    def test_settlement_extinguishes_both_sides(self):
        claim = self.book.issue(self.issuer, self.alice, Money.of(100))
        self.book.transfer(claim.id, from_holder=self.alice, to_holder=self.bob)
        self.book.settle(claim.id, holder=self.bob)
        self.assertEqual(str(self.book.total_assets()), "0.00 EUR")
        self.assertEqual(str(self.book.total_liabilities()), "0.00 EUR")
        self.assertEqual(len(self.book.claims), 0)

    def test_non_holder_cannot_transfer(self):
        claim = self.book.issue(self.issuer, self.alice, Money.of(100))
        with self.assertRaises(ClaimError):
            self.book.transfer(claim.id, from_holder=self.bob, to_holder=self.alice)

    def test_second_currency_is_rejected(self):
        self.book.issue(self.issuer, self.alice, Money.of(100, "EUR"))
        with self.assertRaises(ClaimError):
            self.book.issue(self.issuer, self.bob, Money.of(10, "USD"))


class ClaimBookCurrencyContextTests(unittest.TestCase):
    def test_settlement_preserves_zero_balance_currency(self):
        issuer = Party("issuer", "Issuer")
        alice = Party("alice", "Alice")
        book = ClaimBook()
        claim = book.issue(issuer, alice, Money.of(100, "USD"))
        book.settle(claim.id, holder=alice)
        self.assertEqual(str(book.total_assets()), "0.00 USD")
        self.assertEqual(str(book.total_liabilities()), "0.00 USD")


class ClaimBookPersistentCurrencyContextTests(unittest.TestCase):
    def test_currency_cannot_change_after_full_settlement(self):
        issuer = Party("issuer", "Issuer")
        alice = Party("alice", "Alice")
        bob = Party("bob", "Bob")
        book = ClaimBook()
        claim = book.issue(issuer, alice, Money.of(100, "USD"))
        book.settle(claim.id, holder=alice)

        with self.assertRaises(ClaimError):
            book.issue(issuer, bob, Money.of(10, "EUR"))
