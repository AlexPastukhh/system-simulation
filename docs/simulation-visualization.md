# Simulation Visualization

The visualization exists to make a running simulation observable.

It does not need to explain the source-code structure. Code diagrams are a separate concern.

The visual layer should remain simple and grow only when a scenario needs more observability.

## Useful views

### Current world state

Show the important entities and values for the current scenario.

Example for a banking simulation:

```text
                 CENTRAL BANK
             reserves: 2,000
                /        \
             960          1,040
             /              \
          BANK A           BANK B
       deposits 60      deposits 40
       loans   100      loans     0
           |                |
         Alice             Bob
```

This is a view of the simulated world, not a class diagram.

### Event / state change

When an action occurs, show what changed.

```text
Alice pays Bob 40

Alice.deposit       100 → 60
Bob.deposit           0 → 40
BankA.reserves     1000 → 960
BankB.reserves     1000 → 1040

Total deposits       100 → 100
Total reserves      2000 → 2000
```

For many educational scenarios this may be the most useful visualization.

### Timeline

A short event history makes the temporal sequence explicit.

```text
0  Initial state
1  Bank A issues Alice a loan
2  Alice pays Bob
3  Government spends to Bob
4  Bob pays tax
```

Selecting a point in the timeline can restore or inspect that simulation state.

### Flows

When something moves between entities, show the direction and amount.

Examples include money, reserves, goods, energy, packets, material, or organisms.

The visual should reflect the modeled semantics. For example, bank credit creation should not be shown as an existing pile of money physically moving from a vault if the domain model says a new deposit is created.

### Metrics over time

Charts are useful when the important behavior emerges over many simulation steps.

Examples:

- money supply;
- private debt;
- prices;
- production;
- employment;
- inventory;
- energy;
- population.

They are less useful for a single short transaction that can be understood directly from state changes.

## Controls

Simulation controls should invoke meaningful domain or scenario actions.

Examples:

```text
Issue loan
Make payment
Raise policy rate
Collect tax
Run next step
Advance one month
Pause
Reset scenario
```

Avoid exposing arbitrary raw state mutation unless the simulation explicitly needs a debugging mode.

## Visual examples as project assets

There is no need to define a large visualization framework up front.

When a visualization works well for a concrete simulation, keep it as a project example.

A useful example can include:

- a screenshot or executable demo;
- the scenario it visualizes;
- a short note on what it makes visible;
- any important choice about what it intentionally hides.

Over time these examples can become reusable patterns if actual repetition appears.

The preferred direction is:

```text
concrete simulation
    ↓
useful visualization
    ↓
keep successful example
    ↓
notice repetition across examples
    ↓
extract reusable component only when justified
```
