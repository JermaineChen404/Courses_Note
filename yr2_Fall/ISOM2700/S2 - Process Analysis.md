# A Process View
## Definition
> A ==business process== is a network of activities performed by resources that transform inputs into outputs.

> The ==flow unit== is what is tracked through the process and generally defines the process output of interest

![[Pasted image 20250918153002.png]]
## Process Flow Chart
![[Pasted image 20250918152851.png]]

# Process Measures
## Measures of Process Performance
- Flow Time
	- the time spent by a unit of product
	- time worked on + time in buffer
- Process Capacity
	- maximum rate at which output can be created given infinite inputs
	- i.e., the smallest capacity among all activities
- Cycle Time
	- the time between two successive product completions
- Work-in-Process Inventory
	- the number of units staying throughout the process at a given time
## Tool: Gantt Chart
### Example
![[Pasted image 20250918154502.png]]
- Flow time: 10 min
- Process capacity: $\frac{1}{4}=0.25$ unit per min
	- worker B takes the longest time
- cycle time: 4 min
- average work-in-process inventory: $\frac{10}{4}=2.5$ units
#### Tighter Arrangement
![[Pasted image 20250918154928.png]]
> A worse scheduling with higher work-in-process inventory
---
==Gantt chart does not work well for complex process==
# Process Analysis
## Law of the Minimum
Bottleneck: The resource that has the lowest capacity
- determines the capacity of the entire process
- add up all the activities performed by each resource to compare
## Little's Law
$$L=\lambda \times W$$
$$\text{Work-in-process Inventory}=\text{Capacity}\times \text{Flow Time}$$
## Introducing Capacity $\neq$ Demand

