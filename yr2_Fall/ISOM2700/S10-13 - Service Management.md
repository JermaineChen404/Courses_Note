Service management focus on the buffer station in a process (queue).

![[Ust_Note/yr2_Fall/ISOM2700/attachments/Pasted image 20251031025243.png]]


Given random variable $L_{n}$ in queue, $A_{n}$ of arrivals, and $C_{n}$ of capacity,

$$L_{n}=\max(A_{n}+L_{n-1}-C_{n},0)$$

Queues exist due to
- variability of arrival process
	- random input (arrival)
- variability of service time
	- resources breakdown/maintenance

# Queuing Model
![[Ust_Note/yr2_Fall/ISOM2700/attachments/Pasted image 20251031025719.png]]

## M/M/s Model
**Kendall's notation**：

![[Ust_Note/yr2_Fall/ISOM2700/attachments/Pasted image 20251020180503.png]]

Markovian/Markovian/# of servers

Input of the queue
- Exponential inter-arrival time: arrival rate $=\lambda$ (customers/period)
- Exponential service time: service rate *at each server* $=\mu$ (customer/period)
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
![[Ust_Note/yr2_Fall/ISOM2700/attachments/Pasted image 20251020180838.png]]

Server utilization is the average fraction of time a server is busy.

Given the assumption $\lambda<s\mu$,

$$\text{Utilization}=\rho=\frac{\text{Flow Rate}}{\text{Capacity}}=\frac{\lambda}{s\mu}<100\%$$

A queue is stable when $\rho<1$

## Little‘s Law Revisited (1 Server)
Recalling the [[S2&3 - Process Analysis#Little's Law|Little's Law]],

$$\text{Work-in-process inventory}=\text{Flow rate}\times \text{Flow time}$$

In a queue specifically,

$$\text{Average \# in system}=\min(\lambda,\mu)\times \text{Average waiting/service time}$$

![[Ust_Note/yr2_Fall/ISOM2700/attachments/Pasted image 20251020181830.png]]
## Modeling Random Arrivals
### Random Service Time
![[Ust_Note/yr2_Fall/ISOM2700/attachments/Pasted image 20251020182446.png]]
### Random Number of Arrivals
![[Ust_Note/yr2_Fall/ISOM2700/attachments/Pasted image 20251020182538.png]]
### Number vs. Time
Poisson Arrival Process:
- random arrival
- independent of one another
- at the same average rate

A process that has exponentially distributed inter-arrival/service times is, by definition, a **Poisson Process**.

![[Ust_Note/yr2_Fall/ISOM2700/attachments/Pasted image 20251020184206.png]]
![[Ust_Note/yr2_Fall/ISOM2700/attachments/Pasted image 20251020184219.png]]

Let the random variable $T$ represent the inter-arrival time, we state that

$$T\sim \text{Exponential}(\lambda)$$

where $\lambda$ is the average arrival rate. The mean of this distribution is $E[T]=\frac{1}{\lambda}$.

Define a new random variable $N_{t}$ representing the number of arrivals, thus

$$N_{t}\sim \text{Poisson}(\lambda t)$$

## Formulas for M/M/1 Queuing Model
![[Ust_Note/yr2_Fall/ISOM2700/attachments/Pasted image 20251020185437.png]]
![[Ust_Note/yr2_Fall/ISOM2700/attachments/Pasted image 20251020185449.png]]

## Formulas for M/M/s Queuing Model
![[Ust_Note/yr2_Fall/ISOM2700/attachments/Pasted image 20251020185543.png]]

## Values of $L_{q}$
![[Ust_Note/yr2_Fall/ISOM2700/attachments/Pasted image 20251020185617.png]]

## Queuing System Cost Tradeoff
- $C_{w}=$ Cost of waiting per customer per hour
- $L_{q}=$ Mean number of waiting customers
- $C_{s}=$ Cost of service per server per hour
- $S=$ Number of servers

$$\text{Total Cost}=C_{s}S+C_{w}L_{q}$$

![[Ust_Note/yr2_Fall/ISOM2700/attachments/Pasted image 20251020185855.png]]

## Pooling
### Common Queue vs. Separate Queues
![[Ust_Note/yr2_Fall/ISOM2700/attachments/Pasted image 20251031164958.png]]
![[Ust_Note/yr2_Fall/ISOM2700/attachments/Pasted image 20251031165153.png]]

Pooling resources is more efficient:
- Same utilization $\rho$
- Less waiting time in common queue

### Limitations to Pooling
- A longer queue could annoy customers
- Pooling requires well-rounded workers/servers
	- higher training/development cost
- customer-server relationship
	- customers could prefer choosing instead of being assigned a server
## Queuing Model with General Inputs: Monte-Carlo Simulation
![[Ust_Note/yr2_Fall/ISOM2700/attachments/Pasted image 20251031170616.png]]
### Random Variable
![[Ust_Note/yr2_Fall/ISOM2700/attachments/Pasted image 20251020182233.png]]
### Exponential Random Variable
Given $X\sim \text{Exponential}(\mu)$,

$$X=-\frac{1}{\mu}\ln(U)$$

where $U\sim \text{Uniform}(0,1)$. 

The exponential distribution with rate parameter $\mu\geq 0$ has the cumulative distribution function (CDF):

$$F(x)=1-e^{-\mu x}$$

### Identify Relationship
![[Ust_Note/yr2_Fall/ISOM2700/attachments/Pasted image 20251031170507.png]]

### Simulate General Queuing Model
![[Ust_Note/yr2_Fall/ISOM2700/attachments/Pasted image 20251031171019.png]]

![[Ust_Note/yr2_Fall/ISOM2700/attachments/Pasted image 20251031171038.png]]

## Psychology of Waiting
- Unoccupied time feels longer
	- divert customers' attention in queue
- Pre-process waiting feels longer
	- give customers indication that their request has been accepted and the service process has begun
- Unexplained waiting feels longer
	- provide real reasons for keeping customers waiting
- Unfair waiting feels longer
	- ensure a fair waiting system (FCFS)
- Uncertain waiting feels longer
	- inform and even surprise customer with shorter waiting time
- Solo waiting feels longer
	- encourage interaction in the waiting environment


