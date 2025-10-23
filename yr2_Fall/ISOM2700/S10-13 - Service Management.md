Given random variable $L_{n}$ in queue, $A_{n}$ of arrivals, and $C_{n}$ of capacity,
$$L_{n}=\max(A_{n}+L_{n-1}-C_{n},0)$$

Queues exist due to
- variability of arrival process
	- random input (arrival)
- variability of service time
	- resources breakdown/maintenance

# Queuing Model
## M/M/s Model
**Kendall's notation**：

![[Pasted image 20251020180503.png]]

Markovian/Markovian/# of servers

Input of the queue
- Exponential inter-arrival time: arrival rate $=\lambda$
	- customer/period
- Exponential service time: service rate *at each server* $=\mu$
	- customer/period
- Number of servers $=s$
- Assumption:
	- one queue
	- First-come-first-serve
	- $\lambda<s\mu$

Output of the queue (System performance measures)
- Average number of customers in the queue $L_{q}$ or in the system $L$
- Average time spent in the queue $W_{q}$ or in the system $W$
- Probability of delay
- Utilization of the server $\rho$

## Service Utilization $\rho$
![[Pasted image 20251020180838.png]]
Given the assumption $\lambda<s\mu$,
$$\rho=\frac{\lambda}{s\mu}<100\%$$
Server utilization is the average fraction of time a server is busy.

## Little‘s Law Revisited (1 Server)
Recalling the [[S2&3 - Process Analysis#Little's Law|Little's Law]],

![[Pasted image 20251020181830.png]]

## Random Variable
![[Pasted image 20251020182233.png]]
### Random Service Time
![[Pasted image 20251020182446.png]]
### Random Number of Arrivals
![[Pasted image 20251020182538.png]]
### Number vs. Time
A process that has exponentially distributed inter-arrival/service times is, by definition, a **Poisson Process**.

![[Pasted image 20251020184206.png]]
![[Pasted image 20251020184219.png]]

Let the random variable $T$ represent the inter-arrival time, we state that
$$T\sim \text{Exponential}(\lambda)$$
where $\lambda$ is the average arrival rate. The mean of this distribution is $E[T]=\frac{1}{\lambda}$.

Define a new random variable $N_{t}$ representing the number of arrivals, thus
$$N_{t}\sim \text{Poisson}(\lambda t)$$

## Formulas for M/M/1 Queuing Model
![[Pasted image 20251020185437.png]]
![[Pasted image 20251020185449.png]]

## Formulas for M/M/s Queuing Model
![[Pasted image 20251020185543.png]]

## Values of $L_{q}$
![[Pasted image 20251020185617.png]]

## Queuing System Cost Tradeoff
- $C_{w}=$ Cost of waiting per customer per hour
- $L_{q}=$ Mean number of waiting customers
- $C_{s}=$ Cost of service per server per hour
- $S=$ Number of servers
$$\text{Total Cost}=C_{s}S+C_{w}L_{q}$$
![[Pasted image 20251020185855.png]]

## Pooling
Pooling resources is more efficient

### Limitations to Pooling

## Monte-Carlo Simulation

