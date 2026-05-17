---
type: theorem
subject: measure-theory
prereqs:
  - "Def - The Integral"
  - "Thm - Monotone Convergence Theorem"
  - "Thm - Approximation by Simple Functions"
tags: [analysis, measure-theory]
---

# Notation

$(X,\mathcal{A},\mu)$ a measure space; $f,g\in L^1(\mu)$ [[Def - The Integral|integrable functions]]; $\alpha,\beta\in\mathbb{R}$.

---

# Motivation

The [[Def - The Integral|integral]] was *defined* in three stages (simple, non-negative, signed). The properties one actually uses — that it is **linear**, **monotone**, and satisfies the **triangle inequality** $|\int f|\le\int|f|$ — are not part of the definition; they must be proved. This theorem is that proof. Linearity in particular is surprisingly non-trivial: the integral of a non-negative function is a *supremum*, and "sup of a sum $=$ sum of sups" is false in general — linearity has to be routed through MCT.

---

# Sources and Targets

**Sources.** Hypothesis "$f,g\in L^1$." Broadened: linearity for non-negative measurable $f,g$ holds with no integrability assumption (values in $[0,\infty]$); monotonicity holds for any $f\le g$; the [[Def - Almost Everywhere|a.e.]] versions ($f\le g$ a.e., $f=g$ a.e.) hold by discarding null sets.

**Targets.** Linearity is what makes $\int$ a *linear functional* — the structure underlying [[Def - Lp Spaces|Lᵖ spaces]] as normed vector spaces. The triangle inequality $|\int f|\le\int|f|$ is the prototype of the $L^p$ norm inequalities and the workhorse estimate for [[Thm - Dominated Convergence Theorem|DCT]] and convergence proofs. Monotonicity is invoked silently in essentially every estimate.

---

# Formal Statement

Let $f,g$ be measurable.

1. **(Monotonicity)** If $0\le f\le g$, then $\int f\,d\mu\le\int g\,d\mu$. More generally, for $f,g\in L^1$, $f\le g$ $\mu$-a.e. $\implies\int f\le\int g$; hence $f=g$ a.e. $\implies\int f=\int g$.
2. **(Linearity)** For $f,g\ge0$ measurable and $\alpha,\beta\ge0$: $\int(\alpha f+\beta g)\,d\mu=\alpha\int f+\beta\int g$ (in $[0,\infty]$). For $f,g\in L^1$ and $\alpha,\beta\in\mathbb{R}$: $\alpha f+\beta g\in L^1$ and $\int(\alpha f+\beta g)=\alpha\int f+\beta\int g$.
3. **(Triangle inequality)** For $f\in L^1$, $\big|\int f\,d\mu\big|\le\int|f|\,d\mu$.

---

# Why Is It True

**Monotonicity** is immediate from the definition: for $0\le f\le g$, every simple $s\le f$ also satisfies $s\le g$, so the supremum defining $\int f$ is over a *subset* of the functions defining $\int g$ — a smaller sup. The a.e. version: if $f\le g$ off a null set $N$, replace $f$ by $f\mathbf{1}_{N^c}$, which equals $f$ a.e. (so has the same integral) and is $\le g$ everywhere.

**Linearity for non-negative $f,g$** cannot be read off the definition — $\sup(s+t)\neq\sup s+\sup t$ for arbitrary families. MCT supplies the route. Take simple $s_n\uparrow f$ and $t_n\uparrow g$ ([[Thm - Approximation by Simple Functions]]); then $s_n+t_n\uparrow f+g$, all simple. Linearity *for simple functions* is elementary (just rearrange the finite sum $\sum\alpha_i\mu(A_i)$ over the common refinement of the two partitions). Now apply [[Thm - Monotone Convergence Theorem|MCT]] three times: $\int(f+g)=\lim\int(s_n+t_n)=\lim(\int s_n+\int t_n)=\int f+\int g$. **MCT is what transports linearity from the simple functions, where it is obvious, up to all non-negative functions.** Scaling $\int\alpha f=\alpha\int f$ is direct from the definition.

**Linearity for signed $f,g$** reduces to the non-negative case by splitting into positive and negative parts. The only care: $(f+g)^+-(f+g)^-=f^+-f^-+g^+-g^-$ must be rearranged into an identity between *non-negative* functions, $(f+g)^++f^-+g^-=(f+g)^-+f^++g^+$, before applying non-negative linearity — one never subtracts possibly-infinite quantities. Integrability of $\alpha f+\beta g$ follows from $|\alpha f+\beta g|\le|\alpha||f|+|\beta||g|$ and monotonicity.

**Triangle inequality.** $\pm f\le|f|$, so by linearity and monotonicity $\pm\int f=\int(\pm f)\le\int|f|$; hence $|\int f|\le\int|f|$. It is the integral inheriting the triangle inequality of $\mathbb{R}$, one point at a time.

---

# What Makes This Hard

Only linearity is hard, and the difficulty is structural, not computational: the integral of $f\ge0$ is a *supremum*, and suprema do not add. The non-obvious step is to *not* work with the definition directly but to approximate $f,g$ by simple functions, use the trivial simple-function linearity, and let [[Thm - Monotone Convergence Theorem|MCT]] carry the identity to the limit. For signed functions the trap is "$\infty-\infty$": one must rearrange $f+g=f^+-f^-+g^+-g^-$ into an all-non-negative equation before integrating. The common error is to apply linearity to signed functions before checking integrability.

---

# Rederivation Scaffold

**High-level strategy.** Monotonicity: smaller sup. Non-negative linearity: simple-function linearity + MCT. Signed linearity: split into $f^\pm,g^\pm$, rearrange to non-negative, apply non-negative linearity. Triangle inequality: $\pm f\le|f|$.

**Subgoal decomposition.**

1. **Monotonicity.** $0\le f\le g$: $\{s\le f\}\subseteq\{s\le g\}$, so $\sup$ over the smaller set is smaller. A.e. version: modify on the null set.
2. **Simple linearity.** $\int(s+t)=\int s+\int t$ for simple $s,t$ via the common refinement of partitions.
3. **Non-negative linearity.** $s_n\uparrow f$, $t_n\uparrow g$; $s_n+t_n\uparrow f+g$; MCT three times.
4. **Signed linearity.** Rearrange $(f+g)^++f^-+g^-=(f+g)^-+f^++g^+$; apply step 3; integrability from $|\alpha f+\beta g|\le|\alpha||f|+|\beta||g|$.
5. **Triangle inequality.** $-|f|\le f\le|f|$; integrate.

---

# Lemma Decomposition

> [!note]- Lemma 1: Linearity for simple functions
> **Statement:** $\int(s+t)\,d\mu=\int s+\int t$ and $\int\alpha s=\alpha\int s$ for $s,t\in\mathcal{S}^+$, $\alpha\ge0$.
>
> > [!note]- Full proof
> > Write $s=\sum_i\alpha_i\mathbf{1}_{A_i}$, $t=\sum_j\beta_j\mathbf{1}_{B_j}$ over partitions $(A_i)$, $(B_j)$. On the common refinement $(A_i\cap B_j)$, $s+t=\sum_{i,j}(\alpha_i+\beta_j)\mathbf{1}_{A_i\cap B_j}$, so $\int(s+t)=\sum_{i,j}(\alpha_i+\beta_j)\mu(A_i\cap B_j)=\sum_i\alpha_i\sum_j\mu(A_i\cap B_j)+\sum_j\beta_j\sum_i\mu(A_i\cap B_j)=\sum_i\alpha_i\mu(A_i)+\sum_j\beta_j\mu(B_j)=\int s+\int t$, using finite additivity of $\mu$. Scaling is immediate. $\square$

> [!note]- Lemma 2: Linearity for non-negative measurable functions
> **Statement:** $\int(\alpha f+\beta g)=\alpha\int f+\beta\int g$ for $f,g\ge0$ measurable, $\alpha,\beta\ge0$.
>
> > [!note]- Full proof
> > Pick simple $s_n\uparrow f$, $t_n\uparrow g$ ([[Thm - Approximation by Simple Functions]]). Then $\alpha s_n+\beta t_n\uparrow\alpha f+\beta g$, all in $\mathcal{S}^+$. By [[Thm - Monotone Convergence Theorem|MCT]] applied to each of the three increasing sequences and Lemma 1, $\int(\alpha f+\beta g)=\lim\int(\alpha s_n+\beta t_n)=\lim(\alpha\int s_n+\beta\int t_n)=\alpha\int f+\beta\int g$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> (1) For $0\le f\le g$, $\{s\in\mathcal{S}^+:s\le f\}\subseteq\{s\le g\}$, so $\int f=\sup\le\sup=\int g$; the a.e. version follows by replacing $f$ with $f\mathbf{1}_{\{f\le g\}}$. (2) Non-negative case is Lemma 2. Signed case: from $(f+g)^++f^-+g^-=(f+g)^-+f^++g^+$ (all non-negative), Lemma 2 gives $\int(f+g)^++\int f^-+\int g^-=\int(f+g)^-+\int f^++\int g^+$; rearranging (all terms finite, as $f,g\in L^1$) yields $\int(f+g)=\int f+\int g$; combined with $\int\alpha f=\alpha\int f$ (case $\alpha\ge0$ from Lemma 2, $\alpha<0$ from $\int(-f)=-\int f$). (3) $-|f|\le f\le|f|$ and (1),(2) give $-\int|f|\le\int f\le\int|f|$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

Linearity makes $f\mapsto\int f\,d\mu$ a linear functional on [[Def - Lp Spaces|L¹]] — the starting point of duality theory and the Riesz representation theorem. In probability it is **linearity of expectation**, $\mathbb{E}[\alpha X+\beta Y]=\alpha\mathbb{E}X+\beta\mathbb{E}Y$, which holds with *no independence assumption* — a fact that trivialises many computations (e.g. the expected number of fixed points of a random permutation, by indicator decomposition).

---

# Bridges

- **[[Thm - Monotone Convergence Theorem]]** — the vehicle carrying linearity from simple functions to all of $L^1$.
- **[[Thm - Hölder and Minkowski Inequalities]]** — the triangle inequality $|\int f|\le\int|f|$ is the $p=1$ progenitor of the $L^p$ norm inequalities.
- **[[Def - Lp Spaces]]** — linearity is what makes $L^p$ a vector space and $\int$ a functional on it.
