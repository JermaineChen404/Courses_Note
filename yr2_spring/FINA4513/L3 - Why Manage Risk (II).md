# Why Manage Risk? (Part II)

## Overview
This lecture explores **when and why risk management adds value to a firm**, moving beyond the Modigliani-Miller irrelevance proposition to examine real-world imperfections that make hedging beneficial.

---

## 1. The Irrelevance Proposition: When Hedging Doesn't Matter

### Setup: Two Identical Aluminum Producers
| Feature | Company A | Company B |
|---------|-----------|-----------|
| Shares outstanding | 50 million | 50 million |
| Debt | None | None |
| Production cost | $1000/ton | $1000/ton |
| Output | 10,000 tons | 10,000 tons |
| Hedging strategy | Sells forward at $1200/ton | No hedging |

### The Question
Would you pay more for Company A's shares? **No** – under perfect markets.

### The Arbitrage Proof

**If $P_A > P_B$**:

1. **Buy** 500,000 shares of B (represents 1% of B, since 500k/50M = 0.01)
2. **Sell** 100 tons of aluminum forward at $1200 (replicates A's hedge)
3. **Short** 500,000 shares of A

**Today's cash flow**: $500,000 \times (P_A - P_B) > 0$

**Year 1 payoff**:
- From B shares: $\frac{500,000}{50,000,000} \times 10,000(S_1 - 1000) = 0.01 \times 10,000(S_1 - 1000) = 100(S_1 - 1000)$
- From forward contract: $100(1200 - S_1)$
- From short A shares: $-\frac{500,000}{50,000,000} \times 10,000(1200 - 1000) = -100(200)$

**Total** = $100(S_1 - 1000) + 100(1200 - S_1) - 20,000 = 0$

**If $P_B > P_A$**: Reverse the strategy (buy A, sell forward, short B) for a risk-free profit.

> [!important] Core Insight
> In a frictionless world, **investors can replicate any corporate hedge** themselves. Therefore, hedging does not affect firm value. This is a direct application of Modigliani-Miller.

---

## 2. Conditions for Irrelevance (page 7)

Risk management doesn't affect firm value when:
- ✅ No distress costs
- ✅ No tax effects
- ✅ No frictions on financing
- ✅ No transaction costs
- ✅ Investors can manage risk as cheaply and efficiently as firms

---

## 3. Market Imperfections: When Hedging Creates Value (page 8)

| Imperfection | Why It Matters |
|--------------|----------------|
| **Financial distress costs** | Bankruptcy is expensive |
| **Progressive taxes** | Convex tax function makes smoothing profitable |
| **Costly external financing** | Internal funds are cheaper |
| **Asymmetric information** | External financing signals problems |
| **Moral hazard / conflicts** | Agency problems affect investment |
| **Transaction costs** | Firms may hedge more cheaply |
| **Managerial concerns** | Risk-averse managers with undiversified human capital |
| **Risk-averse owners** | Owners with concentrated wealth |

---

## 4. Financial Distress Costs (pages 9-11)

### Types of Distress Costs
- Lost sales (customers avoid bankrupt companies)
- Key employees leave
- Legal and accounting costs
- Forced asset sales at depressed prices

### Numerical Example
| Parameter | Value |
|-----------|-------|
| Default costs | $25 million |
| Default probability without hedging | 10% |
| Hedging cost | $2 million |
| Default probability with hedging | 0% |

**Expected distress cost without hedge** = $0.10 × $25M = $2.5M  
**Hedging cost** = $2.0M  
**Net benefit of hedging** = $0.5M

> [!tip] Decision Rule
> Hedge if: **Reduction in expected distress cost > Cost of hedging**

---

## 5. Progressive Taxes (pages 12-15)

### Key Insight
With progressive (convex) tax rates, after-tax income is a **concave function** of pre-tax income. By Jensen's inequality:
$$ E[U(\text{income})] < U(E[\text{income}]) $$

Smoothing income via hedging **reduces expected tax payments**.

### In-Class Exercise (page 15)

**Setup**:
- Before-tax income: $20M or $80M with equal probability (0.5 each)
- Tax system is progressive (higher rate on higher income)

**Task**: Compare expected after-tax income:
1. Without hedging (random income)
2. With hedging that guarantees $50M before-tax income

**Why hedging wins**:
- Without hedge: You pay high tax rate half the time
- With hedge: You pay the medium tax rate all the time
- The reduction in tax in the high state outweighs the slight increase in tax in the low state

---

## 6. Costly External Financing & Investment Opportunities (pages 16-22)

### Model Structure (page 17)

**Timeline**:
- **Period 0**: Hedging decision against cash flow shock
- **Period 1**: Investment financed by:
  - Internal cash flow $w$ (realized)
  - External financing $e$ (costly)

**Key relationships**:
- Investment: $I = w + e$
- External financing cost: $C(e)$, with $C'(e) > 0$, $C''(e) > 0$ (convex)
- Return on investment: $f(I)$, with $f'(I) > 0$, $f''(I) < 0$ (concave)

### Firm's Problem at Period 1 (page 18)
Given realized cash flow $w$:
$$ P(w) = \max_{I} f(I) - I - C(e) $$
subject to $I = w + e$

Rewriting with $e = I - w$:
$$ P(w) = \max_{I} f(I) - I - C(I - w) $$

### Properties of the Solution (page 19)

**First derivative** (envelope theorem):
$$ P'(w) = f'(I^*(w)) - 1 > 0 $$
Higher cash flow → higher firm value

**Second derivative**:
$$ P''(w) = f''(I^*(w)) \times \frac{dI^*(w)}{dw} < 0 $$
Because $f'' < 0$ and $\frac{dI^*}{dw} > 0$

> [!important] Key Result
> The firm's value $P(w)$ is **increasing and concave** in internal cash flow $w$.

### Why Concavity Creates Hedging Value (pages 21-22)

**Without hedging**: $w = w_0 \epsilon$, where $\epsilon$ is random (e.g., 0 or 2 with equal probability)

**With hedging**: $w = w_0(h + (1-h)\epsilon)$, where $h$ is hedge ratio
- $h=0$: no hedge (full exposure)
- $h=1$: full hedge (certain cash flow $w_0$)

**Expected payoff comparison**:
$$ E[P(w_{\text{no hedge}})] = 0.5P(0) + 0.5P(2w_0) $$
$$ E[P(w_{\text{full hedge}})] = P(w_0) $$

By concavity:
$$ P(w_0) > 0.5P(0) + 0.5P(2w_0) $$

> [!check] Hedging Benefit
> Concavity of $P(w)$ means that **stabilizing cash flow increases expected firm value**.

---

## 7. Correlation Between Cash Flow and Investment Opportunities (pages 23-24)

### Extended Model: Petroleum Company
Two random variables both depend on oil price:

| Variable | Relationship |
|----------|--------------|
| Revenue ($w$) | $w = w_0 \epsilon$ |
| Investment productivity ($\theta$) | $\theta = 1 + \alpha(\epsilon - 1)$ |

Where $\epsilon$ is the oil price shock (e.g., 1 or 2 with equal probability)

### Interpretation of $\alpha$
- **$\alpha > 0$**: Positive correlation – high oil price means:
  - High cash flow ($\epsilon=2$)
  - Good investment opportunities ($\theta > 1$)
- **$\alpha < 0$**: Negative correlation – high oil price means:
  - High cash flow
  - Poor investment opportunities ($\theta < 1$)

### Hedging Implications

| Scenario | Hedging Incentive |
|----------|-------------------|
| $\alpha > 0$ | **Weaker** – When cash flow is low, investment opportunities are also poor (don't need much cash) |
| $\alpha < 0$ | **Stronger** – When cash flow is low, investment opportunities are good (need cash the most) |

> [!question] True/False (page 24)
> **"When $\alpha$ is positive, the higher the $\alpha$, the weaker incentive for firms to hedge"**
> 
> **Answer: TRUE** – Higher $\alpha$ means stronger positive correlation, reducing the need to transfer cash to low-cash states (because those states also have low investment needs).

---

## 8. Managerial Concerns (page 25)

### Problem
- Managers are **risk-averse**
- Their human capital is **undiversified** and tied to the firm
- They may also have firm stock in their private portfolios

### Solution
Hedging reduces firm value volatility, benefiting managers who cannot easily:
- Diversify away firm-specific risk
- Write perfect employment contracts that compensate for this risk

> [!note] Condition for Value
> Risk management for managerial concerns is valuable only if:
> 1. No employment contract can fully satisfy risk-averse managers
> 2. Managers cannot easily diversify their firm-specific exposure

---

## Concept Checklist

- [ ] Understand the arbitrage proof of hedging irrelevance
- [ ] List the conditions under which MM holds for risk management
- [ ] Identify real-world imperfections that make hedging valuable
- [ ] Calculate expected distress costs and hedging benefits
- [ ] Explain how progressive taxes create a hedging motive (convexity)
- [ ] Model costly external financing and derive concave $P(w)$
- [ ] Understand why concavity of $P(w)$ implies hedging benefit
- [ ] Analyze how correlation between cash flows and investment opportunities affects hedging incentives
- [ ] Explain managerial risk aversion as a rationale for hedging

---

## Key Formulas Summary

| Concept | Formula |
|---------|---------|
| Firm value given cash flow $w$ | $P(w) = \max_I f(I) - I - C(I-w)$ |
| First derivative | $P'(w) = f'(I^*(w)) - 1 > 0$ |
| Second derivative | $P''(w) = f''(I^*(w)) \frac{dI^*}{dw} < 0$ |
| Hedging benefit (concavity) | $E[P(w)] < P(E[w])$ |
| Investment productivity with correlation | $\theta = 1 + \alpha(\epsilon - 1)$ |