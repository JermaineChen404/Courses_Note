# VaR in Practice

## Overview
This lecture moves beyond basic VaR calculation to address its **limitations**, introduces **Expected Shortfall** as a superior alternative, and covers **variance forecasting** techniques (EWMA, GARCH) that capture volatility dynamics.

---

## Part 1: Backtesting Recap & Binomial Tests (Page 3-7)

### 1.1 Statistical Model for Violations

Under the null hypothesis (VaR model is correct):

- Violations follow Binomial distribution: $m \sim \text{Binomial}(N, p)$
- $p = 1 - X$ (e.g., for 99% VaR, $p = 0.01$)

### 1.2 One-Sided Tests (page 5)

| Case | Test Statistic | Reject if |
|------|----------------|-----------|
| Too few ($m < Np$) | $\text{BINOMDIST}(m, N, p, 1)$ | $\le 0.05$ |
| Too many ($m > Np$) | $1 - \text{BINOMDIST}(m-1, N, p, 1)$ | $\le 0.05$ |

> [!warning] Common Mistake (page 6)
> The statement "Given that BINOMDIST(2,252,0.01,1)=0.54, we should reject the model with 5% confidence level if we observe 3 violations" is **INCORRECT**.
> 
> $P(\ge 3) = 1 - 0.54 = 0.46 > 0.05$ → **Do not reject**.

---

## Part 2: Limitations of VaR

### 2.1 The Normality Assumption Fails (pages 9-12)

**Reality**: Daily returns are **not** normally distributed. They exhibit:
- **Heavy tails** (more extreme events than normal)
- **Higher peak** (more observations near zero)

#### Measuring Tail Thickness: Kurtosis
$$ \text{Kurt}[X] = E\left[\left(\frac{X-\mu}{\sigma}\right)^4\right] = \frac{E[(X-\mu)^4]}{\sigma^4} $$

| Distribution | Kurtosis |
|--------------|----------|
| Normal | 3 |
| Heavy-tailed | > 3 (excess kurtosis) |

### 2.2 The Critical Problem with VaR (pages 13-14)

> [!danger] VaR's Blind Spot
> VaR only counts **how often** losses exceed the threshold, but ignores **how large** those losses are.

**Consequence**: Two portfolios with the **same 99% VaR** can have very different:
- Expected losses beyond VaR
- Exposure to catastrophic events

### 2.3 Gaming VaR (page 16)

A trader can **exploit VaR's limitations** by:
- Selling deep out-of-the-money options
	- Collecting premium most days (small gains)
	- Facing a rare but **huge** loss

The 99% VaR might not capture this loss if it lies beyond the 99th percentile.

---

## Part 3: Expected Shortfall (ES) – The Solution

### 3.1 Definition (page 14)
$$ \text{ES}_\alpha = E[\,L \mid L \geq \text{VaR}_\alpha\,] $$

"**If things do get bad, what is the expected loss?**"

### 3.2 ES Under Normality (page 17)

Let:
- $X$ = confidence level
- $Y = N^{-1}(X)$ (standard normal quantile)

Then:
$$ \text{VaR} = \mu + \sigma Y $$
$$ \text{ES} = \mu + \sigma \frac{e^{-Y^2/2}}{\sqrt{2\pi}(1-X)} $$

### 3.3 Visual Intuition (page 15)
Two distributions can have identical VaR but different ES because:
- One may have a "thicker" tail beyond VaR
- The other may have a "lighter" tail

> [!tip] Why Regulators Prefer ES
> ES captures the **average loss in the tail**, providing a more complete picture of extreme risk.

---

## Part 4: Coherence of Risk Measures (pages 18-20)

### 4.1 The Four Axioms of Coherent Risk Measures

| Axiom | Mathematical Statement | Meaning |
|-------|------------------------|---------|
| **Monotonicity** | If $L_1 \le L_2$ always, then $\rho(L_1) \le \rho(L_2)$ | Worse outcomes → higher risk |
| **Translation invariance** | $\rho(L - C) = \rho(L) - C$ | Adding cash reduces risk by that amount |
| **Positive homogeneity** | $\rho(\lambda L) = \lambda \rho(L)$, $\lambda \ge 0$ | Scaling portfolio scales risk |
| **Subadditivity** | $\rho(L_1 + L_2) \le \rho(L_1) + \rho(L_2)$ | Diversification shouldn't increase risk |

### 4.2 VaR vs. ES: Coherence Comparison

| Measure | Monotonicity | Translation Invariance | Positive Homogeneity | Subadditivity |
|---------|--------------|------------------------|----------------------|---------------|
| **VaR** | ✅ | ✅ | ✅ | ❌ |
| **ES** | ✅ | ✅ | ✅ | ✅ |

> [!important] Why Subadditivity Matters
> Without subadditivity, a risk measure could discourage diversification. VaR can violate this (e.g., with certain derivatives), while ES always satisfies it.

---

## Part 5: Variance Forecasting

### 5.1 Stylized Fact: Volatility Clustering (pages 22-23)

Returns exhibit:
- **Autocorrelation** in squared returns
- Periods of high volatility followed by high volatility
- Periods of low volatility followed by low volatility

### 5.2 Simple Moving Average (page 22)

Assuming zero mean for $u_i = \ln(S_i/S_{i-1})$:
$$ \sigma_n^2 = \frac{1}{m}\sum_{i=1}^m u_{n-i}^2 $$

**Problem**: Equal weights on all observations – doesn't reflect recent conditions.

### 5.3 EWMA (Exponentially Weighted Moving Average) – pages 24-25

**Formula**:
$$ \sigma_{t+1}^2 = \lambda \sigma_t^2 + (1-\lambda) R_t^2 $$

**Properties**:
- $\lambda$ = decay factor (typically 0.94 for daily data – RiskMetrics)
- Only need: current variance estimate + most recent return
- Tracks volatility changes quickly

> [!note] RiskMetrics Choice
> $\lambda = 0.94$ has been found optimal across many market variables.

### 5.4 GARCH(1,1) – pages 26-29

**Full name**: Generalized Autoregressive Conditional Heteroskedasticity

**Formula**:
$$ \sigma_n^2 = \gamma V_L + \alpha u_{n-1}^2 + \beta \sigma_{n-1}^2 $$

**Constraints**: $\gamma + \alpha + \beta = 1$ (weights sum to 1)

**Components**:
- $\gamma V_L$: weight on long-run average variance
- $\alpha u_{n-1}^2$: weight on most recent squared return
- $\beta \sigma_{n-1}^2$: weight on previous variance estimate

### 5.5 Worked Example (pages 28-29)

**Model**:
$$ \sigma_n^2 = 0.000002 + 0.13u_{n-1}^2 + 0.86\sigma_{n-1}^2 $$

**Long-run variance**:
$$ V_L = \frac{0.000002}{\gamma} \text{ where } \gamma = 1 - 0.13 - 0.86 = 0.01 $$
$$ V_L = \frac{0.000002}{0.01} = 0.0002 $$
$$ \text{Long-run volatility} = \sqrt{0.0002} = 1.4\% \text{ per day} $$

**Current state**:
- Current volatility estimate $\sigma_{n-1} = 1.6\%$ → $\sigma_{n-1}^2 = 0.000256$
- Most recent return $u_{n-1} = 1\%$ → $u_{n-1}^2 = 0.0001$

**New variance**:
$$ 
\begin{aligned}
\sigma_n^2 &= 0.000002 + 0.13 \times 0.0001 + 0.86 \times 0.000256 \\
&= 0.000002 + 0.000013 + 0.00022016 \\
&= 0.00023516
\end{aligned}
$$

**New volatility**:
$$ \sigma_n = \sqrt{0.00023516} = 1.53\% \text{ per day} $$

> [!check] Interpretation
> After a 1% return, volatility decreases from 1.6% to 1.53% because the return was smaller than the previous volatility estimate.

---

## Summary: VaR's Limitations & Solutions

| Limitation | Solution |
|------------|----------|
| Assumes stable variance | EWMA, GARCH |
| Ignores tail magnitude | Expected Shortfall |
| Not subadditive | Use ES instead |
| Normal distribution fails | Use historical simulation or heavy-tailed distributions |

---

## Concept Checklist

- [ ] Perform binomial backtesting correctly (including $m-1$ nuance)
- [ ] Explain heavy tails and kurtosis
- [ ] Describe VaR's blind spot (ignores tail magnitude)
- [ ] Calculate Expected Shortfall under normality
- [ ] List the four coherence axioms
- [ ] Explain why VaR fails subadditivity and ES doesn't
- [ ] Understand volatility clustering
- [ ] Apply EWMA formula and interpret $\lambda$
- [ ] Work through GARCH(1,1) examples
- [ ] Compare EWMA and GARCH

---

## Key Formulas Summary

| Concept | Formula |
|---------|---------|
| Kurtosis | $\text{Kurt}[X] = E\left[\left(\frac{X-\mu}{\sigma}\right)^4\right]$ |
| Expected Shortfall (normal) | $\text{ES} = \mu + \sigma \frac{e^{-Y^2/2}}{\sqrt{2\pi}(1-X)}$, $Y=N^{-1}(X)$ |
| EWMA | $\sigma_{t+1}^2 = \lambda \sigma_t^2 + (1-\lambda)R_t^2$ |
| GARCH(1,1) | $\sigma_n^2 = \gamma V_L + \alpha u_{n-1}^2 + \beta \sigma_{n-1}^2$, $\gamma+\alpha+\beta=1$ |
| Long-run variance (GARCH) | $V_L = \frac{\gamma V_L}{\gamma}$ (solved from parameters) |