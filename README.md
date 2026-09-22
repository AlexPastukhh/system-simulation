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
- [`docs/simulation-visualization.md`](docs/simulation-visualization.md) — observability-oriented visualization for running simulations.

## Current executable chapter

### Finance · Chapter 01 — Claims and balance sheets

Learning goal: understand that one financial claim is simultaneously an asset of its holder and a liability of its issuer.

The first model supports:

- issuing a claim;
- transferring it between holders;
- settling it;
- observing explicit before/after simulation traces.

Theory:

[`curriculum/finance/ch01/README.md`](curriculum/finance/ch01/README.md)

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

For each subject:

1. analyze the learning progression;
2. define a chapter;
3. identify the required domain mechanisms;
4. implement the minimal executable model;
5. create scenarios;
6. add only the observability required to understand them;
7. continue to the next chapter.

Reusable infrastructure should be extracted when repeated needs appear across concrete models.