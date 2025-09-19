# Capital Structure Theory
- ROE: Return on Earning
- EPS: Earning per Share
- Cost of Capital $\iff$ Riskiness of the cash flow
## Effect of Leverage
- Leverage amplifies the variation in both ROE and EPS
- Capital structure affects the value of the firm through
  - Cost of Capital
  - Cash Flow
$$\sum \frac{FCF_{n}}{(1+R_{wacc})^n}$$
## Three Special Cases
- Case I
	- No corporate or personal taxes
	- No bankruptcy costs
- Case II
	- Corporate taxes, but no personal taxes
	- No bankruptcy costs
- Case III
	- Corporate taxes, but no personal taxes
	- Bankruptcy costs

## Case I
### Assumption
[[Ust_Note/yr2_Fall/FINA3303/Capital Structure#Perfect Capital Market|Perfect capital market]]
- No corporate or personal taxes
- No bankruptcy costs

### Proposition I - Firm Value
$$V_{L}=V_{U}=D+E$$
> How cash flow is divided  between bondholders and shareholders doesn't affect the value of the firm

### Proposition II - WACC
$$R_{U}=R_{wacc}=\frac{E}{D+E}\times R_{E}+\frac{D}{D+E}\times R_{D}$$
- Given a fixed FCFF, $R_{wacc}$ is a constant
	- $R_{wacc}$ can be interpreted as
		- cost of the firm's business risk
		- the risk of the firm's assets
	- $R_{E}=R_{U}+(R_{U}-R_{D})\frac{D}{E}$
		- ![[Ust_Note/yr2_Fall/FINA3303/attachments/Pasted image 20250912122854.png]]
		- More debt, more volatile, higher required return on levered equity
- When $\frac{D}{V}$ is high enough
	- $r_{D}$ is no longer constant and starts to increase

![[Ust_Note/yr2_Fall/FINA3303/attachments/Pasted image 20250912123127.png]]

## Case II
### Assumption
- Corporate taxes, but no personal taxes
- No bankruptcy costs

>Cash flow is divided among bondholders, shareholders, and government (tax)

### Proposition I - Firm Value
>$PV=DT_{C}$
- Present value of annual interest tax shield
	- interest tax shield = tax rate $\times$ interest payment
		- $its=T_{C}\times D\times R_{D}$
		- assume perpetual debt
			- $PV=\frac{its}{R_{D}}=DT_{C}$

>$V_{L}=V_{U}+DT_{C}$
- Value of a levered firm = value of an unlevered firm $+$ PV of interest tax shield

![[Ust_Note/yr2_Fall/FINA3303/attachments/Pasted image 20250912125435.png]]

### Proposition II - WACC
$$R_{wacc}=\frac{E}{D+E}\times R_{E}+\frac{D}{D+E}\times R_{D}(1-T_{C})$$
Rewrite the formula we have:
> $R_{wacc}=R_{U}-\frac{D}{D+E}\times R_{D}\times T_{C}$

![[Pasted image 20250918200250.png]]

## Case III
### Assumption
- Corporate taxes, but no personal taxes
- Bankruptcy costs

### Proposition I - Firm Value
![[Pasted image 20250918200753.png]]

### Proposition II - WACC
![[Pasted image 20250918201420.png]]

### Implication
- bankruptcy costs offset additional value of interest tax shield at some point
- $\text{marginal gain on tax shield}=\text{marginal loss from expected bankruptcy costs}\to$ max value/lowest $WACC$ $\to$ optimal capital structure

### The Tradeoff Theory
Determinant of Financial Distress Costs
- debt ratio
- volatility of cash flows and asset values
- utility companies vs. semiconductor firms

![[Pasted image 20250918202810.png]]

## Leverage Effects on Beta of Equity
Given that
$$D+E=V_{u}+PVits$$
>Beta of a portfolio is the weight average of the betas of the individual assets in the portfolio

$$\frac{D}{D+E}\times B_{D}+\frac{E}{D+E}\times B_{E}=\frac{V_{u}}{V_{u}+PVits}\times B_{u}+\frac{PVits}{V_{u}+PVits}\times B_{its}$$

### Assumption I
>$B_{its}=B_{u}$

$$B_{U}=\frac{E}{D+E}\times B_{E}+\frac{D}{D+E}\times B_{D}$$
#### Implication
- assume tax shield are as risky as the operation
- require firm to rebalance it debt to maintain a ==constant debt-to-value ratio==
### Assumption II
>- $B_{its}=B_{u}$
>- $B_{D}=0$

$$B_{U}=\frac{E}{D+E}\times B_{E}$$

#### Implication
- same framework as assumption I
- further assume $B_{D}$ to be zero for simplicity

### Assumption III
>$B_{its}=B_{D}=0$

We have the ==Hamada's equation==
$$B_{U}=\left[\frac{1}{1+(1-T_{c})\frac{D}{E}}\right]\times B_{E}$$
$$\iff B_{E}=\left[1+(1-T_{c})\frac{D}{E}\right]B_{U}$$

#### Implication
- The risk of the interest tax shield is equal to the risk of the debt that creates it
- treat tax shield as a fixed, promised cash flow whose risk is tied directly to that of where it derive from, the debt
- opposite to Assumption I
- does not require a constant debt-to-value ratio

==Not applicable in Exam except explicitly mentioned!!!==


# Appendix
## Perfect Capital Market
- Securities are fairly prices (no bid-ask spread)
- No tax, no transaction costs
- Investment cash flows are independent of financing choices
## Homemade Leverage
Investors can create homemade leverages for their portfolio regardless of how a specific firm leverages to achieve their desired debt/equity ratio.
- Assumptions: Same interest rate for investors and firms (valid in perfect market assumption)
- To leverage $\to$ borrow money to buy stocks
- To deleverage $\to$ sell stocks to buy bonds (lend money)
- Goal: Maintain the desired debt/equity ratio


## Tax cut
- Lower tax shield $\to$ less debt
- Stronger ability to repay debt $\to$ more debt

## Assumption
- $B_{its}=B_{U}$
	- when D/V is constant
	- $its=r_{d}\times D_{t}\times T_{c}=r_{d} \times \frac{D}{V}\times V\times T_{c}$
- 
- 
- 
- 
- In exam, formula I and II if not specified
- Positive NPV Projects $\to$ stock price rise