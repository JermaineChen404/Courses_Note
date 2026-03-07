---
title: L5 - Forwards and Futures on Interest Rates
course: FINA3203
type: Lecture
tags:
  - fina3203
  - interest_rates
  - forward_rate
  - fra
  - repo
  - convergence_trade
---

# Forward Interest Rate
>[!Forward Rate]
> At $t_{0}$, what the market thinks of the interest rate from $t_{1}$ to $t_{2}$
>- denoted as $f_{t_{0},t_{1},t_{2}}$
>- known at $t_{0}$ and is expected to be earned from $t_{1}$ to $t_{2}$
>- continuously compounded and quoted in annualized terms

By definition,
$$f_{t_{0},t_{1},t_{2}}=\frac{1}{t_{2}-t_{1}}[r_{t_{0},t_{2}}\times(t_{2}-t_{0})-r_{t_{0},t_{1}}\times(t_{1}-t_{0})]$$

To hedge the interest rate risk, we can lock in the forward rate as our future interest rate by investing in forward rate.

## Investing in Forward Rate
### Synthetic Investment
At $t_{0}$,
- short a T-Bill of $t_{1}$ at $r_{t_{0},t_{1}}$
	- $+N_{0}\times e^{-r_{t_{0},t_{1}}(t_{1}-t_{0})}$
- long a T-Bill of $t_{2}$ at $r_{t_{0},t_{2}}$
	- $-N_{0}\times e^{-r_{t_{0},t_{1}}(t_{1}-t_{0})}$
- $=0$

At $t_{1}$,
- The short position matures
	- $-N_{0}$

At $t_{2}$,
- The long position matures
	- $+N_{0}\times e^{-r_{t_{0},t_{1}}(t_{1}-t_{0})}\times e^{r_{t_{0},t_{2}}(t_{2}-t_{1})}$
- $=N_{0}\times e^{r_{t_{0},t_{2}}(t_{2}-t_{1})-r_{t_{0},t_{1}}(t_{1}-t_{0})}=N_{0}\times e^{f_{t_{0},t_{1},t_{2}}(t_{2}-t_{1})}$

Overall, we effectively short the forward rate from $t_{1}$ to $t_{2}$

![[Pasted image 20251014201618.png]]

### Forward Rate Agreement (FRA)
FRAs are [[L1 - Intro to Derivatives#Over-The-Counter (OTC) Derivative|OTC]] contracts that guarantee a borrowing or lending rate
- on a given notional principal amount
- at a future date
- for a specific period

FRA payoff for the long position:
$$N_{0}\times\left( \frac{(r_{t_{1},t_{2}}-r^{FRA}_{t_{0},t_{1},t_{2}})\times(t_{2}-t_{1})}{1+r_{t_{1},t_{2}}\times(t_{2}-t_{1})} \right)$$
where $r_{t_{1},t_{2}}$ is the interest rate in the future (unknown today).
- $r_{t_{1},t_{2}}$ and $r^{FRA}_{t_{0},t_{1},t_{2}}$ are all annualized [[L2 - Forward and Futures Contracts#Interest Rate|simple interest rate]].
- an FRA at $t_{0}$ for $t_{1}$ to $t_{2}$ pays off at $t_{1}$
- $r^{FRA}_{t_{0},t_{1},t_{2}}=f_{t_{0},t_{1},t_{2}}$ according to No Arbitrage Principle (==adjustment needed==)


|Position|Goal|Expectation/Hedge|
|---|---|---|
|**Short FRA**|Fix Lending/Investing Rate|**Fall** in interest rates|
|**Long FRA**|Fix Borrowing Rate|**Rise** in interest rates|

#### Short FRA
We want to invest $N_{0}$ from $t_{1}$ to $t_{2}$ at the fixed FRA rate

At $t_{1}$,
- Invest $N_{0}$
	- $-N_{0}$
- short FRA
	- $-N_{0}\times\left( \frac{(r_{t_{1},t_{2}}-r^{FRA}_{t_{0},t_{1},t_{2}})\times(t_{2}-t_{1})}{1+r_{t_{1},t_{2}}\times(t_{2}-t_{1})} \right)$
- Offset the short position by invest/borrow
	- $+N_{0}\times\left( \frac{(r_{t_{1},t_{2}}-r^{FRA}_{t_{0},t_{1},t_{2}})\times(t_{2}-t_{1})}{1+r_{t_{1},t_{2}}\times(t_{2}-t_{1})} \right)$
- $=-N_{0}$

At $t_{2}$,
- Gain from $N_{0}$ investment
	- $N_{0}\times(1+r_{t_{1},t_{2}}(t_{2}-t_{1}))$
- Gain/Pay from/for the offset
	- $-N_{0}\times\left( \frac{(r_{t_{1},t_{2}}-r^{FRA}_{t_{0},t_{1},t_{2}})\times(t_{2}-t_{1})}{1+r_{t_{1},t_{2}}\times(t_{2}-t_{1})} \right)\times(1+r_{t_{1},t_{2}}(t_{2}-t_{1}))$
	- $=-N_{0}\times[(r_{t_{1},t_{2}}-r^{FRA}_{t_{0},t_{1},t_{2}})\times(t_{2}-t_{1})]$
- $=N_{0}\times[1+r^{FRA}_{t_{0},t_{1},t_{2}}(t_{2}-t_{1})]$

#### Long FRA
We want to borrow from $t_{1}$ to $t_{2}$ at the fixed FRA rate

At $t_{1}$,
- Borrow $N_{0}$
	- $+N_{0}$
- long FRA
	- $N_{0}\times\left( \frac{(r_{t_{1},t_{2}}-r^{FRA}_{t_{0},t_{1},t_{2}})\times(t_{2}-t_{1})}{1+r_{t_{1},t_{2}}\times(t_{2}-t_{1})} \right)$
- Offset the long position by invest/borrow
	- $-N_{0}\times\left( \frac{(r_{t_{1},t_{2}}-r^{FRA}_{t_{0},t_{1},t_{2}})\times(t_{2}-t_{1})}{1+r_{t_{1},t_{2}}\times(t_{2}-t_{1})} \right)$
- $=+N_{0}$

At $t_{2}$,
- Payment to $N_{0}$ debt
	- $-N_{0}\times(1+r_{t_{1},t_{2}}(t_{2}-t_{1}))$
- Gain/Pay from/for the offset
	- $N_{0}\times\left( \frac{(r_{t_{1},t_{2}}-r^{FRA}_{t_{0},t_{1},t_{2}})\times(t_{2}-t_{1})}{1+r_{t_{1},t_{2}}\times(t_{2}-t_{1})} \right)\times(1+r_{t_{1},t_{2}}(t_{2}-t_{1}))$
	- $=N_{0}\times[(r_{t_{1},t_{2}}-r^{FRA}_{t_{0},t_{1},t_{2}})\times(t_{2}-t_{1})]$
- $=-N_{0}\times[1+r^{FRA}_{t_{0},t_{1},t_{2}}(t_{2}-t_{1})]$

### Repo Transactions
Repurchase Agreement (repo):
- borrow cash against the security as a collateral
- obtain cash funding

Reverse Repo: 
- lending cash accepting securities as collateral
- invests risk-free since the collaterals are mostly T-Bill

![[Pasted image 20251015012113.png]]

>[!tip] Forward Equivalent
>- long a forward  $\iff$ buy a security and repo it
>- short a forward $\iff$ borrow a security by reverse-repo it and sell it

>[!Haircut]
>the difference between the market value of the collateral and the notional amount of the loan

#### Convergence Trade
>[!On-the-run]
>newly issued

|   |liquidity|price|risk|original maturity|
|---|---|---|---|---|
|on-the-run 30-year Treasury bond|high|high|US gov|30 y|
|off-the-run 29.5-year Treasury bond|low|low|US gov|30 y|

>[!arbitrage opportunity]
>The price spread due to the liquidity only lasts for a short period, i.e., their prices will converge soon.

1. Buy off-the-run bond and repo it
	- long the underpriced
2. Borrow on-the-run bond by entering into a reverse repo and sell it
	- short the overpriced
3. earn the spread after their prices converges

Repo/reverse repo allow us to long/short a bond without entry cost

# Case Study: LTCM
huge leverage on "little risk" arbitrage spread trade.




