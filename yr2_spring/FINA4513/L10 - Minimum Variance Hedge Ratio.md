# Minimum Variance Hedge Ratio

## Overview
This lecture explains how to choose the **optimal number of futures contracts** to minimize hedging risk. It formalizes the **minimum variance hedge ratio**, shows its link to **covariance, correlation, and regression**, and applies the idea to both:

- **commodity cross-hedging** (e.g. jet fuel with crude oil futures)
- **equity portfolio hedging** with stock index futures

The lecture also explains how to measure **hedge effectiveness** and how to target a desired **portfolio beta**. :contentReference[oaicite:1]{index=1}

---

## Part 1: The Hedging Question

### 1.1 Direction Is Not Enough
When hedging, there are really two separate questions:

- What direction should the hedge take?
- **How many futures contracts** should be used?

The lecture emphasizes that even if we know whether to go long or short, we still need to determine the **size** of the hedge. :contentReference[oaicite:2]{index=2}

### 1.2 Short Hedge Payoff Reminder
For a short hedge, the effective value at time `t` is:

$$
S_t + F_0 - F_t
$$

or equivalently,

$$
S_0 + \Delta S - \Delta F
$$

This makes clear that hedging performance depends on how the change in the spot price, `\Delta S`, relates to the change in the futures price, `\Delta F`. 

> [!important] Key Idea
> The right hedge size depends on the statistical relationship between **spot-price changes** and **futures-price changes**.

---

## Part 2: Why Hedge Ratios Matter

### 2.1 If Futures Move More Than Spot
The lecture asks:

> Suppose `dF = 2 dS`; how many futures contracts should you enter if you have one exposure in `S`?

If futures change **twice as much** as spot, then a **1-for-1 hedge is too large**. You would only need about **half as many futures contracts** per unit of spot exposure.

### 2.2 If Correlation Is Zero
The lecture also asks what hedge ratio should be used if correlation is zero.

Answer:
- the optimal hedge ratio is **0**

Reason:
- if futures changes and spot changes are unrelated, the futures contract does not reduce the variance of the spot exposure.

> [!warning] Common Intuition Trap
> A futures contract is **not automatically** a good hedge.  
> If correlation is very low or zero, adding futures may not reduce risk at all.

---

## Part 3: Formal Setup

### 3.1 Hedged Revenue
The lecture writes the hedged position as:

$$
H = Q_A S_t - Q_F^*(F_t - F_0)
$$

or equivalently:

$$
H = Q_A \bigl(S_t - h(F_t - F_0)\bigr)
$$

where:

- `Q_F` = size of futures position
- `Q_A` = size of the asset exposure being hedged
- `h = Q_F / Q_A` = hedge ratio
- `Q_A S_t` = unhedged revenue
- `-Q_F(F_t - F_0)` = payoff from the short futures hedge :contentReference[oaicite:6]{index=6}

### 3.2 Objective
Choose `h` to minimize:

$$
\text{Var}(H)
$$

That is, the goal is **not** to maximize expected return, but to **minimize uncertainty** of the combined position. :contentReference[oaicite:7]{index=7}

---

## Part 4: Deriving the Minimum Variance Hedge Ratio

### 4.1 Variance of the Hedged Position
Using changes in spot and futures prices, the lecture shows:

$$
\text{Var}(H)=Q_A^2 \text{Var}(S_0+\Delta S-h\Delta F)
$$

which simplifies to:

$$
Q_A^2 \left[\text{Var}(\Delta S)+h^2\text{Var}(\Delta F)-2h\,\text{Cov}(\Delta S,\Delta F)\right]
$$

### 4.2 First-Order Condition
Differentiating with respect to `h` and setting equal to zero gives:

$$
2h\,\text{Var}(\Delta F)-2\text{Cov}(\Delta S,\Delta F)=0
$$

So the **minimum variance hedge ratio** is:

$$
h^*=\frac{\text{Cov}(\Delta S,\Delta F)}{\text{Var}(\Delta F)}
$$

This is the core result of the lecture. :contentReference[oaicite:8]{index=8}

> [!check] Minimum Variance Hedge Ratio
> $$
> h^*=\frac{\text{Cov}(\Delta S,\Delta F)}{\text{Var}(\Delta F)}
> $$
> This is the proportion of the exposure that should be hedged to minimize variance.

---

## Part 5: Correlation Form

### 5.1 Equivalent Formula
Using covariance and correlation relationships:

$$
\text{Cov}(\Delta S,\Delta F)=\rho \sigma_S \sigma_F
$$

we can rewrite the hedge ratio as:

$$
h^*=\frac{\rho \sigma_S \sigma_F}{\sigma_F^2}
=\rho \frac{\sigma_S}{\sigma_F}
$$

where:

- `\sigma_S` = standard deviation of `\Delta S`
- `\sigma_F` = standard deviation of `\Delta F`
- `\rho` = correlation between `\Delta S` and `\Delta F` :contentReference[oaicite:9]{index=9}

### 5.2 Interpretation
The hedge ratio is larger when:
- spot and futures are **more strongly correlated**
- spot prices are **more volatile**
- futures prices are **less volatile**

The hedge ratio is smaller when:
- correlation is weak
- futures are very volatile relative to spot

> [!tip] Intuition
> A hedge should be larger when futures are a **reliable, closely related** offset to spot risk.

---

## Part 6: Regression Interpretation

### 6.1 Hedge Ratio as a Slope
The lecture gives a graphical interpretation:

If we regress spot-price changes on futures-price changes,

$$
\Delta S = \alpha + \beta \Delta F + \epsilon
$$

then the optimal hedge ratio is the slope coefficient:

$$
h^*=\beta=\frac{\text{Cov}(\Delta S,\Delta F)}{\text{Var}(\Delta F)}
$$

So the hedge ratio is literally the **best-fit line slope** relating `\Delta S` to `\Delta F`. :contentReference[oaicite:10]{index=10}

### 6.2 Why This Matters
This means:
- the hedge ratio can be estimated empirically with regression
- historical data on spot and futures changes can be used directly
- the estimated beta tells you how much the spot exposure tends to move for a unit movement in futures

> [!important] Statistical Interpretation
> The minimum variance hedge ratio is the **regression beta** of spot changes on futures changes.

---

## Part 7: Special Cases

### 7.1 Perfect 1-for-1 Hedge
If:

$$
\Delta F \approx \Delta S
$$

then:

$$
Q_F = Q_A
$$

and the hedge ratio is about:

$$
h^* = 1
$$

### 7.2 Futures Move Twice as Much
If:

$$
\Delta F \approx 2\Delta S
$$

then you only need about:

$$
h^* \approx \frac{1}{2}
$$

### 7.3 Futures Move Half as Much
If:

$$
\Delta F \approx \frac{1}{2}\Delta S
$$

then you need about:

$$
h^* \approx 2
$$

These examples show that the number of contracts depends on the **relative sensitivity** of futures to the underlying exposure. :contentReference[oaicite:11]{index=11}

---

## Part 8: Hedge Effectiveness and \(R^2\)

### 8.1 Correlation and Hedge Quality
The lecture emphasizes that hedging effectiveness depends on the **coefficient of correlation**.

- If correlation is high, the hedge works well
- If correlation is low, the hedge is weak
- If correlation is zero, do not hedge with that futures contract

### 8.2 \(R^2\) Interpretation
The lecture states that:

$$
R^2 = \rho^2
$$

in the simple regression setting.

This has two interpretations:
- a statistical measure of how well the regression line fits the data
- the **proportion of variance eliminated by hedging** :contentReference[oaicite:12]{index=12}

Example:
If

$$
\rho = 0.9
$$

then

$$
R^2 = 0.81
$$

meaning about **81% of variance** is explained / hedged away. :contentReference[oaicite:13]{index=13}

> [!note] Hedge Effectiveness
> A high hedge ratio alone does **not** mean a hedge is effective.  
> Effectiveness depends on how well futures and spot actually move together.

---

## Part 9: Airline Cross-Hedging Example

### 9.1 Setup
The lecture considers an airline that expects to purchase:

- **2 million gallons of jet fuel in one month**

It uses **crude oil futures** for hedging. This is a **cross-hedge** because the asset being hedged and the futures underlying are not identical. :contentReference[oaicite:14]{index=14}

### 9.2 Given Data
From the slide:

- `\sigma_F = 0.0313`
- `\sigma_S = 0.0263`
- `\rho = 0.928`

The optimal hedge ratio is computed as:

$$
h^* = 0.928 \times \frac{0.0263}{0.0313} = 0.778
$$

The hedge effectiveness is:

$$
\rho^2 = (0.928)^2 = 0.862
$$

So roughly **86.2%** of variance is eliminated. :contentReference[oaicite:15]{index=15}

### 9.3 Number of Contracts
Each crude oil futures contract covers:

- **42,000 gallons**

Using:

$$
h=\frac{Q_F}{Q_A}
$$

the lecture computes:

$$
0.0778 = \frac{N \times 42{,}000}{2{,}000{,}000}
$$

giving:

$$
N \approx 37.03
$$

So the airline should use about **37 contracts**. :contentReference[oaicite:16]{index=16}

> [!warning] Small Notation Caution
> The slide’s contract-count step appears to use a decimal presentation that can look confusing, but the final result shown is about **37 contracts**, based on the hedge ratio and contract size.

### 9.4 Why This Works
The next slide answers the question directly:

- **High correlation**

The strategy works because jet fuel and crude oil prices move closely together, even though they are not the same asset. :contentReference[oaicite:17]{index=17}

---

## Part 10: Hedging an Equity Portfolio

### 10.1 Same Logic, New Setting
The lecture then moves from firms hedging commodities to investors hedging an equity portfolio with **stock index futures**.

Mapping:
- asset to be hedged = your equity portfolio
- futures underlying = stock index, e.g. **S&P 500** :contentReference[oaicite:18]{index=18}

### 10.2 Why Use Stock Index Futures?
Advantages over directly buying or selling all the stocks include:

- lower transaction costs
- better for timing or allocation strategies
- faster to implement
- cash settlement rather than physical delivery of all component stocks :contentReference[oaicite:19]{index=19}

---

## Part 11: Hedge Ratio for Equity Portfolios

### 11.1 Connection to CAPM Beta
For stock index futures, the optimal hedge ratio is linked to portfolio beta.

The lecture writes:

$$
E[R_A] - R_f = \beta \bigl(E[R_m] - R_f\bigr)
$$

and explains that the optimal hedge ratio is the slope when **excess portfolio return** is regressed on **excess market return**. That slope is the portfolio’s **beta**. :contentReference[oaicite:20]{index=20}

### 11.2 Contract Formula
The number of index futures contracts needed to hedge market risk is:

$$
N^* = \beta \frac{V_A}{V_F}
$$

where:
- `V_A` = value of the asset / portfolio
- `V_F` = value of one futures contract :contentReference[oaicite:21]{index=21}

For a full hedge of market risk, this is typically a **short futures** position.

> [!important] Equity Hedge Rule
> To hedge away systematic market risk:
> $$
> N^* = \beta \frac{V_A}{V_F}
> $$

---

## Part 12: S&P 500 Portfolio Example

### 12.1 Given
The lecture’s example assumes:

- futures price of S&P 500 = **1,000**
- portfolio size = **$5 million**
- portfolio beta = **1.5**
- one contract = **$250 times the index** :contentReference[oaicite:22]{index=22}

### 12.2 Value of One Futures Contract
So:

$$
V_F = 250 \times 1000 = 250{,}000
$$

### 12.3 Number of Contracts
Then:

$$
N = 1.5 \times \frac{5{,}000{,}000}{250{,}000}
= 1.5 \times 20
= 30
$$

So the investor should take a **short position in 30 futures contracts** to hedge market risk. :contentReference[oaicite:23]{index=23}

### 12.4 Beta After Hedging
The lecture asks what the beta is **after** hedging with S&P 500 futures.

Answer:
- approximately **0**

The systematic market exposure is removed, though not all total risk necessarily disappears. :contentReference[oaicite:24]{index=24}

---

## Part 13: Is Any Risk Left?

### 13.1 Yes
The lecture asks:
- how effective is the hedge?
- what does \(R^2\) mean in CAPM language?

Answer:
- a market hedge removes **systematic risk**
- **non-systematic risk** may remain :contentReference[oaicite:25]{index=25}

### 13.2 Diversified Portfolio vs Single Stock
For a **diversified portfolio**, CAPM is a better predictor of actual returns, so hedging with stock index futures can be very effective.

For a **single stock**, CAPM is described as:
- an unbiased predictor
- but **not a particularly good** predictor of actual return

So a futures hedge removes market-related risk, but firm-specific risk remains. :contentReference[oaicite:26]{index=26}

> [!danger] Important Distinction
> Hedging a single stock with index futures does **not** make it risk-free.  
> It mainly removes the **market component** of risk.

---

## Part 14: Reasons for Hedging an Equity Portfolio

The lecture gives two main motivations:

### 14.1 Temporary Exit from the Market
An investor may want to be out of the market for a short time.

Using futures can be cheaper than:
- selling the portfolio
- then buying it back later

### 14.2 Hedge Systematic Risk Only
An investor may believe the chosen stocks will outperform the market.

Then hedging market risk isolates:
- performance of the portfolio **relative to the market**

This is especially relevant for alpha-seeking managers. :contentReference[oaicite:27]{index=27}

---

## Part 15: Positive Alpha Interpretation

### 15.1 CAPM with Alpha
The lecture writes:

$$
E[R_A]-R_f=\beta(E[R_m]-R_f)+\alpha
$$

If a manager generates positive alpha, then hedging market risk with S&P 500 futures leaves a payoff tied to alpha. :contentReference[oaicite:28]{index=28}

### 15.2 Hedged Return
Using:

$$
N^*=\beta \frac{V_A}{V_F}
$$

the lecture shows that the market component cancels, leaving approximately:

$$
V_A \alpha
$$

So the manager can hedge market exposure and still retain abnormal performance if alpha is truly positive. :contentReference[oaicite:29]{index=29}

> [!tip] Alpha Hedge Intuition
> Hedge with index futures to strip out **beta**, leaving the portfolio’s **alpha** as the main driver of performance.

---

## Part 16: Targeting Any Beta

### 16.1 General Formula
The lecture generalizes from “hedge to beta zero” to “target any beta.”

It gives:

$$
\beta^* = \beta - h \times 1
$$

so:

$$
\frac{N V_F}{V_A} = \beta - \beta^*
$$

This means the futures position can be chosen to move the portfolio from current beta `\beta` to desired beta `\beta^*`. :contentReference[oaicite:30]{index=30}

### 16.2 Example: Reduce Beta from 1.5 to 0.75
Using the earlier portfolio:

$$
N = (1.5-0.75)\frac{5{,}000{,}000}{250 \times 1000}
= 0.75 \times 20
= 15
$$

So the investor should **short 15 contracts**. :contentReference[oaicite:31]{index=31}

### 16.3 Example: Increase Beta to 2.0
To increase beta from 1.5 to 2.0:

$$
N = (1.5-2.0)\frac{5{,}000{,}000}{250 \times 1000}
= -0.5 \times 20
= -10
$$

A negative number means take the opposite side:
- **long 10 futures contracts** :contentReference[oaicite:32]{index=32}

> [!check] Target Beta Rule
> - Reduce beta → **short** index futures
> - Increase beta → **long** index futures

---

## Summary

| Concept | Key Result |
|--------|------------|
| Minimum variance hedge ratio | $h^*=\dfrac{\text{Cov}(\Delta S,\Delta F)}{\text{Var}(\Delta F)}$ |
| Correlation form | $h^*=\rho \dfrac{\sigma_S}{\sigma_F}$ |
| Regression interpretation | $h^*$ is the slope in regressing $\Delta S$ on $\Delta F$ |
| Hedge effectiveness | $R^2=\rho^2$ |
| Commodity cross-hedge | Use correlation + relative volatilities |
| Equity hedge contracts | $N^*=\beta \dfrac{V_A}{V_F}$ |
| Full market hedge | target beta = 0 |
| Target-beta adjustment | $\dfrac{N V_F}{V_A}=\beta-\beta^*$ |

---

## Concept Checklist

- [ ] Explain why choosing hedge direction is not enough
- [ ] Derive the minimum variance hedge ratio
- [ ] Rewrite hedge ratio using correlation and standard deviations
- [ ] Interpret the hedge ratio as a regression slope
- [ ] Explain why zero correlation implies no hedge
- [ ] Interpret \(R^2\) as hedge effectiveness
- [ ] Compute optimal contracts in a cross-hedge example
- [ ] Explain why crude oil futures can hedge jet fuel risk
- [ ] Use stock index futures to hedge a portfolio
- [ ] Compute contracts needed to hedge portfolio beta
- [ ] Distinguish systematic vs non-systematic risk after hedging
- [ ] Adjust futures position to target any desired beta

---

## Key Formulas Summary

| Concept | Formula |
|---------|---------|
| Short hedge value at time $t$ | $S_t + F_0 - F_t$ |
| Hedged revenue | $H = Q_A S_t - Q_F(F_t-F_0)$ |
| Hedge ratio | $h = \dfrac{Q_F}{Q_A}$ |
| Minimum variance hedge ratio | $h^*=\dfrac{\text{Cov}(\Delta S,\Delta F)}{\text{Var}(\Delta F)}$ |
| Correlation form | $h^*=\rho \dfrac{\sigma_S}{\sigma_F}$ |
| Regression form | $\Delta S=\alpha+\beta \Delta F+\epsilon,\quad h^*=\beta$ |
| Hedge effectiveness | $R^2=\rho^2$ |
| Equity index hedge contracts | $N^*=\beta \dfrac{V_A}{V_F}$ |
| Target beta formula | $\dfrac{N V_F}{V_A}=\beta-\beta^*$ |

---

## Quick Exam Traps

> [!warning] Common Trap
> The optimal hedge ratio is **not always 1**. It depends on correlation and relative volatility.

> [!warning] Common Trap
> If the futures contract is weakly related to the spot exposure, adding more contracts does **not** improve the hedge. It may make risk worse.

> [!warning] Common Trap
> For equity portfolios, hedging with index futures mainly removes **systematic risk**, not all risk.

> [!warning] Common Trap
> A fully beta-hedged **single stock** is still exposed to firm-specific risk.

> [!warning] Common Trap
> To **increase** portfolio beta, you usually need to go **long** index futures, not short.

---