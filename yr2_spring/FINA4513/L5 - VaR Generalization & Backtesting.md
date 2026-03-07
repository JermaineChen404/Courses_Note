# Value at Risk (VaR): Generalization & Backtesting

## Course Overview
This note covers how to calculate VaR for portfolios with multiple risk factors, sensitivity analysis, and the critical process of backtesting to validate VaR models.

---

## Part 1: Generalizing VaR to Multiple Risk Factors

### 1.1 Sensitivity Analysis: The Foundation

Before calculating risk, we must measure **exposure** – how much the portfolio value changes when risk factors move.

#### Delta (Linear Approximation)
$$ \delta_i = \frac{\partial P}{\partial x_i} $$
$$ \Delta P \approx \sum_{i=1}^n \delta_i \Delta x_i $$

> [!note] Interpretation
> $\delta_i$ tells you the dollar change in portfolio value for a **small change** in risk factor $x_i$.

### 1.2 Example 1: Equity Portfolio (page 6)

**Model for individual stocks**:
$$ S_{k,t} = S_{k,0}(1 + \beta_k R_m + \epsilon) $$

**Portfolio change given market return $R_m$**:
$$ \Delta P = \left(\sum_k N_k S_{k,0} \beta_k\right) R_m $$

Here, $\delta_{\text{market}} = \sum_k N_k S_{k,0} \beta_k$ is the portfolio's "beta exposure."

### 1.3 Example 2: Bond (pages 10-11)

**Bond price** (annual compounding):
$$ P = \sum_t \frac{c}{(1+r)^t} $$

**Sensitivity to interest rates**:
$$ \frac{dP}{dr} = -\sum_t \frac{t \cdot c}{(1+r)^{t+1}} = -\text{Duration} $$

**Numerical example** (page 11):
- 5-year bond, £100 face value, 6% rate
- Present value = £74
- $\delta_r = -352$
- Daily volatility $\sigma_r = 0.5\%$
- 99% VaR multiplier = 2.32

$$ \text{VaR} = |\delta_r| \times (2.32 \times \sigma_r) = 352 \times (2.32 \times 0.005) = 4.08 $$

> [!interpretation]
> 99% confident that daily loss from interest rate moves won't exceed £4.08.

---

## 2. Multiple Risk Factors: The General Formula (pages 7-8)

### 2.1 Portfolio Variance with Correlated Factors

For a portfolio linearly dependent on $n$ risk factors:
$$ \Delta P = \sum_{i=1}^n \delta_i \Delta x_i $$

**Variance of portfolio change**:
$$ \sigma_P^2 = \sum_{i=1}^n \sum_{j=1}^n \rho_{ij} \delta_i \delta_j \sigma_i \sigma_j $$

**Expanded form**:
$$ \sigma_P^2 = \sum_{i=1}^n \delta_i^2 \sigma_i^2 + 2\sum_{i<j} \rho_{ij} \delta_i \delta_j \sigma_i \sigma_j $$

### 2.2 Matrix Representation
$$ \sigma_P^2 = \boldsymbol{\delta}^\mathsf{T} \mathbf{C} \boldsymbol{\delta} $$
where:
- $\boldsymbol{\delta}$ = column vector of deltas
- $\mathbf{C}$ = covariance matrix of risk factor changes ($\text{cov}_{ij} = \rho_{ij}\sigma_i\sigma_j$)

> [!important] Key Insight
> Total risk is **not** the sum of individual risks – **correlations matter critically**.

---

## 3. Worked Example: Foreign-Currency Bond (pages 15-20)

### 3.1 Scenario
A US bank holds a UK bond (5-year, £100 face value, 6% discount rate).

**Risk factors**:
1. UK interest rate ($r_p$)
2. Exchange rate ($FX$, $/£)

### 3.2 Data

| Parameter | Value |
|-----------|-------|
| Cash flow $C_p$ | £100 |
| Maturity $t$ | 5 years |
| Interest rate $r_p$ | 6% |
| Daily vol of $r_p$, $\sigma_{r_p}$ | 0.5% |
| Exchange rate $FX$ | 1.6 $/£ |
| Daily vol of $FX$, $\sigma_{FX}$ | 0.02 $/£ |
| Correlation $\rho_{FX,r_p}$ | -0.6 |

### 3.3 Step 1: Compute Deltas

**Bond value in pounds**:
$$ \text{PV}_\text{pounds} = \frac{100}{(1.06)^5} = 74.73 $$

**Delta with respect to FX**:
$$ \delta_{FX} = \text{PV}_\text{pounds} = 74.73 $$
*Interpretation*: If exchange rate rises by $1/£, dollar value increases by $74.73.

**Delta with respect to UK interest rate**:
$$ \delta_{r_p} = FX \times \frac{-t \cdot C_p}{(1+r_p)^{t+1}} = 1.6 \times \frac{-5 \times 100}{(1.06)^6} = 1.6 \times (-352) = -563.2 $$
*Interpretation*: If UK rates rise by 1% (0.01), dollar value falls by $5.63.

### 3.4 Step 2: Compute Portfolio Variance

**Risk contributions** (dollar change per one standard deviation move):
- From FX: $\delta_{FX}\sigma_{FX} = 74.73 \times 0.02 = 1.4946$
- From rates: $\delta_{r_p}\sigma_{r_p} = (-563.2) \times 0.005 = -2.816$

**Apply two-factor variance formula**:
$$ 
\begin{aligned}
\sigma_P^2 &= (\delta_{FX}\sigma_{FX})^2 + (\delta_{r_p}\sigma_{r_p})^2 + 2\rho_{FX,r_p}(\delta_{FX}\sigma_{FX})(\delta_{r_p}\sigma_{r_p}) \\
&= (1.4946)^2 + (-2.816)^2 + 2(-0.6)(1.4946)(-2.816) \\
&= 2.234 + 7.930 + 2(-0.6)(-4.207) \\
&= 2.234 + 7.930 + 5.048 \\
&= 15.212
\end{aligned}
$$

$$ \sigma_P = \sqrt{15.212} = 3.90 \text{ dollars per day} $$

> [!tip] Correlation Effect
> The negative correlation (-0.6) **reduces** total risk compared to the sum of absolute contributions (1.49 + 2.82 = 4.31). This is diversification at work.

### 3.5 Step 3: Calculate 99% VaR

For normal distribution, 99% quantile = 2.326 (often rounded to 2.32):
$$ \text{VaR}_{99\%} = 2.326 \times \sigma_P = 2.326 \times 3.90 = 9.07 $$

> [!interpretation]
> The US bank can be 99% confident that it will not lose more than **$9.05** (rounded) in one day from holding this UK bond.

---

## 4. Adding Cash: Translation Invariance in Action (pages 21-22)

### Question
What happens to VaR if the bank also holds £100 of cash?

### Critical Distinction

| Cash Currency | Effect on VaR | Why? |
|---------------|---------------|------|
| **USD (domestic)** | Decreases | Cash is risk-free; adding it reduces portfolio risk (translation invariance) |
| **GBP (foreign)** | **Increases** | Cash is now exposed to FX risk; total FX delta becomes 74.7 + 100 = 174.7 |

> [!warning] Important Nuance
> Translation invariance ($\text{VaR}(L-C) = \text{VaR}(L) - C$) only applies if cash $C$ is truly risk-free in the **reporting currency**. Foreign cash still carries FX risk.

---

## 5. The 5-Step Parametric VaR Process (page 23)

1. **Define risk factors** sufficient to value the portfolio
2. **Find sensitivities** ($\delta_i$) of each instrument to each risk factor
3. **Get historical data** on risk factors to estimate:
   - Standard deviations ($\sigma_i$)
   - Correlations ($\rho_{ij}$)
4. **Estimate portfolio standard deviation** using:
   $$ \sigma_P^2 = \sum_i \sum_j \rho_{ij}\delta_i\delta_j\sigma_i\sigma_j $$
5. **Assume normality**, approximate 99% VaR as $2.32 \times \sigma_P$

---

## Part 2: Backtesting VaR Models

### 6. Why Backtest? (page 24)

| Outcome | Problem |
|---------|---------|
| Too many exceptions | **Underestimation** – regulatory capital insufficient |
| Too few exceptions | **Overestimation** – capital tied up inefficiently |

> [!quote] 
> "Neither of the above are good scenarios."

### 7. Statistical Framework (pages 25-26)

**Under the null hypothesis** (model is correct):
- Violations follow Binomial distribution: $m \sim \text{Binomial}(N, p)$
- $p = 1 - X$ (e.g., for 99% VaR, $p = 0.01$)
- Expected violations = $N \times p$

### 8. One-Sided Tests (pages 27-29)

#### Case 1: Too Few Violations ($m < Np$)
$$ P(\text{at most } m) = \text{BINOMDIST}(m, N, p, \text{TRUE}) $$
Reject at 5% level if this probability ≤ 0.05.

#### Case 2: Too Many Violations ($m > Np$)
$$ P(\text{at least } m) = 1 - \text{BINOMDIST}(m-1, N, p, \text{TRUE}) $$
Reject at 5% level if this probability ≤ 0.05.

> [!warning] Critical: Why $m-1$?
> `BINOMDIST(m, N, p, TRUE)` gives $P(\le m)$.  
> To get $P(\ge m)$, we need $1 - P(\le m-1)$.  
> Using `1 - BINOMDIST(m, N, p, TRUE)` would give $P(\ge m+1)$, **excluding** the case of exactly $m$ exceptions.

### 9. Examples (page 27-28)

**Setup**: 99% VaR, $N = 600$ days, $p = 0.01$, expected violations = 6

| Observed $m$ | Calculation | Probability | Result (5% level) |
|--------------|-------------|-------------|-------------------|
| 9 violations | $1 - \text{BINOMDIST}(8,600,0.01,1)$ | 0.152 | **Not reject** |
| 12 violations | $1 - \text{BINOMDIST}(11,600,0.01,1)$ | 0.019 | **Reject** (underestimated) |
| 1 violation | $\text{BINOMDIST}(1,600,0.01,1)$ | 0.017 | **Reject** (overestimated) |
| 3 violations | $\text{BINOMDIST}(3,600,0.01,1)$ | 0.151 | Not reject |

### 10. General Decision Rules (page 29)

| Case | Condition | Reject if |
|------|-----------|-----------|
| $m < Np$ | $\Pr\{m \le \text{\#violations}\} \le 5\%$ | $\text{BINOMDIST}(m, N, p, 1) \le 0.05$ |
| $m > Np$ | $\Pr\{m \ge \text{\#violations}\} \le 5\%$ | $1 - \text{BINOMDIST}(m-1, N, p, 1) \le 0.05$ |

---

## Concept Checklist

- [ ] Understand sensitivity analysis and delta
- [ ] Calculate VaR for single risk factor (bond, equity)
- [ ] Apply multi-factor variance formula with correlations
- [ ] Work through foreign-currency bond example
- [ ] Explain translation invariance and its limits (cash currency matters)
- [ ] Know the 5-step parametric VaR process
- [ ] Understand binomial distribution of violations
- [ ] Perform one-sided backtesting tests
- [ ] Correctly use `BINOMDIST` with $m-1$ for right-tail tests

---

## Key Formulas Summary

| Concept              | Formula                                                                    |
| -------------------- | -------------------------------------------------------------------------- |
| Linear approximation | $\Delta P = \sum \delta_i \Delta x_i$                                      |
| Portfolio variance   | $\sigma_P^2 = \sum\sum \rho_{ij}\delta_i\delta_j\sigma_i\sigma_j$          |
| Matrix form          | $\sigma_P^2 = \boldsymbol{\delta}^\mathsf{T}\mathbf{C}\boldsymbol{\delta}$ |
| Bond delta           | $\delta_r = -t \cdot C_p / (1+r)^{t+1}$ (times FX if foreign)              |
| Expected violations  | $E[m] = N \times (1-X)$                                                    |
| Left-tail test       | $P(\le m) = \text{BINOMDIST}(m, N, p, 1)$                                  |
| Right-tail test      | $P(\ge m) = 1 - \text{BINOMDIST}(m-1, N, p, 1)$                            |