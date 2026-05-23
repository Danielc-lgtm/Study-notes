---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Integral of a Compactly Supported Form on a Manifold"
  - "Def - Orientation of a Smooth Manifold"
  - "Def - Pullback of a Differential Form on a Manifold"
  - "Def - Partition of Unity on a Manifold"
tags: [geometry, differential-geometry, integration, well-definedness]
---

# Notation

$(M, \mathcal{O})$ is an oriented smooth $n$-manifold ($n \geq 1$), possibly with boundary. $\omega \in \Omega^n_c(M)$ is a compactly supported smooth $n$-form. Charts $(U, \varphi)$ are smooth and either positively or negatively oriented. The change-of-variables formula in $\mathbb{R}^n$ — see [[Thm - The Change of Variables Formula]] — is the analytical input. The full notation registry is at [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem]].

---

# Statement

> **Well-Definedness of Manifold Integration.** Let $(M, \mathcal{O})$ be an oriented smooth $n$-manifold ($n \geq 1$), possibly with boundary, and let $\omega \in \Omega^n_c(M)$ be a compactly supported smooth $n$-form. Define
> $$\int_M\omega := \sum_i\int_{\varphi_i(U_i)}(\varphi_i^{-1})^*(\psi_i\omega)$$
> where $\{(U_i, \varphi_i)\}_{i=1}^N$ is a finite cover of $\mathrm{supp}\,\omega$ by positively-oriented smooth charts and $\{\psi_i\}$ is a subordinate smooth partition of unity. (Negatively-oriented charts contribute with a sign $-1$, but the construction proceeds analogously.) Then:
>
> (a) The integral does not depend on the choice of cover $\{U_i\}$.
> (b) The integral does not depend on the choice of partition of unity $\{\psi_i\}$.
> (c) For a single-chart-supported form, the integral does not depend on which positively-oriented chart is used.

---

# Motivation

The definition of the manifold integral $\int_M\omega$ in [[Def - Integral of a Compactly Supported Form on a Manifold]] uses a *choice* of oriented chart cover and a *choice* of subordinate partition of unity. For the definition to be useful, the answer must not depend on these choices — otherwise different mathematicians computing the same integral would get different answers, and the integral would be ill-defined.

The well-definedness theorem says: the answer is the same regardless of the auxiliary data. This is what makes the manifold integral *intrinsic* to $M$ and $\omega$.

The proof has two layers:
- **Chart independence (single-chart case).** Two oriented charts $(U, \varphi)$ and $(U, \widetilde\varphi)$ covering the same support of $\omega$ are related by an orientation-preserving diffeomorphism (the transition map, restricted to $\varphi(U) \subseteq \mathbb{R}^n$). The form transforms by $\det DF$; the multivariable Riemann integral transforms by $|\det DF|$; these agree because the chart is *positively oriented*, hence $\det DF > 0$ and $|\det DF| = \det DF$. So the integral is independent of the chart.
- **Partition independence.** Two different partitions $\{\psi_i\}$ and $\{\widetilde\psi_j\}$ give two different sums; their equality follows by the standard refinement argument $\sum_i\psi_i\widetilde\omega = \sum_{i,j}\psi_i\widetilde\psi_j\widetilde\omega$, applied to both summations.

The crucial step is the chart-independence: it is the exact place where the *orientation* hypothesis is used. Without orientation, the chart transitions could have negative Jacobian, and the integral would be sign-ambiguous. *This is the reason integration is restricted to oriented manifolds*: it is precisely the case where the chart-by-chart construction is well-defined.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis "the integral is well-defined" is invoked whenever one computes an integral via a *specific* chart and treats the answer as canonical. Several disguised sources arise:

The first source is **using one of several "natural" parametrizations of $M$** — for instance, computing $\int_{S^2}\omega$ by stereographic projection rather than spherical coordinates. The bridge: both parametrizations are orientation-preserving diffeomorphisms onto an open dense subset of $S^2$, so the well-definedness theorem guarantees they give the same answer. Non-obvious: different-looking parametrizations are interchangeable for the purpose of the integral.

The second source is **using an over-cover and partition of unity for a non-globally-parametrizable manifold** — e.g., the torus $T^2$ via two charts that overlap on a strip. The well-definedness ensures that the sum-with-partition is the same as a sum with a different cover-and-partition choice.

The third source is **the "integration over parametrizations" Proposition 16.8 of Lee** — replacing the partition-of-unity formula by a chart-by-chart formula via disjoint orientation-preserving diffeomorphisms $F_i : D_i \to W_i$ whose images cover $M$ up to measure zero. The well-definedness theorem is what makes this alternative formula give the same answer as the partition-of-unity definition. This is the computationally useful version.

**Targets (Output Amplification)**

Combine the theorem with **integration on a Riemannian manifold**: the Riemannian volume form $\omega_g$ provides a canonical chart-independent way to integrate functions ($\int_M f := \int_M f\omega_g$), with chart-independence guaranteed by this theorem. The further result: $L^p$ spaces, Sobolev spaces, the Laplace–Beltrami operator, the heat kernel, and all spectral theory on Riemannian manifolds are well-defined exactly because of the well-definedness of integration.

Combine the theorem with **diffeomorphism invariance**: integration is invariant under orientation-preserving diffeomorphisms $F : N \to M$, because $F^*\omega$ pulled back through a chart of $N$ matches $\omega$ pulled back through the corresponding chart of $M$. The further result is the **change of variables formula** ([[Thm - Change of Variables for Integration on Manifolds]]), the manifold-level analog of $\int_M f(x)\,dx = \int_N f(\varphi(y))|\det D\varphi|\,dy$.

Combine the theorem with **the special case of Stokes**: in proving Stokes's theorem one reduces to a half-space chart and computes by FTC; the well-definedness of integration is what lets one do this reduction without worrying about the choice of half-space coordinates.

---

# Why Is It True

The truth is a combination of two ingredients: the **change-of-variables formula** in $\mathbb{R}^n$ and the **positive-Jacobian condition** of an oriented atlas.

Stage 1: chart independence. Suppose $\omega$ is supported in a single domain $U$ covered by two positively-oriented charts $\varphi : U \to \widehat U$ and $\widetilde\varphi : U \to \widehat{\widetilde U}$. The transition $F := \widetilde\varphi \circ \varphi^{-1} : \widehat U \to \widehat{\widetilde U}$ is an orientation-preserving diffeomorphism — $\det DF > 0$ throughout. Now $\omega$ pulled back through $\varphi$ is $(\varphi^{-1})^*\omega = A(x)\,dx^1\wedge\cdots\wedge dx^n$ for some compactly supported function $A$, and through $\widetilde\varphi$ is $(\widetilde\varphi^{-1})^*\omega = \widetilde A(y)\,dy^1\wedge\cdots\wedge dy^n$. These are related by $F^*$: $(\varphi^{-1})^*\omega = F^*\big((\widetilde\varphi^{-1})^*\omega\big)$, since $\widetilde\varphi^{-1}\circ F = \varphi^{-1}$. Pulling back a top-form by $F$ multiplies by $\det DF$: $A(x)\,dx^1\wedge\cdots\wedge dx^n = \widetilde A(F(x))\det DF\,dx^1\wedge\cdots\wedge dx^n$, so $A(x) = \widetilde A(F(x))\det DF$.

The two candidate integrals are $\int_{\widehat U}A(x)\,dx$ and $\int_{\widehat{\widetilde U}}\widetilde A(y)\,dy$. By the change-of-variables formula in $\mathbb{R}^n$, $\int_{\widehat{\widetilde U}}\widetilde A(y)\,dy = \int_{\widehat U}\widetilde A(F(x))|\det DF|\,dx$. Since $\det DF > 0$, $|\det DF| = \det DF$, and $\widetilde A(F(x))\det DF = A(x)$. So the two candidate integrals agree.

**The bolded one-liner mechanism: the form's transformation rule is $\det DF$, the multiple-integral's transformation rule is $|\det DF|$, and they agree exactly when $\det DF > 0$ — the positive-Jacobian condition of orientation.**

Without orientation, the form transforms by signed determinant, the integral by absolute, and the two give *different* answers (differing in sign) when the Jacobian is negative. Orientation is the *exact* condition under which the two match.

Stage 2: partition independence. Once chart independence is established, the partition-of-unity construction is independent of the partition by a standard refinement argument. Suppose $\{\psi_i\}$ and $\{\widetilde\psi_j\}$ are two partitions of unity subordinate to (possibly different) finite oriented chart covers. Then
$$\sum_i\int_M\psi_i\omega = \sum_i\int_M\psi_i\Big(\sum_j\widetilde\psi_j\Big)\omega = \sum_{i,j}\int_M\psi_i\widetilde\psi_j\omega,$$
using $\sum_j\widetilde\psi_j = 1$ on $\mathrm{supp}\,\omega$. By Stage 1, each $\int_M\psi_i\widetilde\psi_j\omega$ is well-defined regardless of which chart it is computed in (the form is supported in both the chart of $\psi_i$ and the chart of $\widetilde\psi_j$, so either chart works). The same computation starting from $\sum_j\int_M\widetilde\psi_j\omega$ gives the same double sum. So the two partition sums agree.

---

# What Makes This Hard

The genuinely subtle point is recognizing that the **change-of-variables formula in $\mathbb{R}^n$, with $|\det DF|$, is what makes the form integral well-defined, *because* the orientation hypothesis converts $|\det DF|$ into $\det DF$**. Students who learned the multivariable change-of-variables formula with absolute value often forget that the "form version" omits the absolute value, and this is the entire content of the well-definedness. A common error is to invoke chart independence as if it were obvious, without specifying *that* the chart transitions have positive Jacobian — orientation is the load-bearing hypothesis.

A second subtlety is that the partition-independence argument uses the *finiteness* of the partition (so the sums converge in the obvious sense) and the *compactness* of the support of $\omega$ (so finite covers exist). Without compact support, the argument fails.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove chart independence first, using the change-of-variables formula in $\mathbb{R}^n$ and the positive-Jacobian condition. Then prove partition independence by a refinement argument, applying chart independence termwise.

**Subgoal decomposition:**

1. **Pullback transformation of top-forms.** For an orientation-preserving diffeomorphism $F : V \to W$ of open subsets of $\mathbb{R}^n$, and $\alpha = A(y)\,dy^1\wedge\cdots\wedge dy^n$, $F^*\alpha = A(F(x))\det DF(x)\,dx^1\wedge\cdots\wedge dx^n$.
   - *Hint:* Direct computation of $F^*(dy^i) = \sum_j(\partial F^i/\partial x^j)dx^j$, then wedge.
   - *Why needed:* It tells us how the integrand changes under chart transition.

2. **Change-of-variables formula in $\mathbb{R}^n$.** For an orientation-preserving diffeomorphism $F : V \to W$ and a compactly supported continuous function $A$ on $W$, $\int_W A(y)\,dy = \int_V A(F(x))|\det DF(x)|\,dx$ ([[Thm - The Change of Variables Formula]]).
   - *Hint:* This is the standard multivariable change-of-variables theorem from Lebesgue integration; absolute value of Jacobian.
   - *Why needed:* It provides the relationship between integrals over the source and target of $F$.

3. **Synthesize 1 and 2 to get chart independence.** Combine pullback rule (signed det) with change-of-variables (absolute det) and use $\det DF > 0$ from positive-orientation to conclude the two chart-by-chart integrals of a single-patch-supported form agree.
   - *Hint:* $|\det DF| = \det DF$ when the chart is oriented.
   - *Why needed:* It establishes (c) of the theorem.

4. **Refinement for partition independence.** Given two partition-of-unity computations $\sum_i\int_M\psi_i\omega$ and $\sum_j\int_M\widetilde\psi_j\omega$, multiply each by the other partition: $\sum_i\int_M\psi_i\omega = \sum_{i,j}\int_M\psi_i\widetilde\psi_j\omega = \sum_j\int_M\widetilde\psi_j\omega$.
   - *Hint:* Each $\psi_i\widetilde\psi_j\omega$ is supported in the intersection of two charts, so single-chart well-definedness applies.
   - *Why needed:* It establishes (a) and (b) of the theorem.

---

# Lemma Decomposition

> [!note]- Lemma 1: Pullback of a top-form under a diffeomorphism multiplies by $\det DF$
> **Statement:** Let $F : V \to W$ be a smooth map between open subsets of $\mathbb{R}^n$, and let $\alpha = A(y)\,dy^1\wedge\cdots\wedge dy^n$ be a smooth $n$-form on $W$. Then $F^*\alpha = A(F(x))\det DF(x)\,dx^1\wedge\cdots\wedge dx^n$ on $V$.
>
> **Hint:** Compute $F^*(dy^i) = \sum_j(\partial F^i/\partial x^j)\,dx^j$, then wedge all of them.
>
> **Why needed:** It is the source of the signed Jacobian factor on the form side, contrasted with the absolute Jacobian on the integral side.
>
> > [!note]- Full proof
> > $F^*(dy^i) = d(y^i\circ F) = dF^i = \sum_j(\partial F^i/\partial x^j)\,dx^j$. Wedging:
> > $$F^*(dy^1\wedge\cdots\wedge dy^n) = \bigwedge_i\Big(\sum_{j_i}(\partial F^i/\partial x^{j_i})\,dx^{j_i}\Big) = \det DF\,dx^1\wedge\cdots\wedge dx^n,$$
> > by the alternating-multilinear definition of the determinant. With the function $A(y) = A(F(x))$ pulled back, $F^*\alpha = A(F(x))\det DF\,dx^1\wedge\cdots\wedge dx^n$. $\square$

> [!note]- Lemma 2: Chart independence for single-chart support
> **Statement:** If $\omega \in \Omega^n_c(M)$ is supported in $U \cap \widetilde U$, where $(U, \varphi)$ and $(\widetilde U, \widetilde\varphi)$ are positively-oriented charts, then $\int_{\varphi(U)}(\varphi^{-1})^*\omega = \int_{\widetilde\varphi(\widetilde U)}(\widetilde\varphi^{-1})^*\omega$.
>
> **Hint:** Let $F := \widetilde\varphi\circ\varphi^{-1}$, an orientation-preserving diffeomorphism. Use Lemma 1 and the multivariable change-of-variables formula; the signed and absolute Jacobians agree because $F$ is orientation-preserving.
>
> **Why needed:** It establishes the single-chart well-definedness, the core of the chart-independence claim.
>
> > [!note]- Full proof
> > Let $F = \widetilde\varphi\circ\varphi^{-1} : \varphi(U \cap \widetilde U) \to \widetilde\varphi(U \cap \widetilde U)$, an orientation-preserving diffeomorphism (positive Jacobian by oriented atlas). Writing $(\varphi^{-1})^*\omega = A(x)\,dx^1\wedge\cdots\wedge dx^n$ and $(\widetilde\varphi^{-1})^*\omega = \widetilde A(y)\,dy^1\wedge\cdots\wedge dy^n$, since $\widetilde\varphi^{-1}\circ F = \varphi^{-1}$, we have $(\varphi^{-1})^*\omega = F^*((\widetilde\varphi^{-1})^*\omega)$, so by Lemma 1, $A(x) = \widetilde A(F(x))\det DF(x)$.
> >
> > By the multivariable change-of-variables formula in $\mathbb{R}^n$ applied to $F$ (with $|\det DF|$),
> > $$\int_{\widetilde\varphi(U \cap \widetilde U)}\widetilde A(y)\,dy = \int_{\varphi(U \cap \widetilde U)}\widetilde A(F(x))|\det DF(x)|\,dx = \int_{\varphi(U \cap \widetilde U)}\widetilde A(F(x))\det DF(x)\,dx,$$
> > using $\det DF > 0$ to drop the absolute value. The integrand equals $A(x)$, so
> > $$\int_{\widetilde\varphi(\widetilde U)}\widetilde A(y)\,dy = \int_{\varphi(U)}A(x)\,dx,$$
> > the two chart-integrals coincide. $\square$

> [!note]- Lemma 3: Partition-of-unity refinement
> **Statement:** If $\{\psi_i\}_{i=1}^N$ and $\{\widetilde\psi_j\}_{j=1}^M$ are two finite smooth partitions of unity on $\mathrm{supp}\,\omega$ subordinate to finite oriented chart covers, then $\sum_i\int_M\psi_i\omega = \sum_j\int_M\widetilde\psi_j\omega$.
>
> **Hint:** Multiply each partition by the other and use chart independence (Lemma 2) for each cross-term.
>
> **Why needed:** It establishes (a) and (b) of the theorem — independence of cover and partition.
>
> > [!note]- Full proof
> > $\sum_j\widetilde\psi_j = 1$ on $\mathrm{supp}\,\omega$, so
> > $$\sum_i\int_M\psi_i\omega = \sum_i\int_M\psi_i\Big(\sum_j\widetilde\psi_j\Big)\omega = \sum_{i,j}\int_M\psi_i\widetilde\psi_j\omega.$$
> > Each term $\psi_i\widetilde\psi_j\omega$ is supported in the intersection of the chart of $\psi_i$ and the chart of $\widetilde\psi_j$ — a region where both charts are positively oriented. So by Lemma 2, $\int_M\psi_i\widetilde\psi_j\omega$ is well-defined and equals the chart-integral in either chart. Symmetrically,
> > $$\sum_j\int_M\widetilde\psi_j\omega = \sum_{i,j}\int_M\psi_i\widetilde\psi_j\omega.$$
> > The double sums are equal, so the original sums are equal. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** The integral $\int_M\omega$ defined in [[Def - Integral of a Compactly Supported Form on a Manifold]] is independent of the choice of oriented chart cover and subordinate partition of unity.
>
> **Step 0 — Setup.** $M$ is oriented; $\omega \in \Omega^n_c(M)$. By compactness of $\mathrm{supp}\,\omega$, finite oriented chart covers exist; by paracompactness (from second-countability + Hausdorff), subordinate smooth partitions of unity exist.
>
> **Step 1 — Single-chart well-definedness (Lemma 2).** For $\omega$ supported in $U \cap \widetilde U$ with two positively-oriented charts, the chart-integrals agree.
>
> **Step 2 — Multi-chart consistency (Lemma 3).** For two partition-of-unity choices, the sums agree. Combined with Step 1, the chart-by-chart computation of each $\psi_i\widetilde\psi_j\omega$ contribution is well-defined.
>
> **Step 3 — Conclude.** The full integral $\int_M\omega = \sum_i\int_M\psi_i\omega$ is independent of choices, hence canonically defined.
>
> $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Numerical analysis / quadrature.** The chart-by-chart definition of $\int_M\omega$ leads naturally to a numerical quadrature scheme on a manifold: cover by charts, choose a partition, integrate each piece by ordinary multivariable quadrature, sum. Well-definedness ensures the result is independent of the chart choice up to numerical error.

**Stochastic differential equations on manifolds.** Brownian motion on a Riemannian manifold is defined via the heat semigroup $e^{t\Delta_g}$, which uses the integral on $M$ (against $\omega_g$). Well-definedness of integration is what makes the heat kernel and Brownian motion intrinsic — independent of the local coordinate system used to set up the equations.

**Diffeomorphism-invariant physical theories.** General relativity and other diffeomorphism-invariant theories use action integrals $\int_M\mathcal{L}\,\omega_g$ where $\mathcal{L}$ is a scalar Lagrangian density. The diffeomorphism invariance of the theory rests on the well-definedness of the integral.

---

# Bridges

- **[[Def - Integral of a Compactly Supported Form on a Manifold]]** — this theorem is the **proof that the definition is consistent**: without it, the definition would depend on auxiliary choices and would not be a function of $\omega$ alone. The theorem completes the construction.

- **[[Thm - The Change of Variables Formula]] / [[Thm - Change of Variables for Integration on Manifolds]]** — the well-definedness theorem uses the $\mathbb{R}^n$ change-of-variables formula on charts, and *implies* the manifold-level change-of-variables formula for orientation-preserving diffeomorphisms. The two theorems are dual: one is the chart-level analytical input, the other is the manifold-level conclusion.

- **[[Def - Oriented Atlas]]** — the well-definedness theorem makes essential use of the positive-Jacobian condition. Without orientation (without an oriented atlas), the chart-by-chart integrals do not agree on overlap, and the integral is ill-defined. This is the precise place where the orientation hypothesis is used.

- **Riemann–Lebesgue measure theory** — the chart-by-chart approach treats each chart as a domain in $\mathbb{R}^n$ with ordinary Lebesgue measure; the Jacobian compatibility makes these glue into a global measure on $M$. This is exactly the construction of the Riemannian (or volume-form) measure $\mu_g$ as a measure on $M$.

- **The boundary case** — for a manifold with boundary, the same well-definedness theorem holds, with the chart-level argument applied to half-space charts $\mathbb{H}^n$ instead of $\mathbb{R}^n$. The boundary contributions are handled by the induced orientation, and well-definedness extends to the boundary integral as well (used implicitly in Stokes's theorem).

---

# Unlocked by This

> [!tip] Diffeomorphism Invariance of the Integral *(continued in this topic)*
> A direct corollary: orientation-preserving diffeomorphisms preserve the integral. This is [[Thm - Change of Variables for Integration on Manifolds]] and is what makes manifold integration intrinsic.

> [!tip] Integration of Functions via the Riemannian Volume Form *(continued in this topic)*
> Once the integral of top-forms is well-defined, the integral of functions is defined by $\int_M f := \int_M f\omega_g$ for any choice of (compactly supported) function and the Riemannian volume form. Well-definedness of the integral and uniqueness of $\omega_g$ make this canonical on Riemannian manifolds.

> [!tip] Diffeomorphism-Invariant Physical Theories *(from Mathematical Physics)*
> The well-definedness of the integral is the mathematical underpinning of general relativity, gauge theory, and any field theory whose action is given as an integral on a manifold. The diffeomorphism invariance of these theories is the manifold-level analog of "the integral does not depend on coordinates".
