## Forward contracts
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
> [!Case]
> A hedge fund owns 10,000 shares of firm A, each trading at ==$S_{0}=\$100$== now.
>
> It wants to clear the entire position in A and replace it with zero-coupon bonds with maturity ==$T=1.8$== years.
> 
> The interest rate today is ==$r_{0}=5\%$==

> [!Problem]
> - large transaction costs
> - market liquidation issues
> - maturity mismatch with standardized bonds traded on exchanges

> [!Solution]
> short a forward contract with forward price ==$F_{0,T}=\$109$== at ==$T=1.8$==

![[Ust_Note/yr2_Fall/FINA3203/attachments/Pasted image 20250915150042.png]]
- The future stock price $S_{T}$ is unknown but canceled out.
- The final payoff $N_{0}\times F_{o,T}$ is independent of $S_{T}$ and risk-free (certain)
- The $F_{0,T}$ is constructed to make the final payoff equivalent to that of a risk-free zero-coupon bond with an interest rate $r_{0}=5\%$
- Thereby the fund achieve an equivalent effect of a zero-coupon bond with $r_{0}=5\%$

## The Forward Price 
Why will the buyer agree on the forward price $F_{0,T}$ in the previous example?
- According to the no arbitrage principle (law of one price), the discount rate to get $F_{0,T}$ has to equal the market interest rate

i.e.
$$F_{0,T}=S_{0}\times e^{r_{0}T}$$
---
Another way to consider the forward price is by **replicating portfolio**


### Interest Rate
- Simple interest rate $r_{0}^S$
	- $r_{0}^S=\frac{1}{T}\left( \frac{FV}{S}-1 \right)$
	- $FV=S(1+r_{0}^ST)$
- Continuously-compounded rate ([[Ust_Note/yr2_Fall/FINA3203/L2 - Forward and Futures contracts#Log-Return|log-return]]) $r_{0}$
	- $r_{0}=\frac{1}{T}\left( \ln \frac{FV}{S_{0}} \right)$
	- $FV=Se^{r_{0}T}$
	- $S=FVe^{-r_{0}T}$









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
