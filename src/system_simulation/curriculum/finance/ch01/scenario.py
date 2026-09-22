from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from system_simulation.domain import ClaimBook, CurrencyAmount, Party
from system_simulation.simulation import Change, SimulationTrace, TraceFrame


@dataclass(frozen=True)
class ChapterPartySet:
    issuer: Party
    alice: Party
    bob: Party


@dataclass(frozen=True)
class LearningScenarioGuide:
    key: str
    title: str
    prediction: str
    observable: str
    learning_payoff: str
    variation: str


SCENARIO_GUIDES: dict[str, LearningScenarioGuide] = {
    "issue": LearningScenarioGuide(
        key="S01.1",
        title="Выпуск требования (Issue Claim)",
        prediction=(
            "Если Issuer создаёт claim на 100 EUR в пользу Alice, у кого появится asset, "
            "а у кого liability?"
        ),
        observable=(
            "Alice claim assets увеличиваются на сумму claim; Issuer claim liabilities "
            "увеличиваются на ту же сумму; total claim assets == total claim liabilities."
        ),
        learning_payoff=(
            "Asset и liability здесь не два независимых объекта, а две стороны одного "
            "financial claim."
        ),
        variation="Reset, измени сумму claim и заранее предскажи обе стороны изменения.",
    ),
    "transfer": LearningScenarioGuide(
        key="S01.2",
        title="Передача требования (Transfer Claim)",
        prediction=(
            "Если Alice передаст claim Bob, исчезнет ли liability Issuer или изменится "
            "только holder?"
        ),
        observable=(
            "Alice claim assets уменьшаются, Bob claim assets увеличиваются, а liability "
            "Issuer и общий размер outstanding claims не меняются."
        ),
        learning_payoff="Transfer меняет holder, но не прекращает обязательство issuer.",
        variation="До запуска назови все значения, которые должны остаться неизменными.",
    ),
    "discharge": LearningScenarioGuide(
        key="S01.3",
        title="Погашение требования (Claim Discharge)",
        prediction=(
            "Если требование исполнено и прекращается, какие две стороны финансового "
            "отношения должны исчезнуть?"
        ),
        observable=(
            "Bob claim assets и Issuer claim liabilities одновременно уменьшаются до нуля; "
            "active claim исчезает."
        ),
        learning_payoff=(
            "Discharge прекращает сам financial claim. В C01 намеренно не моделируется, "
            "каким экономическим средством issuer его исполнил."
        ),
        variation=(
            "Сравни результат с Transfer: какой state change принципиально отличает "
            "прекращение claim от смены holder?"
        ),
    ),
}


class FinancialClaimsScenario:
    """C01 / M01 / SL0: issue -> transfer -> discharge one financial claim."""

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
            raise ValueError("This learning scenario issues one active claim at a time.")
        before = self.snapshot()
        claim = self.book.issue(
            self.parties.issuer,
            self.parties.alice,
            CurrencyAmount.of(amount),
        )
        self.claim_id = claim.id
        after = self.snapshot()
        return self.trace.record(
            event="ClaimIssued",
            description=f"Issuer creates a {claim.amount} financial claim held by Alice.",
            changes=self._diff(before, after),
            snapshot=after,
        )

    def transfer_to_bob(self) -> TraceFrame:
        if self.claim_id is None:
            raise ValueError("Issue the claim before transferring it.")
        before = self.snapshot()
        claim = self.book.transfer(
            self.claim_id,
            from_holder=self.parties.alice,
            to_holder=self.parties.bob,
        )
        after = self.snapshot()
        return self.trace.record(
            event="ClaimTransferred",
            description=f"Alice transfers the {claim.amount} financial claim to Bob.",
            changes=self._diff(before, after),
            snapshot=after,
        )

    def discharge_with_bob(self) -> TraceFrame:
        if self.claim_id is None:
            raise ValueError("Issue the claim before discharging it.")
        before = self.snapshot()
        claim = self.book.discharge(
            self.claim_id,
            issuer=self.parties.issuer,
            holder=self.parties.bob,
        )
        self.claim_id = None
        after = self.snapshot()
        return self.trace.record(
            event="ClaimDischarged",
            description=(
                f"The {claim.amount} claim held by Bob is discharged. "
                "The mechanism of fulfillment is intentionally outside C01."
            ),
            changes=self._diff(before, after),
            snapshot=after,
        )

    def run_complete(self, amount: int | float | str = 100) -> tuple[TraceFrame, ...]:
        self.issue_claim(amount)
        self.transfer_to_bob()
        self.discharge_with_bob()
        return self.trace.frames

    def current_learning_step(self) -> str | None:
        if self.claim_id is None:
            if self.trace.frames[-1].event == "ClaimDischarged":
                return None
            return "issue"
        claim = self.book.claims[0]
        if claim.holder.id == self.parties.alice.id:
            return "transfer"
        if claim.holder.id == self.parties.bob.id:
            return "discharge"
        raise AssertionError("Unexpected holder in Chapter 01 scenario.")

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
        self.trace.record(
            event="InitialState",
            description="No active financial claims exist.",
            changes=[],
            snapshot=snapshot,
        )

    @staticmethod
    def _diff(before: dict[str, Any], after: dict[str, Any]) -> list[Change]:
        keys = sorted(set(before) | set(after))
        return [
            Change(key, before.get(key), after.get(key))
            for key in keys
            if before.get(key) != after.get(key)
        ]
