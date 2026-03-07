---
title: L2 - Forward and Futures Contracts
course: FINA3203
type: Lecture
tags:
  - fina3203
  - forward_contracts
  - futures_contracts
  - forward_price
---

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
> Assume the risk-free rate is ==$r=5\%$== p.a. in continuous compounding.

- It's already long the stock!
- It wants to be **short** the stock and **long** the risk-free asset
	- Short sell the stocks (or short a forward contract)
	- Invest the cash proceeds in the risk-free asset
### Establish position in Forward
- It enters a forward contract in which it agrees to **sell** the stock at time $T$ for a price of $F_{0,T}$
- By going short forward, the hedge fund essentially holds a synthetic risk-free bond with face value
$$N_{0}\times F_{0,T}=10,000\times F_{0,T}$$
- By buying a zero-coupon bond today, the present value is $$PV=10,000\times F_{0,T}\times e^{-rT}$$

#### Value of Bond at Maturity
| scenario                     | stock                 | forward                                     | total           |
| ---------------------------- | --------------------- | ------------------------------------------- | --------------- |
| if $S_{T}$                   | $N_{0}\times S_{T}$   | $-N_{0}\times(S_{T}-F_{0,T})$               | $N_{0}\times F_{0,T}$  |
| known at $t_{0}$             | $N_{0}\times S_{0}$   | $N_{0}\times(F_{0,T}-S_{0})$ | $N_{0}\times F_{0,T}$  |
| known at $t_{0}$ in PV terms | $N_{0}\times S_{0}$ | $N_{0}\times(F_{0,T}-S_{0})$ | $N_{0}\times F_{0,T}\times e^{-rT}$ |

>[!Caution]
>At $t=0$, the values of both the stock and the forward are known, while the value of the synthetic bond is ==**unknown**== since the forward contract has **no liquid market**. All we know is it **must** worth $N_{0}\times F_{0,T}$ at the maturity date. So the PV is known.
>
>However, $N_{0}\times F_{0,T}\times e^{-rT}$ has to equal $N_{0}\times(S_{0}-0)$ to rule out the arbitrage opportunities. 


> [!important] Forward Price
> $$F_{0,T}=S_{0}\times e^{rT}$$
> - PV of forward price = Spot price at time 0
> $$PV[F_{0,T}]=F_{0,T}\times e^{-rT}=S_{0}$$
> - [[#^d8f4e2|When Stock with Dividend]]

^da7c80

---

## Forward on Stocks with Known Dividend Yield
Yield is known (e.g., 3%) but dividend is unknown (e.g., 3%\*S)

> [!Assumption]
> At some future times $t_{1}, \ldots t_{k}$ between $t_{0}$ and $T$ (i.e., $t_{0}<t_{1}<\ldots<t_{k}<T$), stock will pay $N_{0}\times D_{t_{i}}$ dividends *per share*, where $D_{t_{i}}$ is known at $t_{0}$. Let $D_{0,T}$ denotes the **present value** at time $t_{0}$ of all these dividends.

| scenario         | long forward                         | short stock                  | Invest $(S_{0}-D_{0,T})$ in risk-free rate                              |
| ---------------- | ------------------------------------ | ---------------------------- | ----------------------------------------------------------------------- |
| today in $ | $0$                                  | $+N_{0}\times S_{0}$         | $-N_{0}\times S_{0}+N_{0}\times D_{0,T}$                                |
| at $T$ in $      | $+N_{0}\times(S_{T}-F_{0,T})$        | $-N_{0}\times(S_{T}-D_{0,T}e^{rT})$ | $+N_{0}\times(S_{0}-D_{0,T})\times e^{rT}$                              |
|                  |                                      |                              | ==$+N_{0}\times(S_{0}e^{rT}-D_{0,T}e^{rT})$==                           |
| in total at $T$  | $N_{0}\times(S_{0}-D_{0,T})e^{rT}-N_{0}\times F_{0,T}$ |                              |                                                                         |
| Arbitrage if $>$ | sell forward, short stock, invest    |                              |                                                                         |
| Arbitrage if $<$ | buy forward, long stock, borrow cash |                              |                                                                         |

> [!important] Forward Price
> $$\begin{align*}F_{0,T}&=(S_{0}-D_{0,T})e^{rT}\\&=S_{0}e^{rT}-D_{0,T}e^{rT}\end{align*}$$
> - The forward price should equal the future value at $T$ of buying the stock today (which costs $S_{0}$) and **subtracting the dividends** that you will receive along the way (which have a total present value $D_{0,T}$).
> - If [[#^da7c80|Stock pays no Dividend]], then $D_{0,T}=0$
> - Stock price should drop by the amount of dividend right after declaring
> $$S_{\text{ex}}=S_{\text{cum}}-D$$

^d8f4e2

### Continuous Dividends

> [!Assumption]
> Stock pays dividends continuously at the yield of $q$

- where $q$ is a continuously compounded annual rate.
- the present value of the dividends to be collected is $$D_{0,T}=S_{0}\times(1-e^{-qT})$$

> [!important] Forward Price
> $$\begin{align*}F_{0,T}&=(S_{0}-D_{0,T})e^{rT}\\&=S_{0}e^{(r-q)T}\end{align*}$$
> - If $r>q$, forward price is an ==increasing== function of maturity
> - If $r<q$, forward price is an ==decreasing== function of maturity
> - If $r=q$, forward price is a ==constant== function of maturity

---

## Features of Forward contracts
- customized products between 2 counterparties
- transacted in over-the-counter (OTC) markets
	- no standardized contract terms (strike date and maturity)
	- no centralized trading platform
- allow for **credit risk**
	- one party can default (the one with negative payoff at maturity)

## Future contracts
- standardized contracts (including contract size, maturity etc.)
- traded in an exchange
	- liquid in buying and selling
	- centralized clearinghouse serves as the counterparty to both sides of the transaction
- greatly reduces credit risks via the ==mark-to-market== mechanism
	- at the end of each trading day, gains and losses from the day's price movements are removed from the margin account

### Differences: Forward vs. Future
| feature                | forward                   | future                                  |
| ---------------------- | ------------------------- | --------------------------------------- |
| credit risk            | depends on counterparty   | tiny due to margin                      |
| frequency of cashflows | once (at maturity)        | daily (gain / loss from margin account) |
| contract terms         | fully customizable        | fully standardized                      |
| early termination      | difficult                 | easy (close position)                   |
| pricing                | forward price $F_{0,T}$   | future price $\overline{F}_{0,T}$       |

### Margin Account
- The exchange requires each party to **post** and maintain a **margin account** to cover (a part of) the obligations it has under the contract (in case the party defaults)
- If the balance in the margin account **fall below** the required amount, the party gets a **margin call** and will **have to deposit additional funds** to replenish the account **by the next business day**
- If he cannot replenish the account, his position will be **closed out immediately** by the clearinghouse, the loss is capped at most the margin left.

### Future Price
$$\overline{F}_{0,T}=F_{0,T}$$
when
- interest rate is **constant** within the maturity span OR
- future price is **uncorrelated** with the interest rate