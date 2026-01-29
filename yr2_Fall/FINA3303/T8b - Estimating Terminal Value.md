# Estimating Terminal Value
$$\text{Value of a firm}=\sum_{t=1}^{t=n}\frac{\text{CF}_{t}}{(1+r)^t}+\frac{\text{Terminal Value}_{n}}{(1+r)^n}$$

- Multiple approach
	- apply a multiple (P/E, P/S, P/B, and EV/EBITDA) to estimate the value in the terminal year
- Stable Growth Model
	- assume the cash flows will grow at a constant rate forever
- Liquidation value
	- assume a liquidation of the firm's assets in the terminal year

## Stable Growth Model
$$\text{Terminal Value of Equity}_{t}=\frac{\text{Cash flow to equity}_{t+1}}{R_{e}-g}$$
$$\text{Terminal Value of Firm}_{t}=\frac{\text{FCFF}_{t+1}}{R_{wacc}-g}$$

>[!warning] Constraints on $g$
>- cannot be higher than the cost ($R_{e}$/$R_{wacc}$)
>- cannot be higher than the growth rate of the economy
>- vary depending on the inflation rate of the currency used
>- can be negative

### Characteristics of Stable Growth Firm
- Average risk
	- less exposure to market risk ($\beta \approx 1$)
- More debt
	- Greater debt capacity
		- stable cash flow
	- lower default risk
		- lower cost of debt
- lower (or no) excess returns ($ROE-\text{cost of equity}$)
- Reinvest less
	- due to lower return on investment

>[!note]
>>In dividend discount model
>>
>>$$\text{retention ratio}=\frac{\text{Expected growth rate of EPS}}{ROE}$$
>
>>In a free cash flow to equity model
>>
>>$$\text{Equity reinvestment rate}=\frac{\text{Expected growth rate of net income}}{ROE}$$
>
>>In a free cash flows to firm model
>>$$\text{Reinvestment rate}=\frac{\text{Expected EBIT growth rate}}{ROC}$$

### How Growth Rate Assumption affects Terminal Value
>[!tip] Short Answer
>- If $\text{Return}>\text{Cost}$, higher the assumed growth rate, higher the terminal value
>- If $\text{Return}<\text{Cost}$, higher the assumed growth rate, lower the terminal value

>[!question] Intuition
>Increase in growth rate sacrifices cash flow due to higher reinvestment rate. Return is greater than cost implies that the new investment has a positive NPV.

>[!Proof]
>$$b\equiv \text{reinvestment rate}$$
>$$b=\frac{g}{ROC}$$
>$$\text{Unlevered FCFF}=EBIT(1-T_{c})(1-\text{b})$$
>$$\text{Terminal value}_{n}=\frac{EBIT_{n-1}(1-T_{c})(1-b)}{R_{wacc}-g}=\frac{EBIT_{n-1}(1-T_{c})\left( 1-\frac{g}{ROC} \right)}{R_{wacc}-g}$$
>$$\frac{d\text{ Terminal Value}_{n}}{dg}=\frac{EBIT_{n-1}(1-T_c)\left(1 - \tfrac{R_{wacc}}{ROC}\right)}{(R_{wacc} - g)^2}$$
>
>Thus, the terminal value is strictly increasing in $b$ if $ROE>R_{E}$, and vice versa.

This result is essentially equivalent to the impact of [[T8a - Estimating Growth Rates#Payout or Reinvest|retention rate on stock price]].