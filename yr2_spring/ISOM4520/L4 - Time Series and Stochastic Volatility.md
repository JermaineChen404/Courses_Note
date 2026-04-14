---
title: "ISOM4520 Class 4 - Time Series and Stochastic Volatility"
aliases:
  - "Time Series and Stochastic Volatility"
  - "ISOM4520 Class 4"
tags:
  - course/ISOM4520
  - topic/time-series
  - topic/volatility
  - topic/financial-econometrics
  - topic/stochastic-volatility
  - status/complete
created: 2026-03-09
source: "Class 4 lecture slides"
---
# Time Series and Stochastic Volatility

> [!abstract]
> This note studies the statistical structure of financial returns and volatility. The key message is:
> - **returns are often approximately uncorrelated,**
> - **but volatility is persistent and predictable.**
>
> This is the conceptual bridge from basic return analysis to [[ARCH]], [[GARCH]], and stochastic volatility models.


---

## Table of Contents

- [[#1. Learning Objectives]]
- [[#2. Why Volatility Matters]]
- [[#3. Stylized Facts of Financial Returns]]
- [[#4. Time Series Foundations]]
- [[#5. Stationarity]]
- [[#6. Autocovariance and Autocorrelation]]
- [[#7. Benchmark Model: IID Process]]
- [[#8. Moving Average Process MA(1)]]
- [[#9. Autoregressive Process AR(1)]]
- [[#10. Why Returns Can Be Uncorrelated but Volatility Predictable]]
- [[#11. Financial Applications]]
- [[#12. Visual Pattern Recognition for ACF]]
- [[#13. Exam Traps]]
- [[#14. Flashcards]]
- [[#15. Compact Formula Sheet]]

---

# 1. Learning Objectives

After this note, you should be able to:

1. explain why **mean return** and **volatility** matter in finance,
2. describe the main **stylized facts** of returns and volatility,
3. define a **time series** and **weak stationarity**,
4. derive and interpret the **autocovariance function** and **autocorrelation function**,
5. prove the ACF formulas for:
   - IID,
   - MA(1),
   - AR(1),
6. explain why volatility can be predictable even if returns are not,
7. connect these ideas to risk management and volatility modeling.

---

# 2. Why Volatility Matters

In finance, two central quantities are:

$$
\mu = E[R_t], \qquad \sigma^2 = \mathrm{Var}(R_t)
$$

where $R_t$ is the return in period $t$.

Estimates of expected return and volatility are crucial for mean-variance analysis.
## 2.1 Estimating expected return

Common approaches:

- historical sample means,
- asset pricing models such as CAPM,
- fundamental analysis,
- forecasting assumptions.

## 2.2 Estimating volatility

Common approaches:

- historical sample variances and covariances,
- stochastic volatility models,
- high-frequency data,
- options data.

> [!important]
> In practice, expected return is often much harder to estimate precisely than volatility. That is one reason why volatility modeling is so central in empirical finance.
> - for the mean, randomness is an obstacle. 
> - for volatility, randomness is exactly the thing you are measuring.
> 
> Expected return is hard to estimate because it is a **small average buried inside large noise**, while volatility is the **size of that noise itself**.

The present topic focuses on **how to estimate volatility**.
## 2.3 Why volatility is economically important

Volatility enters:

- portfolio construction,
	- portfolio weights depend on the covariance matrix: $$\Sigma =
\begin{pmatrix}
\sigma_1^2 & \mathrm{Cov}(R_1,R_2) \\
\mathrm{Cov}(R_1,R_2) & \sigma_2^2
\end{pmatrix}$$
- risk management,
	- $VaR\approx z\cdot\sigma \cdot \text{position size}$
- option pricing,
	- $\text{Call}\propto \sigma$
- hedging,
	- Delta $\Delta$ and Gamma $\Gamma$ in dynamic hedging
- margin and capital requirements,
	- $\propto VaR$
- stress testing.

---

# 3. Stylized Facts of Financial Returns

## 3.1 Returns are approximately uncorrelated

For log returns $r_t$, empirical autocorrelations are often near zero:

$$
\rho_r(k) \approx 0 \quad \text{for } k \ge 1
$$

This is shown in the ACF plots for monthly, daily, and 5-second S&P 500 log returns.

![[image-2.png]]

### Intuition

If returns were linearly predictable, traders would exploit the pattern:

- if positive returns tend to follow positive returns, traders buy,
- if negative returns tend to follow positive returns, traders sell.

Equilibrium: Competitive trading pressure tends to eliminate predictable linear return patterns.

> [!warning]
> “Uncorrelated” means no linear dependence.
> It does **not** mean no dependence at all.

---

## 3.2 Ultra-high-frequency exception

However, at extremely high frequencies, returns can show significant autocorrelation, especially due to market microstructure effects

At ordinary frequencies, we often think of price as:
$$\text{observed price} \approx \text{fundamental price}$$
But at ultra-high frequency, it is more like:
$$\text{observed price}
=
\text{fundamental price}
+
\text{microstructure noise}$$
That extra noise comes from how markets actually operate:

> [!example] Market microstructure effects causing high-frequency return autocorrelation
>  >[!note]- Bid-ask bounce
>   At very high frequency, trades may alternate between the **ask** and the **bid** even when fundamental value is unchanged. This can create **negative autocorrelation** in observed returns.
>
>  >[!note]- Order splitting
>   Large traders often split one large order into many smaller trades executed over time. This can create repeated buying or selling pressure and lead to **positive short-run autocorrelation**.
>
>  >[!note]- Dealer inventory control
>   Market makers adjust quotes to manage inventory risk. These quote changes can generate predictable short-horizon return patterns.
>
>  >[!note]- Tick size discreteness
>   Prices move in fixed increments rather than continuously. At ultra-high frequency, this can distort measured returns and their autocorrelation.
>
>  >[!note]- Stale quotes
>   Some quotes or transaction prices update with delay. This can create artificial serial dependence in very short-horizon returns.
>
>  >[!note]- Latency
>   Different traders and systems react to information at different speeds. At ultra-high frequency, these timing differences can create temporary predictability.

So the statement “returns are uncorrelated” is mostly an approximation valid at ordinary frequencies.

---

## 3.3 Squared returns are positively autocorrelated

The slides show that squared log returns have positive autocorrelation across lags.

Formally,

$$
\rho_{r^2}(k) > 0
$$

for many values of $k$.

This means:

> Large price movements tend to be followed by large price movements.

This is the phenomenon of **volatility clustering**.

It implies that stock returns are **uncorrelated (linearly independent)** but not **independent**. 

---

## 3.4 Volatility is predictable

Because squared returns are correlated, volatility is not just random noise. Instead, it has structure, and thus **predictable**.

- volatility is **random and time-varying**,
- volatility is **clustered**,
- volatility is **mean-reverting**.

![[image-3.png]]

---


> [!note]- Why are squared returns a proxy for volatility?  
> We write
> 
> $$  
> r_t = \sigma_t z_t  
> $$
> 
> to separate the return into:
> 
> - a **scale part**: $\sigma_t$
>     
> - a **random shock part**: $z_t$
>     
> 
> ## What is $z_t$?
> 
> $z_t$ is the **standardized shock** or **innovation** at time $t$.
> 
> It is usually assumed to satisfy:
> 
> $$  
> E[z_t]=0, \qquad E[z_t^2]=1  
> $$
> 
> So $z_t$ has:
> 
> - mean $0$
>     
> - variance $1$
>     
> 
> That means $z_t$ gives the **direction and relative size** of the shock, while $\sigma_t$ determines how large that shock becomes in actual return units.
> 
> **Intuition:** think of $z_t$ as the “raw surprise,” and $\sigma_t$ as the “volatility multiplier.”
> 
> Example:
> 
> - if $z_t = 0.5$, that is a moderate positive shock
>     
> - if $z_t = -2$, that is a large negative shock
>     
> - if $\sigma_t$ is large, the same $z_t$ creates a bigger return move
>     
> 
> ## Why write $r_t = \sigma_t z_t$?
> 
> Because it is a convenient way to model **time-varying volatility**.
> 
> If volatility were constant, we might write:
> 
> $$  
> r_t = \sigma z_t  
> $$
> 
> But in financial markets, volatility changes over time, so we let it depend on $t$:
> 
> $$  
> r_t = \sigma_t z_t  
> $$
> 
> This says:
> 
> > return = volatility level $\times$ standardized shock
> 
> So:
> 
> - $\sigma_t$ captures how risky the market is at time $t$
>     
> - $z_t$ captures the random news or shock arriving at time $t$
>     
> 
> This setup is widely used in ARCH, GARCH, and stochastic volatility models.
> 
> ## What is $\mathcal{F}_{t-1}$?
> 
> $\mathcal{F}_{t-1}$ means the **information set available up to time $t-1$**.
> 
> It includes everything known before period $t$, such as past:
> 
> - returns,
>     
> - prices,
>     
> - volatility estimates,
>     
> - other variables in the model.
>     
> 
> So when we write
> 
> $$  
> E[r_t^2 \mid \mathcal{F}_{t-1}]  
> $$
> 
> we mean:
> 
> > the expected value of $r_t^2$, given everything already known before time $t$
> 
> This is a **conditional expectation**.
> 
> ## Why does
> 
> $$  
> E[r_t^2 \mid \mathcal{F}_{t-1}] = \sigma_t^2  
> $$
> 
> hold?
> 
> Start from
> 
> $$  
> r_t = \sigma_t z_t  
> $$
> 
> Square both sides:
> 
> $$  
> r_t^2 = \sigma_t^2 z_t^2  
> $$
> 
> Now take conditional expectation given $\mathcal{F}_{t-1}$:
> 
>  $$  
> E[r_t^2 \mid \mathcal{F}_{t-1}]
> 
> E[\sigma_t^2 z_t^2 \mid \mathcal{F}_{t-1}]  
> $$
> 
> Since $\sigma_t$ is known at time $t-1$ in this setup, we can treat $\sigma_t^2$ as fixed relative to $\mathcal{F}_{t-1}$:
> 
>  $$  
> E[r_t^2 \mid \mathcal{F}_{t-1}]
> 
> \sigma_t^2 E[z_t^2 \mid \mathcal{F}_{t-1}]  
> $$
> 
> If $z_t$ is a fresh shock with conditional variance $1$, then
> 
> $$  
> E[z_t^2 \mid \mathcal{F}_{t-1}] = 1  
> $$
> 
> so
> 
> $$  
> E[r_t^2 \mid \mathcal{F}_{t-1}] = \sigma_t^2  
> $$
> 
> ## Why does this mean $r_t^2$ is a proxy for volatility?
> 
> Because $r_t^2$ is centered around the conditional variance $\sigma_t^2$.
> 
> It is not exactly equal to $\sigma_t^2$ in each period, because $z_t^2$ is random. But on average, conditional on past information, it tracks volatility.
> 
> **Intuition:** if volatility is high, then returns tend to be large in magnitude, so
> 
> $$  
> |r_t| \text{ large } \Rightarrow r_t^2 \text{ large}  
> $$
> 
> This is true whether the return is positive or negative:
> 
> - $r_t = 0.08 \Rightarrow r_t^2 = 0.0064$
>     
> - $r_t = -0.08 \Rightarrow r_t^2 = 0.0064$
>     
> 
> Both indicate a large move, hence high volatility.
> 
> That is why squared returns are useful: they ignore direction and focus on **magnitude**.
> 
> ## One-line summary
> 
> - $z_t$ = standardized random shock
>     
> - $\sigma_t$ = time-$t$ volatility
>     
> - $\mathcal{F}_{t-1}$ = all information known before time $t$
>     
> - $r_t^2$ is informative about volatility because its conditional expectation equals $\sigma_t^2$
>     
> 
> > Squared returns are **noisy observations of latent volatility**.

---

# 4. Time Series Foundations

A **time series** is a sequence of random variables indexed by time:

$$
X_1, X_2, \dots, X_T.
$$

$X_{T}$ can be:

- returns,
- volatility,
- interest rates,
- inflation,
- exchange rates.
## 4.1 Why I.I.D. is often unrealistic

I.I.D. means:

1. **identically distributed**, and
2. **independent across time**.

Financial time series often violate both since:

- volatility changes across time,
- crises alter the distribution,
- squared returns are serially dependent.

So we replace I.I.D. with a weaker and more useful concept: **stationarity**.

---

# 5. Stationarity

## 5.1 Informal definition

A time series is stationary if its statistical behavior does not change over time.

That means:

- the average level is stable,
- the variance is stable,
- the dependence structure is stable.

Intuitively: the way $X_t$ and $X_{t+1}$ relate should be the same as the way $X_{t+100}$ and $X_{t+101}$ relate.

---

## 5.2 Weak stationarity: formal definition

A time series $\{X_t\}$ is **weakly stationary** if:

$$
E[X_t] = \mu \quad \text{for all } t,
$$

and

$$
\gamma(k) = \mathrm{Cov}(X_t, X_{t+k})
$$

depends only on the lag $k$, not on $t$.

Thus:

- the mean is constant,
- the variance is constant, since
  $$
  \mathrm{Var}(X_t)=\text{Cov}(X_{t},X_{t})=\gamma(0),
  $$
- covariance depends only on temporal distance.

---

## 5.3 Why stationarity matters

> [!important]
> Stationarity makes historical data informative about future behavior.

If the process is nonstationary, a relationship observed in one period may not apply later.

Stationarity allows us to estimate:

- mean,
- variance,
- autocorrelation,

from a single realized sample.

---

## 5.4 Weak vs strict stationarity (supplementary)

### Strict stationarity

A process is strictly stationary if every joint distribution is invariant to time shifts.

That is, for any $n$, any times $t_1,\dots,t_n$, and any shift $h$,

$$
(X_{t_1},\dots,X_{t_n})
\overset{d}{=}
(X_{t_1+h},\dots,X_{t_n+h}).
$$

### Weak stationarity

Only first and second moments must be invariant.

In many linear time series models, weak stationarity is enough.

---

# 6. Autocovariance and Autocorrelation

## 6.1 Autocovariance function

The autocovariance at lag $k$ is

$$
\gamma(k)=\mathrm{Cov}(X_t,X_{t+k}).
$$

It measures linear dependence between observations $k$ periods apart.

---

## 6.2 Autocorrelation function (ACF)

The autocorrelation at lag $k$ is

$$
\rho(k)=\mathrm{Corr}(X_t,X_{t+k}).
$$

Under weak stationarity,

$$
\rho(k)
=
\frac{\mathrm{Cov}(X_t,X_{t+k})}{\sqrt{\mathrm{Var}(X_t)\mathrm{Var}(X_{t+k})}}
=
\frac{\gamma(k)}{\gamma(0)}.
$$

---

## 6.3 Basic properties

For a weakly stationary process:

$$
\gamma(0)=\mathrm{Var}(X_t)\ge 0
$$

$$
\rho(0)=1
$$

$$
|\rho(k)|\le 1
$$

$$
\gamma(-k)=\gamma(k), \qquad \rho(-k)=\rho(k)
$$

### Proof that $\gamma(-k)=\gamma(k)$

$$
\gamma(-k)=\mathrm{Cov}(X_t,X_{t-k})
$$

Let $s=t-k$. Then

$$
\gamma(-k)=\mathrm{Cov}(X_{s+k},X_s)
=\mathrm{Cov}(X_s,X_{s+k})
=\gamma(k)
$$

because covariance is symmetric.

---

## 6.4 Interpretation of ACF

- large positive $\rho(k)$: persistence,
- large negative $\rho(k)$: reversal,
- near-zero $\rho(k)$: little linear predictability at lag $k$.

> [!tip]
> In applications, the shape of the ACF is often a diagnostic clue for model identification.

---

# 7. Benchmark Model: IID Process

Suppose

$$
X_t \sim IID(\mu,\sigma^2).
$$

The slides use IID as the benchmark case.

## 7.1 Mean and variance

$$
E[X_t]=\mu, \qquad \mathrm{Var}(X_t)=\sigma^2.
$$

## 7.2 Autocovariance derivation

For $k\neq 0$, independence implies

$$
E[X_tX_{t+k}] = E[X_t]E[X_{t+k}] = \mu^2.
$$

Therefore

$$
\gamma(k)
=
\mathrm{Cov}(X_t,X_{t+k})
=
E[X_tX_{t+k}] - E[X_t]E[X_{t+k}]
=
\mu^2-\mu^2
=
0.
$$

For $k=0$,

$$
\gamma(0)=\mathrm{Var}(X_t)=\sigma^2.
$$

Hence

$$
\gamma(k)=
\begin{cases}
\sigma^2, & k=0,\\
0, & k\neq 0.
\end{cases}
$$

## 7.3 ACF derivation

Since

$$
\rho(k)=\frac{\gamma(k)}{\gamma(0)},
$$

we get

$$
\rho(k)=
\begin{cases}
1, & k=0,\\
0, & k\neq 0.
\end{cases}
$$

> [!summary]
> For an IID process, the ACF is zero at all nonzero lags.

---

# 8. Moving Average Process MA(1)

The first-order moving average process is defined as:

$$
X_t = \mu + \varepsilon_t + \theta \varepsilon_{t-1},
\qquad
\varepsilon_t \sim IID(0,\sigma^2).
$$

---

> [!tip] Intuition
> An MA(1) process depends on:
>
> - the current shock $\varepsilon_t$,
> - the immediately previous shock $\varepsilon_{t-1}$.
>
> So its memory is short (independent on previous value).

---

## 8.1 Mean derivation

$$
E[X_t]
=
E[\mu+\varepsilon_t+\theta\varepsilon_{t-1}]
=
\mu + E[\varepsilon_t] + \theta E[\varepsilon_{t-1}]
=
\mu.
$$

Thus the mean is constant.

---

## 8.2 Variance derivation

Subtract the mean:

$$
X_t-\mu = \varepsilon_t + \theta \varepsilon_{t-1}.
$$

Then

$$
\mathrm{Var}(X_t)
=
\mathrm{Var}(\varepsilon_t + \theta\varepsilon_{t-1}).
$$

Using independence of $\varepsilon_t$ and $\varepsilon_{t-1}$,

$$
\mathrm{Var}(X_t)
=
\mathrm{Var}(\varepsilon_t)
+
\theta^2\mathrm{Var}(\varepsilon_{t-1})
=
\sigma^2 + \theta^2\sigma^2
=
(1+\theta^2)\sigma^2.
$$

So

$$
\gamma(0)=(1+\theta^2)\sigma^2.
$$

---

## 8.3 Lag-1 autocovariance derivation

We compute

$$
\gamma(1)=\mathrm{Cov}(X_t,X_{t+1}).
$$

Using

$$
X_t-\mu=\varepsilon_t+\theta\varepsilon_{t-1},
\qquad
X_{t+1}-\mu=\varepsilon_{t+1}+\theta\varepsilon_t,
$$

we get

$$
\gamma(1)
=
\mathrm{Cov}(\varepsilon_t+\theta\varepsilon_{t-1}, \varepsilon_{t+1}+\theta\varepsilon_t).
$$

Expand:

$$
\gamma(1)
=
\mathrm{Cov}(\varepsilon_t,\varepsilon_{t+1})
+
\theta \mathrm{Cov}(\varepsilon_t,\varepsilon_t)
+
\theta \mathrm{Cov}(\varepsilon_{t-1},\varepsilon_{t+1})
+
\theta^2 \mathrm{Cov}(\varepsilon_{t-1},\varepsilon_t).
$$

By independence, all cross-time covariances are zero except

$$
\mathrm{Cov}(\varepsilon_t,\varepsilon_t)=\sigma^2.
$$

Therefore

$$
\gamma(1)=\theta\sigma^2.
$$

By symmetry,

$$
\gamma(-1)=\theta\sigma^2.
$$

---

## 8.4 Higher-lag autocovariance derivation

For $k\ge 2$, $X_t$ and $X_{t+k}$ share no common innovation terms.

Hence

$$
\gamma(k)=0 \quad \text{for } |k|\ge 2.
$$

---

## 8.5 ACF formula

Therefore,

$$
\rho(1)=\frac{\gamma(1)}{\gamma(0)}
=
\frac{\theta\sigma^2}{(1+\theta^2)\sigma^2}
=
\frac{\theta}{1+\theta^2}.
$$

Thus,

$$
\rho(k)=
\begin{cases}
1, & k=0,\\
\dfrac{\theta}{1+\theta^2}, & |k|=1,\\
0, & |k|\ge 2.
\end{cases}
$$

---

## 8.6 Interpretation

> [!tip]
> The ACF of an MA(1) **cuts off after lag 1**.

This sharp cutoff is the classic signature of an MA(1) process.

---

## 8.7 Extra background: invertibility

A standard condition for MA(1) invertibility is

$$
|\theta|<1.
$$

Invertibility ensures a unique and stable representation in terms of past observed values.

> [!note] MA(1) invertibility
> For the MA(1) model
>
> $$
> X_t = \mu + \varepsilon_t + \theta \varepsilon_{t-1},
> $$
>
> invertibility means we can recover the hidden shock $\varepsilon_t$ from current and past observed values $X_t, X_{t-1}, X_{t-2}, \dots$ in a **unique and stable** way.
>
> Starting from
>
> $$
> X_t-\mu = (1+\theta L)\varepsilon_t,
> $$
>
> where we use lag-operator notation $L^k X_t = X_{t-k}$. We want to invert the operator:
>
> $$
> \varepsilon_t = \frac{1}{1+\theta L}(X_t-\mu).
> $$
>
> This expansion works stably only when
>
> $$
> |\theta|<1.
> $$
>
> Then
>
> $$
> \varepsilon_t
> =
> (X_t-\mu) - \theta(X_{t-1}-\mu) + \theta^2(X_{t-2}-\mu) - \theta^3(X_{t-3}-\mu)+\cdots
> $$
>
> and the coefficients shrink over time.
>
> This matters because without invertibility, different MA(1) parameters can generate the same autocorrelation. In particular,
>
> $$
> \rho(1)=\frac{\theta}{1+\theta^2}
> $$
>
> is the same for $\theta$ and $1/\theta$. So the restriction $|\theta|<1$ selects the unique canonical representation.
>
> > [!summary]
> > Invertibility ensures the MA(1) model is identifiable and that shocks can be recovered from observed data in a stable way.


# 9. Autoregressive Process AR(1)

AR(1) process is defined as:

$$
X_t = \phi X_{t-1} + \varepsilon_t,
\qquad
\varepsilon_t \sim IID(0,\sigma^2).
$$

where

$$
E[X_t]=0, \qquad \rho(k)=\phi^k.
$$
> [!tip] Intuition
> An AR(1) process depends directly on its previous value. So persistence propagates through time. This gives longer memory than MA(1).

---

## 9.1 Stationarity condition

The AR(1) is weakly stationary only if

$$
|\phi|<1.
$$

### Why?

Repeated substitution gives:

$$
X_t
=
\phi X_{t-1}+\varepsilon_t
=
\phi(\phi X_{t-2}+\varepsilon_{t-1})+\varepsilon_t
=
\phi^2X_{t-2}+\phi\varepsilon_{t-1}+\varepsilon_t.
$$

Continuing:

$$
X_t
=
\varepsilon_t+\phi\varepsilon_{t-1}+\phi^2\varepsilon_{t-2}+\cdots+\phi^m X_{t-m}.
$$

As $m\to\infty$, this converges only if $\phi^m\to 0$, i.e.

$$
|\phi|<1.
$$

Then

$$
X_t = \sum_{j=0}^\infty \phi^j \varepsilon_{t-j}.
$$

---

## 9.2 Mean derivation

Take expectation of both sides:

$$
E[X_t]=\phi E[X_{t-1}] + E[\varepsilon_t].
$$

Under stationarity, $E[X_t]=E[X_{t-1}]=\mu$, and $E[\varepsilon_t]=0$. So

$$
\mu = \phi\mu.
$$

Hence

$$
(1-\phi)\mu=0.
$$

If $\phi\neq 1$, then

$$
\mu=E[X_{t}]=0.
$$


> [!note] More generally
> for
>
> $$
> X_t = c + \phi X_{t-1} + \varepsilon_t,
> $$
>
> the stationary mean is
>
> $$
> E[X_t]=\frac{c}{1-\phi}.
> $$

---

## 9.3 Variance derivation

Since $E[X_t]=0$,

$$
X_t=\phi X_{t-1}+\varepsilon_t.
$$

Square both sides:

$$
X_t^2 = \phi^2 X_{t-1}^2 + 2\phi X_{t-1}\varepsilon_t + \varepsilon_t^2.
$$

Take expectations:

$$
E[X_t^2]
=
\phi^2 E[X_{t-1}^2]
+
2\phi E[X_{t-1}\varepsilon_t]
+
E[\varepsilon_t^2].
$$

Because $\varepsilon_t$ is independent of past information, including $X_{t-1}$,

$$
E[X_{t-1}\varepsilon_t]=Cov(X_{t-1}\epsilon_{t})+E[X_{t-1}]E[\epsilon_{t}]=0.
$$

Under stationarity,

$$
E[X_t^2]=E[X_{t-1}^2]=\gamma(0).
$$

So

$$
\gamma(0)=\phi^2\gamma(0)+\sigma^2.
$$

Therefore,

$$
\gamma(0)(1-\phi^2)=\sigma^2,
$$

and

$$
\gamma(0)=\frac{\sigma^2}{1-\phi^2}.
$$

This exists only if $|\phi|<1$.

---

## 9.4 Autocovariance derivation

For $k\ge 1$,

$$
\gamma(k)=\mathrm{Cov}(X_t,X_{t-k}).
$$

Using the AR(1) equation,

$$
X_t=\phi X_{t-1}+\varepsilon_t,
$$

we get

$$
\gamma(k)
=
\mathrm{Cov}(\phi X_{t-1}+\varepsilon_t, X_{t-k}).
$$

Since $\varepsilon_t$ is independent of $X_{t-k}$ for $k\ge 1$,

$$
\gamma(k)=\phi\,\mathrm{Cov}(X_{t-1},X_{t-k})=\phi\gamma(k-1).
$$

So the autocovariances satisfy the recursion:

$$
\gamma(k)=\phi\gamma(k-1).
$$

Iterating,

$$
\gamma(k)=\phi^k\gamma(0).
$$

Hence the ACF is

$$
\rho(k)=\frac{\gamma(k)}{\gamma(0)}=\phi^k.
$$


---

## 9.5 Interpretation

> [!tip]
> The ACF of an AR(1) **decays geometrically**.

- if $0<\phi<1$, the decay is positive and smooth,
- if $-1<\phi<0$, it alternates sign,
- if $|\phi|$ is close to 1, persistence is strong.

---

## 9.6 Infinite MA representation

When $|\phi|<1$,

$$
X_t
=
\varepsilon_t + \phi\varepsilon_{t-1} + \phi^2\varepsilon_{t-2} + \cdots
$$

This representation explains why shocks have a gradually fading impact.

---

# 10. Why Returns Can Be Uncorrelated but Volatility Predictable

This is the deepest conceptual point in the lecture. The slides say:

- returns are uncorrelated,
- squared returns are correlated,
- therefore returns are uncorrelated but not independent,
- and volatility is predictable.

---

## 10.1 Uncorrelated does not imply independent

Independence implies zero covariance, but zero covariance does not imply independence.

So it is possible to have

$$
\mathrm{Corr}(r_t,r_{t-1})=0
$$

while still having

$$
\mathrm{Corr}(r_t^2,r_{t-1}^2)>0.
$$

That is exactly what is seen in financial returns.

---

## 10.2 Conditional heteroskedasticity view

Suppose returns satisfy

$$
r_t = \sigma_t z_t,
$$

where:

- $z_t$ is IID with $E[z_t]=0$, $E[z_t^2]=1$,
- $\sigma_t$ varies over time and depends on past information.

Then

$$
E[r_t \mid \mathcal{F}_{t-1}]
=
E[\sigma_t z_t \mid \mathcal{F}_{t-1}]
=
\sigma_t E[z_t \mid \mathcal{F}_{t-1}]
=
0.
$$

So returns may be unpredictable in the mean.

But

$$
E[r_t^2 \mid \mathcal{F}_{t-1}]
=
E[\sigma_t^2 z_t^2 \mid \mathcal{F}_{t-1}]
=
\sigma_t^2 E[z_t^2]
=
\sigma_t^2.
$$

So volatility is forecastable through the conditional variance.

> [!important]
> This is the mathematical reason volatility models work even when return forecasting is difficult.

---

## 10.3 Relation to volatility clustering

If $\sigma_t^2$ is persistent, then $r_t^2$ will also be persistent on average.

Thus correlated squared returns are evidence of time-varying conditional variance.

---

# 11. Financial Applications

## 11.1 Portfolio allocation

Portfolio weights depend heavily on covariance estimates.

In practice, volatility and covariance modeling are often more useful than trying to forecast mean return precisely.

---

## 11.2 Risk management

Volatility forecasting supports:

- Value-at-Risk,
- Expected Shortfall,
- stress testing,
- capital allocation.

If volatility clusters, a recent shock raises near-term risk estimates.

---

## 11.3 Option pricing

Option values depend strongly on expected future volatility.

Even though Black-Scholes assumes constant volatility, actual markets price options with time-varying and state-dependent implied volatility.

So the lecture's emphasis on time-varying volatility connects directly to derivatives pricing. :contentReference[oaicite:18]{index=18}

---

## 11.4 High-frequency trading

At ultra-high frequencies, small return predictability may exist due to microstructure effects, as noted in the slides. :contentReference[oaicite:19]{index=19}

Applications include:

- market making,
- execution optimization,
- latency-sensitive trading,
- short-horizon statistical arbitrage.

---

## 11.5 Crisis dynamics

The volatility chart in the slides shows large spikes during crisis periods and lower levels during calm periods. :contentReference[oaicite:20]{index=20}

This visually supports:

- time variation,
- clustering,
- mean reversion.

---

# 12. Visual Pattern Recognition for ACF

This is very exam-relevant.

## 12.1 IID

ACF pattern:

- spike at lag 0,
- zero elsewhere.

Interpretation: no serial dependence.

---

## 12.2 MA(1)

ACF pattern:

- spike at lag 1,
- zero for lags 2 and beyond.

Interpretation: dependence only through the most recent innovation.

---

## 12.3 AR(1)

ACF pattern:

- gradual exponential decay.

Interpretation: persistent dependence carried by lagged values.

---

## 12.4 Rule of thumb

> [!tip]
> - **cutoff ACF** → think MA
> - **tapering ACF** → think AR

---

# 13. Exam Traps

> [!warning]
> These are common mistakes.

## Trap 1: Uncorrelated = independent

False.

Returns can be uncorrelated yet dependent in higher moments.

---

## Trap 2: Constant mean implies stationarity

False.

You also need constant variance and lag-based covariance structure.

---

## Trap 3: Volatility clustering means returns are autocorrelated

False.

Usually the clustering appears in:

- squared returns,
- absolute returns,
- conditional variance,

not in signed returns themselves.

---

## Trap 4: AR(1) is always stationary

False.

AR(1) is stationary only if

$$
|\phi|<1.
$$

---

## Trap 5: MA(1) has geometric ACF decay

False.

That is AR(1).  
MA(1) cuts off after lag 1.

---

## Trap 6: Zero ACF means no useful predictability

Not necessarily.

The mean may be unpredictable while variance is still forecastable.

---

# 14. Flashcards

## Definitions

**Q:** What is a time series?  
**A:** A sequence of random variables indexed by time.

**Q:** What is weak stationarity?  
**A:** Constant mean and covariance that depends only on lag, not calendar time.

**Q:** What is autocovariance?  
**A:** $\gamma(k)=\mathrm{Cov}(X_t,X_{t+k})$.

**Q:** What is autocorrelation?  
**A:** $\rho(k)=\gamma(k)/\gamma(0)$ under weak stationarity.

---

## Concepts

**Q:** Why can returns be uncorrelated but volatility predictable?  
**A:** Because zero correlation in returns does not imply independence; dependence can remain in squared returns or conditional variance.

**Q:** What does volatility clustering mean?  
**A:** Large moves tend to be followed by large moves; calm periods tend to be followed by calm periods.

**Q:** Why use squared returns as a volatility proxy?  
**A:** Because both large positive and large negative returns imply high volatility.

---

## Model recognition

**Q:** What is the ACF pattern of IID?  
**A:** Zero at all nonzero lags.

**Q:** What is the ACF pattern of MA(1)?  
**A:** Nonzero at lag 1, zero afterward.

**Q:** What is the ACF pattern of AR(1)?  
**A:** Geometric decay: $\rho(k)=\phi^k$.

---

## Formulas

**Q:** For IID $(\mu,\sigma^2)$, what is $\gamma(k)$?  
**A:** $\gamma(0)=\sigma^2$, and $\gamma(k)=0$ for $k\neq 0$.

**Q:** For MA(1), what is $\rho(1)$?  
**A:** $\rho(1)=\frac{\theta}{1+\theta^2}$.

**Q:** For AR(1), what is $\rho(k)$?  
**A:** $\rho(k)=\phi^k$, assuming $|\phi|<1$.

**Q:** For AR(1), what is $\mathrm{Var}(X_t)$?  
**A:** $\frac{\sigma^2}{1-\phi^2}$, assuming $|\phi|<1$.

---

# 15. Compact Formula Sheet

## Weak stationarity

$$
E[X_t]=\mu
$$

$$
\gamma(k)=\mathrm{Cov}(X_t,X_{t+k})
$$

$$
\rho(k)=\frac{\gamma(k)}{\gamma(0)}
$$

---

## IID

$$
X_t \sim IID(\mu,\sigma^2)
$$

$$
\gamma(k)=
\begin{cases}
\sigma^2, & k=0\\
0, & k\neq 0
\end{cases}
$$

$$
\rho(k)=
\begin{cases}
1, & k=0\\
0, & k\neq 0
\end{cases}
$$

---

## MA(1)

$$
X_t=\mu+\varepsilon_t+\theta\varepsilon_{t-1}, \qquad \varepsilon_t\sim IID(0,\sigma^2)
$$

$$
E[X_t]=\mu
$$

$$
\gamma(0)=(1+\theta^2)\sigma^2
$$

$$
\gamma(1)=\theta\sigma^2
$$

$$
\gamma(k)=0 \quad \text{for } |k|\ge 2
$$

$$
\rho(1)=\frac{\theta}{1+\theta^2}
$$

$$
\rho(k)=0 \quad \text{for } |k|\ge 2
$$

---

## AR(1)

$$
X_t=\phi X_{t-1}+\varepsilon_t, \qquad \varepsilon_t\sim IID(0,\sigma^2)
$$

Stationarity requires:

$$
|\phi|<1
$$

Mean:

$$
E[X_t]=0
$$

Variance:

$$
\gamma(0)=\frac{\sigma^2}{1-\phi^2}
$$

Autocovariance:

$$
\gamma(k)=\phi^k\gamma(0)
$$

Autocorrelation:

$$
\rho(k)=\phi^k
$$

---

# 16. Big Picture Summary

> [!summary]
> This lecture establishes the statistical foundation of volatility modeling.
>
> - Financial returns usually have little linear predictability.
> - Squared returns are persistent.
> - Therefore, returns can be uncorrelated without being independent.
> - Time series tools are needed because financial data are not IID.
> - Weak stationarity provides the basic framework.
> - ACF behavior helps identify dependence patterns.
> - IID, MA(1), and AR(1) are core benchmark processes.
> - These ideas motivate later models of conditional volatility such as [[ARCH]] and [[GARCH]].

---

# 17. Suggested Obsidian Links


[[Mean-Variance Analysis]]
[[CAPM]]
[[Log Returns]]
[[Stationarity]]
[[Autocovariance Function]]
[[Autocorrelation Function]]
[[IID Process]]
[[MA(1)]]
[[AR(1)]]
[[ARCH]]
[[GARCH]]
[[Stochastic Volatility]]
[[Realized Volatility]]
[[Option Pricing]]
[[Risk Management]]
[[High-Frequency Trading]]