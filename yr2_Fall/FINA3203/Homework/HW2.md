# Q1
## 1
- Manage a duration mismatch
- Bet on economic recessions
- Create synthetic corporate bonds

## 2
An American option allows the buyer to buy (if call) or sell (if put) the underlying asset at the time before maturity, while a European option can only exercise the option at the exact pre-specified maturity date.

## 3
Wrong: The option is a right for the long position but an obligation for the short position. A European put option allows the long side to sell the underlying at the strike price. When the spot price is higher than the strike price at maturity, the long side can simply ignore the option and lose at most the option premium. When the spot price is lower than the strike price at maturity, the long side can exercise the option and earn the spread, which can be huge. On the other hand, the short position in a call option must sell the option at maturity if the spot price is higher than the strike price, where the loss can be infinite. The profit from the option premium if the otherwise, however, is limited. Therefore, they are not equivalent.

# Q2
Assume the quote currency is USD. The continuously-compounded US interest rate is $r$, and the EUR rate is $r^*$. The spot exchange rates today and at time $T$ are $S_{0}$ and $S_{T}$.

We further assume the US interest rate $r$ is lower than that of EU $r^*$, i.e.,
$$r<r^*$$
So we borrow $S_{0}e^{-r^*T}$ units of USD and convert it into $e^{-r^*T}$ EUR, and invest it at $r^*$. The payoffs at time $T$ is 

$$e^{-r^*T}\times e^{r^{*}T}=1\text{ EUR}$$

Convert it back to $S_{T}$ USD and pay back the debt gives our final payoff in USD:
$$S_{T}-S_{0}e^{(r-r^*)T}$$
To hedge the risk of decreased $S_{T}$, we can short the forward exchange rate and receive $F_{0,T}-S_{T}$ at time $T$. Thus, the final payoff is
$$F_{0,T}-S_{T}+S_{T}-S_{0}e^{(r-r^*)T}=F_{0,T}-S_{0}e^{(r-r^*)T}$$
The forward interest rate $F_{0,T}$, spot exchange rate $S_{0}$, and interest rates in both country are all known, and therefore we eliminate the exchange rate risk.

# Q3
## 1
We should 
- At $t=0$, long the 3mth $\times$ 15mth FRA from bank XYZ to hedge the borrowing cost.
-  At $t=3mth$,
	1. borrow the one year \$1M loan form the bank ABC in 3 month and
	2. - if $r_{3mth,15mth}>r_{0,3mth,15mth}$,
			- invest at $r_{3mth,15mth}$ the proceed from long the FRA
		- if $r_{3mth,15mth}<r_{0,3mth,15mth}$
			- borrow at $r_{3mth,15mth}$ to cover the loss from long the FRA
- At $t=15mth$, pay back the loan to bank ABC

## 2
We own bank ABC
$$1\times\left[ 1+12\%\times \frac{(15-3)}{12} \right]=1.12\text{M}$$
in 15 month. We will receive 
$$N_{0}\times\left( \frac{(r_{t_{1},t_{2}}-r^{FRA}_{t_{0},t_{1},t_{2}})\times(t_{2}-t_{1})}{1+r_{t_{1},t_{2}}\times(t_{2}-t_{1})} \right)=\frac{1\times((12\%-10\%)\times 1)}{1+12\%\times 1}=\frac{1}{56}\text{M}$$
in 3 months. In 15 months, we will have
$$\frac{1}{56}\times(1+12\%)-1.12=-1.1\text{M}$$
Thus, the actual borrowing cost is 
$$\frac{1.1-1}{1}=10\%$$

## 3
We own bank ABC
$$1\times\left[ 1+5\%\times \frac{(15-3)}{12} \right]=1.05\text{M}$$
in 15 month. We will pay 
$$N_{0}\times\left( \frac{(r_{t_{1},t_{2}}-r^{FRA}_{t_{0},t_{1},t_{2}})\times(t_{2}-t_{1})}{1+r_{t_{1},t_{2}}\times(t_{2}-t_{1})} \right)=\frac{1\times((10\%-5\%)\times 1)}{1+5\%\times 1}=\frac{1}{21}\text{M}$$
in 3 months. In 15 months, we will have
$$-\frac{1}{21}\times(1+5\%)-1.05=-1.1\text{M}$$
Thus, the actual borrowing cost is 
$$\frac{1.1-1}{1}=10\%$$

# Q4
- background
In January 2008, the bank Société Générale lost approximately €4.9 billion closing out positions over three days of trading beginning January 21, 2008, a period in which the market was experiencing a large drop in equity indices. The bank states these positions were fraudulent transactions created by Jérôme Kerviel, a trader with the company.

- trade and instruments involved
Jérôme Kerviel's primary instruments were European stock index futures. His trades included heavy directional bets on European stock market indices. In 2007, he initially profited by betting that markets would fall. By the end of that year, he had hidden profits of €1.4 billion. In early 2008, he reversed his strategy, taking a €50 billion long position betting that markets would rise. This sum was greater than the bank's own market capitalization at the time.

- trader's approach to the trade
His approach was fictitious trades. He took unhedged long positions betting on rising markets, without the required offsetting short positions typical in arbitrage. To conceal these, he entered fictitious hedge trades into the system, which he would cancel and replace when alerts arose, often describing them as errors. He closed positions just before detection windows (typically two to three days) and shifted to new instruments. When profitable, he created intentional losing trades to mask gains and avoid scrutiny.

- what went wrong & why did they lose

During this period, Europe equity markets, which were already under pressure from the emerging credit crisis, experienced a significant and sharp drop.

The scheme unraveled on January 19, 2008, when internal alerts finally traced the unauthorized positions to Kerviel. The bank unwound the €49.9 billion in positions over three days starting January 21, during a sharp market decline (e.g., a 6% drop in European indices on January 21), amplifying losses through unfavorable conditions. What went wrong was the failure of internal controls: despite 75 alerts, Kerviel's forgeries, lies, and system knowledge allowed evasion, as controls lacked a holistic view across departments. The positions violated prudential limits, risking the bank's solvency. Kerviel blamed panic selling by the bank, while Société Générale attributed the full loss to his fraud. The €4.9 billion net loss stemmed from a €6.3 billion unwinding hit offsetting the prior €1.4 billion hidden profit.

- conclusion
Individual vs. Institutional Responsibility: While Kerviel was found criminally liable and sentenced (though the fine was later canceled), French courts also acknowledged institutional failings. A Paris labour court even ruled that his dismissal was unlawful because the bank was aware of his misconduct, ordering SocGen to pay him compensation.
The Danger of a Profits-Over-Control Culture: The case suggests that a corporate culture which embraces risk-taking as long as it is profitable can create major flaws in operations. One analysis concluded that "risk taking was embraced as long as it made money for the bank".
The Critical Need for Robust and Enforced Controls: The case is a stark reminder that having control procedures is not enough. The bank had invested in controls, but a breakdown in their application allowed the fraud to go undetected. This underscores the importance of interpersonal oversight and managers knowing their employees' activities.

- Reference
https://www.societegenerale.com/sites/default/files/documents/proces-jk/jkerviel-10-points-uk.pdf
https://en.wikipedia.org/wiki/2008_Soci%C3%A9t%C3%A9_G%C3%A9n%C3%A9rale_trading_loss
https://www.theguardian.com/business/2008/feb/04/europeanbanks.france
https://www.investopedia.com/terms/j/jerome-kerveil.asp
# Q5
## 1
The net premium is
$$1.55+0.85-0.30-0.45=\$1.65$$

## 2
We first consider the payoff of the long position.
$$f(x)=\begin{cases}
27.5-x, \quad x \in[15,27.5)\\
0, \quad x\in[27.5,32.5) \\
x-32.5, \quad x\in[32.5,50]
\end{cases}
$$
![[Figure_1.png]]
The payoff of the short position is given by
$$f(x)=\begin{cases}
x-30, \quad x\in[15,30) \\
30-x, \quad x\in[30,50]
\end{cases}
$$
![[Figure_2.png]]
Combining them together and shift the combined curve by the net premium gives the profit diagram:
$$f(x)=\begin{cases}
-0.85, \quad x \in[15,27.5)\\
x-28.35, \quad x\in[27.5,30) \\
31.65-x, \quad x\in[30,32.5) \\
-0.85, \quad x\in [32.5,50]
\end{cases}
$$
![[Figure_3.png]]


