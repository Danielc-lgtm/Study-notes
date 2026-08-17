---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Selberg L-Function"
  - "Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces"
tags: [paper, zeta-functions, loop-measures]
---

# Signature

| symbol | type |
|---|---|
| $\chi$ | $H_1(X,\mathbb{Z})\to S^1$ unitary |
| $s$ | $=\tfrac12+\sqrt{\tfrac14+\kappa}$, $\mathrm{Re}(s)>\delta$ |
| $\mu^\kappa_X(\mathcal{C}_X(\gamma^m))$ | $=\frac1m\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}$ |

---

# Type card

> [!abstract] Type card — Corollary 6.4
> **Given.**
> **(H1)** $\chi\in\widehat{H_1(X,\mathbb{Z})}$ unitary.
> **(H2)** $\kappa\geq-\tfrac14$, $s=\tfrac12+\sqrt{\tfrac14+\kappa}$, $\mathrm{Re}(s)>\delta$.
>
> **Produces.**
> $$-\log L_X(s,\chi)=\sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^{\infty}\chi([\gamma])^m\,\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big)=\sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^{\infty}\frac1m\cdot\frac{\chi([\gamma])^m\,e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}.\tag{76}$$
>
> **Lets you.** Read $-\log L_X(s,\chi)$ as the **$\chi$-twisted total loop mass**. Setting $\chi\equiv1$ recovers [[Thm - Selberg Zeta Identity (Killing Case)|Cor 4.3]]; letting $\chi$ vary gives the Fourier transform of the homology-class masses.

---

# Statement

> **Corollary 6.4 (Selberg $L$-function identity).** Assume (H1),(H2). Then (76) holds, absolutely convergent.

---

# Discharges

| result | applied to | returns |
|---|---|---|
| [[Def - Selberg L-Function\|(F2)]] | $\lvert\chi\rvert\equiv1$ | $\lvert z\rvert=e^{-(\mathrm{Re}(s)+k)\ell_\gamma}<1$, so term-by-term logarithms are legitimate |
| $-\log(1-z)=\sum_{m\geq1}z^m/m$ | $z=\chi([\gamma])e^{-(s+k)\ell_\gamma}$ | $\sum_m\frac{\chi([\gamma])^m}{m}e^{-(s+k)m\ell_\gamma}$ |
| geometric series in $k$ | $\sum_{k\geq0}e^{-(s+k)m\ell_\gamma}$ | $\dfrac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}$ |
| [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces\|(26)]] | that expression | $m\,\mu^\kappa_X(\mathcal{C}_X(\gamma^m))$, giving (76) |
| [[Def - Critical Exponent\|$\mathrm{Re}(s)>\delta$]] | the double sum | absolute convergence |

---

# Proof

**Strategy.** Identical to [[Def - Selberg Zeta Function|(F1)]] for $Z_X$, with the extra factor $\chi([\gamma])^m$ carried along; unitarity is what keeps every $\lvert z\rvert<1$.

> [!note]- Proof (skippable)
> For $\mathrm{Re}(s)>\delta$ the Euler product (75) converges absolutely, so one may take logarithms term by term and expand each factor with $-\log(1-z)=\sum_{m\geq1}z^m/m$, valid since $\lvert z\rvert=\lvert\chi([\gamma])\rvert e^{-(\mathrm{Re}(s)+k)\ell_\gamma}=e^{-(\mathrm{Re}(s)+k)\ell_\gamma}<1$ by unitarity. Summing over $k\geq0$,
> $$\sum_{k\geq0}e^{-(s+k)m\ell_\gamma}=\frac{e^{-sm\ell_\gamma}}{1-e^{-m\ell_\gamma}}=\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1},$$
> and the resulting summand is $\frac{\chi([\gamma])^m}{m}\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}=\chi([\gamma])^m\mu^\kappa_X(\mathcal{C}_X(\gamma^m))$ by (26). $\;\square$

---

# What this assumes, and where to climb

- **Unitarity of $\chi$** — the only hypothesis doing work. Without it the expansion is invalid where $\lvert z\rvert\geq1$, and the abscissa moves; cf. [[Def - Ruelle Zeta Function and its Twist|$c_\rho$]].
- **The mass formula (26)** — [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces]], hence the §3 stack. Without it (76) is a statement about $L$-functions with no probabilistic content.
- **$\mathrm{Re}(s)>\delta$** — [[Def - Critical Exponent]]; for convergence only, not for the term-by-term identity.
- **Not assumed:** any continuation of $L_X$. Everything is inside the Euler-product region.

---

# Consumed by

- [[Thm - Fourier Expansion and Inversion by Homology Class]] — regroups (76) by homology class
- [[Thm - Distribution of the Total Homology of the Loop Soup]] — applied to $\chi$ **and** to the trivial character, giving the ratio $Z_X/L_X$
- [[Constr - The Mass in a Homology Class]] — (76) is its generating function
- [[§6 Probability Measures on Homotopy and Homology Classes]] §6.2

---

# Commentary

> [!note]- Commentary (skippable)
> The corollary is Corollary 4.3 with a character inserted, and the proof is the same two geometric-series expansions. Its value is entirely in what it makes possible downstream: because the twist $\chi([\gamma])^m$ depends on $(\gamma,m)$ **only through the homology class $m[\gamma]$**, the double sum can be regrouped by homology without disturbing the weights. That is Theorem 6.5, and it is why the $L$-function is the right generating object rather than an ornament.
>
> Read as Fourier analysis: (76) says that the function $\chi\mapsto-\log L_X(s,\chi)$ on the character torus has Fourier coefficients $\mu^\kappa_X(\beta)$ on $H_1(X,\mathbb{Z})$. Everything else in §6.2–§6.3 is an application of inversion — including Proposition 6.7, where the exponential formula for the loop soup produces $(Z_X/L_X)^\lambda$ and the same inversion extracts $\mathbb{P}(\beta(\lambda)=\beta)$.
