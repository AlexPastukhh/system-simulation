# system-simulation

A repository for describing systems as executable domain models and then running simplified simulations on top of those models.

The project separates **what a system is allowed to do** from **what drives it through time**.

## Documentation

- [`docs/architecture.md`](docs/architecture.md) — project scopes and boundaries.
- [`docs/simulation-runtime.md`](docs/simulation-runtime.md) — time, drivers, agents, processes, scenarios, and execution.
- [`docs/simulation-visualization.md`](docs/simulation-visualization.md) — simple observability-oriented visualization for running simulations.

## Core idea

The domain model describes a possible world:

- entities and value objects;
- state;
- allowed actions;
- domain events;
- invariants and constraints.

The simulation layer makes that world evolve:

- time and scheduling;
- autonomous agents;
- deterministic or stochastic processes;
- physical dynamics and controllers;
- external events and scenario configuration.

A separate code-visualization tool may project the descriptive code into diagrams, but it is supplementary. The source code remains the primary description of the system.

The simulation UI is also separate from code visualization. Its job is to make a running scenario observable: current state, events, flows, metrics, and changes over time.
