from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC = PROJECT_ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from system_simulation.curriculum.finance.ch01 import FinancialClaimsScenario, SCENARIO_GUIDES

st.set_page_config(page_title="System Simulation — Finance C01", layout="wide")
st.title("Finance · C01 / M01")
st.subheader("Финансовые требования (Financial Claims)")
st.caption("SL0 · ручные детерминированные переходы состояния")
st.markdown(
    """
**Цель:** понять, почему одно финансовое требование (**financial claim**) одновременно
является активом (**asset**) держателя (**holder**) и обязательством (**liability**)
эмитента/должника (**issuer**), а также отличать передачу (**transfer**) от прекращения
требования (**claim discharge**).

Учебный цикл: **прочитай → предскажи → запусти → наблюдай → объясни → измени условие**.
"""
)

with st.expander("Краткая теория · §1.1–§1.6", expanded=False):
    st.markdown(
        """
**§1.1 Стороны (Parties).** В модели есть независимые участники финансового отношения.

**§1.2 Финансовое требование (Financial Claim).** Claim — право holder требовать исполнения
от issuer на заданную величину.

**§1.3 Holder и Issuer.** Holder владеет требованием; issuer несёт соответствующее обязательство.

**§1.4 Asset и Liability.** Один claim виден с двух сторон: asset holder и liability issuer.
В M01 действует инвариант `total claim assets == total claim liabilities`.

**§1.5 Передача (Transfer).** Меняется holder; обязательство issuer не исчезает.

**§1.6 Погашение/исполнение (Claim Discharge).** Сам claim прекращается, поэтому исчезают
и asset holder, и liability issuer. C01 намеренно **не моделирует**, чем именно issuer
экономически исполнил требование. Это не interbank settlement.

`100 EUR` здесь — **величина в валютной единице (CurrencyAmount)**, а не утверждение о том,
что сам claim уже является money. Денежные инструменты изучаются позже.
"""
    )

if "scenario" not in st.session_state:
    st.session_state.scenario = FinancialClaimsScenario()

scenario: FinancialClaimsScenario = st.session_state.scenario
snapshot = scenario.snapshot()

left, right = st.columns([2, 1])
with left:
    st.subheader("Учебный эксперимент")
with right:
    if st.button("↺ Reset / Сбросить", use_container_width=True):
        st.session_state.scenario = FinancialClaimsScenario()
        st.rerun()

step = scenario.current_learning_step()
last_event = scenario.trace.frames[-1].event
last_guide_key = {
    "ClaimIssued": "issue",
    "ClaimTransferred": "transfer",
    "ClaimDischarged": "discharge",
}.get(last_event)

if last_guide_key is not None:
    previous = SCENARIO_GUIDES[last_guide_key]
    st.success(f"**Что выяснили:** {previous.learning_payoff}")

if step is not None:
    guide = SCENARIO_GUIDES[step]
    st.markdown(f"### {guide.key} · {guide.title}")
    st.info(f"**Prediction / Предсказание:** {guide.prediction}")
    st.caption(f"После запуска наблюдай: {guide.observable}")

    if step == "issue":
        amount = st.number_input(
            "Сумма claim, EUR",
            min_value=1.0,
            value=100.0,
            step=10.0,
            help="Это CurrencyAmount — величина требования, а не отдельный денежный инструмент.",
        )
        if st.button("Запустить · Issue Claim", type="primary", use_container_width=True):
            scenario.issue_claim(amount)
            st.rerun()
    elif step == "transfer":
        if st.button("Запустить · Alice → Bob", type="primary", use_container_width=True):
            scenario.transfer_to_bob()
            st.rerun()
    elif step == "discharge":
        if st.button("Запустить · Discharge Claim", type="primary", use_container_width=True):
            scenario.discharge_with_bob()
            st.rerun()

    st.caption(f"Variation: {guide.variation}")
else:
    st.success("C01 core scenarios завершены. Теперь попробуй Exit questions без подсматривания в trace.")
    st.markdown(
        """
**Exit questions**

1. Почему один claim одновременно является asset и liability?
2. Что меняется и что не меняется при transfer?
3. Чем transfer отличается от claim discharge?
4. Почему `100 EUR` в C01 ещё не означает, что мы определили, что такое money?
5. Какой вопрос естественно ведёт к C02? — Как системно записывать много таких отношений?
"""
    )

st.divider()
st.subheader("Состояние модели (Current State)")
rows = []
for party in (scenario.parties.issuer, scenario.parties.alice, scenario.parties.bob):
    prefix = party.name.lower()
    rows.append(
        {
            "Party": party.name,
            "Claim assets": snapshot[f"{prefix}.assets"],
            "Claim liabilities": snapshot[f"{prefix}.liabilities"],
        }
    )
st.dataframe(rows, use_container_width=True, hide_index=True)

st.caption(
    f"Invariant · total claim assets: {snapshot['total_claim_assets']} · "
    f"total claim liabilities: {snapshot['total_claim_liabilities']}"
)

if snapshot["active_claims"]:
    st.write(
        f"Active claim · issuer: **{snapshot['claim.issuer']}** · "
        f"holder: **{snapshot['claim.holder']}** · amount: **{snapshot['claim.amount']}**"
    )
else:
    st.write("Active claim: **none**")

st.divider()
st.subheader("Trace · before → after")
for frame in reversed(scenario.trace.frames):
    with st.expander(
        f"{frame.step} · {frame.event}",
        expanded=(frame == scenario.trace.frames[-1]),
    ):
        st.write(frame.description)
        if frame.changes:
            st.dataframe(
                [
                    {"path": c.path, "before": c.before, "after": c.after}
                    for c in frame.changes
                ],
                use_container_width=True,
                hide_index=True,
            )
        else:
            st.caption("No state changes.")
