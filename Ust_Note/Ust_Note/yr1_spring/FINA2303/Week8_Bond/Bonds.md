## Cash Flow Structure

|P|C|C|C|C| C + Principal |
| --- | --- | --- | --- | --- | --- |
|   t=0  |  t=1   |t=2| ...|t=N-1|t=N|
Coupon rates are expressed as an **APR**.
## Risk-Free Zero-Coupon Bonds (ZCB)
Always sell at a discount since rate of return (positive) always higher than coupon rate (0)
$$P=\frac{Principle}{(1+r)^N}$$
## Yield to Maturity ($ytm$)
- $ytm$ is defined as $r$ such that the bond's price equals the discounted cash flow for any bond.
- $ytm^0$ is defined as the $ytm$ on a ZCB with N-year maturity.
### $ytm$ and Rate of Return
Two different but linked concepts
- $ytm$ is determined by the price which is set by the issuer.
- $r$ is determined by investors' expectation.
- They are linked by law of one price (supply and demand).
- Specially, for risk-free ZCB, $ytm^0=r$ for any maturity
### Yield Curve
The yield curve plots risk-free ZCB $ytm^0$ as a function of maturity.
- Yield curve is usually upward sloping since investors require a liquidity premium to hold long-term assets (lower price).
### Risk-Free Bond Pricing
- risk-free cash flows with maturity $t$ should be discounted using $ytm^0_{t}$
- Coupon bonds can be seen as a collection of $N$ ZCBs with different maturity
$$P=\sum^N_{t=1}\frac{C}{(1+ytm^0_{t})^t}+\frac{Principal}{(1+ytm^0_{N})^N}$$
- Price of coupon bond moves around with $tym^0_{t}$, i.e., the yield curve.

***Here, we use different $ytm^0_{t}$ to discount each coupon.***
### YTM on a (given) Coupon Bond
The $ytm$ on a given coupon bond is the unique interest rate that solves $$P=\sum^N_{t=1}\frac{C}{(1+ytm)^t}+\frac{Principal}{(1+ytm)^N}$$
***Here, we use one single $ytm$ to equate bond price to future cash flow***
- There is only one $ytm$ for a given bond at a given point in time
- $ytm$ is the IRR of the bond (use IRR on calculator to find YTM)
- $ytm$ is a weighted average of the $ytm^0_{t}$ on ZCB's with different maturity $t$, where the weights are the bond cash flows. Therefore, we have $$ytm^0_{N-1}<ytm<ytm^0_{N}$$
- $ytm$ of coupon bonds also moves around with the yield curve
## Non-Annual Coupons
In general, price of ZCB is $$P=\frac{Principal}{\left( 1+\frac{ytm^0_{t}}{n} \right)^{n\times t}}$$
where $n$ is the number of compounding periods within a year.
## Bond Price Sensitivity
$$P=\sum^N_{t=1}\frac{C}{(1+ytm)^t}+\frac{Principal}{(1+ytm)^N}=\frac{C}{ytm}\left(1-\frac{1}{(1+ytm)^N}\right)+\frac{Principal}{(1+ytm)^N}$$
### Bond Price Sensitivity to YTM
- $ytm$ determined by bond prices, which move around based on demand and supply
- $k$ is pre-specified by the contract

|$k=ytm$|Price = Principal | at par|
| --- | --- | --- |
|$k>ytm$|Price > Principal| at premium|
|$k<ytm$|Price < Principal| at discount
### Bond Price to Time to Maturity
The lower the time to maturity, the higher the price of the bond.
- Less coupons to be paid out; principal payment gets closer
- as $N\to 0$, $P\to Principal$
## Bond Risk
- Investors are willing to pay a lower price for corporate bonds
- $ytm$ of corporate bonds is higher than those of risk-free bonds
- The yield spread is the difference between the $ytm$ of a corporate bond and the $ytm$ on a risk-free US government bonds.