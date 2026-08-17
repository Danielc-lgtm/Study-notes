---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Primitive Hyperbolic Element and Translation Length"
  - "Def - Critical Exponent"
tags: [paper, spectral-theory, zeta-functions]
---

# Signature

| symbol | type |
|---|---|
| $X=\Gamma\backslash\mathbb{H}^2$ | geometrically finite hyperbolic surface |
| $\mathcal{P}_X$ | the set of **primitive** closed geodesics / primitive hyperbolic conjugacy classes |
| $\ell_\gamma$ | $\in(0,\infty)$, the translation length of $\gamma\in\mathcal{P}_X$ |
| $\delta$ | $\in(0,1]$ — the [[Def - Critical Exponent\|critical exponent]] of $\Gamma$ |
| $Z_X$ | $\{\mathrm{Re}(s)>\delta\}\to\mathbb{C}$, extended meromorphically to $\mathbb{C}$ |
| $s$ | $\in\mathbb{C}$; in this paper $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ |

---

# Definition

> **Definition 4.1 (Selberg zeta function).**
> $$Z_X(s):=\prod_{\gamma\in\mathcal{P}_X}\prod_{k=0}^{\infty}\Big(1-e^{-(s+k)\ell_\gamma}\Big),\qquad\mathrm{Re}(s)>\delta.\tag{31}$$
> A **double** Euler product: outer over primitive geodesics, inner over $k\geq0$.

> **(F1) Logarithmic expansion — the identity the paper actually uses.** For $\mathrm{Re}(s)>\delta$,
> $$-\log Z_X(s)=\sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^{\infty}\frac1m\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}.\tag{32}$$
> *Derivation:* $-\log(1-x)=\sum_{m\geq1}x^m/m$ applied to each factor, then the inner geometric series $\sum_{k\geq0}e^{-(s+k)m\ell_\gamma}=\dfrac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}$.
>
> **(F2) Convergence.** Absolute for $\mathrm{Re}(s)>\delta$; **divergent** at $s=\delta$. As $s\downarrow\delta$, $-\log Z_X(s)\uparrow\infty$, hence $Z_X(s)\to0$.
>
> **(F3) Continuation.** $Z_X$ extends meromorphically to $\mathbb{C}$ — quoted, see [[Ext - Meromorphic Continuation of the Selberg Zeta and L-Functions|(MC)]].
>
> **(F4) Bosonic reading (Remark 4.4).** Put $Z_\gamma(s):=\prod_{k\geq0}\big(1-e^{-(s+k)\ell_\gamma}\big)^{-1}$ and $Z(s):=\prod_\gamma Z_\gamma(s)=Z_X(s)^{-1}$. Each $Z_\gamma$ is the partition function of bosonic modes indexed by $k\geq0$ with weights $(s+k)\ell_\gamma$; $Z$ is the grand canonical partition function of a free Bose gas at zero chemical potential.

---

# Type card

> [!abstract] Type card — $Z_X$
> **Given.** **(H1)** $X=\Gamma\backslash\mathbb{H}^2$ geometrically finite. **(H2)** $\mathrm{Re}(s)>\delta$.
>
> **Produces.** A number $Z_X(s)\in\mathbb{C}^\times$; equivalently, via (F1), the number $-\log Z_X(s)\in(0,\infty)$.
>
> **Lets you.** Recognise the double sum $\sum_{\gamma,m}\frac1m\frac{e^{(1-s)L}}{e^L-1}$ — which is **exactly** the total loop mass of [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Thm 3.5]] — as a single closed-form object. Every identity of §4 is (F1) read backwards.

---

# Depends on

- [[Def - Primitive Hyperbolic Element and Translation Length]] — the index set $\mathcal{P}_X$ and $\ell_\gamma$
- [[Def - Critical Exponent]] — the abscissa $\delta$
- [[Ext - Meromorphic Continuation of the Selberg Zeta and L-Functions]] — (F3)
- 🟢 Euler products, $-\log(1-x)$ expansion, geometric series — *Complex Analysis*, elementary

---

# Checks

**Instance.** $X$ a closed hyperbolic surface: $\delta=1$, (31) converges for $\mathrm{Re}(s)>1$, and (32) at $s=1$ diverges — consistently with [[Thm - Finiteness of the Total Mass|Cor 4.7]], where the Brownian total mass on a finite-area surface is infinite.

**Instance.** $X$ of infinite area: $\delta<1$, so $s=1$ lies in the half-plane of convergence and $\sum_{\gamma,m}\mu_X(\mathcal{C}_X(\gamma^m))=-\log Z_X(1)<\infty$.

**Non-instance (fails F2).** $s=\delta$. Every factor of (31) is still defined, but the product does not converge absolutely and (32) diverges. **Consequence:** the finiteness statement of §4.2 is *strict*: $s>\delta$, not $s\geq\delta$.

**Non-instance (fails H1).** $\Gamma$ with elliptic or parabolic elements taken as "primitive": (31) indexes only the **hyperbolic** primitive classes. A parabolic $\tau$ has $\ell_\tau=0$ and the factor $1-e^{-(s+k)\cdot0}=0$ would kill the product. This is why peripheral classes are excluded throughout — see [[Def - Geometrically Finite Surfaces, Cusps and Funnels]].

---

# Used at

- [[Thm - Selberg Zeta Criterion]] — (F1) is the right-hand side to be matched
- [[Thm - Selberg Zeta Identity (Killing Case)]] — $\sum_{\gamma,m}\mu^\kappa_X=-\log Z_X(s)$
- [[Def - Ruelle Zeta Function and its Twist]] — $R_X(s)=Z_X(s)/Z_X(s+1)$
- [[Thm - Finiteness of the Total Mass]] — (F2) at $s\downarrow\delta$
- [[Constr - The Probability Measure on Free Homotopy Classes]] — $-\log Z_X(s)$ is the normalising constant
- [[Def - Selberg L-Function]] — $Z_X$ is the trivial-character case

---

# Commentary

> [!note]- Commentary (skippable)
> Almost everything in §4 is the single observation that (32) and the §3.1.2 mass formula are the **same expression**. Theorem 3.5 gives $\mu^\kappa_X(\mathcal{C}_X(\gamma^m))=\frac1m\frac{e^{(1-s)L}}{e^L-1}$ with $L=m\ell_\gamma$; (F1) says the sum of exactly those numbers over all $(\gamma,m)$ is $-\log Z_X(s)$. No analysis is required to see it, only the two geometric-series expansions. The work was done in §3, where the mass was computed; §4 recognises the answer.
>
> Why the *double* product. The outer product over $\gamma$ is the Euler product proper — primitive geodesics are the primes. The inner product over $k$ is what makes $Z_X$, rather than the Ruelle zeta $R_X$, the function with good spectral properties: its zeros sit at $s_j=\tfrac12\pm\sqrt{\tfrac14-\lambda_j}$, one for each Laplace eigenvalue. That is the Selberg trace formula's doing, and it is why §5 can express $\log\det\Delta_X$ through $Z_X$.
>
> (F4) is not used anywhere but is a good sanity anchor: $-\log Z_X(s)$ is a *free energy*, the total mass is a sum of independent mode contributions, and the Poissonian independence of [[Thm - Poissonian Structure of Homotopy Classes|Prop 3.8]] is the probabilistic shadow of "non-interacting".
