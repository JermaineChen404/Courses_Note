# Value at Risk (VaR): Basics

## Course Overview
This lecture introduces the **fundamental concepts of Value at Risk (VaR)**, including its definition, calculation under normality, scaling over time, portfolio applications, and the link to **economic capital**.

---

## Part 1: What is VaR?

### 1.1 The Classic Statement (page 3)

> "There is **5% chance** that the bank will lose **more than \$10 million** over the next week"

This is equivalent to:
> "We are **95% certain** that the bank will **NOT lose more than \$10 million** over the next week"

Therefore:
> **5% VaR is \$10 million over the next week**

### 1.2 Formal Definition (pages 4-5)

$$ \text{VaR}(X, T) = \text{Upper bound for losses in } T \text{ business days with } X\% \text{ confidence} $$

If $z$ represents future losses:
$$ \Pr\{z \leq \text{VaR}(X,T)\} = X $$

**Example**: $\text{VaR}(0.95, 21)$ means "21-day VaR at 95% confidence"

> [!note] Interpretation
> VaR answers the question: **"How bad can things get?"** with a specified confidence level over a given horizon.

---

## Part 2: Basic Examples

### 2.1 Example 1: Uniform Distribution (page 6)

**Scenario**: All outcomes between -\$50 million and +\$50 million are **equally likely** (uniform distribution) for a one-year project.

**Find**: $\text{VaR}(0.99, 1\text{yr})$

**Solution**:
- Total range: 100 million (from -50 to +50)
- 99% VaR means we want the loss level such that 99% of outcomes are **below** it
- Since losses are positive numbers in VaR definition, we need to be careful with sign

For uniform distribution from -50 to +50:
- The 99th percentile of the **loss distribution** (where loss = negative of return) occurs at the point where 99% of losses are below this value
- With uniform distribution, this is simply: $-50 + 0.99 \times 100 = 49$

**Answer**: $\text{VaR}(0.99, 1\text{yr}) = \$49 \text{ million}$

---

### 2.2 The Standard Normal CDF: $N(x)$ (page 7)

$N(x)$ = probability that a standard normal variable is **less than** $x$

**Key property**:
$$ N(-x) = 1 - N(x) $$

**Important values**:

| $x$ | $N(x)$ |
|-----|--------|
| -2.326 | 0.01 |
| -1.645 | 0.05 |
| 0 | 0.5 |
| 1.645 | 0.95 |
| 2.326 | 0.99 |

> [!tip] Excel Function
> `NORMSDIST(x)` gives $N(x)$ in Excel.

---

## Part 3: VaR Under Normality

### 3.1 Derivation of the VaR Formula (pages 8-9)

If losses follow a normal distribution: $l \sim N(\mu, \sigma^2)$

Let $z$ be standard normal, so $l = \mu + \sigma z$

$$
\begin{aligned}
\Pr(l \leq \text{VaR}) &= X \\
\Pr(\mu + \sigma z \leq \text{VaR}) &= X \\
\Pr\left(z \leq \frac{\text{VaR} - \mu}{\sigma}\right) &= X \\
N\left(\frac{\text{VaR} - \mu}{\sigma}\right) &= X
\end{aligned}
$$

Therefore:
$$ \boxed{\text{VaR}(X,T) = \mu + \sigma N^{-1}(X)} $$

> [!important] Key Insight
> $N^{-1}(X)$ is the inverse CDF (quantile function) of the standard normal. For 99% VaR, $N^{-1}(0.99) = 2.326$.

### 3.2 Example 2: Single Security (page 10)

**Given**:
- Daily return normally distributed
- Mean = 0
- Standard deviation = 2.5%

**Find**: 1% VaR for one-day ahead return

**Solution**:
$$ \text{VaR}(0.99, 1\text{day}) = 0 + (2.5\%) \times N^{-1}(0.99) = 2.5\% \times 2.326 = 5.815\% $$

**Interpretation**: There is a 1% chance of losing more than 5.815% in one day.

### 3.3 Example 3: With Non-Zero Mean (page 11)

**Given**:
- Mean return = \$2 million
- Standard deviation = \$10 million

**Find**: 1% VaR

$$ \text{VaR} = 2 + 10 \times 2.326 = 2 + 23.26 = \$25.26 \text{ million} $$

---

## Part 4: Scaling VaR Over Time (page 13)

### 4.1 The Square Root Rule

If per-period losses are **i.i.d.** with $z_i \sim N(\mu, \sigma^2)$, then over $T$ periods:

$$ \mathbb{E}(z_1 + z_2 + \dots + z_T) = \mu T $$
$$ \text{Var}(z_1 + z_2 + \dots + z_T) = \sigma^2 T $$
$$ \text{Std}(z_1 + z_2 + \dots + z_T) = \sigma \sqrt{T} $$

Therefore:
$$ \boxed{\text{VaR}(X, T) = \mu T + \sigma \sqrt{T} N^{-1}(X)} $$

> [!warning] Assumptions
> This scaling rule assumes:
> 1. Returns are **independent** across periods
> 2. Returns are **identically distributed**
> 3. The mean scales linearly with time (often assumed zero for short horizons)

### 4.2 Microsoft Example (page 14)

**Position**: \$10 million in Microsoft shares

**Assumptions**:
- Expected change = 0 (reasonable for short horizons)
- Daily volatility = 2% (≈ 32% annual)

**Calculate 10-day 99% VaR**:

1. Daily standard deviation in dollars: $10\text{M} \times 2\% = \$200,000$
2. 10-day standard deviation: $200,000 \times \sqrt{10} = \$632,500$
3. 99% VaR: $632,500 \times 2.326 = \$1,471,300$

**Interpretation**: The bank can be 99% confident that it will not lose more than \$1.47 million over 10 days from this Microsoft position.

---

## Part 5: Portfolio VaR with Two Assets

### 5.1 Example: Microsoft + AT&T (pages 15-17)

**Portfolio composition**:
- Microsoft: \$10 million, daily volatility 2% → daily $\sigma_{MSFT} = \$200,000$
- AT&T: \$5 million, daily volatility 1% → daily $\sigma_{T} = \$50,000$
- Correlation between returns: $\rho = 0.3$

### 5.2 Standard Deviation of Portfolio (page 16)

**Formula for two assets**:
$$ \sigma_{X+Y} = \sqrt{\sigma_X^2 + \sigma_Y^2 + 2\rho\sigma_X\sigma_Y} $$

**Calculation**:
$$
\begin{aligned}
\sigma_{\text{portfolio, daily}} &= \sqrt{(200,000)^2 + (50,000)^2 + 2(0.3)(200,000)(50,000)} \\
&= \sqrt{40,000,000,000 + 2,500,000,000 + 2(0.3)(10,000,000,000)} \\
&= \sqrt{42,500,000,000 + 6,000,000,000} \\
&= \sqrt{48,500,000,000} \\
&= \$220,200
\end{aligned}
$$

### 5.3 10-Day 99% VaR for Portfolio (page 17)

$$ \text{VaR}_{10\text{-day, }99\%} = 220,200 \times \sqrt{10} \times 2.326 = \$1,620,100 $$

### 5.4 Incremental Effect of AT&T

| Position | 10-day 99% VaR |
|----------|----------------|
| Microsoft only | \$1,471,300 |
| Microsoft + AT&T | \$1,620,100 |
| AT&T only (standalone) | \$367,800 |

**Observation**: Adding AT&T increases VaR by only \$148,800, which is **less than** AT&T's standalone VaR (\$367,800). This is the **diversification benefit** from less-than-perfect correlation ($\rho = 0.3$).

> [!tip] Diversification Effect
> When $\rho < 1$, portfolio VaR < sum of individual VaRs.

---

## Part 6: Properties of VaR

### 6.1 Translation Invariance (page 20)

> **Statement**: If an amount of cash $C$ is added to a portfolio, VaR must go down by $C$.

**Mathematically**:
$$ \text{VaR}(L - C) = \text{VaR}(L) - C $$

**Intuition**: Cash is risk-free. Adding it creates a cushion that directly reduces potential loss.

**Answer**: **TRUE** (this is a fundamental property)

### 6.2 Positive Homogeneity (page 20)

> **Statement**: Changing the size of a portfolio by $\lambda$ should result in the risk measure being multiplied by $\lambda$.

**Mathematically**:
$$ \text{VaR}(\lambda L) = \lambda \cdot \text{VaR}(L), \quad \lambda \ge 0 $$

**Intuition**: If you double the position, you double the risk.

**Answer**: **TRUE**

> [!note] These are two of the four coherence axioms (more in L6).

---

## Part 7: Economic Capital (pages 23-29)

### 7.1 The Core Question (page 23)

**Given**:
- Portfolio return next year: $r \sim N(0.6\%, 1.5\%)$ (mean 0.6%, standard deviation 1.5%)
- Find: 1% VaR (in percentage of assets)

**Solution**:
$$ \text{VaR}_{99\%} = \mu + \sigma N^{-1}(0.99) = 0.6\% + 1.5\% \times 2.326 = 0.6\% + 3.489\% = 2.889\% $$

**Interpretation**: The bank is 99% confident that it will not lose more than **2.889% of assets**.

### 7.2 From VaR to Required Equity (pages 23-25)

**Question**: How much equity is needed so that the bank is 99% confident of having **positive equity** (no default)?

**Setup**:
- Initial assets: $A_0$
- Initial equity (as % of assets): $E_0$
- Debt: $D_0 = A_0(1 - E_0)$
- Return next year: $r \sim N(\mu, \sigma^2)$

**Assets next year**: $A_1 = A_0(1 + r)$
**Equity next year**: $E_1 = A_1 - D_0 = A_0(1 + r) - A_0(1 - E_0) = A_0(r + E_0)$

**Equity next year as percentage of initial assets**:
$$ E' = r + E_0 $$

**Solvency condition**:
$$ \Pr(E' > 0) = \Pr(r + E_0 > 0) = 0.99 $$

**Solve for $E_0$**:
$$ \Pr(r > -E_0) = 0.99 $$
Since $r \sim N(\mu, \sigma^2)$:
$$ \frac{-E_0 - \mu}{\sigma} = N^{-1}(0.01) = -2.326 $$
$$ -E_0 - \mu = -2.326\sigma $$
$$ E_0 = 2.326\sigma - \mu $$

**Plug numbers** ($\mu = 0.6\%$, $\sigma = 1.5\%$):
$$ E_0 = 2.326 \times 1.5\% - 0.6\% = 3.489\% - 0.6\% = 2.889\% $$

> [!important] Key Result
> The required equity equals the **VaR**! To be 99% confident of solvency, equity must be at least the 99% VaR.

### 7.3 In-Class Exercise: Multi-Period Case (pages 26-29)

**Problem**:
- Profit each year: $r \sim N(1.5\%, 2.5\%)$ (mean 1.5%, std 2.5%)
- Time horizon: 2 years
- Target: 99% confident that equity at end of 2 years ≥ 5% of assets
- Find: Required initial equity $E_0$ (as % of assets)

**Step 1: 2-year return distribution**
$$ \mu_{2y} = 2 \times 1.5\% = 3\% $$
$$ \sigma_{2y} = \sqrt{2} \times 2.5\% = 3.536\% $$

**Step 2: Solvency condition**
Let $r_{2y}$ be 2-year return. End equity (as % of initial assets) = $r_{2y} + E_0$

We need:
$$ \Pr(r_{2y} + E_0 \geq 5\%) = 0.99 $$

**Step 3: Standardize**
$$ \Pr\left(\frac{r_{2y} - \mu_{2y}}{\sigma_{2y}} \geq \frac{5\% - E_0 - \mu_{2y}}{\sigma_{2y}}\right) = 0.99 $$

Let $z$ be standard normal. Then:
$$ \Pr\left(z \geq \frac{5\% - E_0 - 3\%}{3.536\%}\right) = 0.99 $$

**Step 4: Use quantile**
For standard normal, $\Pr(z \geq k) = 0.99$ means $k = -2.326$ (since $\Pr(z \leq -2.326) = 0.01$)

Therefore:
$$ \frac{5\% - E_0 - 3\%}{3.536\%} = -2.326 $$

**Step 5: Solve for $E_0$**
$$ 2\% - E_0 = -2.326 \times 3.536\% $$
$$ 2\% - E_0 = -8.225\% $$
$$ E_0 = 2\% + 8.225\% = 10.225\% $$

> [!check] Answer
> The company needs **10.23%** initial equity (as % of assets) to be 99% confident that equity won't fall below 5% after 2 years.

---

## Part 8: Economic Capital and Credit Ratings (pages 30-31)

### 8.1 Definition of Economic Capital (page 30)

> **Economic Capital**: The amount of capital a financial institution needs to absorb losses over one year with a certain confidence level so that it can remain solvent (or meet a target credit rating) with high probability.

### 8.2 Choosing the Confidence Level (page 31)

The confidence level depends on the **target credit rating**:

| Target Rating | 1-Year Default Probability | Appropriate Confidence Level |
|---------------|----------------------------|------------------------------|
| AA | 0.03% | 99.97% |
| BBB- | 0.2% | 99.8% |

> [!note] Link to Ratings
> A bank aiming for AA rating must hold enough capital to survive events that occur with probability 99.97%. This means its VaR should be calculated at the 99.97% confidence level.

---

## Concept Checklist

- [ ] Understand the verbal definition of VaR
- [ ] Convert between "chance of loss > X" and "confidence of loss ≤ X"
- [ ] Know key standard normal quantiles (1.645, 2.326)
- [ ] Derive the normal VaR formula: $\text{VaR} = \mu + \sigma N^{-1}(X)$
- [ ] Calculate VaR for single assets
- [ ] Apply the square root rule for time scaling
- [ ] Compute portfolio VaR with two assets and correlation
- [ ] Explain diversification benefit in VaR terms
- [ ] Understand translation invariance and positive homogeneity
- [ ] Link VaR to required equity for solvency
- [ ] Solve multi-period equity requirement problems
- [ ] Connect confidence levels to credit ratings

---

## Key Formulas Summary

| Concept | Formula |
|---------|---------|
| VaR definition | $\Pr(l \leq \text{VaR}) = X$ |
| Normal VaR | $\text{VaR} = \mu + \sigma N^{-1}(X)$ |
| Time scaling (i.i.d.) | $\text{VaR}(X,T) = \mu T + \sigma \sqrt{T} N^{-1}(X)$ |
| Two-asset portfolio std | $\sigma_{X+Y} = \sqrt{\sigma_X^2 + \sigma_Y^2 + 2\rho\sigma_X\sigma_Y}$ |
| Translation invariance | $\text{VaR}(L - C) = \text{VaR}(L) - C$ |
| Positive homogeneity | $\text{VaR}(\lambda L) = \lambda \text{VaR}(L)$ |
| Equity requirement (1 period) | $E_0 = \text{VaR}$ for solvency at same confidence |
| Equity requirement (T periods) | $E_0 = \text{Target} - \mu_T + N^{-1}(X)\sigma_T$ |

---

## Common Pitfalls to Avoid

> [!warning] 
> 1. **Sign confusion**: Remember that in standard VaR definition, we work with **losses** as positive numbers. Returns/profits are often negative losses.
> 2. **Mean matters**: For short horizons, assuming $\mu=0$ is often OK, but for longer periods, the mean scaling ($\mu T$) is important.
> 3. **Square root rule**: Only valid for i.i.d. normal returns. Not applicable if returns are correlated over time.
> 4. **Portfolio diversification**: $\sigma_{X+Y} < \sigma_X + \sigma_Y$ whenever $\rho < 1$.
> 5. **Equity vs. VaR**: Required equity equals VaR **only** when the target is zero equity. For positive target (like 5%), the formula adjusts accordingly.