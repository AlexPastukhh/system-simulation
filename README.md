# system-simulation

A repository for learning complex systems through theory plus executable simulation models.

The project separates:

- the **domain/world model** — what exists, what actions are possible, and which invariants hold;
- the **simulation runtime** — what drives the world through time;
- **code visualization** — supplementary views over the descriptive source code;
- **simulation visualization** — observability of a running scenario;
- the **learning model** — chapters, theory, executable models, and scenarios that progressively deepen understanding.

## Documentation

- [`docs/architecture.md`](docs/architecture.md) — project scopes and boundaries.
- [`docs/learning-model.md`](docs/learning-model.md) — chapter-based learning progression tied to executable models.
- [`docs/simulation-runtime.md`](docs/simulation-runtime.md) — time, drivers, agents, processes, scenarios, and execution.
- [`docs/simulation-visualization.md`](docs/simulation-visualization.md) — simple observability-oriented visualization for running simulations.

## Core direction

The project should grow primarily through concrete subjects.

For each subject:

1. analyze the learning progression;
2. define a chapter;
3. identify the domain mechanisms needed for that chapter;
4. implement the minimal executable model;
5. create scenarios;
6. add only the observability needed to understand the mechanisms;
7. continue to the next chapter.

Reusable simulation infrastructure should be extracted only when repeated needs appear across concrete models.
