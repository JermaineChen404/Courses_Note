## Comparison with [[Ust_Note/yr1_spring/FINA2303/Week10_Stock/Stock Valuation Models/Dividend Discount Model|DDM]]
$$\text{Asset}-\text{Liability}=\text{Stockholders' Equity}$$
- Dividend discount model directly estimate the value of equity (focuses right-hand side)
- DCF model estimates the value of firm assets, then subtracts debt to obtain equity value
## Idea
Estimate the value of the firm independent on how it is  
financed
- [[Ust_Note/yr1_spring/FINA2303/Week7_Capital_Budgeting/Capital Budgeting|Estimate free cash flows FCF]] available to all investors (both debt and  equity holders)
- Compute present value of FCF—this is the value of the firm’s assets
-   Subtract debt value to obtain equity value
## Discount Rate
Instead of using $r_{E}$ as in the [[Ust_Note/yr1_spring/FINA2303/Week10_Stock/Stock Valuation Models/Dividend Discount Model]], we use an adjusted (or weighted) discounted rate since we are discounting Free Cash Flows that belong to both debt holders and equity holders, and their costs of capital are different. This discount rate is called [[Weighted Average Cost of Capital]], denoted by $r_{wacc}$
## Discount FCF
Suppose our estimation of FCF is only valid/relevant from $t=1$ to $t=N$, and that FCF will grow at rate $g_{FCF}$ from day $N+1$ onward.
Using $r_{wacc}$ as discounted rate, $$V_{0}=\frac{FCF_{1}}{1+r_{wacc}}+\frac{FCF_{2}}{(1+r_{wacc})^2}+\dots+\frac{FCF_{N}}{(1+r_{wacc})^N}+\frac{V_{N}}{(1+r_{wacc})^N}$$
where the terminal value $V_{N}$ is given by  $$V_{N}=\frac{FCF_{N+1}}{r_{wacc}-g_{FCF}}$$
Since it is difficult to forecast FCF that are far distant in the future, we assume a constant growth rate for period-N cash flows for simplicity. How we choose $N$ and $g_{FCF}$ determines the quality of our DCF model.
## Stock Price
The value of the firm's per-share equity value, i.e., the stock price is given by
$$P_{0}=\frac{V_{0}-Debt+Cash}{\text{Number of Shares Outstanding}}$$
