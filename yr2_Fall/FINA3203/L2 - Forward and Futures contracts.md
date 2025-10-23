# Forward contracts
> [!Definition] Forward price $F_{0,T}$:
> the price set to ensure that the value of the forward contract equals zero for both parties at the inception of the contract

>[!Definition] Notional value $N_{0}\times S_{0}$
> total market value of the underlying today

$S_{T}$: the spot price at time $T$
- payoff to long forward contract = $N_{0}\times(S_{T}-F_{0,T})$
- payoff to short forward contract = $N_{0}\times(F_{0,T}-S_{T})$
- imaging the buyer pay at $F_{0,T}$ to complete the contract and sell the underlying immediately at price $S_{T}$

Forward is a zero-sum game
- only one party profits and the other lose money

## Synthetic Zero-Coupon Bond
> [!Background]
> A hedge fund owns 10,000 shares of firm A, each trading at ==$S_{0}=\$100$== now.
>
> It wants to clear the entire position in A and replace it with zero-coupon bonds with maturity ==$T=1.8$== years.
> 
> The interest rate today is ==$r_{0}=5\%$==

> [!Warning] Problem
> - large transaction costs
> - market liquidation issues
> - maturity mismatch with standardized bonds traded on exchanges

> [!Success] Solution
> short a forward contract with forward price ==$F_{0,T}=\$109$== at ==$T=1.8$==

![[Ust_Note/yr2_Fall/FINA3203/attachments/Pasted image 20250915150042.png]]
- The future stock price $S_{T}$ is unknown but canceled out.
- The final payoff $N_{0}\times F_{o,T}$ is independent of $S_{T}$ and risk-free (certain)
- The $F_{0,T}$ is constructed to make the final payoff equivalent to that of a risk-free zero-coupon bond with an interest rate $r_{0}=5\%$
- Thereby the fund achieve an equivalent effect of a zero-coupon bond with $r_{0}=5\%$

## Forward Price
Why will the buyer agree on the forward price $F_{0,T}$ in the previous example?
- According to the no arbitrage principle (law of one price), the discount rate to get $F_{0,T}$ has to equal the market interest rate

i.e.
$$F_{0,T}=S_{0}\times e^{r_{0}T}$$
---
> Another way to consider the forward price is by **replicating portfolio**

There are three products in the market at time 0
- a forward contract with ==market forward price $F_{0,T}$== 
-  the underlying with ==current market price $S_{0}$==
- zero-coupon bonds with ==interest rate $r_{0}$==

We can construct two portfolios
- Portfolio 1: enter a long position of a forward contract

|Portfolio holdings | Payoffs at time 0 | Payoffs at time T|
|---|---|---|
| Long forward|0|$N_{0}\times(S_{T}-F_{0,T})$|

- Portfolio 2: 
	- long the underlying
		- buy the underlying at time 0 and sell it at time T
	- short bonds (borrow money)
		- receive proceeds at time 0 and repay it at time T

| | Portfolio holdings | Payoffs at time 0 | Payoffs at time T|
|---|---|---|---|
|Portfolio 2| Long underlying|$-N_{0}\times S_{0}$|$N_{0}\times S_{T}$|
||Short bonds|$N_{0}\times F_{0,T}\times e^{-r_{0}\times T}$|$-N_{0}\times(S_{T}-F_{0,T})$
||Total|$N_{0}\times(F_{0,T}\times e^{-r_{0}\times T}-S_{0})$|$N_{0}\times(S_{T}-F_{0,T})$

Two portfolios have the same payoffs at time T,

- if $F_{0,T}>S_{0}\times e^{r_{0}\times T}$
	- The forward is overpriced
		- short portfolio 1 and long portfolio 2
- if $F_{0,T}<S_{0}\times e^{r_{0}\times T}$
	- The forward is underpriced
		- long portfolio 1 and short portfolio 2

according to the no arbitrage principle, they must have the same payoffs at time 0

> i.e., $F_{0,T}\times e^{-r_{0}\times T}-S_{0}=0 \iff F_{0,T}=S_{0}\times e^{r_{0}\times T}$

## Forward Price $\neq$ Expected Future Price
$$F_{0,T}=S_{0}\times e^{r_{0}\times T}$$
The forward price  **only** use information from the current spot markets and therefore cannot predict future spot price.

The expected log-return of the underlying $\mu_{0}$ is defined as
$$E_{0}[S_{T}]=S_{0}\times e^{\mu_{0}T}$$
> Risk Premium: $\mu_{0}-r_{0}$
- risky underlying $\to$ positive

## Value of Forward Contract
Consider **shorting** a forward

At time 0, $V=0$
- it costs nothing to enter a forward

At maturity T, $V=F_{0, T}-S_{T}$
- the value equals the final payoff

At time $0<t<T$, the value is the present value of the final payoff if we cancel the forward contract now.

> Cancel a forward contract $\iff$ Enter a reverse contract

We **long** a forward contract which also matures at time $T$ and have a forward price $F_{t,T}$ today at time $t$
$$F_{t,T}=S_{t}\times e^{r(T-t)}$$
The final payoff is $N_{0}\times(S_{T}-F_{t,T})$. The combined final payoff is
$$N_{0}\times(F_{0,T}-S_{T})+N_{0}\times(S_{T}-F_{t,T})=N_{0}\times(F_{0,T}-F_{t,T})$$
Therefore, the value of the short forward contract at time $t$ is
>$$e^{-r(T-t)}\times N_{0}\times(F_{0,T}-F_{t,T})$$

and vice versa for long position
$$e^{-r(T-t)}\times N_{0}\times(F_{t,T}-F_{0,T})$$
---
Alternatively, replicating the portfolio we have

||t|T|
|---|---|---|
|original long position|Value|$S_{T}-F_{0,T}$|

||t|T|
|---|---|---|
|new long position|0|$S_{T}-F_{t,T}$|
|PV of future payoff|$e^{-r(T-t)}(F_{t,T}-F_{0,T})$|$F_{t,T}-F_{0,T}$|
|Synthetic payoff|0|$S_{T}-F_{0,T}$|

Therefore, the value of the original long position at time $=t$ is 
$$e^{-r(T-t)}\times N_{0}\times(F_{t,T}-F_{0,T})$$

## Forward on Stocks with Known Dividend Yield
Assume a continuously-compounded dividend yield $q$
- to have 1 share at time $T$, I need $e^{-q\times T}$ at time 0
	- Incorporate the effect of dividend in the quantity instead of the price
		- value = quantity $\times$ price

![[Pasted image 20250924222548.png]]

Again from **no arbitrage principle**
$$S_{0}\times e^{-q\times T}-F_{0,T}\times e^{-r\times T}=0$$
i.e.
$$F_{0,T}=S_{0}\times e^{(r-q)\times T}$$ ^da7c80

# Future Contracts
Similar to forward contracts except
- [[L1 - Intro to Derivatives#Exchange-Traded Derivative (ETD)|traded on an exchange]]
- standardized (with respect to size, maturity, underlying)
	- reduce liquidity risk
	- but introduce inefficient mismatch between buyers and sellers
- P/L are [[L2 - Forward and Futures Contracts#Margin Requirement|marked to market]] (daily settlement)

## Future Prices
Similar to the [[L2 - Forward and Futures Contracts#Forward Price|forward price]], the future price at time $t$ is represented by $\hat{F}_{t,T}$.

As the future price moves, profits and losses accrue to both counterparty

For ==buyer (long position)==
$$\text{Daily P\&L}=\text{Contract Size}\times(\hat{F}_{t,T}-\hat{F}_{t-1,T})$$
and vice versa for sellers

## Margin Requirement

```mermaid
flowchart LR

Buyers<-->|Daily P/L|Exchange
Exchange<-->|Daily P/L|Sellers

```

- Both counterparties must set up collateral with the exchange
- At the close of each day traders pay losses (out of their margin accounts) or receive gains (credited to their margin accounts)
- If the amount in the trader’s account falls below a [[L1 - Trading Securities#Buying on Margin|maintenance margin]], the exchange issues a [[L1 - Trading Securities#Buying on Margin|margin call]]
- The trader must post additional collateral to restore the initial margin if he wants to keep the position open. Otherwise the position is closed by the exchange
- Therefore, the exchange does not take any risks

# Appendix
## Interest Rate
- Simple interest rate $r_{0}^S$
	- $r_{0}^S=\frac{1}{T}\left( \frac{FV}{S}-1 \right)$
	- $FV=S(1+r_{0}^ST)$
- Continuously-compounded rate ([[L2 - Forward and Futures Contracts#Log-Return|log-return]]) $r_{0}$
	- $r_{0}=\frac{1}{T}\left( \ln \frac{FV}{S_{0}} \right)$
	- $FV=Se^{r_{0}T}$
	- $S=FVe^{-r_{0}T}$

Conversion between simple interest rate and log-return:
$$1+r_{0}^s=e^{r_{0}T}$$
## Log-Return
[Log-return](https://gregorygundersen.com/blog/2022/02/06/log-returns/) are defined as
$$z_{t}=\ln(1+r_{t})=\ln\left( \frac{p_{t}}{p_{t-1}} \right)$$

Log-return is a good approximation of raw return when returns are close to 0 since
$$\ln(1+x)\approx x$$
when $x\to 0$

Given
$$r_{0:T}=\frac{p_{T}}{p_{0}}-1=\prod_{t=1}^T(1+r_{t})-1$$
 Consider

$$
\begin{align}
z_{0:T}&=\ln(1+r_{0:T}) \\
&=\sum_{t=1}^T\ln(1+r_{t}) \\
&=\sum_{t=1}^T\ln\left( \frac{p_{t}}{p_{t-1}} \right) \\
&=\ln p_{T}-\ln p_{0} \\
&=z_{T}-z_{0}
\end{align}
$$
We use **log returns** when we are **doing quantitative analysis, modeling, and working with data over time**. Their additivity, symmetry, and better statistical properties make them the superior choice for computational finance, portfolio theory, and derivatives pricing.
