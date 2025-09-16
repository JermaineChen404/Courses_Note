## Returns on a Portfolio
The return on a portfolio is the weighted average of the individual returns on the stocks that comprise the portfolio, where the weights are the portfolio weights. i.e., $$r_{p}=\sum_{i=1}^Nw_{i}r_{i}$$ is the realized return. Similarly, $$\mathbb{E}[r_{p}]=\sum_{i=1}^Nw_{i}\mathbb{E}[r_{i}]$$ is the expected return.
## Correlation
Return correlation $\rho \in[-1,1]$ captures co-movement between two stocks’ returns.
In general, for a N-stock portfolio, the portfolio return variance is $$Var(r_{p})=\sum_{i=1}^N\sum_{j=1}^N\rho_{ij}w_{i}w_{j}SD(r_{i})SD(r_{j})$$
- Lower $\rho$, lower $Var(r_{p})$
- Higher $N$, lower $Var(r_{p})$
- $Var(r_{p})$ will **never** tend to zero due to systematic risk

Specially, the return variance for a two-stock portfolio is $$Var(r_{p})=w_{1}^2SD(r_{1})^2+w_{2}^2SD(r_{2})^2+2\rho_{12}w_{1}w_{2}SD(r_{1})SD(r_{2})$$
## Stock Returns' Exposure to Systematic Risk
- Non-systematic risk can be [[Ust_Note/yr1_spring/FINA2303/Week11_Risk_and_Return/Risk and Return#High *Systematic* Risk $ iff$ High Return|diversified away]] by building a portfolio
- Therefore, stocks have higher returns is because they are more exposed to systematic risk

We measure systematic risk exposure as the correlation of one stock with a portfolio that only contains systematic risk, i.e., market portfolio.
## Market $\beta$
- $\beta$ is defined as the expected percentage change in the return of a stock for a 1% change in the market's return.
- It captures individual stocks' exposure to the market portfolio
- In practice, we estimate $\beta_{i}$ as the slope coefficient of a regression of stock $i$'s returns on the market portfolio return, i.e., $$r_{i,t}=\alpha_{i}+\beta_{i}r_{m,t}+\varepsilon_{i,t}$$

## The Capital Asset Pricing Model (CAPM)
### Intuition
The expected return on a stock should be the sum of
- Risk-free rate
- Risk premium to compensate for systematic risk
### The CAPM Formula
$$\mathbb{E}[r_{i}]=r_{f}+\beta_{i}(\mathbb{E}[r_{m}]-r_{f})$$
### Application
- We can use $\mathbb{E}[r_{i}]$, the expected return according to CAPM, as the discount rate in [[Ust_Note/yr1_spring/FINA2303/Week10_Stock/Stock Valuation Models/Dividend Discount Model]]. It estimates the cost of equity capital for individual firms.
- use it to detect stock mis-pricing with [[Ust_Note/yr1_spring/FINA2303/Week12_Systematic_Risk_and_Equity_Premium/Systematic Risk and Equity Premium#The Security Market Line (SML)|SML]].
## The Security Market Line (SML)
- The Security Market Line plots different stocks’ expected returns $\mathbb{E}[r_{i}]$ as functions of their expos!ure to systematic risk $\beta_{i}$.
- [[Ust_Note/Attachment/Pasted image 20250521144908.png|Sample SML]]
- Theoretically, every asset return should lie on the SML. If not, there is potential mis-pricing and therefore profitable.