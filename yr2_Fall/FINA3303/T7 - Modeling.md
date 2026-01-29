# Modeling
## Understand the business
- Annual report
- Financial ratio
	-  Profitability:  (gross/operating/net) Profit Margin
	- Efficiency: Inventory/Receivable Turnover
	- Return: Rate of return ($\text{ROE}=\frac{\text{net income}}{\text{Equity}}$)
		- ROE decomposition: Profitability + Efficiency + Leverage level
		$$\text{ROE}=\frac{\text{net income}}{\text{sales}}\times \frac{\text{sales}}{\text{total asset}}\times \frac{\text{total asset}}{\text{equity}}$$
	-  Liquidity: $\frac{\text{EBIT}}{\text{interest expanse}}$, Debt ratio (for long term)

## Building Excel
Convert financial statements into common size:

- income statements: divide everything by **Sales**
- balance sheet: divide everything by **Total assets**

Different colors to distinguish data types

- historic facts: green
- assumptions: red
	- changeable
	- need to be explained by business stories or historic performances
		- e.g., cash is percentage of sales since if business grows, cash needed to support the business also grows
- formula: black

Balancing term.

- e.g., Liability (long- or short-term), dividends
- not driven by business/operating
- If long-term debt becomes negative
	- reduce short-term debt by changing assumptions
	- increase dividends paid

Tax is different in income statement and FCFF calculation since the FCFF calculation excludes the interest effect

- hide it

Justify terminal growth rate

Circular referencing

Defense of using one WACC to discount the whole timeline when the debt ratio is changing during the first 5 year

- We assume the firm will reach a stable state after year 2029
- the debt to equity ratio used to compute WACC is the target ratio
- in the first 5 year, the firm is moving towards the target ratio
- the investors also have this info, requiring the rate of return to reflect this

## Simulation
- normal distribution
- triangular distribution
- uniform distribution

do 10000 simulation

## Determining Growth Rate
Growth rate $g$

$$g=\text{retention rate}\times \text{return on new investment}$$
### Dividends-Reinvestment Tradeoff

### Incorporate the Tradeoff into Growth Rate Assumption
#### Marginal Returns
The average ROE measures the quality of both older and new projects, and is thus a backward-looking estimate.

To build a forward-looking estimate, we use marginal ROE that measures the quality of new projects

$$\text{Marginal ROE}=\frac{\Delta \text{Net income}_{t}}{\Delta \text{Book value of equity}_{t-1}}$$

Efficiency generated growth

- one-time impact

#### Growth in Earning per Share

#### Growth in Net Income
$$\text{Equity reinvested in business}=\text{CapEx}-\text{Dep.}+\Delta\text{Working Cap}-\text{Net Debt
}$$

#### Growth in EBIT
most relevant due to WACC method

ROIC

$$\text{Terminal Value}_{n}=\frac{\text{EBIT}_{n+1}(1-t)(1-\text{Reinvestment rate})}{(1-\text{Reinvestment rate})\times\text{ROC}+(\text{WACC}-\text{ROC})}=$$











