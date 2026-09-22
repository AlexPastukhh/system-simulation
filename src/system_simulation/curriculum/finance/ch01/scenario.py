from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from system_simulation.domain import ClaimBook, Money, Party
from system_simulation.simulation import Change, SimulationTrace, TraceFrame


@dataclass(frozen=True)
class ChapterPartySet:
    issuer: Party
    alice: Party
    bob: Party


class ClaimsChapterScenario:
    """Chapter 01: issue -> transfer -> settle one claim."""

    def __init__(self) -> None:
        self.parties = ChapterPartySet(
            issuer=Party("issuer", "Issuer"),
            alice=Party("alice", "Alice"),
            bob=Party("bob", "Bob"),
        )
        self.book = ClaimBook()
        self.trace = SimulationTrace()
        self.claim_id = None
        self._record_initial_state()

    def issue_claim(self, amount: int | float | str = 100) -> TraceFrame:
        if self.claim_id is not None:
            raise ValueError("This learning scenario issues one claim only.")
        before = self.snapshot()
        claim = self.book.issue(self.parties.issuer, self.parties.alice, Money.of(amount))
        self.claim_id = claim.id
        after = self.snapshot()
        return self.trace.record(
            event="ClaimIssued",
            description=f"Issuer creates a {claim.amount} claim held by Alice.",
            changes=self._diff(before, after),
            snapshot=after,
        )

    def transfer_to_bob(self) -> TraceFrame:
        if self.claim_id is None:
            raise ValueError("Issue the claim before transferring it.")
        before = self.snapshot()
        claim = self.book.transfer(self.claim_id, from_holder=self.parties.alice, to_holder=self.parties.bob)
        after = self.snapshot()
        return self.trace.record(
            event="ClaimTransferred",
            description=f"Alice transfers the {claim.amount} claim to Bob.",
            changes=self._diff(before, after),
            snapshot=after,
        )

    def settle_with_bob(self) -> TraceFrame:
        if self.claim_id is None:
            raise ValueError("Issue the claim before settling it.")
        before = self.snapshot()
        claim = self.book.settle(self.claim_id, holder=self.parties.bob)
        self.claim_id = None
        after = self.snapshot()
        return self.trace.record(
            event="ClaimSettled",
            description=f"Bob settles the {claim.amount} claim with its issuer.",
            changes=self._diff(before, after),
            snapshot=after,
        )

    def run_complete(self, amount: int | float | str = 100) -> tuple[TraceFrame, ...]:
        self.issue_claim(amount)
        self.transfer_to_bob()
        self.settle_with_bob()
        return self.trace.frames

    def snapshot(self) -> dict[str, Any]:
        state: dict[str, Any] = {
            "total_claim_assets": str(self.book.total_assets()),
            "total_claim_liabilities": str(self.book.total_liabilities()),
            "active_claims": len(self.book.claims),
        }
        for party in (self.parties.issuer, self.parties.alice, self.parties.bob):
            prefix = party.name.lower()
            state[f"{prefix}.assets"] = str(self.book.assets_of(party))
            state[f"{prefix}.liabilities"] = str(self.book.liabilities_of(party))
        if self.book.claims:
            claim = self.book.claims[0]
            state["claim.holder"] = claim.holder.name
            state["claim.issuer"] = claim.issuer.name
            state["claim.amount"] = str(claim.amount)
        else:
            state["claim.holder"] = None
            state["claim.issuer"] = None
            state["claim.amount"] = None
        return state

    def _record_initial_state(self) -> None:
        snapshot = self.snapshot()
        self.trace.record(event="InitialState", description="No active claims exist.", changes=[], snapshot=snapshot)

    @staticmethod
    def _diff(before: dict[str, Any], after: dict[str, Any]) -> list[Change]:
        return [Change(key, before.get(key), after.get(key)) for key in sorted(set(before) | set(after)) if before.get(key) != after.get(key)]
