# Learning Chapter Template

Use this template when designing a chapter before implementation. Remove sections that are genuinely not applicable, but do not omit material assumptions merely for brevity.

```markdown
# Chapter NN — Русское название (English Name)

## Learning goal

After this chapter, the learner can ...

## Prerequisites

- ...

## Why this chapter exists

What unresolved question from the previous chapter does it answer?

## Paragraphs

### §N.1 ... (...)

### §N.2 ... (...)

### §N.3 ... (...)

## Important terms

Introduce terms naturally in the text using the course's bilingual rule, for example:

- обязательство (**liability**)
- платёжеспособность (**solvency**)

Only list terms here when a compact reference is useful.

## Knowledge classification

### Identities / invariants

- ...

### Domain / institutional rules

- ...

### Behavioral assumptions

- ...

### Empirical parameters

- ...

### Scenario inputs

- ...

## Executable model

Model stage: `MNN`

Simulation level: `SL0 | SL1 | SL2 | SL3 | SL4`

New capabilities:

- ...

Reused capabilities:

- ...

Intentionally hidden / omitted:

- ...

## Scenario SNN.1 — Name

### Learning question

...

### Initial state

...

### Prediction

Before running it, ask the learner: ...

### Trigger

...

### Observable

- ...

### Expected transition

...

### Learning payoff

...

### Variation

Change one condition and predict again: ...

## Scenario SNN.2 — Name

Repeat the same contract when another scenario teaches a materially different distinction.

## Visualization

What is the smallest view that makes the mechanism understandable?

- state table / before-after diff / flow / timeline / chart / comparison / distribution

## Exit criteria

The learner can, without relying on the prepared trace:

1. ...
2. ...
3. ...

## Next question

What question now becomes unavoidable and motivates the next chapter?

## Sources / institutional profile

List authoritative references or the explicit institutional/version profile when required.
```

## Template rules

- The chapter is a learning unit, not a software milestone.
- A paragraph does not imply a new class.
- A model stage does not imply a separate source tree.
- A scenario must exist for a learning purpose, not just as a feature demo.
- The learner predicts before the core result is revealed.
- Intentional omissions are part of the chapter contract.
- Later software must be able to preserve the early chapter's bounded view.
