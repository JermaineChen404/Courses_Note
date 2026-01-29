# Multi-step Binomial Tree Models
![[Pasted image 20251215234239.png]]
## Method I: Dynamic Replication
We start from the end of the tree at $T=1$ and move backward towards $t=0$

$$
S_{0}u^{2}\Delta_{1,u}-f_{uu}=S_{0}ud\Delta_{1,u}-f_{ud}
$$

$$(S_{0}u^{2}\Delta_{1,u}-f_{uu})e^{-rh}=S_{0}u\Delta_{1,u}-f_{u}$$

Thus, 

$$f_{u}=\frac{f_{uu}(1-de^{-rh})+f_{ud}(ue^{-rh}-1)}{u-d}$$

Similarly,

$$f_{d}=\frac{f_{ud}(1-de^{-rh})+f_{dd}(ue^{-rh}-1)}{u-d}$$

Iterating again gives

$$f=\frac{f_{u}(1-de^{-rT})+f_{d}(ue^{-rT}-1)}{u-d}$$

>[!question] Self-Financing
>The dynamic replication is self-financing, i.e., there is no inflow or withdrawal of cash after the initial purchase/sale of assets. Thus, we do not have to pay any further costs for changes in hedges

>[!warning] Limitation
>We note that for $n$-step binomial tree models, we have to iterate $n$ times, which is complicated and impractical for large $n$.
## Method II: Risk-Neutral Pricing
Recall that

$$f=e^{-rT}[pf_{u}+(1-p)f_{d}]$$

where

$$p=\frac{e^{rT}-d}{u-d}$$

i.e., $p$ does not depends on the stock price and is **the same at all nodes** as long as we assume the same $u$ and $d$ for each steps.

Repeated the pricing formula gives

$$\begin{align}
f_{u}&=e^{-rh}[pf_{uu}+(1-p)f_{ud}] \\
f_{d}&=e^{-rh}[pf_{du}+(1-p)f_{dd}] \\
f&=e^{-rh}[pf_{u}+(1-p)f_{d}]
\end{align}$$

Thus,

$$f=e^{-2rh}[p^{2}f_{uu}+2p(1-p)f_{ud}+(1-p)^{2}f_{dd}]$$

As we add more steps to the binomial tree, the risk-neutral valuation principle continues to hold. The option price is always equal to its expected payoff in a risk-neutral world discounted at the risk-free interest rate.

For $n$-step binomial tree, from binomial expansion we have 

$$C_0 = e^{-rT} \sum_{k=0}^{n} \binom{n}{k} p^k (1-p)^{n-k} 
\cdot \max\!\big(S_0 u^k d^{\,n-k} - K, \, 0\big)$$

## Cox-Ross-Rubinstein (CRR) Binomial Model
$$p=\frac{e^{r\Delta t}-d}{u-d}$$

The parameters $u$ and $d$ should be chosen to match the volatility of the stock. Assume the expected stock return are $\mu$ and the stock return volatility is $\sigma$.

The expected return at $t$ is

$$E_{t}\left[ \frac{S_{t+\Delta t}}{S_{t}} \right]=e^{\mu \Delta t}$$

Recall that $\sigma_{X}^{2}=E[X^{2}]-[E(X)]^{2}$, the variance of the return at $t$ is

$$p(u-1)^{2}+(1-p)(d-1)^{2}-[p(u-1)+(1-p)(d-1)]^{2}=\sigma^{2}\Delta t$$

Substituting for $p$,

$$e^{r\Delta t}(u+d)-ud-e^{2r\Delta t}=\sigma^{2}\Delta t$$

We solve for $u$ and $d$:

$$u=e^{\sigma \sqrt{ \Delta t }}\quad \text{and}\quad d=e^{-\sigma \sqrt{ \Delta t }}$$

Note that $ud=1$ implies the stock price remains the same after an up-move and a down-move.
