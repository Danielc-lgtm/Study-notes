---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Constr - The Probability Measure on Free Homotopy Classes"
  - "Def - Selberg Zeta Function"
tags: [paper, probability, zeta-functions]
---

# Signature

| symbol | type |
|---|---|
| $F$ | $F(s):=-\log Z_X(s)$, defined and positive for $s>\delta$ |
| $L$ | the random variable $L(\gamma,m)=m\ell_\gamma$ under $\mathbb{P}_s$ |
| $\mathbb{E}_s,\mathrm{Var}_s$ | expectation and variance under $\mathbb{P}_s$ |
| $r$ | $>1-s$ — the tilting parameter in the Laplace transform |
| $n$ | $\geq1$, the moment order; $F^{(n)}$ the $n$-th derivative |

---

# Type card

> [!abstract] Type card — §6.1 moment formulas
> **Given.**
> **(H1)** $\kappa>0$, $s=\tfrac12+\sqrt{\tfrac14+\kappa}>\delta$, $\mathbb{P}_s$ as constructed.
> **(H2)** $F(s)=-\log Z_X(s)$, real-analytic on $(\delta,\infty)$.
>
> **Produces.** Four identities:
> $$\mathbb{E}_s\big[e^{-rL}\big]=\frac{\log Z_X(s+r)}{\log Z_X(s)}\ \ (r>1-s);\qquad \mathbb{E}_s\big[L^n\big]=\frac{(-1)^nF^{(n)}(s)}{F(s)};$$
> $$\mathbb{E}_s[L]=-\frac{\mathrm{d}}{\mathrm{d}s}\log F(s)=-\frac{Z_X'(s)}{Z_X(s)\log Z_X(s)};\qquad \mathrm{Var}_s(L)=\frac{\mathrm{d}^2}{\mathrm{d}s^2}\log F(s).$$
>
> **Lets you.** Compute **every** moment of the geodesic length of a random class by differentiating one zeta function. No summation over classes is ever performed.

---

# Statement

> **§6.1 (moments).** Assume (H1),(H2).
> **(a) Derivative of the weight.** $\dfrac{\mathrm{d}}{\mathrm{d}s}\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big)=-(m\ell_\gamma)\,\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big)$. (69)
> **(b) Laplace transform = shift.** For $r>1-s$,
> $$\mathbb{E}_s\big[e^{-rL}\big]=\frac{-\log Z_X(s+r)}{-\log Z_X(s)}=\frac{\log Z_X(s+r)}{\log Z_X(s)}.\tag{70}$$
> **(c) All moments.** $\displaystyle\mathbb{E}_s\big[L^n\big]=\frac{(-1)^nF^{(n)}(s)}{F(s)}$, $n\geq1$. (71)
> **(d) Cumulants.** $\mathbb{E}_s[L]=-\dfrac{F'(s)}{F(s)}$ (72) and $\mathrm{Var}_s(L)=\dfrac{F''F-(F')^2}{F^2}$ (73).
> **(e) Monotonicity.** $\log F$ is strictly convex on $(1,\infty)$, hence $s\mapsto\mathbb{E}_s[L]$ is **strictly decreasing**: increasing the killing rate shortens the typical class.

---

# Discharges

| result | applied to | returns |
|---|---|---|
| [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces\|(26)]] | $\partial_s$ of $e^{(1-s)m\ell_\gamma}$ | (69): $\partial_s\mu^\kappa_X=-L\mu^\kappa_X$ |
| **the same weight at parameter $s+r$** | $\mu^\kappa_X(\mathcal{C}_X(\gamma^m))e^{-rm\ell_\gamma}$ | is *exactly* the weight at $s+r$ — giving (70) |
| [[Thm - Selberg Zeta Identity (Killing Case)\|Cor 4.3]] | numerator and denominator of (70) | both are $-\log Z_X$ at the respective parameters |
| (69) iterated $n$ times | $\sum_{\gamma,m}\mu^\kappa_X L^n$ | $=(-1)^nF^{(n)}(s)$, giving (71) |
| $\mathrm{Var}=\mathbb{E}[L^2]-\mathbb{E}[L]^2$ | (71) at $n=1,2$ | (73), i.e. $(\log F)''$ |
| Cauchy–Schwarz / strict positivity of $\mathrm{Var}_s(L)$ | (73) | strict convexity of $\log F$, hence (e) |

---

# Proof

**Strategy.** One observation does all the work: **shifting the spectral parameter is the same as exponentially tilting by the length**, because the weight depends on $s$ only through $e^{(1-s)L}$.

> [!note]- Proof (skippable)
> **(a)** $\mu^\kappa_X(\mathcal{C}_X(\gamma^m))=\frac1m\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}$ depends on $s$ only through $e^{(1-s)m\ell_\gamma}$; differentiating gives (69).
>
> **(b)** Multiplying the summand at parameter $s$ by $e^{-rm\ell_\gamma}$ produces exactly the summand at parameter $s+r$. Hence
> $$\mathbb{E}_s\big[e^{-rL}\big]=\frac{\sum_{\gamma,m}\mu^\kappa_X(\mathcal{C}_X(\gamma^m))e^{-rm\ell_\gamma}}{-\log Z_X(s)}=\frac{-\log Z_X(s+r)}{-\log Z_X(s)},$$
> convergent for $s+r>\delta$, i.e. $r>\delta-s$; the stated $r>1-s$ suffices since $\delta\leq1$.
>
> **(c)** Iterating (69), $\sum_{\gamma,m}\mu^\kappa_X(\mathcal{C}_X(\gamma^m))(m\ell_\gamma)^n=(-1)^nF^{(n)}(s)$; dividing by $F(s)$ gives (71).
>
> **(d)** $n=1$ gives (72); $\mathrm{Var}_s(L)=\mathbb{E}_s[L^2]-\mathbb{E}_s[L]^2=\frac{F''}{F}-\frac{(F')^2}{F^2}=(\log F)''$, which is (73). Substituting $F=-\log Z_X$, $F'=-Z_X'/Z_X$ gives the explicit forms
> $$\mathbb{E}_s[L]=-\frac{Z_X'(s)}{Z_X(s)\log Z_X(s)},\qquad \mathrm{Var}_s(L)=\frac{\big(Z_XZ_X''-(Z_X')^2\big)\log Z_X-(Z_X')^2}{Z_X^2\log^2Z_X}.$$
>
> **(e)** $(\log F)''=\mathrm{Var}_s(L)>0$ since $L$ is non-constant, so $\log F$ is strictly convex and $\mathbb{E}_s[L]=-(\log F)'$ is strictly decreasing. $\;\square$

---

# What this assumes, and where to climb

- **Differentiation under the sum** — legitimate on $(\delta,\infty)$, where the series converges absolutely and locally uniformly. Not stated separately in the paper.
- **The closed form (26)** — [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces]]. The tilting identity (b) works *only* because $s$ enters the weight through a single exponential in $L$; for a general subordinator it would fail.
- **$Z_X$ real and positive on $(\delta,\infty)$** — so $\log Z_X$ and its derivatives are real; from the Euler product, since each factor $1-e^{-(s+k)\ell_\gamma}\in(0,1)$.
- **Not assumed:** any continuation of $Z_X$. Everything happens inside the region of absolute convergence.

---

# Consumed by

- [[Thm - Concentration on Systolic Classes]] — (e) is the monotone statement its $s\to\infty$ limit sharpens
- [[§6 Probability Measures on Homotopy and Homology Classes]] §6.1

---

# Commentary

> [!note]- Commentary (skippable)
> **The mechanism in one line: the spectral parameter $s$ and the length $L$ are conjugate — shifting one is tilting by the other — so the moment generating function is the partition function at a shifted argument.** That is (70), and (71)–(73) are its derivatives at $r=0$.
>
> This is the standard structure of a Gibbs measure with $s$ playing the role of inverse temperature and $L$ the energy: $\log F$ is the free energy, its first derivative the mean energy, its second the variance, and convexity is the statement that the variance is non-negative. The unusual feature is that the partition function is not an abstract sum but $-\log Z_X(s)$, so "free energy" is a concrete analytic object whose derivatives are $Z_X'/Z_X$ — a logarithmic derivative of a Selberg zeta function, the same quantity that appears in explicit formulas for geodesic counting.
>
> (e) is the physically obvious statement made precise: raising the killing rate makes long loops rarer, so the typical class shortens. Its proof is one line and its content is entirely in the identification $\mathrm{Var}=(\log F)''$.
