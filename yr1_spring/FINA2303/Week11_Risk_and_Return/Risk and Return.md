## Intuition
Higher risk, higher return.
## Multi-Period Stock Return
In general, given a historical series of prices and dividends, $$r_{t+N}=\frac{P_{t+N}+\sum_{n=t+1}^{t+N}D_{n}(1+r_{n-N})}{P_{t}}-1$$
where $r_{n-N}$ stands for the return from $t=n$ to $t=N$. We assume that dividends paid between $t$ to $t+N$ are re-invested in the stock, earning a return.  

The return can be obtained by either
- Compounding product of (1+sub-period returns) $$1+r_{ann}=\prod_{i=1}^{250}(1+r_{di})$$
- Computing the return over the entire period from $t$ to  $t+1$ $$1+r_{t+N}=\frac{P_{t+N}+\sum_{n=t+1}^{t+N}D_{n}(1+r_{n-N})}{P_{t}}$$
## Average Stock Returns
- The arithmetic average annual return
	- $\bar{r}$ is given by $$\bar{r}=\frac{1}{T}\sum_{n=1}^Tr_{n}$$
	- Independent of individual investors' investment horizons
	- We use it when comparing risk and return
- The geometric average annual return
	- $\hat{r}$ is given by $$\hat{r}=\left( \prod_{t=1}^T(1+r_{t}) \right)^\frac{1}{T}-1$$
	- Depends on how long we invest for
	- We use it when analyzing the **cumulative** performance of a stock
## Risk Measurement
Stock return standard deviation (volatility) is $$SD(r)=\sqrt{ Var(r) }=\sqrt{ \frac{1}{T-1}\sum_{t=1}^T(r_{t}-\bar{r})^2 }$$
Note that $\frac{1}{T-1}$ since it is a sample SD.
### Why variance as measurement
Most finance models assume that the returns we observe in the real world are random variables coming from a normal distribution that are fully characterized by their mean and variance.
### High Returns $\centernot\iff$ High Standard Deviation
- The positive relationship between risk and return is valid only for stock portfolios.
- No clear pattern for individual stocks
- Why? Diversification!
## Diversification
Stock prices fluctuate due to two types of risk
- Non-systematic (diversifiable) risk
	- Firm-specific risk
	- Industry-specific risk
- Systematic (non-diversifiable) risk
	- e.g. Country-wide or global recession
## High *Systematic* Risk $\iff$ High Return
- Invertors can fully diversify non-systematic risk by holding a large enough portfolios.
- Therefore, **only systematic risk should be compensated** with higher returns.