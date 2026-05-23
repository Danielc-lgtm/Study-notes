---
type: exercise
subject: measure-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Lp Spaces"
  - "Thm - Hölder and Minkowski Inequalities"
  - "Thm - Completeness of Lp Spaces"
tags: [analysis, measure-theory, probability]
---

# Problem Statement

Let $(X,\mathcal{A},\mu)$ be a measure space and $L^2(\mu)$ its [[Def - Lp Spaces|L² space]], with $\langle f,g\rangle=\int f\bar g\,d\mu$.

**(a)** Show $\langle\cdot,\cdot\rangle$ is an inner product on $L^2(\mu)$ and the **Cauchy–Schwarz inequality** $|\langle f,g\rangle|\le\|f\|_2\|g\|_2$ holds — as the case $p=q=2$ of [[Thm - Hölder and Minkowski Inequalities|Hölder]].

**(b)** Conclude $L^2(\mu)$ is a **Hilbert space** (complete inner-product space), and that for a closed [[Def - Subspace|subspace]] $V\subseteq L^2$ every $f$ has a unique orthogonal projection onto $V$.

**(c)** Interpret on a probability space: for $X,Y\in L^2(\Omega,\mathcal{F},\mathbb{P})$, $|\mathrm{Cov}(X,Y)|\le\sigma(X)\sigma(Y)$, and the [[Def - Conditional Expectation|conditional expectation]] $\mathbb{E}[X\mid\mathcal{G}]$ is the orthogonal projection of $X$ onto $L^2(\mathcal{G})$.

**Recall:**

[[Thm - Hölder and Minkowski Inequalities|Hölder]] with $p=q=2$: $\int|fg|\le\|f\|_2\|g\|_2$. [[Thm - Completeness of Lp Spaces|L² is complete]].

---

# Convergent Strategy

**Problem class:** identifying $L^2$ as the canonical Hilbert space and reading off the geometric consequences.

**Assumption pattern:** $L^2$ has an inner product $\Rightarrow$ it has *geometry* — angles, orthogonality, projection. Cauchy–Schwarz is what makes $\langle\cdot,\cdot\rangle$ well-defined ($fg\in L^1$) and bounds the "angle."

**Theorem routing:** Hölder ($p=q=2$) $\Rightarrow$ Cauchy–Schwarz $\Rightarrow$ inner product well-defined; completeness $\Rightarrow$ Hilbert; Hilbert $\Rightarrow$ projection theorem.

**Key decision point:** the projection theorem is what *gives* conditional expectation; recognising "$\mathbb{E}[\cdot\mid\mathcal{G}]=$ projection onto $L^2(\mathcal{G})$" is the payoff.

---

# Legal Operations Used

1. **Hölder $p=q=2$** to bound the inner product / certify $fg\in L^1$.
2. **Completeness $+$ inner product $=$ Hilbert space.**
3. **Orthogonal projection** onto a closed subspace.

---

# Hints

> [!note]- Hint 1
> $\langle f,g\rangle=\int f\bar g$ is finite because $|f\bar g|\le\tfrac12(|f|^2+|g|^2)$, or directly by Hölder $p=q=2$.

> [!note]- Hint 2
> Cauchy–Schwarz *is* Hölder with $p=q=2$: $\int|f\bar g|\le\|f\|_2\|g\|_2$.

> [!note]- Hint 3
> A complete inner-product space is a Hilbert space; in one, every closed *convex* set (in particular every closed subspace) admits unique nearest-point projection.

---

# Solution

**Step 1 — (a) Inner product and Cauchy–Schwarz.** For $f,g\in L^2$, Hölder with $p=q=2$ gives $\int|f\bar g|\,d\mu\le\|f\|_2\|g\|_2<\infty$, so $f\bar g\in L^1$ and $\langle f,g\rangle=\int f\bar g\,d\mu$ is well-defined. It is sesquilinear, conjugate-symmetric, and positive: $\langle f,f\rangle=\int|f|^2=\|f\|_2^2\ge0$, with $=0$ iff $f=0$ in $L^2$ (i.e. $f=0$ a.e.). Cauchy–Schwarz $|\langle f,g\rangle|=|\int f\bar g|\le\int|f\bar g|\le\|f\|_2\|g\|_2$ is exactly [[Thm - Hölder and Minkowski Inequalities|Hölder p=q=2]].

**Step 2 — (b) Hilbert space and projection.** $\|f\|_2=\sqrt{\langle f,f\rangle}$, and by [[Thm - Completeness of Lp Spaces|Riesz–Fischer]] $L^2(\mu)$ is complete. A complete inner-product space is a **Hilbert space**. In a Hilbert space the projection theorem holds: for a closed subspace $V$, every $f$ has a unique $P_V f\in V$ minimising $\|f-v\|_2$ over $v\in V$, characterised by $f-P_V f\perp V$.

> [!note]- Derivation
> The projection theorem follows from the parallelogram law and completeness: a minimising sequence $v_n\in V$ for $\|f-v\|$ is Cauchy (parallelogram identity), converges by completeness, and its limit lies in $V$ since $V$ is closed. Orthogonality $f-P_Vf\perp V$ is the first-order optimality condition.

**Step 3 — (c) Probabilistic reading.** On $(\Omega,\mathcal{F},\mathbb{P})$ with $X,Y\in L^2$: Cauchy–Schwarz applied to the centred variables $X-\mathbb{E}X$, $Y-\mathbb{E}Y$ gives
$$|\mathrm{Cov}(X,Y)|=|\langle X-\mathbb{E}X,\,Y-\mathbb{E}Y\rangle|\le\|X-\mathbb{E}X\|_2\,\|Y-\mathbb{E}Y\|_2=\sigma(X)\,\sigma(Y),$$
so the correlation coefficient lies in $[-1,1]$. And for a sub-$\sigma$-algebra $\mathcal{G}$, $L^2(\mathcal{G})$ is a closed subspace of $L^2(\mathcal{F})$; the orthogonal projection of $X$ onto it is, by the defining property "$X-P_{L^2(\mathcal{G})}X\perp L^2(\mathcal{G})$" i.e. $\mathbb{E}[(X-P X)\mathbf{1}_A]=0$ for $A\in\mathcal{G}$, exactly the [[Def - Conditional Expectation|conditional expectation]] $\mathbb{E}[X\mid\mathcal{G}]$.

> [!note]- Complete formal solution
> (a) Hölder $p=q=2$ gives $f\bar g\in L^1$ and $|\langle f,g\rangle|\le\|f\|_2\|g\|_2$; sesquilinearity, conjugate symmetry, positive-definiteness (modulo a.e.) are direct. (b) $L^2$ complete (Riesz–Fischer) $+$ inner product $=$ Hilbert; the projection theorem gives unique nearest-point projection onto any closed subspace. (c) Cauchy–Schwarz on centred variables bounds covariance by $\sigma(X)\sigma(Y)$; orthogonal projection onto the closed subspace $L^2(\mathcal{G})$ satisfies the defining equations of $\mathbb{E}[X\mid\mathcal{G}]$. $\blacksquare$

---

# Key Takeaways

**$L^2$ is the one $L^p$ space with *geometry*: its norm comes from an inner product, so it has orthogonality, angles, and projections.** Cauchy–Schwarz — the $p=q=2$ case of [[Thm - Hölder and Minkowski Inequalities|Hölder]] — is what makes $\langle f,g\rangle$ finite and bounds it, certifying $L^2$ as an inner-product space; [[Thm - Completeness of Lp Spaces|completeness]] then promotes it to a Hilbert space. The single most consequential gift of the Hilbert structure is the **orthogonal projection theorem**: nearest-point projection onto any closed subspace exists and is unique.

**Orthogonal projection onto $L^2(\mathcal{G})$ *is* conditional expectation — this is the cleanest construction of $\mathbb{E}[X\mid\mathcal{G}]$.** The defining property of the projection ("the error is orthogonal to the subspace") translates verbatim into the defining property of conditional expectation ("$\mathbb{E}[(X-Y)\mathbf{1}_A]=0$ for all $A\in\mathcal{G}$"). So [[Def - Conditional Expectation|conditional expectation]] is, for $L^2$ random variables, a purely geometric operation — the best $\mathcal{G}$-measurable approximation of $X$ in mean square. Cauchy–Schwarz, in the same breath, bounds covariance by the product of standard deviations, making the correlation coefficient a genuine cosine.
