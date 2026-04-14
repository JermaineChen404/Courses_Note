---
title: "ISOM4520 Class 5 - Conditional Expectations and the GARCH Model"
aliases:
  - "Conditional Expectations and GARCH"
  - "ISOM4520 Class 5"
tags:
  - course/ISOM4520
  - topic/conditional-expectation
  - topic/time-series
  - topic/volatility
  - topic/garch
  - topic/financial-econometrics
  - status/complete
source: "Class 5 lecture slides"
---
# Conditional Expectations and the GARCH Model

> [!abstract]
> This note develops the predictive language of time series through **conditional expectations** and then applies it to asset returns and volatility modeling. The main idea is:
>
> - unconditional quantities like $E(X_t)$ and $\mathrm{Var}(X_t)$ summarize average behavior,
> - but forecasting requires conditioning on current information,
> - and in finance, the most important conditional object is often **conditional variance**, i.e. volatility.
>
> This leads naturally to the standard asset return model
>
> $$
> R_t = \mu_t + \sigma_t z_t
> $$
>
> and then to the [[GARCH(1,1)]] model.

---

## Table of Contents

- [[#1. Learning Objectives]]
- [[#2. Why Conditional Expectations Matter]]
- [[#3. Basic Intuition: Conditioning Changes Forecasts]]
- [[#4. Conditional Expectation: Rules and Properties]]
- [[#5. Information Sets in Time Series]]
- [[#6. Conditional Mean and Variance in MA(1) and AR(1)]]
- [[#7. Homoscedasticity vs Conditional Heteroscedasticity]]
- [[#8. The Standard Asset Return Model]]
- [[#9. Unconditional Mean, Variance, and Autocovariance in the Standard Return Model]]
- [[#10. The GARCH(1,1) Model]]
- [[#11. Long-Run Variance in GARCH(1,1)]]
- [[#12. Interpretation of GARCH Parameters]]
- [[#13. Standardized Returns]]
- [[#14. Visual and Empirical Interpretation]]
- [[#15. Exam Traps]]
- [[#16. Flashcards]]
- [[#17. Compact Formula Sheet]]

---

# 1. Learning Objectives

After this note, you should be able to:

1. explain why unconditional moments are not enough for prediction,
2. define and interpret **conditional expectation**,
3. work with the information set $\mathcal{F}_t$ in time series,
4. compute conditional means and conditional variances in simple models,
5. distinguish between:
   - homoscedasticity,
   - heteroscedasticity,
   - conditional heteroscedasticity,
6. understand the standard return model
   $$
   R_t = \mu_t + \sigma_t z_t,
   $$
7. derive the unconditional variance of a GARCH(1,1) model,
8. explain why returns can be uncorrelated but still have time-varying volatility.

---

# 2. Why Conditional Expectations Matter

Unconditional quantities such as mean, variance, ACF, and VaR already have some predictive interpretation, but they do **not** use current information.

For a stationary process:

- $E(X_t)=\mu$ tells us the typical future level,
- $\mathrm{Var}(X_t)=\sigma^2$ tells us the typical squared deviation from the mean.

But this is often too crude.

> [!important]
> Forecasts should depend on the current state of the world.

For example:

- on a calm day, tomorrow's volatility forecast should be low,
- on a crisis day, tomorrow's volatility forecast should be much higher.

That is why we need **conditional expectations**.

---

# 3. Basic Intuition: Conditioning Changes Forecasts

## 3.1 Two-dice sum example

Let $X_1$ and $X_2$ be two die rolls and define

$$
S=X_1+X_2.
$$

Unconditionally,

$$
E(S)=E(X_1)+E(X_2)=3.5+3.5=7.
$$

Conditioning on the first roll $X_1$:

$$
E(S\mid X_1)=E(X_1+X_2\mid X_1)=X_1+E(X_2\mid X_1).
$$

Since the rolls are independent,

$$
E(X_2\mid X_1)=E(X_2)=3.5,
$$

so

$$
E(S\mid X_1)=X_1+3.5.
$$

> [!note]
> The key idea is that once a variable is known, we no longer average over it.

---

## 3.2 Finance intuition

Similarly, in finance:

- unconditional mean return is a rough baseline,
- but conditional mean and conditional variance use current information,
- and in practice, conditional variance is often the more important object.

---

# 4. Conditional Expectation: Rules and Properties

## 4.1 Treat known variables as constants

If conditioning on $Y$, then anything measurable with respect to $Y$ is treated as known.

Examples:

$$
E(X+Y\mid Y)=E(X\mid Y)+Y
$$

$$
E(XY\mid Y)=Y\,E(X\mid Y)
$$

More generally, if $Z$ is already known under the conditioning information, it can be pulled outside the conditional expectation.

---

## 4.2 Independence

If $X$ is independent of $Y$, then

$$
E(X\mid Y)=E(X).
$$

Conditioning on irrelevant information does not change the forecast.

---

## 4.3 Linearity

$$
E(aX+b\mid Y)=aE(X\mid Y)+b
$$

for constants $a,b$. It is obvious due to the linearity of Expectation operator.

---

## 4.4 Tower property / law of total expectation

$$
E(X)=E(E(X\mid Y)).
$$

This says:

> if you first take the best forecast of $X$ given $Y$, and then average that forecast over all possible values of $Y$, you recover the unconditional mean.

---

## 4.5 Conditional variance

The conditional variance of $X$ given $Y$ is

$$
\mathrm{Var}(X\mid Y)=E\left((X-E(X\mid Y))^2\mid Y\right).
$$

Equivalent formula:

$$
\mathrm{Var}(X\mid Y)=E(X^2\mid Y)-\left(E(X\mid Y)\right)^2.
$$

This is the conditional version of the usual variance formula.

---

# 5. Information Sets in Time Series

In time series, the conditioning object is usually not a single random variable but the whole past information set denoted by $\mathcal{F}_t$.

## 5.1 Definition

$\mathcal{F}_t$ contains all random variables observed up to time $t$ (before and including $t$).

So:

- $\mathcal{F}_{t-1}$ = all information known just before time $t$,
- $E_{t-1}(X)$ is shorthand for
  $$
  E(X\mid \mathcal{F}_{t-1}),
  $$
- $\mathrm{Var}_{t-1}(X)$ is shorthand for
  $$
  \mathrm{Var}(X\mid \mathcal{F}_{t-1}).
  $$

---

## 5.2 Interpretation

> [!important]
> $E_{t-1}(X_t)$ is the best forecast of $X_t$ using all information available before time $t$.

Similarly,

$$
\mathrm{Var}_{t-1}(X_t)
$$

is the uncertainty about $X_t$ from the perspective of time $t-1$.

---

# 6. Conditional Mean and Variance in MA(1) and AR(1)

## 6.1 MA(1) example

Consider a MA(1) process

$$
X_t=\varepsilon_t+0.5\varepsilon_{t-1},
\qquad
\varepsilon_t \sim IID(0,1).
$$

### Unconditional moments

$$
E(X_t)=0
$$

and

$$
\mathrm{Var}(X_t)=1+0.5^2=1.25.
$$

### Conditional mean

Condition on $\mathcal{F}_{t-1}$.

At time $t-1$, $\varepsilon_{t-1}$ is already known, but $\varepsilon_t$ is not.

So

$$
E_{t-1}(X_t)=E_{t-1}(\varepsilon_t+0.5\varepsilon_{t-1})
=E_{t-1}(\varepsilon_t)+0.5\varepsilon_{t-1}.
$$

Since $\varepsilon_t$ is independent of the past,

$$
E_{t-1}(\varepsilon_t)=E(\varepsilon_t)=0.
$$

Hence

$$
E_{t-1}(X_t)=0.5\varepsilon_{t-1}.
$$

### Conditional variance

$$
\mathrm{Var}_{t-1}(X_t)
=
\mathrm{Var}_{t-1}(\varepsilon_t+0.5\varepsilon_{t-1}).
$$

Since $0.5\varepsilon_{t-1}$ is already known at time $t-1$, it is a constant under conditioning, so only $\varepsilon_t$ contributes uncertainty:

$$
\mathrm{Var}_{t-1}(X_t)=\mathrm{Var}_{t-1}(\varepsilon_t)=1.
$$

> [!summary]
> In the MA(1), the unconditional variance is $1.25$, but the conditional variance is $1$ because part of $X_t$ is already known from the past.

---

## 6.2 AR(1) example

Consider

$$
X_t=\phi X_{t-1}+\varepsilon_t,
\qquad
\varepsilon_t\sim IID(0,1).
$$

### Conditional mean

Since $X_{t-1}$ is known at time $t-1$,

$$
E_{t-1}(X_t)
=
E_{t-1}(\phi X_{t-1}+\varepsilon_t)
=
\phi X_{t-1}+E_{t-1}(\varepsilon_t)
=
\phi X_{t-1}.
$$

### Conditional variance

Again, the only unknown part is $\varepsilon_t$, so

$$
\mathrm{Var}_{t-1}(X_t)=\mathrm{Var}_{t-1}(\varepsilon_t)=1.
$$

> [!note]
> In both MA(1) and AR(1), forecasting the next observation means separating the known part from the new shock.

---

# 7. Homoscedasticity vs Conditional Heteroscedasticity

## 7.1 Homoscedasticity

A time series $\{X_t\}$ is **homoscedastic** if

$$
\mathrm{Var}(X_t)
$$

is constant over time.

If the variance changes with $t$, the series is **heteroscedastic**.

Since stationary time series have constant unconditional variance, stationarity implies homoscedasticity.

---

## 7.2 Conditional homoscedasticity

A time series is **conditionally homoscedastic** if

$$
\mathrm{Var}_{t-1}(X_t)
$$

is constant over time.

Otherwise, it is **conditionally heteroscedastic**.

For asset returns $R_t$, the quantity

$$
\mathrm{Var}_{t-1}(R_t)
$$

is called **volatility** in the lecture.

> [!important]
> Conditional heteroscedasticity is the right concept for time-varying risk.

---

## 7.3 Key conceptual distinction

A return series can have:

- constant unconditional variance,
- but time-varying conditional variance.

This is exactly the structure seen in financial returns.

![[image-4.png|Daily sample SD of 5 min S&P 500 ETF returns]]

The chart in the slides shows large volatility spikes during certain periods, but this does not necessarily mean that the unconditional variance has structurally changed; instead, it reflects changing conditions over time.

> [!summary]
> Volatility can change over time even when the return process remains stationary.

---

# 8. The Standard Asset Return Model

$$
R_t=\mu_t+\sigma_t z_t.
$$

- $R_t$ is the log return from $t-1$ to $t$,
- $z_t\sim IID(0,1)$,
- $z_t$ is independent of all random variables in $\mathcal{F}_{t-1}$,
- $\mu_t$ and $\sigma_t$ belong to $\mathcal{F}_{t-1}$.

---

## 8.1 Interpretation

At time $t-1$, before today’s return is realized:

- $\mu_t$ is the forecasted mean return,
- $\sigma_t^2$ is the forecasted variance,
- $z_t$ is the new standardized shock arriving at time $t$.

So:

$$
\text{return} = \text{forecastable part} + \text{unexpected shock}.
$$

More precisely:

$$
R_t=\mu_t+\sigma_t z_t.
$$

---

## 8.2 Why this specification is useful

The model assumes $$z_{t}=\frac{R_{t}-\mu_{t}}{\sigma_{t}}\sim IID(0,1)\iff \mu_{t}\text{ and }\sigma_{t}^{2} \text{ capture all available info about } R$$
After isolating all predictable variation in:

- the conditional mean $\mu_t$,
- the conditional variance $\sigma_t^2$.

The standardized residual

$$
z_t=\frac{R_t-\mu_t}{\sigma_t}
$$

is assumed IID. This means the model says:

> once we account for conditional mean and volatility, the remaining shocks are structureless noise.

---

## 8.3 Conditional mean and conditional variance

$$
E_{t-1}(R_t)=\mu_t
$$

and

$$
\mathrm{Var}_{t-1}(R_t)=\sigma_t^2.
$$
### Proof of the conditional mean

$$
E_{t-1}(R_t)
=
E_{t-1}(\mu_t+\sigma_t z_t)
=
\mu_t+\sigma_t E_{t-1}(z_t).
$$

Since $\mu_t$ and $\sigma_t$ are known at time $t-1$ and $z_t$ is independent of the past with mean 0,

$$
E_{t-1}(z_t)=E(z_t)=0.
$$

So

$$
E_{t-1}(R_t)=\mu_t.
$$

### Proof of the conditional variance

$$
\mathrm{Var}_{t-1}(R_t)=\mathrm{Var}_{t-1}(\sigma_t z_t).
$$

Because $\sigma_t$ is known at time $t-1$,

$$
\mathrm{Var}_{t-1}(R_t)=\sigma_t^2 \mathrm{Var}_{t-1}(z_t).
$$

Since $z_t$ has variance 1,

$$
\mathrm{Var}_{t-1}(R_t)=\sigma_t^2.
$$

---

# 9. Unconditional Mean, Variance, and Autocovariance in the Standard Return Model

Here we simplify to the case where $\mu_t\equiv \mu$, and eventually to $\mu=0$ for convenience.

So we work with

$$
R_t=\sigma_t z_t.
$$

It makes sense since

- stochastic volatility models are mostly used on short to medium horizons
- On such short horizons, the expected daily return is trivial: Take S&P 500 for example,
	- Daily return $=$ Annual Return$/T\approx 0.25\%$ 
	- Daily Volatility $=$ Annual Volatility $/\sqrt{ T }\approx 1.2\%$

---

## 9.1 Unconditional mean

By the tower property,

$$
E(R_t)=E(E_{t-1}(R_t)).
$$

Since $E_{t-1}(R_t)=0$,

$$
E(R_t)=0.
$$

---

## 9.2 Unconditional variance

Since $E(R_t)=0$,

$$
\mathrm{Var}(R_t)=E(R_t^2)-(E(R_{t}))^2=E(R_{t}^2).
$$

Now

$$
R_t^2=\sigma_t^2 z_t^2.
$$

So

$$
\mathrm{Var}(R_t)=E(\sigma_t^2 z_t^2).
$$

Apply iterated expectations:

$$
E(\sigma_t^2 z_t^2)
=
E\left(E_{t-1}(\sigma_t^2 z_t^2)\right).
$$

Because $\sigma_t^2$ is known at time $t-1$,

$$
E_{t-1}(\sigma_t^2 z_t^2)=\sigma_t^2 E_{t-1}(z_t^2).
$$

Since $z_t$ is independent of the past and has variance 1,

$$
E_{t-1}(z_t^2)=E(z_t^2)=1.
$$

Hence

$$
\mathrm{Var}(R_t)=E(\sigma_t^2).
$$

> [!important] Law of total variance (return model)
> In general,
> $$
> \mathrm{Var}(R_t)
> =
> E\!\left[\mathrm{Var}(R_t\mid \mathcal F_{t-1})\right]
> +
> \mathrm{Var}\!\left(E(R_t\mid \mathcal F_{t-1})\right).
> $$
> So the unconditional variance has two parts:
> - the **average conditional variance**, and
> - the variability of the **conditional mean**.
>
> Here we simplify to
> $$
> E(R_t\mid \mathcal F_{t-1}) = 0,
> $$
> so the second term is zero, and
> $$
> \mathrm{Var}(R_t)
> =
> E\!\left[\mathrm{Var}(R_t\mid \mathcal F_{t-1})\right]
> = E(\sigma_t^2).
> $$

---

## 9.3 Uncorrelated returns

For $k\ge 1$,

$$
\mathrm{Cov}(R_t,R_{t+k})=0.
$$

### Proof sketch

Since $E(R_t)=0$, $$\mathrm{Cov}(R_t,R_{t+k})=E(R_t R_{t+k})+E(R_{t})E(R_{t+k})=E(R_{t}R_{t+k})$$
Substitute $R_t = \sigma_t z_t$ and apply the law of iterated expectations conditioning on $\mathcal{F}_{t+k-1}$:

$$
\begin{align*}
E(R_t R_{t+k}) &= E\left[ E_{t+k-1}(\sigma_t z_t \sigma_{t+k} z_{t+k}) \right] \\
&= E\left[ \sigma_t z_t \sigma_{t+k} E_{t+k-1}(z_{t+k}) \right] \\
&= 0
\end{align*}
$$

This holds because everything except $z_{t+k}$ is known at $t+k-1$, and $E_{t+k-1}(z_{t+k}) = 0$.

> [!summary]
> Even with stochastic volatility, returns can be serially uncorrelated.

This is a central stylized fact in finance.

---
## 9.4 Summary

If $\sigma_{t}^2$ is also stationary, we have
$$E(\sigma_{t}^{2})=\text{constant}$$
A return series can be:

- **uncorrelated**, because $\mathrm{Cov}(R_t,R_{t+k})=0$ for $k\ge 1$,
- **weakly stationary**, because it has constant mean, constant variance, and lag-dependent autocovariances,
- **homoscedastic**, because $\mathrm{Var}(R_t)=E(\sigma_t^2)$ is constant,
- **conditionally heteroscedastic**, because $\mathrm{Var}_{t-1}(R_t)=\sigma_t^2$ may still vary over time.
# 10. The GARCH(1,1) Model

The lecture then introduces one of the most important volatility models in empirical finance: GARCH.

GARCH stands for:

**Generalized AutoRegressive Conditional Heteroscedasticity**


The GARCH(1,1) model is

$$
R_t=\sigma_t z_t,
$$

$$
\sigma_t^2=\omega+\alpha R_{t-1}^2+\beta \sigma_{t-1}^2,
$$

with parameters satisfying:

$$
\omega>0,\qquad \alpha,\beta\ge 0,\qquad \alpha+\beta<1.
$$

---

## 10.1 Interpretation

Today’s conditional variance depends on:

1. a constant base level $\omega$,
2. yesterday’s squared return $R_{t-1}^2$,
	- Yesterday's realized volatility
3. yesterday’s conditional variance $\sigma_{t-1}^2$.
	- Previous prediction of yesterday's volatility

So volatility reacts both to:

- **new shocks** through $R_{t-1}^2$,
- **persistence** through $\sigma_{t-1}^2$.

---

## 10.2 ARCH as a special case

If $\beta=0$, then

$$
\sigma_t^2=\omega+\alpha R_{t-1}^2,
$$

which is the original ARCH(1) model introduced by Engle.

So GARCH generalizes ARCH by letting volatility depend on both lagged squared returns and lagged conditional variance.

---

# 11. Long-Run Variance in GARCH(1,1)

A major derivation in the lecture is the unconditional variance of the GARCH(1,1) model.

Let

$$
\sigma^2=\mathrm{Var}(R_t)=E(\sigma_t^2).
$$

Assuming $\sigma_t^2$ is stationary, take expectations in

$$
\sigma_t^2=\omega+\alpha R_{t-1}^2+\beta \sigma_{t-1}^2.
$$

Then

$$
\sigma^2=\omega+\alpha E(R_{t-1}^2)+\beta E(\sigma_{t-1}^2).
$$

Since

$$
E(R_{t-1}^2)=\mathrm{Var}(R_{t-1})=\sigma^2
$$

and

$$
E(\sigma_{t-1}^2)=\sigma^2,
$$

we get

$$
\sigma^2=\omega+\alpha \sigma^2+\beta \sigma^2.
$$

So

$$
\sigma^2=\omega+(\alpha+\beta)\sigma^2.
$$

Rearrange:

$$
\sigma^2(1-\alpha-\beta)=\omega.
$$

Hence

$$
\sigma^2=\frac{\omega}{1-\alpha-\beta}.
$$

> [!important]
> This is the **unconditional variance** or **long-run variance** of the GARCH(1,1) model.

The condition

$$
\alpha+\beta<1
$$

ensures this quantity exists and is finite.

---

# 12. Interpretation of GARCH Parameters

Using the long-run variance formula, we can rewrite the variance equation as:

$$
\sigma_t^2=(1-\alpha-\beta)\sigma^2+\alpha R_{t-1}^2+\beta \sigma_{t-1}^2.
$$

This shows that today’s variance is a weighted average of:

- the long-run variance $\sigma^2$,
2. yesterday’s squared return $R_{t-1}^2$,
	- Yesterday's realized volatility
3. yesterday’s conditional variance $\sigma_{t-1}^2$.
	- Previous prediction of yesterday's volatility

---

## 12.1 Role of $\alpha$

$\alpha$ measures how strongly volatility reacts to new return shocks.

Large $\alpha$ means:

- volatility responds strongly to yesterday’s squared return,
- shocks have immediate impact.

---

## 12.2 Role of $\beta$

$\beta$ measures volatility persistence.

Large $\beta$ means:

- volatility forecasts depend heavily on past volatility,
- once volatility rises, it tends to stay high for a while.

---

## 12.3 Role of $\alpha+\beta$

The sum $\alpha+\beta$ measures total persistence.

- if $\alpha+\beta$ is close to 1, volatility is highly persistent,
- if it is small, volatility reverts quickly toward its long-run level.

> [!summary]
> In practice, many financial return series have $\alpha+\beta$ close to 1, reflecting strong volatility persistence.

---

## 12.4. Standardized Returns

The lecture emphasizes the standardized return

$$
z_t=\frac{R_t}{\sigma_t}
$$

when $\mu=0$.

If the model is well specified, the standardized returns should behave approximately like IID noise.

That means:

- standardized returns should have little autocorrelation,
- standardized squared returns should also have little autocorrelation.

This is why checking the ACF of:

- $R_t/\sigma_t$,
- $(R_t/\sigma_t)^2$

is an important diagnostic after fitting a GARCH model.
## 12.6 Estimation

---

# 14. Visual and Empirical Interpretation

## 14.1 Simulation

```r  
install.packages("fGarch")  
library(fGarch)  
a <- 0.3 #alpha value  
b <- 0.55 #beta value  
v <- 0.2^2/252 #unconditional variance  
om <- v*(1-a-b) #omega  
set.seed(123)  
specif <- garchSpec(model = list(omega=om, alpha = a, beta = b, cond.dist = "norm"))  
data <- garchSim(spec = specif, n = 1000, extended = TRUE)  
R <- data$garch  
si <- data$sigma  
z <- data$eps
```

The simulation slides display:

- standardized shocks $z_t$,
- volatility process $\sigma_t$,
- returns $R_t$.

![[image-5.png]]

The key lesson is:

- shocks may be IID,
- but returns inherit time-varying scale through $\sigma_t$,
- so returns can show volatility clustering even if $z_t$ itself does not.

## 14.3 Estimation

```r
data <- read.csv("sp500_daily_2005_2024.csv")
logret <- diff(log(data$PRC))
dates <- as.Date(data$date, "%m/%d/%y")
model <- garchFit(~garch(1, 1), logret, cond.dist="norm",
include.mean = FALSE, trace = FALSE)
model@fit$coef
omega      alpha1      beta1
2.760499e-06 1.270681e-01 8.493568e-01
plot(dates[1:(length(dates)-1)], logret, xlab="", ylab="Log Returns", type="l")
plot(dates[1:(length(dates)-1)], model@sigma.t*sqrt(252),
xlab="", ylab="Annualized Volatility", type="l")
plot(dates[1:(length(dates)-1)], logret/model@sigma.t, xlab="",
ylab="Standardized Returns", type="l")
```

The empirical example fits a GARCH(1,1) model to S&P 500 daily log returns and plots:

- raw returns,
- annualized volatility estimates,
- standardized returns. :contentReference[oaicite:19]{index=19}

![[image-7.png]]

The intended takeaway is:

> after scaling returns by estimated volatility, much of the dependence in magnitudes should disappear.

---

# 15. Exam Traps

> [!warning]
> These are common mistakes.

## Trap 1: Unconditional mean is the same as conditional mean

False.

Unconditional mean is the average over all situations. Conditional mean uses current information.

---

## Trap 2: If unconditional variance is constant, then volatility is constant

False.

Volatility usually refers to conditional variance:

$$
\mathrm{Var}_{t-1}(R_t).
$$

This can vary over time even when unconditional variance is constant.

---

## Trap 3: Heteroscedasticity and conditional heteroscedasticity are the same

False.

- heteroscedasticity concerns $\mathrm{Var}(X_t)$ varying with $t$,
- conditional heteroscedasticity concerns $\mathrm{Var}_{t-1}(X_t)$ varying with $t$.

---

## Trap 4: If returns are uncorrelated, they must be independent

False.

GARCH returns are a standard counterexample:

- returns are uncorrelated,
- but squared returns are dependent.

---

## Trap 5: In GARCH(1,1), $\alpha+\beta<1$ is optional

False.

It is needed for existence of the long-run variance

$$
\frac{\omega}{1-\alpha-\beta}.
$$

---

## Trap 6: Large $\beta$ means large immediate reaction to shocks

Not exactly.

- $\alpha$ controls immediate reaction to new shocks,
- $\beta$ controls persistence.

---

# 16. Flashcards

## Definitions

**Q:** What is $E(X\mid Y)$?  
**A:** The conditional expectation of $X$ given $Y$, i.e. the best forecast of $X$ using information in $Y$.

**Q:** What is $ \mathcal{F}_t $?  
**A:** The information set containing all variables known up to time $t$.

**Q:** What is conditional variance in finance?  
**A:** For returns $R_t$, it is
$$
\mathrm{Var}_{t-1}(R_t),
$$
often called volatility.

---

## Rules

**Q:** If $X$ is independent of $Y$, what is $E(X\mid Y)$?  
**A:** $E(X)$.

**Q:** What is the tower property?  
**A:** 
$$
E(X)=E(E(X\mid Y)).
$$

**Q:** What is the conditional variance formula?  
**A:** 
$$
\mathrm{Var}(X\mid Y)=E(X^2\mid Y)-\left(E(X\mid Y)\right)^2.
$$

---

## Standard return model

**Q:** In
$$
R_t=\mu_t+\sigma_t z_t,
$$
what is $\mu_t$?  
**A:** The conditional mean:
$$
\mu_t=E_{t-1}(R_t).
$$

**Q:** What is $\sigma_t^2$?  
**A:** The conditional variance:
$$
\sigma_t^2=\mathrm{Var}_{t-1}(R_t).
$$

**Q:** Why is $z_t$ useful?  
**A:** It is the standardized residual, ideally IID after removing conditional mean and volatility.

---

## GARCH

**Q:** What is GARCH(1,1)?  
**A:** 
$$
R_t=\sigma_t z_t,\qquad
\sigma_t^2=\omega+\alpha R_{t-1}^2+\beta \sigma_{t-1}^2.
$$

**Q:** What is the long-run variance?  
**A:** 
$$
\frac{\omega}{1-\alpha-\beta}.
$$

**Q:** What does a large $\alpha$ mean?  
**A:** Strong reaction to recent shocks.

**Q:** What does a large $\beta$ mean?  
**A:** High volatility persistence.

---

# 17. Compact Formula Sheet

## Conditional expectation rules

$$
E(aX+b\mid Y)=aE(X\mid Y)+b
$$

$$
E(XY\mid Y)=Y\,E(X\mid Y)
$$

if $Y$ is known under the conditioning information.

$$
E(X\mid Y)=E(X)
$$

if $X$ is independent of $Y$.

$$
E(X)=E(E(X\mid Y))
$$

$$
\mathrm{Var}(X\mid Y)=E(X^2\mid Y)-\left(E(X\mid Y)\right)^2
$$

---

## Time-series notation

$$
E_t(X)=E(X\mid \mathcal{F}_t)
$$

$$
\mathrm{Var}_t(X)=\mathrm{Var}(X\mid \mathcal{F}_t)
$$

---

## Standard return model

$$
R_t=\mu_t+\sigma_t z_t
$$

$$
\mu_t=E_{t-1}(R_t)
$$

$$
\sigma_t^2=\mathrm{Var}_{t-1}(R_t)
$$

If $\mu_t\equiv 0$:

$$
R_t=\sigma_t z_t
$$

$$
E(R_t)=0
$$

$$
\mathrm{Var}(R_t)=E(\sigma_t^2)
$$

$$
\mathrm{Cov}(R_t,R_{t+k})=0 \qquad (k\ge 1)
$$

---

## GARCH(1,1)

$$
R_t=\sigma_t z_t
$$

$$
\sigma_t^2=\omega+\alpha R_{t-1}^2+\beta \sigma_{t-1}^2
$$

with

$$
\omega>0,\qquad \alpha,\beta\ge 0,\qquad \alpha+\beta<1
$$

Long-run variance:

$$
\sigma^2=\frac{\omega}{1-\alpha-\beta}
$$

Rewritten form:

$$
\sigma_t^2=(1-\alpha-\beta)\sigma^2+\alpha R_{t-1}^2+\beta \sigma_{t-1}^2
$$

---

# 18. Big Picture Summary

> [!summary]
> This lecture provides the forecasting language needed for volatility modeling.
>
> - Unconditional moments summarize average behavior.
> - Conditional expectations incorporate current information.
> - In time series, conditioning is done on the information set $ \mathcal{F}_{t-1} $.
> - For financial returns, conditional variance is the key forecast object.
> - The standard return model writes returns as
>   $$
>   R_t=\mu_t+\sigma_t z_t.
>   $$
> - If $\mu_t$ and $\sigma_t^2$ capture all available information, then standardized shocks are IID.
> - GARCH(1,1) models time-varying volatility through lagged squared returns and lagged variance.
> - Returns can still be uncorrelated even when volatility is highly persistent.

