---
title: L3 - Forwards and Futures on Commodities
course: FINA3203
type: Lecture
tags:
  - fina3203
  - commodities
  - forward_curve
  - contango
  - backwardation
  - convenience_yield
---

![[Pasted image 20250924233022.png]]

## Forward Curve
The forward prices for all available maturities
- Contango (**positive** correlation)
	- [[L2 - Forward and Futures Contracts#^da7c80|r>q]]
- Backwardation (**negative** correlation)
	- [[L2 - Forward and Futures Contracts#^da7c80|r<q]]

## Yield on Forward Price
Along sides with [[L2 - Forward and Futures Contracts#Forward on Stocks with Known Dividend Yield|Dividend Yield]], there can be various positive or negative yield on forward price.
In general,
1. identify price factors
2. summarize as a continuously-compounded rate
3. Incorporate into price formula
	- Cost to carrying the underlying $\to +$
	- Benefit carrying the underlying $\to-$

### Storage Cost
Storage cost can affect commodity forward pricing, serving as a **negative** yield, which is exactly the opposite of a [[L2 - Forward and Futures Contracts#Forward on Stocks with Known Dividend Yield|dividend yield]]

If the commodity has a continuously compounded storage cost $\lambda$, the forward price is
$$F_{0,T}=S_{0}e^{(r+\lambda)T}$$
The forward price increases with maturity $T$, i.e., a Contango.

### Convenience Yield
Holding physically a commodity have an extra value due to higher certainty.

e.g., food production will stop if run out of corn, incurring costs

Therefore, convenience yield $y$ is a positive yield, the same as a dividend yield:
$$F_{0,T}=S_{0}e^{(r+\lambda-y)T}$$
If the convenience yield is large enough, the forward price might decrease with maturity, i.e., a Backwardation

#### Importance
Risk in the commodity market
1. moves in the spot price
2. convenience yield

Convenience yield
- cannot be measured directly
- changes with economic conditions
- change the slope of the forward curve
- tricky to hedge

## Trading the Slope of Forward Curve
Forward curve for the same period is different everyday given new prices (info)

We can bet on the changes of forward curve (slope) for a given period by:
- long the near-term and short the distant forward
	- if predict the curve changes from contango to backwardation
- short the near-term and long the distant forward
	- if predict the curve changes from contango to backwardation

### Example
Consider a **contango** forward with
- $S_{0}=22$
- $F_{0,1}=23$
- $F_{0,2}=24$

We predict it to turn backwardation.

- long a one-month forward at time 0
	- $S_{1}-F_{0,1}$ at time 1 
- short a two-month forward at time 0
	- $F_{0,2}-S_{2}$ at time 2
- long a one-month forward at time 1
	- $S_{2}-F_{1,2}$ at time 2

Ignore the discount of payoff from time 1 and time 2, the total payoff is
$$
\begin{align}
(S_{1}-F_{0,1})+(F_{0,2}-S_{2})+(S_{2}-F_{1,2})&=(F_{0,2}-F_{0,1})-(F_{1,2}-S_{1}) \\
&=(\text{Slope at time 0})-(\text{Slope at time 1})
\end{align}
$$
By definition,
$$S_{1}\equiv F_{1,1}$$
Essentially, we are shorting the slope of the forward curve within period 1-2, expecting the curve of this period go from contango at time 0 to backwardation at time 1.

### Case Study: Metallgesellschaft (MG)
[[Case Study: Metallgesellschaft (MG)]]

#### Stack-and-Roll Strategy



