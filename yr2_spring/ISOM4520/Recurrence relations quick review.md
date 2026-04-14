## Recurrence relations quick review

> [!abstract]
> In this course, the most important recursions are usually **first-order linear recursions**.  
> The key idea is:
>
> > turn the recursion into a geometric recursion whenever possible.
>
> This section is a quick reference for recognizing common recursions, solving them, and understanding their long-run behavior.

---

### 1. What is a recursion?

A recursion defines the current term using previous terms.

Example:

$$
a_n = 2a_{n-1}+1
$$

So instead of writing a direct formula for $a_n$, we describe how the sequence evolves step by step.

Typical goals:

1. find a closed-form formula,
2. determine whether the sequence converges,
3. find the long-run limit or steady state.

---

### 2. Geometric recursion

This is the most basic case.

#### Form

$$
a_n = c a_{n-1}
$$

#### Solution

Repeated substitution gives

$$
a_n = c^n a_0.
$$

#### Long-run behavior

- if $|c|<1$, then $a_n\to 0$
- if $c=1$, then $a_n=a_0$
- if $c=-1$, then $a_n$ oscillates
- if $|c|>1$, then $a_n$ diverges

> [!tip]
> This is the simplest recursion. Many other recursions are solved by reducing them to this one.

---

### 3. First-order linear recursion

This is the most important case in this course.

#### Form

$$
a_n = b + c a_{n-1}
$$

Examples in econometrics and finance:

- AR(1)-type dynamics
- volatility forecast recursion
- mean-reverting processes

---

### 4. Fixed point / long-run mean

To find the long-run mean, suppose the sequence converges to a constant $a^*$.

Then both $a_n$ and $a_{n-1}$ approach the same value, so substitute:

$$
a^* = b + c a^*.
$$

Solve:

$$
a^*(1-c)=b
$$

so

$$
a^*=\frac{b}{1-c}, \qquad c\neq 1.
$$

This $a^*$ is called the:

- fixed point,
- steady state,
- long-run mean,
- equilibrium.

> [!important]
> The long-run mean is found by setting “current value = previous value”.

---

### 5. Turning it into a geometric recursion

This is the key trick.

Define the deviation from the long-run mean:

$$
u_n := a_n-a^*.
$$

Then:

$$
u_n = a_n-a^*
$$

and using

$$
a_n=b+ca_{n-1}, \qquad a^*=b+ca^*,
$$

subtract the two equations:

$$
a_n-a^* = c(a_{n-1}-a^*).
$$

So

$$
u_n = c u_{n-1}.
$$

Now it becomes a geometric recursion.

Hence

$$
u_n = c^n u_0.
$$

Substitute back:

$$
a_n = a^* + c^n(a_0-a^*).
$$

Since

$$
a^*=\frac{b}{1-c},
$$

we get the closed-form solution:

$$
a_n = \frac{b}{1-c} + c^n\left(a_0-\frac{b}{1-c}\right).
$$

---

### 6. Long-run behavior of first-order linear recursions

For

$$
a_n = b + c a_{n-1},
$$

the long-run behavior depends on $|c|$.

#### If $|c|<1$

Then

$$
c^n \to 0,
$$

so

$$
a_n \to a^* = \frac{b}{1-c}.
$$

So the sequence converges to the fixed point.

#### If $|c|>1$

Then $c^n$ grows in magnitude, so the sequence usually diverges.

#### If $c=1$

Then the recursion becomes

$$
a_n = a_{n-1}+b,
$$

so the sequence usually grows linearly.

#### If $c=-1$

Then the sequence usually oscillates.

> [!summary]
> For first-order linear recursions, convergence is determined by whether $|c|<1$.

---

### 7. Alternative method: repeated substitution

Another way to solve

$$
a_n = b + c a_{n-1}
$$

is to expand repeatedly:

$$
a_n = b + c(b + c a_{n-2})
$$

$$
a_n = b + cb + c^2 a_{n-2}
$$

Continuing:

$$
a_n = b + cb + c^2b + \cdots + c^{n-1}b + c^n a_0.
$$

So

$$
a_n = b(1+c+c^2+\cdots+c^{n-1}) + c^n a_0.
$$

Using the geometric sum formula,

$$
1+c+\cdots+c^{n-1} = \frac{1-c^n}{1-c},
$$

we obtain

$$
a_n = \frac{b(1-c^n)}{1-c} + c^n a_0.
$$

This is the same solution as before.

> [!note]
> Both methods are correct:
> - fixed-point method is more intuitive,
> - repeated substitution is more mechanical.

---

### 8. Second-order linear recursion

This is less central in this course, but it is a common class of recursions.

#### Form

$$
a_n = p a_{n-1} + q a_{n-2}
$$

Example: Fibonacci numbers

$$
F_n = F_{n-1}+F_{n-2}.
$$

#### Standard method

Guess a solution of the form

$$
a_n = r^n.
$$

Substitute:

$$
r^n = p r^{n-1} + q r^{n-2}.
$$

Divide by $r^{n-2}$:

$$
r^2 = pr + q.
$$

So the characteristic equation is

$$
r^2 - pr - q = 0.
$$

Then solve for the roots.

#### Typical outcomes

- two distinct real roots:  
  $$
  a_n = A r_1^n + B r_2^n
  $$
- repeated root $r$:  
  $$
  a_n = (A+Bn)r^n
  $$

> [!tip]
> For second-order linear homogeneous recursions, think “characteristic equation”.

---

### 9. How to recognize common recursion types quickly

#### Case 1

If you see

$$
a_n = c a_{n-1},
$$

think:

- geometric recursion,
- solution $a_n=c^n a_0$.

---

#### Case 2

If you see

$$
a_n = b + c a_{n-1},
$$

think:

- first-order linear recursion,
- find fixed point,
- subtract fixed point,
- reduce to geometric recursion.

Template:

$$
a^*=\frac{b}{1-c},
$$

$$
a_n=a^*+c^n(a_0-a^*).
$$

---

#### Case 3

If you see

$$
a_n = p a_{n-1} + q a_{n-2},
$$

think:

- second-order linear homogeneous recursion,
- use characteristic equation.

---

#### Case 4

If you see a conditional expectation recursion such as

$$
m_k = a + b m_{k-1},
$$

do not be intimidated by the notation.

Once the conditioning time is fixed, this is still just an ordinary first-order recursion in $k$.

---

### 10. Example: GARCH variance forecast recursion

A key recursion in this course is

$$
m_k = (1-\alpha-\beta)\sigma^2 + (\alpha+\beta)m_{k-1},
$$

where

$$
m_k := E_{t-1}(\sigma_{t+k}^2).
$$

This is exactly of the form

$$
a_n = b + c a_{n-1}
$$

with

$$
b=(1-\alpha-\beta)\sigma^2,
\qquad
c=\alpha+\beta.
$$

#### Step 1: find the fixed point

$$
m^*=\frac{(1-\alpha-\beta)\sigma^2}{1-(\alpha+\beta)}=\sigma^2.
$$

#### Step 2: write the solution

$$
m_k = \sigma^2 + (\alpha+\beta)^k(m_0-\sigma^2).
$$

Since

$$
m_0 = E_{t-1}(\sigma_t^2)=\sigma_t^2,
$$

we get

$$
m_k = \sigma^2 + (\alpha+\beta)^k(\sigma_t^2-\sigma^2).
$$

Equivalently,

$$
m_k = \big(1-(\alpha+\beta)^k\big)\sigma^2 + (\alpha+\beta)^k \sigma_t^2.
$$

> [!summary]
> GARCH forecast recursion says:
>
> - current volatility matters in the short run,
> - but its influence decays geometrically,
> - and the forecast converges to the long-run variance.

---

### 11. Intuition behind mean reversion

For

$$
a_n = b + c a_{n-1},
$$

after subtracting the steady state $a^*$, we get

$$
a_n-a^* = c(a_{n-1}-a^*).
$$

So the deviation from the long-run mean is multiplied by $c$ each period.

- if $|c|<1$, the deviation shrinks,
- if $|c|>1$, the deviation grows,
- if $c<0$, the deviation alternates sign.

> [!important]
> Mean reversion means “the gap from the long-run mean decays over time”.

---

### 12. One-line memory template

> [!summary]
> For
>
> $$
> a_n=b+ca_{n-1},
> $$
>
> remember:
>
> - fixed point:
>   $$
>   a^*=\frac{b}{1-c}
>   $$
> - solution:
>   $$
>   a_n=a^*+c^n(a_0-a^*)
>   $$
> - convergence:
>   $$
>   |c|<1
>   $$

---

### 13. Mini practice problems

#### Practice 1

Solve and find the limit:

$$
a_n = 0.8 a_{n-1}+2.
$$

#### Practice 2

Solve and find the limit:

$$
a_n = -0.5 a_{n-1}+3.
$$

#### Practice 3

Rewrite in “long-run mean + decaying deviation” form:

$$
m_k = 0.1 + 0.9 m_{k-1}.
$$

> [!tip]
> If you can do these three quickly, your recursion intuition is back.

---

### 14. Key takeaway

> [!summary]
> The most useful recursion skill in this course is:
>
> 1. recognize a first-order linear recursion,
> 2. find the fixed point,
> 3. subtract the fixed point,
> 4. reduce the problem to a geometric recursion.
>
> This is exactly the logic behind the GARCH volatility forecast formula.