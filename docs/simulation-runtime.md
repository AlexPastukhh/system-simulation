# Simulation Runtime

The simulation runtime turns a static domain model into a system that evolves through time.

## Time is simulation infrastructure

The domain model does not need a clock in order to describe valid actions.

The simulation does.

Typical infrastructure:

```python
class SimulationClock:
    ...

class Scheduler:
    ...

class Simulation:
    ...
```

A simulation step may:

1. process scheduled events;
2. evaluate processes or physical dynamics;
3. let agents observe the world;
4. let agents choose actions;
5. execute those actions through the domain model;
6. record domain events and metrics;
7. advance time.

The exact ordering can differ by simulation type.

## Drivers

A **driver** is anything that can cause the simulated world to change.

This is intentionally broader than "agent".

### Agents

Agents choose actions according to a policy, objective, heuristic, or decision model.

Examples:

- household;
- bank;
- firm;
- animal;
- autonomous vehicle.

A domain entity and its simulation agent should usually remain separate.

```python
class Household:
    # domain state and allowed actions
    ...

class HouseholdAgent:
    household: Household

    def decide(self, world):
        ...
```

This matters because the same domain entity can be simulated with different behavioral assumptions.

### Processes

Processes do not need goals.

Examples:

- interest accrual;
- radioactive decay;
- plant growth;
- periodic tax collection;
- inventory spoilage.

They simply execute according to a rule or schedule.

### Physical dynamics

Some changes are continuous rather than command-like.

Examples:

- gravity;
- friction;
- heat transfer;
- fluid flow.

A simulation may integrate these dynamics over a time step and then update domain state through the appropriate boundary.

### Controllers

Controllers react to observed state and try to maintain a target.

Examples:

- thermostat;
- autopilot;
- monetary-policy rule;
- industrial feedback controller.

They can be represented as agents when useful, but do not need to be treated as human-like decision makers.

### Stochastic processes

Randomness can produce changes without an intentional actor.

Examples:

- component failure;
- mutation;
- arrival process;
- random demand;
- weather transition.

Randomness should be explicit simulation input, ideally with a controllable seed for reproducibility.

### External events

A scenario may inject events from outside the modeled system.

Examples:

- earthquake;
- oil supply shock;
- regulation change;
- technology breakthrough.

These are scenario inputs, not autonomous entities inside the domain.

## Goals and policies

Agents can "strive" toward something, but this can remain simple.

Examples:

```text
Household:
  maintain consumption
  avoid insolvency

Bank:
  earn profit
  remain within liquidity and capital constraints

Firm:
  sell inventory
  maintain profitability

Central bank controller:
  keep selected macro variables near targets
```

A policy may be no more than a transparent heuristic:

```python
if inventory > target_inventory:
    lower_price()

if reserves < liquidity_buffer:
    reduce_lending()
```

Simple rules are often preferable for educational simulations because the causal chain remains visible.

## Scenario

A scenario configures one experiment.

It may define:

- initial world state;
- number and type of entities;
- which drivers are active;
- agent policies;
- scheduled processes;
- external events;
- random seed;
- simulation horizon;
- metrics to record.

Example:

```python
PostLaborScenario(
    households=10_000,
    banks=5,
    initial_automation_rate=0.40,
    policy_rate=0.03,
)
```

The simulation engine should be reusable across scenarios.

## Important boundary

Domain rule:

```text
Repaying loan principal reduces both the loan balance and the matching deposit balance.
```

Simulation assumption:

```text
Households repay 5% of discretionary debt each month.
```

The first describes the modeled system.

The second describes one chosen behavior inside one class of simulations.

Keeping them separate makes assumptions visible and replaceable.
