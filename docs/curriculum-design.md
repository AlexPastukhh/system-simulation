# Curriculum Design Principles

This document defines reusable principles for designing the learning side of a system-simulation subject. It is intentionally subject-independent.

The curriculum is not a table of contents for the software. It is a planned sequence of changes in the learner's mental model.

## 1. Start from understanding, not implementation

Before choosing chapters, define the target understanding:

- What should the learner be able to explain at the end?
- Which mechanisms must be understood rather than memorized?
- Which distinctions are commonly confused?
- Which later questions depend on which earlier concepts?
- Which claims can be demonstrated through an executable model?

Do not start by enumerating classes that would be convenient to implement.

## 2. Build a dependency chain of questions

A strong chapter sequence can often be written as a chain of unresolved questions:

```text
Chapter N answers question A
        ↓
that answer exposes question B
        ↓
Chapter N+1 answers question B
```

The transition should feel necessary rather than arbitrary.

For example:

```text
What is a financial claim?
        ↓
How do many claims fit into a coherent accounting system?
        ↓
What is a bank deposit?
        ↓
How are deposits created?
```

A roadmap should be reviewed for jumps, circular prerequisites, and chapters that exist only because a textbook convention says they should.

## 3. Chapter contract

Every chapter should define the following before implementation begins.

### Learning goal

One or a small number of concrete things the learner should understand after the chapter.

Prefer:

> Explain why a transfer changes the holder of a claim without extinguishing the issuer's liability.

over:

> Learn about claims.

### Prerequisites

Only knowledge actually required to reason about the chapter. If a prerequisite has not been established earlier, either move the chapter or introduce the prerequisite explicitly.

### Paragraphs

Paragraphs (`§`) should form the shortest useful theoretical route to the learning goal.

A paragraph may introduce:

- one concept;
- one distinction;
- one mechanism;
- one invariant;
- one necessary piece of context.

Paragraph boundaries are pedagogical, not code boundaries. Several paragraphs may use the same model and scenario.

### Important terminology

Use the normal explanatory language of the course and attach an English professional term at the first or conceptually important use:

> актив (**asset**)

> платёжеспособность (**solvency**)

Prefer natural text over a permanently duplicated bilingual paragraph. Add a dedicated glossary only when the subject genuinely benefits from one.

If translation can hide an important distinction, preserve both terms explicitly. For example, generic claim discharge and interbank settlement should not be silently collapsed into the same translated word.

### Model stage

Identify the minimum executable world needed by the chapter (`Mxx`). The model stage is a capability boundary, not necessarily a separate source tree or software release.

### Learning scenarios

At least one scenario must justify why execution helps the chapter. Each core scenario should state:

- **Prediction** — what the learner predicts before running it;
- **Action / process** — what the simulator executes;
- **Observable** — what state, event, flow, invariant, or metric to inspect;
- **Learning payoff** — what mechanism or distinction becomes clearer.

If a scenario has no meaningful learning payoff, remove it or redesign it.

### Intentional omissions

State which real mechanisms are deliberately absent.

An omission is acceptable when:

- the omitted mechanism is not necessary for the current learning goal;
- its absence does not make the demonstrated mechanism false inside the declared model;
- the chapter says enough to prevent the simplification from being mistaken for a universal real-world claim.

### Assumptions and scope

State assumptions that materially affect interpretation. This is especially important for jurisdiction-specific institutions, behavioral rules, empirical parameters, and simplified physical or social models.

### Exit criteria

A chapter is complete for the learner when they can explain or predict the mechanism without merely reproducing the UI.

Exit criteria can include:

- explanation questions;
- prediction of a new variation;
- identification of an invariant;
- comparison of two mechanisms;
- diagnosis of an intentionally misleading example.

### Next question

End with the unresolved question that motivates the next chapter.

This keeps the course cumulative rather than encyclopedic.

## 4. Use simulation as an experiment

The simulator should not be a moving illustration placed after the theory. It should be part of the reasoning process.

Preferred learning cycle:

```text
read
  ↓
predict
  ↓
run
  ↓
observe
  ↓
explain
  ↓
change one condition
  ↓
predict again
```

The learner should have a chance to be wrong before the simulator reveals the result.

Useful scenario roles include:

- expose a hidden state transition;
- compare two mechanisms that produce superficially similar outcomes;
- demonstrate an invariant;
- show that a plausible intuition fails;
- make a multi-step causal chain inspectable;
- compare the same initial state under different explicit assumptions;
- demonstrate a failure or blocked operation without corrupting state.

## 5. Prefer progressive concretization over premature abstraction

When possible, introduce a mechanism concretely before asking the learner to synthesize a broad abstract concept.

For example, it can be stronger to observe claims, bank deposits, reserves, and settlement before asking for a full synthesis of the monetary system.

Integration chapters are therefore valid. They may add little or no new code while producing an important new mental model.

## 6. Separate mechanism from realism

More realistic is not automatically more educational.

A chapter should add complexity because that complexity explains something new.

A simple model can intentionally omit:

- time;
- regulation;
- uncertainty;
- heterogeneous agents;
- institutional detail;
- secondary markets;
- physical constraints;
- strategic behavior.

Later chapters remove simplifications when those mechanisms become the learning target.

## 7. Distinguish kinds of knowledge

Curriculum text and scenarios should label materially different kinds of claims.

### Identity / invariant

A relation true by construction of the model.

### Domain or institutional rule

A rule of the selected system or institutional profile.

### Behavioral assumption

A chosen description of how an actor decides or reacts.

### Empirical parameter

A number calibrated or estimated from observations.

### Scenario input

A deliberately chosen condition or shock used for an experiment.

This classification prevents a learner from confusing accounting necessities with behavioral or empirical claims.

## 8. Handle institution-specific material explicitly

Some systems vary by jurisdiction, implementation, historical period, protocol version, or organizational policy.

Do not generalize one implementation into a universal rule.

Use one of these approaches:

- declare a stylized institutional profile;
- name the concrete jurisdiction/version being modeled;
- compare multiple profiles later;
- keep the current chapter at a more abstract mechanism level.

The model should make the chosen profile visible rather than silently embedding it.

## 9. Plan simulation complexity alongside curriculum complexity

The curriculum should anticipate when new simulation capabilities first become educationally necessary:

```text
SL0 — manual deterministic transitions
SL1 — multi-entity operation chains
SL2 — time and scheduled processes
SL3 — agents and feedback
SL4 — repeated experiments and sensitivity analysis
```

This avoids building a general simulator before the learning program has demonstrated the need for one.

## 10. Preserve earlier chapters

Later implementation may contain mechanisms that early chapters intentionally hide.

A mature application should still be able to expose the early chapter's bounded world:

```text
rich underlying software
        ↓
chapter projection
        ↓
only the concepts and actions appropriate to C01 / M01
```

Do not rewrite early learning history every time the software becomes more capable.

## 11. Use a short Lab 00 when needed

Before the subject itself, a short orientation can teach how to learn with the simulator:

- state;
- action;
- event;
- scenario;
- before / after;
- invariant;
- assumption;
- prediction.

This is not a domain chapter. It is a reusable learning-tool orientation.

## 12. Curriculum design workflow

Recommended workflow:

```text
1. Define target understanding.
2. List the major causal/mechanistic questions.
3. Build a prerequisite graph.
4. Convert the graph into a chapter sequence.
5. Define each chapter contract.
6. Design one or more learning scenarios per chapter.
7. Map chapters to M stages and SL levels.
8. Review intentional omissions and assumptions.
9. Review the entire sequence for conceptual jumps.
10. Only then implement the next chapter.
```

## 13. Review checklist

Before accepting a curriculum baseline, verify:

- every chapter has a specific learning goal;
- prerequisites are already established or explicitly introduced;
- the chapter exists for a learning reason, not a software reason;
- paragraphs form a coherent route to the goal;
- important bilingual terms are introduced naturally;
- every core scenario has Prediction, Action, Observable, and Learning payoff;
- important simplifications are declared;
- behavioral assumptions are not presented as identities or facts;
- institution-specific rules are scoped;
- simulation complexity grows only when needed;
- each chapter has exit criteria;
- each chapter leaves a meaningful next question;
- integration chapters are allowed when synthesis itself is the learning goal.

The template in [`learning-chapter-template.md`](learning-chapter-template.md) materializes this contract for concrete subjects.
