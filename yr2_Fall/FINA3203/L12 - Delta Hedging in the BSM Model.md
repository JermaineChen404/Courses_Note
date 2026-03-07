---
title: "L12 - Delta Hedging in the BSM Model"
course: FINA3203
type: Lecture
tags: [fina3203, delta hedging, bsm, gamma, theta, hedging]
---

Delta hedging is to hedge the first-order risks coming from the moves in the underlying stock price.

$$\Delta\equiv \frac{\partial \text{ Option Price}}{\partial S}$$

This is a general definition of Delta, regardless of the model we use.

Specifically in BSM model,

$$\Delta=\mathcal{N}(d_{1}) \quad\text{for calls,}\quad\text{and}\quad\Delta=-\mathcal{N}(-d_{1})\quad\text{for puts}$$

Geometrically, delta is the slope of the option price, plotted as a function of the underlying price


## Over a short time interval

- Small changes in stock price
	- Delta hedging works well
- Large changes in stock price
	- Delta hedging fails
	- we can use Gamma to hedge the second-order price risk

![[Pasted image 20251216234310.png]]

Geometrically, Delta hedging are trying to approximate the option price function (which is convex, not linear) with a line tangent to this function. This approximation is good for small moves in the underlying price but increasingly inaccurate for larger and larger moves.

## Over a longer time interval

- Small changes in stock price
	- Delta hedging makes profits
		- The profit will be the highest if the stock price stays the same
		- The profit comes from time decay ($\Theta$)
- Large changes in stock price
	- Delta hedging fails
		- We will not always lose but not well hedged (speculation instead)
		- Rebalance the hedge more often
			- incurs transaction costs

![[Pasted image 20251216234855.png]]

## Tradeoff between $\Theta$ and $\Gamma$
BSM implies a tradeoff between time decay $\Theta$ and convexity $\Gamma$

Time decay benefits sellers and hurts buyers

- lower chances of exercising the option

Convexity benefits buyers and hurts sellers

- For Option Buyers (Long Gamma)
	- **Positive Gamma:** When you buy options (calls or puts), you are **long gamma**.
    - **Effect:** Your Delta increases when the stock rises and decreases when the stock falls.
	    - If the stock goes up, your option behaves more like being long the stock (Delta rises).
        - If the stock goes down, your option behaves more like being short the stock (Delta falls).

The seller of the delta-hedged option takes the risk for large moves (measured by convexity or Gamma) and is compensated for that precisely with time decay (measured by Theta).
