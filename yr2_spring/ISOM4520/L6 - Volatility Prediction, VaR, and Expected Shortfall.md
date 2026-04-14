---
title: "ISOM4520 Class 6 - Volatility Prediction, VaR, and Expected Shortfall"
aliases:
  - "ISOM4520 Class 6"
  - "Volatility Prediction and Tail Risk"
  - "VaR and Expected Shortfall"
tags:
  - course/ISOM4520
  - topic/volatility-forecasting
  - topic/garch
  - topic/var
  - topic/expected-shortfall
  - topic/tail-risk
  - topic/financial-econometrics
  - status/complete
source: "Class 6 lecture slides"
---
# Volatility Prediction, VaR, and Expected Shortfall

> [!abstract]
> This note has two main parts:
>
> 1. **Volatility prediction**: how to forecast future conditional variance in the GARCH model using conditional expectations.
> 2. **Tail risk**: why variance is not enough for extreme events, and how to quantify downside risk using [[Value at Risk]] (VaR) and [[Expected Shortfall]] (ES).
>
> The key ideas are:
>
> - the best predictor under mean squared error is a conditional expectation,
> - returns themselves are often hard to predict,
> - but volatility is predictable,
> - standard deviation captures “normal-period” risk,
> - VaR and ES are designed to measure **tail risk**.
>
> Source: Class 6 slides. :contentReference[oaicite:0]{index=0}

---

## Table of Contents

- [[#1. Recap: The GARCH Return Model]]
- [[#2. Why Prediction Means Conditional Expectation]]
- [[#3. Best Predictor Under Mean Squared Error]]
- [[#4. Conditional Prediction in Time Series]]
- [[#5. Examples of One-Step-Ahead Prediction]]
- [[#6. Why Returns Are Hard to Predict but Volatility Is Predictable]]
- [[#7. One-Step-Ahead Volatility Prediction in GARCH]]
- [[#8. k-Step-Ahead Volatility Prediction in GARCH]]
- [[#9. Implementation and Forecast Graph]]
- [[#10. Tail Risk]]
- [[#11. Why Normality Fails for Daily Returns]]
- [[#12. Value at Risk (VaR)]]
- [[#13. Expected Shortfall (ES)]]
- [[#14. Computing VaR in Practice]]
- [[#15. Analytical VaR for the Normal Distribution]]
- [[#16. General ES Formula]]
- [[#17. ES for the Normal Distribution]]
- [[#18. Double Exponential Example: VaR]]
- [[#19. Double Exponential Example: ES]]
- [[#20. Exam Traps]]
- [[#21. Flashcards]]
- [[#22. Compact Formula Sheet]]

---

# 1. Recap: The GARCH Return Model

The lecture begins by recalling the standard return model:

$$
R_t = \mu_t + \sigma_t z_t, \qquad t=1,\dots,T,
$$

where: :contentReference[oaicite:1]{index=1}

- $\mu_t$ and $\sigma_t^2$ depend only on information available up to time $t-1$,
- $z_t \sim IID(0,1)$,
- $z_t$ is independent of all random variables in $\mathcal{F}_{t-1}$.

Hence,

$$
E_{t-1}(R_t)=\mu_t,
\qquad
\mathrm{Var}_{t-1}(R_t)=\sigma_t^2.
$$

As in Class 5, the lecture assumes

$$
\mu_t=0
$$

for simplicity.

---

## 1.1 GARCH(1,1) recap

The GARCH(1,1) model is

$$
R_t=\sigma_t z_t,
$$

$$
\sigma_t^2=(1-\alpha-\beta)\sigma^2+\alpha R_{t-1}^2+\beta \sigma_{t-1}^2.
$$

Interpretation: today’s conditional variance is a weighted average of:

- the long-run variance $\sigma^2$,
- yesterday’s squared return $R_{t-1}^2$,
- yesterday’s conditional variance $\sigma_{t-1}^2$.

Equivalently, one may write

$$
\omega=(1-\alpha-\beta)\sigma^2
$$

and express the model as

$$
\sigma_t^2=\omega+\alpha R_{t-1}^2+\beta \sigma_{t-1}^2.
$$

---

## 1.2 Empirical recap

The lecture emphasizes two empirical points:

- log returns clearly show **conditional heteroscedasticity**,
- GARCH captures the autocorrelation in squared returns very well.

The plots on pages 6–8 show:

- raw S&P 500 log returns,
- estimated annualized volatility,
- standardized returns,
- ACFs of standardized returns and standardized squared returns.

The intended takeaway is:

> After scaling by fitted volatility, most of the dependence in return magnitudes disappears.

---

# 2. Conditional Expectation as the Best Possible Prediction

The lecture next asks a basic question:

> If you want to predict a random variable $X$, what is the “best” possible prediction?

There are many ways to define “best,” but the most common is to minimize **mean squared error** (MSE):

$$
E\big((X-\hat X)^2\big).
$$

In dynamic settings, we typically want to use current information. Then the relevant objective is **conditional MSE**:

$$
E_t\big((X-\hat X)^2\big).
$$

The lecture’s key message is:

> Prediction means computing a conditional expectation based on current information.

---

# 3. Best Predictor Under Mean Squared Error

Let $x$ be a constant predictor for $X$ and define

$$
f(x)=E\big((X-x)^2\big).
$$

To minimize this, differentiate:

$$
f'(x)=E(-2(X-x))=-2E(X)+2x.
$$

Set $f'(x)=0$:

$$
-2E(X)+2x=0
\quad \Rightarrow \quad
x=E(X).
$$

So the best constant predictor under MSE is

$$
\hat X = E(X).
$$

> [!important]
> Under squared-error loss, the expected value is the optimal predictor.

---

# 4. Conditional Prediction in Time Series

In reality, we do not predict using only the unconditional distribution. We predict using the information currently available.

So instead of minimizing

$$
E\big((X-\hat X)^2\big),
$$

we minimize

$$
E_t\big((X-\hat X)^2\big).
$$

The lecture states that the best predictor is then

$$
E_t(X).
$$

So in time series,

> “prediction” means conditional expectation with respect to the current information set. 

---

# 5. Examples of One-Step-Ahead Prediction

The lecture gives several examples of predicting $X_t$ at time $t-1$.

---

## 5.1 Return model

Suppose

$$
X_t=\sigma_t z_t.
$$

Then

$$
E_{t-1}(X_t)=E_{t-1}(\sigma_t z_t)=\sigma_t E_{t-1}(z_t).
$$

Since $\sigma_t$ is known at time $t-1$ and $z_t$ is independent of the past with mean zero,

$$
E_{t-1}(z_t)=E(z_t)=0.
$$

Hence

$$
E_{t-1}(X_t)=0.
$$

> [!summary]
> Asset returns are not predictable in the mean.

---

## 5.2 MA(1) process

Suppose

$$
X_t=\varepsilon_t+\theta \varepsilon_{t-1}.
$$

Then at time $t-1$,

$$
E_{t-1}(X_t)=E_{t-1}(\varepsilon_t+\theta\varepsilon_{t-1})
=E(\varepsilon_t)+\theta\varepsilon_{t-1}
=\theta\varepsilon_{t-1}.
$$

So the process is predictable.

---

## 5.3 AR(1) process

Suppose

$$
X_t=\phi X_{t-1}+\varepsilon_t.
$$

Then

$$
E_{t-1}(X_t)=E_{t-1}(\phi X_{t-1}+\varepsilon_t)
=\phi X_{t-1}+E(\varepsilon_t)
=\phi X_{t-1}.
$$

So the AR(1) is also predictable.

---

## 5.4 Interpretation

The lecture summarizes the contrast clearly:

- returns are hard to predict,
- MA and AR processes are predictable because they are correlated time series.

---

# 6. Why Returns Are Hard to Predict but Volatility Is Predictable

The slides state:

- we cannot predict asset returns,
- but we can predict squared returns / volatility.

This matches the central stylized facts from Class 4 and Class 5:

- returns are roughly uncorrelated,
- squared returns are persistent,
- therefore conditional variance is forecastable.

So the main forecasting object in financial econometrics is often not

$$
E_{t-1}(R_t),
$$

but rather

$$
E_{t-1}(R_t^2)
\quad \text{or} \quad
E_{t-1}(\sigma_t^2).
$$

---

# 7. One-Step-Ahead Volatility Prediction in GARCH

Start from the GARCH(1,1) model:

$$
\sigma_t^2=(1-\alpha-\beta)\sigma^2+\alpha R_{t-1}^2+\beta \sigma_{t-1}^2.
$$

We want the one-step-ahead predictor of future conditional variance:

$$
E_{t-1}(\sigma_{t+1}^2).
$$

From the model,

$$
\sigma_{t+1}^2=(1-\alpha-\beta)\sigma^2+\alpha R_t^2+\beta \sigma_t^2.
$$

Take conditional expectation given $\mathcal F_{t-1}$:

$$
E_{t-1}(\sigma_{t+1}^2)
=
(1-\alpha-\beta)\sigma^2+\alpha E_{t-1}(R_t^2)+\beta E_{t-1}(\sigma_t^2).
$$

Now

$$
R_t^2=\sigma_t^2 z_t^2.
$$

So

$$
E_{t-1}(R_t^2)
=
E_{t-1}(\sigma_t^2 z_t^2)
=
\sigma_t^2 E_{t-1}(z_t^2).
$$

Since $\sigma_t^2$ is known at time $t-1$ and $E(z_t^2)=1$,

$$
E_{t-1}(R_t^2)=\sigma_t^2.
$$

Also,

$$
E_{t-1}(\sigma_t^2)=\sigma_t^2
$$

because $\sigma_t^2$ is already known at time $t-1$.

Therefore,

$$
E_{t-1}(\sigma_{t+1}^2)
=
(1-\alpha-\beta)\sigma^2+(\alpha+\beta)\sigma_t^2.
$$


> [!important]
> The one-step-ahead forecast is a weighted average of:
>
> - current conditional variance $\sigma_t^2$,
> - long-run variance $\sigma^2$,
>
> with weights $\alpha+\beta$ and $1-\alpha-\beta$.

---

# 8. k-Step-Ahead Volatility Prediction in GARCH

The lecture extends the argument to $k$ steps ahead and derives the recursion:

$$
E_{t-1}(\sigma_{t+k}^2)
=
(1-\alpha-\beta)\sigma^2
+
(\alpha+\beta)E_{t-1}(\sigma_{t+k-1}^2).
$$

This says:

> each forecast is a weighted average of the long-run variance and the previous forecast.

The explicit formula is

$$
E_{t-1}(\sigma_{t+k}^2)
=
\big(1-(\alpha+\beta)^k\big)\sigma^2 + (\alpha+\beta)^k \sigma_t^2.
$$

For recurrence relations, refer to [[Recurrence relations quick review| a quick review]].


---

## 8.1 Interpretation

As $k$ increases:

- if $\alpha+\beta<1$, then $(\alpha+\beta)^k \to 0$,
- so the $k$-step-ahead volatility forecast converges to the long-run variance:

$$
E_{t-1}(\sigma_{t+k}^2)\to \sigma^2.
$$

So GARCH implies:

- short-horizon forecasts depend strongly on current volatility,
- long-horizon forecasts revert to the long-run level.

> [!summary]
> Volatility is mean-reverting in forecast space.

---

# 9. Implementation and Forecast Graph

The lecture then shows how to produce GARCH volatility forecasts in R.

The code on the slide is:

```r
model <- garchFit(~ garch(1, 1), logret, include.mean = FALSE, trace = FALSE)
pred <- predict(model, n.ahead=252)
plot(pred$standardDeviation*sqrt(252), xlab="k", ylab="",
main="k-Step Ahead Forecast of Volatility")
```

## 9.1 What the code does

- `garchFit(...)` estimates a GARCH(1,1) model on the return series,
    
- `predict(model, n.ahead=252)` generates forecasts for the next 252 trading days,
    
- `pred$standardDeviation*sqrt(252)` annualizes the predicted daily volatility.
    

## 9.2 What the graph shows

The graph on page 27 shows the **k-step-ahead forecast of volatility** rising toward a long-run level.

This is exactly what the formula predicts:

$$  
E_{t-1}(\sigma_{t+k}^2)

\big(1-(\alpha+\beta)^k\big)\sigma^2 + (\alpha+\beta)^k \sigma_t^2.  
$$

If current volatility is below long-run volatility, the forecast curve rises upward; if it were above long-run volatility, it would slope downward.

> [!note]  
> The graph is a visual illustration of volatility mean reversion.

---

# 10. Tail Risk 

The lecture then moves from volatility forecasting to **tail risk**.

So far, risk has mostly been measured by:

- variance,
    
- standard deviation.
    

But standard deviation mainly captures risk during **normal periods**.

Tail risk refers to risk due to **extreme events**, especially during crises.

---

## 10.1 Why tail risk matters

The slide on page 31 lists some of the largest daily gains and losses of the S&P 500 and notes that these should be compared with a standard daily return volatility of about 1–2%.

This highlights that:

- extreme returns can be many standard deviations away from the mean,
    
- crisis-period losses are much larger than what “normal times” intuition suggests.
    

---

# 11. Why Normality Fails for Daily Returns

The lecture argues that daily returns should **not** be modeled as normal if the goal is to capture tail risk.

The slide gives normal tail probabilities:

- beyond $3\sigma$: about 0.27%
    
- beyond $4\sigma$: about 0.01%
    
- beyond $5\sigma$: essentially never in practical time scales.
    

But financial data show extreme daily moves much more often than that.

The density plot of S&P 500 daily log returns (page 34) visually shows a distribution with fat tails relative to the normal benchmark.

---

## 11.1 Longer horizons

The lecture also notes that for **longer horizons**, returns become more normal-like due to the central limit theorem.

So:

- daily returns are often fat-tailed,
    
- annual returns may look closer to normal.
    

---

# 12. Value at Risk (VaR)

Let $X$ be the return of an asset.

The lecture defines the value at risk of $X$ at level $\alpha\in(0,1)$, denoted by $\mathrm{VaR}_\alpha(X)$, as the loss threshold for the worst $(100\alpha)%$ of cases.

In words:

> $\mathrm{VaR}_\alpha(X)$ tells us how much the asset loses **at least** on very bad days.

Example from the slide:

> If the 1-day 1% VaR is 5.8%, then the asset loses 5.8% or more during the worst 1% of trading days.

Mathematically, VaR is just the $\alpha$-quantile of returns with the minus sign removed.

If $F_X$ is the CDF of $X$, then

$$  
\mathrm{VaR}_\alpha(X) = -F_X^{-1}(\alpha).  
$$

---

# 13. Expected Shortfall (ES)

VaR tells us the threshold loss on bad days. But it does not tell us how bad losses are **beyond** that threshold.

So the lecture introduces expected shortfall (ES).

The expected shortfall at level $\alpha$, denoted $\mathrm{ES}_\alpha(X)$, is:

$$  
\mathrm{ES}_\alpha(X)
=
E(-X \mid -X > \mathrm{VaR}_\alpha(X)).  
$$

Equivalently,

$$  
\mathrm{ES}_\alpha(X)
=
-E\big(X \mid X < -\mathrm{VaR}_\alpha(X)\big).  
$$

Interpretation:

> ES is the average loss on a bad day, conditional on the loss exceeding VaR.

The lecture notes that clearly,

$$  
\mathrm{ES}_\alpha(X)>\mathrm{VaR}_\alpha(X).  
$$

---

# 14. Computing VaR in Practice

The lecture says VaR can be computed:

1. analytically, if the model is tractable,
    
2. numerically using software such as R.
    

In R, if the return distribution is supported by a quantile function, one can write:

```r
VaR = -qdist(alpha, ...)
```

Examples from the slide:

```r
VaR = -qnorm(0.05, mean=0.02, sd=0.01)
VaR = -qt(0.05, df=10)
```

Here:

- `qnorm` is the normal quantile function,
    
- `qt` is the Student-t quantile function.
    

---

# 15. Analytical VaR for the Normal Distribution

Suppose

$$  
X\sim N(\mu,\sigma^2).  
$$

Then the lecture derives:

$$  
\mathrm{VaR}_\alpha(X)

 -\mu-\Phi^{-1}(\alpha)\sigma

-\mu+\Phi^{-1}(1-\alpha)\sigma,  
$$

where:

- $\Phi$ is the CDF of $N(0,1)$,
    
- $\Phi^{-1}$ is the standard normal quantile function.
    

---

## 15.1 Special case: 1% VaR

At the 1% level,

$$  
\Phi^{-1}(0.01)\approx -2.3263.  
$$

So

 $$  
\mathrm{VaR}_{1\%}(X)

-\mu+2.3263,\sigma.  
$$

This is the normal VaR formula shown in the slides.

---

# 16. General ES Formula

Suppose $X$ has PDF $f$ and CDF $F$.

The lecture shows that the conditional density of $X$ given $X<a$ is

$$  
\frac{f(x)}{F(a)}, \qquad x<a.  
$$

> [!note]- Derivation of conditional density
> Suppose $X$ is a continuous random variable with PDF $f(x)$, and we condition on the event
>
> $$
> B=\{X<a\}.
> $$
>
> We want the conditional density of $X$ given $X<a$.
>
> ---
>
> ### Step 1: Start from conditional probability
>
> For a very small interval $[x,x+dx]$ with $x<a$,
>
> $$
> P(x\le X\le x+dx\mid X<a)
> =
> \frac{P(x\le X\le x+dx,\; X<a)}{P(X<a)}.
> $$
>
> ---
>
> ### Step 2: Simplify the numerator
>
> If $x<a$, then the interval $[x,x+dx]$ already lies inside the event $\{X<a\}$. So
>
> $$
> P(x\le X\le x+dx,\; X<a)=P(x\le X\le x+dx).
> $$
>
> For a continuous random variable,
>
> $$
> P(x\le X\le x+dx)\approx f(x)\,dx.
> $$
>
> ---
>
> ### Step 3: Simplify the denominator
>
> The probability of the conditioning event is
>
> $$
> P(X<a)=F(a),
> $$
>
> where $F$ is the CDF of $X$.
>
> ---
>
> ### Step 4: Form the conditional density
>
> Therefore,
>
> $$
> P(x\le X\le x+dx\mid X<a)
> \approx
> \frac{f(x)\,dx}{F(a)}.
> $$
>
> So the conditional density is
>
> $$
> f_{X\mid X<a}(x)=\frac{f(x)}{F(a)}, \qquad x<a.
> $$
>
> And for $x\ge a$,
>
> $$
> f_{X\mid X<a}(x)=0,
> $$
>
> because once we know $X<a$, values greater than or equal to $a$ are impossible.
>
> ---
>
> ### Final formula
>
> $$
> f_{X\mid X<a}(x)=
> \begin{cases}
> \dfrac{f(x)}{F(a)}, & x<a, \\
> 0, & x\ge a.
> \end{cases}
> $$
>
> ---
>
> ### Intuition
>
> The conditional density is just:
>
> - keep the original density on the region allowed by the condition,
> - throw away everything outside that region,
> - divide by the probability of the condition so the remaining density integrates to 1.
>
> In short:
>
> > conditional density = **truncate + renormalize**.
> > 
Using this, expected shortfall can be written as

$$  
\mathrm{ES}_\alpha(X)
=
-\frac{1}{F(a)}\int_{-\infty}^{a} x f(x),dx,  
\qquad  
a=-\mathrm{VaR}_\alpha(X).  
$$

Since $F(a)=\alpha$ by the definition of VaR,

$$  
\mathrm{ES}_\alpha(X)
=
-\frac{1}{\alpha}  
\int_{-\infty}^{-\mathrm{VaR}_\alpha(X)} x f(x),dx.  
$$

This is the general formula given in the slides.

## 16.1 Alternative Expression
Here is a more intuitive expression, starting from the definition that 

>Expected Shortfall is the average of all VaR levels from 0 up to $\alpha$.

Thus, 

$$\mathrm{ES}_\alpha(X)=\frac{1}{\alpha}\int_0^\alpha \mathrm{VaR}_y(X)\,dy$$
This naturally gives $ES_{\alpha}(X)\geq VaR$


---

# 17. ES for the Normal Distribution

The lecture derives a useful normal-distribution identity first.

If

$$  
Z\sim N(0,1),  
$$

then

$$  
E(Z\mid Z<a)

-\frac{\phi(a)}{\Phi(a)},  
$$

where $\phi$ is the standard normal PDF and $\Phi$ is the standard normal CDF.

Using this, if

$$  
X\sim N(\mu,\sigma^2),  
$$

then

$$  
\mathrm{ES}_\alpha(X)

\frac{\sigma}{\alpha}\phi\big(\Phi^{-1}(\alpha)\big)-\mu.  
$$

This is the lecture formula for normal ES.

> [!important]  
> ES for the normal distribution is larger than VaR because it averages losses in the tail beyond the VaR cutoff.

---

# 18. Double Exponential Example: VaR

The lecture gives a numerical example where $X$ has a double exponential (Laplace-type) density:

$$  
f(x)=\frac{1}{2\sigma}e^{-|x|/\sigma}, \qquad x\in\mathbb R,  
$$

with $\sigma>0$.

We want the $\alpha$-VaR.

For $x<0$,

$$  
f(x)=\frac{1}{2\sigma}e^{x/\sigma}.  
$$

So the CDF on the left tail is

$$  
F(x)=\int_{-\infty}^{x}\frac{1}{2\sigma}e^{z/\sigma},dz  
=\frac12 e^{x/\sigma}.  
$$

Set $F(x)=\alpha$:

$$  
\frac12 e^{x/\sigma}=\alpha  
\quad \Rightarrow \quad  
x=\sigma\log(2\alpha).  
$$

So

$$  
F^{-1}(\alpha)=\sigma\log(2\alpha).  
$$

Hence

$$  
\mathrm{VaR}_\alpha(X)

-\sigma\log(2\alpha).  
$$

For $\alpha=0.01$,

$$  
\mathrm{VaR}_{1\%}(X)=3.9120,\sigma.  
$$

This is exactly the slide result.

---

# 19. Double Exponential Example: ES

Using the general formula,

$$  
\mathrm{ES}_\alpha(X)

-\frac1\alpha  
\int_{-\infty}^{-\mathrm{VaR}_\alpha(X)} x f(x),dx.  
$$

The lecture already found

$$  
F^{-1}(\alpha)=-\mathrm{VaR}_\alpha(X)=\sigma\log(2\alpha).  
$$

So

$$  
\mathrm{ES}_\alpha(X)

-\frac{1}{\alpha}  
\int_{-\infty}^{\sigma\log(2\alpha)}  
x\cdot \frac{1}{2\sigma}e^{x/\sigma},dx.  
$$

Carrying out the integration yields the lecture result:

$$  
\mathrm{ES}_\alpha(X)

\sigma\big(1-\log(2\alpha)\big).  
$$

For $\alpha=0.01$,

$$  
\mathrm{ES}_{1\%}(X)=4.9120,\sigma.  
$$

So in this example,

$$  
\mathrm{ES}_{1\%}(X)>\mathrm{VaR}_{1\%}(X),  
$$

as expected.

---

# 20. Exam Traps

> [!warning]  
> These are common mistakes.

## Trap 1: Best predictor always means expected value

Not always.

- under unconditional MSE: best predictor is $E(X)$,
    
- under conditional MSE: best predictor is $E_t(X)$.
    

---

## Trap 2: If returns are unpredictable, volatility must also be unpredictable

False.

The lecture explicitly shows:

- returns are hard to predict,
    
- squared returns / volatility are predictable.
    

---

## Trap 3: One-step-ahead GARCH forecast equals current volatility

Not exactly.

The forecast is

$$  
E_{t-1}(\sigma_{t+1}^2)

(1-\alpha-\beta)\sigma^2+(\alpha+\beta)\sigma_t^2,  
$$

which is a weighted average of current volatility and long-run volatility.

---

## Trap 4: VaR and ES are the same

False.

- VaR is a tail cutoff,
    
- ES is the average loss beyond that cutoff.
    

---

## Trap 5: Daily returns are well modeled by a normal distribution

Usually false.

The lecture emphasizes that daily returns are too fat-tailed for a normal model to capture tail risk accurately.

---

## Trap 6: Long-horizon volatility forecast stays forever at today’s volatility

False.

In GARCH, long-horizon forecasts revert toward the long-run variance.

---

# 21. Flashcards

## Prediction

**Q:** Under squared-error loss, what is the best constant predictor of $X$?  
**A:** $E(X)$.

**Q:** Under conditional squared-error loss, what is the best predictor?  
**A:** $E_t(X)$.

---

## Return prediction

**Q:** If $X_t=\sigma_t z_t$, what is $E_{t-1}(X_t)$?  
**A:** $0$.

**Q:** If $X_t=\varepsilon_t+\theta \varepsilon_{t-1}$, what is $E_{t-1}(X_t)$?  
**A:** $\theta \varepsilon_{t-1}$.

**Q:** If $X_t=\phi X_{t-1}+\varepsilon_t$, what is $E_{t-1}(X_t)$?  
**A:** $\phi X_{t-1}$.

---

## GARCH forecasting

# **Q:** What is the one-step-ahead GARCH variance forecast?  
**A:**  
$$  
E_{t-1}(\sigma_{t+1}^2)

(1-\alpha-\beta)\sigma^2+(\alpha+\beta)\sigma_t^2.  
$$

# **Q:** What is the $k$-step-ahead variance forecast?  
**A:**  
$$  
E_{t-1}(\sigma_{t+k}^2)

\big(1-(\alpha+\beta)^k\big)\sigma^2+(\alpha+\beta)^k \sigma_t^2.  
$$

---

## Tail risk

**Q:** What does VaR measure?  
**A:** The loss threshold in the worst $\alpha$ fraction of cases.

**Q:** What does ES measure?  
**A:** The average loss conditional on being beyond VaR.

**Q:** Which is larger, ES or VaR?  
**A:** ES.

---

## Normal formulas

# **Q:** If $X\sim N(\mu,\sigma^2)$, what is $\mathrm{VaR}_\alpha(X)$?  
**A:**  
$$  
-\mu-\Phi^{-1}(\alpha)\sigma

-\mu+\Phi^{-1}(1-\alpha)\sigma.  
$$

**Q:** If $X\sim N(\mu,\sigma^2)$, what is $\mathrm{ES}_\alpha(X)$?  
**A:**  
$$  
\frac{\sigma}{\alpha}\phi(\Phi^{-1}(\alpha))-\mu.  
$$

---

# 22. Compact Formula Sheet

## Best predictor under MSE

$$  
\hat X = E(X)  
$$

## Best predictor under conditional MSE

$$  
\hat X_t = E_t(X)  
$$

---

## One-step-ahead predictions

If

$$  
X_t=\sigma_t z_t,  
$$

then

$$  
E_{t-1}(X_t)=0.  
$$

If

$$  
X_t=\varepsilon_t+\theta\varepsilon_{t-1},  
$$

then

$$  
E_{t-1}(X_t)=\theta\varepsilon_{t-1}.  
$$

If

$$  
X_t=\phi X_{t-1}+\varepsilon_t,  
$$

then

$$  
E_{t-1}(X_t)=\phi X_{t-1}.  
$$

---

## GARCH(1,1)

$$  
R_t=\sigma_t z_t  
$$

$$  
\sigma_t^2=(1-\alpha-\beta)\sigma^2+\alpha R_{t-1}^2+\beta \sigma_{t-1}^2  
$$

One-step-ahead forecast:

$$  
E_{t-1}(\sigma_{t+1}^2)

(1-\alpha-\beta)\sigma^2+(\alpha+\beta)\sigma_t^2  
$$

$k$-step-ahead forecast:

$$  
E_{t-1}(\sigma_{t+k}^2)

\big(1-(\alpha+\beta)^k\big)\sigma^2+(\alpha+\beta)^k \sigma_t^2  
$$

---

## VaR

$$  
\mathrm{VaR}_\alpha(X)=-F_X^{-1}(\alpha)  
$$

If $X\sim N(\mu,\sigma^2)$:

$$  
\mathrm{VaR}_\alpha(X)

 -\mu-\Phi^{-1}(\alpha)\sigma

-\mu+\Phi^{-1}(1-\alpha)\sigma  
$$

---

## ES

$$  
\mathrm{ES}_\alpha(X)

 E(-X\mid -X>\mathrm{VaR}_\alpha(X))

-E(X\mid X<-\mathrm{VaR}_\alpha(X))  
$$

General integral formula:

$$  
\mathrm{ES}_\alpha(X)

-\frac{1}{\alpha}  
\int_{-\infty}^{-\mathrm{VaR}_\alpha(X)} x f(x),dx  
$$

If $X\sim N(\mu,\sigma^2)$:

$$  
\mathrm{ES}_\alpha(X)

\frac{\sigma}{\alpha}\phi(\Phi^{-1}(\alpha))-\mu  
$$

---

## Double exponential example

If

$$  
f(x)=\frac{1}{2\sigma}e^{-|x|/\sigma},  
$$

then

$$  
\mathrm{VaR}_\alpha(X)=-\sigma\log(2\alpha)  
$$

and

$$  
\mathrm{ES}_\alpha(X)=\sigma(1-\log(2\alpha)).  
$$

---

# 23. Big Picture Summary

> [!summary]  
> Class 6 links conditional expectation, volatility forecasting, and tail risk.
> 
> - Prediction under squared error means conditional expectation.
>     
> - Returns are hard to predict in the mean.
>     
> - Volatility is predictable in GARCH.
>     
> - GARCH forecasts revert toward a long-run variance.
>     
> - Standard deviation measures ordinary risk, but not tail risk well.
>     
> - VaR measures a bad-day loss threshold.
>     
> - ES measures the average loss beyond that threshold.
>     
> - Daily return tails are too heavy for a normal model to be fully adequate.
>     

---

# 24. Suggested Obsidian Links

```text
[[Conditional Expectation]]
[[Mean Squared Error]]
[[Volatility Forecasting]]
[[GARCH(1,1)]]
[[Conditional Variance]]
[[Mean Reversion]]
[[Tail Risk]]
[[Value at Risk]]
[[Expected Shortfall]]
[[Normal Distribution]]
[[t-Distribution]]
[[Fat Tails]]
[[Financial Econometrics]]
```
