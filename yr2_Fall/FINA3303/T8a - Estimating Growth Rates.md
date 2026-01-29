# Estimating Growth Rates
- Historical average growth rates
- Estimates of sell-side analysts
	- overly optimistic
- computed based on fundamental factors
	- internal growth comes from retaining some of profits for reinvestment, in turn resulting in the growth of future earnings

$$g=\text{retention rate}\times \text{return on new investment}$$
$$\text{dividend payoutr ratio}=\frac{\text{dividends}}{\text{earning}}=1-\text{retention rate}$$

## Growth in Earnings per Share
>In the Dividend Discount Model

$$EPS=\frac{\text{Net Income}-\text{Preferred Dividends}}{\text{Shares Outstanding}}$$

>[!Assumption]
>- the number of shares outstanding is constant
>
>$$\text{growth in EPS}=\text{growth in Net Income}$$
>
>- ROE (return on equity) are constant

the **growth rate of EPS** is given by


$$g_{t}=\text{retention ratio}\times \text{ROE}$$

>[!tip]- Proof
>$$g_{t}=\frac{NI_{t}-NI_{t-1}}{NI_{t-1}}$$
>
>The net income can be written as
>
>$$\begin{align}
NI_{t}&=\text{Equity}_{t-1}\times ROE_{t} \\
&=(\text{Equity}_{t-2}+\text{Retained earning}_{t-1})\times ROE_{t}
\end{align}
>$$
>$$NI_{t-1}=\text{Equity}_{t-2}\times ROE_{t-1}$$
>
>Thus,
>
>$$\begin{align}
g_{t}&=\frac{\text{Retained earning}_{t-1}}{NI_{t-1}}\times ROE \\
&=\text{retention ratio}\times ROE
\end{align}$$

- If $\text{retention rate}=0\%$, $g_{EPS}=0$
- If $\text{retention rate}=100\%$, $g_{EPS}=ROE$

### Payout or Reinvest
>[!tip] Short Answer
>- If $ROE>R_{E}$, cut dividends to reinvest to increase stock price
>- If $ROE<R_{E}$, cut retention to payout to increase stock price

>[!question] Intuition
>Return on equity is greater than cost of equity ($ROE>R_{E}$) implies that the new investment has a positive NPV. Thus, cutting dividends to increase its investment creates value for its shareholders

>[!Proof]
>Assume dividends grow at a constant rate
>
>$$b\equiv \text{retention rate}$$
>$$P_{0}=\frac{D_{1}}{R_{E}-g}=\frac{EPS_{1}\times b}{R_{E}-ROE\times b}$$
>$$\frac{dP}{db}=EPS \times \frac{(ROE-R_{E})}{(R_{E}-b\times ROE)^{2}}$$
>
>Thus, the stock price is strictly increasing in $b$ if $ROE>R_{E}$, and vice versa.

### Average and Marginal Returns
$$ROE=\frac{\text{Net income}}{\text{Book value of equity}}$$

- ROE measures the quality of both older projects that have been on the books for a substantial period and new projects from more recent periods.
- For large firms, the average returns may not shift substantially since older investments represent a significant portion of earnings

To measure the returns that reflects the best info about the potential growth, we introduce **marginal return on equity**

$$\text{Marginal ROE}=\frac{\Delta \text{ Net income}_{t}}{\Delta \text{ Book value of equity}_{t-1}}$$

### Changing ROE
We introduce the effect of changing ROE on existing investments over time.

$$\text{Efficiency generated growth}=\frac{ROE_{t}-ROE_{t-1}}{ROE_{t-1}}$$
$$\text{Expected growth rate in EPS}=ROE_{t}\times \text{retention rate}+\frac{ROE_{t}-ROE_{t-1}}{ROE_{t-1}}$$

The efficiency generated growth only affect the growth rate in the year in which ROE changes.

## Growth in Net Income
> In the Free Cash Flow to Equity Model

$$\text{Expected growth in net income}=\frac{\text{CapEx}-\text{Depre.}+\Delta \text{NWC}-\text{Net Debt}}{\text{Net income}}\times ROE$$

We no longer assume retained earnings is the only source of equity, i.e., a firm can grow net income by issuing new equity to fund new investment.

$$\text{growth in EPS}\ne\text{growth in Net Income}$$

First, we estimate how much equity the firm reinvests back into its business in the form of net capital expenditures and investments in working capital.

$$\text{Equity reinvested in business}=\text{CapEx}-\text{Depre.}+\Delta \text{NWC}-\text{Net Debt}$$
$$\text{Equity reinvestment rate}=\frac{\text{Equity reinvested}}{\text{Net income}}$$

>[!warning]
>Equity reinvestment rate can be more than 100% with the excess being funded with new equity

The expected growth in net income can be written as

$$\text{Expected growth in net income}=\text{Equity reinvestment rate}\times ROE$$

## Growth in EBIT
>In a Free Cash Flow to Firm Model (WACC method)

$$\text{Expected growth of EBIT}=\text{Reinvestment rate}\times \text{Return on capital}$$
$$\text{Reinvestment rate}=\frac{\text{CapEx}-\text{Depre.}+\Delta NWC}{EBIT(1-T_{C})}$$
$$\text{Return on capital}=\frac{EBIT(1-T_{C})}{\text{Equity}+\text{Debt}-\text{Cash}}$$

## Implications
- $g=b\cdot ROE<ROE$
	- The expected growth rate in earnings for a company cannot exceed its ROE in the long term
- $b=\frac{g}{ROE}$
	- The net capital expenditure needs for a firm (**retention/reinvestment rate**), for a given growth rate, should be inversely proportional to the quality of its investments (**ROE/ROC**).
- If $b=0$ (no reinvestment), $g=0$ (no growth of income)
	- No firm can expect its operating income to grow over time without reinvesting some of the operating income in net capital expenditures and/or working capital.

## Appendix
### Sales-to-Capital Ratio
$$\text{Sales-to-capital ratio}=\frac{\text{Sales}}{\text{capital reinvestment needs}}$$
