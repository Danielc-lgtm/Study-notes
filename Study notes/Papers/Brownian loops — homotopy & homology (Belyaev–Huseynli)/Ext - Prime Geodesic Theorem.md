---
type: external
paper: "BH26"
subject: brownian-loops
tags: [paper, external, spectral-theory, hyperbolic-geometry]
---

# Signature

| symbol | type |
|---|---|
| $N_X$ | $[0,\infty)\to\mathbb{Z}_{\geq0}$, $N_X(R):=\#\{\gamma\in\mathcal{P}_X:\ell_\gamma\leq R\}$ — a counting function |
| $\delta$ | $\in(0,1]$ — the [[Def - Critical Exponent\|critical exponent]] |
| $\mathrm{Li}$ | $\mathrm{Li}(x)=\int_2^x\frac{\mathrm{d}t}{\log t}\sim x/\log x$ |
| $\lambda_j$ | eigenvalues of $\Delta_X$ in $(0,\tfrac14]$; $s_j:=\tfrac12+\sqrt{\tfrac14-\lambda_j}\in[\tfrac12,1)$ |

---

# Statement

> **(PGT) Prime geodesic theorem.** *Precondition:* **(P1)** $X$ geometrically finite hyperbolic surface with critical exponent $\delta$. *Conclusion:*
> $$N_X(R)\ \sim\ \frac{e^{\delta R}}{\delta R}\qquad(R\to\infty).\tag{40}$$

> **(PGT$'$) Refined form, closed surfaces.** *Additional precondition:* **(P2)** $X$ **closed** (so $\delta=1$). *Conclusion:*
> $$N_X(R)=\mathrm{Li}(e^{R})+\sum_{0<\lambda_j\leq1/4}\mathrm{Li}\big(e^{s_jR}\big)+O_X\!\big(e^{3R/4}/R\big).\tag{43}$$

> **(F1) Finiteness.** $N_X(R)<\infty$ for every $R$. Hence $\ell_\gamma\to\infty$ along $\mathcal{P}_X$ (only finitely many geodesics below any bound), which is what licenses the asymptotic $-\log(1-x)=x+O(x^2)$ in §4.2 Step 1.
>
> **(F2) The comparison it is used for.** $\sum_{\gamma\in\mathcal{P}_X}e^{-s\ell_\gamma}<\infty\iff s>\delta$, by Stieltjes integration against $N_X$.

---

# Type card

> [!abstract] Type card — (PGT)
> **Given.** (P1) — and (P2) additionally for the refined form (43).
>
> **Produces.** An asymptotic for $N_X(R)$, of type "function $\sim$ function as $R\to\infty$" with an explicit error term in (43).
>
> **Lets you.** Convert **any** sum over $\mathcal{P}_X$ of a decaying function of $\ell_\gamma$ into a one-dimensional integral $\int^\infty e^{-sR}\,\mathrm{d}N_X(R)$, and decide its convergence. Used exactly twice: (40) in [[Thm - Finiteness of the Total Mass|Cor 4.7]], (43) in §5.1 via Naud's formula.

---

# Status

- **Proved here:** no.
- **Source:** Huber, Selberg (compact case); Lalley, Naud, Patterson–Perry (geometrically finite / infinite area). The refined form (43) is standard and is the input Naud uses.
- **DAG node that would close this:** 🔵 *Automorphic Forms / Selberg Trace Formula* (non-anchor). **This is a genuine gap**: (PGT) is proved from the Selberg trace formula, which this note-set imports rather than develops.
- **What is safe to assume:** (40),(43),(F1),(F2). Note that (40) alone does **not** decide the boundary case $s=\delta$ — the $1/R$ factor does, and §4.2 uses it explicitly.
- **Scope:** (40) in Corollary 4.7 only; (43) in §5.1 only, and there only through [[Ext - Naud's Formula for the Log-Determinant|(N)]]. A reader who accepts (N) never needs (43).

> [!warning] The $1/(\delta R)$ is load-bearing
> With $N_X(R)\asymp e^{\delta R}$ alone, the integral $\int^\infty e^{-(s-\delta)R}\,\mathrm{d}R$ would be inconclusive at $s=\delta$. With the $1/R$, the tail integrand is $e^{-(s-\delta)R}/R$, which **diverges** at $s=\delta$ like $\int^\infty\mathrm{d}R/R$. That is how §4.2 gets a strict inequality rather than a non-strict one.

---

# Used at

- [[Thm - Finiteness of the Total Mass]] — (40),(F1),(F2)
- [[Def - Critical Exponent]] — (F5) there is (40) here
- [[Ext - Naud's Formula for the Log-Determinant]] — (43) is its input
- [[§4 Zeta Identities and Finiteness of the Total Mass]] §4.2

---

# Commentary

> [!note]- Commentary (skippable)
> The analogy the name advertises is exact enough to be useful: primitive closed geodesics play the role of primes, $\ell_\gamma$ plays the role of $\log p$, and (40) with $\delta=1$ is $\pi(x)\sim x/\log x$ after the substitution $x=e^R$. The refined form (43) is the analogue of the explicit formula, with **small Laplace eigenvalues in place of zeta zeros** — each $\lambda_j\in(0,\tfrac14]$ contributing a term $\mathrm{Li}(e^{s_jR})$ of lower order than the main term but larger than the error.
>
> That correspondence is the reason $Z_X$ rather than $R_X$ is the well-behaved zeta function: the zeros of $Z_X$ sit at the $s_j$, so (43) *is* the Selberg zeta's explicit formula. In this paper the connection is used in one direction only — as an input to convergence estimates — but it is the same mechanism that makes §5 possible.
