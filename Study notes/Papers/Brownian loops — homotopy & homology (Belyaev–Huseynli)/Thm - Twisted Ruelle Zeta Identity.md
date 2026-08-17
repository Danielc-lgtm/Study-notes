---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Ruelle Zeta Function and its Twist"
  - "Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces"
tags: [paper, zeta-functions, loop-measures]
---

# Signature

| symbol | type |
|---|---|
| $\kappa_-$ | $\kappa_-(s):=s(s-1)$; then $\tfrac12+\sqrt{\tfrac14+\kappa_-(s)}=s$ |
| $\kappa_+$ | $\kappa_+(s):=s(s+1)$; then $\tfrac12+\sqrt{\tfrac14+\kappa_+(s)}=s+1$ |
| $\rho$ | $\Gamma\to\mathrm{GL}(V_\rho)$ finite-dimensional; $c_\rho$ its abscissa |
| $\tau$ | representative of the primitive class of $\gamma$; $\mathrm{tr}\,\rho(\tau^m)$ is a class function |
| $L$ | $=m\ell_\gamma$ |

> **Convention.** $\mathrm{Re}(s)>\tfrac12$ ensures the **principal** square root gives $s$ and $s+1$ respectively; for $\mathrm{Re}(s)\leq\tfrac12$ the branch flips and the two lines below are false.

---

# Type card

> [!abstract] Type card — Corollary 4.6
> **Given.**
> **(H1)** $\rho:\Gamma\to\mathrm{GL}(V_\rho)$ finite-dimensional complex, abscissa $c_\rho$.
> **(H2)** $\mathrm{Re}(s)>\max(c_\rho,\tfrac12)$.
> **(H3)** $\kappa_\pm(s)$ as above, so that $s(\kappa_-)=s$ and $s(\kappa_+)=s+1$.
>
> **Produces.**
> $$-\log R_X(s,\rho)=\sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^{\infty}\mathrm{tr}\,\rho(\tau^m)\Big[\mu^{\kappa_-(s)}_X\big(\mathcal{C}_X(\gamma^m)\big)-\mu^{\kappa_+(s)}_X\big(\mathcal{C}_X(\gamma^m)\big)\Big]=\sum_{\gamma,m}\frac{\mathrm{tr}\,\rho(\tau^m)e^{-sm\ell_\gamma}}{m}.\tag{39}$$
>
> **Lets you.** Read a *dynamical* zeta function as a **difference of two loop measures at different killing rates**. Passing from $\kappa_-$ to $\kappa_+$ suppresses long loops more strongly, and the difference isolates each class's net contribution between the two rates.

---

# Statement

> **Corollary 4.6 (twisted Ruelle zeta identity).** Assume (H1)–(H3). Then (39) holds, absolutely convergent.

---

# Discharges

| result | applied to | returns |
|---|---|---|
| [[Def - Ruelle Zeta Function and its Twist\|(F4)]] | $\log$ of the product (38) | $-\log R_X(s,\rho)=\sum_{\gamma,m}\mathrm{tr}\,\rho(\tau^m)e^{-smL}/m$ |
| [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces\|(26)]] | $\kappa=\kappa_-(s)$ | $\mu^{\kappa_-}_X(\mathcal{C}_X(\gamma^m))=\frac1m\frac{e^{(1-s)L}}{e^L-1}$ |
| [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces\|(26)]] | $\kappa=\kappa_+(s)$ | $\mu^{\kappa_+}_X(\mathcal{C}_X(\gamma^m))=\frac1m\frac{e^{-sL}}{e^L-1}$ |
| algebra: $e^{(1-s)L}-e^{-sL}=e^{-sL}(e^L-1)$ | the difference | $\frac{e^{-sL}}{m}$ — the summand above |
| [[Def - Ruelle Zeta Function and its Twist\|c_ρ]] | the double sum | absolute convergence for $\mathrm{Re}(s)>\max(c_\rho,\tfrac12)$ |

---

# Proof

**Strategy.** Expand $-\log\det$; then observe that the *difference* of the two mass formulas telescopes the denominator $e^L-1$ away.

> [!note]- Proof (skippable)
> Expanding $-\log\det(I-M)=\sum_{m\geq1}\mathrm{tr}(M^m)/m$ with $M=\rho(\tau)e^{-s\ell_\gamma}$ gives the second equality of (39). For the first, by (26),
> $$\mu^{\kappa_-(s)}_X\big(\mathcal{C}_X(\gamma^m)\big)-\mu^{\kappa_+(s)}_X\big(\mathcal{C}_X(\gamma^m)\big)=\frac1m\cdot\frac{e^{(1-s)L}-e^{-sL}}{e^L-1}=\frac{e^{-sL}}{m},$$
> since $e^{(1-s)L}-e^{-sL}=e^{-sL}(e^L-1)$. Matching term by term gives (39). Absolute convergence follows from that of the product (38). $\;\square$

---

# What this assumes, and where to climb

- **The branch condition (H2).** $\mathrm{Re}(s)>\tfrac12$ is what makes $\tfrac12+\sqrt{\tfrac14+s(s-1)}=s$ rather than $1-s$. This is a statement about the **principal** square root, and it is the only place in §4 where the branch matters.
- **$\kappa_+(s)=s(s+1)\geq0$ and $\kappa_-(s)=s(s-1)$** — both admissible killing rates in the sense of §3.1.2, and $\kappa_-\geq-\tfrac14$ automatically since $s(s-1)\geq-\tfrac14$ for real $s$.
- **The mass formula (26)** — [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces]], hence the §3 stack.
- **Not assumed:** unitarity of $\rho$. That only improves $c_\rho$ to $\delta$.

---

# Consumed by

- [[§4 Zeta Identities and Finiteness of the Total Mass]] §4.1.2
- Nothing else. The paper states explicitly that these identities are "more difficult to use in a meaningful way", and does not use them again. The analogous *unitary character* identity that §6 does use is built on $Z_X$, not $R_X$ — see [[Def - Selberg L-Function]].

---

# Commentary

> [!note]- Commentary (skippable)
> The mechanism in one line: **the Selberg zeta matches a single loop measure because its Euler factor carries the $1/(e^L-1)$; the Ruelle zeta lacks that factor, so it needs a difference of two loop measures to cancel it.**
>
> The cancellation is exact and slightly magical on first sight — $e^{(1-s)L}-e^{-sL}=e^{-sL}(e^L-1)$ is a one-line identity, but it says that the two killing rates $s(s-1)$ and $s(s+1)$ are precisely the pair whose spectral parameters differ by $1$, which is precisely the shift appearing in the inner product $\prod_k$ of $Z_X$. The relation $R_X(s)=Z_X(s)/Z_X(s+1)$ of [[Def - Ruelle Zeta Function and its Twist|(F2)]] is the same fact at the level of the zeta functions rather than their logarithms.
>
> The paper's own assessment is worth taking at face value. The identity is correct and cheap, but the difference $\mu^{\kappa_-}_X-\mu^{\kappa_+}_X$ is a signed quantity: it is not a measure, cannot be normalised, and carries no probabilistic interpretation. That is why §6 goes back to $Z_X$ and builds the $L$-function there.
