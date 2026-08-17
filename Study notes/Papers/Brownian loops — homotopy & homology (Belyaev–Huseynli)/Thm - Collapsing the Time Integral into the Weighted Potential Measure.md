---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Constr - The Weighted Potential Measure Vϕ"
  - "Def - Subordinator and Subordination of a Semigroup"
tags: [paper, probability, subordination]
---

# Notation

- $\phi$ — a [[Def - Bernstein Function and the Lévy–Khintchine Representation|Bernstein function]] satisfying [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)|Assumption 2.3]]; $\psi^\phi_t$ its subordinator law at time $t$
- $p^{\mathcal{E}}(s,x,y)$ — the base transition density; $p^\phi(t,x,y)=\int_{[0,\infty)}p^{\mathcal{E}}(s,x,y)\,\psi^\phi_t(\mathrm{d}s)$ the subordinate one, equation (4)
- $V_\phi$ — the [[Constr - The Weighted Potential Measure Vϕ|weighted potential measure]] on $(0,\infty)$, defined by (7)
- $h$ — a non-negative measurable test function on $(0,\infty)$

---

# Type card

> [!abstract] Type card — Lemma 2.11
> **Given.** A Bernstein function $\phi$ satisfying [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)|Assumption 2.3]]; the base transition density $p^{\mathcal{E}}$ of a regular symmetric [[Def - Dirichlet Form and the Hunt Process Correspondence|Dirichlet form]]; the [[Def - Subordinator and Subordination of a Semigroup|subordination formula]] (4) for $p^\phi$; and the [[Constr - The Weighted Potential Measure Vϕ|weighted potential measure]] $V_\phi$.
>
> **Produces.** An identity between two integrals, valid for all $x,y\in X$ as an equality in $[0,\infty]$ — both sides may be infinite, and no integrability hypothesis is needed.
>
> **Lets you.** Perform the collapse in one step wherever a $\mathrm{d}t/t$ integral meets a subordinated kernel. This is the workhorse of both [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]] and [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds|Theorem 7.2]], and it is invoked in both with the same structure: discharge the spatial integral first, call the result $h(s)$, then apply this lemma to that $h$.

---

# Statement

> **Lemma 2.11.** For all $x,y\in X$,
> $$\int_0^\infty\frac{\mathrm{d}t}{t}\,p^\phi(t,x,y) \;=\; \int_{(0,\infty)} p^{\mathcal{E}}(s,x,y)\,V_\phi(\mathrm{d}s).\tag{8}$$

---

# Why it is true

The lemma says nothing that Definition 2.9 has not already said; its content is that Definition 2.9 was the right definition to have made.

Look at what the left-hand side is. Substituting (4), it is a double integral in $(t,s)$ of the product of two factors: $p^{\mathcal{E}}(s,x,y)$, which depends on $s$ and the two spatial points but *not on $t$*; and $\psi^\phi_t(\mathrm{d}s)\,\mathrm{d}t/t$, which is a measure on the pair $(t,s)$ carrying all the information about $\phi$. Since $t$ appears in only one of the two factors, integrating it out first costs nothing and produces a measure in $s$ alone — and that measure is $V_\phi$ by definition.

**The mechanism in one line: $t$ is a dummy variable of the subordination and appears nowhere in the geometry, so it can always be integrated out first, and $V_\phi$ is the name of the result.**

The only thing to check is that exchanging the order of integration is legal, and it is, for the simplest possible reason: every quantity in sight is non-negative, so Tonelli applies with no integrability hypothesis whatever. This is why the identity holds as an equality in $[0,\infty]$ rather than under a convergence assumption — both sides are simultaneously finite or infinite, and downstream, when finiteness matters, it is established separately.

---

# Strategy

**Strategy.** Substitute the subordination formula (4) for $p^\phi$; exchange the two integrals by Tonelli, legitimate because the integrand is non-negative; then read off the result from Definition 2.9 with $h(s)=p^{\mathcal{E}}(s,x,y)$.

> [!note]- Proof (skippable)
> Fix $x,y\in X$. By the subordination formula (4),
> $$\int_0^\infty\frac{\mathrm{d}t}{t}\,p^\phi(t,x,y) = \int_0^\infty\frac{\mathrm{d}t}{t}\int_{(0,\infty)}p^{\mathcal{E}}(s,x,y)\,\psi^\phi_t(\mathrm{d}s),$$
> where the inner integral runs over $(0,\infty)$ rather than $[0,\infty)$ because [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)|Assumption 2.3]] gives $\psi^\phi_t(\{0\})=0$, so discarding the origin discards no mass.
>
> The integrand $(t,s)\mapsto p^{\mathcal{E}}(s,x,y)$ is non-negative and jointly measurable — joint measurability of $p^{\mathcal{E}}$ is part of the standing hypothesis on the Dirichlet form, and $(t,s)\mapsto\psi^\phi_t(\mathrm{d}s)\,\mathrm{d}t/t$ is a $\sigma$-finite product-type kernel. Tonelli therefore applies with no further condition.
>
> Taking $h(s)=p^{\mathcal{E}}(s,x,y)$ in the defining relation (7) of $V_\phi$,
> $$\int_0^\infty\frac{\mathrm{d}t}{t}\int_{(0,\infty)}h(s)\,\psi^\phi_t(\mathrm{d}s) = \int_{(0,\infty)}h(s)\,V_\phi(\mathrm{d}s),$$
> which is (8). $\;\square$

---

# What this assumes, and where to climb

Three hypotheses, all of them cheap, and it is worth being clear about which does what.

**Assumption 2.3**, via [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)]]. Two jobs. It is why $p^\phi$ exists at all — without a transition density there is no left-hand side. And it is why the integral over $(0,\infty)$ loses nothing: $\psi^\phi_t(\{0\})=0$. Without it the subordinate semigroup has an atom on the diagonal and neither side of (8) is well posed.

**The subordination formula (4)**, via [[Def - Subordinator and Subordination of a Semigroup]]. This is where the independence of the subordinator from the base process is used; a non-independent clock would not give the semigroup as a plain average against $\psi^\phi_t$.

**Definition 2.9**, via [[Constr - The Weighted Potential Measure Vϕ]]. The definition of $V_\phi$ is stated by its action on test functions precisely so that this proof is one substitution.

Notably **not** assumed: any finiteness. The lemma is an identity in $[0,\infty]$. When Theorem 3.5 applies it, finiteness of the resulting expression is a separate matter, settled in §4 by [[Thm - Finiteness of the Total Mass|Corollary 4.7]].

---

# What consumes this

- [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]] — applied with $h(s)=\frac{e^{-s/4}e^{-L^2/(4s)}}{2\sqrt{\pi s}}$, the output of the Wang–Xue identity, to collapse (22) into (21)
- [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds|Theorem 7.2]] — applied with $h(s)=\frac{2se^{-s}}{(4\pi s)^{3/2}}e^{-(m\ell_\gamma)^2/4s}$, the output of the $\mathbb{H}^3$ slab identity
- [[§2.3–2.4 Subordination and the Weighted Potential Measure]] — the section page states it as the section's payoff

The pattern in both consumers is identical and is worth naming as a move rather than a fact. **Trigger:** a $\mathrm{d}t/t$ integral standing in front of a subordinated kernel, with the spatial integral already discharged. **Action:** name the discharged spatial integral $h(s)$ and collapse.

---

# Reading it against the rest of the paper

The technique — collapsing a time integral against a subordinator law into a single potential measure — is Schilling–Song–Vondraček's, cited to Chapter 5 of *Bernstein functions*. What is specific to this paper is the weight: the classical potential measure of a subordinator uses $\mathrm{d}t$, and here the weight is the Haar measure $\mathrm{d}t/t$ forced by the loop-measure construction. That single change is what makes $V_\phi(\mathrm{d}s)=\mathrm{d}s/s$ in the Brownian case rather than Lebesgue measure, and hence what produces the scale-invariance obstruction discussed on [[Constr - The Weighted Potential Measure Vϕ]].
