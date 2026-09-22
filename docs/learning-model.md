# Learning Model

The project treats simulation primarily as a tool for learning systems.

This approach is most suitable for subject areas where understanding depends substantially on:

- entities and state;
- algorithms and processes;
- rules and constraints;
- invariants;
- interactions between parts of a system;
- changes over time;
- causal consequences of actions;
- scenarios that can meaningfully be simulated.

Examples include financial systems, software systems, networks, game mechanics and economies, physical systems, control systems, logistics, and other domains with sufficiently explicit mechanisms.

It is less useful as the primary learning method when the subject is mainly declarative, interpretive, aesthetic, or otherwise cannot be represented meaningfully through system behavior. Simulation may still be used for individual mechanisms inside such subjects.

## Theory and executable models

Learning progresses along two connected tracks:

```text
Theory
  +
Executable domain model
```

Theory explains the concepts and mechanisms.

The executable model makes those mechanisms observable and allows them to be exercised through scenarios.

Neither replaces the other.

## Chapters

A subject is divided into learning chapters.

Each chapter introduces a coherent next layer of understanding.

A chapter may contain several theoretical sections or paragraphs:

```text
Chapter
├── § concept / mechanism
├── § concept / mechanism
├── § concept / mechanism
└── executable model
```

The chapter's executable model should contain the minimum system needed to exercise the mechanisms introduced by that chapter.

A chapter therefore defines both:

1. a learning scope;
2. a model scope.

## Progressive model development

Models normally develop together with the curriculum.

```text
Chapter 01 → Model 01

Chapter 02 → Model 02
             extends the understood system

Chapter 03 → Model 03
             adds another mechanism
```

Later models may reuse and extend earlier domain capabilities.

The purpose of progression is not to continuously increase realism. Complexity should be introduced when it enables a new piece of understanding.

An early model may intentionally omit real-world mechanisms that are not yet relevant.

For example:

```text
Chapter: Commercial Bank

Model:
  Bank
  Deposit
  Loan
  IssueLoan
  RepayPrincipal

Not modeled yet:
  central-bank reserves
  regulation
  bank failure
  government
```

The omission is deliberate. A later chapter can remove that simplification when the omitted mechanism becomes the subject of study.

## Chapters are not software versions

Learning progression and software maturity are separate dimensions.

```text
software:
v0.1 → v0.2 → v1.0

learning:
Chapter 01 → Chapter 02 → Chapter 03
```

A mature implementation should still be able to present an early chapter in its intentionally simplified form.

The underlying domain code may contain more capabilities than a chapter exposes.

## Paragraphs

A chapter can be divided into smaller theoretical units.

Example:

```text
Chapter 04 — Central Bank

§4.1 Why banks need another kind of money
§4.2 Reserve accounts
§4.3 Settlement
§4.4 Reserve shortage
§4.5 Central-bank lending
§4.6 Policy rate
```

Not every paragraph requires a new model. Several paragraphs can use one chapter model and different scenarios.

## Scenarios

A model becomes useful for learning through scenarios.

A scenario exercises one or more mechanisms of the chapter:

```text
initial state
    ↓
actions / processes
    ↓
state transitions
    ↓
observable result
```

Scenarios can be manually controlled or driven through simulation infrastructure such as agents, scheduled processes, physical dynamics, randomness, or external events.

The goal is to make the mechanism inspectable rather than merely produce an outcome.

## Visualization

Visualization is used when it improves observability of the running model.

It may expose:

- current state;
- state transitions;
- events;
- flows;
- timelines;
- metrics over time.

The visualization is secondary to the domain model and scenario. It should remain as simple as necessary to understand the mechanism being studied.

Successful project-specific visualizations can be retained as examples and reused when similar needs appear.

## Development principle

The project should develop primarily by studying concrete subjects rather than by designing a universal simulation framework in advance.

The preferred process is:

```text
select subject
    ↓
analyze learning progression
    ↓
define chapter
    ↓
identify required domain mechanisms
    ↓
implement minimal executable model
    ↓
create scenarios
    ↓
add only the observability required to understand them
    ↓
continue to the next chapter
```

Reusable simulation infrastructure and abstractions should be extracted when repeated needs appear across concrete models.
