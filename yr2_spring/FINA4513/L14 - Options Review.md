# Options Review

## Overview
This lecture reviews the fundamentals of **option payoffs**, **intrinsic and time value**, and the **Black‑Scholes‑Merton (BSM) model**. It uses a real‑world example (SVB puts during the 2023 banking turmoil) to illustrate option profit calculations. The lecture then connects options to a corporate finance application: the **Employee Stock Purchase Plan (ESPP)** as an embedded option. Finally, it walks through the BSM formula, its intuition as a **replicating portfolio**, and how option prices behave in extreme cases.

---

## Part 1: Option Payoffs and a Real‑World Example

### 1.1 The SVB Put Trade
- On **March 6**, SVB stock was **$283**.
- A trader bought **96 put contracts** with strike **$150** expiring **March 17** for **$0.01** per share.
- On **March 9**, SVB fell to **$106** and the puts traded at **$64.30**.

### 1.2 Profit Calculation
- Cost per contract:$0.01 \times 100 = \$1 $. Total cost:$ 96 \times 1 = \$96$.
- Sale value on March 9:$96 \times 64.30 \times 100 = \$617,280 $.
- **Profit =$617,184**.

> [!important] Why So Large?
> The options were **deep out‑of‑the‑money** on March 6 (strike $150, stock$283). After the stock crash, they became **deep in‑the‑money**. The **time value** component exploded due to extreme volatility.

---

## Part 2: Intrinsic Value and Time Value

### 2.1 Definitions
- **Intrinsic Value (IV):** The payoff if exercised immediately. For a put: $\max(K - S_t, 0)$.
- **Time Value (TV):** Option price minus intrinsic value. $TV = C - IV$.

### 2.2 Why Is Time Value Positive?
Because there is a chance the **intrinsic value may increase** before expiration. This explains why:
- **Out‑of‑the‑money options** trade at positive prices.
- **American options** are rarely exercised early (better to sell than exercise).

### 2.3 SVB Put Example
- **March 6:** $S = 283, K = 150$. IV = 0. Price = 0.01 → **All time value**.
- **March 9:** $S = 106, K = 150$. IV = 44. Price = 64.30 → TV = 20.30.

---

## Part 3: Employee Stock Purchase Plan (ESPP) as an Embedded Option

### 3.1 NVIDIA’s ESPP
- **15% discount** on the **lower of**:
    - Stock price at the **beginning** of the offering period.
    - Stock price at the **end** of the purchase period.
- This is a **lookback option** with a discount.

### 3.2 Payoff Example
- Offering period: 7/1/2021 – 12/31/2021.
- Start price $S_0 = \$202$.
- Contribution: **$10,625**.

**Scenario A: NVDA goes to$300.**
- Purchase price = $0.85 \times \min(202, 300) = 0.85 \times 202 = \$171.70$.
- Shares bought = $10,625 / 171.70 \approx 61.87$ shares.
- Value at $300 =$ 61.87 \times 300 = \$18,561$.
- **Gain =$18,561 -$10,625 =$7,936**.

**Scenario B: NVDA goes to $150.**
- Purchase price =$0.85 \times \min(202, 150) = 0.85 \times 150 = \$127.50 $.
- Shares bought =$10,625 / 127.50 \approx 83.33$shares.
- Value at$150 =$83.33 \times 150 = \$12,500$.
- **Gain = $12,500 -$10,625 = $1,875**.

> [!tip] The Option Feature
> The lookback ensures employees **always** get a discount off the **lower** price, creating a payoff similar to a **put option plus a forward**. Volatility increases the value of this benefit.

---

## Part 4: Factors Affecting Option Prices

| Factor | Effect on Call Price | Effect on Put Price |
|--------|---------------------|---------------------|
| Stock price ($S_0$) | + | – |
| Strike price ($K$) | – | + |
| Time to expiration ($T$) | + (usually) | + (usually) |
| Volatility ($\sigma$) | + | + |
| Risk‑free rate ($r$) | + | – |
| Dividends ($q$) | – | + |

> [!important] General Principle
> Option value increases when a variable **increases the probability or size of a positive payoff**.

---

## Part 5: The Black‑Scholes‑Merton (BSM) Model Intuition

### 5.1 The Call Price Formula
$$
C = S_0 N(d_1) - K e^{-rT} N(d_2)
$$
-$N(d_1)$: **Delta** – the number of shares in the replicating portfolio.
-$S_0 N(d_1)$: Cost of buying$\Delta$shares today.
-$K e^{-rT} N(d_2)$: Amount borrowed (present value of strike times risk‑neutral probability of exercise).

### 5.2 Risk‑Neutral Valuation
The BSM formula can be derived from:
$$
C_0 = e^{-rT} \, \mathbb{E}^Q[ \max(S_T - K, 0) ]
$$
It is the **discounted expected payoff** under the **risk‑neutral measure**.

---

## Part 6: Extreme Cases

### 6.1 As$S_0$Becomes Very Large (Deep In‑the‑Money Call)
-$d_1$and$d_2 \to \infty$, so$N(d_1) \to 1$and$N(d_2) \to 1$.
-$C \to S_0 - K e^{-rT}$(the lower bound).

### 6.2 As$S_0$Becomes Very Small (Deep Out‑of‑the‑Money Call)
-$C \to 0$.

### 6.3 As$T \to 0$(At Expiration)
- If$S_0 > K$,$d_1$and$d_2 \to +\infty$,$C \to S_0 - K$.
- If$S_0 < K$,$d_1$and$d_2 \to -\infty$,$C \to 0$.
- The option price converges to **intrinsic value**; time value vanishes.

> [!tip] Intuition
> At expiration, uncertainty is resolved. The option is either worth its exercise value or zero.

---

## Part 7: Generalized BSM for Dividends, Currency, and Futures

### 7.1 The General Formula
$$
C = S_0 e^{-qT} N(d_1) - K e^{-rT} N(d_2)
$$
$$
d_1 = \frac{\ln(S_0/K) + (r - q + \sigma^2/2)T}{\sigma\sqrt{T}}, \quad d_2 = d_1 - \sigma\sqrt{T}
$$

### 7.2 Special Cases of$q$| Asset Type |$q$Interpretation |
|------------|------------------------|
| Stock with dividend yield | Continuously compounded dividend yield |
| Currency option | Foreign risk‑free rate$r_f$|
| Futures option |$q = r$, and$S_0 = F_0$|

---

## Part 8: Risks in an Option Position (The Greeks Preview)

The value of an option is a function:
$$
V = f(S, K, T, r, \sigma, q)
$$
- **Delta ($\Delta$)**: Sensitivity to underlying price$S$.
- **Gamma ($\Gamma$)**: Sensitivity of delta to$S$(convexity).
- **Theta ($\Theta$)**: Time decay.
- **Vega ($\nu$)**: Sensitivity to volatility$\sigma$.
- **Rho ($\rho$)**: Sensitivity to interest rate$r$.

> [!note] For This Lecture
> The BSM formula provides the foundation for calculating all these risk measures.

---

## Summary

| Concept | Key Formula / Idea |
|---------|---------------------|
| Option Value | Intrinsic Value + Time Value |
| Intrinsic Value (Put) |$\max(K - S_t, 0)$|
| ESPP Gain | Discounted min($S_0, S_T$) |
| BSM Call Price |$C = S_0 N(d_1) - K e^{-rT} N(d_2)$|
| Replicating Portfolio | Long$\Delta$shares, borrow$K e^{-rT} N(d_2)$|
| General BSM | Replace$S_0$with$S_0 e^{-qT}$|
| Extreme$T \to 0$| Call value →$\max(S_0 - K, 0)$|

---

## Concept Checklist

- [ ] Calculate profit from a simple option trade given prices.
- [ ] Distinguish between intrinsic value and time value.
- [ ] Explain why time value is positive.
- [ ] Value an ESPP with a lookback feature.
- [ ] List the six factors affecting option prices and their directional effects.
- [ ] Write down the BSM call formula and interpret each term.
- [ ] Describe the behavior of call and put prices as$S_0 \to \infty$and$S_0 \to 0$.
- [ ] Explain what happens to option price as$T \to 0$.
- [ ] Identify the meaning of$q$for stocks, currencies, and futures.

---

## Quick Exam Traps

> [!warning] Trap
> Time value is **not** the amount of time remaining. It is the **excess of option price over intrinsic value**.

> [!warning] Trap
> For a put, intrinsic value =$\max(K - S, 0)$. Do not use$S - K$.

> [!warning] Trap
> An increase in volatility **always** increases both call and put prices (holding all else equal).

> [!warning] Trap
> In the BSM formula,$N(d_1)$is **not** the probability that the option will be in the money. That is$N(d_2)$in the risk‑neutral world.

> [!warning] Trap
> For futures options, the underlying “$S_0$” is the futures price$F_0$, and$q = r$. This changes the$d_1$$ term accordingly.