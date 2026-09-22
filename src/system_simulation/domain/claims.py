from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID, uuid4

from .amount import CurrencyAmount


class ClaimError(ValueError):
    pass


@dataclass(frozen=True)
class Party:
    id: str
    name: str


@dataclass(frozen=True)
class Claim:
    id: UUID
    issuer: Party
    holder: Party
    amount: CurrencyAmount

    @classmethod
    def create(
        cls,
        issuer: Party,
        holder: Party,
        amount: CurrencyAmount,
    ) -> "Claim":
        if issuer.id == holder.id:
            raise ClaimError("Issuer and holder must be different parties.")
        if amount.amount == 0:
            raise ClaimError("A claim must have a positive amount.")
        return cls(uuid4(), issuer, holder, amount)


class ClaimBook:
    """M01: minimal domain model for bilateral financial claims."""

    def __init__(self) -> None:
        self._claims: dict[UUID, Claim] = {}
        self._currency_code: str | None = None

    @property
    def claims(self) -> tuple[Claim, ...]:
        return tuple(self._claims.values())

    def issue(
        self,
        issuer: Party,
        holder: Party,
        amount: CurrencyAmount,
    ) -> Claim:
        self._require_currency_compatible(amount)
        if self._currency_code is None:
            self._currency_code = amount.currency
        claim = Claim.create(issuer, holder, amount)
        self._claims[claim.id] = claim
        self._assert_balanced()
        return claim

    def transfer(
        self,
        claim_id: UUID,
        *,
        from_holder: Party,
        to_holder: Party,
    ) -> Claim:
        claim = self._require_claim(claim_id)
        if claim.holder.id != from_holder.id:
            raise ClaimError("Only the current holder can transfer the claim.")
        if to_holder.id == claim.issuer.id:
            raise ClaimError(
                "Chapter 01 does not model transfer to the issuer as a transfer; "
                "use discharge()."
            )
        if to_holder.id == from_holder.id:
            raise ClaimError("Transfer requires a different holder.")
        transferred = Claim(claim.id, claim.issuer, to_holder, claim.amount)
        self._claims[claim.id] = transferred
        self._assert_balanced()
        return transferred

    def discharge(
        self,
        claim_id: UUID,
        *,
        issuer: Party,
        holder: Party,
    ) -> Claim:
        """Extinguish the claim without modeling the fulfillment mechanism itself."""

        claim = self._require_claim(claim_id)
        if claim.issuer.id != issuer.id:
            raise ClaimError("Only the claim issuer can discharge this claim.")
        if claim.holder.id != holder.id:
            raise ClaimError("Discharge must name the current holder.")
        del self._claims[claim.id]
        self._assert_balanced()
        return claim

    def assets_of(self, party: Party) -> CurrencyAmount:
        currency = self._currency()
        total = sum(
            (c.amount.amount for c in self._claims.values() if c.holder.id == party.id),
            start=0,
        )
        return CurrencyAmount.of(total, currency)

    def liabilities_of(self, party: Party) -> CurrencyAmount:
        currency = self._currency()
        total = sum(
            (c.amount.amount for c in self._claims.values() if c.issuer.id == party.id),
            start=0,
        )
        return CurrencyAmount.of(total, currency)

    def total_assets(self) -> CurrencyAmount:
        currency = self._currency()
        total = sum((c.amount.amount for c in self._claims.values()), start=0)
        return CurrencyAmount.of(total, currency)

    def total_liabilities(self) -> CurrencyAmount:
        currency = self._currency()
        total = sum((c.amount.amount for c in self._claims.values()), start=0)
        return CurrencyAmount.of(total, currency)

    def _currency(self) -> str:
        return self._currency_code or "EUR"

    def _require_currency_compatible(self, amount: CurrencyAmount) -> None:
        if self._currency_code is not None and amount.currency != self._currency_code:
            raise ClaimError("Chapter 01 supports one currency denomination at a time.")

    def _require_claim(self, claim_id: UUID) -> Claim:
        try:
            return self._claims[claim_id]
        except KeyError as exc:
            raise ClaimError(f"Unknown claim: {claim_id}") from exc

    def _assert_balanced(self) -> None:
        if self.total_assets() != self.total_liabilities():
            raise AssertionError("ClaimBook invariant violated: assets != liabilities.")
