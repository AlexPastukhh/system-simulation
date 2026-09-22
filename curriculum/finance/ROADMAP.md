# Finance Curriculum Roadmap

Status: planning baseline for the finance subject.

This roadmap applies the reusable learning and executable-model principles defined in:

- [`../../docs/curriculum-design.md`](../../docs/curriculum-design.md)
- [`../../docs/executable-learning-model-design.md`](../../docs/executable-learning-model-design.md)
- [`../../docs/learning-chapter-template.md`](../../docs/learning-chapter-template.md)

The finance subject is designed as a cumulative chain of questions. Each chapter introduces only the mechanisms needed for the next layer of understanding and pairs them with executable learning scenarios.

The current executable `ch01` predates this roadmap. This roadmap intentionally does not change that code or chapter file; alignment is deferred to a later implementation package.

## Course conventions

### Bilingual terminology

The main explanatory language is Russian. Important professional terms are introduced with the English equivalent at the first or conceptually important use:

> финансовое требование (**financial claim**)

> обязательство (**liability**)

> межбанковский расчёт (**interbank settlement**)

Code/API vocabulary remains English.

### Four progressions

```text
Learning:          C01 → C02 → ... → C21
Model capability:  M01 → M02 → ... → M21
Simulation level:  SL0 → SL1 → SL2 → SL3 → SL4
Software release:  v0.x → v1.x → ...
```

These dimensions are independent. A mature software release should still be able to present `C01 / M01` without exposing later mechanisms.

### Learning loop

Every core scenario should support:

```text
Theory → Predict → Run → Observe → Explain → Modify → Exit
```

### Knowledge labels

From the beginning, and especially in later macroeconomic chapters, distinguish:

- **identity / invariant**;
- **domain or institutional rule**;
- **behavioral assumption**;
- **empirical parameter**;
- **scenario input / shock**.

### Simulation levels

- `SL0` — manual deterministic transitions;
- `SL1` — multi-entity operation chains and transaction states;
- `SL2` — clock, scheduling, accrual, maturity, periodic processes;
- `SL3` — agents, policies, controllers, feedback loops;
- `SL4` — repeated runs, controlled randomness, parameter sweeps, sensitivity analysis.

## Lab 00 — Как учиться с симулятором (How to Learn With the Simulator)

This is an orientation, not a finance chapter.

### Topics

- состояние (**state**);
- действие (**action**);
- событие (**event**);
- сценарий (**scenario**);
- изменение `before → after`;
- инвариант (**invariant**);
- предположение (**assumption**);
- prediction before execution.

### Scenario

Run one tiny non-financial or neutral state transition, first predict the result, then inspect the trace.

### Learning payoff

The learner understands that the simulator is not an answer machine. It is an experimental instrument for checking an explicit causal model.

---

# Part I — Financial Claims and Accounting

## C01 / M01 — Финансовые требования (Financial Claims)

### Learning goal

Понять двустороннюю природу финансового требования: один и тот же `claim` является активом (**asset**) держателя и обязательством (**liability**) эмитента/должника.

### Paragraphs

- §1.1 Стороны финансового отношения (Parties)
- §1.2 Финансовое требование (Financial Claim)
- §1.3 Держатель (Holder) и эмитент/должник (Issuer)
- §1.4 Актив (Asset) и обязательство (Liability)
- §1.5 Передача требования (Transfer)
- §1.6 Исполнение/погашение требования (Claim Discharge)

`Claim discharge` здесь намеренно не называется interbank `settlement`: механизм, чем именно issuer исполняет claim, пока абстрагирован.

### M01

`Party`, `Claim`, `ClaimBook`, `IssueClaim`, `TransferClaim`, `DischargeClaim`.

Simulation level: `SL0`.

### Core scenarios

**S01.1 Issue claim.** Prediction: если issuer создаёт claim 100 в пользу Alice, какие две стороны баланса отношений появляются? Observable: `Alice asset +100`, `Issuer liability +100`. Learning payoff: asset и liability — две стороны одного финансового отношения.

**S01.2 Transfer claim.** Prediction: исчезает ли obligation issuer, если Alice передаст claim Bob? Observable: holder меняется, issuer liability не меняется. Learning payoff: transfer ≠ discharge.

**S01.3 Discharge claim.** Prediction: что должно исчезнуть при исполнении требования? Observable: asset holder и corresponding liability issuer исчезают вместе. Learning payoff: extinguishing the relationship affects both sides.

### Intentional omissions

Нет полноценного balance sheet, equity, банков, депозитов, резервов, времени и механизма, которым claim discharge physically/economically выполняется.

### Exit

Learner can explain why one claim is an asset and a liability simultaneously and distinguish transfer from discharge.

### Next question

Как системно записывать много таких отношений и проверять, что accounting state согласован?

---

## C02 / M02 — Баланс и двойная запись (Balance Sheet & Double-Entry Accounting)

### Learning goal

Понять balance sheet, equity и почему одна transaction обычно меняет несколько accounts.

### Paragraphs

- §2.1 Запас и поток (Stock vs Flow)
- §2.2 Активы, обязательства и капитал (Assets, Liabilities, Equity)
- §2.3 Балансовое равенство (Balance-Sheet Equation)
- §2.4 Счёт (Account)
- §2.5 Проводка и двойная запись (Posting / Double Entry)
- §2.6 Journal Entry как переход состояния

### M02

Adds `Account`, `AccountType`, `Ledger`, `Posting`, `JournalEntry`, `Equity`.

Simulation level: `SL0`.

### Core scenarios

**S02.1 Asset transformation.** `Cash 100 → 60`, `Equipment 0 → 40`. Prediction: changed ли net worth? Observable: asset composition changes, total assets/equity do not. Learning payoff: transaction may change composition without changing wealth.

**S02.2 Acquire asset with debt.** `Equipment +60`, `Debt +60`. Prediction: does more assets necessarily mean more net worth? Observable: assets and liabilities expand together. Learning payoff: gross assets ≠ net worth.

**S02.3 Repay liability.** `Cash -20`, `Debt -20`. Learning payoff: paired accounting changes and preserved identity.

### Exit

Learner can construct and explain a simple journal entry and distinguish stock, flow, assets, liabilities, and equity.

### Next question

Как выглядит конкретный financial claim, которым люди обычно платят в современной банковской системе?

---

# Part II — Commercial Bank Money and Credit

## C03 / M03 — Банковский депозит (Bank Deposit)

### Learning goal

Понять, что balance на банковском счёте — это financial claim клиента к commercial bank, а не отдельная коробка с принадлежащими клиенту банкнотами.

### Paragraphs

- §3.1 Коммерческий банк (Commercial Bank)
- §3.2 Депозитный счёт (Deposit Account)
- §3.3 Депозит как claim к банку
- §3.4 Deposit как asset клиента
- §3.5 Deposit как liability банка
- §3.6 Платёж между клиентами одного банка (Same-Bank Payment)

### M03

Adds `CommercialBank`, `Customer`, `DepositAccount`, `BankDeposit`, `InternalPayment`.

Simulation level: `SL0`.

The chapter starts from a declared opening balance sheet. It does not invent an unexplained origin story for the initial deposit.

### Core scenarios

**S03.1 Inspect deposit.** Prediction: whose liability is Alice's deposit asset? Observable: one amount appears on Alice and Bank balance sheets from opposite perspectives. Learning payoff: bank deposit is a bank liability.

**S03.2 Same-bank payment.** Alice pays Bob 30 inside one bank. Observable: `Alice deposit -30`, `Bob deposit +30`, total bank deposit liabilities unchanged. Learning payoff: payment can transfer ownership of bank money without creating/destroying its total amount.

### Intentional omissions

Origin of bank assets/deposits, loans, reserves, cash withdrawal, regulation.

### Next question

Откуда новые bank deposits вообще появляются?

---

## C04 / M04 — Банковский кредит и создание депозитов (Bank Lending & Deposit Creation)

### Learning goal

Понять balance-sheet mechanics loan origination and principal repayment.

### Paragraphs

- §4.1 Кредитный договор (Loan)
- §4.2 Loan как liability borrower
- §4.3 Loan как asset банка
- §4.4 Выдача кредита (Loan Origination)
- §4.5 Одновременное создание deposit
- §4.6 Погашение principal

### M04

Adds `Loan`, `Borrower`, `IssueLoan`, `RepayPrincipal`, `CloseLoan`.

Simulation level: `SL0`.

### Core scenarios

**S04.1 Issue loan 100.** Prediction: does the bank debit an existing saver's deposit? Observable: `Bank loan asset +100`, `Bank deposit liability +100`, `Borrower deposit asset +100`, `Borrower loan liability +100`. Learning payoff: bank lending expands both sides rather than simply transferring an existing saver deposit.

**S04.2 Repay principal 40.** Observable: loan and deposit amounts contract together in the simplified same-bank scenario. Learning payoff: principal repayment reverses part of the balance-sheet expansion.

### Important scope note

The chapter explains the accounting mechanism, not an unlimited lending capacity. Capital, funding, liquidity, risk, regulation, borrower demand, profitability, and monetary policy constraints are later subjects.

### Next question

Что происходит, когда borrower тратит созданный deposit человеку в другом банке?

---

# Part III — Multiple Banks, Reserves, and Settlement

## C05 / M05 — Проблема двух банков (The Two-Bank Problem)

### Learning goal

Понять, почему same-bank ledger transfer недостаточен для payment между клиентами независимых банков.

### Paragraphs

- §5.1 Два независимых bank ledgers
- §5.2 Cross-Bank Payment Instruction
- §5.3 Почему Bank A не может изменить ledger Bank B
- §5.4 Межбанковское обязательство (Interbank Obligation)
- §5.5 Clearing
- §5.6 Требование к общему settlement asset

### M05

Adds second bank, `PaymentInstruction`, `InterbankObligation`, `ClearingPosition`.

Simulation level: `SL1`.

### Core scenarios

**S05.1 Attempt cross-bank payment without settlement mechanism.** Prediction: can Bank A simply decrease Alice and force Bank B to increase Bob? Model should reject completion without partial invalid mutation. Observable: payment remains unresolved/blocked. Learning payoff: independent issuers need an interbank mechanism.

**S05.2 Create clearing obligation.** Observable: Bank A owes Bank B 30, but customer payment is not yet finally settled. Learning payoff: clearing obligation ≠ final settlement.

### Next question

Какой asset могут использовать оба банка для окончательного расчёта?

---

## C06 / M06 — Центральный банк и резервы (Central Bank & Reserves)

### Learning goal

Понять reserves как financial claims коммерческих банков к central bank.

### Paragraphs

- §6.1 Центральный банк (Central Bank)
- §6.2 Резервный счёт (Reserve Account)
- §6.3 Reserve как asset commercial bank
- §6.4 Reserve как liability central bank
- §6.5 Holders of reserves
- §6.6 Transfer of reserves

### M06

Adds `CentralBank`, `ReserveAccount`, `ReserveBalance`, `TransferReserves`.

Simulation level: `SL1`.

### Core scenario

**S06.1 Reserve transfer.** Bank A transfers 30 reserves to Bank B. Prediction: does total reserve quantity necessarily change? Observable: A -30, B +30, central-bank liabilities shift between holders, total unchanged. Learning payoff: reserves are another financial claim with a different issuer and holder population.

### Next question

Как reserve transfer завершает customer cross-bank payment from C05?

---

## C07 / M07 — Межбанковский расчёт (Interbank Settlement)

### Learning goal

Соединить customer deposit transfer и reserve transfer в одну complete payment chain.

### Paragraphs

- §7.1 Payment instruction
- §7.2 Customer deposit legs
- §7.3 Reserve settlement leg
- §7.4 Clearing vs settlement
- §7.5 Settlement finality
- §7.6 Full cross-bank payment trace

### M07

Adds end-to-end `InterbankPayment` / `SettlementService` composition using M05 + M06 capabilities.

Simulation level: `SL1`.

### Core scenario

**S07.1 Alice at Bank A pays Bob at Bank B 30.** Observable: `Alice deposit -30`, `Bank A reserves -30`, `Bank B reserves +30`, `Bob deposit +30`. Important invariants: total customer deposits unchanged in this transfer scenario; total reserves unchanged. Learning payoff: retail payment and bank settlement are related but distinct layers.

### Variation

Run the same payment inside one bank and compare which state transitions disappear.

### Next question

Что происходит, если тысячи payments идут в обе стороны и reserves недостаточно для gross settlement каждого отдельно?

---

## C08 / M08 — Clearing, Netting and Liquidity

### Learning goal

Понять difference between gross payment obligations, net settlement positions, and settlement liquidity.

### Paragraphs

- §8.1 Gross settlement
- §8.2 Clearing
- §8.3 Netting
- §8.4 Net position
- §8.5 Settlement liquidity
- §8.6 Liquidity shortage and intraday liquidity

### M08

Adds `PaymentBatch`, `ClearingHouse`, `NetPosition`, `SettlementQueue`, optional stylized `LiquidityFacility`.

Simulation level: `SL1`.

### Core scenarios

**S08.1 Bilateral netting.** Example: A→B obligations 900, B→A obligations 850. Observable: gross obligations 1750 versus net settlement obligation 50. Learning payoff: payment volume ≠ settlement liquidity requirement.

**S08.2 Reserve shortage.** A has 40 available reserves and a net obligation 70. Payment remains pending until a declared liquidity source adds capacity. Learning payoff: liquidity is the ability to meet settlement obligations on time; do not infer solvency yet.

### Next question

Как deposits, cash и reserves вместе образуют monetary system rather than unrelated claims?

---

## C09 / M09 — Денежная система (The Monetary System)

### Learning goal

Собрать изученные instruments into one mental model of money, issuance, convertibility, and settlement.

### Paragraphs

- §9.1 Money as a special financial claim
- §9.2 Наличные (Currency / Cash)
- §9.3 Bank Deposits
- §9.4 Central Bank Reserves
- §9.5 Convertibility at par
- §9.6 Единство денег (Singleness of Money)

### M09

Integration model. Adds `Cash`/currency representation and a `MoneyView`/instrument matrix if useful, but its main purpose is synthesis rather than new mechanics.

Simulation level: `SL1`.

### Core scenario

**S09.1 Follow value through instruments.** Trace a stylized path across cash/deposit/payment/reserve settlement while displaying `instrument`, `issuer`, `holder`, `who can use it`, and `what settles it`. Learning payoff: “money” is understood through institutional relationships already observed, not only through an abstract definition.

### Exit

Learner can distinguish deposit, cash, and reserve claims and explain why users can generally treat same-currency bank deposits at par in the modeled two-tier system.

### Next question

Что меняется, если financial contracts evolve through time and interest accrues even without a new payment action?

---

# Part IV — Time, Bank Income, and Stability

## C10 / M10 — Процент и время (Interest & Time)

### Learning goal

Понять principal, interest, maturity, accrual, and the distinction between interest accruing and interest being paid.

### Paragraphs

- §10.1 Principal
- §10.2 Interest
- §10.3 Interest Rate
- §10.4 Maturity
- §10.5 Interest Accrual
- §10.6 Repayment Schedule

### M10

Adds `SimulationClock`, `Scheduler`, `LoanTerms`, `AccruedInterest`, `PaymentSchedule`.

Simulation level: first `SL2` chapter.

### Core scenarios

**S10.1 Advance time without payment.** Prediction: can financial state change without a transfer? Observable: accrued interest changes according to explicit contract/rule. Learning payoff: time-dependent flow versus transaction.

**S10.2 Accrual vs payment.** Compare accounting state when interest accrues with state after actual payment. Learning payoff: economic accrual and money movement are not the same event.

### Next question

Как interest income, expenses, losses, and equity affect the commercial bank itself?

---

## C11 / M11 — Доход, капитал и платёжеспособность банка (Bank Income, Capital & Solvency)

### Learning goal

Понять how profits/losses change bank equity and how loan losses can produce insolvency.

### Paragraphs

- §11.1 Bank income and expense
- §11.2 Profit
- §11.3 Equity / Bank Capital
- §11.4 Interest income
- §11.5 Credit loss / write-down
- §11.6 Solvency

### M11

Adds `BankIncome`, `BankExpense`, `BankEquity`, `LoanLoss`, `WriteDown` and selected solvency metrics.

Simulation level: `SL2`.

### Core scenarios

**S11.1 Interest payment.** In a simplified same-bank case, inspect customer deposit reduction and bank equity/income effect. Learning payoff: principal and interest payments have different balance-sheet meanings. Explicitly note that later bank spending/salaries/dividends may redistribute deposits again; a single payment trace is not a claim that interest permanently removes money from circulation.

**S11.2 Loan loss.** Write down a bad loan against equity. Observable: asset loss reduces equity; crossing zero demonstrates insolvency in the simplified accounting model. Learning payoff: bank capital absorbs losses.

### Next question

Может ли solvent bank nevertheless fail to settle payments today?

---

## C12 / M12 — Ликвидность, стресс и bank run (Liquidity Stress & Bank Runs)

### Learning goal

Сделать различие liquidity vs solvency operationally obvious.

### Paragraphs

- §12.1 Liquidity
- §12.2 Solvency
- §12.3 Deposit outflow
- §12.4 Bank run
- §12.5 Lender of Last Resort
- §12.6 Deposit insurance — conceptual role

### M12

Adds stress scenarios, outgoing payment pressure, liquidity sources, and optional stylized withdrawal/transfer behavior. Do not yet require behavioral agents unless the run mechanism itself becomes the learning target.

Simulation level: `SL2`, with a path to `SL3` later.

### Core scenarios

**S12.1 Solvent but illiquid.** Good assets and positive equity, but available settlement liquidity is below outgoing payment demand. Observable: payments cannot all settle now while net worth remains positive. Learning payoff: liquidity shortage is not insolvency.

**S12.2 Liquid but insolvent.** High reserves but negative equity after asset losses. Learning payoff: reserves do not repair negative net worth.

**S12.3 Optional run sequence.** Increase transfer/withdrawal requests under an explicit scenario policy. Learning payoff: a run is a dynamic liquidity process, not the definition of insolvency.

### Next question

Как government payments and taxes enter the same monetary plumbing without confusing Treasury and central bank?

---

# Part V — Government and Monetary Policy

## C13 / M13 — Государственные платежи и налоги (Government Payments & Taxes)

### Learning goal

Понять fiscal payment flows inside an explicitly declared institutional profile.

### Paragraphs

- §13.1 Government sector vs central bank
- §13.2 Treasury
- §13.3 Government cash / Treasury account
- §13.4 Government spending
- §13.5 Taxes
- §13.6 Fiscal balance

### M13

Adds `Treasury`, government payment/tax operations, and an explicit `InstitutionalProfile` or clearly documented stylized arrangement.

Simulation level: `SL2`.

### Core scenarios

**S13.1 Government payment.** Under the selected profile, trace Treasury/central-bank/bank/household balance-sheet changes. Learning payoff: fiscal payment uses financial infrastructure already understood.

**S13.2 Tax payment.** Trace the reverse direction under the same profile and compare with ordinary private payment.

### Critical scope rule

Treasury-central-bank account and debt-management arrangements vary by jurisdiction and period. The chapter must name a stylized or concrete profile; it must not present one implementation as a universal law.

### Next question

Как government funds itself through securities and how does primary issuance differ from later trading?

---

## C14 / M14 — Государственный долг (Government Debt)

### Learning goal

Понять government bond as a financial claim and distinguish issuance from secondary transfer.

### Paragraphs

- §14.1 Government Bond
- §14.2 Bond as financial claim
- §14.3 Primary issuance
- §14.4 Coupon
- §14.5 Maturity and redemption
- §14.6 Secondary market

### M14

Adds `GovernmentBond`, `BondHolding`, `IssueBond`, `TransferBond`, `RedeemBond` within the chosen institutional profile.

Simulation level: `SL2`.

### Core scenarios

**S14.1 Primary issuance.** New government liability is created and acquired. Learning payoff: issuance changes government outstanding debt and investor asset composition.

**S14.2 Secondary sale.** Alice transfers an existing bond to Bob. Observable: holder changes while government outstanding bond does not. Learning payoff: primary issuance ≠ secondary market trade.

### Next question

Что central bank directly changes through monetary policy, and what later economic reactions are assumptions rather than accounting identities?

---

## C15 / M15 — Денежно-кредитная политика (Monetary Policy)

### Learning goal

Separate operational monetary-policy mechanisms from behavioral transmission assumptions.

### Paragraphs

- §15.1 Policy Rate
- §15.2 Central-bank facilities / reserve remuneration
- §15.3 Financial conditions and bank pricing
- §15.4 Transmission assumptions
- §15.5 Quantitative Easing (QE)
- §15.6 Quantitative Tightening (QT)

### M15

Adds `MonetaryPolicy`, `PolicyRate`, selected central-bank facilities, `AssetPurchase`/`AssetSale`, and optional explicit pricing policies.

Simulation level: `SL2`, with controlled policies beginning to appear.

### Core scenarios

**S15.1 Policy-rate change.** Directly change the policy variable, then optionally apply a clearly labelled bank pricing policy such as `loan_rate = policy_rate + spread`. Learning payoff: central-bank operation is distinct from the modeled transmission response.

**S15.2 QE purchase from non-bank holder.** Trace central-bank asset increase, reserve increase at the commercial bank, investor bond decrease, and investor deposit increase. Learning payoff: counterparty and payment mechanics matter.

**S15.3 QE purchase from a bank.** Compare with direct bank counterparty: bank swaps bond for reserves while customer deposits need not change in the same way. Learning payoff: reserve creation ≠ automatically identical public-deposit effect.

### Next question

До сих пор мы в основном моделировали financial claims. Где реальные goods, labor and production?

---

# Part VI — Real Economy and Markets

## C16 / M16 — Домохозяйства, фирмы и производство (Households, Firms & Production)

### Learning goal

Separate financial state from real production and consumption.

### Paragraphs

- §16.1 Financial asset vs real asset
- §16.2 Household
- §16.3 Firm
- §16.4 Labor and wage
- §16.5 Production
- §16.6 Goods and inventory

### M16

Adds `Household`, `Firm`, `Worker`, `Product`, `Inventory`, `ProductionProcess`.

Simulation level: `SL2`.

### Core scenario

**S16.1 Produce, earn, consume.** Firm hires/uses labor, production creates goods, wage payment changes financial claims, household consumption transfers money and reduces inventory. Learning payoff: creation of output and transfer of money are distinct processes.

### Next question

Что происходит, когда desired purchases exceed available goods/capacity and prices are allowed to respond?

---

## C17 / M17 — Рынки, цены и дефицитность (Markets, Prices & Scarcity)

### Learning goal

Понять that price dynamics require an explicit market/price-formation mechanism rather than emerging from accounting alone.

### Paragraphs

- §17.1 Scarcity
- §17.2 Supply
- §17.3 Demand
- §17.4 Inventory / capacity
- §17.5 Price
- §17.6 Price-formation rule

### M17

Adds `Market`, demand/supply representation, `PricingPolicy`, capacity/inventory constraints.

Simulation level: `SL2`; policies are explicit but not yet fully autonomous macro agents.

### Core scenarios

**S17.1 Demand shock under one explicit pricing rule.** Learning payoff: observe consequences of the chosen rule, not a universal law.

**S17.2 Same initial state, two pricing rules.** Example: sticky versus responsive pricing. Observable: different price/inventory/output paths. Learning payoff: behavioral/institutional mechanism matters; simulation must label it as an assumption/policy.

### Next question

Как many local spending, lending, pricing and investment decisions create system-wide feedback?

---

# Part VII — Macro Feedback, Distribution, and Automation

## C18 / M18 — Кредит и макроэкономические обратные связи (Credit & Macro Feedback)

### Learning goal

Понять how local decisions form feedback loops across credit, spending, revenue, production, losses, and future lending.

### Paragraphs

- §18.1 Household spending behavior
- §18.2 Firm investment
- §18.3 Bank credit policy
- §18.4 Aggregate demand
- §18.5 Debt servicing
- §18.6 Feedback loops

### M18

Adds `HouseholdAgent`, `FirmAgent`, `BankAgent` or equivalent drivers plus explicit `SpendingPolicy`, `InvestmentPolicy`, `CreditPolicy`.

Simulation level: first full `SL3` chapter.

### Core scenarios

**S18.1 Credit expansion loop.** Easier credit under an explicit policy affects borrowing, deposits, spending, firm revenue, and investment. Learning payoff: multi-step feedback cannot be understood as one transaction.

**S18.2 Negative income/default shock.** Trace income decline → default pressure → bank loss/credit-policy reaction → spending/investment feedback. Learning payoff: outcomes depend on policy assumptions; identities and behavioral rules must remain separately labelled.

### Next question

Даже при одинаковом output, почему purchasing power can be distributed very differently?

---

## C19 / M19 — Доход, собственность и распределение (Income, Ownership & Distribution)

### Learning goal

Separate production from distribution and identify different income channels.

### Paragraphs

- §19.1 Wage income
- §19.2 Profit
- §19.3 Interest
- §19.4 Dividend
- §19.5 Transfer
- §19.6 Ownership and purchasing power

### M19

Adds `Ownership`, `EquityShare`, `Dividend`, `IncomeFlow`, `Transfer` and distribution metrics.

Simulation level: `SL3`.

### Core scenario

**S19.1 Same production, different ownership.** Keep technology/output/prices fixed, vary capital ownership distribution. Observable: household income/purchasing-power distribution changes while production is held constant. Learning payoff: production and distribution are separate mechanisms.

### Next question

Что меняется, если technology allows the same or greater output with less direct labor?

---

## C20 / M20 — Автоматизация и труд (Automation & Labor)

### Learning goal

Понять that automation does not determine one universal labor outcome; effects depend on whether technology substitutes for or complements labor and on ownership/distribution institutions.

### Paragraphs

- §20.1 Productivity
- §20.2 Automation Capital
- §20.3 Labor substitution
- §20.4 Labor complementarity
- §20.5 Wage share
- §20.6 Ownership of automated production

### M20

Adds `AutomationCapital`, `AutomationPolicy`, labor-demand/productivity relationships.

Simulation level: `SL3`.

### Core scenarios

**S20.1 Gradual substitution profile.** Increase automation under a declared substitution assumption and observe output, labor demand, wages, profit, consumption.

**S20.2 Complementarity profile.** Apply the same technology improvement under a productivity-augmentation assumption. Compare paths. Learning payoff: “automation” alone is not a complete causal model.

**S20.3 Same technology, different ownership.** Hold technology fixed and vary ownership. Learning payoff: technology and distribution institutions are separate causal layers.

### Next question

Если wage income перестаёт быть главным distribution channel, какие alternative institutions can distribute purchasing power?

---

## C21 / M21 — Лаборатория посттрудовых систем (Post-Labor Systems Laboratory)

### Learning goal

Use the accumulated model to compare explicitly defined distribution institutions under controlled assumptions without turning the simulator into a normative answer engine.

### Paragraphs

- §21.1 Production without proportional labor income
- §21.2 Purchasing-power problem
- §21.3 Universal transfers / UBI
- §21.4 Broad capital ownership
- §21.5 Citizen dividend / public wealth fund
- §21.6 Mixed institutional systems

### M21

Adds configurable `DistributionPolicy`, `TaxTransferPolicy`, `BasicIncomePolicy`, `DividendPolicy`, `OwnershipPolicy`, and optional public-fund mechanisms.

Simulation level: `SL4`.

### Core experiment

Hold as much as possible constant:

```text
population
technology
productive capacity
automation profile
initial state
behavioral model / seed where applicable
```

Vary one institutional design at a time, for example:

- wage-heavy baseline;
- wage + basic income;
- broad capital ownership;
- citizen dividend / public fund;
- mixed system.

Observe selected outcomes such as production, consumption, debt, defaults, income/wealth distribution, capacity utilisation, inventories, prices, fiscal flows, and financial stability.

### Learning payoff

The simulator must not answer “which system is best”. The educational objective is:

> understand which consequences arise from which explicit institutional rules under which behavioral assumptions and parameter choices.

Repeated runs and sensitivity analysis are used to test robustness, not to hide assumptions behind averages.

### Exit

Learner can identify the mechanisms, assumptions, and distribution channels responsible for a result and can explain why changing one assumption may reverse the result.

---

# Course dependency chain

The intended conceptual progression is:

```text
financial claim
  ↓
accounting system
  ↓
bank deposit
  ↓
bank lending / deposit creation
  ↓
two-bank problem
  ↓
central-bank reserves
  ↓
interbank settlement
  ↓
clearing / netting / liquidity
  ↓
monetary-system synthesis
  ↓
time / interest
  ↓
bank income / capital / solvency
  ↓
liquidity stress
  ↓
government payments
  ↓
government debt
  ↓
monetary policy
  ↓
real production
  ↓
markets / prices
  ↓
macro feedback
  ↓
ownership / distribution
  ↓
automation
  ↓
post-labor institutional experiments
```

# Model progression

```text
M01  Claims
M02  + Accounting Ledger
M03  + Commercial Bank / Deposits
M04  + Loans / Deposit Creation
M05  + Multiple Banks / Payment Intent
M06  + Central Bank / Reserves
M07  + Interbank Settlement
M08  + Clearing / Netting / Liquidity
M09  Monetary-System Integration + Cash
M10  + Clock / Interest
M11  + Income / Equity / Loss
M12  + Liquidity Stress
M13  + Government Institutional Profile
M14  + Government Securities
M15  + Monetary Policy Operations
M16  + Real Economy
M17  + Markets / Pricing Policies
M18  + Agents / Feedback
M19  + Ownership / Income Channels
M20  + Automation
M21  + Institutional Experiment Framework
```

# Simulation progression

```text
C01–C04  → SL0
C05–C09  → SL1
C10–C17  → SL2
C18–C20  → SL3
C21      → SL4
```

This mapping is a planning default, not a rigid implementation law. A chapter may use a lower level if the learning question can be answered more simply.

# Roadmap validation rules

Before implementation of a chapter begins, confirm:

1. Its prerequisites are already established.
2. Its paragraphs lead to one coherent learning goal.
3. At least one executable scenario has a clear Prediction, Observable, and Learning payoff.
4. The model stage contains no unnecessary conceptual machinery.
5. Important omissions and institutional/behavioral assumptions are explicit.
6. The scenario does not rely on a later mechanism without saying so.
7. The exit criteria can be answered without memorizing the prepared trace.
8. The next question follows naturally from what remains unresolved.

# Reference frame used to verify the finance progression

These sources are reference checks for the planned mechanisms, not a claim that one institution's implementation is universal:

- Bank of England, *Money in the modern economy: an introduction* — money as special IOUs; currency, bank deposits and central-bank reserves: https://www.bankofengland.co.uk/quarterly-bulletin/2014/q1/money-in-the-modern-economy-an-introduction
- Bank of England, *Money creation in the modern economy* — commercial-bank lending and deposit creation, repayment and constraints: https://www.bankofengland.co.uk/quarterly-bulletin/2014/q1/money-creation-in-the-modern-economy
- BIS, *The next-generation monetary and financial system* — two-tier money, central-bank reserves, singleness, settlement liquidity: https://www.bis.org/publications/aer-2025/next-generation-monetary-financial-system
- CPMI-IOSCO, *Principles for Financial Market Infrastructures*, Principle 9 — settlement in central-bank money where practical and available: https://www.bis.org/committees/cpmi/pfmi/overview
- ECB, *Government deposits* — evidence that government deposit/cash-management arrangements vary across national central banks and treasuries: https://www.ecb.europa.eu/mopo/liq/html/treas.en.html

Institution-specific implementation details should be rechecked again when the relevant chapter is written and modeled.
