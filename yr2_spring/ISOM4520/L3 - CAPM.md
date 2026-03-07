# Capital Asset Pricing Model (CAPM)

## 1. From MPT to CAPM

- MPT gives a theoretical framework but requires many inputs.
- **CAPM** (Sharpe, 1964) adds equilibrium assumptions to make MPT operational.
- It is one of the most influential models in finance (Nobel Prize 1990 for William Sharpe).

### Assumptions
- Investors are rational and follow MPT (mean‑variance optimization).
- Homogeneous expectations: everyone uses the same list of expected returns, variances, and covariances.
- Single‑period horizon.
- All assets are tradable, infinitely divisible, no frictions (taxes, transaction costs, short‑sale constraints).

---

## 2. The Market Portfolio

- Because all investors have identical expectations, they all choose the **same** tangency portfolio.
- In equilibrium, **supply equals demand**:
  - Total market value of all risky assets = total wealth invested in the tangency portfolio.
  - Weight of asset $i$ in the tangency portfolio equals its relative market value:
    $$w_i = \frac{V_i}{\sum_j V_j} \quad\text{(value‑weighted)}$$

- **Definition:** The **market portfolio** is the value‑weighted portfolio of **all** risky assets in the economy.
- **First main result of CAPM:** The tangency portfolio = the market portfolio.
  - All investors hold the market portfolio combined with the risk‑free asset.

> [!important] Practical implication
> The only rational risky investment is a **broad market index fund** (e.g., S&P 500 ETF). Any stock picking is suboptimal according to CAPM.

- **Capital Market Line (CML):** the CAL of the market portfolio. It shows the best possible risk‑return combinations available to investors.

---

## 3. Security Market Line (SML) – Pricing Individual Assets

CAPM also tells us how expected returns of individual assets are determined.

**Second main result:** The expected excess return (risk premium) of any asset is proportional to its **beta** with the market.
  $$E[r_i] - r_f = \beta_i \big( E[r_M] - r_f \big)$$
  where
  $$\beta_i = \frac{\mathrm{Cov}(r_i, r_M)}{\mathrm{Var}(r_M)}$$

- $\beta_i$ measures the asset’s **sensitivity to market movements**.
- Only **systematic risk** (market risk) is priced; idiosyncratic risk earns no premium.

> [!note] Derivation insight
> The formula comes from the condition that the market portfolio already has the highest Sharpe ratio. Any deviation (tilting toward a stock) would lower the Sharpe ratio unless the stock’s expected excess return exactly matches its beta times the market risk premium.

- Graphically, the SML plots expected return against beta. All assets lie on this line in equilibrium.

---

## 4. Estimating Beta: The Single‑Index Model

The CAPM relationship suggests a linear regression model:
  $$r_{i,t} - r_f = \alpha_i + \beta_i (r_{M,t} - r_f) + \epsilon_{i,t}$$

- $\alpha_i$: intercept (should be zero under CAPM).
- $\beta_i$: slope coefficient = estimate of beta.
- $\epsilon_{i,t}$: idiosyncratic shock (mean zero, uncorrelated with market).

**OLS estimators:**
  $$\hat{\beta}_i = \frac{\mathrm{Cov}(r_i - r_f,\; r_M - r_f)}{\mathrm{Var}(r_M - r_f)}$$
  $$\hat{\alpha}_i = \overline{(r_i - r_f)} - \hat{\beta}_i \overline{(r_M - r_f)}$$

- $R^2$ measures the proportion of total risk that is systematic: $R^2 = \frac{\text{systematic variance}}{\text{total variance}}$.

> [!example] Apple (AAPL) vs S&P 500 (monthly data 2015–2024)
> ```
> Coefficients:
>             Estimate Std. Error t value Pr(>|t|)
> (Intercept) 0.008881   0.005416   1.64    0.104
> sp.ret      1.274654   0.113279  11.25   <2e-16 ***
> ```
> - $\hat{\beta} \approx 1.27$ (AAPL is more volatile than the market).
> - $\hat{\alpha} \approx 0.009$ (not statistically significant, p=0.104 → cannot reject $\alpha=0$).
> - $R^2 \approx 0.52$ (52% of AAPL’s variance is systematic).

---

## 5. Does CAPM Hold in Practice? – Empirical Evidence

### Roll’s Critique (1977)
- The true market portfolio is **unobservable** (includes real estate, human capital, private companies, etc.).
- Any test of CAPM is actually a test of the chosen **proxy** (e.g., S&P 500). Rejection may be due to a poor proxy, not CAPM itself.

### Testing for $\alpha \neq 0$
- For an individual stock, a t‑test on $\hat{\alpha}$ tells whether it has earned abnormal returns after adjusting for market risk.
- **Problem:** If you pick a stock *after* seeing its stellar performance (e.g., NVIDIA), a significant $\alpha$ is expected by chance (data‑snooping bias).

> [!example] NVIDIA (NVDA) 2015–2024
> ```
> (Intercept) 0.04074 ***  (p = 0.00012)
> ```
> This suggests a positive alpha of about 4% per month. But if we use data from **2005–2014** (before the huge rise):
> ```
> (Intercept) 0.00944 (p = 0.388)
> ```
> Alpha disappears. Hindsight selection creates the illusion of alpha.

- **Ex‑ante alpha** is what matters for active management, and it’s very hard to find.

### Mutual Fund Performance
- Studies (e.g., Jensen 1968, Malkiel 1995) show that most actively managed funds **do not** have statistically significant positive alphas.
- After fees, many underperform the market.

> [!quote] Warren Buffett’s bet (2008–2017)
> A low‑cost S&P 500 index fund outperformed a portfolio of hedge funds hand‑picked by a fund manager.  
> [Buffett’s letter](https://www.berkshirehathaway.com/letters/20161tr.pdf)

---

## 6. Factor Models and the “Zoo” of Factors

- Most researchers agree that a single market factor is insufficient.
- Multi‑factor models add extra sources of systematic risk:
  $$r_{i} - r_f = \alpha_i + \beta_{i,M} F_M + \beta_{i,1} F_1 + \beta_{i,2} F_2 + \dots$$
- **Examples of factors:**
  - SMB (Small minus Big – size)
  - HML (High minus Low – value)
  - RMW (Robust minus Weak – profitability)
  - CMA (Conservative minus Aggressive – investment)
  - MOM (Momentum)
  - STR/LTR (short‑/long‑term reversal)
  - BAB (Betting against beta)
  - QMJ (Quality minus Junk)

- Over 200 factors have been proposed. Many are weak, time‑varying, or spurious.

---

## 7. Why Might CAPM Fail in Reality?

- Assumptions are violated:
  - Investors care about more than mean and variance.
  - Heterogeneous expectations.
  - Different horizons.
  - Frictions (taxes, transaction costs, short‑sale constraints).
  - Non‑tradable assets.
  - **Behavioral biases** (see below).

---

## 8. Behavioral Finance – A Challenge to Rationality

- **Memory bias:** Overweight recent events, ignore long‑term averages.
- **Overconfidence:** Overestimate own skill → excessive trading.
  - Men trade more than women and earn lower net returns.
  - “Trading is hazardous to your wealth” (Barber & Odean).
- **Representativeness:** See patterns in random data (hot‑hand fallacy).
- **Conservatism:** Slow to update beliefs → underreaction to news.
- **Other biases:** loss aversion, mental accounting, framing, disposition effect, regret avoidance.

These biases can lead to persistent mispricing and may explain why some factors earn premiums.

---

## 9. Practical Takeaways

- **If you have no special information or skill:** be a CAPM investor – buy a diversified low‑cost market index fund and combine with risk‑free assets according to your risk tolerance.
- **If you try to beat the market:** be aware that it is extremely difficult, especially after costs.
- The Grossman‑Stiglitz paradox: There must be some incentives for information gathering, otherwise markets would be inefficient. But for most individuals, passive investing remains the optimal choice.

> [!summary] CAPM in a nutshell
> 1. The market portfolio is the only risky portfolio anyone should hold.
> 2. An asset’s expected return depends only on its beta with the market.
> 3. Alpha (abnormal return) should be zero in equilibrium.
> 4. In practice, the model is a useful baseline, but deviations exist.