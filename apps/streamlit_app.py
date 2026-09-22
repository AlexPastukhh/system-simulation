from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC = PROJECT_ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from system_simulation.curriculum.finance.ch01 import ClaimsChapterScenario

st.set_page_config(page_title="System Simulation — Finance Ch. 01", layout="wide")
st.title("Finance · Chapter 01")
st.subheader("Claims and balance sheets")
st.markdown(
    """
**Learning goal:** one financial claim is simultaneously an **asset of its holder**
and a **liability of its issuer**.

This chapter deliberately models only `issue → transfer → settle`.
"""
)

if "scenario" not in st.session_state:
    st.session_state.scenario = ClaimsChapterScenario()

scenario: ClaimsChapterScenario = st.session_state.scenario
controls = st.columns(4)

with controls[0]:
    if st.button("Reset", use_container_width=True):
        st.session_state.scenario = ClaimsChapterScenario()
        st.rerun()

with controls[1]:
    if st.button("1 · Issue 100 EUR", use_container_width=True):
        if scenario.claim_id is None:
            scenario.issue_claim(100)
            st.rerun()

with controls[2]:
    if st.button("2 · Alice → Bob", use_container_width=True):
        if scenario.claim_id is not None and scenario.book.claims and scenario.book.claims[0].holder.id == scenario.parties.alice.id:
            scenario.transfer_to_bob()
            st.rerun()

with controls[3]:
    if st.button("3 · Settle", use_container_width=True):
        if scenario.claim_id is not None and scenario.book.claims and scenario.book.claims[0].holder.id == scenario.parties.bob.id:
            scenario.settle_with_bob()
            st.rerun()

snapshot = scenario.snapshot()
st.divider()
st.subheader("Current state")

for column, party in zip(
    st.columns(3),
    (scenario.parties.issuer, scenario.parties.alice, scenario.parties.bob),
):
    prefix = party.name.lower()
    with column:
        st.markdown(f"### {party.name}")
        st.metric("Claim assets", snapshot[f"{prefix}.assets"])
        st.metric("Claim liabilities", snapshot[f"{prefix}.liabilities"])

st.caption(
    f"Invariant · total assets: {snapshot['total_claim_assets']} · "
    f"total liabilities: {snapshot['total_claim_liabilities']}"
)

st.divider()
st.subheader("Timeline")

for frame in reversed(scenario.trace.frames):
    with st.expander(f"{frame.step} · {frame.event}", expanded=(frame == scenario.trace.frames[-1])):
        st.write(frame.description)
        if frame.changes:
            st.dataframe(
                [{"path": c.path, "before": c.before, "after": c.after} for c in frame.changes],
                use_container_width=True,
                hide_index=True,
            )
        else:
            st.caption("No state changes.")
