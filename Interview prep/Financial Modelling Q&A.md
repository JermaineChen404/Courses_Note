
## 1. "Walk me through a DCF."

Sure. The idea behind a DCF is that a company is worth the present value of all the cash it will generate in the future. A dollar today is worth more than a dollar tomorrow, so we discount future cash flows back to what they're worth right now.

Here's how I'd build one.

First, I'd project the company's unlevered free cash flows, typically over a five-to-ten-year period. I start with revenue, work down to operating income, tax that at the marginal rate — not the effective rate, because we want to isolate operating performance before any financing effects — and that gives me NOPAT. Then I add back depreciation and amortization because it's a non-cash charge, subtract capital expenditures because that's real cash going out the door to maintain and grow the asset base, and subtract any increase in net working capital, because when working capital goes up, cash is getting tied up in things like inventory and receivables. What's left is unlevered free cash flow.

The reason we use unlevered free cash flow — meaning before interest and debt repayments — is that we're trying to value the entire enterprise independent of how it's financed. The financing decision gets captured separately in the discount rate.

Second, I calculate the discount rate, which is the weighted average cost of capital, or WACC. Since unlevered free cash flow belongs to all capital providers — both debt holders and equity holders — the discount rate needs to reflect the blended cost of both. For the cost of equity, I'd use CAPM: risk-free rate plus beta times the equity risk premium. For the cost of debt, I'd use the company's pre-tax borrowing cost and multiply it by one minus the tax rate, because interest expense is tax-deductible and that makes debt effectively cheaper. Then I weight each by the proportion of debt and equity in the capital structure, using market values rather than book values.

Third, I need to deal with the fact that I can't forecast cash flows forever. So I calculate a terminal value to capture everything beyond the projection period. There are two ways to do this. The perpetuity growth method takes the last year's free cash flow, grows it at a modest long-term rate — usually two to three percent, roughly in line with GDP growth — and divides by WACC minus that growth rate. The logic is that no company can grow faster than the economy indefinitely. The other approach is the exit multiple method, where I apply a comparable EV-to-EBITDA multiple to the final year's EBITDA. In practice I use both and cross-reference them. Terminal value typically represents sixty to eighty percent of total enterprise value, which is exactly why it's so important to sensitivity-test those assumptions.

Fourth, I discount all the projected free cash flows and the terminal value back to today using WACC. One practical detail: I'd use a mid-year convention, meaning I discount by half a year, one and a half years, two and a half years, and so on, because cash flows arrive throughout the year, not in a lump sum on December 31st. Without this adjustment, you'd systematically undervalue the company.

Finally, I bridge from enterprise value to equity value. I subtract net debt — that's total debt minus cash — and also subtract minority interest and preferred stock. Then I divide the resulting equity value by diluted shares outstanding to arrive at an implied share price. The intuition here is straightforward: enterprise value is what it costs to buy the whole business, but as an equity buyer you inherit the debt and you get to keep the cash, so you adjust accordingly.

I'd always present the result as a range rather than a single number, using a sensitivity table around WACC and the terminal growth rate, because small changes in those assumptions can meaningfully move the output. That's actually the biggest limitation of a DCF — the heavy dependence on terminal value assumptions — but it's also the most theoretically rigorous valuation method because it's grounded in the company's own fundamentals rather than what the market happens to be doing today.

---

## 2. "What's WACC and why do we use it?"

WACC stands for weighted average cost of capital. It's the blended rate that reflects what it costs a company to finance itself through both debt and equity.

The reason we use it in a DCF is a matter of consistency. When we calculate unlevered free cash flow, we're measuring cash flow that belongs to everyone who has a claim on the company — both lenders and shareholders. So the discount rate needs to reflect the cost of capital for all of those stakeholders, not just one. That's exactly what WACC does. It takes the cost of equity, weights it by the proportion of equity in the capital structure, adds the after-tax cost of debt weighted by the proportion of debt, and blends them together.

The after-tax piece on the debt side is important. Interest is tax-deductible, so the true cost of debt to the company is lower than the stated interest rate. WACC captures that benefit.

One thing I'd be careful about in practice is making sure I'm using market values of debt and equity for the weightings, not book values. The market value of equity is the company's market cap, and for debt, ideally you'd use market value as well, though book value is a reasonable approximation when bonds aren't actively traded.

---

## 3. "Why do you use unlevered FCF in a DCF?"

The short answer is that we want to separate the question of what the business is worth from the question of how it's financed.

Unlevered free cash flow strips out interest payments and debt repayments. It represents the cash flow generated by the core operations of the business before any financing decisions come into play. This is important because two identical businesses with different capital structures would have different levered cash flows but the same unlevered cash flows — and they should have the same enterprise value.

By using unlevered free cash flow, we capture the operating value cleanly. Then the financing side — the cost and benefit of debt — gets reflected in the discount rate through WACC. It's a clean separation. The business value goes into the numerator, and the financing cost goes into the denominator.

If I were to use levered free cash flow instead, I'd need to discount it at the cost of equity alone, and that would give me equity value directly rather than enterprise value. That approach works, but it's less common in practice because it's harder to keep the capital structure assumptions consistent over time — as debt gets paid down, the cost of equity changes, the leverage ratio changes, and everything becomes circular. The unlevered approach avoids that complexity.

---

## 4. "Walk me through an LBO."

An LBO analysis answers the question of what a private equity firm could afford to pay for a company, given a target return, when the acquisition is primarily financed with debt. The analogy I'd use is buying a house: you put down a fraction of the purchase price as equity, borrow the rest as a mortgage, and use the property's rental income to pay down the mortgage over time. When you eventually sell, you keep everything above what you owe.

Here's how I'd walk through it.

First, I'd establish the purchase price. Typically you start with an entry multiple — say, eight times LTM EBITDA — to get the enterprise value. Then I'd use the enterprise value bridge in reverse to figure out how much equity the sponsor actually needs to write a check for.

Next, I'd build the sources and uses table. On the uses side, you have the purchase price plus any transaction fees and financing fees. On the sources side, you have the various debt tranches — a revolver, term loans, senior notes, possibly mezzanine debt — and then the sponsor's equity fills the gap. The sources and uses must balance. In a typical deal, total leverage might be four to six times EBITDA, with the sponsor putting up thirty to forty percent as equity.

Then I'd project the company's cash flows over the hold period, which is usually five years. This part is similar to a DCF, except I'm using levered free cash flow — meaning after interest expense — because what I care about is how much cash is left to pay down debt each year. I'd model each debt tranche separately, tracking mandatory amortization on the term loans and any optional paydowns with excess cash flow. Year by year, the debt balance comes down, and the equity value implicitly grows.

At the end of the hold period, I'd model the exit. I'd apply an exit multiple to the final year's EBITDA — often the same multiple as entry for a conservative assumption — to get the exit enterprise value. Then I subtract whatever debt is still outstanding at that point to get the exit equity value.

Finally, I'd calculate the returns. The two key metrics are IRR and MOIC. MOIC is simply exit equity divided by entry equity — how many times did you get your money back. IRR is the annualized return — what rate of return solves the equation where the equity invested today grows to the exit equity value over the hold period. Sponsors typically target twenty to twenty-five percent IRR and two to three times MOIC.

The important takeaway is that there are really three levers that create value in an LBO. The first is deleveraging: you use the company's cash flow to pay down debt, so even if nothing else changes, the equity value grows because there's less debt sitting in front of it. The second is EBITDA growth through revenue growth or margin improvement — the pie gets bigger. The third is multiple expansion — you sell at a higher multiple than you bought at. The best LBOs are driven by the first two; relying on multiple expansion alone is essentially speculation.

---

## 5. "What makes a good LBO candidate?"

The ideal LBO candidate is a business that generates very stable and predictable cash flows. That's the single most important characteristic, because the company needs to reliably service a significant amount of debt. If cash flows are volatile, you run the risk of missing interest payments, and the entire deal structure falls apart.

Beyond that, you want low capital expenditure requirements so that a large portion of EBITDA actually converts into free cash flow available for debt paydown. A business that needs to reinvest heavily in itself leaves less cash for deleveraging.

You're also looking for a strong and defensible market position — meaningful barriers to entry, loyal customer base, recurring revenue if possible — because that provides downside protection. Lenders need to believe the business will survive and thrive even in a downturn.

Then there's the operational improvement angle. The best PE deals involve a clear thesis for how the sponsor can grow the business or improve margins — whether that's through better management, pricing optimization, cost cutting, or buy-and-build strategies with add-on acquisitions.

Finally, a clean and separable business is easier to finance. Minimal off-balance-sheet liabilities, not overly dependent on a single customer or product line, and ideally in a non-cyclical industry. Lenders want simplicity and certainty.

---

## 6. "When would you NOT use a DCF?"

There are a few situations where a DCF either doesn't work well or is the wrong tool entirely.

The most obvious case is early-stage or high-growth companies with negative or highly unpredictable cash flows. If a company isn't generating free cash flow yet and won't for years, you're essentially guessing at numbers for most of the projection, and the entire valuation becomes a function of your terminal value assumption. At that point, the model gives you a false sense of precision. For companies like that, you might be better off using revenue multiples, a comparable company analysis, or some kind of unit-economics-based approach.

Banks and financial institutions are another case. For a bank, debt isn't really a financing choice — it's the raw material of the business. Deposits and borrowed funds are the lifeblood of how a bank operates. The concept of unlevered free cash flow doesn't apply cleanly, and WACC doesn't work in the traditional sense. For banks, you'd use a dividend discount model or a residual income model instead, and you'd value them on price-to-book or price-to-tangible-book multiples.

Highly cyclical businesses can also be tricky. If a company's earnings swing wildly with the commodity cycle or the economic cycle, your five-year projection is very sensitive to where in the cycle you start. You might pick a period that looks great or terrible just based on timing. It's not that you can't run the DCF — you can — but you need to be extra thoughtful about normalizing the cash flows and being honest about the uncertainty.

And practically speaking, if you have very little information about a company — maybe it's a private business with limited financials — it may not be worth running a DCF because the inputs would be so uncertain that the output isn't meaningful.

---

## 7. "Why might Precedent Transactions give a higher value than Trading Comps?"

The main reason is the control premium. Trading comps reflect what investors are willing to pay for a minority stake in a company — you're buying a few shares on the open market, you have no control over the company's strategy. Precedent transaction multiples, on the other hand, reflect what an acquirer actually paid to buy the entire company. Acquirers are willing to pay more because with full ownership comes control — the ability to change management, cut costs, realize synergies, redirect strategy. That extra amount — typically a twenty to forty percent premium over the trading price — gets baked into the transaction multiple.

On top of the pure control premium, there may be deal-specific synergies driving the price higher. If the acquirer believed they could take out two hundred million dollars of redundant costs by combining the two businesses, they would have been willing to share some of that value with the seller in the form of a higher purchase price. That synergy value doesn't exist in the trading market.

There can also be competitive dynamics. In an auction process with multiple bidders, the price gets bid up above what any single buyer's fundamental analysis might suggest. Winner's curse is a real phenomenon.

So when I present a valuation using both methods, I'd expect precedent transactions to sit above trading comps, and I'd explain the gap primarily through the control premium and any embedded synergies.

---

## 8. "EV/EBITDA vs. P/E — when to use which?"

The key distinction comes down to what you're trying to compare and whether capital structure differences matter.

EV-to-EBITDA is an enterprise-level multiple. It measures how the market values the entire business — debt plus equity — relative to its pre-interest, pre-tax, pre-depreciation earnings. Because it sits above the capital structure, it lets you compare companies with very different levels of debt on an apples-to-apples basis. If I'm comparing two companies in the same industry but one is highly leveraged and the other has no debt, EV-to-EBITDA will give me a much cleaner comparison than P/E. It also removes the distortion from different depreciation policies, which is useful when comparing companies with different asset bases. For these reasons, it's the default multiple in most M&A and valuation work.

P/E — price to earnings — is an equity-level multiple. It tells you how the market values the company's earnings after all expenses including interest and taxes. It's the most intuitive multiple for equity investors because it directly relates to what shareholders actually receive. I'd use P/E for mature, stable companies where the peer group has similar capital structures and tax situations. It's also the multiple that public market investors talk about most, so it's useful when the audience is equity investors rather than M&A professionals.

The one thing I'd never do is mix them up conceptually. Enterprise value pairs with pre-interest metrics like EBITDA because both belong to all capital providers. Equity value pairs with post-interest metrics like net income because both belong only to shareholders. Crossing those wires — like computing EV-to-net-income — would be a fundamental error because the numerator and denominator would reflect claims of different stakeholder groups.

---

## 9. "What has the biggest impact on a DCF output?"

In my experience, the answer is almost always the terminal value assumptions, and it's not even close. Terminal value typically represents sixty to eighty percent of the total enterprise value in a DCF, so even small changes to the terminal growth rate or the discount rate have an outsized effect on the final number.

To put it concretely, if I change the terminal growth rate from two percent to three percent, or if I move WACC by fifty basis points, the implied share price can easily shift by ten to twenty percent or more. That's a huge swing from changing assumptions that are inherently very difficult to pin down. Nobody really knows what the right long-term growth rate is — we're making educated guesses.

Beyond terminal value, revenue growth assumptions in the projection period have the next biggest impact, because revenue is the top line that drives everything else. If I'm off on revenue growth by a couple of percentage points each year, that compounds over the projection period and also flows through into the terminal value.

This is exactly why I'd always present a DCF as a range rather than a point estimate, and I'd show a two-dimensional sensitivity table with WACC on one axis and the terminal growth rate on the other. The honest answer is that a DCF gives you a framework for thinking about value and a defensible range — but anyone who gives you a single precise number from a DCF is probably overconfident in their assumptions.