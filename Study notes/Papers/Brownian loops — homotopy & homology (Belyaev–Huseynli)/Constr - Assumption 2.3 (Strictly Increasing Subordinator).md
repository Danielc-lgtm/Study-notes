---
type: construction
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Bernstein Function and the Lévy–Khintchine Representation"
  - "Def - Subordinator and Subordination of a Semigroup"
tags: [paper, probability, subordination]
---

# Notation

- $\phi$ — a [[Def - Bernstein Function and the Lévy–Khintchine Representation|Bernstein function]] with Lévy–Khintchine triple $(a,b,\nu)$: $a\geq0$ killing rate, $b\geq0$ drift, $\nu$ the Lévy measure on $(0,\infty)$
- $S_t$ — the associated subordinator; $\psi^\phi_t$ its law on $[0,\infty)$
- $p^\phi(t,x,y)$ — the subordinate transition density, whose existence is what this assumption buys

---

# In plain language

The assumption says: **the clock has actually moved by time $t$, for every $t>0$, almost surely.** Nothing more.

Stated on the triple it reads $b>0$ or $\nu(0,\infty)=\infty$ — either the clock has a drift, so it advances continuously, or it has infinitely many jumps in any interval, so it advances by jumping. Stated on the process it reads $S_t>0$ almost surely for every $t>0$. Stated on the law it reads $\psi^\phi_t(\{0\})=0$: no atom at the origin.

The reason to care is entirely about densities. If $\psi^\phi_t$ has an atom of mass $c$ at $s=0$, then the subordination formula $p^\phi(t,x,y)=\int_{[0,\infty)}p^{\mathcal{E}}(s,x,y)\,\psi^\phi_t(\mathrm{d}s)$ picks up a term $c\cdot p^{\mathcal{E}}(0,x,y)$ — and $p^{\mathcal{E}}(0,\cdot,\cdot)$ is a delta function, not a density. Concretely, the subordinate semigroup at time $t$ has an atom of size $c$ sitting on the diagonal: with probability $c$ the process has not moved at all. A semigroup with an atomic part has no transition density with respect to $\mathrm{vol}_g$, so $p^\phi$ does not exist and **every formula in the paper from §2.4 onwards has no left-hand side.**

The processes this excludes are exactly the compound Poisson subordinators: finite $\nu$, no drift, so the clock sits still between jumps and $\psi^\phi_t(\{0\}) = e^{-\nu(0,\infty)t} > 0$.

---

# The construction

> **Assumption 2.3.** Throughout the paper it is assumed that
> $$b>0\qquad\text{or}\qquad\nu(0,\infty)=\infty;$$
> equivalently, that $S_t>0$ almost surely for every $t>0$, so that $\psi^\phi_t(\{0\})=0$. This excludes compound Poisson subordinators, whose semigroups do not admit a transition density.

The equivalence of the three formulations is standard subordinator theory. In one direction: if $b>0$ then $S_t\geq bt>0$ deterministically; if $\nu(0,\infty)=\infty$ then the number of jumps in $[0,t]$ is Poisson with infinite mean, so almost surely there is at least one, and jumps are positive. In the other: if $b=0$ and $\nu(0,\infty)<\infty$, then the process is a killed compound Poisson process, which is at $0$ until its first jump, an event of positive probability at every fixed $t$.

Note that the assumption says nothing about $a$. Killing is permitted — indeed the killing case $\phi(\lambda)=\lambda+\kappa$ has $a=\kappa>0$ and satisfies the assumption via $b=1>0$. A killed subordinator has $|\psi^\phi_t|=e^{-at}<1$, but its mass is still supported away from the origin, and the loss of total mass is exactly the factor $e^{-\kappa t}$ that turns up in the transition density.

---

# Type card

> [!abstract] Type card — Assumption 2.3
> **Given.** A Bernstein function $\phi$ with triple $(a,b,\nu)$.
>
> **Produces.** The standing hypothesis $b>0$ or $\nu(0,\infty)=\infty$; equivalently $S_t>0$ almost surely for all $t>0$; equivalently $\psi^\phi_t(\{0\})=0$. A condition, not an object.
>
> **Lets you.** Assume the subordinate semigroup admits a transition density $p^\phi(t,x,y)$ against $\mathrm{vol}_g$ — which every formula from §2.4 onwards uses without further comment. It is exactly what excludes compound Poisson subordinators.

---

# Properties relied on later

**Existence of the subordinate density.** The single consequence, and the reason the assumption exists. Every one of the following depends on it: the subordination formula (4) as an identity between densities; the definition of the subordinate loop measure via bridge measures of mass $p^\phi(t,x,y)$; and the whole of §3, since the periodisation of §3 is a sum of kernel values and there is nothing to sum without a kernel.

**All four of the paper's examples satisfy it, for two different reasons.** Brownian motion, killing, and both stable cases: the first two by $b=1>0$, the last two by $\nu_\alpha(0,\infty)=\infty$ (the density $\frac{\alpha/2}{\Gamma(1-\alpha/2)}s^{-1-\alpha/2}$ is not integrable at $0$). So the assumption is never a live constraint in the paper — it is a hypothesis stated once so that the general theorems are true as stated.

---

# Consumed by

- [[Constr - The Subordinate Brownian Loop Measure]] — needs $p^\phi$ to exist in order for the bridge measures to have the stated mass
- [[Constr - The Weighted Potential Measure Vϕ]] — Definition 2.9 is stated under the assumption
- [[Thm - Collapsing the Time Integral into the Weighted Potential Measure|Lemma 2.11]] — both sides of the identity are integrals of densities
- [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]] — quoted verbatim in the hypotheses
- [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds|Theorem 7.2]] — the same, via "any of the Bernstein functions considered in this paper"
- [[Thm - Poissonian Structure of Homotopy Classes|Proposition 3.8]] — quoted in the hypotheses

---

# Where this sits in my DAG

Reduces one step to [[Def - Bernstein Function and the Lévy–Khintchine Representation]] and [[Def - Subordinator and Subordination of a Semigroup]], and from there to anchors: Lévy processes, Poisson jump counts and the existence of transition densities are all *Advanced Probability / Measure-Theoretic* (🟢) and *SDEs* (🟢). The equivalence of the three formulations is standard and is quoted from Schilling–Song–Vondraček.
