# Chapter 01 — Финансовые требования (Financial Claims)

Model stage: `M01`  
Simulation level: `SL0`

## Learning goal

После этой главы ты должен понимать двустороннюю природу финансового требования (**financial claim**): один и тот же `claim` является активом (**asset**) держателя (**holder**) и обязательством (**liability**) эмитента/должника (**issuer**).

Также нужно уметь отличать передачу требования (**transfer**) от его исполнения/погашения (**claim discharge**).

## Prerequisites

Специальные финансовые знания не требуются. Достаточно понимать базовые элементы учебного симулятора: состояние (**state**), действие (**action**), событие (**event**), изменение `before → after` и инвариант (**invariant**).

## How to study this chapter

Для каждого core scenario используй один цикл:

```text
прочитай механизм
    ↓
сделай prediction до запуска
    ↓
запусти действие
    ↓
посмотри before → after
    ↓
объясни изменение своими словами
    ↓
измени одно условие и предскажи снова
```

Не используй simulator как answer machine: сначала сформулируй собственное ожидание.

## §1.1 Стороны финансового отношения (Parties)

В простейшем финансовом отношении есть независимые стороны (**parties**).

В учебном сценарии:

- `Issuer` — сторона, которая несёт обязательство;
- `Alice` и `Bob` — возможные держатели требования.

На этом этапе `Party` — намеренно общий concept. Это ещё не банк, домохозяйство или государство.

## §1.2 Финансовое требование (Financial Claim)

Финансовое требование (**financial claim**) — это право одной стороны требовать исполнения от другой стороны на заданную величину.

В `M01` claim содержит:

```text
issuer
holder
amount
```

Например:

```text
Claim
  issuer = Issuer
  holder = Alice
  amount = 100 EUR
```

`100 EUR` здесь — величина, выраженная в валютной единице (**CurrencyAmount**). Это ещё не утверждение, что сам `Claim` является деньгами (**money**). Денежные инструменты будут введены позже.

## §1.3 Держатель и эмитент/должник (Holder and Issuer)

**Holder (держатель)** владеет требованием.

**Issuer (эмитент / должник требования)** — сторона, против которой существует требование.

Для одного claim эти роли различны:

```text
Holder  ── has claim against ──> Issuer
```

## §1.4 Актив и обязательство (Asset and Liability)

Один claim виден с двух сторон.

Если Issuer должен Alice 100 EUR:

```text
Alice
  claim asset: +100 EUR

Issuer
  claim liability: +100 EUR
```

Это не два независимых финансовых объекта. Это две стороны одного отношения.

Для `M01` действует инвариант:

```text
total claim assets == total claim liabilities
```

Это локальный инвариант модели claims. Полный balance sheet, equity и double-entry accounting появятся только в `C02`.

## §1.5 Передача требования (Transfer)

Holder может передать (**transfer**) существующее требование другому holder.

Если Alice передаёт claim Bob:

```text
Alice claim asset   100 → 0
Bob claim asset       0 → 100
Issuer liability    100 → 100
```

Меняется владелец (**holder**), но сам issuer и размер outstanding claim не меняются.

Следовательно:

```text
transfer != discharge
```

## §1.6 Исполнение/погашение требования (Claim Discharge)

Когда требование исполнено и прекращается (**claim discharge**), исчезает само финансовое отношение:

```text
Bob claim asset       100 → 0
Issuer liability      100 → 0
active claim            1 → 0
```

Важно: `C01` намеренно **не моделирует механизм**, посредством которого Issuer экономически исполнил обязательство. Мы не вводим cash, bank deposit, reserves или interbank settlement.

Поэтому generic `claim discharge` здесь не следует путать с позднейшим понятием межбанковского расчёта (**interbank settlement**).

## Knowledge classification

### Identity / invariant

```text
total claim assets == total claim liabilities
```

Это истинно по структуре `M01`: каждый active claim одновременно учитывается как asset holder и liability issuer.

### Domain rules

- issuer и holder одного claim должны быть разными parties;
- claim имеет положительную amount;
- только текущий holder может transfer claim;
- discharge требует правильного issuer и текущего holder; способ исполнения обязательства остаётся вне `M01`;
- transfer меняет holder, но не issuer и не amount;
- discharge удаляет сам active claim;
- `M01` использует одну currency denomination в одном `ClaimBook`.

### Behavioral assumptions

Нет. В `SL0` никакие autonomous agents не принимают решения.

### Empirical parameters

Нет.

### Scenario inputs

- amount claim, по умолчанию `100 EUR`;
- последовательность ручных действий learner.

## Executable model

`M01` содержит только необходимый минимум:

```text
Party
CurrencyAmount
Claim
ClaimBook

Issue Claim
Transfer Claim
Discharge Claim
```

Simulation level `SL0` означает:

- действия запускает пользователь;
- нет clock;
- нет scheduler;
- нет agents;
- нет randomness;
- каждый переход детерминирован и наблюдаем через trace.

## Scenario S01.1 — Выпуск требования (Issue Claim)

### Learning question

Почему создание одного claim одновременно создаёт asset и liability?

### Initial state

```text
no active claims
Alice claim assets = 0
Issuer claim liabilities = 0
```

### Prediction

Перед запуском ответь:

> Если Issuer создаёт claim на 100 EUR в пользу Alice, у кого появится asset, а у кого liability?

### Trigger

```text
Issue Claim 100 EUR
```

### Observable

```text
Alice claim assets      0 → 100
Issuer liabilities      0 → 100
active claims            0 → 1
```

И проверь invariant.

### Learning payoff

Asset и liability — две стороны одного financial claim.

### Variation

Reset, измени amount claim и заранее предскажи обе стороны изменения.

## Scenario S01.2 — Передача требования (Transfer Claim)

### Learning question

Что именно меняется, когда claim переходит новому holder?

### Prediction

> Исчезнет ли liability Issuer, если Alice передаст claim Bob?

### Trigger

```text
Alice → Bob
```

### Observable

```text
Alice claim assets    100 → 0
Bob claim assets        0 → 100
Issuer liabilities    100 → 100
active claims           1 → 1
```

### Learning payoff

Transfer меняет holder, но не прекращает obligation issuer.

### Variation

До запуска перечисли все values, которые должны остаться неизменными.

## Scenario S01.3 — Погашение требования (Claim Discharge)

### Learning question

Что должно исчезнуть, когда прекращается сам financial claim?

### Prediction

> Какие две стороны отношения должны одновременно исчезнуть?

### Trigger

```text
Discharge Claim
```

### Observable

```text
Bob claim assets       100 → 0
Issuer liabilities     100 → 0
active claims            1 → 0
```

### Learning payoff

Discharge прекращает сам claim, поэтому asset holder и corresponding liability issuer исчезают вместе.

### Variation

Сравни `Transfer` и `Discharge` и назови state change, который принципиально отличает их.

## Visualization

Для `C01` достаточно:

- текущего state по трём parties;
- active claim (`issuer`, `holder`, `amount`);
- invariant totals;
- event trace;
- exact `before → after` changes.

Chart, timeline over real time и network diagram пока не нужны: они не добавляют понимания к трём коротким детерминированным переходам.

## Intentional omissions

В `C01` намеренно отсутствуют:

- полноценный balance sheet;
- equity;
- accounts / ledger / double entry;
- commercial banks;
- bank deposits;
- loans;
- cash;
- central-bank reserves;
- interest and time;
- defaults;
- government;
- production and markets;
- механизм, которым claim discharge фактически выполняется.

Эти omissions нужны, чтобы learner сначала увидел саму структуру bilateral financial claim.

## Exit criteria

Не подсматривая в prepared trace, learner может объяснить:

1. Почему один claim одновременно является asset и liability?
2. Кто такие holder и issuer?
3. Что меняется и что не меняется при transfer?
4. Чем transfer отличается от claim discharge?
5. Почему `100 EUR` в `M01` ещё не означает, что мы определили money?
6. Почему полный balance sheet не нужен для learning goal этой главы?

## Next question

Теперь мы умеем рассуждать об одном или нескольких claims, но пока записываем их очень специальным способом.

Следующий вопрос:

> Как системно записывать много финансовых отношений и проверять согласованность accounting state?

Это ведёт к `C02 — Баланс и двойная запись (Balance Sheet & Double-Entry Accounting)`.
