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
- [`docs/learning-model.md`](docs/learning-model.md) — overview of the learning-first approach and its synchronized progressions.
- [`docs/curriculum-design.md`](docs/curriculum-design.md) — reusable curriculum-design principles.
- [`docs/executable-learning-model-design.md`](docs/executable-learning-model-design.md) — reusable executable-model and scenario principles.
- [`docs/learning-chapter-template.md`](docs/learning-chapter-template.md) — reusable chapter contract/template.
- [`docs/simulation-runtime.md`](docs/simulation-runtime.md) — time, drivers, agents, processes, scenarios, and execution.
- [`docs/simulation-visualization.md`](docs/simulation-visualization.md) — observability-oriented visualization for running simulations.

## Finance curriculum

- [`curriculum/finance/ROADMAP.md`](curriculum/finance/ROADMAP.md) — planned finance progression from `C01 / M01` through `C21 / M21`.
- [`curriculum/finance/ch01/README.md`](curriculum/finance/ch01/README.md) — implemented Chapter 01 learning material and scenarios.

## Current executable chapter

### C01 / M01 — Финансовые требования (Financial Claims)

Learning goal: understand that one financial claim is simultaneously an asset of its holder and a liability of its issuer, and distinguish transfer from claim discharge.

The current `SL0` model supports:

- issuing a financial claim;
- transferring it from Alice to Bob;
- discharging the claim without pretending to model the fulfillment mechanism;
- predicting each transition before execution;
- observing exact before/after changes and the claim asset/liability invariant;
- varying the claim amount and replaying the experiment.

`CurrencyAmount` represents a denomination such as `100 EUR`; the chapter does not yet define a monetary instrument or the monetary system.

## Run

CLI:

    python .\run_demo.py

Tests:

    python -m unittest discover -s tests -v

Streamlit:

    pip install -r .\requirements-ui.txt
    streamlit run .\apps\streamlit_app.py

The Streamlit UI is a learning/observability layer. Domain rules remain in the executable model.

## Development direction

The project keeps four progressions distinct:

```text
learning:          C01 → C02 → C03 → ...
model capability:  M01 → M02 → M03 → ...
simulation level:  SL0 → SL1 → SL2 → ...
software release:  v0.1 → v0.2 → v1.0 → ...
```

A chapter is designed before implementation. Its scenarios exist to test a concrete prediction and make a mechanism observable. Reusable framework abstractions are extracted only after repeated needs appear across concrete models.
