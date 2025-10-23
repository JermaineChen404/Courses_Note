determine the production capacity to meet uncertain demand
# Decision Tree Method
![[Pasted image 20251009145929.png]]
## Value of Perfect Information
![[Pasted image 20251009150339.png]]
![[Pasted image 20251009150349.png]]

# Linear Programming Method
Both the objective function and the constraints are linear with respect to decision variables

![[Pasted image 20251009154631.png]]

![[Pasted image 20251009154614.png]]

Necessary conditions for linear function:
- $f(x+y)=f(x)+f(y)$
- $f(cx)=cf(x)$

A linear constraint requires that the expressions involved are linear functions

## Graphical Method
for 2 variable only

![[Pasted image 20251009160813.png]]
- draw the feasible region by the constraints
	- $k_{1}x+k_{2}y\leq C$
		- $y\leq -\frac{k_{1}}{k_{2}}x+\frac{C}{k_{2}}$
- Shift the iso-profit line upwards for maximization
	- $Z=k_{1}x+k_{2}y$
		- $y= -\frac{k_{1}}{k_{2}}x+\frac{Z}{k_{2}}$
		- Therefore, the Z is maximized when the line reach the largest y-intercept

Binding constraints:
- $LHS=RHS$
- $Slack=0$
- limit the improvement in the objective function
- e.g., constraint 1 and 2

Non-binding constraints
- $LHS<RHS$
- $Slack>0$
- do not limit improvement
- e.g., constraint 3

Idle time: any period when a resource is ready but is not being productive
- represent a cost without generating any output
- non-binding constraints have idle time
	- e.g., constraint 3 has 50 min of idle time ($B_{\text{constraint 3}}-B_{\text{optimal}}$)


Shadow price: the **change in the optimal value of the objective function** (e.g., total profit or cost) resulting from a **one-unit increase** in the right-hand side (RHS) of a constraint.

$S_{i}$ : slack variable
$SP_{i}$ : shadow price

有 slack 必无 shadow price
$$S_{i}>0\text{ (non-binding)}\Rightarrow SP_{i}=0$$
根据逆否命题与原命题等价，有 shadow price 必无 slack
$$SP_{i}>0\Rightarrow S_{i}=0\text{ (binding)}$$
==But The opposites do not hold==

![[Pasted image 20251009230759.png]]
## Solving LP with Excel Solver
1. Construct a spreadsheet as below

![[Pasted image 20251009220836.png]]

2. Specify solver parameter

![[Recording 2025-10-09 222439.mp4]]

3. Interpret the reports

### Answer Report

![[Pasted image 20251009223146.png]]

## Sensitivity Analysis
How will the optimal objective value change if the right hand side (RHS) of some constraint changes?
### Sensitivity Report

![[Pasted image 20251009223234.png]]

|Column|Interpretation|
|---|---|
|**Final Value**|Optimal solution|
|**Reduced Cost**|**How much the objective coefficient must improve before the variable becomes positive**|
|**Objective Coefficient**|Original profit/unit or cost/unit|
|**Allowable Increase**|Maximum amount you can **increase** the coefficient without changing the optimal solution|
|**Allowable Decrease**|Maximum amount you can **decrease** the coefficient without changing the optimal solution|

### Changes in Right-Hand Side
$$\Delta \text{Optimal Objective}=\Delta RHS \times \text{Shadow Price}$$
where $\Delta \text{RHS}\leq\text{allowable changes}$.

It is a changes in the feasible region.

### Changes in Objective Coefficients
$$\Delta \text{Optimal Objective}=0$$
as long as $\Delta \text{coefficient}\leq \text{allowable changes}$

It is a changes in the slope of the maximized iso-profit line.

![[Pasted image 20251009230021.png]]