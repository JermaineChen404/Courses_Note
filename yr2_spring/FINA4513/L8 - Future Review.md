# Futures and Forwards Reviews

## Overview
This lecture reviews the core mechanics of **forwards** and **futures contracts**, explains **marking to market**, shows why **futures and spot prices converge**, and introduces **no-arbitrage pricing** for forwards/futures with and without income or carrying costs.

---

## Part 1: Forwards vs Futures

### 1.1 Forward / Futures Contract Definition
A forward or futures contract is a **binding agreement** to buy or sell an underlying asset at a predetermined future date for a price set today.

The contract specifies:
- The underlying asset and quantity
- The expiration / delivery date
- The delivery price

### 1.2 Timeline
- At time `0`: contract is entered
- At time `T`: settlement or delivery occurs

### 1.3 Key Difference: Futures Contracts
Futures contracts are:
- **Exchange-traded**
- **Standardized**
- Guaranteed by the **clearing house**
- Settled daily through **mark-to-market**
- Supported by **margin requirements**

> [!important] Futures vs Forwards
> A **forward** is typically customized and traded OTC.  
> A **future** is standardized, exchange-traded, and settled daily.

---

## Part 2: Notation

Given an underlying asset and expiration date `T`:

- `S_0`: spot price at time 0
- `S_t`: spot price at time t
- `F_0`: futures (or forward) price at time 0
- `F_t`: futures price at time t

---

## Part 3: Opening and Closing Futures Positions

### 3.1 Offsetting Trades
Most futures contracts do **not** end in physical delivery. They are closed before maturity using an **offsetting trade**.

- A **long position** is closed by taking a **short position**
- A **short position** is closed by taking a **long position**

### 3.2 Profit / Loss from Closing a Position
The total gain or loss is determined by the difference between the opening futures price and the closing futures price.

For a position opened at `F_0` and closed at `F_t`:

- **Long futures payoff**: `-F_0 + F_t = F_t - F_0`
- **Short futures payoff**: `F_0 - F_t`

> [!tip] Sign Convention
> Long benefits when futures price rises.  
> Short benefits when futures price falls.

---

## Part 4: Marking to Market (MTM)

### 4.1 Core Idea
Unlike forwards, futures are settled **daily**.

At the end of each trading day:
- Gains are added to the margin account
- Losses are deducted from the margin account

This process is called **marking to market**.

### 4.2 Example
Suppose:
- Initial futures price: `F_0 = 850`
- Spot price today: `S_0 = 840`

Then futures prices evolve as:
- `F_1 = 880`
- `F_2 = 860`
- `F_3 = 855`

Daily cash flow for the **buyer (long)**:
- Period 1: `+30`
- Period 2: `-20`
- Period 3: `-5`

Daily cash flow for the **seller (short)**:
- Period 1: `-30`
- Period 2: `+20`
- Period 3: `+5`

### 4.3 Net Result
- Buyer net cash flow: `+5`
- Seller net cash flow: `-5`

This matches the total change from initial to final futures price:

$$
F_3 - F_0 = 855 - 850 = 5
$$

> [!note] Key Insight
> Marking to market breaks the total profit/loss into **daily realized cash flows**, but the cumulative payoff still reflects the total price change over the life of the contract.

---

## Part 5: Review Question

### 5.1 Short Position in March S&P 500 Future
Question:
You enter a **short position** in a March futures contract in January. By February, what is your gain/loss so far?

For a short position:
$$
\text{Gain} = F_{\text{Jan}} - F_{\text{Feb}}
$$

> [!check] Correct Answer
> The gain/loss is:
> $$
> F_{\text{Jan}} - F_{\text{Feb}}
> $$

Because a short profits if the futures price falls after entering the contract.

---

## Part 6: Convergence of Futures and Spot Prices

### 6.1 Main Idea
As delivery approaches, the **futures price converges to the spot price**.

At maturity:
$$
F_T = S_T
$$

### 6.2 Why Must They Converge?
If futures price is higher than spot near delivery:
- Short the futures
- Buy the asset in the spot market
- Deliver the asset into the futures contract
- Lock in profit:
$$
F_T - S_T
$$

If spot price is higher than futures near delivery:
- Go long the futures
- Sell the asset in the spot market
- Use futures delivery to cover
- Lock in arbitrage profit

> [!danger] Arbitrage Logic
> If `F_T \ne S_T` at delivery, traders can construct a riskless profit.  
> Therefore competition forces:
> $$
> F_T = S_T
> $$

---

## Part 7: Why Do People Trade?

The lecture raises three motivations:
- **Risk**
- **Information**
- Whether markets are a **zero-sum game**

### 7.1 Main Market Participants

#### Hedgers
Use derivatives to reduce exposure from another position.

#### Speculators
Take “naked” positions and bet on the future direction of prices.

#### Arbitrageurs
Exploit price discrepancies by entering offsetting transactions to earn low-risk or riskless profit.

> [!important] Roles in the Market
> - **Hedgers** transfer risk
> - **Speculators** absorb risk in exchange for expected profit
> - **Arbitrageurs** enforce pricing efficiency

---

## Part 8: Hedging vs Speculation Example

### 8.1 Hedging
Example:
- You will need gold in one year
- You fear gold prices may rise
- You go **long a forward contract**

Purpose:
- Reduce future price uncertainty
- Lock in acquisition cost

### 8.2 Speculation
Example:
- You do **not** need gold in one year
- You think the forward price is too low
- You go **long the forward contract**
- At maturity, receive gold and sell it in the spot market

Purpose:
- Create exposure to price movements
- Earn profit from a forecast

> [!tip] Distinction
> Hedging reduces existing risk.  
> Speculation creates new risk exposure.

---

## Part 9: No-Arbitrage Pricing

### 9.1 Synthetic Forward Logic
A long forward can be replicated by:
- Buying the underlying asset today
- Borrowing funds to finance the purchase

This is a **synthetic forward**.

### 9.2 Basic Pricing Formula
For an investment asset with:
- No income
- No storage cost

the fair forward price is:

$$
F_0 = S_0 e^{rT}
$$

where:
- `S_0` = current spot price
- `r` = continuously compounded risk-free rate
- `T` = time to maturity

> [!note] Intuition
> Buying now and carrying the asset to time `T` should cost the same as entering a forward today, otherwise arbitrage exists.

---

## Part 10: Effect of Income / Dividends

### 10.1 If the Underlying Pays Income
If the asset provides benefits to the holder, such as dividends, then owning the asset today is more attractive.

This lowers the fair forward/futures price.

### 10.2 General Pricing Relation
Given benefits and costs:

$$
S_0 - PV(\text{benefit}) + PV(\text{cost}) = F_0 e^{-rT}
$$

Equivalently:

$$
F_0 = \bigl(S_0 - PV(\text{benefit}) + PV(\text{cost})\bigr)e^{rT}
$$

### 10.3 Yield / Cost Form
If the asset has:
- continuous income yield `q`, or
- storage/carry cost `u`

then:

$$
F_0 = S_0 e^{(r - q + u)T}
$$

> [!check] Direction of Effect
> - Higher **income yield** `q` → **lower** forward price
> - Higher **carrying cost** `u` → **higher** forward price

---

## Part 11: Law of One Price

### 11.1 Statement
The **Law of One Price** says that two equivalent assets must have the same price.

### 11.2 Meaning of "Equivalent"
Equivalent means:
- They deliver **identical payoffs in every state of the world**

### 11.3 Importance
This principle underpins derivative pricing:
- Replicate derivative payoffs using other assets
- Compare costs
- Eliminate arbitrage opportunities

> [!important] Core Principle
> Pricing is relative.  
> If two portfolios have the same payoff, they must have the same price.

---

## Part 12: Arbitrage Strategies

### 12.1 Cash and Carry
Used when forward price is **too high**.

Strategy:
- Borrow money
- Buy the asset in spot market
- Short the forward
- Deliver at maturity and repay borrowing

### 12.2 Reverse Cash and Carry
Used when forward price is **too low**.

Strategy:
- Short sell the asset
- Invest proceeds
- Go long the forward
- Take delivery later to close short position

> [!danger] When Arbitrage Appears
> - If `F_0` is above fair value → use **cash and carry**
> - If `F_0` is below fair value → use **reverse cash and carry**

---

## Summary

| Concept | Key Idea |
|--------|----------|
| Forward/Futures | Agreement today for future trade |
| Futures | Standardized, exchange-traded, marked to market |
| Long payoff | `F_t - F_0` |
| Short payoff | `F_0 - F_t` |
| MTM | Daily settlement through margin account |
| Convergence | `F_T = S_T` at maturity |
| No-arbitrage pricing | Fair forward price comes from replication |
| With no income/cost | `F_0 = S_0 e^{rT}` |
| With income/cost | `F_0 = S_0 e^{(r-q+u)T}` |
| Law of One Price | Same payoff ⇒ same price |

---

## Concept Checklist

- [ ] Define a forward and a futures contract
- [ ] Explain how futures differ from forwards
- [ ] Use notation `S_0`, `S_t`, `F_0`, `F_t`
- [ ] Compute long and short futures payoff
- [ ] Explain marking to market
- [ ] Work through daily MTM cash flows
- [ ] Explain why futures and spot prices converge
- [ ] Distinguish hedging, speculation, and arbitrage
- [ ] Apply no-arbitrage pricing formula
- [ ] Explain how dividends/income affect futures prices
- [ ] State the Law of One Price
- [ ] Identify when to use cash and carry vs reverse cash and carry

---

## Key Formulas

| Concept | Formula |
|--------|---------|
| Long futures payoff | `F_t - F_0` |
| Short futures payoff | `F_0 - F_t` |
| Final convergence | `F_T = S_T` |
| Basic forward pricing | `F_0 = S_0 e^{rT}` |
| General pricing with benefits/costs | `S_0 - PV(\text{benefit}) + PV(\text{cost}) = F_0 e^{-rT}` |
| Yield/cost form | `F_0 = S_0 e^{(r-q+u)T}` |

---

## Quick Exam Traps

> [!warning] Common Trap
> For a **short futures** position, profit is:
> $$
> F_0 - F_t
> $$
> not `F_t - F_0`.

> [!warning] Common Trap
> Futures are **marked to market daily**, while forwards usually settle only at maturity.

> [!warning] Common Trap
> If the underlying pays dividends or other benefits, the fair futures/forward price generally **decreases**, not increases.

---
