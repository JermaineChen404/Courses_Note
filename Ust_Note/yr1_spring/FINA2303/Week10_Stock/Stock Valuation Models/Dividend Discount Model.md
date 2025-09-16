## Initial Assumption: 
The price of the stock is the **future cash flow** to the investor, i.e., discounted present value of future dividends plus future price.

Suppose that the investor has a ***N***-year holding period, and that the investor requires an [[Ust_Note/yr1_spring/FINA2303/Week12_Systematic_Risk_and_Equity_Premium/Systematic Risk and Equity Premium#The Capital Asset Pricing Model (CAPM)|expected rate of return]] of $r_{E}$.
The price is:
$$
   P_0 = \sum_{n=1}^N \frac{D_n}{(1 + r_E)^n} + \frac{P_N}{(1 + r_E)^N}
$$
Here, $P_N$ is not arbitrary, according to the definition of $P_0$, it is the present value of dividends **beyond $N$**:
$$
   P_N = \sum_{n=N+1}^\infty \frac{D_n}{(1 + r_E)^{n-N}}
   $$
Substituting $P_N$ back:
   $$
   P_0 = \sum_{n=1}^N \frac{D_n}{(1 + r_E)^n} + \sum_{n=N+1}^\infty \frac{D_n}{(1 + r_E)^n} = \sum_{n=1}^\infty \frac{D_n}{(1 + r_E)^n}
$$
As $N \to \infty$, 
$$
P_{0}=\lim_{ N \to \infty } \left( \sum_{n=1}^N \frac{D_n}{(1 + r_E)^n} + \frac{P_N}{(1 + r_E)^N} \right)=\sum_{n=1}^\infty \frac{D_n}{(1 + r_E)^n}
$$
Therefore,
$$
\lim_{ N \to \infty } \frac{P_{N}}{(1+r_{E})^N}=0
$$
## Key Takeaway
1. The price of a stock is the discounted present value of its future dividends. $$P_0 = \sum_{n=1}^\infty \frac{D_n}{(1 + r_E)^n}$$ This equation holds for **any** holding period (**No need for $N \to \infty$**).
2. The price does **not** depend on capital gain (future price minus present price).
3. The future price (**$P_N$**) represent the present value (**at time N**) of dividend beyond **N**.
## Dividend Growth
$$
\text{Dividend}=\frac{\text{Earnings}}{\text{Shares Outstanding}}\times \text{Dividend Payout Rate}
$$
### Constant Dividend Growth
The simplest assumption that dividend will grow at constant rate $g$. Therefore. the cash flow of dividends can be treated as a [[Ust_Note/yr1_spring/FINA2303/Week3_Annuity_and_Perpetuity/Perpetuity#Growing Perpetuity|growing perpetuity]] with price (also present price of the stock):
$$
P_{0}=\frac{D_{1}}{r_{E}-g}
$$
### Earning Growth
$$
\Delta\text{Earnings}=\Delta \text{Investment}\times \text{Return on New Investment} \tag{1}
$$
$$
\Delta \text{Investment}=\text{Earnings}\times \text{Retention Rate} \tag{2}
$$
where **Retention Rate=1-Payout Ratio**.
Combining (1) and (2), 
$$
\text{Earnings Growth}=\frac{\Delta \text{Earnings}}{\text{Earning}}=\text{Retention Rate}\times \text{Return on New Investment}
$$
### Dividend Growth V.S.  Earnings Growth
For a given level of the Dividend Payout Rate and Shares  
Outstanding, the growth rate of dividends is **equal** to the growth rate in earnings.

Therefore, the stock price is affected by **two competing effects** of **increasing dividend payouts**:
- **Immediate increase** due to **increased dividends**
- **long-run decrease** due to **decreased dividends growth**
#### Implication
Whether a company should  spend more on investment or on increasing dividends depends on the **profitability of new investment**. Specifically, compare **return on new investment** and **the cost of capital $r_{E}$** (similar to evaluate the [[Net Present Value|NPV]] of the new project).
### Changing Growth Rate
As mentioned in the [[Ust_Note/yr1_spring/FINA2303/Week10_Stock/Stock Valuation Models/Dividend Discount Model#Implication]], companies often change the growth rate of dividends depends on the **profitability of new investment** in different stages or periods  to maximize the stock price.