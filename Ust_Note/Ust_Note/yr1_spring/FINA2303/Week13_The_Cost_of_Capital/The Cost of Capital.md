## Recap
The fundamental PV formula:$$PV=\sum_{t=0}^\infty \frac{C_{t}}{(1+r)^t}$$
- For debt, $r$ is the [[Ust_Note/yr1_spring/FINA2303/Week8_Bond/Bonds#Yield to Maturity ($ytm$)|yield to maturity]]
- For equity, $r$ is estimated by [[Ust_Note/yr1_spring/FINA2303/Week12_Systematic_Risk_and_Equity_Premium/Systematic Risk and Equity Premium#The Capital Asset Pricing Model (CAPM)|CAPM]]
## Weighted Average Cost of Capital (WACC)
If a project is financed by both debt and equity, its cost of capital is a  
combination of cost of debt and cost of equity.
### WACC (No Taxes)
Without taxes, $r_{WACC}$ is a weighted average of the firm's cost of debt and cost of equity: $$r_{WACC}=w_{B}r_{B}+w_{E}r_{E}$$ where the weights are the fraction of the total assets that are financed by debt and equity: $$w_{B}=\frac{\text{Debt}}{\text{Total Assets}}$$ $$w_{E}=\frac{\text{Equity}}{\text{Total Assets}}$$
Additionally, $$r_{B}<r_{WACC}<r_{E}$$
### WACC (With Tax) and Tax Shields
- Interest expense is tax-deductible
	- More levered $\to$ More debt (the proportion of debt in total assets) $\to$ Lower taxes $\to$ Lower $r_{WACC}$
- Incorporating the tax advantage in $r_{WACC}$ gives: $$r_{WACC}=w_{B}r_{B}(1-\tau)+w_{E}r_{E}$$ where $\tau$ is the corporate tax rate.
### WACC and Preferred Equity

[[Ust_Note/yr1_spring/FINA2303/Week10_Stock/Stocks#Preferred Stock|Preferred equity]] is cheaper than common equity. If a firm is partially financed with preferred equity, $r_{WACC}$ becomes $$r_{WACC}=w_{B}r_{B}(1-\tau)+w_{E}r_{E}+w_{P}r_{P}$$
## Key Assumption and Limitation
- Average risk
	- New projects have the same risk as the average project of the firm
	- Otherwise, use project-specific discount rate
- Constant debt-equity ratio
	- Firms adjust their capital structure to maintain a constant leverage ratio during the lifetime of the project
	- Otherwise, $r_{WACC}$ is not constant
- Ignore the higher bankruptcy risk due to higher leverage (debt)