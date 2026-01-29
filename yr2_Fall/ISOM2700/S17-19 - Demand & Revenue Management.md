# Demand & Revenue Management
## Demand Management
Goal: Matching supply with demand

- Passive Approaches
	- Forecast Customer Demand
		- Demand forecasting method
- Active Approaches
	- Prioritize Customer Demand
		- Capacity-based revenue management
	- Influence Customer Demand
		- Price-based revenue management

### Demand Forecasting Methods
>[!Principle]
>Tradeoff between **forecasting accuracy** and **interpretability**

#### Simple Moving Average
Forecast future demand using the simple average of past $n$ data

$$F_{t}=\frac{1}{n}\sum_{k=1}^n A_{t-k}$$

where $n$ is the **forecast window**

![[Pasted image 20251121171324.png]]

#### Weighted Moving Average
Forecast future demand using the weighted average of past $n$ data.

Weights are chosen to reflect past patterns appropriately

- often give more significance to more recent data

$$F_{t}=\sum_{k=1}^n w_{t-k}A_{t-k}$$

where $\sum_{k=1}^n w_{t-k}=1$

#### Exponential Smoothing
$$\begin{align}
F_{t}&=F_{t-1}+\alpha (A_{t-1}-F_{t-1}) \\
&=\alpha A_{t-1}+(1-\alpha)\times F_{t-1}
\end{align}
$$

$\alpha$ is a smoothing constant chosen

- $0<\alpha<1$
- larger $\alpha$ gives more weight on recent data
	- react quickly to sudden changes
- smaller $\alpha$ gives more weight on old data
	- smoother and more stable


|$\alpha$     |  $w_{t-1}$   | $w_{t-2}$ | $w_{t-3}$|
| --- | --- |---|---|
| 0.1    | 0.1 |0.09   |0.081|
|0.5|0.5|0.25|0.125|
|0.9|0.9|0.09|0.009|

![[Pasted image 20251121174438.png]]

#### Simple Linear Regression Model
For $n$ data points $\{(x_{i},y_{i}):i=1,\dots,n\}$, the forecast value is

$$Y_{i}=a+bx_{i}$$

while $y_{i}$ is the actual value.

The least squares method minimize $\sum_{i=1}^{n}(y_{i}-Y_{i})^2$ to obtain the optimal coefficients $a^*$ and $b^*$

$$b^*=\frac{\sum_{i=1}^{n}x_{i}y_{i}-n\bar{x}\bar{y}}{\sum_{i=1}^{n}x_{i}^{2}-nx^{2}}$$

$$a^*=\bar{y}-b^*\bar{x}$$

#### Measuring Forecast Accuracy
Forecast Error: 

$$\text{Error}_{i}=\text{Actual}_{i}-\text{Forecast}_{i}$$

Mean Absolute Deviation (MAD):

$$MAD=\frac{1}{n}\sum_{i=1}^{n}|\text{Actual}_{i}-\text{Forecast}_{i}|$$

Tracking Signal: ratio of cumulative error and MAD

$$TS=\frac{\sum_{i=1}^{n}(\text{Actual}_{i}-\text{Forecast}_{i})}{MAD}$$

>[!Tip] Intuition
>- The **numerator (CFE)** tells you whether errors are piling up in one direction (positive = under-forecasting, negative = over-forecasting).
>- The **denominator (MAD)** scales this bias relative to the typical error size, so you don’t overreact to small fluctuations.    
>- The tracking signal is essentially a **bias-to-variability ratio**.

>[!Interpretation]
>- **TS near 0** → Forecast errors are balanced; no systematic bias.
>- **TS > +4** → Forecasts are consistently too low (under-forecasting).
>- **TS < -4** → Forecasts are consistently too high (over-forecasting).

## Revenue Management
Goal: Maximizing revenue by optimizing

- Product availability: **capacity-control**
- Price: **price-control**

### Capacity-based Revenue Management
How to allocate limited **capacity** to different customer segments (demand) **at given prices**

- Protection level and booking limits
- overbooking to deal with no-show customers

#### Two-Class Allocation Problem

|     | Price | Selling Horizon | Demand |
| --- | --- |---| ---|
|Business | Full price $f_{1}$|Last minutes | Uncertain $D_{B}\sim N(\mu,\sigma^2)$ |
|Leisure | Discount price $f_{2}$| In advance | Ample |

- Protection level $Q$: **Decision variable**
	- seats reserved for business travelers
- Booking limit: $\text{Capacity}-Q$
	- maximum seats sold at the discount price

![[Pasted image 20251121183648.png]]

Similar to [[S14-16 - Inventory Management#Newsvendor Model|Newsvendor Model]], we use marginal analysis.

$$\begin{align}
\text{Profit}(Q\to Q+1)&=C_{u}\times P(D_{B}>Q)-C_{o}\times P(D_{B}\leq Q) \\
&=C_{u}-(C_{u}+C_{o})\times P(D_{B}\leq Q)
\end{align}
$$

where $C_{u}=f_{1}-f_{2}$ and $C_{o}=f_{2}$

The optimal protection level $Q^*$ is given by

$$P(D_{B}\leq Q^*)=\frac{C_{u}}{C_{u}+C_{o}}$$

Since $D_{B}\sim N(\mu,\sigma^2)$, we have

$$Q^{*}=\mu+\sigma z^{*}$$

where

$$z^{*}=\text{Normsinv}\left( \frac{C_{u}}{C_{u}+C_{o}} \right)$$

![[Pasted image 20251121185322.png]]

### Price-based Revenue Management
How to determine the **prices** of goods or services based on market conditions and customer behavior **at given capacity**

- e.g., dynamic pricing in e-commerce

#### Price Optimization: Linear Demand Model
Suppose the demand is a linear function of price $p$

$$D(p)=a-bp$$

The revenue at price $p$ is given by

$$R(p)=p\times D(p)=p(a-bp)$$

The revenue-maximizing price $p^*$ satisfies

$$\frac{dR(p^*)}{dp}=0$$

i.e.,

$$p^{*}=\frac{a}{2b}$$

---

Now suppose there are two products with linear demand curves.

$$D_{1}(p_{1},p_{2})=a_{1}-b_{1}p_{1}+c_{1}p_{2}$$
$$D_{2}(p_{1},p_{2})=a_{2}+b_{2}p_{1}-c_{2}p_{2}$$

We have 

$$R_{1}(p_{1},p_{2})=p_{1}D_{1}(p_{1},p_{2})$$
$$R_{2}(p_{1},p_{2})=p_{2}D_{2}(p_{1},p_{2})$$

To obtain the optimal prices, we set

$$\frac{\partial (R_1(p_1, p_2) + R_2(p_1, p_2))}{\partial p_1} = 0$$
$$\frac{\partial (R_1(p_1, p_2) + R_2(p_1, p_2))}{\partial p_2} = 0$$

Thus,

$$p_1^\ast = \frac{-2 a_1 c_2 - (c_1 + b_2) a_2}{\Delta}, \qquad
p_2^\ast = \frac{-2 b_1 a_2 - (c_1 + b_2) a_1}{\Delta}$$

where $\Delta = (c_1 + b_2)^2 - 4 b_1 c_2$

