from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_EVEN

_CENT = Decimal("0.01")


@dataclass(frozen=True, order=True)
class CurrencyAmount:
    """A quantity denominated in a currency unit, not a monetary instrument."""

    amount: Decimal
    currency: str = "EUR"

    def __post_init__(self) -> None:
        amount = Decimal(self.amount).quantize(_CENT, rounding=ROUND_HALF_EVEN)
        currency = self.currency.upper()
        if amount < 0:
            raise ValueError("CurrencyAmount cannot be negative.")
        if len(currency) != 3 or not currency.isalpha():
            raise ValueError("Currency must be a three-letter alphabetic code.")
        object.__setattr__(self, "amount", amount)
        object.__setattr__(self, "currency", currency)

    @classmethod
    def of(
        cls,
        amount: int | float | str | Decimal,
        currency: str = "EUR",
    ) -> "CurrencyAmount":
        return cls(Decimal(str(amount)), currency)

    def __str__(self) -> str:
        return f"{self.amount:.2f} {self.currency}"
