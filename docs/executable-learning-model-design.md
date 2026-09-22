# Executable Learning Model Design Principles

This document defines reusable principles for constructing executable models that support the curriculum.

The central rule is simple:

> Build the smallest executable world that can answer the current learning question faithfully and observably.

The model is not a miniature copy of reality. It is an executable explanatory instrument.

## 1. Separate four responsibilities

### Domain / world model

Defines what exists, valid state, allowed actions, events, constraints, and invariants.

### Simulation runtime

Drives the world when time, scheduling, processes, agents, controllers, randomness, or external events are required.

### Scenario

Configures one learning experiment: initial conditions, enabled capabilities, actions/processes, assumptions, and observations.

### Visualization / observability

Projects relevant state and transitions for the learner. It must not become the semantic owner of domain rules.

The flow should normally be:

```text
scenario / driver
    ↓
domain action
    ↓
domain rules and invariants
    ↓
state transition + event
    ↓
trace / metrics
    ↓
visualization
```

## 2. Model stages are learning capability boundaries

Use `M01`, `M02`, ... to describe the cumulative capability needed by the curriculum.

```text
M01
basic mechanism

M02
M01 + next required capability

M03
M02 + next required capability
```

An M stage is not necessarily:

- a package version;
- a branch;
- a duplicated source tree;
- a deployable release.

It is a semantic capability boundary that a chapter can expose.

Later code may implement more than an early M stage. The application should use chapter projections/configuration so the learner still sees the intended bounded model.

## 3. Do not force one new model per paragraph

A chapter may introduce several concepts that all use the same model. Conversely, one model stage may support several scenarios with different learning purposes.

An integration chapter may add no major domain type at all. Its executable value may come from composing mechanisms already learned.

## 4. Scenario contract

A learning scenario should define:

### Learning question

What conceptual question is this experiment answering?

### Initial state

Only the state required for the experiment. Avoid incidental complexity.

### Prediction

What should the learner predict before execution?

### Trigger

The action, process, event, time advance, or policy change that starts the mechanism.

### Expected transition

Which semantic state changes should occur if the model is working correctly?

### Observables

Which values, relationships, events, flows, or metrics should the learner inspect?

### Learning payoff

What distinction, invariant, causal chain, or failed intuition should be clearer after the run?

### Variation

A small modification that tests whether the learner understood the mechanism rather than memorized one trace.

## 5. Failed scenarios are first-class learning tools

A scenario may intentionally demonstrate that an operation cannot be completed yet.

For example, a model with two independent ledgers may reject a cross-system payment because the settlement mechanism has not been introduced.

A blocked educational scenario should normally preserve valid state:

```text
request
  ↓
validate
  ↓
cannot satisfy precondition
  ↓
no partial mutation
  ↓
explain missing mechanism
```

Do not corrupt half the world merely to visualize a problem unless partial completion is itself the real mechanism being studied.

## 6. Use before/after traces for local mechanisms

For deterministic transactional chapters, a compact trace is often more useful than a chart:

```text
Event: TransferClaim

Alice.asset   100 → 0
Bob.asset       0 → 100
Issuer.debt   100 → 100
```

A useful frame may contain:

```text
time / step
trigger or event
actors
changes: path, before, after
important invariants
selected metrics
assumptions active in this scenario
```

Do not introduce time if `step` is enough.

## 7. Simulation levels

### SL0 — Manual deterministic transitions

Use when the learner only needs to inspect explicit actions and immediate consequences.

Examples: issue, transfer, repay, create, delete, route, toggle.

Infrastructure needed: scenario state, domain actions, trace, reset.

### SL1 — Multi-entity operation chains

Use when one outcome spans several independent entities or stages.

Examples: clearing/settlement, distributed request flow, logistics handoff.

Infrastructure may add operation state such as pending, failed, cleared, settled, or completed.

### SL2 — Time and scheduled processes

Add only when time changes the mechanism.

Examples: interest accrual, maturity, inventory spoilage, growth, periodic control loops.

Infrastructure may add clock, scheduler, scheduled processes, and time-series metrics.

### SL3 — Agents, policies, controllers, feedback

Use when the learning question depends on decisions or feedback rather than a fixed sequence.

Keep domain entities separate from simulation policies so multiple behaviors can drive the same world.

### SL4 — Experiment framework

Use when the lesson concerns uncertainty, robustness, distributions, or institutional comparison.

Capabilities may include controlled random seeds, repeated runs, parameter sweeps, sensitivity analysis, and result comparison.

## 8. Add simulation infrastructure only when earned

Ask before adding a mechanism:

- Does the learning question require time?
- Does it require autonomous decision-making?
- Does it require randomness?
- Does it require many runs rather than one inspectable trace?
- Does it require continuous dynamics rather than actions/events?

If the answer is no, keep the model simpler.

## 9. Keep domain rules and simulation behavior separate

Example:

```text
Domain rule:
Repaying principal reduces an outstanding loan according to the contract.

Behavioral assumption:
A household chooses to repay 5% of discretionary debt each month.
```

The first belongs to the possible world. The second belongs to a simulation policy or scenario.

This boundary makes behavioral assumptions replaceable and visible.

## 10. Label truth categories

Executable models should make it possible to distinguish:

- **identity / invariant**;
- **domain or institutional rule**;
- **behavioral assumption**;
- **empirical parameter**;
- **scenario input / shock**.

For later learning stages, the UI or trace should expose this classification where confusion would materially affect interpretation.

## 11. Scope institution-specific rules

If a mechanism differs by jurisdiction, product, protocol, organization, historical period, or implementation, model an explicit profile rather than silently claiming universality.

Possible strategies:

```text
StylizedProfile
UKProfile
USProfile
EuroAreaProfile
ProtocolV2Profile
```

Do not build every profile early. First declare the one being used and preserve a path for later comparison.

## 12. Prefer semantic actions over raw state mutation

Controls should invoke meaningful operations:

```text
Issue loan
Transfer claim
Advance one month
Settle payment
Apply shock
```

Avoid controls such as:

```text
set bank.reserves = -50
```

unless the application is in an explicit debugging or scenario-authoring mode.

## 13. Observability follows the learning question

Choose the smallest useful projection:

- before/after changes for short transactions;
- relationship diagrams for flows between a few entities;
- timelines for sequence-sensitive mechanisms;
- charts for behavior emerging over many time steps;
- comparison panels for alternate assumptions;
- distributions for repeated stochastic runs.

Do not add visualization merely because the data exists.

## 14. Bilingual terms and code vocabulary

Explanatory material may use Russian with English professional terms at important introductions. Code should use stable English domain names.

For example:

```text
финансовое требование (financial claim)
```

maps naturally to:

```python
FinancialClaim
```

Avoid creating two parallel code vocabularies.

## 15. Extract reusable infrastructure after repetition

A concrete chapter may reveal a reusable need. Do not immediately generalize it into a framework.

Preferred sequence:

```text
concrete model A
  ↓
concrete model B has the same need
  ↓
compare both implementations
  ↓
extract the smallest stable abstraction
```

This applies to schedulers, traces, agent interfaces, experiment runners, visualization components, and domain-support libraries.

## 16. Model review checklist

Before accepting an M stage, verify:

- it contains every mechanism required by the chapter and no unnecessary conceptual burden;
- domain state and actions are explicit;
- invariants are enforceable or observable;
- scenario behavior does not bypass domain rules;
- scenario assumptions are separate from domain rules;
- blocked operations fail without invalid partial mutation unless partial completion is intentional;
- the core scenario has Prediction, Trigger, Observable, and Learning payoff;
- early chapters can still expose their simplified world later;
- time, agents, randomness, and experiment infrastructure appear only when justified;
- visualization is a projection, not the source of truth;
- model terms connect cleanly to the terminology used in the chapter.

## 17. Implementation order

For one chapter:

```text
chapter contract
  ↓
scenario design on paper
  ↓
minimal domain additions
  ↓
scenario orchestration
  ↓
trace / observability
  ↓
tests of domain invariants
  ↓
tests of scenario learning transitions
  ↓
UI only if it improves understanding
```

This order keeps the executable model subordinate to the learning design rather than the other way around.
