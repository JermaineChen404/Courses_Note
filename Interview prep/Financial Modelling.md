

# Financial Modelling: A Practical Guide for Interview Preparation

> *Focused on logic, intuition, and the "why" behind each step — not just the math.*

---

## I. Discounted Cash Flow (DCF) Analysis

### The Core Idea

A DCF answers one fundamental question: **"What is this business worth based on the cash it will generate in the future?"**

The intuition is simple: a dollar today is worth more than a dollar tomorrow (time value of money). So we forecast all the cash a company will generate, then "discount" those future cash flows back to today's value.

### Walk-Through: Step by Step

---

#### Step 1: Project Free Cash Flow (FCF) — Typically 5–10 Years

**Motivation:** You need an explicit forecast of how much cash the business produces *after* reinvesting to sustain/grow operations.

**The Build (Unlevered Free Cash Flow):**

```
  Revenue
- Cost of Goods Sold
- Operating Expenses
──────────────────────
= EBIT (Operating Income)
- Taxes on EBIT              ← Use the MARGINAL tax rate, not the effective rate
──────────────────────
= NOPAT (Net Operating Profit After Tax)
+ Depreciation & Amortization ← Non-cash charge; add it back
- Capital Expenditures (CapEx) ← Cash spent to maintain/grow assets
- Change in Net Working Capital (NWC) ← Cash tied up in operations
──────────────────────
= Unlevered Free Cash Flow (UFCF)
```

**Why "Unlevered"?**
We strip out the impact of debt (interest, debt repayment) because we want to value the *entire enterprise* — the business itself — independent of how it's financed. The capital structure is handled separately in the discount rate (WACC). This is one of the most common conceptual interview traps.

**Key Details & Pitfalls:**

| Item | What to Watch |
|---|---|
| **Revenue growth** | Don't use overly aggressive assumptions. Interviewers will push back. Anchor to historical growth, industry trends, and management guidance. |
| **Margins** | Should they expand, contract, or stay flat? Have a thesis. |
| **D&A vs. CapEx** | In steady state, D&A ≈ CapEx. If CapEx >> D&A, the company is investing heavily. If D&A >> CapEx, the company is under-investing — a red flag. |
| **Change in NWC** | An *increase* in NWC is a *use* of cash (you're tying up money in inventory/receivables). This is counter-intuitive and a common error source. Think of it as: "I sold the product but haven't collected the cash yet." |
| **Tax rate** | Use the marginal rate on EBIT, not the company's effective rate (which includes interest tax shields already). |

---

#### Step 2: Calculate the Discount Rate (WACC)

**Motivation:** Since we're valuing unlevered cash flows (belonging to *all* capital providers — debt and equity), we need a blended rate that reflects the cost of *all* sources of capital: **Weighted Average Cost of Capital (WACC).**

```
WACC = (E/V) × Re + (D/V) × Rd × (1 - Tax Rate)

Where:
  E = Market value of equity
  D = Market value of debt
  V = E + D
  Re = Cost of equity (from CAPM)
  Rd = Cost of debt (pre-tax)
```

**Cost of Equity — CAPM:**

```
Re = Risk-Free Rate + Beta × Equity Risk Premium (ERP)
```

| Component | Intuition | Practical Detail |
|---|---|---|
| **Risk-Free Rate** | What you'd earn with zero risk | Use the 10-year government bond yield matching your cash flow currency |
| **Beta** | How much does this stock move with the market? | Use comparable company betas; unlever them, take the median, then re-lever to target capital structure. Raw Bloomberg betas are noisy. |
| **ERP** | Extra return investors demand for holding stocks over risk-free bonds | Typically 5–7%; use Duff & Phelps or Damodaran's estimate. Don't make one up. |

**Why (1 - Tax Rate) on debt?**
Interest is tax-deductible, so debt is effectively cheaper than its stated rate. The tax shield is captured here.

**Common Pitfall:** Using book value of equity instead of market value. Always use market cap for E.

---

#### Step 3: Calculate Terminal Value (TV)

**Motivation:** You can't forecast cash flows forever. Terminal value captures everything *beyond* the explicit forecast period. It typically represents **60–80%+ of total DCF value** — which is both its importance and its weakness.

**Two Methods:**

**A. Gordon Growth Model (Perpetuity Growth Method) — More Common in Interviews**

```
TV = Final Year FCF × (1 + g) / (WACC - g)
```

- **g = terminal growth rate**, usually **2–3%** (roughly in line with long-term GDP/inflation)
- **Why?** No company can grow faster than the economy forever. If you use g > GDP growth, you're implying the company eventually *becomes* the entire economy.
- **Sanity check:** If WACC = 10% and g = 3%, the implied exit multiple is 1/(10%−3%) ≈ 14.3× — does that make sense for this business?

**B. Exit Multiple Method**

```
TV = Final Year EBITDA × Exit EV/EBITDA Multiple
```

- Use a multiple derived from comparable companies
- **Advantage:** market-grounded, practical
- **Disadvantage:** introduces relative valuation into what's supposed to be an intrinsic analysis (somewhat circular)

**Interview Tip:** Be prepared to explain why you'd use one vs. the other. Best practice is to use *both* and cross-check. The Gordon Growth method is more "theoretically pure"; the exit multiple is more "practically defensible."

---

#### Step 4: Discount Everything Back to Today

```
Enterprise Value = Σ [ UFCFt / (1 + WACC)^t ] + [ TV / (1 + WACC)^n ]
```

**Key Detail:** Use **mid-year convention** unless told otherwise. Cash flows arrive throughout the year, not in a lump sum on Dec 31st. Without mid-year convention, you *undervalue* the company by half a year's discounting. In practice, this means using exponents of 0.5, 1.5, 2.5… instead of 1, 2, 3…

---

#### Step 5: Bridge from Enterprise Value → Equity Value → Share Price

This is the **"Enterprise Value bridge"** — one of the most frequently tested concepts:

```
Enterprise Value (what the whole business is worth)
- Net Debt (Total Debt - Cash & Cash Equivalents)
- Minority Interest
- Preferred Stock
+ Equity Investments / Associates (if excluded from FCF)
──────────────────────
= Equity Value

Equity Value / Diluted Shares Outstanding = Implied Share Price
```

**The Intuition:** Enterprise Value is what you'd pay to buy the *whole* business. But as an equity buyer, you also *assume* the debt and you *receive* the cash sitting on the balance sheet. So you subtract debt, add back cash.

**Common Pitfalls:**
- Forgetting to use **diluted** shares (include in-the-money options via Treasury Stock Method)
- Missing **off-balance-sheet obligations** (operating leases under old standards, pension liabilities)
- Not subtracting **minority interest** (you included their earnings in your FCF, but you don't own them)

---

#### Step 6: Sensitivity Analysis

**Motivation:** A DCF is only as good as its assumptions. You *must* show how the valuation changes when key inputs change.

**Standard sensitivities to present:**
- **WACC vs. Terminal Growth Rate** → Show a 2D table
- **Revenue Growth vs. EBITDA Margin**
- Present a **range of values**, not a single point estimate

**Interview Insight:** When asked "What's the biggest weakness of a DCF?", the answer is: *it's highly sensitive to terminal value assumptions (growth rate and discount rate), which are inherently uncertain.* This is why you always present a range.

---

## II. Leveraged Buyout (LBO) Analysis

### The Core Idea

An LBO answers: **"What can a financial sponsor (PE firm) afford to pay for this business, given a target return (IRR), using primarily debt financing?"**

Think of it like buying a house: you put down 20–40% equity and borrow the rest. You use the house's "income" (rent / cash flow) to pay down the mortgage. When you sell, you keep the upside.

---

### Walk-Through: Step by Step

#### Step 1: Determine the Purchase Price (Entry)

- Start with an assumed **Entry Multiple** (e.g., 8× LTM EBITDA → Enterprise Value)
- Apply the **EV bridge** in reverse to get the equity check the sponsor writes

**Why EBITDA?** It's the standard proxy for cash-generating ability, comparable across companies, and what lenders underwrite against.

---

#### Step 2: Build the Sources & Uses Table

This is the "where does the money come from, where does it go" table:

```
SOURCES                         USES
─────────────────                ─────────────────
Revolving Credit Facility        Enterprise Value (Purchase Price)
Term Loan A / B                  Financing Fees
Senior Notes / Bonds             Transaction Fees (Advisory, Legal)
Mezzanine / Subordinated Debt    Refinancing of Existing Debt
Sponsor Equity
Management Rollover Equity
─────────────────                ─────────────────
Total Sources = Total Uses       ← MUST balance
```

**Debt Tranches — Key Hierarchy:**

| Tranche | Cost | Risk (to Lender) | Typical Sizing |
|---|---|---|---|
| Revolver | Lowest (L + 150-250bp) | Lowest — first claim | 0–1× EBITDA |
| Term Loan | Low-Mid (L + 200-350bp) | Low — senior secured | 2–4× EBITDA |
| Senior Notes | Mid (5–8%) | Moderate — senior unsecured | 1–2× EBITDA |
| Mezzanine / Sub Debt | Highest (10–14%) | Highest — last debt claim | 0.5–1.5× EBITDA |

**Total leverage typically 4–6× EBITDA.** Key constraint: lenders look at **Debt/EBITDA** and **Interest Coverage (EBITDA/Interest).**

---

#### Step 3: Project Cash Flows & Debt Paydown

**The Central Mechanic of an LBO:** Free cash flow is used to pay down debt — this is the "delevering" that creates equity value.

```
EBITDA
- Cash Interest Expense
- Cash Taxes
- CapEx
- Change in NWC
──────────────────
= Free Cash Flow Available for Debt Repayment
```

**Key Differences from DCF:**
- Here you use **levered** cash flow (after interest) because you care about what's left for the equity sponsor
- You model each debt tranche separately — mandatory amortization on term loans, optional "cash sweep" on remaining FCF
- You must track the **debt schedule** year by year: beginning balance → repayment → ending balance

**What Makes a Good LBO Candidate?**
- Stable, predictable cash flows (to service debt)
- Low CapEx requirements (maximizes FCF for debt paydown)
- Strong market position / defensible business (downside protection)
- Opportunities for operational improvement (margin expansion)
- Potential to acquire add-on businesses ("buy & build")
- Non-cyclical industry (lenders need confidence in repayment)

---

#### Step 4: Determine the Exit & Calculate Returns

**Exit Assumptions:**
- Hold period: typically **5 years** (standard assumption)
- Exit multiple: often = entry multiple (conservative) or with a thesis for expansion/contraction
- Exit Enterprise Value = Exit Year EBITDA × Exit Multiple

**Returns Calculation:**

```
Exit Enterprise Value
- Net Debt Remaining at Exit
──────────────────
= Exit Equity Value

IRR = the rate that solves:
  Equity Invested × (1 + IRR)^n = Exit Equity Value

MOIC (Multiple of Invested Capital) = Exit Equity / Entry Equity
```

**Target Returns:** PE firms typically target **20–25%+ IRR** and **2.0–3.0×+ MOIC.**

---

#### The Three Value Creation Levers in an LBO

This is one of the most important conceptual interview questions:

| Lever | Mechanism | Example |
|---|---|---|
| **1. Debt Paydown (Delevering)** | FCF used to reduce debt; equity grows as the "mortgage" shrinks | Pay down $200M of debt over 5 years → equity value grows by $200M |
| **2. EBITDA Growth** | Revenue growth + margin expansion → larger earnings base at exit | Grow EBITDA from $100M to $150M → 50% more enterprise value at exit |
| **3. Multiple Expansion** | Exit at a higher multiple than entry | Buy at 8×, sell at 10× → 25% more enterprise value at exit |

**Interview Nuance:** Sponsors should *never* rely on multiple expansion alone. That's speculative. The best LBOs are driven by delevering and operational improvement. Multiple expansion is "nice to have."

---

## III. Comparable Company Analysis ("Comps" / Trading Comps)

### The Core Idea

Comps answers: **"What is this company worth based on how similar companies are valued by the market right now?"**

It's relative valuation: if Company A is nearly identical to Company B and trades at 10× EBITDA, then Company A should trade at roughly 10× EBITDA too.

---

### Walk-Through: Step by Step

#### Step 1: Select the Peer Universe

**This is the most judgment-intensive step — and where most errors occur.**

Selection criteria (prioritize in this order):
1. **Industry / Sub-sector** — Same business model and end market
2. **Size** — Similar revenue / market cap range (valuation multiples correlate with scale)
3. **Growth Profile** — Similar growth rates (high-growth companies trade at higher multiples)
4. **Margin Profile** — Similar profitability
5. **Geography** — Same markets / regulatory environment
6. **Capital Structure** — Similar leverage (relevant for equity multiples)

**Interview Tip:** "I'd start with companies in the same sub-industry with similar size, growth, and margin profiles. I'd aim for 5–10 true comparables rather than 30 loosely related names — precision matters more than quantity."

**Common Error:** Including companies that are in the same sector but fundamentally different businesses (e.g., comparing a SaaS company to a hardware company because both are "tech").

---

#### Step 2: Gather Market Data & Calculate Multiples

**Enterprise Value Multiples (most important):**

| Multiple | When to Use | Why |
|---|---|---|
| **EV / EBITDA** | Default for most industries | Capital-structure-neutral, ignores D&A differences |
| **EV / EBIT** | When D&A is meaningful and differs across peers | Captures investment intensity |
| **EV / Revenue** | High-growth or unprofitable companies | Only option when earnings are negative |

**Equity Value Multiples:**

| Multiple | When to Use |
|---|---|
| **P/E (Price / EPS)** | Mature, stable companies; most intuitive to investors |
| **P/B (Price / Book)** | Financial institutions (banks, insurance) where book value is meaningful |

**Critical Rule:** **Numerator and denominator must match.**
- **Enterprise Value** (belongs to all capital providers) → pair with **pre-interest** metrics (Revenue, EBITDA, EBIT)
- **Equity Value** (belongs to shareholders) → pair with **post-interest** metrics (Net Income, EPS, Book Value of Equity)

Mixing these (e.g., EV / Net Income) is a **fundamental error** and an interview red flag.

---

#### Step 3: Calendarize and Normalize

**Calendarize:** If peers have different fiscal year ends (e.g., December vs. March), adjust so you're comparing the same time periods. Otherwise you're comparing 2025 earnings for one company to 2026 earnings for another.

**Normalize:** Strip out one-time items (restructuring charges, litigation gains, asset sales) so you're valuing *recurring* earnings power.

**Use Forward Multiples:** NTM (Next Twelve Months) or "current year" multiples are standard because they reflect expectations, not history. LTM (Last Twelve Months) multiples can be distorted by one-time events.

---

#### Step 4: Apply the Multiple to Your Target

```
Implied Enterprise Value = Target Company's EBITDA × Selected Multiple
→ EV Bridge → Implied Equity Value → Implied Share Price
```

**What multiple to use?**
- **Median** of the peer group (resilient to outliers — preferred)
- Apply a **premium or discount** if your target is better/worse than the median peer (higher growth = premium, lower margins = discount)
- Present a **range** (e.g., 25th to 75th percentile of peer multiples)

---

## IV. Comparable Transactions Analysis ("Transaction Comps" / Precedent Transactions)

### The Core Idea

**"What have acquirers actually paid for similar companies in recent M&A transactions?"**

Identical framework to trading comps, except you use **deal multiples** instead of current trading multiples.

### Key Differences from Trading Comps

| Dimension | Trading Comps | Transaction Comps |
|---|---|---|
| **Data source** | Current market prices | Historical M&A deal values |
| **Includes control premium?** | No (minority, market price) | **Yes (typically 20–40%)** |
| **Timeliness** | Always current | May be stale (deal was 2 years ago) |
| **Typical result** | Lower valuation | **Higher valuation** |

**Why higher?** Transaction multiples embed a **control premium** — the extra amount a buyer pays for 100% ownership and the ability to control the company's strategy.

**Pitfalls:**
- **Stale deals:** A deal from 3 years ago in a different market environment may not be relevant
- **Deal-specific synergies:** The buyer may have paid up because of unique synergies not available to your client
- **Limited universe:** There may be very few truly comparable transactions

---

## V. Putting It All Together: The "Football Field"

In practice, you use **all three (or four) methods** and present results as a **valuation range chart** (the "football field"):

```
              $30    $35    $40    $45    $50    $55    $60
               |------|------|------|------|------|------|
 DCF:                    [==========###==========]
 Comps:             [========###========]
 Precedent Txns:              [==========###==========]
 LBO (Floor):    [=====###=====]
 52-Week Range: [================================]
```

- **DCF** = intrinsic, stand-alone value
- **Comps** = relative market value today
- **Precedent Transactions** = what acquirers have paid (includes control premium)
- **LBO** = financial sponsor value (the "floor" — what a PE firm can afford to pay)

**Interview Answer Framework:** *"I'd triangulate across methodologies. If all three point to a similar range, I have high conviction. If they diverge, I'd investigate why — and that divergence itself tells a story about the market's view vs. intrinsic value."*

---

## VI. Quick-Reference: Common Interview Questions

| Question | Key to the Answer |
|---|---|
| "Walk me through a DCF." | Use the 5-step framework above. Hit every step but keep it crisp. |
| "What's WACC and why do we use it?" | Blended cost of all capital, because UFCF belongs to all capital providers. |
| "Why do you use unlevered FCF in a DCF?" | To value the business independently of financing; capital structure is in WACC. |
| "Walk me through an LBO." | Sources & Uses → Project Cash Flows → Pay Down Debt → Exit → Calculate Returns. |
| "What makes a good LBO candidate?" | Stable cash flows, low CapEx, strong market position, operational improvement potential. |
| "When would you NOT use a DCF?" | Early-stage companies with no/negative cash flows, highly unpredictable businesses, banks/financial institutions (use dividend discount model instead). |
| "Why might Precedent Transactions give a higher value than Comps?" | Control premium embedded in acquisition prices. |
| "EV/EBITDA vs. P/E — when to use which?" | EV/EBITDA for comparing across capital structures; P/E for mature, similarly leveraged companies. |
| "What has the biggest impact on a DCF output?" | Terminal value assumptions (growth rate, WACC) and revenue growth — always sensitivity-test these. |

---

*This guide is designed to build your intuition for how these models work and why each step exists. In interviews, demonstrating that you understand the **logic** behind the mechanics — not just the formulas — is what separates strong candidates from average ones.*