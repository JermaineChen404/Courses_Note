---
title: L9 - Binomial Tree Models
course: FINA3203
type: Lecture
tags:
  - fina3203
  - binomial_tree
  - pricing
  - risk_neutral
  - hedging
---
# Binomial Tree Models
>[!Note] Pricing
>
>>[!check] Asset Pricing
>>The price of any asset is the present value of its expected future value (or cash flows) using a risk-adjusted discount rate
>>
>>$$S_{0}=e^{-\mu T}\mathbb{E}_{0}[S_{T}]$$
>>
>>Since the asset itself carries risk that cannot be perfectly hedged, investors demand compensation for bearing the risk. The discount rate reflects both the time value of money and the risk premium.
>
>>[!check] Derivative Pricing
>>The price of a derivative is determined by the cost of replicating or hedging its payoff. 
>>Traders sell and hedge derivative immediately, since they do not want to bear the fundamental risks that are on the other side of their clients. Instead, they only charge a mark-up for providing liquidity.

## One Step Binomial Tree
![[Pasted image 20251214210128.png]]

Consider a call option with payoff as shown above. 
## Cost of Hedging Pricing
Since there are only two possible outcomes, we can always construct a portfolio of two securities **(long $\Delta$ of shares and short the option )** with **no uncertainty about the final value (riskless)**. The portfolio is riskless if the final value of the portfolio is the same for both alternative.

$$S_{0}u\Delta-f_{u}=S_{0}d\Delta-f_{d}$$

or

$$\Delta=\frac{f_{u}-f_{d}}{S_{0}u-S_{0}d}$$

In this case, the portfolio is riskless and, for there to be no arbitrage opportunities, it must earn the risk-free interest rate.

If we denote the risk-free interest rate by $r$, the present value of the portfolio is

$$(S_{0}u\Delta-f_{u})e^{-rT}$$

The cost of setting up the portfolio is

$$S_{0}\Delta-f$$

From no arbitrage principle, it follows that

$$(S_{0}u\Delta-f_{u})e^{-rT}=S_{0}\Delta-f$$

Substituting $\Delta$, we obtain the current price of the option

$$f=\frac{f_{u}(1-de^{-rT})+f_{d}(ue^{-rT}-1)}{u-d}$$

or

$$f=e^{-rT}[pf_{u}+(1-p)f_{d}]$$

where

$$p=\frac{e^{rT}-d}{u-d}$$

The **only** assumption needed for the equation is that there are **no arbitrage opportunities** in the market.

>[!question] Irrelevance of the Stock's Expected Return
>The option pricing formula obtained does not involve the probabilities of the stock price moving up or down. Why?
>
>- Knowing $S_{0}u$ and $S_{0}d$ is enough for perfectly hedging (replicating) the option
>- We are calculating its value in terms of the price of the underlying stock. The probabilities of future up or down movements are already incorporated into the stock price: we do not need to take them into account again when valuing the option in terms of the stock price.

## Risk-Neutral Pricing
We introduce a risk-neutral world where investors are risk-neutral as opposed to risk-averse.

>[!note] Risk-Averse
>People dislike risk and thus require a higher expected return as a compensation for increased risks. In the real world, people are risk-averse.

In the risk-neutral world,

- The expected return on any assets is the risk-free rate
- The discount  rate used for the expected payoff on any derivatives is the risk-free rate

Previously we obtain the present value of an option

$$f=e^{-rT}[pf_{u}+(1-p)f_{d}]$$

where

$$p=\frac{e^{rT}-d}{u-d}$$

is the probability of an up movement **in a risk-neutral world**

and

$$pf_{u}+(1-p)f_{d}=\mathbb{E}_{0}^{*}[f_{T}]$$

is the expected future payoff from the option in a risk-neutral world.

Thus, 

$$f=e^{-rT}\mathbb{E}_{0}^{*}[f_{T}]$$

which states that the value of the option today is its expected future payoff in a risk-neutral world discounted at the risk-free rate.



>[!note]
>Since $p$ is the probability of an up movement **in a risk-neutral world**, the expected stock price is given by
>
>$$\mathbb{E}[S_{T}]=pS_{0}u+(1-p)S_{0}d$$
>
>Substituting for $p$ gives
>
>$$\mathbb{E}[S_{T}]=S_{0}e^{rT}$$
>
>which means the stock price grows, on average, **at the risk-free rate** as well in the risk-neutral world.

**The price we obtain in the risk-neutral world is the right price in all world (in the real world)**

- It **has been proved to be true** assuming a simple binomial model for how the stock price evolves
- It is **also true** regardless of the assumptions made about the evolution of the stock price

### Forward Revisited
The payoff at $T$ from a forward contract is

$$G(S_{T})\equiv S_{T}-F_{0,T}$$

The value of a forward today is zero, and according to the conclusion above

$$e^{-rT}\times \mathbb{E}_{0}^{*}[S_{T}-F_{0,T}]=0$$

Thus

$$F_{0,T}=\mathbb{E}_{0}^{*}[S_{T}]=S_{0}\times e^{rT}$$

i.e., The forward price is the risk-neutral expectation of the underlying price at $T$

$$F_{0,T}=\mathbb{E}_{0}^{*}[S_{T}]\neq \mathbb{E}_{0}[S_{T}]$$

However, with the real expectation:

$$E[S_{T}]=S_{0}\times e^{\mu T}$$

We could see the forward price in a different way

$$F_{0,T}=e^{-(\mu-r)T}E[S_{T}]$$

i.e., the expected future stock price, discounted at the excess rate of return $(\mu-r)$

### Swaps Revisited
In a swap, two counter-parties agree to exchange cashflows at $T_{1},T_{2},\dots,T_{n}$

$$\text{Cash Flow at }T_{i}\equiv G(S_{T_{i}})=S_{T_{i}}-x$$

The Value of the swap at time $0$ is 

$$V_{0}=\sum_{i=1}^{n}e^{-rT_{i}} E_{0}^{*}[S_{T_{i}}-x]$$

Since $F_{0,T}=E_{0}^{*}[S_{T}]$,

$$V_{0}=\sum_{i=1}^{n}e^{-rT_{i}} (F_{0,T_{i}}-x)$$

To solve for $x$, we set $V_{0}=0$ and obtain

$$x=\sum_{i=1}^{n}w_{i}F_{0,T_{i}}\quad \text{where}\quad w_{i}=\frac{e^{-rT_{i}}}{\sum_{i=1}^{n}e^{-rT_{i}}}$$
