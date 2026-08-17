---
type: construction
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Bernstein Function"
  - "Def - Subordinator"
tags: [paper, probability, subordination]
---

# Signature

| symbol | type |
|---|---|
| $\phi$ | [[Def - Bernstein Function\|Bernstein function]] with triple $(a,b,\nu)$ |
| $b$ | $\in[0,\infty)$ — the drift |
| $\nu$ | measure on $(0,\infty)$ with $\int(1\wedge s)\,\nu(\mathrm{d}s)<\infty$; $\nu(0,\infty)\in[0,\infty]$ |
| $S_t$ | the subordinator; $\psi^\phi_t$ its law on $[0,\infty)$ |
| $p^\phi$ | the subordinate transition density against $\operatorname{vol}_g$ — exists **iff** (A2.3) |

---

# Construction

> **Assumption 2.3 (A2.3).** Throughout the paper,
> $$\boxed{\ b>0\quad\text{or}\quad\nu(0,\infty)=\infty.\ }$$
> Equivalently:
> **(A2.3a)** $b>0$ or $\nu(0,\infty)=\infty$;
> **(A2.3b)** $S_t>0$ almost surely for every $t>0$;
> **(A2.3c)** $\psi^\phi_t(\{0\})=0$ for every $t>0$.
>
> This **excludes** compound Poisson subordinators ($b=0$, $\nu(0,\infty)<\infty$), whose semigroups admit no transition density.

> [!note]- Equivalence of (a), (b), (c) (skippable)
> **(a) $\Rightarrow$ (b).** If $b>0$ then $S_t\geq bt>0$ deterministically. If $\nu(0,\infty)=\infty$ then the number of jumps in $[0,t]$ is Poisson with mean $t\,\nu(0,\infty)=\infty$, so a.s. at least one occurs, and jumps are strictly positive.
> **(b) $\Leftrightarrow$ (c).** $\psi^\phi_t(\{0\})=\mathbb{P}(S_t=0)$.
> **(¬a) $\Rightarrow$ (¬c).** If $b=0$ and $\nu(0,\infty)<\infty$, $S$ is a (killed) compound Poisson process, at $0$ until its first jump, so $\psi^\phi_t(\{0\})=e^{-(a+\nu(0,\infty))t}>0$.

**Note on $a$.** (A2.3) says nothing about the killing rate. Killing is permitted: $\phi(\lambda)=\lambda+\kappa$ has $a=\kappa>0$ and satisfies (A2.3) via $b=1>0$. A killed subordinator has $\lvert\psi^\phi_t\rvert=e^{-at}<1$, but its mass is still supported away from the origin.

---

# Type card

> [!abstract] Type card — (A2.3)
> **Given.** **(H1)** $\phi$ Bernstein with triple $(a,b,\nu)$.
>
> **Produces.** A proposition about $(b,\nu)$ — not an object. When true: $\psi^\phi_t(\{0\})=0$, hence by [[Ext - Phillips Subordination of Semigroups and Dirichlet Forms|(PH)(C3)]] the subordinate semigroup admits a transition density $p^\phi$ satisfying (4).
>
> **Lets you.** Write $p^\phi$ at all. Every formula from §2.4 onward has $p^\phi$ on one side, so without (A2.3) they have no left-hand side.

---

# Depends on

- [[Def - Bernstein Function]] — the triple
- [[Def - Subordinator]] — the law $\psi^\phi_t$
- [[Ext - Lévy–Khintchine Representation for Bernstein Functions]] — the equivalence proof uses the jump structure
- [[Ext - Phillips Subordination of Semigroups and Dirichlet Forms]] — (C3) is what (A2.3) unlocks

---

# Properties

**(P1) Existence of $p^\phi$.** The single consequence, and the reason (A2.3) exists. Consumed by: the definition of $\mu^\phi_X$ via bridges of mass $p^\phi(t,x,y)$; the periodisation of §3, which sums kernel values; and every mass formula.

**(P2) All four of the paper's $\phi$ satisfy it — for two different reasons.**

| $\phi(\lambda)$ | $(a,b,\nu)$ | (A2.3) via |
|---|---|---|
| $\lambda$ | $(0,1,0)$ | $b=1>0$ |
| $\lambda+\kappa$ | $(\kappa,1,0)$ | $b=1>0$ |
| $\lambda^{\alpha/2}$ | $(0,0,\nu_\alpha)$ | $\nu_\alpha(0,\infty)=\infty$ |
| $(\lambda+\kappa)^{\alpha/2}$ | composition | $\nu(0,\infty)=\infty$ |

So (A2.3) is never a live constraint in the paper; it is stated once so the general theorems are true as stated.

---

# Consumed by

- [[Constr - The Subordinate Brownian Loop Measure]] — needs $p^\phi$ for the bridges
- [[Constr - The Weighted Potential Measure Vϕ]] — Definition 2.9 integrates over $(0,\infty)$ rather than $[0,\infty)$, discarding no mass precisely by (A2.3c)
- [[Thm - Collapsing the Time Integral into the Weighted Potential Measure]] — both sides are integrals of densities
- [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces]] — quoted as (H1)
- [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds]] — via "any of the Bernstein functions considered in this paper"
- [[Thm - Poissonian Structure of Homotopy Classes]] — quoted as (H1)

---

# Commentary

> [!note]- Commentary (skippable)
> In one sentence: **the clock has actually moved by time $t$, for every $t>0$, almost surely.** Either it drifts ($b>0$) or it jumps infinitely often ($\nu(0,\infty)=\infty$).
>
> Why an atom at $0$ is fatal: (4) reads $p^\phi(t,x,y)=\int_{[0,\infty)}p^{\mathcal{E}}(s,x,y)\,\psi^\phi_t(\mathrm{d}s)$, and an atom of mass $c$ at $s=0$ contributes $c\cdot p^{\mathcal{E}}(0,x,y)$ — but $p^{\mathcal{E}}(0,\cdot,\cdot)$ is $\delta_x$, not a function. Concretely, with probability $c$ the process has not moved, so the semigroup has an atomic part on the diagonal, and a semigroup with an atomic part has no density against $\operatorname{vol}_g$.
