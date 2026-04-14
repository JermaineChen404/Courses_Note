# Hedging with Futures and Forwards

## Overview
This lecture explains how **forwards and futures can be used to hedge price risk**, from both the **producer’s** and **buyer’s** perspective. It distinguishes **short hedges** and **long hedges**, applies the ideas to **foreign exchange**, and then shows why real-world hedging is often **imperfect** because of **basis risk** and mismatches in asset or maturity.

---

## Part 1: Producer's Hedging

### 1.1 Economic Exposure of a Producer
A producer that plans to **sell a commodity in the future** has an inherent **long position** in that commodity.

- If the commodity price rises, the producer benefits
- If the commodity price falls, the producer is harmed

From the producer's perspective, hedging means reducing downside exposure to falling prices. This is done with a **short forward/futures hedge**.

### 1.2 Gold-Mining Example
Example from the lecture:
- A gold-mining firm has production cost of **$500/oz**
- The cost is paid at year-end
- The firm enters a **short forward** to sell gold for **$850/oz in 1 year**

Without hedging:
$$
\pi_{\text{unhedged}} = S_1 - 500
$$

Profit rises with the future gold price `S_1`.

With a short forward at 850:
$$
\pi_{\text{forward}} = 850 - S_1
$$

Total hedged profit:
$$
\pi_{\text{hedged}} = (S_1 - 500) + (850 - S_1) = 350
$$

> [!important] Producer Hedge Logic
> A producer is naturally **long** the commodity and hedges by going **short forward/futures**, locking in a selling price. :contentReference[oaicite:4]{index=4}

### 1.3 Main Takeaway
The short hedge transforms uncertain profit into a **fixed profit**.

In the gold example:
- Unhedged profit varies with `S_1`
- Short forward payoff falls as `S_1` rises
- Combined payoff is a flat **$350 per ounce**

---

## Part 2: Buyer's Hedging

### 2.1 Economic Exposure of a Buyer
A firm that will **purchase a commodity in the future** as an input has an inherent **short position** in that commodity.

- If the input price rises, profit falls
- If the input price falls, profit rises

To hedge this risk, the firm enters a **long forward/futures contract**.

### 2.2 Input Hedging Example
Lecture example:
- A firm needs **1 unit of gold** as an input for each unit of output
- It enters a **long forward** at **$850/oz**
- Additional production costs are **$340/unit**
- Selling price of final output is locked at **$1300**
- Horizon is 1 year

Without hedging:
$$
\pi_{\text{unhedged}} = 1300 - 340 - S_1 = 960 - S_1
$$

With long forward:
$$
\pi_{\text{forward}} = S_1 - 850
$$

Total hedged profit:
$$
\pi_{\text{hedged}} = (960 - S_1) + (S_1 - 850) = 110
$$

> [!tip] Buyer Hedge Logic
> A buyer is naturally **short** the input commodity and hedges by going **long forward/futures**, locking in a purchase price. 

---

## Part 3: Long vs Short Hedges

### 3.1 Short Hedge
A **short hedge** is appropriate when you know you will **sell** an asset in the future and want to lock in the price.

Typical cases:
- You already own the asset
- You will produce and sell the asset later
- You expect to receive the asset or an income stream tied to it

### 3.2 Long Hedge
A **long hedge** is appropriate when you know you will **buy** an asset in the future and want to lock in the purchase price.

Typical cases:
- You need the asset as an input
- You plan to acquire the asset in the future

> [!check] Summary Rule
> - **Sell later** → use a **short hedge**
> - **Buy later** → use a **long hedge** :contentReference[oaicite:7]{index=7}

---

## Part 4: Foreign Currency Application

### 4.1 Importer vs Exporter
The lecture applies hedging logic to foreign exchange risk:

- **ImportCo** must **pay 10 million GBP** in 1 month
- **ExportCo** will **receive 30 million GBP** in 6 months

Assume the exchange quote is **USD per GBP**. 

### 4.2 Hedging Strategy
#### Importer
ImportCo needs to **buy GBP in the future**, so it faces risk if GBP appreciates.

Appropriate hedge:
- **Long GBP forward**

This locks in the future USD cost per GBP.

#### Exporter
ExportCo will **receive GBP in the future**, so it faces risk if GBP depreciates.

Appropriate hedge:
- **Short GBP forward**

This locks in the future USD value of its GBP receipts.

> [!important] FX Mapping
> Receiving foreign currency later is like being **long** that currency.  
> Paying foreign currency later is like being **short** that currency. :contentReference[oaicite:9]{index=9}

---

## Part 5: Bid-Ask Spread in FX Forwards

### 5.1 Dealer Quotes
The lecture provides spot and forward dealer quotes for **USD/GBP** and reminds:

- The dealer **buys GBP at the bid**
- The dealer **sells GBP at the ask**
- Therefore: **buy at ask, sell at bid**

### 5.2 Sample Quotes

![[image.png]]

### 5.3 Hedge Pricing Rule
- If you need to **buy GBP forward**, you transact at the **ask**
- If you need to **sell GBP forward**, you transact at the **bid**

So:
- Importer hedging future GBP payment uses the **ask**
- Exporter hedging future GBP receipt uses the **bid**

> [!warning] Common Mistake
> Do not use the midpoint quote mechanically. The correct hedge rate depends on whether you are effectively **buying** or **selling** the foreign currency.

---

## Part 6: Perfect Hedging Assumptions

### 6.1 Conditions for a Perfect Hedge
So far, the lecture assumes:
- The asset being hedged is exactly the **same** as the asset underlying the futures
- The futures expiration date exactly matches the actual buying/selling date of the asset

Under these assumptions, the hedge is “perfect.”

### 6.2 Effective Price of a Short Hedge
For a short hedge closed at time `t`, the effective price received is:
$$
S_t + (F_0 - F_t)
$$

This is:
- spot sale proceeds `S_t`
- plus gain/loss on the short futures position

If the hedge is perfect and carried to maturity, i.e. $S_{T}=F_{T}$, this effectively locks in the original futures price $F_{0}$ 

---

## Part 7: Date Mismatch

### 7.1 Example
Lecture example:
- It is **March 1**
- A U.S. company expects to receive **10 million GBP at the end of July**
- September GBP futures price is currently **1.6 USD/GBP**
- One contract size is **10 million GBP**

Question:
- Should the company go long or short September futures?
- When should it close the position?

### 7.2 Correct Hedging Logic
Because the company will **receive GBP**, it is exposed to a fall in GBP value.

Therefore:
- It should take a **short futures** position
- It should close the futures position when the exposure ends, i.e. **at the end of July**

### 7.3 Effective Exchange Rate
For a short hedge closed in July:
$$
\text{Effective rate} = S_{\text{July}} + F_{\text{March}} - F_{\text{July}}
$$

Using the lecture numbers:
- `F_March = 1.6`
- `F_July = 1.4`
- `S_July = 1.65`

So:
$$
1.65 + 1.6 - 1.4 = 1.85
$$

> [!note] Why Not Use the September Spot?
> The firm closes the hedge when the underlying cash flow occurs in **July**, not at the contract delivery month in September. :contentReference[oaicite:16]{index=16}

---

## Part 8: Convergence of Futures and Spot

As a futures contract approaches expiration, the futures price converges to the spot price:

$$
F_T = S_T
$$

The lecture recalls this convergence visually to explain why date mismatches matter:
- If you hedge with a contract expiring after your exposure date, then at your hedge closing date `t`, it is generally **not** true that `F_t = S_t`
- This creates residual risk

---

## Part 9: Cross-Hedging

### 9.1 Hedging One Asset with Another
Sometimes no futures contract exists for the exact asset you want to hedge.

Lecture example:
- **Jet fuel futures do not exist in the U.S.**
- Airlines hedge jet fuel using **crude oil** or **heating oil** futures

This is called **cross-hedging**.

### 9.2 Notation
- `S_t`: spot price of jet fuel at time `t`
- `F_t^*`: futures/forward price of crude oil at time `t`
- `S_t^*`: spot price of crude oil at time `t`

Here:
- Jet fuel is the asset being hedged
- Crude oil is the asset underlying the futures contract

> [!important] Cross-Hedge Tradeoff
> Cross-hedging reduces risk, but usually cannot eliminate it completely because the two prices do not move perfectly together.

---

## Part 10: Basis Risk

### 10.1 Definition
If a company uses a short hedge and closes it at time `t`, it gets:
$$
(S_t - F_t^*) + F_0^*
$$

The lecture decomposes this as:
$$
(S_t - S_t^*) + (S_t^* - F_t^*) + F_0^*
$$

The uncertain part is called **basis risk**.

### 10.2 Two Sources of Basis Risk
#### 1. Asset mismatch
$$
S_t - S_t^*
$$
This captures the mismatch between:
- the asset being hedged
- the asset underlying the futures contract

This matters in cross-hedging.

#### 2. Date mismatch
$$
S_t^* - F_t^*
$$
This captures the mismatch between:
- the futures expiration date
- the actual hedge ending date

This matters when the hedge is closed before futures maturity.

> [!danger] Basis Risk
> A hedge is imperfect whenever the spot price exposure and the futures contract do not line up exactly in **asset** and **timing**.

---

## Part 11: Minimizing Basis Risk

### 11.1 Asset Choice
To reduce the first component of basis risk:
- Choose a futures contract on an asset whose price is **highly correlated** with the asset being hedged

### 11.2 Delivery Month Choice
To reduce the second component:
- Choose a delivery month **as close as possible** to the expiration of the hedge

These choices do not eliminate basis risk, but they reduce it. :contentReference[oaicite:22]{index=22}

---

## Part 12: Southwest Airlines Example

### 12.1 Strategic Alternatives
The lecture ends with a discussion of hedging strategies for Southwest:

1. Do nothing
2. Hedge using options
3. Hedge using a **zero-cost collar**
4. Hedge using **crude oil or heating oil futures** :contentReference[oaicite:23]{index=23}

### 12.2 Zero-Cost Collar
Example setup:
- Southwest must purchase **1000 million gallons of jet fuel**
- Estimated ticket revenue is **3000 million**
- Strategy: **buy 80-cent call and sell 60-cent put**

A collar creates:
- protection against large price increases
- reduced or zero upfront premium
- but limited upside from falling prices

> [!tip] Collar Intuition
> A collar places the effective purchase price into a band:
> - above the call strike, losses are capped
> - below the put strike, gains are given back

### 12.3 Open Questions
The lecture closes with reflective questions:
- How many crude oil futures contracts should the airline use?
- What risks remain after hedging?

This points toward **hedge ratio design** and residual **basis risk**.

---

## Summary: Long and Short Hedges

| Situation | Natural Exposure | Hedge Type |
|----------|------------------|------------|
| Producer will sell asset later | Long | Short hedge |
| Buyer will purchase asset later | Short | Long hedge |
| Exporter will receive foreign currency | Long foreign currency | Short hedge |
| Importer must pay foreign currency | Short foreign currency | Long hedge |

---

## Concept Checklist

- [ ] Explain why a producer has an inherent long position
- [ ] Explain why a buyer has an inherent short position
- [ ] Identify when to use a short hedge
- [ ] Identify when to use a long hedge
- [ ] Apply hedging logic to importers and exporters
- [ ] Use bid and ask quotes correctly in FX hedging
- [ ] Compute effective price under a short hedge
- [ ] Explain why date mismatch creates hedge imperfection
- [ ] Define cross-hedging
- [ ] Decompose basis risk into asset mismatch and date mismatch
- [ ] Explain how to minimize basis risk
- [ ] Interpret zero-cost collar intuition

---

## Key Formulas Summary

| Concept | Formula |
|---------|---------|
| Producer unhedged profit | $\pi = S_1 - 500$ |
| Producer short forward payoff | $850 - S_1$ |
| Producer hedged profit | $(S_1 - 500) + (850 - S_1) = 350$ |
| Buyer unhedged profit | $\pi = 1300 - 340 - S_1$ |
| Buyer long forward payoff | $S_1 - 850$ |
| Buyer hedged profit | $(1300 - 340 - S_1) + (S_1 - 850)$ |
| Effective price of short hedge at time $t$ | $S_t + (F_0 - F_t)$ |
| Short hedge with cross-hedge decomposition | $(S_t - F_t^*) + F_0^* = (S_t - S_t^*) + (S_t^* - F_t^*) + F_0^*$ |
| Futures convergence at maturity | $F_T = S_T$ |

---

## Quick Exam Traps

> [!warning] Common Trap
> A **producer** usually hedges with a **short** futures/forward position, not a long one.

> [!warning] Common Trap
> A firm that will **buy** an input later should use a **long hedge**, because rising input prices hurt it.

> [!warning] Common Trap
> In FX quotes, the correct hedge rate depends on whether you are **buying** or **selling** the foreign currency:
> **buy at ask, sell at bid**.

> [!warning] Common Trap
> A hedge can still be imperfect even if you choose the correct long/short direction. Asset mismatch and timing mismatch create **basis risk**.

---