

# Independent Projects: Detailed Guide

You're right that replicating and adapting an existing open-source project is a perfectly legitimate approach — in fact, it's what most people do at your stage. Nobody expects a first-year student to invent something from scratch. What matters is that you **understand what you built, can explain the logic, and made meaningful modifications** that show independent thinking.

Let me break this down by project type, from most useful for banking interviews to most intellectually interesting.

---

## I. Project Selection Framework

Before picking a project, ask yourself three questions:

| Question | Why It Matters |
|---|---|
| **Can I explain every line of this to an interviewer?** | If you can't, it's a liability, not an asset. They will ask. |
| **Does it demonstrate a skill relevant to the role I'm targeting?** | A cool ML project that has no finance angle won't help you in a banking interview. |
| **Did I make meaningful changes or additions beyond the original?** | "I cloned a repo and ran it" is not a project. "I cloned a repo, changed the strategy, backtested on different data, and analysed why results differed" is. |

The sweet spot for your profile is projects that sit at the **intersection of finance knowledge and technical ability** — that's your unique selling point as an IS major targeting banking.

---

## II. Recommended Projects (Ranked by Interview Relevance)

---

### Project A: Three-Statement Financial Model with Automated Sensitivity Analysis

**Why this is the single best project for banking interviews:**
This is literally what analysts do on the job. If you can show you've built one independently, it eliminates the biggest concern a recruiter has about a first-year candidate — "can this person actually do the work?"

**What to build:**
- A fully integrated three-statement model (Income Statement, Balance Sheet, Cash Flow Statement) in Excel for a real public company
- A DCF valuation module that pulls from the three statements
- A VBA macro that automates sensitivity analysis across WACC and terminal growth rate, outputting a formatted data table
- A trading comps sheet with 5–8 comparable companies

**How to approach it:**
1. Pick a company you find genuinely interesting — you'll be asked about it, so choose one you want to talk about
2. Pull historical financials from Bloomberg, Capital IQ, or even the company's annual report
3. Build the three statements from scratch, linking them properly (this is the hard part and the whole point)
4. Layer on the DCF and comps
5. Write the VBA sensitivity macro

**What makes this impressive:**
- The three statements actually balance and link correctly (Net Income flows to Retained Earnings flows to Cash Flow Statement — the circular reference between interest expense and debt balance is handled)
- You can walk someone through the model live and explain every assumption
- The VBA component shows you can automate, not just spreadsheet

**What to say in an interview:**

> "I built a fully integrated three-statement model for [Company] in Excel, covering five years of historical data and a five-year projection. The model feeds into a DCF with a terminal value using both the perpetuity growth method and the exit multiple method. I also wrote a VBA macro that runs a two-dimensional sensitivity analysis across WACC and terminal growth rate and outputs a formatted table automatically. On the comps side, I pulled trading data for eight comparable companies and calculated EV/EBITDA, EV/Revenue, and P/E multiples. The implied valuation range from the DCF was [X to Y], which compared to the company's actual trading price of [Z], suggesting [the stock is undervalued/overvalued/fairly valued]. The most interesting finding was [something specific — e.g., how sensitive the valuation was to margin assumptions, or how the company traded at a discount to peers despite higher growth]."

**CV bullet:**

```
- Built a fully integrated 3-statement financial model and DCF valuation for
  [Company] in Excel; automated sensitivity analysis via VBA macro across WACC
  and terminal growth rate scenarios
```

**Resources to learn from:**
- Wall Street Prep or Breaking Into Wall Street (BIWS) free samples show the structure
- Aswath Damodaran's publicly available models on his NYU website are excellent references
- YouTube channels like "Mergers & Inquisitions" walk through the linking logic

---

### Project B: Equity Research Report

**Why this is valuable:**
It demonstrates that you can form and defend an investment view — which is exactly what the VC challenge tested, but in a more rigorous, written format. In interviews, when they say "pitch me a stock," you can hand them an actual written report.

**What to build:**
- A 5–10 page equity research report on a publicly traded company
- Industry overview and competitive positioning
- Financial analysis: historical performance, key ratios, trends
- Valuation: DCF and/or comps (can reference Project A's model)
- Investment thesis: Buy / Hold / Sell with a price target
- Key risks and catalysts

**How to approach it:**
1. Read two or three real sell-side equity research reports to understand the format (your Bloomberg Terminal access should give you access to these, or look for initiation reports from banks)
2. Pick a company — ideally one relevant to Hong Kong or Asia markets, since that's where you're interviewing
3. Write it as if you were a junior analyst publishing it for clients
4. Have someone review it for logical gaps

**What makes this impressive:**
- The thesis is clear and falsifiable — not wishy-washy
- The financial analysis is grounded in real numbers, not hand-waving
- You've identified a non-obvious insight (something the market might be missing)

**CV bullet:**

```
- Authored an independent equity research report on [Company] with a [Buy/Sell]
  recommendation and a 12-month price target of $[X], supported by DCF valuation
  and peer group analysis across [Y] comparable companies
```

---

### Project C: Quantitative Trading Strategy (Backtest)

**Now we're entering your stated area of interest.** This is where Python comes in. Let me be very specific about how to do this credibly versus how most students do it badly.

**The common mistake:**
Most students find a moving-average crossover strategy on GitHub, run it, see a 200% backtest return, put it on their CV, and can't explain why it doesn't work in practice. This is worse than not having the project at all because it signals naivety.

**What to actually build:**

A **factor-based equity strategy** or a **momentum/mean-reversion strategy** with proper backtesting methodology. The key is not the return — it's the rigour.

**Recommended approach:**

**Option 1: Momentum Strategy**

```
1. Universe: Hong Kong-listed stocks (or S&P 500 if data is easier to get)
2. Signal: 12-month price momentum minus the most recent month
   (the classic Jegadeesh & Titman 1993 formulation)
3. Portfolio: Go long the top decile, rebalance monthly
4. Backtest: 10+ years of data
5. Analysis: Sharpe ratio, maximum drawdown, turnover, performance
   during different market regimes (bull vs. bear vs. sideways)
```

**Option 2: Value + Quality Factor Strategy**

```
1. Universe: S&P 500 or Hang Seng constituents
2. Signals: Earnings yield (value) + ROE (quality)
3. Rank stocks by composite score, go long top quintile
4. Backtest: Track performance vs. benchmark
5. Analysis: Factor exposure decomposition, sector tilts,
   transaction cost sensitivity
```

**The critical additions that separate a good project from a bad one:**

| Element | Why It Matters |
|---|---|
| **Transaction costs** | Without these, every backtest looks amazing. Include realistic bid-ask spread and commission assumptions. |
| **Out-of-sample testing** | Train on 2010–2018, test on 2019–2024. If it only works in-sample, it's curve-fitted. |
| **Benchmark comparison** | Beating zero is meaningless. Compare to a passive buy-and-hold of the index. |
| **Risk metrics** | Sharpe ratio, max drawdown, Calmar ratio — not just total return. |
| **Regime analysis** | How does it perform in a crash? In a low-volatility grind? This shows you think about risk, not just return. |
| **Honest assessment of weaknesses** | "The strategy suffered during X because Y" is far more impressive than pretending it's perfect. |

**Python libraries to use:**

```python
# Core
import pandas as pd
import numpy as np

# Data
import yfinance as yf           # Free price data (good enough for a project)
# Or: use the Bloomberg API if you have terminal access

# Backtesting frameworks (pick one)
# Option 1: Build your own (more impressive, more control)
# Option 2: Use an existing framework and modify it

import matplotlib.pyplot as plt  # Visualization
import scipy.stats as stats      # Statistical testing
```

**GitHub repos worth studying and adapting:**

You mentioned hearing that replicating a GitHub project with proper changes is acceptable. Here are good starting points:

1. **Build your own from scratch using `pandas` and `numpy`** — This is the most impressive approach and not as hard as it sounds. You're essentially writing a loop that:
   - At each rebalance date, ranks stocks by your signal
   - Forms a portfolio of the top-ranked stocks
   - Tracks the portfolio return until the next rebalance
   - Records everything in a dataframe

2. **Adapt an open-source backtesting framework** — Frameworks like `backtrader`, `zipline-reloaded`, or `vectorbt` give you the infrastructure. Your value-add is the strategy logic, the analysis, and the interpretation.

**The key rule for adapting someone else's code:**
- You must change the **strategy** (not just the parameters)
- You must run it on **different data** (different market, different time period)
- You must add **your own analysis layer** (regime analysis, risk decomposition, comparison to published academic results)
- You must be able to **explain every function** in the codebase

**What to say in an interview:**

> "I built a momentum-based equity strategy in Python and backtested it over fifteen years of S&P 500 data. The strategy ranks stocks by their trailing twelve-month return, excluding the most recent month to avoid short-term reversal effects, and goes long the top decile with monthly rebalancing. After accounting for estimated transaction costs of twenty basis points per trade, the strategy generated an annualised return of [X]% with a Sharpe ratio of [Y], compared to [Z]% for a passive buy-and-hold. The most interesting finding was that the strategy significantly underperformed during [specific period, e.g., the 2020 COVID crash and recovery] because momentum strategies inherently struggle with sharp reversals — which taught me a lot about the practical limitations of systematic strategies."

**CV bullet:**

```
- Developed and backtested a momentum-based equity strategy in Python across 15
  years of S&P 500 data; analysed risk-adjusted returns, drawdown behaviour, and
  transaction cost sensitivity, achieving a Sharpe ratio of [X] vs. [Y] for the benchmark
```

---

### Project D: Machine Learning for Finance

**Honest advice first:** Machine learning projects are the most impressive-sounding but also the easiest to do badly. If you put ML on your CV, the interviewer — if they know anything about ML — will probe whether you actually understand the methodology or just called `sklearn.fit()`. For banking specifically (not quant funds), ML is less relevant than Projects A–C. But if you're genuinely interested, here's how to do it right.

**Good ML project ideas for your level:**

**Option 1: Earnings Surprise Prediction**

```
Goal: Predict whether a company will beat or miss consensus earnings estimates
Features: Historical beat/miss rate, analyst revision trends, sector momentum,
          pre-earnings price drift, short interest changes
Model: Logistic regression → Random forest → Compare
Data: Pull from Bloomberg or free sources (SimFin, Financial Modelling Prep API)
```

**Why this works as an interview talking point:** It connects ML to something fundamental — earnings — and the feature engineering requires financial intuition, not just coding ability.

**Option 2: Credit Risk / Default Prediction**

```
Goal: Predict probability of default for corporate bonds
Features: Leverage ratios, interest coverage, cash flow volatility,
          industry, credit rating history, macroeconomic indicators
Model: Logistic regression → Gradient boosted trees → Compare
Data: Publicly available datasets (e.g., from academic papers or Kaggle)
```

**Why this works:** Credit analysis is core to banking. This shows you understand both the ML and the finance.

**Option 3: Sentiment Analysis on Earnings Calls**

```
Goal: Extract sentiment from earnings call transcripts and test whether
      sentiment predicts subsequent stock returns
Tools: NLP (nltk or spaCy), potentially a pre-trained model like FinBERT
Data: Earnings call transcripts (Seeking Alpha, or scrape from SEC EDGAR)
Analysis: Does positive/negative sentiment predict 1-day, 5-day, 30-day returns?
```

**What makes an ML project credible vs. cringe:**

| Credible | Cringe |
|---|---|
| "I used logistic regression as a baseline and compared it to a random forest to see if added complexity improved out-of-sample accuracy" | "I used a deep neural network" (and can't explain why) |
| "Out-of-sample accuracy was only 54%, which is expected because markets are efficient, but the top-decile predictions showed a statistically significant edge" | "My model had 95% accuracy" (almost certainly overfit or using leaky features) |
| "I was careful to avoid look-ahead bias — all features were available before the prediction date" | No mention of train/test split or temporal ordering |
| "The most predictive feature was analyst revision momentum, which makes intuitive sense because..." | "The model found some patterns" (no interpretation) |

**CV bullet:**

```
- Built a logistic regression and random forest model in Python to predict
  earnings surprises for S&P 500 companies using financial and market features;
  achieved [X]% out-of-sample accuracy with top-decile precision of [Y]%
```

---

## III. Practical Execution Plan

Given your current position (first-year, limited time, interviews approaching), here's what I'd prioritise:

| Priority | Project | Time Required | Interview Payoff |
|---|---|---|---|
| **Do first** | Project A: Three-Statement Model + DCF in Excel with VBA | 2–3 weeks | Extremely high — directly proves you can do the job |
| **Do second** | Project B: Equity Research Report (can use Project A's model) | 1–2 weeks | High — gives you a stock pitch and shows written communication |
| **Do if time allows** | Project C: Quant Strategy Backtest | 2–4 weeks | Medium for banking, high for quant/AM roles |
| **Do if genuinely interested** | Project D: ML for Finance | 3–5 weeks | Low for banking, high for quant roles; risk of being hard to explain |

**My strong recommendation:** Do Projects A and B first. They are the highest-ROI activities for banking interview preparation, and they compound — the model feeds the report, the report gives you a stock pitch, and together they prove that the "Financial Modelling" and "Python" lines on your CV are real.

Project C is excellent if you're also considering quant funds, asset management, or if you simply want to build the skill. And it aligns with your stated interest in quant trading — which means you'll be more motivated to finish it, and that matters.

Project D is the most interesting intellectually but the hardest to execute credibly. Save it for after you've landed the internship, or for a second-year course project where you have more time and academic supervision.

---

## IV. How to Present These on Your CV

Create a dedicated section between Experience and Skills:

```
────────────────────────────────────────────────────────────
PROJECTS
────────────────────────────────────────────────────────────
Three-Statement Financial Model & DCF Valuation               Dec 2025
- Built a fully integrated 3-statement model for [Company] in Excel with
  5 years of historical data and a 5-year forward projection; linked IS, BS,
  and CFS with circular reference handling for interest expense
- Developed a DCF valuation module with terminal value via both perpetuity
  growth and exit multiple methods; automated sensitivity analysis using VBA
- Constructed a trading comps sheet across 8 peers; implied valuation range
  of $[X]–$[Y] vs. current trading price of $[Z]

Momentum Equity Strategy Backtest                             Nov 2025
- Designed and backtested a 12-1 month momentum strategy in Python across
  15 years of S&P 500 data with monthly rebalancing and 20bp transaction costs
- Analysed risk-adjusted performance (Sharpe [X], max drawdown [Y]%) across
  market regimes; identified underperformance during sharp reversals as key
  strategy limitation
```

---

## V. The "Replicated Project" Question

You mentioned hearing that replicating a GitHub project with changes is acceptable. Let me be precise about what's okay and what's not:

### Totally Fine:
- You find an open-source backtesting framework, study how it works, implement your *own* strategy using it, and analyse the results with your own interpretation
- You follow a tutorial to build a three-statement model, then build a *second one* independently for a different company
- You read an academic paper (e.g., Jegadeesh & Titman on momentum), replicate the methodology in Python, extend it to a different market (e.g., Hong Kong stocks instead of US stocks), and analyse whether the findings hold

### Risky:
- You fork a repo, change a few parameters, and put it on your CV — if someone looks at your GitHub and sees the commit history, it's obvious
- You use a project that's so common that the interviewer has seen it ten times (e.g., the default Kaggle Titanic classification project)

### Not Okay:
- You clone something and can't explain how it works
- You claim credit for architecture decisions you didn't make

**The golden rule:** If you can sit in front of an interviewer, open the code, and explain every design choice — why you used this data structure, why you chose this rebalancing frequency, why this risk metric and not that one — then the project is legitimate regardless of where you got the initial inspiration.

---

## VI. One Final Thought

The best project is the one you actually finish and can talk about with genuine enthusiasm. Interviewers can tell the difference between someone reciting a rehearsed explanation of code they half-understand and someone whose eyes light up when they talk about a finding that surprised them. Your curiosity about quant strategies and ML is a real asset — channel it into something concrete, make it rigorous, and be honest about what you learned and what the limitations are. That combination of technical ability, intellectual honesty, and genuine interest is exactly what makes a candidate memorable.



# How to Handle Your Existing Course Model

Short answer: **Don't start from scratch, but don't put the course homework on your CV as-is either.** What you have is a foundation — now you need to elevate it into something that's genuinely yours.

Let me explain the reasoning and exactly what to do.

---

## I. Why the Course Homework Alone Doesn't Work

Here's the problem. When a recruiter or interviewer sees "Built a three-statement financial model" on your CV, they're imagining that you:

1. Picked a real company
2. Pulled real financials from filings or Bloomberg
3. Made your own assumptions about revenue growth, margins, CapEx, working capital
4. Built the structure and the linkages yourself
5. Produced an output that reflects independent analytical judgment

What you actually have right now is:

1. A professor gave you the framework
2. The company is hypothetical
3. The assumptions were either given to you or heavily guided
4. You filled in cells and connected formulas, but the architecture was pre-built
5. Every student in your class submitted the same thing

That's a learning exercise, which is great — it means you understand the mechanics. But it's not a differentiator on your CV because you can't credibly claim ownership of the work, and if an interviewer asks "walk me through your model" and you say "well, my professor gave us the structure and we filled in the numbers," the impact collapses.

---

## II. What You Actually Need to Do

The good news is you're maybe **40% of the way there already.** You understand how the three statements link. You've done the wiring. You know that net income flows to retained earnings, that D&A adds back on the cash flow statement, that the balance sheet has to balance. That's the hard conceptual part and you've already done it.

What's left is applying that knowledge to a real company with real data and real judgment calls. Here's the exact process:

---

### Step 1: Pick a Real Company (Half a Day)

**Criteria for choosing well:**

| Factor | Why It Matters |
|---|---|
| **You find it genuinely interesting** | You'll be asked about it in interviews. Enthusiasm matters. |
| **Relatively simple business model** | Avoid conglomerates, banks, or companies with dozens of segments. You want a company where revenue drivers are clear and understandable. |
| **Publicly traded with clean financials** | You need real filings to pull from. Avoid companies with lots of one-time items, discontinued operations, or complex accounting. |
| **Relevant to your target banks' coverage** | If you're interviewing at a bank with a strong TMT practice in Hong Kong, model a Hong Kong or Asia-listed tech company. It becomes a natural conversation piece. |

**Good examples for your profile:**
- A mid-cap Hong Kong or China-listed company in consumer, tech, or industrials
- A well-known US company if you want easier data access (e.g., Starbucks, Nike, Spotify — simple business models, clean financials, easy to tell a story about)

**Avoid:**
- Banks and insurance companies (completely different modelling framework)
- Early-stage companies with no earnings (the three-statement model won't work well)
- Companies with extremely complex segment reporting

---

### Step 2: Pull Real Historical Data (One Day)

This is where the course exercise and a real model diverge completely. In class, the numbers were given to you. Now you need to go to the source.

**Where to get the data:**
- **Best:** Bloomberg Terminal (you have access) — use the FA function to pull standardised financials
- **Also good:** Capital IQ (you listed it on your CV)
- **Free alternative:** Company's actual annual reports / 10-K filings from the company's investor relations page or HKEX / SEC EDGAR
- **Acceptable shortcut:** SimFin, Macrotrends, or Financial Modelling Prep (free financial data APIs)

**Pull five years of historical data** for all three statements. Enter them manually into your model — don't just paste a Bloomberg export. The act of manually entering the data forces you to understand each line item, which is exactly the point.

**Why this step matters more than people think:**
Real financials are messy. You'll encounter line items that don't match your textbook template. You'll find one-time charges, reclassifications, changes in accounting standards, items that appeared in 2022 but not 2023. Dealing with that messiness is what makes this a real modelling exercise. Your course homework had none of that, and that's precisely why it wasn't sufficient.

---

### Step 3: Build the Projection (Two to Three Days)

This is the intellectual core of the project — and where your independent judgment comes in.

**Revenue build:**
Don't just assume "revenue grows at 8% per year." Build a simple revenue driver model. For example:
- A retail company: number of stores × revenue per store, with assumptions for new store openings and same-store sales growth
- A SaaS company: number of subscribers × average revenue per user, with assumptions for customer acquisition and churn
- A manufacturing company: volume × price, with assumptions for market share and pricing trends

**Why this matters:** In an interview, when they ask "how did you project revenue," saying "I assumed 8% growth" is weak. Saying "I modelled store count growth based on management's guidance for 30 new openings per year and assumed same-store sales growth of 3%, which is in line with the three-year historical average" is what an analyst actually does.

**Expenses:**
- Project each major cost line as a percentage of revenue (gross margin, SG&A as a percent of revenue, R&D as a percent of revenue)
- Have a view on whether margins expand, contract, or stay flat — and be able to explain why
- Look at historical trends and anchor your assumptions to them

**Balance sheet and cash flow statement:**
- Working capital items (receivables, inventory, payables) should be projected using turnover ratios (days sales outstanding, days inventory outstanding, days payable outstanding) — calculate the historical ratios and hold them constant or trend them based on your thesis
- CapEx: look at historical CapEx as a percentage of revenue or CapEx relative to D&A
- Debt schedule: if the company has debt maturities, model them. If not, keep the debt balance flat for simplicity.

**The linking logic you already know from class:**
- Net income from the income statement flows to retained earnings on the balance sheet and to the top of the cash flow statement
- D&A from the income statement adds back on the cash flow statement
- CapEx on the cash flow statement reduces PP&E on the balance sheet
- Changes in working capital items on the balance sheet flow through the operating section of the cash flow statement
- Cash at the end of the cash flow statement equals cash on the balance sheet

The difference is that now you're doing this with real numbers that don't always cooperate, and the assumptions are yours.

---

### Step 4: Build the DCF (One Day)

You've done this conceptually. Now apply it:

- Calculate UFCF from your projections
- Calculate WACC using real inputs (pull the company's beta from Bloomberg, use the actual 10-year government bond rate, use a standard ERP)
- Calculate terminal value using both methods (perpetuity growth and exit multiple)
- Discount everything back using mid-year convention
- Bridge from enterprise value to equity value using the company's actual net debt, minority interest, etc.
- Compare your implied share price to the actual current trading price

**This last step is what makes the project come alive.** Your model spits out an implied value of, say, HK$45 per share, and the stock currently trades at HK$52. Now you have something to talk about. Is the stock overvalued? Or are your assumptions too conservative? Where's the gap? That analytical conversation is exactly what an interviewer wants to have with you.

---

### Step 5: Build the Comps Table (Half a Day)

- Identify five to eight comparable companies
- Pull their trading multiples (EV/EBITDA, EV/Revenue, P/E) from Bloomberg or Capital IQ
- Calculate the median and mean
- Apply the median multiple to your target company's metrics
- Compare the comps-implied value to your DCF-implied value

**Why include comps:** It gives you a second valuation methodology and shows you understand triangulation. In interviews, they'll ask "what if your DCF says $45 but comps say $38?" You need to be able to discuss why they might differ (your growth assumptions are more optimistic than what the market is pricing, or the peer group isn't perfectly comparable, etc.).

---

### Step 6: Add VBA Sensitivity Analysis (Half a Day to One Day)

This is the cherry on top and it's easier than you think. You're not building a complex application. You're writing a macro that does something very specific:

```vba
Sub SensitivityTable()

    Dim WACCRange As Variant
    Dim GrowthRange As Variant
    Dim i As Integer, j As Integer
    
    ' Define the ranges to iterate through
    WACCRange = Array(0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11)
    GrowthRange = Array(0.015, 0.02, 0.025, 0.03, 0.035)
    
    ' Reference cells in your model where WACC and growth rate are inputs
    Dim WACCCell As Range
    Dim GrowthCell As Range
    Dim OutputCell As Range
    
    Set WACCCell = Sheets("DCF").Range("C5")      ' Your WACC input cell
    Set GrowthCell = Sheets("DCF").Range("C6")     ' Your terminal growth input cell
    Set OutputCell = Sheets("DCF").Range("C30")     ' Your implied share price output
    
    ' Store original values
    Dim origWACC As Double
    Dim origGrowth As Double
    origWACC = WACCCell.Value
    origGrowth = GrowthCell.Value
    
    ' Output location for the sensitivity table
    Dim OutputStart As Range
    Set OutputStart = Sheets("Sensitivity").Range("C3")
    
    ' Write headers
    For j = 0 To UBound(GrowthRange)
        OutputStart.Offset(0, j + 1).Value = GrowthRange(j)
    Next j
    For i = 0 To UBound(WACCRange)
        OutputStart.Offset(i + 1, 0).Value = WACCRange(i)
    Next i
    
    ' Iterate and record
    For i = 0 To UBound(WACCRange)
        WACCCell.Value = WACCRange(i)
        For j = 0 To UBound(GrowthRange)
            GrowthCell.Value = GrowthRange(j)
            Application.Calculate   ' Force recalculation
            OutputStart.Offset(i + 1, j + 1).Value = OutputCell.Value
        Next j
    Next i
    
    ' Restore original values
    WACCCell.Value = origWACC
    GrowthCell.Value = origGrowth
    Application.Calculate
    
    ' Optional: format the base case cell
    ' (find the cell where WACC and growth match the originals and bold it)
    
    MsgBox "Sensitivity table complete."
    
End Sub
```

**What this does:** It loops through every combination of WACC and terminal growth rate, plugs each pair into your model, lets the spreadsheet recalculate, reads the implied share price output, and writes it into a clean table. When it's done, you restore the original values.

**This is not complex programming.** It's a nested loop with cell references. But it's impressive on a CV because most students don't bother to learn VBA, and it demonstrates that you can automate repetitive analytical work — which is exactly what banks want from a junior analyst who knows how to code.

You can extend it with conditional formatting (highlight cells where the implied price is above/below the current trading price) or add a second output variable (e.g., implied EV/EBITDA at each scenario).

---

## III. How to Frame This on Your CV and in Interviews

### On Your CV

Do **not** mention the course homework at all. Present this as an independent project:

```
Three-Statement Financial Model & DCF Valuation                Jan 2026
- Built a fully integrated 3-statement model for [Company] in Excel using 5
  years of historical filings; projected revenue via a bottom-up driver model
  (e.g., store count × same-store sales) and modelled margins, working capital,
  and CapEx based on historical trends
- Developed a DCF with terminal value via both perpetuity growth and exit
  multiple methods; implied share price of HK$[X] vs. current price of HK$[Y],
  suggesting [undervaluation / overvaluation] of approximately [Z]%
- Automated WACC / terminal growth rate sensitivity analysis using VBA;
  built a trading comps sheet across [8] peers to cross-check DCF-implied value
```

### In an Interview

If they ask "how did you learn to build this," be honest:

> "I first learned the three-statement linking logic in my Corporate Finance class, where we built a model with a given framework and a hypothetical company. After that, I wanted to test whether I could actually do it independently with real data, so I picked [Company], pulled five years of historical financials from Bloomberg, and built the model from scratch. The biggest difference was dealing with real-world messiness — line items that don't match the textbook, one-time charges I had to normalise, and having to make my own assumptions about growth and margins instead of being given them. I also added a DCF module, a comps sheet, and a VBA macro for sensitivity analysis, none of which were part of the course."

This framing is honest, credible, and actually *more* impressive than pretending you invented the concept from nothing. It shows a learning progression: guided exercise → independent application → extension with new tools. That's exactly the trajectory a bank wants to see in an intern.

---

## IV. What You Can Reuse vs. What You Need to Build New

| From Course Homework | What to Do With It |
|---|---|
| Understanding of how the three statements link | **Reuse the knowledge, not the file.** Open a blank workbook. |
| The formula logic (e.g., how to calculate UFCF, how to handle the D&A add-back) | **Reuse directly.** This is knowledge, not copied work. |
| The specific template structure and layout | **Redesign it.** Use your own layout, your own colour coding, your own tab structure. Make it yours. |
| The hypothetical company's numbers | **Throw them away entirely.** Use a real company. |
| Assumptions given by the professor | **Replace with your own.** This is the entire point. |

---

## V. Timeline

If you work on this consistently, here's a realistic schedule:

| Day | Task |
|---|---|
| **Day 1** | Pick the company, pull and enter historical financials |
| **Day 2–3** | Build the income statement projection, including the revenue driver model |
| **Day 4** | Build the balance sheet projection (working capital, PP&E, debt schedule) |
| **Day 5** | Build the cash flow statement, link everything, make sure the balance sheet balances |
| **Day 6** | Build the DCF module (WACC calculation, terminal value, discounting, EV bridge) |
| **Day 7** | Build the comps table, write the VBA macro |
| **Day 8** | Review, stress-test, clean up formatting, prepare to walk someone through it |

Eight days of focused work. That's it. And at the end you'll have something concrete, credible, and genuinely impressive for a first-year student — because very few first-years do this independently.

The course gave you the training wheels. Now ride without them.

