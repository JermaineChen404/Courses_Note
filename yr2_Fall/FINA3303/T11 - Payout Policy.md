# Payout Policy
## Uses of Free Cash Flow
![[Pasted image 20251103163911.png]]

$$\frac{\text{Future Cash Flow}}{\text{Shares Outstanding}}\iff \text{Expected Future Dividends Paid}$$

For companies that **pay dividends**, present value of the payoff to shareholders is:

$$PV_{d}=\frac{1}{\text{Shares Outstanding}}\left(\text{Excess Cash}+\sum \frac{FCFF_{t}}{(1+R_{wacc})^t}\right)$$




## Dividends Payment

### Dividend Payment Timeline
![[Pasted image 20251103164204.png]]


- Cum-dividend date: buyers are eligible for the dividend
- Ex-dividend date: sellers are eligible for the dividend

$$|\Delta \text{Stock Price}|=\text{Dividends Paid per share}$$

>[!Proof]
>>[!check] Dividend Discount Model
>>
$$P_{\text{cum}}=\frac{1}{\text{Shares Outstanding}}\left(\text{Excess Cash}+\sum \frac{FCFF_{t}}{(1+R_{wacc})^t}\right)$$
$$P_{\text{ex}}=\frac{1}{\text{Shares Outstanding}}\sum \frac{FCFF_{t}}{(1+R_{wacc})^t}$$
$$-\Delta \text{Stock Price}=P_{cum}-P_{ex}=\frac{\text{Excess Cash}}{\text{Shares Outstanding}}=\text{Dividends Paid per share}$$
>
>>[!check] Market Value Balance Sheet
>>![[Pasted image 20251207202827.png]]






Dividends are long-term commitments

Dividends can mitigate agency costs

## Stock Repurchase
$$\Delta \text{Stock Price}=0$$

>[!Proof]
>>[!check] Dividend Discount Model
>>
Let$$
P_{0}=\frac{1}{\text{Shares Outstanding}_{0}}\left(\text{Excess Cash}+\sum_{t=1}^{\infty} \frac{FCFF_{t}}{(1+R_{wacc})^t}\right)$$
Define$$
V_{\text{op}} \equiv \sum_{t=1}^{\infty} \frac{FCFF_{t}}{(1+R_{wacc})^t},\quad N_{0}\equiv \text{Shares Outstanding}_{0},\quad C\equiv \text{Excess Cash}.$$
Then $P_0=\frac{C+V_{\text{op}}}{N_0}$.
The repurchase uses $C$ at price $P_0$, so$$
\text{Shares Outstanding}_{rep}=N_{0}-\frac{C}{P_{0}}
= N_0-\frac{C}{(C+V_{\text{op}})/N_0}
= N_0\left(1-\frac{C}{C+V_{\text{op}}}\right)
= N_0\cdot\frac{V_{\text{op}}}{C+V_{\text{op}}}.$$
Post-repurchase, cash $C$ is paid out, leaving only the operating value $V_{\text{op}}$. Thus$$
\begin{aligned}
P_{rep}
&=\frac{1}{\text{Shares Outstanding}_{rep}}\sum_{t=1}^{\infty} \frac{FCFF_{t}}{(1+R_{wacc})^t} \\
&= \frac{V_{\text{op}}}{\,N_0\cdot\frac{V_{\text{op}}}{C+V_{\text{op}}}\,} \\
&= \frac{C+V_{\text{op}}}{N_0} \\
&= P_0.
\end{aligned}$$
Therefore,$$P_{rep}=P_{0}$$
>
>>[!check] Market Value Balance Sheet
>>![[Pasted image 20251207205024.png]]
- Open Market Repurchase ($\sim 95\%$)
	- buy shares at the market price
- Tender Offer ($\sim 5\%$)
	- buy at a prespecified price (typically with premium)

## Dividends or Repurchase
Tradeoff between current and future dividends.

- Pay dividends
	- higher current dividend, lower future dividend
- Share repurchase
	- lower current dividend, higher future dividend

In perfect market, investors are indifferent between dividends and share repurchase

- value of the firm is unchanged
- investors can create whatever income stream by homemade dividends
	- sell stocks (at the same price) to increase current dividends
	- buy stocks (at a lower price) to decrease current dividends

## Taxes on Dividends and Capital Gains
Assume tax on dividends only,

$$P_{cum}-P_{ex}=Dividend(1-T_{c})$$

### The Effective Dividend Tax Rate
Assume $T_{g}$ is the capital gain tax rate, and $T_{d}$ is the dividend tax rate

$$\begin{align}
\text{After tax gain from dividend}&=\text{After tax loss from stock price declines} \\
Div(1-T_{d})&=(P_{cum}-P_{ex})(1-T_{g})
\end{align}$$

Thus,

$$P_{cum}-P_{ex}=Div\times\frac{1-T_{d}}{1-T_{g}}=Div\times\left( 1-\left( \frac{T_{d}-T_{g}}{1-T_{g}} \right) \right)$$

where $T_{d}^*=\frac{T_{d}-T_{g}}{1-T_{g}}$ is the effective dividend tax rate.

$T_{d}^*$ measures the additional tax paid by the investor per dollar of after-tax capital gains income that is instead received as a dividend.
>$T_{d}>T_{g}\quad\Rightarrow$ Share repurchase is better than paying dividend

### Taxes on Interest Income
$$Div=\text{Excess Cash}\times r_{f}\times(1-T_{c})$$
$$P_{\text{retain}}=\frac{Div\times(1-T_{d})}{r_{f}\times(1-T_{i})}$$

The effective tax disadvantage of retaining cash is

$$T^{*}_{\text{retain}}=1-\frac{(1-T_{c})(1-T_{g})}{1-T_{i}}$$

If $T^{*}_{\text{retain}}>0$, the stock price will be lower if the firm retains cash.


