# Portfolio Diversification & Modern Portfolio Theory

## 1. Idiosyncratic vs. Systematic Risk

- **Idiosyncratic (Firm-Specific) Risk:** Risk unique to a single company.
    - *Examples:* Boeing (737 MAX grounding), Meta (earnings miss), McDonald’s (E. coli outbreak), NVIDIA (DeepSeek news), Credit Suisse (collapse).
    - **Can be diversified away** by holding many assets.

- **Systematic (Market) Risk:** Risk that affects the entire market or a large sector.
    - *Examples:* Macroeconomic announcements, natural catastrophes, wars, financial crises.
    - **Cannot be diversified away.**

> [!quote] Key principle
> “Don’t put all your eggs in one basket.” Diversification reduces portfolio risk without necessarily reducing expected return.

### Mathematical Illustration (i.i.d. stocks)
If we have $N$ stocks with independent and identically distributed returns:
- Each stock: $E[r_i] = \mu$, $Var(r_i) = \sigma^2$.
- Equally weighted portfolio: $r_p = \frac{1}{N}\sum_{i=1}^N r_i$.
- Portfolio variance: $Var(r_p) = \frac{\sigma^2}{N}$ → **risk decreases as $N$ increases**.
- Sharpe ratio: $SR = \frac{\mu - r_f}{\sigma / \sqrt{N}} = \sqrt{N} \cdot \frac{\mu - r_f}{\sigma}$.

> [!warning] Important
> The formula above relies on independence. In reality, stocks are correlated due to systematic risk, so the benefit of diversification is limited.

---

## 2. Modern Portfolio Theory (MPT) – Introduction

- Developed by **Harry Markowitz** (Nobel Prize 1990).
- Investors care only about **mean (expected return)** and **variance (risk)** of their portfolio.
- Utility function for an investor with risk aversion $A$:
  $$U = \mu - \frac{1}{2} A \sigma^2$$
  - $A > 0$: risk‑averse.
  - Higher $A$ means steeper indifference curves in $(\sigma, \mu)$ space.

- **Indifference curve:** all combinations of $(\sigma, \mu)$ giving the same utility.
- **Certainty equivalent rate** $r_{CE}$: the risk‑free rate that makes the investor indifferent to the risky asset.
  $$r_{CE} = \mu - \frac{1}{2} A \sigma^2$$

> [!example] Worked Example
> Risky asset: 20% gain (80% prob) or 30% loss (20% prob).  
> $\mu_a = 10\%$, $\sigma_a = 20\%$, $r_f = 4\%$.
> - For $A = 0.5$: Utility $U_a = 0.10 - 0.5 \times 0.5 \times (0.2)^2 = 0.09$ ($9\%$). Since $r_f = 4\%$, the risky asset is preferred.
> - Certainty equivalent $r_{CE} = 9\%$.
> - Indifference level $A$ solves $0.04 = 0.10 - 0.5 A (0.2)^2 \Rightarrow A = 3$.

---

## 3. Capital Allocation: One Risky Asset + Risk‑Free Asset

- Let $w$ = fraction invested in risky asset, $1-w$ in risk‑free.
- Portfolio return: $r_p = w r_a + (1-w) r_f$.
- Portfolio mean and variance:
  $$\mu_p = r_f + w(\mu_a - r_f),\quad \sigma_p = |w| \sigma_a$$

- **Capital Allocation Line (CAL):** plots $\mu_p$ against $\sigma_p$.
  $$\mu_p = r_f + \frac{\mu_a - r_f}{\sigma_a} \sigma_p$$
  - Slope = Sharpe ratio of the risky asset.

### Optimal $w$ (utility maximization)
  $$U_p(w) = r_f + w(\mu_a - r_f) - \frac{1}{2} A w^2 \sigma_a^2$$
  - First-order condition: $\mu_a - r_f - A \sigma_a^2 w = 0$
  - Optimal weight: $$w^* = \frac{\mu_a - r_f}{A \sigma_a^2}$$

> [!tip] Interpretation
> - If $w^* > 1$: investor borrows at $r_f$ to buy more of the risky asset (leverage).
> - $w^*$ can be negative (short selling) if $\mu_a - r_f < 0$, but then the risk‑free asset dominates.

> [!example] Optimal weights for different $A$
> Using the same asset ($\mu_a = 10\%$, $\sigma_a = 20\%$, $r_f = 4\%$):
> - $A = 0.5$: $w^* = 3.22$ (leverage)
> - $A = 1$: $w^* = 1.5$
> - $A = 1.5$: $w^* = 1.0$
> - $A = 2$: $w^* = 0.75$
> - $A = 2.5$: $w^* = 0.6$
> - $A = 3$: $w^* = 0.5$

---

## 4. Two Risky Assets

- Two assets $A$ and $B$ with means $\mu_A, \mu_B$, variances $\sigma_A^2, \sigma_B^2$, and correlation $\rho_{AB}$.
- Portfolio weight $w$ in $A$, $1-w$ in $B$.
- Portfolio mean: $\mu_p = w\mu_A + (1-w)\mu_B$
- Portfolio variance:
  $$\sigma_p^2 = w^2\sigma_A^2 + (1-w)^2\sigma_B^2 + 2w(1-w)\sigma_A\sigma_B\rho_{AB}$$

- **Portfolio opportunity set:** curve of achievable $(\sigma_p, \mu_p)$ as $w$ varies.
- Shape depends on $\rho_{AB}$:
  - $\rho = 1$: straight line (no diversification benefit).
  - $\rho = -1$: can achieve zero risk (perfect hedge).
  - $-1 < \rho < 1$: curve bends left, showing diversification gains.

> [!note] Minimum Variance Portfolio (MVP)
> The portfolio with the lowest possible risk (smallest $\sigma_p$). It lies at the leftmost point of the opportunity set.

---

## 5. Optimal Complete Portfolio (Two Risky + Risk‑Free)

We now combine the two risky assets with the risk‑free asset.

**Two-step procedure:**

1. **Find the tangency portfolio** (the risky portfolio that maximizes the Sharpe ratio).
   - Maximize $SR_p = \frac{\mu_p - r_f}{\sigma_p}$ over $w$.
   - This yields $w_A^*$ (weight of asset A in the tangency portfolio).  
     (Exact formula is derived in homework.)
   - The tangency portfolio is the same for **all investors**, independent of risk aversion.

2. **Allocate between risk‑free and the tangency portfolio** using the capital allocation rule from Section 3.
   - Treat the tangency portfolio as the single risky asset with its own $\mu_T$ and $\sigma_T$.
   - Optimal fraction $w^*$ in tangency portfolio:  
     $$w^* = \frac{\mu_T - r_f}{A \sigma_T^2}$$
   - This step **does depend on risk aversion** $A$.

- Final weights in complete portfolio:
  - Risk‑free: $1 - w^*$
  - Asset A: $w^* \cdot w_A^*$
  - Asset B: $w^* \cdot (1 - w_A^*)$

> [!important] Key insight of MPT
> All investors (regardless of risk tolerance) hold the **same** mix of risky assets (the tangency portfolio). Risk preference only determines how much to allocate to that mix versus the risk‑free asset.

---

## 6. Practical Challenges

- MPT requires estimates of all means, variances, and correlations.
- These estimates are **error‑prone** and small errors can lead to very different optimal portfolios.
- Including more assets increases complexity and estimation risk.
- This is a fundamental trade‑off: closer to true optimum vs. larger estimation error.

> [!seealso] Further reading
> FINA3103 or Bodie, Kane & Marcus, *Investments* for extensions (short‑sale constraints, multiple assets, etc.)
