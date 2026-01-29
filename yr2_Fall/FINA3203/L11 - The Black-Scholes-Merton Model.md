# The Black-Scholes-Merton Model
>[!Assumptions]
>- Financial markets have no frictions
>	- no taxes and transaction costs
>	- assets are perfectly divisible
>	- no restrictions on short sales
>- Same and constant interest rate for borrowing and lending
>- The stock price has a continuous path
>- The mean and variance of the log returns are constant
>- Independent log return over any period
>- normally distributed log return

>[!tip] Inputs
>- $S_{t}=$ stock price at time $t$
>- $K=$ strike price
>- $T=$ maturity time
>- $t=$ current time
>- $r=$ annualized continuously compounded risk-free interest rate
>- $\sigma=$ annualized standard deviation of log returns
>- $q=$ continuously compounded dividend

The value of a European call option at time $t$ is

$$C(S_{t},\sigma,r,K,T-t)=S_{t}e^{-q(T-t)}N(d_{1})-Ke^{-r(T-t)}N(d_{2})$$

where

$$d_{1}=\frac{\ln\left( \frac{S_{t}}{K} \right)+\left( r+\frac{1}{2}\sigma^2 \right)(T-t)}{\sigma \sqrt{ T-t }}$$

$$d_{2}=d_{1}-\sigma \sqrt{ T-t }=\frac{\ln\left( \frac{S_{t}}{K} \right)+\left( r-\frac{1}{2}\sigma^2 \right)(T-t)}{\sigma \sqrt{ T-t }}$$

$N(X)$ is the cumulative density function of a standard normal random variable

The value of a European put option on the same stock with the same strike price is

$$P(S_{t},\sigma,r,K,T-t)=Ke^{-r(T-t)}N(-d_{2})-S_{t}e^{-q(T-t)}N(-d_{1})$$

Since $N(X)=1-N(-X)$, we have

$$Call-Put=S_{t}e^{-q(T-t)}-Ke^{-r(T-t)}$$

which is consistent with the Put-Call Parity.

## Interpretation
### From Replicating Portfolio to BSM
The formula expresses an option as a self-financing portfolio of stock and bond that changes over time

- $N(d_{1})$ is the **number of shares** in the replicating portfolio at time $t$. Thus it is equivalent to $\Delta$ in the binomial model, which is also the sensitivity of the call's price to the stock price

$$\Delta_{call}=\frac{\partial C}{\partial S_{t}}=N(d_{1})\in(0,1)$$

- $Ke^{-r(T-t)}N(d_{2})$ is the value of bonds we short in the replicating portfolio

Thus, the BSM formula essentially states that the value of the call today is the cost of the replicating portfolio today.

$$C(S_{t},\sigma,r,K,T-t)=\Delta_{call}S_{t}-B_{call}=S_{t}N(d_{1})-Ke^{-r(T-t)}N(d_{2})$$

Similarly for a put,

- $\Delta_{put}=\frac{\partial P}{\partial S_{t}}=-N(-d_{1})=-(1-N(d_{1}))<0$ is the number of shares we short
- $Ke^{-r(T-t)}N(-d_{2})$ is the value of bonds we long in the replicating portfolio

$$P(S_{t},\sigma,r,K,T-t)=B_{put}-\Delta_{put}S_{t}=Ke^{-r(T-t)}N(-d_{2})-S_{t}N(-d_{1})$$

### From Binomial Tree to BSM

>[!note] Derivations of the formula
>- **Cox-Ross-Rubinstein:** Use a binomial tree and make the step size very small and the number of steps very large
>- **Merton:** The option price is based on the risk-neutral expectation of the option payoffs, i.e. solve $E^{*}[\max(S_{T}-K,0)]$
>- **Black-Scholes:** Derive a partial differential equation for the option price based on dynamic hedging portfolios

For one-step binomial tree,

$$\begin{align}
C_{0}&=e^{-rT}E^{*}[\max(S_{1}-K,0)]=e^{-rT}p(S_{1,u}-K) \\
&=S_{0}\times(e^{-rT}pu)-Ke^{-rT}\times p \\
&=S_{0}\times N_{1}-Ke^{-rT}\times N_{2}
\end{align}
$$

which looks similar to the BSM formula:

$$C_{0}=S_{0}\times N(d_{1})-Ke^{-rT}\times N(d_{2})$$

This analogy gives us another angle of interpretation:

- $N(d_{2})$ is the risk neutral probability to exercise the option at $T$
- $S_{0}\times N(d_{1})$ is the discounted expected value of the stock that we may receive from the call
- $Ke^{-rT}\times N(d_{2})$ is the discounted expected value of the strike that we may pay on the call

For $n$-step binomial tree, it can be shown mathematically that

$$\lim_{ n \to \infty } N_{1}=N(d_{1})\quad\text{and}\quad \lim_{ n \to \infty } N_{2}=N(d_{2})$$

Thus, the BSM model is the limit of the binomial tree when the number of steps $n$ goes to infinity.

## The Option Greeks
The Greeks measure the sensitivity of the option price with respect to one parameter in the BSM formula, while holding all other parameters fixed.

### Delta $\Delta$
Sensitivity of the option price to a small increase in the price of the underlying

$$\Delta = \frac{\partial \text{ Option Price}}{\partial S} = 
\begin{cases} 
\mathcal{N}(d_1) & \text{for Calls} \\
-\mathcal{N}(-d_1) & \text{for Puts}
\end{cases}$$

![[Pasted image 20251216215452.png]]

For call delta,

- As $S\gg K$ the option is **deep in-the-money**:
	- $d_1 \to \infty$, so $\Delta_{call}=\mathcal{N}(d_1) \to 1$
	- Already guaranteed to pay off, so they move almost one-for-one with the stock.
- As $S \ll K$, the option is **deep out-of-the-money**:
	- Unlikely to pay off, so delta approaches 0

$$\Delta_{put}=-N(-d_{1})=N(d_{1})-1=\Delta_{call}-1$$

### Gamma $\Gamma$
Sensitivity of Delta ($\Delta$) to a small increase in the price of the underlying

$$\Gamma = \frac{\partial \Delta}{\partial S} = \frac{\mathcal{N}'(d_1)}{S \sigma \sqrt{T}} 
\quad \text{where} \quad 
\mathcal{N}'(x) = \frac{e^{-x^2/2}}{\sqrt{2\pi}}$$

![[Pasted image 20251216223158.png]]

$$\Gamma_{call}=\Gamma_{put}$$

>[!Proof]
>$$C-P=S-Ke^{-r(T-t)}$$
>
>$$\frac{\partial}{\partial S}(C-P)=\Delta_{call}-\Delta_{put}=1$$
>
>$$\frac{\partial^{2}}{\partial S^2}(C-P)=\Gamma_{call}-\Gamma_{put}=0$$

### Theta $\Theta$
Sensitivity of the option price to a small **decrease** in the time to maturity $\tau$

$$\Theta=-\frac{\partial \text{ Option Price}}{\partial\,\tau}$$

For Call options,

![[Pasted image 20251216224009.png]]

$\Theta<0$ for all call options

- If $S$ is high, the option is in-the-money. The discounted value of strike call buyers pay is larger as $\tau$ is smaller
	- pay more as maturity approach
	- discounting effect
- If $S$ is low, the option is out-of-the-money, and a smaller $\tau$ makes it less likely that the call will be exercised.
	- uncertainty effect

For Put options,

![[Pasted image 20251216224017.png]]

$\Theta<0$ for high $S$ and $\Theta>0$ for low $S$

- If $S$ is high, the option is out-of-the-money, and a smaller $\tau$ makes it less likely that the put will be exercised.
	- uncertainty effect
- If $S$ is low, the option is in-the-money. The discounted value of strike put buyers receive is larger as $\tau$ is smaller
	- receive more as maturity approach
	- discounting effect

### Vega $\mathcal{V}$
Sensitivity of the option price to a small increase in volatility $\sigma$

$$\mathcal{V} = \frac{\partial \text{ Option Price}}{\partial \sigma} 
= S \sqrt{\tau}\, \mathcal{N}'(d_1) > 0$$

When volatility increases, both put and call prices increase, since options have a higher chance to be exercise.

![[Pasted image 20251216231343.png]]

Vega is the same for calls and puts.