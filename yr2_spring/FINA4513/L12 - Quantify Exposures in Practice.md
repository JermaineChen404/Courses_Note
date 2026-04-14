# Quantifying Exposures in Practice

## Overview
This lecture moves beyond the theoretical idea of exposure to **practical measurement**. It shows that a firm’s exchange‑rate exposure is **not a fixed number**—it depends crucially on the **competitive structure** of the market. Using the example of a UK car exporter (XYZ), the lecture contrasts a perfectly competitive market (where profits are **convex** in the exchange rate) with a monopolistic market (where exposure is smaller and less curved). The lecture also covers **competitive exposure** (exposure to a competitor’s currency), **natural hedges**, and how firms can use **regression analysis** to estimate their exposures.

---

## Part 1: Motivating Example – XYZ Car Exporter

### 1.1 The Setup
- XYZ is a UK car producer that exports part of its production to the U.S.
- Current exchange rate: **1 USD = 0.5 GBP**.
- Tax rate: **25%**.
- The firm’s cash flow statement shows how GBP revenue from U.S. sales depends on the USD/GBP exchange rate.

### 1.2 The Core Question
If the exchange rate is the **only** source of uncertainty, the volatility of XYZ’s cash flow equals:


$$\sigma_{\text{cash flow}} = \text{Exposure} \times \sigma_{\text{exchange rate}}
$$

The lecture asks: **What determines that exposure?**

> [!important] Key Insight
> Exposure is **endogenous**—it depends on how the firm and its competitors react to exchange rate movements. We must model **demand** and **cost** curves.

---

## Part 2: Why Exposure Is Not Constant

### 2.1 The Firm’s Decision Problem
XYZ chooses the quantity of cars to sell in the U.S. to maximize:


$$p_{\text{US}}(q) \times S_t \times q - \text{Cost}(q)$$

where $S_t$ is the exchange rate (USD/GBP). The **functional form** of $p_{\text{US}}(q)$ (the demand curve) is the key determinant of exposure.

### 2.2 Two Polar Cases
- **Case 1:** Fully competitive market – XYZ is a **price‑taker**.
- **Case 2:** XYZ is a **monopolist** in the U.S. market.

> [!tip] Intuition
> In a competitive market, the firm’s quantity adjusts sharply to exchange rate changes. With market power, the firm adjusts **prices** instead of quantities, dampening the exposure.

---

## Part 3: Case 1 – Fully Competitive Market

### 3.1 Assumptions
- U.S. price is fixed at $p_{\text{US}} = 20$ (in USD).
- Cost function in GBP: $C(q) = 10 + \frac{1}{4}q^2$
- Marginal cost: $MC(q) = \frac{1}{2}q$

### 3.2 Optimal Output
The firm equates marginal revenue (in GBP) to marginal cost:

$$
20 \times S_t = \frac{1}{2}q \quad \Rightarrow \quad q(S) = 40S
$$

**Quantity increases linearly with $S$.**

### 3.3 Profit Function
Substitute $q(S)$ back into the profit expression:

$$
\pi(S) = 20S \times (40S) - \left(10 + \frac{1}{4}(40S)^2\right) = 800S^2 - 10 - 400S^2 = 400S^2 - 10
$$

> [!check] Result
> Profit is **convex** (quadratic) in the exchange rate $S$. A depreciation of the dollar (lower $S$) hurts profit, but an appreciation (higher $S$) helps **more than linearly**.

---

## Part 4: Case 2 – XYZ Has No Competitors (Monopoly)

### 4.1 Assumptions
- Demand curve: $p_{\text{US}}(q) = 40 - q$ (price in USD).
- Same cost function as before.

### 4.2 Optimal Output
Maximize $(40 - q) S \times q - \left(10 + \frac{1}{4}q^2\right)$:

$$
S(40 - 2q) = \frac{1}{2}q \quad \Rightarrow \quad q(S) = \frac{80S}{4S + 1}
$$

**Quantity increases nonlinearly and more slowly** than in the competitive case.

### 4.3 Profit Curvature
- The profit function is **less convex** than in the competitive case.
- A depreciation of the dollar leads to a **smaller quantity reduction** but also a **higher USD price**, partially offsetting the impact.

> [!important] Competitive Exposure Matters
> The curvature (convexity) of profits with respect to the exchange rate is **greater in competitive markets** because firms adjust **quantities** rather than **prices**.

---

## Part 5: Competitive Exposure – The Euro Effect

### 5.1 Beyond Your Own Currency
What if XYZ is a small player in a competitive U.S. market **dominated by a German car maker**?
- XYZ’s pricing **follows** the German producer’s USD price.
- If the **Euro appreciates** against the USD, German firms raise their USD prices.
- XYZ, as a price‑taker, can also charge a higher USD price, **increasing its GBP revenue**.

### 5.2 In‑Class Exercise Conclusion
- **Pound appreciates vs. USD:** Adverse effect on XYZ’s GBP income.
- **Euro appreciates vs. USD:** **Good news** for XYZ, even though it does **not** export to Europe.

> [!warning] Hidden Exposure
> A firm can have **indirect exposure** to currencies of its competitors. This is why **competitive exposure** analysis is essential.

---

## Part 6: Additional Real‑World Complications

- **Inflation and Real Exchange Rates:** If U.S. price level rises by 10% and the dollar depreciates by 10%, the **real** exchange rate is unchanged. Exposure should be measured **net of price level changes**.
- **Costs in Foreign Currency:** If XYZ also incurs costs in USD (e.g., U.S. labor or parts), those costs provide a **natural offset** to revenue exposure.

---

## Part 7: Airline Hedging – A Natural Hedge

### 7.1 The Situation
A European airline contracted to pay **several billion USD** for Boeing aircraft. It hedged the USD liability with **forwards**. The dollar subsequently fell ~40%.

### 7.2 The Overlooked Exposure
The airline **forgot** its operating exposure:
- Ticket revenue on transatlantic routes is positively correlated with the USD (many tickets sold in USD).
- When the dollar depreciated, **EUR revenue fell** (demand shifted), while the forward hedge generated a loss on the payable side.

> [!danger] The Lesson
> The Boeing contract was a **natural hedge** for the airline’s USD‑denominated revenue. **Hedging only the payable side doubled the firm’s USD exposure instead of reducing it.**

---

## Part 8: A Firm‑Wide Approach

- Risk management should be done at the **enterprise level**.
- Analyze how **each factor** affects firm value:
    - **Direction:** Does it increase or decrease value?
    - **Correlations:** How do factors move together?
- This holistic view prevents situations like the airline’s where one division’s hedge creates risk for another.

---

## Part 9: Regression Analysis to Measure Exposures

### 9.1 The Method
Estimate a stock’s exposure to multiple risk factors using a regression:

$$
R_{\text{GM},t} = \alpha + \beta R_{m,t} + \gamma S_{\text{euro},t} + \delta S_{\text{yen},t} + \lambda R_{B,t} + \varepsilon_t
$$
- $R_{\text{GM},t}$: Return on General Motors stock.
- $R_{m,t}$: Market return.
- $S_{\text{euro},t}, S_{\text{yen},t}$: Exchange rate changes.
- $R_{B,t}$: Return on a bond index.

### 9.2 Limitations
- **Backward‑looking:** Past relationships may not hold if competition changes.
- **Omitted risks:** Low $R^2$ suggests other important factors are missing.
- **Linearity assumption:** Good only for small changes; real exposures can be nonlinear.

---

## Summary

| Concept | Key Result |
|--------|------------|
| Exposure volatility | $\sigma_{\text{CF}} = \text{Exposure} \times \sigma_S$ |
| Competitive market profit | Convex in $S$: $\pi(S) = 400S^2 - 10$ |
| Monopoly profit | Less convex; price adjustment dampens quantity response |
| Competitor currency exposure | Firm can be exposed to currencies it never invoices in |
| Natural hedge | Operating cash flows may offset contractual exposures |
| Regression approach | $R_{\text{firm}} = \alpha + \beta R_m + \sum \gamma_i \Delta S_i$ |

---

## Concept Checklist

- [ ] Explain why exposure depends on market structure.
- [ ] Derive optimal output and profit for a price‑taking exporter.
- [ ] Contrast the convexity of profits under perfect competition vs. monopoly.
- [ ] Describe how a firm can be exposed to a competitor’s currency.
- [ ] Identify the mistake in the airline hedging example.
- [ ] State the advantages and limitations of regression‑based exposure measurement.

---

## Quick Exam Traps

> [!warning] Trap
> Exposure is **not** simply the face value of foreign currency revenue. It is the **sensitivity** of firm value to the exchange rate, which depends on competitive behavior.

> [!warning] Trap
> A natural hedge means the firm’s **operating cash flows** already offset a financial exposure. **Hedging only one side** can inadvertently increase risk.

> [!warning] Trap
> Regression beta coefficients assume a **linear** relationship. For large exchange rate moves or in competitive markets, exposure may be **convex** and not captured by a single beta.

---
