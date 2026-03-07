---
title: "L2 - Mean-Variance Portfolio Analysis"
course: FINA3103
type: Lecture
tags: [fina3103, portfolio analysis, mean-variance, sharpe ratio, efficient frontier, optimal allocation]
---
ZZZZ
# Utility
## Risk-Return Tradeoff
Investors are risk averse (ask for risk premium).

---

To quantify investors' attitudes over risk and return, **mean-variance utility** is introduced,
$$U=E[r]-\frac{1}{2}A\sigma^2=CE$$
where $A$ measures investor risk aversion
- $A>0$ : risk averse
- $A=0$ : risk neutral
- $A<0$ : risk loving

Optimal investment $\to$ highest possible Utility $U$

different investor $\to$ different $A$ $\to$ different $U$ for the same investment

## Deriving Risk Aversion Level
Utility scores are also called **certainty equivalent**, we can derive $A$ using survey:

Given a risky investment with known expected return $E[r]$ and risk $\sigma$, what risk-free return $E[r_{f}]$ the investor sees as equivalent.
$$A=\frac{2(E[r]-E[r_{f}])}{\sigma^2}$$

## Utility Indifference Curve
![[Pasted image 20251010163543.png]]

Investors with risk aversion of $A$ are indifferent among every investment on the curve, 

![[Pasted image 20251010163909.png]]

For every investment sits outside the curve, investors always can find an investment with higher utility thanks to higher return or lower risk

# Portfolio Variance
## Variance-Covariance Matrix
![[Pasted image 20251010222145.png]]
### Correlation Matrix
A normalized measure of covariance

![[Pasted image 20251010222213.png]]
![[Pasted image 20251010222234.png]]

## Bordered Covariance Matrix Method
For any portfolio of two assets,
$$\sigma_{p}^2=w_{1}^2\sigma_{1}^2+w_{2}^2\sigma_{2}^2+2w_{1}w_{2}\sigma_{12}$$
For portfolios of more than two assets, we use bordered covariance matrix to calculate portfolio variance.

Assume there are three assets with $n$ data point each

|$A_{1}$|$B_{1}$|$C_{1}$|
|---|---|---|
|...|...|...|
|$A_{n}$|$B_{n}$|$C_{n}$|
The variance-covariance matrix is
$$\Sigma= \begin{bmatrix}
\sigma_1^2 & \sigma_{12} & \sigma_{13} \\
\sigma_{21} & \sigma_2^2 & \sigma_{23} \\
\sigma_{31} & \sigma_{32} & \sigma_3^2
\end{bmatrix}$$
In *Excel*, $$\sigma_{12}=COVAR(A_{1}:A_{n},B_{1}:B_{n})$$
Given weights of three assets $w_{1},w_{2},w_{3}$, the bordered covariance matrix is
$$B=\begin{bmatrix}
w_1^2\sigma_{11} & w_1w_2\sigma_{12} & w_1w_3\sigma_{13} \\
w_2w_1\sigma_{21} & w_2^2\sigma_{22} & w_2w_3\sigma_{23} \\
w_3w_1\sigma_{31} & w_3w_2\sigma_{32} & w_3^2\sigma_{33}
\end{bmatrix}$$
In general, each entry $i,j$ in the matrix is given by $w_{i}w_{j}\sigma_{ij}$.

**Portfolio Variance** is given by the sum over all entries in the bordered covariance matrix.
$$\sigma_{P}^2=\sum_{i=1,j=1}^{n} w_{i}w_{j}\sigma _{ij}$$
Alternatively, the Portfolio variance can be given by *Excel* function $$=\text{MMULT}(\text{TRANSPOSE}(w_{1}:w_{n}),MMULT(B,w_{1}:w_{n}))$$

# The Capital Allocation Line (CAL)
Consider only two investments, one risky and the other risk-free, 
## Portfolio Return with 2 Assets
Given
$$E(r_{p})=w_{1}E(r_{1})+w_{2}E(r_{2})$$
we have
$$
\begin{align}
E(r_{c})&=yE(r_{p})+(1-y)r_{f} \\
&=r_{f}+y(E(r_{p})-r_{f})
\end{align}
$$
where $y$ is the risk weight and $E(r_{p})-r_{f}$ is the risk premium.

## Portfolio Variance with 2 Assets
Given
$$\sigma_{p}^2=w_{1}^2\sigma_{1}^2+w_{2}^2\sigma_{2}^2+2w_{1}w_{2}\sigma_{12}$$
we have
$$\sigma_{c}^2=y^2\sigma_{p}^2+(1-y)^2\sigma_{f}^2+2y(1-y)\sigma_{pf}$$
Since $\sigma_{pf}=\sigma_{f}^2=0$ (risk-free),
$$\sigma_{c}=y \sigma_{p}$$

## Possible Allocations
Combining the portfolio return and variance, we can express the portfolio return $E(r_{c})$ in term of portfolio risk $r_{c}$
$$E(r_{c})=r_{f}+\frac{E(r_{p})-r_{f}}{\sigma_{p}} \cdot \sigma_{c}$$
where the slope $\frac{E(r_{p})-r_{f}}{\sigma_{p}}$ is the **Sharpe ratio** that measures the reward to variability we take from the risky investment.

![[Pasted image 20251012142845.png]]

In reality, the rate at which we can borrow money is higher than the rate we get if we deposit, i.e., $r_{b}>r_{f}$

![[Pasted image 20251012142957.png]]

Given a fixed risky investment with known Sharpe ratio, the **CAL** gives all **possible allocation** between the risky investment and a risk-free one.

## Optimal Allocation
For different investors with different risk aversion $A$, they can find their optimal portfolio by obtaining the highest reachable [[L2 - Mean-Variance Portfolio Analysis#Utility Indifference Curve|U-curve]], i.e., where the **U-curve** is tangent to the **CAL**

![[Pasted image 20251012143859.png]]

Alternatively, we can express the utility $U$ in term of the risk weight $y$
$$\begin{align}
U_{c}&=E[r_{c}]-\frac{1}{2}A\sigma_{c}^2 \\
&=-\frac{1}{2}A\sigma_{p}^2\,y^2+(E[r_{p}]-r_{f})\,y+r_{f}
\end{align}$$
we obtain the maximum utility $U$ if and only if $$y=\frac{E(r_{p})-r_{f}}{A\sigma_{p}^2}$$
i.e., the **optimal asset allocation** is $$y^*=\frac{E(r_{p})-r_{f}}{A\sigma_{p}^2}$$
![[Pasted image 20251012145018.png]]

# Minimum-Variance Frontier

## Portfolio Diversification
The diversification benefits depends on the average correlation across all assets.

![[Pasted image 20251012145306.png]]

![[Pasted image 20251012145335.png]]

## Graph
For a given $\rho$, we vary $w$ to plot the lowest $\sigma_{p}$ for given $E(r_{p})$

![[Pasted image 20251012151147.png]]
## 2 Assets Scenario


$$
\begin{align} 
\sigma_{c}^2&=w^2\sigma_{1}^2+(1-w)^2\sigma_{2}^2+2w(1-w)\sigma_{12}\\ \\
&=(\sigma_{1}^2+\sigma_{2}^2-2\sigma_{12})w^2+(2\sigma_{12}-2\sigma_{2}^2)w+\sigma_{2}^2
\end{align}
$$
Therefore, we obtain the minimum variance portfolio when the weight is
$$w_{1}^{MV}=\frac{\sigma_{2}^2-\sigma_{12}}{\sigma_{1}^2+\sigma_{2}^2-2\sigma_{12}}$$

## Optimal Risky Portfolio
![[Pasted image 20251012151937.png]]

$$\text{Minimum Variance}\nRightarrow\text{Optimal}$$
$$\text{Maximum Sharpe Ratio}\Rightarrow \text{Optimal}$$
$P^*$ is a universal optimal risky portfolio for all investors regardless of their risk aversion, since it ensure highest Sharpe Ratio lying on the minimum variance frontier.

![[Pasted image 20251012153452.png]]

The CAL gives all possible allocations between $P^*$ and risk-free assets, with U-curve tailoring the exact weight to maximize utility for different investors.

### 2 Assets Scenario
Let $R_{1}=E(r_{1})-r_{f}$ and $R_{2}=E(r_{2})-r_{f}$
$$w_{1}^*=\frac{R_{1}\sigma_{2}^2-R_{2}\sigma_{12}}{R_{1}\sigma_{2}^2+R_{2}\sigma_{1}^2-(R_{1}+R_{2})\sigma_{12}}$$

## Restricted Minimum Variance Frontier
![[Pasted image 20251012154840.png]]

## Allocation with No Risk-free Asset
![[Pasted image 20251012154930.png]]

## General Procedure
1. Input (security analysis)
	- expected return
	- [[L2 - Mean-Variance Portfolio Analysis#Variance-Covariance Matrix|variance-covariance matrix]]
2. Construct the [[L2 - Mean-Variance Portfolio Analysis#Minimum-Variance Frontier|efficient frontier]] of risky assets
	- find the minimum-variance portfolio for any target expected return
3. Draw the [[L2 - Mean-Variance Portfolio Analysis#The Capital Allocation Line (CAL)|CAL]] to find the optimal portfolio $P^*$
4. Find the appropriate weight between $P^*$ and the risk-free asset by [[L2 - Mean-Variance Portfolio Analysis#Optimal Allocation|U-curve]] according to individual risk aversion

# Mutual Fund Theorems
Optimal risky portfolio $P^*$ is unique and all investors should hold only the safe asset and $P^*$ (only two "mutual funds" are needed)

## Assumption
- All returns are normally distributed (described by only two parameter $E(r)$ and $\sigma$)
- All assets are tradable
- No transaction costs


