# Architecture

## 1. Domain / world model

The domain model describes the possible system.

It answers:

- What exists?
- What state can each thing hold?
- What actions are possible?
- What events result from those actions?
- What invariants and constraints must always hold?

A useful analogy is a multiplayer game engine. The engine defines what players, objects, and systems *can* do, but it does not require anyone to be actively driving them.

Example:

```python
class CommercialBank:
    def issue_loan(self, borrower, amount):
        ...

    def settle_payment(self, payment):
        ...
```

The code should be descriptive enough that the domain can be understood directly from it.

The domain model should not contain simulation-only assumptions such as:

- how often an actor chooses an action;
- what an actor is trying to optimize;
- when a scheduled process runs;
- how randomness is sampled;
- which scenario is currently being tested.

Those belong to the simulation scope.

## 2. Code visualization

Code visualization is a separate, supplementary scope.

Its purpose is to project the descriptive code into useful diagrams such as:

- entities and relationships;
- commands and events;
- state machines;
- dependencies;
- selected scenario traces.

This tooling should not become the semantic source of truth. The code remains primary.

Existing parsers, language indexes, and diagram renderers can be reused. Custom tooling is mainly valuable for selecting and composing useful views rather than implementing a new renderer.

## 3. Simulation runtime

The simulation runtime uses the domain model and adds evolution through time.

It owns concepts such as:

- simulation clock;
- scheduler;
- scenario;
- drivers;
- autonomous policies;
- randomness;
- external events;
- metric recording.

The runtime should invoke domain actions rather than bypassing the domain and mutating arbitrary state.

Conceptually:

```text
driver observes world
    ↓
driver chooses or produces an action
    ↓
domain validates and executes the action
    ↓
domain state changes and events are emitted
    ↓
simulation records the result
    ↓
time advances
```

Not every source of change is an agent. See [`simulation-runtime.md`](simulation-runtime.md).

## 4. Simulation visualization

Simulation visualization is not code visualization.

Its purpose is to make a running scenario understandable.

It may show:

- current world state;
- important entities;
- an event timeline;
- state changes caused by an event;
- flows between entities;
- metrics over time;
- controls for executing or replaying a scenario.

The visual layer should stay as simple as the scenario allows.

See [`simulation-visualization.md`](simulation-visualization.md).

## 5. Learning model

The learning model organizes subject understanding into chapters.

A chapter combines:

- theory;
- a bounded learning scope;
- the minimal executable model needed for that scope;
- scenarios that exercise the new mechanisms;
- observability needed to understand those scenarios.

The chapter sequence and domain-model evolution move together, but they are not the same thing. The codebase may already contain capabilities that an earlier chapter intentionally hides.

See [`learning-model.md`](learning-model.md).

## Boundary summary

```text
                         CODE VISUALIZATION
                         projects the code
                                ▲
                                │
DOMAIN / WORLD MODEL ───────────┤
defines the possible system     │
        │
        ▼
SIMULATION RUNTIME
creates a trajectory through time
        │
        ▼
SIMULATION VISUALIZATION
makes that trajectory observable

LEARNING MODEL
selects which domain mechanisms, scenarios,
and observations are exposed at each chapter
```
