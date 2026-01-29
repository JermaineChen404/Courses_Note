# Estimating WACC
## Market Weights
Use market weights to calculate WACC to reflect current importance of each source of financing to the firm.

>[!Example]
>Suppose Kenai Corp. has debt with a book (face) value of $10 million,  
trading at 95% of face value. It also has book equity of $10 million, and 1  
million shares of common stock trading at $30 per share.

- The market value of debt is the current price at which the debt is traded: $95\%\times \$10 m$
- The market value of equity is the $\text{stock price}\times \text{shares outstanding}=\$30\times 1m$

## Estimating Cost of Debt
### Publicly-Traded Bonds
For publicly-traded bonds, $R_{D}=ytm$ (yield to maturity)

$$\text{Bond Price}=\text{Coupon}\times \frac{\left( 1-\frac{1}{(1+R_{D}^n)} \right)}{R_{D}}+\frac{\text{Par}}{(1+R_{D}^n)}$$

>[!warning]
>$R_{D}$ is an effective annualized simple interest rate

For not publicly-traded bonds, we estimate $R_{D}$ using the YTM on a portfolio of bonds with similar credit ratings and maturity

### Debt with Default Risk
The cash flows used to determine YTM are the contractual or promised cash payments,  
which equal expected cash flow only for default‐free bonds.

For debt with default risk, the expected cash flows must reflect the probability of default $P_{b}$ and the recovery rate $R_{e}$.

$$\text{Bond Price}=\sum \frac{E[\text{Cash Flow}]_{n}}{(1+R_{D})^n}$$

For example, for one-year bonds,

$$\text{Bond Price}=\frac{(\text{Interest}+\text{Principal})\times(1-P_{b})+(\text{Interest}+\text{Principal})\times P_{b}\times R_{e}}{(1+R_{D})}$$

Alternatively, given the **average cumulative default rates**, we can treat the cost of debt as the weighted average of $ytm_{n}$ on the probability of default in that year $P_{n}$

$$R_{D}=\sum P_{n}\times E[ytm]_{n}$$

where $E[ytm]_{n}$ is the expected YTM if default occurs and 

$$P_{n}=P_{n}^{\text{cumulative}}-P_{n-1}^{\text{cumulative}}$$

![[Pasted image 20251017131958.png]]
