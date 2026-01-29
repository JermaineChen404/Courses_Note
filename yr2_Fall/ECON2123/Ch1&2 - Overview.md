# Overview
## GDP: The Aggregate Output
- Production Side:
	- The value of the final goods
	- The sum of value added
		- value of production $-$ value of the intermediate goods used in production
- Income Side:
	- the sum of incomes
		- labor income $+$ capital/profit income
### Nominal and Real GDP
> [!check] Nominal GDP
>
>- sum of the quantities of final goods produced $\times$ respective **current** price
>- "nominal" for variables expressed in current prices
>- Includes the effect of inflation

> [!check] Real GDP
>
>- sum of the quantities of final goods produced $\times$ base year price
>- "real" for variables expressed in goods
>- exclude the effect of inflation

![[Pasted image 20250911005946.png]]

- two lines intersect at the base year (i.e. 2005 in this case)
- price generally inflate over time
	- before the base year, $\text{Real GDP}>\text{Nominal GDP}$
	- after the base year, $\text{Real GDP}<\text{Nominal GDP}$

> [!note] Synonyms
>
>- Nominal GDP
>	- dollar GDP / GDP in current dollar
>	- \$$Y_{t}$
>- Real GDP
>	- GDP in terms of goods / adjusted for inflation
>	- $Y_{t}$

>[!question] Problem with Using Base Year Fixed Prices
>-  changes in qualities (value) of the same goods
>>[!tip] hedonic pricing
>>
>>estimating the value of a good or asset by breaking down its price into the value contributed by its individual characteristics and external factors.
>
>- changes in relative prices
>>[!tip] Real GDP in chained dollars
>>calculating real GDP that uses _chain-weighted indexes_ rather than fixed base-year prices
>>
>>- Uses _average growth rates_ between consecutive years, linking them (“chaining”) together.
>>- This reduces distortion from relative price changes and substitution effects.
### Level versus Growth Rate
Real GDP per capita

- the ratio of real GDP to the population
- measures the average standard of living of the country

GDP Growth in year $t$

- $\frac{Y_{t}-Y_{t-1}}{Y_{t-1}}$
- Recession if at least two consecutive quarters of negative growth

### What GDP Misses
- Without market prices
	- Government services
- Not traded in markets
	- Household production
	- Leisure
- Depletion of natural and environmental resources

>[!quote]
>GDP measures everything, in short, except that which makes life worthwhile.
>\- Robert F. Kennedy
## Unemployment Rate
$N=$ Employment: the number of people **who have a job**

$U=$ Unemployment: number of people do not have a job **but are looking for one**

$$\text{Labour force}=\text{Employment}+\text{Unemployment}$$

$$\text{participation rate}=\frac{\text{labor force}}{\text{population}}$$

$u=$ Unemployment rate

$$u=\frac{\text{Unemployment}}{\text{Labour Force}}=\frac{\text{Unemployment}}{\text{Employment}+\text{Unemployment}}$$


High unemployment can imply

- more people are entering labor market
- suffering of the unemployed
- inefficient utility of resources

## Inflation Rate
Inflation rate is the growth rate of the price level

### Price Level
>[!note] Measures of Price Level
>
>- The average price of **output produced**
>>[!check] GDP deflator: $P_{t}$
>>The GDP Deflator in year $t,P_{t}$ is defined as
>>
>>$$P_{t}=\frac{\text{Nominal }GDP{_{t}}}{\text{Real }GDP_{t}}=\frac{\$Y_{t}}{Y_{t}}$$
>>
>>- $P_{t}$ is a index number, with no economic interpretation for its absolute level
>>- Excludes imports, includes exports
>
> - The average price of **consumption**
>>[!check] Consumer Price Index (CPI)
>>- Measures the cost of living by
>>	- the average price of a fixed basket of goods & services **consumed by households**
>>- Includes imports, excludes exports

CPI and GDP deflator move together most of the time

-  Included in GDP but not CPI
	- **Industrial machinery** (capital goods, not consumed by households)
	-  **Exports** (not consumed domestically)
- Included in CPI but not GDP
	- **Imported goods** (produced abroad but sold domestically)
- Not in Either GDP nor CPI
	- **Intermediate goods** (steel used to make cars, not counted separately)
	- **Unpaid household work** (cooking, childcare at home)
	- **Illegal/underground economy** (unless reported)
	- **Environmental services** (clean air, biodiversity, unless monetized)


### Inflation rate
The rate of inflation $\pi_{t}$ is defined as the rate of change of the GDP deflator:

$$\pi_{t}=\frac{P_{t}-P_{t-1}}{P_{t-1}}$$

- $N$ = Nominal GDP
    
- $R$ = Real GDP
    
- $P$ = GDP Deflator (which is a price index)

Given that $N=R\times P$,

$$\frac{dN}{dt}=\frac{dP}{dt}\times R+P\times \frac{dR}{dt}$$
$$\frac{\frac{dN}{dt}}{N}=\frac{\frac{dP}{dt}\times R}{P\times R}+ \frac{P\times\frac{dR}{dt}}{P\times R}$$
$$\frac{\frac{dN}{dt}}{N}=\frac{\frac{dP}{dt}}{P}+ \frac{\frac{dR}{dt}}{R}$$

The rate of growth of nominal GDP is equal to the inflation rate plus
the rate of growth of real GDP.

- **Proportionate** rate of growth
- Not absolute growth rate (derivative), which requires chain rule

> [!Pure Inflation]
>
>- a faster but proportional increase in all prices and wages
>- relative prices unaffected
>- no pure inflation in reality

> [!question] Cons of Inflation
>
>- inflation affects income distribution
>	- retirees cannot keep up with current price level
>- more uncertainty
>	- some prices are fixed by law or regulation

> [!warning] Deflation $\neq$ Recession
>
>- Deflation is a decrease in price level
>- Recession is a decrease in real output






## Stylized Facts
simplified, broadly observed empirical patterns in economic or social data that are presented in a generalized way, abstracting from specific details
### Okun's  Law
![[Pasted image 20250914161102.png]]

- Higher output growth leads to a decrease in unemployment
	- the key to decreasing unemployment is a high enough rate of growth
- It takes a growth rate of about 3% to keep unemployment constant
	- labor force increases over time
	- output per worker increases over time
### The Phillips Curve
![[Pasted image 20250914163633.png]]

- lower unemployment leads to an increase in inflation
- when unemployment rate has been below 6%, inflation has typically increased
- inflation rate measured in CPI
- only true **on average**

## Appendix
### Hedonic Pricing
Problem: changes in the quality of existing goods

value goods with different characteristics in the market in the given year.
### Chain-Weighting
Problem: changes in the relative price

e.g. real GDP in chained (2005) dollars

1. **Calculate Growth Between Two Consecutive Years:** To find the real growth rate from 2004 to 2005, economists do the calculation _twice_:
	- **Using 2004 prices:** Value the 2005 output at 2004 prices and compare it to 2004's output (valued at 2004 prices). This gives one growth rate.
    
	- **Using 2005 prices:** Value the 2004 output at 2005 prices and compare it to 2005's output (valued at 2005 prices). This gives a second growth rate.
    
	- The **Fisher Index** is the geometric mean of these two growth rates. This creates a single, "chained" growth rate that is not biased toward the structure of either year.
2. **Create a Chain Index:** This process is repeated for every pair of consecutive years (2005-2006, 2006-2007, and so on). This creates a chain of annual growth rates that are always based on contemporary price structures.
3. **Anchor to the Reference Year (2005):** Finally, this entire chain of growth rates is anchored to the **reference year**—2005. The actual dollar value of Nominal GDP in 2005 is set as the Real GDP value for that year. The growth rates for all other years are then applied to this 2005 value to create a continuous time series expressed in "2005 dollars."