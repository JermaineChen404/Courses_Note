# The Goods Market

## The Composition of GDP
GDP

- Consumption (C)
	- goods and services purchased by consumers
- Investment (I) (fixed investment)
	- Non-residential
		- purchase by firms of **new** plants or machines
	- Residential
		- purchases by people of **new** houses
- Government spending (G)
	- purchases of goods and services by the gov
	- excludes government transfers
		- Medical or Social Security payment
	- excludes interest payment on the gov debt
- Net exports/trade balance ($NX=X-IM$)
	- ($+$) Exports (X)
	- ($-$) Imports (IM)
- Inventory investment
	- Production - Sales

>[!note]
>- trade surplus: $X>IM$ 
>- trade deficit: $X<IM$ 

## The Demand for Goods
The decomposition of GDP reveals the source of demand.

The total demand for **domestic** goods $Z$ is

$$Z\equiv C+I+G+X-IM$$

which is an [[Ch3 - The Goods Market#Types of Equation|identity]]

- This is the definition of $Z$
- inventory investment is **not** included
### Assumption
- Only **one good** economy
- Supply any amount at a given price 
	- Perfectly elastic supply
	- fixed price level
		- only valid in short run
	- no inflation concerns
	- focus only on the demand
- Closed economy
	- $X=IM=0$

Thus, demand becomes

$$Z\equiv C+I+G$$

### Consumption (C)
$C$ can be represented by a consumption function

$$C=\underset{(+)}{C(Y_{D})}$$

which is a [[Ch3 - The Goods Market#Types of Equation|behavioral equation]]

To be more specific and simpler, we further assume the function to be linear

$$C=c_{0}+c_{1}Y_{D}$$

where $Y_{D}=Y-T$ is the disposable income

- income after paying taxes and receiving transfers

>[!note] Consumption Parameters
>>[!check] (Marginal) Propensity to Consume
>>$c_{1}$
>>- the effect an additional dollar of disposable income has on consumption
>>- $0<c_{1}<1$
>>	- people tend to consume only part of increased disposable income
>
>>[!check] Consumer Confidence
>>$c_{0}$
>>- in extreme case ($Y_{D}\to 0$)
>>	- people need to eat even without income (by dissave)
>>- in most cases
>>	- changes in $c_{0}$ reflect changes in consumption for a given level of disposable income
>>		- e.g., due to changes in interest rate, optimistic about the future

### Investment (I)
- Endogenous variable
	- depends on other variables in the model
	- explained within the model
	- e.g., [[Ch3 - The Goods Market#Consumption (C)|consumption]]
- Exogenous
	- taken as given
	- not explained within the model
	- e.g. [[Ch3 - The Goods Market#Investment (I)|investment]]

We assume investment to be **exogenous** for simplicity here

$$I=\bar{I}$$

### Government Spending (G)
$T$ and $G$ describe **fiscal policy**, i.e., the choice of taxes and gov's spending.

We also assume $G$ and $T$ exogenous but with different reason from that of investment

- gov behave differently as consumers or firms
	- but not unpredictable
- one of the tasks of macroecon is to explore the implication of fiscal policy
- no need to use $\bar{T}$ and $\bar{G}$ since T and G are almost always exogenous

>[!note]
>- $G>T$: budget deficit
>- $G<T$: budget surplus
>- $G=T$: balanced budget

## The Determination of Equilibrium Output
$$Z= c_{0}+c_{1}(Y-T)+\bar{I}+G$$

Assume no inventory investment, **equilibrium in the goods market** requires that production be equal to the demand for goods:

$$Y=Z=C+I+G$$
which is an [[Ch3 - The Goods Market#Types of Equation|equilibrium equation]].

Further we have

$$Y=c_{0}+c_{1}(Y-T)+\bar{I}+G$$

In equilibrium, *production* $Y$ (the left side) equals *demand*, which in turn depends on *income* $Y$ (the right side) that itself equals *production*

>[!note]
>```mermaid
>flowchart LR
>Production --> |equilibrium condition|Demand
>Demand -->|behavioral observation| Income
>Income --> |identity|Production
>```

### Algebra
Rewrite the equilibrium equation gives

$$Y=\frac{1}{1-c_{1}}(c_{0}+\bar{I}+G-c_{1}T)$$


>[!note] $(c_{0}+\bar{I}+G-c_{1}T)$
>autonomous spending
>- positive for most of the time
>	- $c_{0}>0$
>	- $\bar{I}>0$
>	- $G-c_{1}T=(G-T)+T(1-c_{1})$
>		- $1-c_{1}>0$
>- negative only when $T\gg G$
>	- i.e. a very large budge surplus

>[!note] $\frac{1}{1-c_{1}}$
>multiplier
>- $\frac{1}{1-c_{1}}>1$
>- Effects of changes in each term in autonomous spending will be magnified by multiplier

### Graph
![[Pasted image 20250919151840.png]]
![[Pasted image 20250919153705.png]]

### Words
One unit change in demand will trigger a chain reaction

Demand increases $\to$ Production increases $\to$ Income increases $\to$ Consumption increases $\to$ Demand increases
```mermaid
flowchart LR
Demand --> Production
Production <--> |equivalent|Income
Income--> Consumption
Consumption --> Demand
```
 which can be expressed by a geometric series
$$1+c_{1}+c_{1}^2+c_{1}^3+\dots=\frac{1}{1-c_{1}}$$
The end result is an increase in output that is larger than the initial shift in demand, by a factor equal to the multiplier.

The size of the multiplier depends on the value of the propensity (tendency) to consume.

## IS Relation
There is an alternative view on the equilibrium from investment and saving.
$$\text{Saving}=\text{Private Saving}+\text{Public Saving}$$
Private saving $S$ equals customers' disposable income minus consumption
$$S\equiv Y-T-C$$
Public saving $S'$ equals taxes (net of transfer) minus government spending
$$S'\equiv T-G$$
Subtract taxes ($T$) from both sides of [[Ch3 - The Goods Market#The Determination of Equilibrium Output|previous equilibrium equation]]
$$Y-T-C=I+G-T$$
Or equivalently
$$I=(Y-T-C)+(T-G)=S+S'$$
> Therefore, the equilibrium in the goods market requires that investment equal saving (sum of private and public), which is called **IS relation**

```mermaid
flowchart LR
Firms --> |decide| Investment
Investment <--> |equivalent| Saving
Saving <--o |decide|Consumers
Saving <--o |decide|Government
```

The private saving can be written as
$$
\begin{align}
S&=Y-T-C \\
&=Y-T-c_{0}-c_{1}(Y-T) \\
&=-c_{0}+(1-c_{1})(Y-T)
\end{align}
$$
The parameter $(1-c_{1})$ is called the propensity to save.

Also,
$$I=-c_{0}+(1-c_{1})(Y-T)+(T-G)$$
We get the exact same result as before
$$Y=\frac{1}{1-c_{1}}(c_{0}+\bar{I}+G-c_{1}T)$$

>[!note] Unchanged Saving
>In equilibrium,
>
>$$I=S+(T-G)$$
>
>Saving is unchanged since $I$, $T$, and $G$ are all unchanged in the short run
>
>$$S=-c_{0}+(1-c_{1})(Y-T)$$
>
>- As people want to save more, they decrease consumption, and thus output declines
>	- $c_{0}\downarrow$, $S \uparrow$
>- As output decline, people's income decline, and thus they can save less
>	- $c_{0}\downarrow$, $C \downarrow$, $Y \downarrow$, $S \downarrow$












# Appendix
## Ex-Post vs. Ex-Ante
- Ex-Post (After the fact):
	- It is a measured fact that $GDP=Z$
	- they are the same thing in a ex-post view
- Ex-Ante (Before the fact, Planned)
	- In economic models, **planned aggregate demand** $Z$ and **planned output** $GDP$ might not be equal given inventory investments
## Types of Equation
- Identities
- Behavioral equations
- Equilibrium conditions
## Macroeconomists' Tools
1. Algebra
	- make sure the logic is correct
2. Graphs
	- build the intuition
3. Words
	- explain the results