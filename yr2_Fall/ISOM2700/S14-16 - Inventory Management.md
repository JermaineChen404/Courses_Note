# Inventory Management
Inventory is a stock of goods that 

- company has paid for but customers have not yet paid for
- stored in the physical or virtual warehouses

## Why Hold Inventory
- Transactional motive
	- economies of scale
	- competition purpose
- Precautionary motive
	- Demand/Supply uncertainty
- Speculative motive
	- Fluctuating value

## Newsvendor Model
>[!example] Setup
>- Uncertain Demand
>- Perishable Product
>	- Short lifecycle
>- Order before observing demand 

- Short lifecycle products
- Tradeoff between costs of excess leftover inventory and excess demand

### Critical Fractile Analysis

- Cost of under-stocking: $C_{u}=\text{price}-\text{cost}$
- Cost of over-stocking: $C_{o}=\text{cost}-\text{salvage value}$

$$
\begin{align}
EV[\text{Profit}(n\to n+1)]&=C_{u}\times P(\text{Demand}>n)-C_{o}\times P(\text{Demand}\leq n) \\
&=C_{u}-(C_{u}+C_{o})\times P(\text{Demand}\leq n)
\end{align}
$$

![[Pasted image 20251107185622.png]]

The optimal quantity is $n$ such that $\text{Profit}(n\to n+1)=0$

Thus, $n^*$ is given by

$$P(\text{Demand}\leq n^*)=\frac{C_{u}}{C_{u}+C_{o}}$$

#### Normally Distributed Demand
z value:

$$z=\frac{n-\mu}{\sigma}$$

Optimal inventory amount is given by:

$$n^*=\mu+z^*\times \sigma$$

where $z^*$ is given by:

$$z^*=\text{normsinv}\left( \frac{C_{u}}{C_{u}+C_{o}} \right)$$

![[Pasted image 20251107191657.png]]

## Economic Order Quantity (EOQ) Model
- Long lifecycle products
- Tradeoff between setup and holding costs, driven by the frequency of ordering
- assume deterministic demand
	- known, constant, and predictable

### The Inventory "Saw-Tooth" Pattern
- $Q=$ Quantity in each order
- $D=$ Demand rate
- $\frac{Q}{D}=$ Time between shipments

![[Pasted image 20251107192635.png]]

### Derive EOQ
Given
- $S=$ Setup/Order Cost
- $H=$ Marginal holding cost

$$
\begin{align}
\text{Total Cost}&=\text{Holding Cost}+\text{Ordering Cost} \\
&=\frac{HQ}{2}+\frac{SD}{Q}
\end{align}
$$

![[Pasted image 20251107193137.png]]

The optimal quantity is $Q$ such that $\frac{d\,\text{Total Cost}}{dQ}=0$

$$\frac{d\,TC(Q)}{dQ}=-\frac{DS}{Q^2}+\frac{H}{2}=0$$

We have the optimal order quantity:

$$Q^*=\sqrt{ \frac{2DS}{H} }$$

which is called the **E**conomic **O**rder **Q**uantity.

The **EOQ** can also be obtained by letting $\text{setup cost}=\text{holding cost}$:

$$\frac{DS}{Q}=\frac{QH}{2}$$

which gives the same solution.

#### Purchasing Cost
Introducing per-unit purchasing cost $=DC$ gives:

$$\text{Total cost}=DC+\frac{HQ}{2}+\frac{SD}{Q}$$

which does not affect EOQ.

#### Lead Time
Lead time: $L=$ how long it takes to receive the order, which determines when to order.

Re-Order Point (ROP) is the demand (inventory level) during the lead time

$$ROP=D\times L$$

![[Pasted image 20251107195223.png]]

### EOQ with Uncertain Demand
![[Pasted image 20251107195348.png]]

Optimal Re-Order Point $ROP^*$ under uncertain demand satisfies

$$P(\text{Demand during lead time}\leq ROP^*)=\frac{C_{u}}{C_{u}+C_{o}}$$

Assume **demand per unit time** is normally distributed with mean $D$ and standard deviation $\sigma$

$\Rightarrow$ **Demand during lead time** is normally distributed with mean $DL$ and standard deviation $\sigma \sqrt{ L }$

- $ROP^*=$ ROP with normally distributed demand
- $ROP=$ ROP with deterministic demand

$$ROP^*=ROP+\text{Safety stock}$$

$$ROP^*=DL+z^*\sigma \sqrt{ L }$$

$z^*$ is the **critical fractile quantile** from the standard normal distribution, chosen so that:
    

$$P(Z≤z^*)= \frac{C_u}{C_u + C_o}$$

where $Z \sim N(0,1)$.

### Service Level
Service level $=$ probability that demand during lead time is fully met, i.e.,

$$P(\text{Demand during lead time}\leq ROP^*)=\frac{C_{u}}{C_{u}+C_{o}}$$

![[Pasted image 20251107202948.png]]

As service level approaches 1, Each small increment in service level requires a **big jump in safety stock**, because you’re covering the extreme tail of the distribution.

## Inventory Pooling
>[!tip] No Pooling
> Two branches manage their own inventory separately.
> 
> $$n_{1}^{*}=\mu_{1}+z^{*}\sigma_{1},\quad n_{2}^{*}=\mu_{2}+z^{*}\sigma_{2}$$
> 
> Total inventory $=$
> 
> $$n_{1}^{*}+n_{2}^{*}=(\mu_{1}+\mu_{2})+z^{*}(\sigma_{1}+\sigma_{2})$$

>[!question] Pooling
> Combine two branches into a single inventory pool.
> 
> $$n_{1+2}^{*}=(\mu_{1}+\mu_{2})+z^{*}\sqrt{ \sigma_{1}^2+\sigma_{2}^2 }$$

Since 

$$\sqrt{ \sigma_{1}^2+\sigma_{2}^2 }\leq \sigma_{1}+\sigma_{2}$$

$$n_{1+2}^{*}\leq n_{1}^*+n_{2}^*$$

for $z^*>0$.

>[!takeaway]
>when the underage cost is higher than overage cost ($z^*>0$), pooling reduces the safety stock requirement.