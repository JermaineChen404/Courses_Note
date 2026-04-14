# Simulation Approach

## Overview
This lecture introduces two major simulation-based methods for risk measurement and valuation:

- **Historical Simulation**
- **Monte Carlo Simulation**

It explains why simulation methods are useful for **VaR**, especially when the **parametric VaR approach** performs poorly for nonlinear portfolios, fat tails, or unstable correlations. The lecture also connects Monte Carlo simulation to **option pricing** and to generating **correlated multivariate scenarios**.

---

## Part 1: Why Move Beyond Parametric VaR?

### 1.1 Limitations of the Parametric VaR Approach
The parametric VaR approach has several important weaknesses:

- It gives a **poor description of nonlinear risks**
- It gives a **poor description of extreme tail events**
- It typically assumes risk factors are **Normally distributed**
- It relies on a **covariance matrix**, which assumes correlations are stable over time

In reality:
- Risk-factor distributions often have **high kurtosis**
- Extreme events happen more often than the Normal model predicts
- Correlations may shift during stress periods

> [!warning] Core Limitation
> Parametric VaR is computationally efficient, but it can miss exactly the kinds of risks that matter most in crises: **nonlinearity**, **fat tails**, and **changing dependence**.

---

## Part 2: Historical Simulation

### 2.1 Main Idea
Historical simulation is the most conceptually straightforward VaR technique.

Approach:
- Collect historical data on daily movements in all market variables
- Treat each historical day as a possible scenario for tomorrow
- Revalue the portfolio under each scenario
- Rank resulting profits/losses
- Read VaR from the tail of the empirical loss distribution

### 2.2 How Scenarios Are Created
Suppose today is day `n` and we have `n` days of historical data.

Let `v_i` be the value of a market variable on day `i`.

Then the `i`th historical trial assumes tomorrow’s value is:

If **percentage changes** are matched:
$$
v_n \frac{v_i}{v_{i-1}}
$$

If **actual changes** are matched:
$$
v_n + v_i - v_{i-1}
$$

> [!note] Which Change Measure?
> For variables like **interest rates**, **credit spreads**, and sometimes **volatilities**, we usually use **actual changes** rather than percentage changes.

### 2.3 Portfolio Example
The lecture uses a portfolio on **July 8, 2020** invested across four stock indices:

- **S&P 500**: 4,000 ($000s)
- **FTSE 100**: 3,000 ($000s)
- **CAC 40**: 1,000 ($000s)
- **Nikkei 225**: 2,000 ($000s)

Total portfolio value:
$$
10{,}000 \text{ ($000s)}
$$

Historical index data are then used to generate 500 scenarios for the next day.

### 2.4 Scenario Revaluation
For each historical day:
- Apply the observed historical market move to the current portfolio
- Compute the simulated portfolio value
- Convert the result into a loss number

This produces an empirical distribution of profits/losses.

### 2.5 Reading VaR from Ranked Losses
The lecture ranks losses from worst to best.

For **500 scenarios**, the one-day **99% VaR** corresponds roughly to the **5th worst loss** because:

$$
500 \times 0.01 = 5
$$

The lecture reports:
- One-day **99% VaR = 422.291** ($000s)

> [!check] Historical VaR Logic
> Historical simulation does **not** fit a theoretical distribution.  
> It simply uses the observed historical scenario losses and reads the tail empirically.

---

## Part 3: Correlation Assumption in Historical Simulation

### 3.1 What Is Assumed?
A key in-class question asks: *What is the assumption on the correlation?*

The answer is effectively:
$$
\text{correlation is whatever occurred historically}
$$

Historical simulation does **not** separately estimate volatility and correlation. Instead:
- dependence is embedded in the observed historical joint realizations

### 3.2 Interpretation
This means:
- You do **not** assume zero correlation
- You do **not** assume independence
- You inherit the historical co-movements directly from the data

> [!important] Dependence Structure
> Historical simulation captures correlations through the **actual historical joint outcomes**, not through a separately estimated covariance matrix.

---

## Part 4: Pros and Cons of Historical Simulation

### 4.1 Pros
Historical simulation has several strengths:

- No need to assume a specific distribution for risk factors
- Can capture **fat tails** and **extreme events** if they are present in the data
- No need to estimate volatilities and correlations separately
- Very intuitive conceptually

### 4.2 Cons
However, it also has important drawbacks:

- Complete dependence on a particular historical dataset
- **Window effect**: if a crisis leaves the sample window, measured VaR can drop sharply
- Cannot easily accommodate structural change in the future
- Short samples may lead to biased or imprecise VaR estimates
- May be computationally inefficient for complex portfolios

> [!danger] Historical Data Dependence
> Historical simulation assumes the past is a useful guide to the future.  
> If the future differs structurally from the sample period, the method can be misleading.

---

## Part 5: Monte Carlo Simulation

### 5.1 Main Idea
Monte Carlo simulation predicts the distribution of outcomes by generating a large number of random scenarios from an assumed model.

General idea:
- Specify the risk factors
- Assume a probability distribution for them
- Generate many simulated scenarios
- Revalue the portfolio under each scenario
- Use the simulated payoff/loss distribution for pricing, VaR, or decision analysis

### 5.2 Key Difference from Historical Simulation
Historical simulation uses **real past observations**.

Monte Carlo simulation uses:
- an **assumed probabilistic model**
- **randomly generated scenarios**

> [!tip] Big Picture
> Historical simulation replays the past.  
> Monte Carlo simulation imagines many possible futures.

---

## Part 6: Monte Carlo for Option Pricing

### 6.1 Example Setup
The lecture reviews a European call option with:

- Strike:
$$
K = 101
$$
- Maturity:
$$
T = 150 \text{ days}
$$
- Current stock price:
$$
S_0 = 96
$$
- Volatility:
$$
\sigma = 0.03
$$
- Risk-free rate per period:
$$
r_f = 0.00396\%
$$

The lecture simulates:
$$
N = 1{,}000
$$
paths of stock prices.

### 6.2 Simulating Stock Prices under BSM
The stock evolves according to the Black-Scholes-Merton dynamics in discrete form:

$$
S_{t+1} = e^{\ln(S_t) + \left(r_f - \frac{\sigma^2}{2}\right) + \sigma z}
$$

where:
- `z` is a standard Normal random shock
- one realization of `z` is generated for each step

To simulate one path:
1. Generate `T=150` random shocks
2. Recursively compute prices from `S_0` to `S_{150}`

### 6.3 Option Payoff
At maturity, the European call payoff is:

$$
\max(S_T - K, 0)
$$

Many simulated paths finish below strike, giving zero payoff.

### 6.4 Monte Carlo Price
The call price is estimated as the discounted average payoff:

$$
c = e^{-r_f T}\frac{1}{N}\sum_{i=1}^{N}\max(S_T^{(i)} - K,0)
$$

In the lecture’s simulation:
- Simulated call price ≈ **12.86**
- Theoretical BSM price ≈ **12.22**

> [!note] Simulation Error
> Monte Carlo prices vary from run to run because they depend on random draws.  
> With more simulations, the estimate usually becomes more stable.

---

## Part 7: When Monte Carlo Is Useful

### 7.1 Why Use Monte Carlo If We Already Have BSM?
For plain vanilla European options, BSM often gives a closed-form solution.

Monte Carlo becomes especially useful when:
- pricing **complex derivatives**
- dealing with **nonlinear payoffs**
- handling **many interacting risk factors**
- closed-form formulas are unavailable or inconvenient

Examples include:
- exotic options
- structured products
- path-dependent claims
- portfolios where full revaluation matters

> [!important] Why Monte Carlo Matters
> Monte Carlo is powerful when analytic pricing formulas do not exist, or when the portfolio is too complex for simple approximations.

---

## Part 8: Monte Carlo Simulation for VaR

### 8.1 Basic Setup
For Monte Carlo VaR:
- Assume a known distribution for the risk factors
- A common implementation assumes a **stable joint-Normal distribution**
- Use a **full nonlinear pricing model** to value the portfolio in each scenario

For option portfolios, this means:
- using pricing formulas such as **Black-Scholes**
- rather than relying only on linear approximations or Greeks

### 8.2 Procedure
The lecture’s procedure is:

1. Specify all relevant risk factors
2. Construct scenarios using random numbers
3. Value the portfolio under each scenario
4. Repeat many times
5. Use the resulting profit/loss distribution to compute VaR or other risk measures

### 8.3 Output
Once simulation is complete, you can study:
- expected profit
- VaR
- expected shortfall
- other risk statistics
- broader decision-making questions

---

## Part 9: Pros and Cons of Monte Carlo Simulation

### 9.1 Pros
Monte Carlo simulation has several major advantages:

- Uses **full pricing models**, so it captures **nonlinearities**
- Can generate an effectively unlimited number of future scenarios
- Is highly flexible
- Can accommodate distributions with:
	- fat tails
	- jumps
	- non-Normal behavior
- Makes sensitivity analysis easier

### 9.2 Cons
Main disadvantages:

- Can be **very slow**
- Monte Carlo VaR may take much longer than parametric VaR
- Typically requires assumptions about the underlying distribution
- Model risk matters: wrong assumptions lead to wrong results

> [!warning] Tradeoff
> Monte Carlo is flexible and powerful, but computationally intensive and only as good as the assumptions used to generate scenarios.

---

## Part 10: Simulating Any Known Distribution

### 10.1 Inverse Transform Method
The lecture explains a general technique for simulating from any distribution with CDF `F`.

If:
$$
U \sim \text{Uniform}(0,1)
$$

and we define:
$$
X = F^{-1}(U)
$$

then `X` has CDF `F`.

### 10.2 Why It Works
Because:
$$
\Pr(X \le x) = \Pr(F^{-1}(U) \le x) = \Pr(U \le F(x)) = F(x)
$$

### 10.3 Practical Steps
1. Generate a Uniform random variable
2. Apply the inverse CDF
3. Obtain a sample from the desired distribution

> [!tip] Core Simulation Trick
> Uniform random numbers are the raw material; the inverse CDF transforms them into draws from the target distribution.

---

## Part 11: Simulating Correlated Risk Factors

### 11.1 Goal
When multiple risk factors matter, we need to create simulated scenarios with the desired correlation structure.

Example motivation:
- interest rates and exchange rates may be correlated
- the lecture revisits a foreign-currency bond example with correlation:
$$
\rho = -0.6
$$

### 11.2 Two-Factor Construction
Start with two independent standard Normal draws:

$$
z_1, z_2 \sim N(0,1)
$$

Then define:
$$
\epsilon_1 = z_1
$$

$$
\epsilon_2 = \rho z_1 + z_2\sqrt{1-\rho^2}
$$

This ensures that:
$$
\text{Corr}(\epsilon_1,\epsilon_2)=\rho
$$

### 11.3 Interpretation
The lecture explains the intuition as:
- part of the second factor is driven by the first factor
- the rest is independent noise

> [!check] Correlation Construction
> This is the basic building block for simulating from a **multivariate Normal** distribution.

---

## Part 12: Bond Example Revisited

### 12.1 Foreign-Currency Bond Setup
The lecture revisits a U.S. bank holding a UK bond.

Key parameters shown include:
- Cash flow:
$$
C_p = 100 \text{ pounds}
$$
- Maturity:
$$
t = 5 \text{ years}
$$
- Interest rate:
$$
r_p = 6\%
$$
- Interest-rate standard deviation:
$$
\sigma_r = 0.5\%
$$
- Exchange rate:
$$
FX = 1.6 \text{ dollars/pound}
$$
- FX standard deviation:
$$
\sigma_{FX} = 0.02 \text{ dollars/pound}
$$
- Correlation:
$$
\rho_{r,FX} = -0.6
$$

### 12.2 Linear Approximation Reminder
The lecture recalls the foreign-currency bond value:

$$
PV_\$ = FX \frac{C_p}{(1+r_p)^t}
$$

and the approximation:

$$
\Delta PV_\$ = \delta_{FX}\Delta FX + \delta_{r_p}\Delta r_p
$$

with risk estimated from the variances and correlation of `\Delta FX` and `\Delta r_p`.

### 12.3 Why Simulation Helps
Simulation extends this framework by allowing:
- full scenario generation
- richer distributional assumptions
- potentially nonlinear pricing

---

## Part 13: VaR Under Simulation

### 13.1 How to Compute 1-Day 99% VaR
The simulation-based recipe is:

1. Generate many one-day scenarios for all relevant risk factors
2. Revalue the portfolio under each scenario
3. Compute simulated profits/losses
4. Rank losses from worst to best
5. Take the **99th percentile loss** as 1-day 99% VaR

### 13.2 How Is This Different from Before?
Compared with earlier approaches:

- **Parametric VaR**:
	- uses formulas based on volatility/correlation assumptions
	- usually relies on linearity or Normality

- **Historical Simulation**:
	- uses actual historical scenarios only

- **Monte Carlo VaR**:
	- generates artificial scenarios from a chosen model
	- can accommodate more complexity and more scenarios

---

## Part 14: Comparison Across Methods

### 14.1 Parametric Approach
Strengths:
- fast
- computationally simple

Weaknesses:
- poor for nonlinearity
- poor for non-Normality

### 14.2 Historical Simulation
Strengths:
- captures actual historical dependence
- no explicit distributional assumption

Weaknesses:
- dependent on sample window
- cannot create brand new scenarios

### 14.3 Monte Carlo Simulation
Strengths:
- captures nonlinearity
- flexible
- can generate many scenarios

Weaknesses:
- computationally intensive
- requires model assumptions

> [!important] Summary Comparison
> - **Parametric VaR** is the fastest
> - **Historical simulation** is the most direct and data-driven
> - **Monte Carlo simulation** is the most flexible

---

## Summary

| Method | Main Strength | Main Weakness |
|--------|---------------|---------------|
| Parametric VaR | Fast and efficient | Misses nonlinearity and tail risk |
| Historical Simulation | No distributional assumption | Fully dependent on historical sample |
| Monte Carlo Simulation | Flexible, handles complex portfolios | Slow and model-dependent |

---

## Concept Checklist

- [ ] Explain why parametric VaR can fail for nonlinear and fat-tailed risks
- [ ] Describe how historical simulation constructs scenarios
- [ ] Distinguish percentage-change vs actual-change matching
- [ ] Read VaR from ranked historical losses
- [ ] Explain how correlation is handled in historical simulation
- [ ] List pros and cons of historical simulation
- [ ] Explain the idea of Monte Carlo simulation
- [ ] Simulate option payoffs using many stock-price paths
- [ ] Use discounted expected payoff to price an option
- [ ] Explain when Monte Carlo is preferred to closed-form pricing
- [ ] Describe Monte Carlo VaR procedure
- [ ] Simulate any known distribution using inverse CDF
- [ ] Generate correlated Normal shocks
- [ ] Compare parametric, historical, and Monte Carlo approaches

---

## Key Formulas Summary

| Concept | Formula |
|---------|---------|
| Historical scenario using percentage change | $$v_n \frac{v_i}{v_{i-1}}$$ |
| Historical scenario using actual change | $$v_n + v_i - v_{i-1}$$ |
| European call payoff | $$\max(S_T-K,0)$$ |
| Monte Carlo option price | $$c=e^{-r_fT}\frac{1}{N}\sum_{i=1}^N \max(S_T^{(i)}-K,0)$$ |
| Simulated stock evolution | $$S_{t+1}=e^{\ln(S_t)+\left(r_f-\frac{\sigma^2}{2}\right)+\sigma z}$$ |
| Inverse transform sampling | $$X=F^{-1}(U), \quad U\sim \text{Uniform}(0,1)$$ |
| Correlated Normal draws | $$\epsilon_1=z_1,\quad \epsilon_2=\rho z_1+z_2\sqrt{1-\rho^2}$$ |
| Foreign bond value | $$PV_\$ = FX \frac{C_p}{(1+r_p)^t}$$ |
| Delta approximation | $$\Delta PV_\$ = \delta_{FX}\Delta FX + \delta_{r_p}\Delta r_p$$ |

---

## Quick Exam Traps

> [!warning] Common Trap
> Historical simulation does **not** assume zero correlation or independence. It uses the **historical joint realizations** directly.

> [!warning] Common Trap
> Monte Carlo simulation is not automatically “better” than historical simulation. It is more flexible, but it also depends on modeling assumptions.

> [!warning] Common Trap
> For historical simulation, VaR is read from the **empirical ranked losses**, not from a Normal quantile formula.

> [!warning] Common Trap
> Monte Carlo option prices may differ from theoretical values in small samples because of **simulation noise**.

---