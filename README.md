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
- [`docs/curriculum-design.md`](docs/curriculum-design.md) — reusable principles for designing a subject, chapters, paragraphs, prerequisites, terminology, and exit criteria.
- [`docs/executable-learning-model-design.md`](docs/executable-learning-model-design.md) — reusable principles for executable learning models, scenarios, simulation levels, assumptions, and observability.
- [`docs/learning-chapter-template.md`](docs/learning-chapter-template.md) — reusable chapter contract/template.
- [`docs/simulation-runtime.md`](docs/simulation-runtime.md) — time, drivers, agents, processes, scenarios, and execution.
- [`docs/simulation-visualization.md`](docs/simulation-visualization.md) — observability-oriented visualization for running simulations.

## Finance curriculum

- [`curriculum/finance/ROADMAP.md`](curriculum/finance/ROADMAP.md) — planned finance learning progression, model stages, scenarios, and simulation progression.
- [`curriculum/finance/ch01/README.md`](curriculum/finance/ch01/README.md) — the currently implemented Chapter 01 prototype.

The finance roadmap is the planning baseline for future chapter work. The current Chapter 01 implementation predates that baseline and is intentionally left unchanged until a later implementation package aligns it.

## Current executable chapter

### Finance · Chapter 01 — Claims and balance sheets

Learning goal: understand that one financial claim is simultaneously an asset of its holder and a liability of its issuer.

The first model supports:

- issuing a claim;
- transferring it between holders;
- settling it;
- observing explicit before/after simulation traces.

## Run

CLI:

    python .\run_demo.py

Tests:

    python -m unittest discover -s tests -v

Streamlit:

    pip install -r .\requirements-ui.txt
    streamlit run .\apps\streamlit_app.py

The UI is intentionally a thin observer over the executable model. It does not own domain rules.

## Development direction

The project grows through concrete subjects and keeps four progressions distinct:

```text
learning:          C01 → C02 → C03 → ...
model capability:  M01 → M02 → M03 → ...
simulation level:  SL0 → SL1 → SL2 → ...
software release:  v0.1 → v0.2 → v1.0 → ...
```

A new chapter should be designed before its implementation. Its scenarios should exist to test a concrete learner prediction and make a mechanism observable. Reusable framework abstractions should be extracted only after repeated needs appear across concrete models.
