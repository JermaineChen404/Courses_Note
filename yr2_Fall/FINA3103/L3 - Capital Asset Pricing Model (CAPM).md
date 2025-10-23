Motivation: to find the expected return of individual stock and profit from the mispricing

# Assumption
- All investors are the same in term of the [[L2 - Mean-Variance Portfolio Analysis#General Procedure|Markowitz procedure]]
- only different in wealth and [[L2 - Mean-Variance Portfolio Analysis#Deriving Risk Aversion Level|risk aversion]]

# $P^*=M$
Market portfolio is mean-variance efficient/optimal, i.e., $P^*$

![[Pasted image 20251012175256.png]]

Despite different risk weights, since borrowing and lending cancel out, the aggregate market demand for risky portfolio $P^*$ must equal to the market supply portfolio $M$ (e.g., $\approx \text{SPY}$)
$$P^*=M\iff y_{agg}^*=1$$

## 2 Investors Scenario
Consider only two investors in the economy with wealth $W_{1},W_{2}$ and risk aversion $A_{1},A_{2}$ respectively.

Given the [[L2 - Mean-Variance Portfolio Analysis#Optimal Allocation|optimal assets allocation]]
$$y_{1}^*=\frac{E(r_{m})-r_{f}}{\sigma_{m}^{2}}\cdot\left( \frac{1}{A_{1}} \right)$$
$$y_{2}^*=\frac{E(r_{m})-r_{f}}{\sigma_{m}^{2}}\cdot\left( \frac{1}{A_{2}} \right)$$
By definition,
$$
\begin{align}
y_{agg}^*&=\frac{\text{Total Investment in M}}{\text{Total Wealth of Economy}} \\
&=\frac{W_{1}y_{1}^*+W_{2}y_{2}^*}{W_{1}+W_{2}} \\
&=\frac{E(r_{m})-r_{f}}{\sigma_{m}^{2}}\cdot \frac{\left( \frac{W_{1}}{A_{1}}+\frac{W_{2}}{A_{2}} \right)}{W_{1}+W_{2}} \\
&=\frac{E(r_{m})-r_{f}}{\sigma_{m}^{2}}\cdot\left( \frac{1}{\bar{A}} \right) \\
&=1
\end{align}
$$
i.e., $$E(r_{M})-r_{f}=\bar{A}\sigma_{m}^2$$
where
$$\bar{A}=\frac{W_{1}+W_{2}}{\frac{W_{1}}{A_{1}}+\frac{W_{2}}{A_{2}}}$$
i.e., the weighted harmonic average of $A_{1}$ and $A_{2}$

# Risk & Return for the Market
For more than two investors, the conclusion still holds:
$$E(r_{m})-r_{f}=\bar{A}\sigma_{m}^2$$
where $\bar{A}$ is the weighted harmonic average of all investors' risk aversion.

## Market & Security Risk Premium
$$
\begin{align}
E(r_{m})-r_{f}&=E(\Sigma _{i=1}^nw_{i}r_{i})-r_{f} \\
&=\Sigma_{i=1}^nw_{i}E(r_{i})-r_{f} \\
&=\Sigma_{i=1}^nw_{i}(E(r_{i})-r_{f})
\end{align}
$$
Thus, stock $x$'s contribution to market risk premium is
$$w_{x}(E(r_{x})-r_{f})$$

## Market & Security Risk
### 2 Assets Scenario
$$\sigma_{m}^2=w_{1}^2\sigma_{1}^2+w_{2}^2\sigma_{2}^2+2w_{1}w_{2}\sigma_{12}$$
We can split it into two part.

1's contribution to $\sigma_{m}^2$ is 
$$w_{1}^2\sigma_{1}^2+w_{1}w_{2}\sigma_{12}=w_{1}(w_{1}\sigma_{1}^2+w_{2}\sigma_{12})$$
2's contribution to $\sigma_{m}^2$ is 
$$w_{2}^2\sigma_{2}^2+w_{1}w_{2}\sigma_{12}=w_{1}(w_{2}\sigma_{1}^2+w_{1}\sigma_{12})$$
Now consider $\sigma_{1m}$

Given
$$Cor(x,ay+bz)=a\sigma_{xy}+b\sigma_{xz}$$
We have
$$
\begin{align}
\sigma_{1m}&=Cor(r_{1},r_{m}) \\
&=Cor(r_{1},w_{1}r_{1}+w_{2}r_{2}) \\
&=w_{1}\sigma_{1}^2+w_{2}\sigma_{12}
\end{align}
$$
1's contribution can be written as
$$w_{1}(w_{1}\sigma_{1}^2+w_{2}\sigma_{12})=w_{1}\sigma_{1m}$$
For market with more than two assets, it still holds.

Thus, stock $x$'s contribution to market risk is
$$w_{x}\sigma_{xm}$$

### General Proof
Security $x$'s contribution to market risk is
$$\sigma_{m}^2(x)=\Sigma_{i=1}^nw_{i}w_{x}Cov(x,i)$$
Consider
$$
\begin{align}
\sigma_{xm}&=Cov(r_{x},r_{m}) \\
&=Cov(r_{x},\Sigma w_{i}r_{i}) \\
&=\Sigma w_{i}Cov(r_{i},r_{x}) \\
\end{align}
$$
Substituting back,
$$\sigma_{m}^2(x)=w_{x}\Sigma w_{i}Cov(r_{i},r_{x})=w_{x}\sigma_{xm}$$

## Market & Security Reward to Risk
Similar to [[Sharpe Ratio]], the security reward to risk is
$$\frac{\text{x's contribution to market risk premium}}{\text{x's contribution to market risk}}=\frac{w_{x}(E(r_{x})-r_{f})}{w_{x}\sigma_{xm}}=\frac{(E(r_{x})-r_{f})}{\sigma_{xm}}$$
For the market portfolio,
$$\frac{\text{market risk premium}}{\text{market risk}}=\frac{E(r_{m})-r_{f}}{\sigma_{m}^2}$$

## Equilibrium Reward to Risk
According to no arbitrage rule, security prices will adjust until they offer the same reward to risk as market portfolio, thus
$$\frac{(E(r_{x})-r_{f})}{\sigma_{xm}}=\frac{E(r_{m})-r_{f}}{\sigma_{m}^2}$$
This gives CAPM:
$$E(r_{x})=r_{f}+\frac{\sigma_{xm}}{\sigma_{m}^2}(E(r_{m}-r_{f}))$$
or equivalently,
$$E(r_{x})=r_{f}+\beta_{x}(E(r_{m}-r_{f}))$$
where $\beta_{x}=\frac{\sigma_{xm}}{\sigma_{m}^2}$ is the beta of security $x$

# Security Picking: Seeking Alpha

## Security Market Line (SML)

## Estimating $\beta$ by Regression
The observed CAPM is 
$$r_{it}-r_{ft}=\beta_{i}(r_{mt}-r_{ft})+e_{it}$$
Objective: find a $\beta$ that best fit the observed data

Method: Least Squares Method (最小二乘法)
$$Min\sum e_{it}^2$$

Best estimate of CAPM $\beta$:
$$\frac{Cov(x,y)}{\sigma_{x}^2}$$


## Seeking Alpha by Regression
Introducing $\alpha_{i}$ gives
$$r_{it}-r_{ft}=\alpha_{i}+\beta_{i}(r_{mt}-r_{ft})+e_{it}$$

![[Pasted image 20251015140132.png]]

$$\text{t-statistic}=\frac{\text{coefficient}}{\text{std}}$$