---
type: definition
subject: measure-theory
prereqs:
  - "Def - Measure and Measure Space"
  - "Def - Absolute Continuity and Density"
tags: [analysis, measure-theory]
---

# Notation

$(X,\mathcal{A})$ a measurable space; $\mu,\nu$ measures (or signed measures) on it. $\mu\perp\nu$ — $\mu$ and $\nu$ are mutually singular.

---

# Axiom Motivation

[[Def - Absolute Continuity and Density|Absolute continuity]] $\nu\ll\mu$ describes one extreme of how two measures can relate: $\nu$ is "spread over the same places as $\mu$," every $\mu$-null set is $\nu$-null, and $\nu$ has a density. **Mutual singularity** $\mu\perp\nu$ is the *opposite* extreme: $\mu$ and $\nu$ live on *disjoint* parts of the space — there is a set carrying all of $\mu$ and none of $\nu$, and its complement carries all of $\nu$ and none of $\mu$. They are "as far apart as measures can be."

Why name this extreme? Because of the dichotomy it sets up. Given two measures, neither relation need hold — but the [[Thm - Radon-Nikodym Theorem|Lebesgue decomposition theorem]] says that, relative to a reference measure $\mu$, *any* $\sigma$-finite $\nu$ splits uniquely as $\nu=\nu_{ac}+\nu_s$ with $\nu_{ac}\ll\mu$ and $\nu_s\perp\mu$. Every measure is, canonically, an absolutely continuous part plus a singular part. Mutual singularity is one of the two poles this decomposition is built around; without naming it, the decomposition cannot even be stated.

The everyday example fixes intuition: the [[Def - Lebesgue Measure|Lebesgue measure]] $\lambda$ and a Dirac point mass $\delta_x$ are mutually singular — $\lambda$ ignores the point $\{x\}$ (it is $\lambda$-null) while $\delta_x$ is *concentrated* there. A point mass has no density with respect to $\lambda$ precisely because it is singular to it.

---

# The Definition

Two measures $\mu,\nu$ on $(X,\mathcal{A})$ are **mutually singular**, written $\mu\perp\nu$, if there exists $A\in\mathcal{A}$ with
$$\mu(A)=0\qquad\text{and}\qquad\nu(A^c)=0.$$
Equivalently, $\nu$ is **concentrated** on $A^c$ and $\mu$ on $A$: each measure assigns all its mass to a set the other ignores. The relation is symmetric, and one also says "$\mu$ is singular with respect to $\nu$."

A measure $\nu$ on $\mathbb{R}^n$ is itself called **singular** (with respect to Lebesgue measure) if $\nu\perp\lambda$.

---

# Relate to Other Fields / Compression

Mutual singularity is the measure-theoretic form of *disjoint supports* — $\mu$ and $\nu$ are like functions supported on disjoint sets, or like orthogonal vectors. Indeed in the Banach space of signed measures with the total-variation norm, $\mu\perp\nu$ implies $\|\mu+\nu\|=\|\mu\|+\|\nu\|$, the "orthogonal" additivity of norms. In probability, a *continuous* law (with a density) and a *discrete* law (atoms) are mutually singular; the [[Thm - Radon-Nikodym Theorem|Lebesgue decomposition]] of a distribution into absolutely continuous $+$ singular-continuous $+$ atomic parts is the classification of distribution types. The Cantor measure is the classic *singular-continuous* example — singular to $\lambda$, yet atomless.

---

# Examples / Corollaries

**$\delta_x\perp\lambda$.** Take $A=\{x\}$: $\lambda(A)=0$ and $\delta_x(A^c)=0$. A point mass is singular to Lebesgue measure — which is *why* it has no Lebesgue density.

**Counting measure on $\mathbb{Q}$ vs. $\lambda$.** Take $A=\mathbb{Q}$: $\lambda(\mathbb{Q})=0$, and counting measure restricted to $\mathbb{Q}$ gives the complement measure $0$. Mutually singular.

**The Cantor measure** (uniform on the [[Ex - The Cantor set has Lebesgue measure zero|Cantor set]]) is singular to $\lambda$ (concentrated on a $\lambda$-null set) yet has no atoms — *singular continuous*.

Non-example: a measure $\nu=f\lambda$ with density $f>0$ a.e. is *not* singular to $\lambda$ — it is the opposite, $\nu\ll\lambda$.

Calibration: (i) Can a measure be both $\ll\mu$ and $\perp\mu$? Only if it is the zero measure (it would have to vanish on $A$ and on $A^c$). (ii) Is $\perp$ symmetric? Yes. (iii) Are two measures always comparable by $\ll$ or $\perp$? No — generically neither holds, which is why one needs the *decomposition*.

---

# Unlocked by This

> [!tip] Lebesgue decomposition
> Every $\sigma$-finite $\nu$ splits uniquely as $\nu=\nu_{ac}+\nu_s$ with $\nu_{ac}\ll\mu$ and $\nu_s\perp\mu$ — the absolutely continuous and singular parts. See [[Thm - Radon-Nikodym Theorem]].
