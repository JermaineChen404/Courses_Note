# Introduction to Risk Management

## Course Overview
This lecture sets the foundation for the course: understanding what risk management is, why it matters, and the basic tools and concepts used to assess and treat risk.

---

## 1. Course Logistics & Teaching Philosophy (pages 1–10)

### 1.1 Class Participation (5%)
- Graded based on:
  - Engagement points via Mentimeter Q&A and in‑class exercises
  - Overall impression (effort and reasoning, not just correct answers)
- To be counted, enter your **HKUST Login ID** as your screen name in Mentimeter.

### 1.2 Desired Outcome (from a recruiter’s perspective)
> *“Teach the big concepts and how to approach problems … interviews test your ability to reason and to learn more than specifics.”*

### 1.3 Teaching Philosophy
- Theory & Application (in‑class exercises, cases, projects)
- Active learning
- Focus on **reasoning** – understand *why* things work, not just *what* works.

---

## 2. The Risk Management Process (pages 11–12)

If you were hired as Chief Risk Officer, the first steps would be:

1. **Determine objectives**
2. **Identify the risks** facing the organization
3. **Assess the risks** (measure them)
4. **Evaluate alternative treatments** and choose the approach that best meets objectives
5. **Implement, monitor, learn, and adjust**

> [!tip] This is the core framework of Enterprise Risk Management (ERM).

---

## 3. Types of Risks (page 14)

| Risk Category | Examples |
|---------------|----------|
| **Financial risks** | Price risk (commodity, FX, interest rate), credit risk, liquidity risk |
| **Operational risks** | Failed internal processes, people, systems; external events (natural disasters, climate, legal liability) |
| **Other** | Damage to assets, worker injury, etc. |

---

## 4. Risk Treatment Tools (pages 15–19)

### 4.1 Possible Tools
- **Risk avoidance** – don’t engage in the activity
- **Risk retention** – accept the risk
- **Risk transfer (hedging)** – use insurance or derivatives
- **Risk reduction** – diversification

### 4.2 Hedging through Insurance (page 17–18)
**Example**: Homeowner’s insurance
- House value: $200K
- Policy: $15K premium, $25K deductible, insurer pays all further damages
- **Cost**: premium
- **Benefit**: protection against large losses

### 4.3 Hedging through Derivatives (page 19)
- Financial contracts (forwards, futures, options, swaps) that transfer risk between parties.

---

## 5. Grading Policy: A Mini Risk Management Exercise (pages 20–24)

**Quiz grading**:
- Two in‑class quizzes (10 pts each)
- Online exercises (8–10 practice questions, max 5 pts)
- Final score for each quiz = max{Quiz score, Exercise score}

**Question**: Which distribution of quiz scores (A or B) gives a higher benefit from doing the exercise?
- If scores are **low**, the exercise can boost many students.
- If scores are **high**, the exercise helps fewer.
- This illustrates how the **benefit of a risk treatment** depends on the underlying distribution.

---

## 6. Two Notions of Risk (page 25)

1. **Risk as expected loss** – “something bad could happen” (higher expected loss)
2. **Risk as uncertainty / unpredictability** – higher variance

**Variance formula**:
$$ \mathrm{Var}(X) = \sum_{i=1}^N p_i (x_i - \mu)^2 $$
where $\mu = E[X]$ is the expected value.

> [!note] Both matter in risk management. Expected loss affects the average outcome; variance affects the likelihood of extreme outcomes.

---

## 7. Risk Reduction through Pooling (pages 26–30)

### 7.1 Individual Risk (Emily or Sam)
- Fire probability: 20%
- Loss if fire: $2500
- Expected loss: $0.2 \times 2500 = 500$
- Standard deviation:
  $$ \sigma = \sqrt{0.8(0-500)^2 + 0.2(2500-500)^2} = 1000 $$

### 7.2 Pooling Arrangement
Two people agree to split any losses equally.

**Possible outcomes**:
- No fire (prob 0.8×0.8 = 0.64): each pays $0
- One fire (prob 2×0.8×0.2 = 0.32): total loss $2500, each pays $1250
- Two fires (prob 0.2×0.2 = 0.04): total loss $5000, each pays $2500

**Expected cost per person**:
$$ \mu = 0.64\times 0 + 0.32\times 1250 + 0.04\times 2500 = 500 $$
**Standard deviation**:
$$ \sigma = \sqrt{0.64(0-500)^2 + 0.32(1250-500)^2 + 0.04(2500-500)^2} = 707 $$

> [!important] Pooling **reduces risk** (standard deviation drops from 1000 to 707) without changing expected loss. This is the essence of diversification.

---

## 8. Law of Large Numbers & Central Limit Theorem (page 31)

For i.i.d. random variables $X_i$ with mean $\mu$ and finite variance $\sigma^2$:

- **Law of Large Numbers (LLN)**: $\bar{X}_N = \frac{1}{N}\sum_{i=1}^N X_i \to \mu$ as $N\to\infty$
- **Central Limit Theorem (CLT)**: The distribution of $\bar{X}_N$ approaches a normal distribution with mean $\mu$ and variance $\sigma^2/N$.

**Application to pooling**:
As the number of independent risks grows, the average loss per person becomes almost certain (variance $\to 0$). This is why insurance works – with many uncorrelated policies, the insurer’s risk per policy is tiny.

> [!quote] "Don’t put all your eggs in one basket."

---

## 9. Pooling with Correlated Losses (pages 33–39)

### 9.1 When Correlation is +1 (perfect positive correlation)
- If one has a fire, the other always does too.
- Pooling does **nothing** to reduce risk – each still faces the same distribution as alone.
- Standard deviation remains 1000.

### 9.2 When Correlation is -1 (perfect negative correlation)
- Fires never happen together; when one has a fire, the other doesn’t.
- With two people, total loss is always $2500 (one fire always occurs if probabilities are 50% each? Let's compute correctly.)

**Exercise (page 37)**:
Assume $p=1/2$ (each has 50% chance of fire) and correlation = -1.
- Outcomes:
  - Fire A only (prob 0.5): loss $2500, each pays $1250
  - Fire B only (prob 0.5): loss $2500, each pays $1250
  - No fire or both fire are impossible (correlation -1 means exactly one occurs).
- Each person’s loss = $1250 **with certainty**.
- Expected loss = $1250, standard deviation = 0.

> [!check] With perfect negative correlation, pooling **eliminates all risk**! This is the ideal diversification.

### 9.3 Real‑world Insurance Markets (page 33)
- Insurers often cancel policies in fire‑prone areas because losses are **positively correlated** (e.g., California wildfires affect many homes simultaneously).
- High correlation limits the benefit of pooling and makes insurance expensive or unavailable.

---

## 10. Application to Portfolio Diversification (pages 40–41)

- Stock returns are **positively correlated** (they move together with the market).
- Diversification reduces **idiosyncratic risk** (firm‑specific) but cannot eliminate **systematic risk** (market risk).
- The remaining risk after holding a well‑diversified portfolio is **systematic risk**.

> [!important] This is the foundation of the Capital Asset Pricing Model (CAPM).

---

## Concept Checklist

- [ ] Understand the five‑step risk management process
- [ ] Distinguish financial, operational, and other risks
- [ ] List risk treatment tools (avoidance, retention, transfer, reduction)
- [ ] Explain the difference between expected loss and variance as risk measures
- [ ] Calculate expected loss and standard deviation for individual and pooled risks
- [ ] Show how pooling reduces risk when losses are uncorrelated
- [ ] Apply LLN and CLT to explain why pooling works
- [ ] Analyze the effect of correlation on diversification benefits
- [ ] Relate diversification to systematic vs. idiosyncratic risk

---

## Key Formulas Summary

| Concept | Formula |
|---------|---------|
| Variance | $\mathrm{Var}(X) = \sum p_i (x_i - \mu)^2$ |
| Expected value | $\mu = \sum p_i x_i$ |
| Pooling (two independent, equal risks) | $\sigma_{\text{pooled}} = \frac{\sigma_{\text{individual}}}{\sqrt{2}}$ (for each person) |
| Law of Large Numbers | $\bar{X}_N \to \mu$ |
| Central Limit Theorem | $\bar{X}_N \approx N(\mu, \sigma^2/N)$ |

