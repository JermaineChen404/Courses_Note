---
title: "HW1"
course: FINA3203
type: Homework
tags: [fina3203, derivatives, forward price, margin, exchange rate]
---

# Q2
## (1)
The 6-month forward price is given by
$$
F_{0,\text{6 month}}=S_{0}\times e^{rT_{1}}=100\times e^{0.05\times \frac{1}{2}}\approx102.53
$$
## (2)
The 6-year forward price is given by
$$
F_{0,6}=S_{0}\times e^{rT_{2}}=100\times e^{0.05\times_{6}}\approx 134.99
$$

# Q3
## (1)
$$
F_{0, \text{10 month}}=S_{0}\times e^{rT_{1}}=100 \times e^{\frac{0.1\times 10}{12}}\approx 108.69 
$$

## (2)
$$
F_{\frac{1}{4},\text{7 month}}=S_{\frac{1}{4}}\times e^{rT_{2}}=150 \times e^{\frac{0.1\times 7}{12}}\approx 159.01
$$

## (3)
The value is given by
$$
\left( F_{\frac{1}{4},\text{7 month}} - F_{0, \text{10 month}}\right) \times e^{-rT_{2}}=(150 \times e^{\frac{0.1\times 7}{12}}-100 \times e^{\frac{0.1\times 10}{12}})\times e^{-0.1\times \frac{7}{12}}\approx 47.47
$$

## (4)
$$
\left( F'_{\frac{1}{4},\text{7 month}} - F_{0, \text{10 month}}\right) \times e^{-rT_{2}}=(50 \times e^{\frac{0.1\times 7}{12}}-100 \times e^{\frac{0.1\times 10}{12}})\times e^{-0.1\times \frac{7}{12}}\approx -52.53
$$

## (5)
The value of a short position is given by
$$
\left(F_{0, \text{10 month}}-F_{\frac{1}{4},\text{7 month}} \right) \times e^{-rT_{2}}=(100 \times e^{\frac{0.1\times 10}{12}}-150 \times e^{\frac{0.1\times 7}{12}})\times e^{-0.1\times \frac{7}{12}}\approx -47.47
$$

## (6)
$$
\left(F_{0, \text{10 month}}-F'_{\frac{1}{4},\text{7 month}} \right) \times e^{-rT_{2}}=(100 \times e^{\frac{0.1\times 10}{12}}-50 \times e^{\frac{0.1\times 7}{12}})\times e^{-0.1\times \frac{7}{12}}\approx 52.53
$$

## (7)
The initial value of the long forward is zero since it costs nothing to enter a forward contract initially.

# Q4

A forward curve is a graph showing the forward prices for all available maturities.

Contango is where the forward prices increase with maturity.

Backwardation is where the forward prices decrease with maturity.

Convenience yield is the extra value due to the higher certainty that you will have the commodity exactly when you need it and as much as you need.

Forward exchange rate is the predetermined rate at which two currencies will be exchanged on a future date, derived from the spot rate and adjusted for the interest rate differential between the currencies.

Currency carry trade is a strategy that borrowing in a low-interest-rate currency and investing in a higher-interest-rate currency to profit from the interest rate differential.

Covered interest rate parity is a condition where there is no arbitrage, and therefore the forward exchange rate must equal the spot rate adjusted by the interest rate differential between two countries.

Uncovered interest rate parity is a theoretical condition suggesting that a low-interest rate currency is expected to appreciate, i.e., the expected change in the spot exchange rate will offset the interest rate differential between two countries by assuming that the forward exchange rate equals the spot rate that the market expects today for maturity.

# Q5
## 1
On Jan 28, the P/L is
$$(8336.50-8136.00)\times 10\times 10=\$20050$$
On Jan 29, the P/L is
$$(8112.00-8336.50)\times 10 \times 10=-\$22450$$
At the end of Jan 28, the balance is
$$10\times 13750 \times e^{0.01\times \frac{1}{365}}+20050\approx \$157553.77$$
At the end of Jan 29, the balance is
$$(10\times 13750 \times e^{0.01\times \frac{1}{365}}+20050)\times e^{0.01\times \frac{1}{365}}-22450 \approx \$135108.08>11000\times 10$$
Therefore, no margin call.

## 2
On Jan 28, the P/L is
$$(8136.00-8336.50) \times 5 \times 10=-\$10025$$
On Jan 29, the P/L is
$$(8336.50-8112.00)\times 5 \times 10=\$11225$$

## 3
Given that
$$F_{0,T}=S_{0}\times e^{(r-q)\times T}$$
where $q$ is the dividend yield. We have
$$q=r-\frac{1}{T}\ln \frac{F_{0,T}}{S_{0}}=0.01-\frac{1}{\frac{50}{365}}\ln \frac{8112}{8149.01}\approx 0.0432$$
The implied dividend yield is $4.32\%$.

## 4
There is a backwardation. Investors might expect the value of DJIA will decrease later, or at least the level of increase will be lower than the dividend it will pay out. 

# Q6
## 1
$$F_{0,T}=S_{0}e^{r-r*}=130\times e^{(1\%-2\%)\times \frac{9}{12}}\approx \$129.03$$

## 2
The USD balance in six month is
$$2000000+F_{0,6mth}\times 8 \times 125000=\$3293500$$
The EUR balance in six month is
$$1000000-8\times 125000=0$$



