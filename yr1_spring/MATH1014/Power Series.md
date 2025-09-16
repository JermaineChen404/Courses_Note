## Definition
A power series is a function defined by
$$
f(x)=\sum_{k=0}^{+\infty}c_{k}(x-a)^k
$$
## Natural Domain
- Must be an **interval** since if $f(x+r)$ converges, $f(x)$ converges absolutely for every $x$ with $|x-a|<|r|$, and vice versa. i.e. one continuous interval that is symmetric to the center.
- There exists a number $R\in[0,\infty]$ (**radius of convergence**)such that $f(x)$ converges absolutely if $|x-a|<R$, and vice versa. i.e., $f(x)$ converges at worst at **center $a$**.
- To find the radius, use ratio test (weaker) or root test (**stronger**). When $R=0$ or $R=\infty$ use root test. $$R=\frac{1}{\lim_{ n \to \infty } \sqrt[n]{ |c_{n}| }}=\lim_{ n \to \infty }|\frac{c_{n}}{c_{n+1}}|$$
- End points have to be checked separately. Ratio test and Root test are no longer helpful.
## Properties
### Term wise derivative and integration of Power Series