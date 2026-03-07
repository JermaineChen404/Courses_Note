# Part I: Return, Volatility, and Diversification

## 1. Assets and Returns

An **asset** is a resource with economic value.

- Let **$S_t$** be the price/value of an asset at time *t*.

**Two main types:**
1.  **Risk-Free Asset:** Future value is certain.
    - *Examples:* Cash, US/German/HK Government Bonds.
2.  **Risky Asset:** Future value is random ($\ge 0$).
    - *Examples:* Stocks, ETFs, options, commodities, real estate.

### Defining Returns
Holding an asset from time *t* to *t+1*:

- **Simple Return ($r_{t+1}$):**
  $$r_{t+1} = \frac{S_{t+1} - S_t}{S_t}$$
- **Log Return ($R_{t+1}$):**
  $$R_{t+1} = \log S_{t+1} - \log S_t \quad (\text{log} = \ln)$$

> [!note] Why Use Returns?
> - Prices are unit-dependent and non-stationary (statistical properties change over time).
> - Returns are unit-free and more stationary (properties are stable over time), making them easier to model.
>
![[image.png]]

### Simple vs. Log Returns
- **Relationship:**
  $$R_{t+1} = \log(1 + r_{t+1})$$
  $$r_{t+1} = e^{R_{t+1}} - 1$$
- For **small** returns, they are approximately equal: $R_{t+1} \approx r_{t+1}$.
- Log returns are always **less than or equal** to simple returns.

![[image-1.png]]

> [!note] From Simple to Log: Motivation behind Log Return
>
> Imagine an investment that grows at a nominal annual rate $r$, but compounded $n$ times per year. Over one year, the gross return is $(1 + r/n)^n$. As compounding becomes continuous ($n \to \infty$), this tends to $e^r$.  
>
> If over a given period the actual simple return is $r$, we define the **continuously compounded rate** $R$ such that $e^R = 1+r$. Hence $R = \ln(1+r)$.
>
> Equivalently, the log return is the limit:
> $$
> R = \lim_{n \to \infty} \frac{(1+r)^{1/n} - 1}{1/n} \overset{\text{L'Hospital}}{=} \ln(1+r).
> $$
>
> So $R$ is the **instantaneous** rate that, if compounded continuously, yields the observed simple return $r$ over the period.

---

## 2. Advantages of Different Return Types

### Advantage of Simple Returns: Portfolios Aggregation

Simple returns of a portfolio are a **weighted average** of the individual asset returns.

$$r_{t+1} = \sum_{i} w_i r_{i, t+1} \quad \text{where} \quad w_i = \frac{\text{Value in asset } i}{\text{Total portfolio value}}$$

> [!abstract] Proof
> Given $S_{t} = \sum_{i} N_i S_{i,t}$, the simple return of this portfolio is
> 
> $$
> r_{t+1} = \frac{S_{t+1} - S_t}{S_t} = \frac{\sum_i N_i S_{i,t+1} - \sum_i N_{i}S_{i,t}}{\sum_i N_i S_{i,t}}
> $$
> 
> $$
> = \sum_i \frac{N_i S_{i,t}}{\sum_i N_i S_{i,t}} \times \frac{S_{i,t+1} - S_{i,t}}{S_{i,t}}
> $$
> 
> where $\frac{N_i S_{i,t}}{\sum_i N_i S_{i,t}}$ is the portfolio weight of asset $i$ and $\frac{S_{i,t+1} - S_{i,t}}{S_{i,t}}$ is the simple return of asset $i$. Hence,
> 
> $$
> r_{t+1} = \sum_i w_i r_{i,t+1}
> $$
> 

This linearity makes simple returns the natural choice for **cross‑sectional** (portfolio) analysis.

### Advantages of Log Returns

1.  **Preserves Positivity:** Even with a very negative return, the implied price stays positive ($S_{t+1} = S_t e^{R_{t+1}} > 0$). Simple returns can imply negative prices if $r < -100\%$.
2.  **Easy to Compound (Time Additivity):** The return over *T* periods is the sum of the single-period returns.
   $$R_{t:t+T} =\log S_{t+T}-\log S_{t}=\sum_{k=1}^{T}(\log S_{t+k}-\log S_{t+k-1})= \sum_{k=1}^{T} R_{t+k}$$
3. **Symmetry:** A gain of $+x$ followed by a loss of $-x$ (in log terms) returns to the original price.

4. **Statistical behavior:** Log returns are often closer to normally distributed, making them suitable for models that assume normality (e.g., CAPM, option pricing).
 

---

## 3. Expected Return and Risk

### Expected Return ($\mu$)

The measure of profitability.
- $E[r_{t+1}]$ for simple returns.
- $E[R_{t+1}]$ for log returns.

> [!warning] Important Distinction
> Because log and simple returns have a non-linear relationship:
> $$E[R_{t+1}] \neq \log(1 + E[r_{t+1}])$$
> $$E[r_{t+1}] \neq e^{E[R_{t+1}]} - 1$$

Given the linearity of the portfolio aggregation for simple returns, we have:
$$E[r_{t+1}]=\sum_{i}w_{i}E[r_{i,t+1}]$$
Given the linearity of the time aggregation for log returns, we have:
$$E[R_{t: t+T}]=\sum_{k-1}^{T}E[R_{t+k}]$$
### Risk (Volatility, $\sigma$)
The most common measure is **Standard Deviation (SD)** , a measure of dispersion.
$$\sigma = \sqrt{\text{Var}(R_{t+1})} = \sqrt{E[(R_{t+1} - \mu)^2]}$$

Noted that

$$
\begin{align}
\sigma^{2} &= E\big[(X-\mu)^{2}\big] \\
&= E[X^{2}] - 2\mu E[X] + E[\mu^2] \\
&= E[X^{2}] - \mu^{2}
\end{align}
$$
We have
$$E[R_{t+1}^2]=\mu^{2}+\sigma^2$$

---

## 4. Performance Measures

### Sharpe Ratio (SR)
A key metric for risk-adjusted return.
$$SR = \frac{\mu - R_f}{\sigma}$$
- **$\mu - R_f$:** Risk Premium (excess return over the risk-free rate).
- **$R_f$:** Risk-free rate.
- **$\sigma$:** Volatility.

Why our goal is to maximize Sharpe Ratio?
- Ans: Maximize the utility (refer to the utility function)

>[!Intuition]
>The Sharpe ratio represents the amount of risk premium an investor receives per unit of risk.
### Estimating Sharpe Ratio from Data

With historical returns $R_1, ..., R_T$:
- **Estimated Mean ($\hat{\mu}$):** Sample average of returns.
- **Estimated Variance ($\hat{\sigma}^2$):** Sample variance.
- **Estimated Sharpe Ratio ($\widehat{SR}$):**
  $$\widehat{SR} = \frac{\hat{\mu} - R_f}{\hat{\sigma}}$$

---

## 5. Investment Strategies for Lowering Risk

### Speculation vs. Investment
- **Speculation:** Positive expected return but a significant chance of loss.
- **Investment:** Positive expected return with a **comparatively small** risk of loss.

### Strategy 1: Buy-and-Hold (Time Diversification)
The idea is to hold an asset with a positive expected return over a **long horizon** to reduce risk.

**The Math (assuming i.i.d. returns with mean $\mu$ and SD $\sigma$):**
- **T-period return:** $R_{t:t+T} = \sum_{k=1}^T R_{t+k}$
- **Expected Return:** $$\mu_{t:t+T} =E\left( \sum_{k=1}^{T}R_{t+k} \right)=\sum_{k=1}^{T}E(R_{t+k})= T\mu$$
- **Standard Deviation:** $$\sigma_{t:t+T}=\sqrt{ Var\left( \sum_{k=1}^{T}R_{t+k} \right) } \overset{iid}{=} \sqrt{ \sum_{k=1}^{T}Var(R_{t+k}) }=\sqrt{T}\sigma$$
- **Sharpe Ratio:** $$SR_{t:t+T} = \frac{T\mu - T R_f}{\sqrt{T}\sigma} = \sqrt{T} \times \frac{\mu - R_f}{\sigma}$$

> [!abstract] Proof (SD scaling)
>
> The T-period log return is the sum $R_{t:t+T}=\sum_{k=1}^T R_{t+k}$. Its variance expands to
>
> $$
> \begin{align}
> \mathrm{Var}\Big(\sum_{k=1}^T R_{t+k}\Big) &= \sum_{k=1}^T \mathrm{Var}(R_{t+k}) + 2\sum_{i<j} \mathrm{Cov}(R_{t+i},R_{t+j}) \\
> &= T\sigma^2 + 2\sum_{i<j} \mathrm{Cov}(R_{t+i},R_{t+j}).
> \end{align}
> $$
>
> Under the i.i.d. assumption (or at least zero autocovariances) the cross-period covariances vanish, so Var = $T\sigma^2$ and therefore
>
> $$
> \sigma_{t:t+T} = \sqrt{\mathrm{Var}(R_{t:t+T})} = \sqrt{T}\,\sigma.
> $$

> [!success] The Time Diversification Effect
> The Sharpe ratio grows with the square root of the holding period ($\sqrt{T}$). For long horizons, the expected return grows faster than the risk.

**Statistical Interpretation:**

$$\widehat{SR}_{t:t+T} = \frac{\hat{\mu} - R_f}{\hat{\sigma} / \sqrt{T}}$$
The estimated Sharpe ratio for the buy-and-hold strategy is equivalent to a t-statistic for testing if the expected return is greater than the risk-free rate.

$$H_{0}:\mu \leq R_{f}\quad \text{vs.} \quad H_{1}:\mu>R_{f}$$


---

## 6. Empirical Evidence (S&P 500)

Do the assumptions for time diversification hold in practice?

### Assumption 1: Returns are Uncorrelated
- **Test:** Autocorrelation function (ACF) of annual S&P 500 returns (1928-2024).
- **Conclusion:** The hypothesis of zero correlation cannot be rejected. **Supported.**

### Assumption 2: Returns are Identically Distributed (Constant Mean)
- **Test:** Two-sample t-test comparing mean returns from 1928-1975 vs. 1976-2024.
- **R Output:** p-value = 0.3817
- **Conclusion:** The hypothesis of equal means cannot be rejected. **Supported for this sample.**

### Important Caveats
- This effect is **not guaranteed** for all assets (e.g., individual stocks).
- Even for the S&P 500, **past performance does not guarantee future results**. A structural change during your investment period is always a risk.
