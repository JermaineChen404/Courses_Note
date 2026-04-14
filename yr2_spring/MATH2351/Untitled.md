# Second Order Linear ODEs: Theory & Constant Coefficients

## Overview
These notes connect the **constant coefficient** method (characteristic equation) with the **general theory** (Wronskian, fundamental sets, existence/uniqueness). The key insight: the characteristic equation provides explicit solutions; the general theory guarantees these form a *fundamental set* and thus generate **all** solutions.

---

## 1. Constant Coefficient Case
Consider  
$$
a y'' + b y' + c y = 0,\quad a,b,c \in \mathbb{R}.
$$

### 1.1 Characteristic Equation
Substitute $y = e^{rt}$:
$$
a r^2 + b r + c = 0.
$$
Roots $r_1, r_2$ (real or complex).

### 1.2 Superposition Principle
If $y_1, y_2$ are solutions, then any linear combination  
$$
y = c_1 y_1 + c_2 y_2
$$
is also a solution.

### 1.3 Distinct Real Roots
$r_1 \neq r_2$ real → two solutions $e^{r_1 t}, e^{r_2 t}$.  
At this stage we know they are solutions, but not yet that **every** solution is a linear combination.

### 1.4 Complex Roots
$r_{1,2} = \lambda \pm i\mu$ ($\mu \neq 0$).  
Complex exponentials give real solutions via Euler:
$$
e^{\lambda t}\cos\mu t,\quad e^{\lambda t}\sin\mu t.
$$
These also satisfy superposition. The **phase‑shift** form is:
$$
y = C e^{\lambda t}\cos(\mu t + \phi).
$$

---

## 2. General Theory (Continuous Coefficients)

We now consider the general second order linear homogeneous ODE:
$$
y'' + p(t)y' + q(t)y = 0,
$$
where $p,q$ are continuous on an open interval $I$.

### 2.1 Existence & Uniqueness
> **Theorem**  
> For any $t_0 \in I$ and any initial values $y_0, y_0'$, there exists a unique solution defined on $I$.

### 2.2 Wronskian
For two functions $y_1, y_2$:
$$
W(y_1,y_2)(t) = \begin{vmatrix} y_1 & y_2 \\ y_1' & y_2' \end{vmatrix}.
$$

### 2.3 Fundamental Set & General Solution
If $y_1, y_2$ are solutions and $W(y_1,y_2)(t_0) \neq 0$ for some $t_0 \in I$, then:
- Every solution can be written uniquely as $c_1 y_1 + c_2 y_2$.
- $\{y_1, y_2\}$ is called a **fundamental set of solutions**.

**Why “every solution”?**  
Given any solution $\phi(t)$, consider its initial values at $t_0$. The nonzero Wronskian guarantees we can solve for $c_1, c_2$ so that $c_1 y_1 + c_2 y_2$ matches those initial values. By uniqueness, $\phi(t) = c_1 y_1 + c_2 y_2$ for all $t$.

### 2.4 Existence of a Fundamental Set
Choose $y_1, y_2$ as the unique solutions satisfying:
$$
\begin{cases}
y_1(t_0)=1,\ y_1'(t_0)=0 \\[2pt]
y_2(t_0)=0,\ y_2'(t_0)=1
\end{cases}
$$
Then $W(y_1,y_2)(t_0)=1$, so they form a fundamental set.

### 2.5 Abel’s Formula
For any two solutions $y_1, y_2$:
$$
W(y_1,y_2)(t) = W(y_1,y_2)(t_0)\;\exp\!\left(-\int_{t_0}^{t} p(s)\,ds\right).
$$
Consequences:
- Either $W(t) \equiv 0$ or $W(t) \neq 0$ for **all** $t \in I$.
- $W(t) \neq 0$ ⇔ $y_1, y_2$ are linearly independent.

### 2.6 Linear Independence
$y_1, y_2$ are linearly independent on $I$ iff  
$$
c_1 y_1(t) + c_2 y_2(t) = 0 \ \forall t \ \Rightarrow\ c_1 = c_2 = 0.
$$
For solutions of the ODE, this is equivalent to $W(t) \neq 0$ (and hence equivalent to being a fundamental set).

---

## 3. Connecting Constant Coefficients to the General Theory

| Constant Coefficient Case | General Theory Interpretation |
|---------------------------|--------------------------------|
| Characteristic roots $r_1, r_2$ distinct (real or complex) | The two solutions $e^{r_1 t}, e^{r_2 t}$ (or their real forms) have nonzero Wronskian → they form a fundamental set. |
| Superposition principle | Special case of the linearity of $L(y)$. |
| General solution $c_1 e^{r_1 t} + c_2 e^{r_2 t}$ | The fundamental set **spans** the solution space (dimension 2). |

**Example**: $y'' + 5y' + 6y = 0$  
$r_1 = -2, r_2 = -3$,  
$W = (-2 + 3)e^{-5t} = e^{-5t} \neq 0$ → $\{e^{-2t}, e^{-3t}\}$ is a fundamental set.

**Complex example**: $y'' + y = 0$  
$r = \pm i$, real solutions $\cos t, \sin t$  
$W = 1 \neq 0$ → fundamental set.

---

## 4. Logical Flow Diagram (Mermaid)

```mermaid 
flowchart TD
  A[Constant Coeff. ODE] --> B[Guess y = e^{rt}]
  B --> C[Characteristic equation]
  C --> D[Two solutions y1, y2]
  D --> E[Superposition: linear combos are solutions]
  
  F[General Theory] --> G[Wronskian]
  G --> H[If W != 0, every solution = linear combo]
  H --> I[{y1, y2} is fundamental set]
  D --> G
  I --> J[Abel's formula]
  J --> K[W = 0 everywhere or never zero]
  K --> L[W != 0 iff linear independent]
  
  style A fill:#f9f,stroke:#333
  style F fill:#ccf,stroke:#333
  ```