# Chapter 01 — Claims and Balance Sheets

## Learning goal

Understand the most basic accounting relationship behind financial claims:

> one claim is simultaneously an asset of its holder and a liability of its issuer.

This chapter intentionally does **not** model banks, reserves, loans, interest, government, or markets yet.

## §1.1 Claim

A claim is a right held by one party against another party.

In this model:

- **issuer** owes the claim;
- **holder** owns the claim;
- **amount** is the claim's face value.

## §1.2 Asset and liability are two views of the same relationship

If the issuer owes Alice 100 EUR:

```text
Alice
  asset: Claim +100

Issuer
  liability: Claim +100
```

System invariant:

```text
total claim assets == total claim liabilities
```

## §1.3 Transfer

If Alice transfers the claim to Bob:

```text
Alice asset 100 → 0
Bob asset     0 → 100
Issuer liability remains 100
```

Ownership changes. Outstanding claims do not.

## §1.4 Settlement

If Bob settles the claim with the issuer:

```text
Bob asset          100 → 0
Issuer liability   100 → 0
```

The asset and liability disappear together.

## Model scope

Implemented:

- Party
- Money
- Claim
- ClaimBook
- issue
- transfer
- settle
- balance invariant
- explicit simulation trace

Intentionally omitted:

- commercial banks;
- deposits;
- loans;
- central-bank reserves;
- interest;
- defaults;
- government;
- production and markets.
