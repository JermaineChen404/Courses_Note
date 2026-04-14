---
title: "ISOM4520 Class 7 - Estimating VaR and ES"
aliases:
  - "ISOM4520 Class 7"
  - "Estimating VaR and ES"
  - "Historical Simulation and Filtered Historical Simulation"
tags:
  - course/ISOM4520
  - topic/var
  - topic/expected-shortfall
  - topic/historical-simulation
  - topic/model-based-risk
  - topic/filtered-historical-simulation
  - topic/garch
  - topic/financial-econometrics
  - status/complete
source: "Class 7 lecture slides"
---
# Estimating VaR and ES

> [!abstract]
> This note studies how to **estimate** Value at Risk (VaR) and Expected Shortfall (ES) from return data.
>
> The lecture develops three main approaches:
>
> 1. **Historical Simulation (HS)** — a model-free method based directly on past returns,
> 2. **Model-Based Estimation** — assume a parametric distribution such as normal or double exponential,
> 3. **Filtered Historical Simulation (FHS)** — first remove time-varying volatility, then apply historical simulation to standardized returns.
>
> The key practical lesson is:
>
> - unconditional VaR/ES estimates often react **too slowly** to crises,
> - so in practice we often want **conditional** VaR/ES estimates,
> - FHS is designed to reflect the current volatility environment.

---

## Table of Contents

- [[#1. Recap and Motivation]]
- [[#2. Data Setup]]
- [[#3. Two Broad Approaches to Estimating VaR and ES]]
- [[#4. Historical Simulation (HS)]]
- [[#5. Historical Simulation Example: 5% VaR]]
- [[#6. Historical Simulation Example: 5% ES]]
- [[#7. HS Rolling Estimates in Practice]]
- [[#8. Pros and Cons of Historical Simulation]]
- [[#9. Model-Based Estimation]]
- [[#10. Normal Model Example]]
- [[#11. Pros and Cons of Model-Based Methods]]
- [[#12. Why Normal Tails Can Be Misleading]]
- [[#13. Double Exponential Example]]
- [[#14. Why Unconditional VaR and ES Lag in Practice]]
- [[#15. Conditional VaR and ES]]
- [[#16. Filtered Historical Simulation (FHS)]]
- [[#17. FHS Workflow]]
- [[#18. Interpreting the FHS Graphs]]
- [[#19. HS vs FHS]]
- [[#20. Exam Traps]]
- [[#21. Flashcards]]
- [[#22. Compact Formula Sheet]]

---

# 1. Recap and Motivation

The lecture starts by recalling two tail-risk measures studied earlier:

- **VaR** tells us how much we lose **at least** on a bad day,
- **ES** tells us how much we can expect to lose **on** a bad day.

Earlier classes focused on **calculating** VaR and ES when the return distribution is known.  
This class focuses on the practical problem:

> how do we estimate VaR and ES from data? 

---

# 2. Data Setup

Suppose today is time $t$, and we observe the last $n$ log returns:

$$
R_{t-n+1}, \dots, R_{t-2}, R_{t-1}, R_t.
$$

Here:

- $R_t$ is the log return from yesterday to today,
- $R_{t-1}$ is the return from the day before yesterday to yesterday,
- and so on.

The goal is to use these data to estimate current VaR and ES.

---

# 3. Two Broad Approaches to Estimating VaR and ES

The lecture divides methods into two categories:

1. **model-free methods**
2. **model-based methods**.

The main model-free method studied is:

- Historical Simulation (HS)

The main model-based methods studied are:

- normal model,
- double exponential model.

Later, the lecture combines volatility modeling with HS via:

- Filtered Historical Simulation (FHS)

---

# 4. Historical Simulation (HS)

Historical simulation estimates tail risk directly from the empirical distribution of past returns.

The HS estimator of VaR is defined as:

$$
\widehat{\mathrm{VaR}}^{HS}_\alpha(R)_t
=
(-1)\times \text{sample $\alpha$-quantile of } R_t,\dots,R_{t-n+1}.
$$

That is, to estimate VaR:

1. sort the past returns from smallest to largest,
2. find the sample $\alpha$-quantile,
3. multiply by $-1$ so the answer is expressed as a positive loss number.

---

## 4.1 Sample quantile

The lecture explains that after sorting the returns:

- the sample $\alpha$-quantile is the $(n\alpha)$-th return in the sorted list,
- if $n\alpha$ is not an integer, interpolation is needed,
- in R, the lecture uses:
- ```r
  quantile(data, probs = alpha, type = 3)
```

For large $n$, approximately:

- $100\alpha\%$ of returns lie below the sample $\alpha$-quantile,
    
- $100(1-\alpha)\%$ lie above it.
    

---

# 5. Historical Simulation Example: 5% VaR

Pages 4–5 give a concrete example with 100 daily returns (in %), then sort them from smallest to largest.

The sorted tail begins with:

- $-2.82$
    
- $-2.57$
    
- $-2.56$
    
- $-2.39$
    
- $-2.33$
    
- ...
    

Since $n=100$ and $\alpha=5\%$,

$$  
n\alpha = 100 \times 0.05 = 5.  
$$

So the 5th smallest return is the 5% quantile:

$$  
-2.33\%.  
$$

Hence

$$  
\widehat{\mathrm{VaR}}^{HS}_{5\%}(R)_t = 2.33\%.  
$$

This is exactly the lecture result.

> [!summary]  
> Historical VaR is just the empirical left-tail cutoff of past returns.

---

# 6. Historical Simulation Example: 5% ES

The lecture defines historical ES as the average loss among observations that are worse than the estimated historical VaR:

$$  
\widehat{\mathrm{ES}}^{HS}_\alpha(R)_t

\frac{1}{N_n(\alpha)}  
\sum_{i=1}^n  
R_{t-i+1}  
I_{{R_{t-i+1}<-\widehat{\mathrm{VaR}}^{HS}_\alpha(R)_t}}.  
$$

Here:

- $I_A=1$ if condition $A$ holds and 0 otherwise,
    
- $N_n(\alpha)$ is the number of returns below the VaR cutoff.
    

---

## 6.1 Example calculation

From the sorted 100-return example, the returns strictly worse than the 5% VaR of 2.33% are:

- $-2.82%$
    
- $-2.57%$
    
- $-2.56%$
    
- $-2.39%$
    

So the estimated ES is:

$$  
\widehat{\mathrm{ES}}^{HS}_{5\%}(R)_t

\frac{1}{4}(2.82\%+2.57\%+2.56\%+2.39\%)

2.585\%.  
$$

This matches the slide result.

> [!important]  
> HS-ES averages losses **beyond** the HS-VaR cutoff.

---

# 7. HS Rolling Estimates in Practice

Pages 8–9 show rolling 1%-VaR and 1%-ES estimates for S&P 500 daily returns from 2008–2024, using historical simulation with a 3-year window:

$$  
n=3\times 252.  
$$

The charts show that:

- HS-VaR moves over time,
    
- HS-ES is larger and more volatile than HS-VaR,
    
- both reflect crisis periods such as 2020.
    

This is the real-data version of applying the empirical tail formulas repeatedly through time.

---

# 8. Pros and Cons of Historical Simulation

The lecture lists the following.

## Pros

- easy to understand,
    
- easy to implement,
    
- model-free: no parametric assumption on returns is needed.
    

## Cons

- even if $n$ is large, extreme events are still rare,
    
- if $\alpha$ is very small, estimates can be very imprecise,
    
- especially for ES, the effective sample size is small because
    

$$  
N_n(\alpha)\approx n\alpha.  
$$

So for tiny tail probabilities, there may be very few observations in the relevant tail.

> [!warning]  
> HS is simple, but the data available in the extreme tail can be very thin.

---

# 9. Model-Based Estimation

To avoid relying only on extreme observations in the sample, one can assume a parametric distribution for returns.

The lecture calls this **model-based estimation**.

The basic logic is:

1. assume a distribution for $R_t$,
    
2. derive the formulas for VaR and ES under that distribution,
    
3. estimate the model parameters from data,
    
4. plug those estimates into the formulas.
    

This avoids the “tiny effective sample size” problem of HS.

---

# 10. Normal Model Example

Suppose

$$  
R_t \sim N(\mu,\sigma^2).  
$$

Then the lecture gives:

$$  
\mathrm{VaR}_\alpha(R_t)

-\mu+\Phi^{-1}(1-\alpha)\sigma,  
$$

$$  
\mathrm{ES}_\alpha(R_t)

-\mu+\frac{\phi(\Phi^{-1}(1-\alpha))}{\alpha}\sigma.  
$$

So the model-based estimators are:

$$  
\widehat{\mathrm{VaR}}^{mb}_\alpha(R)_t

-\hat\mu+\Phi^{-1}(1-\alpha)\hat\sigma,  
$$

$$  
\widehat{\mathrm{ES}}^{mb}_\alpha(R)_t

-\hat\mu+\frac{\phi(\Phi^{-1}(1-\alpha))}{\alpha}\hat\sigma.  
$$

Here (\hat\mu) and (\hat\sigma) are estimators of the mean and standard deviation.

---

## 10.1 Parameter estimation

The lecture suggests using:

$$  
\hat\mu = \frac1n\sum_{i=1}^n R_{t-i+1},  
$$

and

$$  
\hat\sigma^2

S^2

\frac{1}{n-1}\sum_{i=1}^n (R_{t-i+1}-\hat\mu)^2.  
$$

That is, the sample mean and sample variance.

---

# 11. Pros and Cons of Model-Based Methods

## Pros

- model parameters such as $\mu$ and $\sigma$ can usually be estimated much more precisely,
    
- there is no dramatic reduction in effective sample size for ES estimation.
    

## Cons

- estimates are only as good as the assumed return distribution,
    
- if the distributional assumption is wrong, the estimated VaR and ES can be highly misleading.
    

> [!important]  
> Model-based methods trade robustness for statistical efficiency.

---

# 12. Why Normal Tails Can Be Misleading

Page 14 compares large historical S&P 500 gains and losses with what a normal model would imply.

Using rough estimates

$$  
\hat\mu \approx \frac{0.1}{252},  
\qquad  
\hat\sigma \approx \frac{0.2}{\sqrt{252}},  
$$

and

$$  
\alpha=\frac{10}{252\times 100},  
$$

the lecture gets:

$$  
\widehat{\mathrm{VaR}}^{mb}_\alpha(R)_t = 4.19%,  
$$

$$  
\widehat{\mathrm{ES}}^{mb}_\alpha(R)_t = 4.51%.  
$$

But the table on the same slide shows realized daily losses as large as:

- (-20.47%) in 1987,
    
- (-12.34%) in 1929,
    
- (-11.98%) in 2020.
    

So the lesson is:

> normal tails are too thin to describe the most extreme market losses.

---

# 13. Double Exponential Example

The lecture next assumes daily log returns follow a double exponential (Laplace-type) distribution:

$$  
f(x)=\frac{1}{2\sigma}e^{-|x|/\sigma}, \qquad x\in\mathbb R.  
$$

The task is to estimate VaR and ES using the sample variance of daily returns over the last 100 years, with volatility again around

$$  
\frac{0.2}{\sqrt{252}}.  
$$

---

## 13.1 Step 1: relate variance to $\sigma$

The lecture derives:

$$  
\mathrm{Var}(X)=2\sigma^2.  
$$

Therefore, if the sample variance is $S^2$, then

$$  
\hat\sigma=\sqrt{\frac{S^2}{2}}.  
$$

This is the estimator used on the slides.

---

## 13.2 Step 2: plug into VaR and ES formulas

Using the formulas from the previous class:

$$  
\widehat{\mathrm{VaR}}^{mb}_\alpha(R)_t

-\hat\sigma \log(2\alpha),  
$$

$$  
\widehat{\mathrm{ES}}^{mb}_\alpha(R)_t

\hat\sigma\big(1-\log(2\alpha)\big).  
$$

The lecture gets:

$$  
\widehat{\mathrm{VaR}}^{mb}_\alpha(R)_t = 6.36%,  
$$

$$  
\widehat{\mathrm{ES}}^{mb}_\alpha(R)_t = 7.25%.  
$$

These are much larger than under the normal model, reflecting the heavier tails of the double exponential distribution.

> [!summary]  
> Heavier-tailed models produce larger VaR and ES estimates.

---

# 14. Why Unconditional VaR and ES Lag in Practice

The lecture then makes an important practical point:

- standard deviation,
    
- VaR,
    
- ES
    

all share one disadvantage when defined unconditionally:

> they do not take current information into account.

Pages 19–21 show two empirical problems around crisis periods:

1. **overestimation after a crisis**  
    VaR stays elevated for too long after the crisis has passed.
    
2. **underestimation at the start of a crisis**  
    VaR does not rise quickly enough when turmoil begins.
    

The plots on pages 20–21 make this especially clear:

- around the financial crisis, VaR stays high for a long time even as prices recover,
    
- at the beginning of a crisis, HS-based VaR responds too slowly to the sudden jump in risk.
    

> [!important]  
> Unconditional VaR/ES are often **lagging indicators** of risk.

---

# 15. Conditional VaR and ES

The lecture emphasizes that this lag is not only a drawback of HS or model-based estimation per se.

Rather, it reflects a deeper issue:

> unconditional VaR/ES may not be the risk measures we really want in practice.

In practice, we often want:

- VaR conditional on the current volatility state,
    
- ES conditional on the current market environment.
    

This motivates **Filtered Historical Simulation (FHS)**.

---

# 16. Filtered Historical Simulation (FHS)

The starting point is the basic return model:

$$  
R_t=\sigma_t z_t.  
$$

Assume we have estimators:

- $\hat\sigma_t$ for volatility,
    
- $\hat z_t$ for standardized returns.
    

The lecture notes that a GARCH model can provide such estimators.

The key idea of FHS is:

> apply historical simulation not to raw returns (R_t), but to standardized returns (\hat z_t).

---

# 17. FHS Workflow

The lecture’s workflow is:

## Step 1: estimate volatility and standardized returns

Using a model such as GARCH(1,1), estimate:

$$  
\hat z_t = \frac{R_t}{\hat\sigma_t}.  
$$

---

## Step 2: apply HS to $\hat z_t$

Compute historical simulation VaR and ES on the standardized return series:

$$  
\widehat{\mathrm{VaR}}^{HS}_\alpha(z)_t,  
\qquad  
\widehat{\mathrm{ES}}^{HS}_\alpha(z)_t.  
$$

---

## Step 3: rescale by current volatility

Then define the FHS estimators:

$$  
\widehat{\mathrm{VaR}}^{FHS}_\alpha(R)_t

\hat\sigma_t \widehat{\mathrm{VaR}}^{HS}_\alpha(z)_t,  
$$

$$  
\widehat{\mathrm{ES}}^{FHS}_\alpha(R)_t

\hat\sigma_t \widehat{\mathrm{ES}}^{HS}_\alpha(z)_t.  
$$

These formulas are given explicitly in the lecture.

---

## 17.1 Interpretation

Because FHS multiplies by the current volatility estimate ($\hat\sigma_t$), the resulting VaR/ES estimates automatically respond to the current market regime.

So:

- when volatility is high, FHS-VaR and FHS-ES rise quickly,
    
- when volatility is low, they fall quickly.
    

> [!summary]  
> FHS is a volatility-adjusted version of historical simulation.

---

# 18. Interpreting the FHS Graphs

Pages 24–28 illustrate the FHS procedure visually.

## Page 24: raw returns, annualized volatility, standardized returns

This slide shows:

- raw log returns,
    
- annualized volatility,
    
- standardized returns.
    

The idea is that standardized returns remove the time-varying volatility scale.

---

## Page 26: standardized returns from GARCH

The standardized return series (\hat z_t) looks much more homogeneous over time than raw returns. This is exactly the point of filtering first.

---

## Page 27: HS on standardized returns

The lecture uses a moving window of 3 years:

$$  
n=3\times 252.  
$$

Then HS is applied to:

$$  
\hat z_t, \hat z_{t-1}, \dots, \hat z_{t-n+1}.  
$$

This yields

$$  
\widehat{\mathrm{VaR}}^{HS}_\alpha(z)_t.  
$$

The graph on page 27 shows the resulting risk estimate for standardized returns.

---

## Page 28: scale by current volatility

The lecture then multiplies the standardized-return VaR estimate by (\hat\sigma_t) to obtain

$$  
\widehat{\mathrm{VaR}}^{FHS}_\alpha(R)_t.  
$$

The page 28 graph shows that the resulting VaR series is much more reactive to current conditions.

---

# 19. HS vs FHS

Pages 29–30 compare HS and FHS directly.

## 19.1 Broad comparison

- **HS** produces a relatively smooth VaR estimate that changes slowly,
    
- **FHS** produces a VaR estimate that responds more strongly to volatility spikes.
    

## 19.2 Crisis onset comparison

Page 30 is especially important. It compares:

- log returns,
    
- HS-based VaR,
    
- FHS-based VaR
    

over a short crisis window.

The key visual conclusion is:

> FHS rises much faster at the beginning of a crisis than HS.

So FHS addresses one of the main practical weaknesses of unconditional HS.

---

# 20. Exam Traps

> [!warning]  
> These are common mistakes.

## Trap 1: Historical simulation means “no assumptions at all”

Not exactly.

HS is model-free in the sense of **not assuming a parametric return distribution**, but it still assumes that past empirical returns are informative for present risk.

---

## Trap 2: HS-ES uses the same sample size as HS-VaR

False.

HS-ES uses only the returns beyond the VaR cutoff, so its effective sample size is roughly

$$  
n\alpha.  
$$

This can be very small for small $(\alpha$).

---

## Trap 3: Model-based methods are always better because they use formulas

False.

They can be more statistically precise, but if the assumed distribution is wrong, the estimates may be very misleading.

---

## Trap 4: Normal and heavy-tailed models should give similar VaR and ES

False.

Heavier-tailed models produce larger tail-risk estimates.

---

## Trap 5: VaR and ES estimated from long windows always reflect current risk well

False.

The lecture shows that unconditional VaR/ES often react too slowly to crises and stay too high for too long afterward.

---

## Trap 6: FHS just means “do HS on returns after GARCH”

Not quite.

The correct procedure is:

1. standardize returns,
    
2. do HS on standardized returns,
    
3. rescale by current estimated volatility.
    

---

# 21. Flashcards

## Historical Simulation

**Q:** How is historical simulation VaR estimated?  
**A:** Take the empirical (\alpha)-quantile of past returns and multiply by (-1).

**Q:** How is historical simulation ES estimated?  
**A:** Average the losses that exceed the estimated HS-VaR cutoff.

---

## Model-Based Estimation

**Q:** What is the idea of model-based estimation?  
**A:** Assume a parametric return distribution, estimate its parameters, and plug them into the VaR/ES formulas.

**Q:** Main advantage?  
**A:** Tail-risk estimates can be statistically more precise.

**Q:** Main drawback?  
**A:** Results can be misleading if the model assumption is wrong.

---

## FHS

**Q:** What is the starting model for FHS?  
**A:**  
$$  
R_t=\sigma_t z_t.  
$$

**Q:** What does FHS apply HS to?  
**A:** Standardized returns (\hat z_t), not raw returns.

# **Q:** How is FHS-VaR computed?  
**A:**  
$$  
\widehat{\mathrm{VaR}}^{FHS}_\alpha(R)_t

\hat\sigma_t \widehat{\mathrm{VaR}}^{HS}_\alpha(z)_t.  
$$

**Q:** Why is FHS more responsive?  
**A:** Because it scales risk estimates by the current volatility estimate (\hat\sigma_t).

---

# 22. Compact Formula Sheet

## Historical Simulation

Historical VaR:

$$  
\widehat{\mathrm{VaR}}^{HS}_\alpha(R)_t

(-1)\times \text{sample $\alpha$-quantile of } R_t,\dots,R_{t-n+1}  
$$

Historical ES:

$$  
\widehat{\mathrm{ES}}^{HS}_\alpha(R)_t

\frac{1}{N_n(\alpha)}  
\sum_{i=1}^n  
R_{t-i+1}  
I_{{R_{t-i+1}<-\widehat{\mathrm{VaR}}^{HS}_\alpha(R)_t}}  
$$

---

## Normal Model

If

$$  
R_t\sim N(\mu,\sigma^2),  
$$

then

$$  
\mathrm{VaR}_\alpha(R_t)

-\mu+\Phi^{-1}(1-\alpha)\sigma  
$$

$$  
\mathrm{ES}_\alpha(R_t)

-\mu+\frac{\phi(\Phi^{-1}(1-\alpha))}{\alpha}\sigma  
$$

Plug-in estimators:

$$  
\widehat{\mathrm{VaR}}^{mb}_\alpha(R)_t

-\hat\mu+\Phi^{-1}(1-\alpha)\hat\sigma  
$$

$$  
\widehat{\mathrm{ES}}^{mb}_\alpha(R)_t

-\hat\mu+\frac{\phi(\Phi^{-1}(1-\alpha))}{\alpha}\hat\sigma  
$$

---

## Double Exponential Model

If

$$  
f(x)=\frac{1}{2\sigma}e^{-|x|/\sigma},  
$$

then

$$  
\mathrm{Var}(X)=2\sigma^2  
$$

so

$$  
\hat\sigma=\sqrt{\frac{S^2}{2}}  
$$

and

 $$  
\widehat{\mathrm{VaR}}^{mb}_\alpha(R)_t

-\hat\sigma\log(2\alpha)  
$$

$$  
\widehat{\mathrm{ES}}^{mb}_\alpha(R)_t

\hat\sigma\big(1-\log(2\alpha)\big)  
$$

---

## Filtered Historical Simulation

Standardized returns:

$$  
\hat z_t=\frac{R_t}{\hat\sigma_t}  
$$

FHS-VaR:

$$  
\widehat{\mathrm{VaR}}^{FHS}_\alpha(R)_t

\hat\sigma_t \widehat{\mathrm{VaR}}^{HS}_\alpha(z)_t  
$$

FHS-ES:

$$  
\widehat{\mathrm{ES}}^{FHS}_\alpha(R)_t

\hat\sigma_t \widehat{\mathrm{ES}}^{HS}_\alpha(z)_t  
$$

---

# 23. Big Picture Summary

> [!summary]  
> Class 7 is about estimating tail risk from return data.
> 
> - HS is simple, intuitive, and model-free, but can be noisy in the tail.
>     
> - Model-based methods can be more precise, but are only as good as the assumed distribution.
>     
> - Normal models often understate extreme market risk.
>     
> - Heavy-tailed models give larger, more realistic VaR/ES estimates.
>     
> - Unconditional VaR/ES are lagging indicators of risk.
>     
> - FHS improves responsiveness by combining volatility filtering with historical simulation.
>     

---

# 24. Suggested Obsidian Links

```text
[[Value at Risk]]
[[Expected Shortfall]]
[[Historical Simulation]]
[[Model-Based Risk Estimation]]
[[Normal Distribution]]
[[Double Exponential Distribution]]
[[Tail Risk]]
[[Conditional VaR]]
[[Conditional ES]]
[[Filtered Historical Simulation]]
[[GARCH(1,1)]]
[[Standardized Returns]]
[[Volatility Filtering]]
[[Financial Econometrics]]
```