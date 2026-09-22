# Learning Model

The project uses executable models primarily as instruments for understanding systems.

The method is strongest when learning depends on mechanisms that can be made explicit: entities, state, rules, constraints, invariants, interactions, algorithms, processes, causal consequences, and changes through time.

Examples include finance, software systems, networks, game economies, logistics, control systems, physical systems, ecology, and other subjects where meaningful system behavior can be represented. It is less suitable as the primary method for material that is mainly declarative, interpretive, aesthetic, or dependent on embodied practice, although simulation may still help with individual mechanisms inside those subjects.

## Core idea

Theory and executable models are complementary:

```text
Theory
  +
Executable model
  +
Learning scenarios
  +
Observability
```

Theory explains concepts and mechanisms. The model defines a deliberately bounded possible world. Scenarios exercise that world. Observability lets the learner inspect why the result happened.

A model is not valuable merely because it runs. It is valuable when it helps answer a learning question.

## Four separate progressions

The project keeps four dimensions separate:

```text
Learning progression
C01 → C02 → C03 → ...

Executable-model progression
M01 → M02 → M03 → ...

Simulation-capability progression
SL0 → SL1 → SL2 → SL3 → SL4

Software-release progression
v0.1 → v0.2 → v1.0 → ...
```

A chapter number is not a software version. A mature application may contain a rich domain implementation while still presenting `C01 / M01` in an intentionally simplified form.

A model stage is also not required to add new classes. A chapter may be an integration chapter whose main purpose is to connect mechanisms learned earlier.

## Chapter as the learning unit

A chapter is a coherent next layer of understanding. It normally contains:

```text
learning goal
prerequisites
§ theoretical paragraphs
important terminology
model stage
learning scenarios
prediction questions
observables
learning payoff
intentional omissions / assumptions
exit criteria
next question
```

Several paragraphs may share one model and several scenarios. Not every paragraph requires another code abstraction.

The canonical reusable design rules are in [`curriculum-design.md`](curriculum-design.md). A working contract is provided by [`learning-chapter-template.md`](learning-chapter-template.md).

## Scenario-centered learning loop

The preferred learning loop is:

```text
THEORY
  ↓
PREDICT
  ↓
RUN SCENARIO
  ↓
OBSERVE
  ↓
EXPLAIN
  ↓
MODIFY
  ↓
EXIT QUESTIONS
  ↓
NEXT CHAPTER
```

The prediction step matters. It exposes the learner's current causal model before the simulator reveals an answer.

A scenario should therefore make explicit:

- what the learner is asked to predict;
- which action, process, or event is run;
- which state transitions should be inspected;
- which invariant, flow, timeline, or metric matters;
- what conceptual distinction the scenario is intended to teach.

## Progressive models

Models normally grow together with the curriculum:

```text
C01 → M01
C02 → M02 extends the understood world
C03 → M03 adds another required mechanism
```

The goal is not monotonically increasing realism. The goal is introducing exactly the complexity needed for the next piece of understanding.

Early models may intentionally omit real mechanisms. This is a teaching device, not a claim that the omitted mechanism does not exist.

The reusable model and scenario rules are in [`executable-learning-model-design.md`](executable-learning-model-design.md).

## Simulation complexity is earned

Simulation infrastructure is introduced only when the subject needs it:

```text
SL0 — manual deterministic state transitions
SL1 — multi-entity transactional scenarios and operation chains
SL2 — time, scheduling, accrual, maturity, periodic processes
SL3 — agents, policies, controllers, feedback loops
SL4 — repeated runs, randomness, parameter sweeps, sensitivity analysis
```

Do not add a clock merely because simulations often have clocks. Do not add agents merely because the domain contains people or organizations. Do not add randomness unless uncertainty itself matters to the learning question.

## Knowledge categories must stay visible

A model should distinguish at least four kinds of statements:

1. **Identity / invariant** — true by the structure of the model, such as a balance-sheet equality.
2. **Domain or institutional rule** — true because the modeled system defines it that way.
3. **Behavioral assumption** — a chosen rule for how an actor behaves.
4. **Empirical parameter** — a value estimated or calibrated from observed data.

These categories must not be presented as interchangeable facts. This distinction becomes especially important in economics, social systems, ecology, and any domain with behavioral models.

## Bilingual terminology

The primary explanatory language may be Russian while important professional terms are introduced with their English equivalents:

> финансовое требование (**financial claim**)

> обязательство (**liability**)

> межбанковский расчёт (**interbank settlement**)

The translation does not need to be repeated in every sentence. It should appear at the first or conceptually important use and whenever a term has a potentially misleading translation.

Code and API vocabulary remains English so the executable model connects naturally to professional literature and tooling.

## Development process

For a new subject:

```text
select subject
  ↓
define target understanding
  ↓
build dependency / question progression
  ↓
design chapters and paragraphs
  ↓
design the M progression
  ↓
design learning scenarios
  ↓
check omissions and assumptions
  ↓
implement the minimum executable model
  ↓
add only required observability
  ↓
validate the chapter as a learning experience
  ↓
continue to the next chapter
```

The curriculum should normally be designed far enough ahead that implementation is following a learning progression rather than inventing the progression opportunistically from code.

Reusable simulation infrastructure should be extracted only when concrete models demonstrate repeated needs.

## Concrete application

The first planned application of these principles is the finance curriculum in [`../curriculum/finance/ROADMAP.md`](../curriculum/finance/ROADMAP.md).
