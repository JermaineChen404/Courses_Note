# Why Manage Risk? Part I

## Overview
This lecture examines **decision making under uncertainty** from an individual perspective (utility theory, risk aversion) and then asks whether firms should care about risk. It introduces the **irrelevance proposition** – under perfect markets, risk management does not affect firm value.

---

## Part 1: Decision Making Under Uncertainty

### 1.1 The Trader Game (pages 3–4)

**Initial wealth**: $100  
**Two strategies** each round:

| Strategy | Return | Probability |
|----------|--------|-------------|
| Safe | +20% | 50% |
|      | –10% | 50% |
| Risky | +100% | 10% |
|       | –50%  | 90% |

**Rules**:
- Three rounds, you can reinvest each round.
- If total profit < $40 at the end, you get fired (payoff = 0).
- Otherwise, bonus = 30% of profits.

**Question**: Would you ever take the risky strategy? Why?

### 1.2 Last Round Decision (pages 7–9)

- If you have **$200** going into the last round:
  - Safe: 50% chance of $240, 50% chance of $180 → expected value $210
  - Risky: 10% chance of $400, 90% chance of $100 → expected value $130
  - Safe gives higher **expected payoff**.
- If you have **$100** going into the last round:
  - Safe: 50% chance of $120, 50% chance of $90 → expected $105
  - Risky: 10% chance of $200, 90% chance of $50 → expected $65
  - Safe again dominates in expected value.

> [!note] With linear utility (risk‑neutral), you always choose the strategy with higher expected value. But real people may have different preferences.

---

## 2. Utility Theory and Risk Attitudes

### 2.1 Expected Utility Framework
$$ E[u(x)] = p u(x_1) + (1-p) u(x_2) $$

### 2.2 Risk Neutrality (page 10)
- Utility is linear: $u(x) = x$ (or $ax+b$)
- Only expected value matters.

### 2.3 Risk Aversion (pages 11–12)
- Utility is **concave**: $u'(x) > 0$, $u''(x) < 0$
- Diminishing marginal utility – each extra dollar is worth less when you're rich.
- **Jensen’s inequality**: For a concave function,
  $$ E[u(x)] \le u(E[x]) $$
  The certainty equivalent (certain amount that gives same utility) is **less** than the expected value.

### 2.4 Risk Loving (page 13)
- Utility is **convex**: $u''(x) > 0$
- You prefer the gamble over a sure thing with same mean.

---

## 3. Certainty Equivalent and Risk Premium (pages 14–19)

### 3.1 Example with Square‑Root Utility
Initial wealth = 40, equally likely to become 16 or 64.
$$ u(x) = \sqrt{x} $$

**Expected utility**:
$$ E[u] = 0.5 \sqrt{16} + 0.5 \sqrt{64} = 0.5\times 4 + 0.5\times 8 = 6 $$

**Certainty equivalent (CE)**:
$$ u(CE) = 6 \implies \sqrt{CE} = 6 \implies CE = 36 $$

**Risk premium**:
$$ E[x] - CE = \frac{16+64}{2} - 36 = 40 - 36 = 4 $$

> [!important] The individual would be willing to pay **up to $4** to replace the risky outcome with a sure $40. This is the maximum insurance premium they'd pay.

### 3.2 Graphical Intuition (page 18)
- CE is the point on the x‑axis where the utility function reaches the same level as expected utility.
- Risk premium = distance between $E[x]$ and CE.

---

## 4. From Individuals to Firms (pages 20–22)

- For a **value‑maximizing firm**, the objective is to increase firm value.
- Risk management is **costly** (insurance premiums, derivative transactions, monitoring).
- So the question: **Can hedging increase firm value?** If so, through which channels?

---

## 5. Review: Valuation Models (pages 23–26)

### 5.1 Discounted Cash Flow (DCF)
$$ \text{Firm Value} = \sum_{t=1}^\infty \frac{E(CF_t)}{(1+r)^t} $$
where $r$ is the cost of capital.

### 5.2 Weighted Average Cost of Capital (WACC)
- Blended cost of debt and equity.

### 5.3 Capital Asset Pricing Model (CAPM)
For an unlevered firm, cost of equity:
$$ E[R] = R_f + \beta (E[R_M] - R_f) $$
$$ \beta = \frac{\mathrm{Cov}(R, R_M)}{\mathrm{Var}(R_M)} $$

- $\beta$ measures **systematic risk** (risk that cannot be diversified away).
- Investors are only compensated for systematic risk, not total risk.

---

## 6. Should a Firm Hedge Diversifiable Risk? (pages 27–28)

**Example**: XYZ has market value $1 billion. It can pay $5 million to transfer a diversifiable risk to an investment bank. The policy reduces expected cash flow by $5 million (the cost) but has no other impact.

**Question**: Should the firm do it?

**Answer**: **No**. Investors can diversify away that risk themselves at no cost. The firm’s cost of capital ($r$ in DCF) does **not** change because the risk is diversifiable. The $5 million cost directly reduces expected cash flow, so firm value falls by $5 million.

> [!quote] "Diversifiable risks will not increase firm value by decreasing the required rate of return of investors (investors can diversify themselves)."

---

## 7. Systematic Risk and Hedging (page 29)

- Systematic risk (market risk) cannot be diversified by investors.
- Hedging it would require transferring it to another party, which is costly.
- In perfect markets, all parties price systematic risk the same way, so the cost of hedging exactly offsets the benefit → no net gain.

---

## 8. The Irrelevance Proposition (pages 30–36)

### 8.1 Setup (page 30)
Two identical aluminum producers, A and B:
- 50 million shares, no debt
- Production cost $1000/ton
- Will produce 10,000 tons to be sold in 1 year
- **A hedges** by selling forward at $1200/ton
- **B does not hedge**

**Question**: Will you pay more for Company A?

### 8.2 Arbitrage Proof (pages 31–32)

**If $P_A > P_B$**:
1. Buy 500,000 shares of B (1% of B)
2. Sell 100 tons of aluminum forward at $1200
3. Short 500,000 shares of A

**Today's cash flow**: $500,000 (P_A - P_B) > 0$

**Year 1 profit** (zero, by construction):
$$ \underbrace{\frac{5\times10^5}{50\times10^6} \times 10,000 (S_1 - 1000)}_{\text{gain on B shares}} + \underbrace{100(1200 - S_1)}_{\text{forward}} - \underbrace{\frac{5\times10^5}{50\times10^6} \times 10,000 (1200 - 1000)}_{\text{short A shares}} = 0 $$

**If $P_B > P_A$**, reverse the strategy (buy A, sell forward, short B) for a risk‑free profit.

> [!important] Conclusion: In perfect markets, **no price difference can persist**. Hedging does **not** increase firm value.

### 8.3 Takeaway (page 35)
Shareholders will not pay a premium for a reduction in **total risk** because they can eliminate diversifiable risk themselves.

### 8.4 Conditions for Irrelevance (page 36)
Same logic as Modigliani‑Miller:
- No distress costs
- No taxes
- No financing frictions
- No transaction costs
- Investors can manage risk as cheaply and efficiently as firms

---

## 9. Concept Checklist

- [ ] Compute expected utility for simple gambles
- [ ] Distinguish risk‑neutral, risk‑averse, and risk‑loving preferences
- [ ] Apply Jensen’s inequality to concave/convex utility
- [ ] Calculate certainty equivalent and risk premium
- [ ] Understand DCF and CAPM: systematic vs. diversifiable risk
- [ ] Explain why hedging diversifiable risk doesn't add value
- [ ] Work through the arbitrage proof of the irrelevance proposition
- [ ] List the conditions under which risk management is irrelevant

---

## Key Formulas Summary

| Concept | Formula |
|---------|---------|
| Expected utility | $E[u(x)] = \sum p_i u(x_i)$ |
| Certainty equivalent | $u(CE) = E[u(x)]$ |
| Risk premium | $E[x] - CE$ |
| CAPM expected return | $E[R] = R_f + \beta (E[R_M]-R_f)$ |
| Beta | $\beta = \frac{\mathrm{Cov}(R,R_M)}{\mathrm{Var}(R_M)}$ |
| Irrelevance arbitrage profit | $500,000(P_A - P_B)$ today, zero future |