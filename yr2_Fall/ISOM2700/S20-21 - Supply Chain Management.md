# Supply Chain Management
>[!Definition]
>A supply chain is the system of organizations, people, activities, information and resources involved in moving a product or service from supplier to customer.

![[Pasted image 20251213200926.png]]

---
title: S20-21 - Supply Chain Management
course: ISOM2700
type: Lecture
tags:
  - isom2700
  - supply_chain
  - bullwhip_effect
  - revenue_sharing
  - matching
---

>[!tip] From Local Optimization to Sequential Optimization
>>[!note] Local Optimization
>>- Make decision based on its own interest
>>- Compete within a supply chain
>>![[Pasted image 20251213202044.png]]
>
>>[!note] Sequential Optimization
>>- Make decision sequentially and collaboratively from the downstream to the upstream
>>- Compete with other chains for end consumers
>>![[Pasted image 20251213202101.png]]

## Pricing: Double Marginalization
![[Pasted image 20251213203922.png]]
![[Pasted image 20251213203936.png]]

Additional $n$ intermediates in the supply chain mark-up $n$ times the price beyond its marginal costs. The resulted higher end price for customer lowers the demanded quantity and thus the overall profits for the supply chain as a whole.

>[!check] Solution
>Revenue Sharing: The whole supply chain acts as a whole and mark-ups only once, and then split the overall revenue among the supply chain.

## Inventory Planning
### The Bullwhip Effect
Demand and inventory variability increases as one moves up in the supply chain away from customers (i.e., from downstream to upstream)

![[Pasted image 20251213210254.png]]

Causes and Solution

- Multiple participants make their decisions independently
	- centralized ordering decisions
- Lead time between requesting for products and receiving actual products
	- improve the efficiency in goods shipment
- Bad forecasting of demand
	- information sharing
- When demand exceeds manufacturing (rationing), customers further exaggerate their needs (shortage gaming).

## Hedging Operational Risk with Contracts
### Wholesale Price Contract
The supplier charges a fixed wholesale price $w\in(c,p)$ for every unit delivered to the retailer. 

Given the wholesale price, the retailer decides how many units to order.

![[Pasted image 20251213224907.png]]

For centralized supply chain,

$$\frac{C_{u}}{C_{o}+C_{u}}=\frac{p-c}{c+(p-c)}=\frac{p-c}{p}$$

For decentralized supply chain,

$$\frac{C_{u}}{C_{o}+C_{u}}=\frac{p-w}{w+(p-w)}=\frac{p-w}{p}$$

Since $w>c$,

$$q^{*}_{c}>q^{*}_{d}$$

Thus, the retailer orders less than the supply chain optimum under wholesale price contract.

![[Pasted image 20251213225605.png]]

$$Profit_{d}=p\times \mathbb{E}[\min(q^{*}_{d},D)]-c\times q^{*}_{d}$$
### Revenue Sharing Contract
- The supplier charges a fixed wholesale price $w\in(0,p)$ for every unit delivered to the retailer.
- For each unit of sales to an end consumer, the retailer pays the supplier a fixed percentage share $y$ of the retail price to the supplier

Given the wholesale price, the retailer decides how many units to order.

![[Pasted image 20251213230054.png]]


$$C_{u}=p(1-y)-w$$

$$C_{o}=w$$

Introducing $y$, we can make retailer order the optimal quantity (the first-best outcome) by choosing a pair of $w$ and $y$ such that

$$\frac{C_{u}}{C_{o}+C_{u}}=\frac{p(1-y)-w}{w+p(1-y)-w}=\frac{p-c}{p}$$

Note that the wholesale price $w$ can be lower than production cost $c$ since the supplier receive additional $p\times y$ as compensation.

The wholesale price can be considered as an internal transfer; does not impact supply chain’s total profit. What really matters is that retailer orders the optimal quantity as the first-best outcome which is determined by $\frac{C_{u}}{C_{o}+C_{u}}$.

![[Pasted image 20251213232822.png]]

## Matching
- Each supplier can be matched to at most one customer;
- Each customer can be matched to at most one supplier.
- Connect the supplier with customer by maximizing the total utility
### Stable Marriage Problem
Stable Marriage problem is the problem of finding a stable matching between two equally sized sets of elements (i.e.,𝑀 = 𝑁) given an ordering of preferences for each element.

- If a man and a woman (who are not couple) prefer each other over their current spouses, then the marriage is **NOT** stable.
- stable marriage is **NOT** unique
### Gale-Shapley Algorithm
>[!rule]
>Men propose to women (can be the other way around):
>
>- Women cannot reject; but she can pick the one at the top of the preference list if there are multiple suitors (in this case, women are passive).
>- Matched men cannot re-propose; but matched women can change the partner.

1. **Initialization:** All participants are unmatched.
2. **Proposal phase:**
    - Each unpaired member of one set (say, men) “proposes” to their most-preferred partner not yet rejected.    
3. **Acceptance phase:**
    - Each member of the other set (say, women) tentatively accepts the best proposal they’ve received so far, and rejects the rest.
4. **Iteration:**
    - Rejected proposers move on to their next choice.
    - Tentative matches can be broken if a better proposal arrives later.
5. **Termination:**
    - Process continues until everyone is matched.
    - The result is a **stable matching**.

>[!tip] Implications
>- a stable matching always exists.
>- The group that proposes receive the optimal result
