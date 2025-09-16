# Aggregate Output
## Gross Domestic Product (GDP)
### Calculation
- Production Side:
	- The value of the **final** goods and services produced in the economy during a given period.
	- The sum of value added in the economy during a given period.
		- value of production $-$ value of the intermediate goods used in production
- Income Side:
	- the sum of incomes in the economy during a given period
		- labor income $+$ capital/profit income
### Nominal and Real GDP
> Nominal GDP
- sum of the quantities of final goods produced $\times$ respective **current** price
- "nominal" for variables expressed in current prices
- Includes the effect of inflation
- normally higher than real GDP

> Real GDP
- sum of the quantities of final goods produced $\times$ a **common** price
- [[Ust_Note/yr2_Fall/ECON2123/Ch1&2 - Overview#Chain-Weighting|real GDP in chained (2005) dollars]]
- ![[Ust_Note/yr2_Fall/ECON2123/attachments/Pasted image 20250911005946.png]]
	- two lines intersect at the anchor year (i.e. 2005 in this case)
	- before 2005, $\text{Real GDP}>\text{Nominal GDP}$ due to inflation

> Synonyms
- Nominal GDP
	- dollar GDP / GDP in current dollar
	- \$$Y_{t}$
- Real GDP
	- GDP in terms of goods / adjusted for inflation
	- $Y_{t}$
### Level versus Growth Rate
> Real GDP per person
- average standard of living of the country

> GDP Growth in year $t$
- $\frac{Y_{t}-Y_{t-1}}{Y_{t-1}}$
- Recession if at least two consecutive quarters of negative growth
# Unemployment Rate
$L$: Labor Force
$N$: Employment
$U$: Unemployment: number of people do not have a job **but are looking for one**
$$
L=N+U
$$
$u$: Unemployment rate
$$u=\frac{U}{L}$$
$$\text{participation rate}=\frac{\text{labor force}}{\text{population}}$$
> High unemployment can imply
- more people are entering labor market
- suffering of the unemployed
- inefficient utility of resources
# Inflation Rate
> Inflation rate: the rate at which the price level increases

> Two measures of the price level
- GDP deflator
- Consumer Price Index

> Pure Inflation
- a faster but proportional increase in all prices and wages
- relative prices unaffected
- no pure inflation in reality

> Cons of Inflation
- inflation affects income distribution
	- retirees cannot keep up with current price level
- more uncertainty
	- some prices are fixed by law or regulation

> Deflation $\neq$ Recession
- Deflation is a decrease in price level
- Recession is a decrease in real output

## The GDP Deflator
The GDP Deflator in year $t,P_{t}$ is defined as
$$P_{t}=\frac{\text{Nominal }GDP{_{t}}}{\text{Real }GDP_{t}}=\frac{\$Y_{t}}{Y_{t}}$$
- $P_{t}$ is a index number
	- no economic interpretation for its level

The rate of inflation $\pi_{t}$ is defined as the rate of change of the GDP deflator:
$$\pi_{t}=\frac{P_{t}-P_{t-1}}{P_{t-1}}$$
### The Growth Rate
- $N$ = Nominal GDP
    
- $R$ = Real GDP
    
- $P$ = GDP Deflator (which is a price index)

Given that $N=R\times P$,
$$\frac{dN}{dt}=\frac{dP}{dt}\times R+P\times \frac{dR}{dt}$$
$$\frac{\frac{dN}{dt}}{N}=\frac{\frac{dP}{dt}\times R}{P\times R}+ \frac{P\times\frac{dR}{dt}}{P\times R}$$
$$\frac{\frac{dN}{dt}}{N}=\frac{\frac{dP}{dt}}{P}+ \frac{\frac{dR}{dt}}{R}$$
The rate of growth of nominal GDP is equal to the rate of inflation plus
the rate of growth of real GDP.
- **Proportionate** rate of growth
- Not absolute growth rate (derivative), which requires chain rule
## The Consumer Price Index (CPI)
- It measures the cost of living
- give the cost in dollars of a specific list of goods and services over time
- CPI and GDP deflator move together most of the time
- when price of imported goods increases, CPI increases faster than the GDP deflator

# Relation among Output, Unemployment, and Inflation
## Okun's  Law
![[Ust_Note/yr2_Fall/ECON2123/attachments/Pasted image 20250914161102.png]]
- Higher output growth leads to a decrease in unemployment
	- the key to decreasing unemployment is a high enough rate of growth
- It takes a growth rate of about 3% to keep unemployment constant
	- labor force increases over time
	- output per worker increases over time
## The Phillips Curve
![[Ust_Note/yr2_Fall/ECON2123/attachments/Pasted image 20250914163633.png]]
- lower unemployment leads to an increase in inflation
- when unemployment rate has been below 6%, inflation has typically increased
- inflation rate measured in CPI
- only true **on average**









# Appendix
## Chain-Weighting
e.g. real GDP in chained (2005) dollars
1. **Calculate Growth Between Two Consecutive Years:** To find the real growth rate from 2004 to 2005, economists do the calculation _twice_:
	- **Using 2004 prices:** Value the 2005 output at 2004 prices and compare it to 2004's output (valued at 2004 prices). This gives one growth rate.
    
	- **Using 2005 prices:** Value the 2004 output at 2005 prices and compare it to 2005's output (valued at 2005 prices). This gives a second growth rate.
    
	- The **Fisher Index** is the geometric mean of these two growth rates. This creates a single, "chained" growth rate that is not biased toward the structure of either year.
2. **Create a Chain Index:** This process is repeated for every pair of consecutive years (2005-2006, 2006-2007, and so on). This creates a chain of annual growth rates that are always based on contemporary price structures.
3. **Anchor to the Reference Year (2005):** Finally, this entire chain of growth rates is anchored to the **reference year**—2005. The actual dollar value of Nominal GDP in 2005 is set as the Real GDP value for that year. The growth rates for all other years are then applied to this 2005 value to create a continuous time series expressed in "2005 dollars."








































