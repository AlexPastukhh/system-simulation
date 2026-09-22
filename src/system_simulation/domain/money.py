from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_EVEN

_CENT = Decimal("0.01")


@dataclass(frozen=True, order=True)
class Money:
    amount: Decimal
    currency: str = "EUR"

    def __post_init__(self) -> None:
        amount = Decimal(self.amount).quantize(_CENT, rounding=ROUND_HALF_EVEN)
        if amount < 0:
            raise ValueError("Money cannot be negative.")
        if len(self.currency) != 3:
            raise ValueError("Currency must be a three-letter code.")
        object.__setattr__(self, "amount", amount)
        object.__setattr__(self, "currency", self.currency.upper())

    @classmethod
    def of(cls, amount: int | float | str | Decimal, currency: str = "EUR") -> "Money":
        return cls(Decimal(str(amount)), currency)

    def __str__(self) -> str:
        return f"{self.amount:.2f} {self.currency}"
