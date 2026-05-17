---
type: definition
subject: measure-theory
prereqs:
  - "Def - Interval and Elementary Figure"
  - "Def - Borel σ-Algebra"
  - "Thm - Hahn-Carathéodory Extension Theorem"
  - "Thm - Uniqueness of the Hahn-Carathéodory Extension"
tags: [analysis, measure-theory, probability]
---

# Notation

$\lambda$ (or $\lambda_n$, or $\mathrm{d}x$) is Lebesgue measure on $\mathbb{R}^n$. $\mathcal{B}(\mathbb{R}^n)$ is the [[Def - Borel σ-Algebra|Borel $\sigma$-algebra]]; $\mathcal{B}^*(\mathbb{R}^n)$ its [[Def - Null Set and Completion|completion]], the Lebesgue $\sigma$-algebra. $\widetilde\lambda$ is [[Def - Interval and Elementary Figure|elementary volume]].

---

# Axiom Motivation

We want one canonical measure on $\mathbb{R}^n$ that deserves the name "volume." The desiderata are short and non-negotiable: (i) a box gets its elementary volume $\prod(b_k-a_k)$; (ii) it is **translation-invariant** — moving a set does not change its size; (iii) it is defined on at least all Borel sets, with countable additivity, so that limits behave.

These desiderata *over-determine* the measure — and that is the point. By the [[Thm - Uniqueness of the Hahn-Carathéodory Extension|uniqueness theorem]], (i) + countable additivity already pin down a *unique* measure on $\mathcal{B}(\mathbb{R}^n)$; translation invariance then comes out as a *theorem*, not an extra axiom, and conversely Lebesgue measure is the *unique* translation-invariant Borel measure normalised by $\lambda([0,1]^n)=1$. So "Lebesgue measure" is not a choice; it is forced.

The construction is the [[Thm - Hahn-Carathéodory Extension Theorem|extension machine]] run on the cleanest possible input: the [[Def - Pre-Measure|pre-measure]] $\widetilde\lambda$ on the algebra of [[Def - Interval and Elementary Figure|elementary figures]]. Existence is the extension theorem; uniqueness is its companion ($\widetilde\lambda$ is $\sigma$-finite — tile $\mathbb{R}^n$ by unit cubes). The one place geometry secretly enters an otherwise topology-free machine is the verification that $\widetilde\lambda$ *is* a pre-measure, which needs the Heine–Borel compactness of closed boxes.

Why bother, given the Riemann integral already integrates over boxes? Because Riemann's theory measures only "Jordan-measurable" sets — sets whose boundary is negligible — and that class is not a $\sigma$-algebra: $\mathbb{Q}\cap[0,1]$ is not Jordan-measurable. Lebesgue measure assigns it size $0$, makes the class of measurable sets a genuine $\sigma$-algebra, and thereby makes the [[Thm - Dominated Convergence Theorem|convergence theorems]] possible.

---

# The Definition

**Lebesgue measure** $\lambda$ on $\mathbb{R}^n$ is the [[Thm - Hahn-Carathéodory Extension Theorem|Hahn–Carathéodory extension]] of the [[Def - Interval and Elementary Figure|elementary-volume pre-measure]] $\widetilde\lambda$. Concretely:

- $\widetilde\lambda$ is a pre-measure on the algebra $\mathcal{A}$ of elementary figures (a theorem, by Heine–Borel);
- $\widetilde\lambda$ is $\sigma$-finite ($\mathbb{R}^n=\bigsqcup_{z\in\mathbb{Z}^n}(z,z+\mathbf 1]$, each cube of volume $1$);
- the extension theorem produces a measure $\mu^*|_\Sigma$ on the [[Def - Carathéodory Measurable Sets|Carathéodory $\sigma$-algebra]] $\Sigma$, with $\mathcal{B}(\mathbb{R}^n)\subseteq\Sigma$;
- by uniqueness this extension is the *only* measure on $\mathcal{B}(\mathbb{R}^n)$ agreeing with $\widetilde\lambda$ on boxes.

We call $\lambda=\mu^*|_{\mathcal{B}(\mathbb{R}^n)}$ Lebesgue measure. The full $\Sigma$ is the **Lebesgue $\sigma$-algebra** $\mathcal{B}^*(\mathbb{R}^n)$, the [[Def - Null Set and Completion|completion]] of $\mathcal{B}(\mathbb{R}^n)$; a set in it is **Lebesgue-measurable**. Restricting $\lambda$ to a Borel set $A$ gives the **Lebesgue measure on $A$**; for $A=[0,1]^n$ this is a probability measure, the **uniform distribution**.

---

# Categorical Definition

Among all Borel measures on $\mathbb{R}^n$, Lebesgue measure is characterised by a universal/uniqueness property: it is the *unique* measure $\mu$ on $\mathcal{B}(\mathbb{R}^n)$ that is **translation-invariant** ($\mu(x_0+A)=\mu(A)$) and **normalised** ($\mu([0,1]^n)=1$). Translation invariance says $\lambda$ is a *Haar measure* — the canonical invariant measure on the locally compact abelian group $(\mathbb{R}^n,+)$ — and Haar measure on any locally compact group is unique up to a positive scalar. Lebesgue measure is thus "the Haar measure of $\mathbb{R}^n$, scaled so the unit cube has mass $1$."

---

# Relate to Other Fields / Compression

Lebesgue measure *is* the Haar measure of the group $(\mathbb{R}^n,+)$ — the same object that, on a compact group, gives the uniform probability and, on a discrete group, gives counting measure. Under a linear map $g\in GL_n(\mathbb{R})$ it scales by $|\det g|$, which is the change-of-variables Jacobian and the bridge to differential geometry's volume forms. Restricted to $[0,1]^n$ it is the **uniform distribution** of probability — the most basic non-trivial law, and (via the [[Def - Distribution Function|quantile transform]]) the seed from which *every* other law on $\mathbb{R}$ is built.

---

# Examples / Corollaries

$\lambda([a,b])=b-a$; $\lambda(\{x\})=0$ (a point is $\bigcap_n(x-\tfrac1n,x+\tfrac1n)$, [[Thm - Properties of Measures|continuity from above]]); hence $\lambda(\mathbb{Q})=0$ — every countable set is **Lebesgue-null**. So $\mathbf{1}_\mathbb{Q}$, not Riemann-integrable, has $\int\mathbf{1}_\mathbb{Q}\,d\lambda=0$. There exist *uncountable* null sets too (the standard Cantor set: $\lambda=0$) and uncountable closed sets of *positive* measure (fat Cantor sets).

The measure is **not finite** ($\lambda(\mathbb{R}^n)=\infty$) but is **$\sigma$-finite**. It is translation-invariant ([[Thm - Translation Invariance of Lebesgue Measure]]) and *outer/inner regular*: $\lambda(A)=\inf\{\lambda(G):G\supseteq A\text{ open}\}=\sup\{\lambda(K):K\subseteq A\text{ compact}\}$ ([[Thm - Regularity of Lebesgue Measure]]).

The sharp limit: **not every subset of $\mathbb{R}^n$ is Lebesgue-measurable** — the [[Thm - Existence of a Non-Measurable Set|Vitali set]] witnesses $\mathcal{B}^*(\mathbb{R})\neq 2^{\mathbb{R}}$.

Calibration: (i) $\lambda(\mathbb{Q}\cap[0,1])$? $0$. (ii) Is the Cantor set measurable, and what is its measure? Measurable (it is closed, hence Borel), measure $0$. (iii) Is $\lambda$ a probability measure? No — but its restriction to $[0,1]^n$ is.

---

# Unlocked by This

> [!tip] The uniform distribution and the quantile transform *(from [[Advanced Probability I — Probability Spaces and Random Variables|Advanced Probability]])*
> $\lambda|_{[0,1]}$ is the uniform probability measure. Composing it with the generalised inverse of any [[Def - Distribution Function|distribution function]] $F$ realises *every* law on $\mathbb{R}$ as the law of a function of a uniform variable — so a single Lebesgue space supports all of one-dimensional probability.

> [!tip] The Lebesgue integral *(from [[Measure Theory II — Integration|Measure Theory II]])*
> Integration against $\lambda$ is the Lebesgue integral, which extends the Riemann integral and, unlike it, commutes with limits via the [[Thm - Monotone Convergence Theorem|MCT]] and [[Thm - Dominated Convergence Theorem|DCT]].
