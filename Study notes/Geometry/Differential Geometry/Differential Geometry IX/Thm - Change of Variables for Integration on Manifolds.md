---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Integral of a Compactly Supported Form on a Manifold"
  - "Def - Orientation of a Smooth Manifold"
  - "Def - Pullback of a Differential Form on a Manifold"
  - "Def - Smooth Map between Manifolds"
  - "Def - Diffeomorphism"
tags: [geometry, differential-geometry, integration, change-of-variables]
---

# Notation

$M, N$ are oriented smooth $n$-manifolds, possibly with boundary. $F : N \to M$ is a smooth map; $F^* : \Omega^n(M) \to \Omega^n(N)$ is the pullback of forms. The pullback satisfies $F^*(f\omega) = (f\circ F)F^*\omega$ and (on top-forms) $F^*\omega(p)(v_1, \ldots, v_n) = \omega(F(p))(dF_p v_1, \ldots, dF_p v_n)$. The full notation registry is at [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem]].

---

# Statement

> **Change of Variables for Manifold Integrals.** Let $M, N$ be oriented smooth $n$-manifolds (possibly with boundary), and let $F : N \to M$ be a smooth map.
>
> (a) **Orientation-preserving [[Def - Diffeomorphism|diffeomorphism]].** If $F$ is an orientation-preserving diffeomorphism and $\omega \in \Omega^n_c(M)$, then
> $$\int_M\omega = \int_N F^*\omega.$$
>
> (b) **Orientation-reversing diffeomorphism.** If $F$ is an orientation-reversing diffeomorphism, then
> $$\int_M\omega = -\int_N F^*\omega.$$
>
> (c) **Integration over parametrizations.** Suppose $D_1, \ldots, D_k \subseteq \mathbb{R}^n$ are open domains of integration, and $F_i : \overline{D_i} \to M$ are smooth maps such that each $F_i$ restricts to an orientation-preserving diffeomorphism from $D_i$ onto an open $W_i \subseteq M$, with $W_i \cap W_j = \emptyset$ for $i \neq j$, and $\mathrm{supp}\,\omega \subseteq \overline{W_1} \cup \cdots \cup \overline{W_k}$. Then
> $$\int_M\omega = \sum_{i=1}^k\int_{D_i}F_i^*\omega,$$
> where the right-hand sides are ordinary multiple Riemann integrals.

---

# Motivation

A manifold integral $\int_M\omega$ ought to be invariant under "relabeling" the manifold — that is, under orientation-preserving [[Def - Diffeomorphism|diffeomorphisms]]. The change-of-variables theorem is the precise statement of this invariance. Parts (a) and (b) say: pulling back a top-form via a diffeomorphism preserves the integral up to a sign that depends only on whether the diffeomorphism preserves or reverses orientation.

Part (c) is the computationally useful version: for an explicit parametrization $F_i$ from a domain $D_i \subseteq \mathbb{R}^n$ into $M$, the integral $\int_M\omega$ over $M$ becomes the ordinary multivariable Riemann integral $\int_{D_i}F_i^*\omega$ on the source. This is how one *actually computes* manifold integrals: parametrize, pull back, integrate.

The theorem is the manifold-level analog of the multivariable change-of-variables formula
$$\int_W f(y)\,dy = \int_V f(F(x))|\det DF(x)|\,dx \quad\text{(for }F : V \to W\text{ orientation-preserving)},$$
with the difference that, in the form-version, $|\det DF|$ is replaced by $\det DF$ (without the absolute value), because the form's pullback already supplies the signed determinant. The two formulations agree exactly when $F$ is orientation-preserving — the cleanness of the form version is the payoff of carrying orientation as data.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis of the theorem — "$F$ is an orientation-preserving diffeomorphism" — can be recognized in several disguises.

The first source is **a global parametrization of $M$**. Most computed examples — sphere via spherical coordinates, torus via $(\theta_1, \theta_2)$, projective space via affine charts — are orientation-preserving diffeomorphisms from a region of $\mathbb{R}^n$ onto $M$ (possibly missing a measure-zero set). The bridge: once one verifies orientation-preservation (by checking $\det DF > 0$), the integral on $M$ equals the parametrized integral on $\mathbb{R}^n$.

The second source is **the inverse function theorem**: if $F : N \to M$ has invertible differential at a point, $F$ is locally a diffeomorphism. Provided it is orientation-preserving (positive Jacobian), it is a local change of variables. This is how one verifies that a specific map qualifies as a chart from which one can pull back.

The third source is **a covering map of oriented manifolds**: for an orientation-preserving smooth covering $\pi : \widetilde M \to M$ of degree $k$, the integral of $\pi^*\omega$ on $\widetilde M$ equals $k$ times the integral on $M$ (because each point of $M$ is covered $k$ times). This is the manifold-level "covering map multiplies integrals by degree".

**Targets (Output Amplification)**

Combine the theorem with **explicit parametrization formulas** like spherical coordinates. The further result: closed-form computation of integrals over $S^n$, $T^n$, $\mathbb{CP}^n$, etc.

Combine the theorem with **Stokes's theorem**: pulling back Stokes via an orientation-preserving diffeomorphism produces Stokes on the new manifold. The further result is that Stokes is diffeomorphism-invariant.

Combine the theorem with **degree theory**: the degree of a smooth map $f : M \to N$ between closed oriented $n$-manifolds is $\deg(f) := \int_M f^*\omega / \int_N\omega$ for any volume form on $N$. The further result is the topological invariance of degree.

---

# Why Is It True

The theorem is a direct consequence of the **well-definedness of manifold integration** ([[Thm - Integration is Well-Defined on Oriented Manifolds]]) plus the chart-level change-of-variables formula in $\mathbb{R}^n$.

The mechanism: $F : N \to M$ orientation-preserving means that pulling back a positively-oriented chart $(U_M, \varphi_M)$ on $M$ gives a positively-oriented chart $(F^{-1}(U_M), \varphi_M\circ F)$ on $N$. So a partition-of-unity computation of $\int_N F^*\omega$ in the pulled-back atlas mirrors the partition-of-unity computation of $\int_M\omega$ in the original atlas — chart by chart, the pullback under $F$ commutes with chart-level integration.

In one line: **$F^*$ on forms is "the same" as $F^{-1}$ on charts; pulling back the integrand and pulling back the chart cancel, leaving the integral invariant.**

For the orientation-reversing case, the sign of the chart's orientation flips, contributing a $-1$.

For part (c) — integration over parametrizations — the disjoint open subsets $W_i$ partition $\mathrm{supp}\,\omega$ up to measure zero (the boundaries of the $W_i$ have measure zero in $M$, and they overlap only on boundaries). The integral over $M$ is the sum of integrals over the $W_i$ (by additivity), and each integral over $W_i$ is, by part (a), the pullback integral over $D_i$. This is the practical version: replace a partition of unity (theoretical) by a measure-zero-overlapping parametrization (computational).

---

# What Makes This Hard

The substantive step is recognizing that the **manifold-level change of variables is just the chart-level change of variables glued via partition of unity** — and that the orientation-preserving hypothesis is what converts the $|\det DF|$ in the chart-level formula into the $\det DF$ used by the manifold integral. Students often confuse the *manifold* statement (which has $F^*$ on the form side and *no* extra Jacobian) with the *chart* statement (which has $|\det DF|$ explicitly), forgetting that the form-pullback already includes the Jacobian.

A second subtlety is part (c): the hypothesis "$F_i$ is a smooth map from $\overline{D_i}$ to $M$ restricting to an orientation-preserving diffeomorphism on $D_i$" allows the boundaries $\partial D_i$ to have measure-zero images that overlap; the $W_i$ are required to be disjoint open subsets of $M$. The boundaries take care of themselves because they have measure zero.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Reduce to a single-chart computation using a partition of unity, then apply the change-of-variables formula in $\mathbb{R}^n$ with $\det DF > 0$ for orientation-preserving $F$.

**Subgoal decomposition:**

1. **Single-chart case.** For $\omega$ supported in a positively-oriented chart $(U, \varphi)$ of $M$, $F^*\omega$ is supported in $F^{-1}(U)$ and (since $F$ is orientation-preserving) $F^{-1}(U)$ is the domain of a positively-oriented chart $(F^{-1}(U), \varphi\circ F)$ of $N$. Compute both integrals in these charts; they are the same Riemann integral.
   - *Hint:* $(\varphi\circ F)_*$ on $F^{-1}(U)$ is the same pushforward to $\mathbb{R}^n$ as $\varphi_*$ on $U$, since $F$ is a diffeomorphism. So the chart-level integrals coincide.
   - *Why needed:* It establishes the single-chart case.

2. **General case via partition of unity.** For general $\omega \in \Omega^n_c(M)$, take a partition of unity subordinate to a positively-oriented chart cover of $\mathrm{supp}\,\omega$. Each $\psi_i\omega$ is single-chart-supported, and step 1 applies. Sum.
   - *Hint:* $F^*(\sum_i\psi_i\omega) = \sum_i(\psi_i\circ F)F^*\omega$, with $\{(\psi_i\circ F)\}$ a partition of unity subordinate to a positively-oriented chart cover of $N$ on $F^{-1}(\mathrm{supp}\,\omega)$.
   - *Why needed:* It assembles the single-chart case into the general statement.

3. **Orientation-reversing case.** Same computation, except that the chart on $N$ is *negatively* oriented (since $F$ reverses orientation), contributing a $-1$ sign in the definition of the integral.
   - *Hint:* By [[Def - Integral of a Compactly Supported Form on a Manifold]], a negatively-oriented chart contributes a $-1$ sign.
   - *Why needed:* It establishes (b).

4. **Parametrization case (c).** The $W_i$ partition $\mathrm{supp}\,\omega$ up to measure zero (the boundaries of $W_i$). $\int_M\omega = \sum_i\int_{W_i}\omega + 0 = \sum_i\int_{D_i}F_i^*\omega$ by (a) applied to each $F_i : D_i \to W_i$.
   - *Hint:* Measure-zero boundaries of $W_i$ contribute nothing to the integral.
   - *Why needed:* It establishes the computationally useful version.

---

# Lemma Decomposition

> [!note]- Lemma 1: Single-chart change of variables
> **Statement:** Let $F : N \to M$ be an orientation-preserving diffeomorphism of oriented $n$-manifolds, and let $\omega \in \Omega^n_c(M)$ be supported in a positively-oriented chart $(U_M, \varphi_M)$. Then $\int_M\omega = \int_N F^*\omega$, both integrals computed in their respective charts.
>
> **Hint:** $F^{-1}(U_M)$ is the domain of the positively-oriented chart $(F^{-1}(U_M), \varphi_M\circ F)$ on $N$. The pullback computation in this chart gives the same multiple integral as the original.
>
> **Why needed:** It is the building block of the full theorem, used in the partition-of-unity argument.
>
> > [!note]- Full proof
> > Since $F$ is an orientation-preserving diffeomorphism, $(F^{-1}(U_M), \varphi_M\circ F)$ is a smooth chart on $N$ with positive Jacobian (the transition between this chart and any positively-oriented chart on $N$ involves the differential of $F$, which has positive determinant). Hence it is a positively-oriented chart.
> >
> > Compute: in $U_M$, write $\omega = A(y)\,dy^1\wedge\cdots\wedge dy^n$ for some compactly supported smooth $A$ on $\varphi_M(U_M)$. Then $\int_M\omega = \int_{\varphi_M(U_M)}A(y)\,dy$.
> >
> > Pull back: $F^*\omega$ is supported in $F^{-1}(U_M)$, and in the chart $(F^{-1}(U_M), \varphi_M\circ F)$ on $N$, the coordinates are the same as $\varphi_M$ but on $F^{-1}(U_M)$. So $(\varphi_M\circ F)^*F^*\omega$ is the same form $A(y)\,dy^1\wedge\cdots\wedge dy^n$ on the same Euclidean image (since $\varphi_M\circ F\circ F^{-1} = \varphi_M$). Hence $\int_N F^*\omega = \int_{\varphi_M(U_M)}A(y)\,dy = \int_M\omega$.
> >
> > $\square$

> [!note]- Lemma 2: Partition of unity propagation
> **Statement:** If a partition of unity $\{\psi_i\}$ on $\mathrm{supp}\,\omega$ in $M$ is subordinate to a positively-oriented chart cover, then $\{\psi_i\circ F\}$ is a partition of unity on $F^{-1}(\mathrm{supp}\,\omega) = \mathrm{supp}(F^*\omega)$ subordinate to the corresponding positively-oriented chart cover of $N$.
>
> **Hint:** $\sum_i(\psi_i\circ F) = (\sum_i\psi_i)\circ F = 1\circ F = 1$ on $F^{-1}(\mathrm{supp}\,\omega)$. Each $\psi_i\circ F$ is supported in $F^{-1}(\mathrm{supp}\,\psi_i) \subseteq F^{-1}(U_i)$, a positively-oriented chart of $N$.
>
> **Why needed:** It transfers the partition-of-unity structure from $M$ to $N$ via $F$.
>
> > [!note]- Full proof
> > $\sum_i\psi_i = 1$ on $\mathrm{supp}\,\omega$, so $\sum_i\psi_i\circ F = 1$ on $F^{-1}(\mathrm{supp}\,\omega)$. Each $\psi_i\circ F$ is smooth (composition of smooth) and supported in $F^{-1}(\mathrm{supp}\,\psi_i)$, contained in $F^{-1}(U_i)$. Since $F$ is an orientation-preserving diffeomorphism, $F^{-1}(U_i)$ is a positively-oriented chart of $N$ (Lemma 1). $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem (a).** Let $F : N \to M$ be an orientation-preserving diffeomorphism of oriented $n$-manifolds, $\omega \in \Omega^n_c(M)$. Then $\int_M\omega = \int_N F^*\omega$.
>
> **Step 0 — Setup.** Cover $\mathrm{supp}\,\omega$ by a finite cover of positively-oriented charts $\{U_i\}$ in $M$ and choose a subordinate partition of unity $\{\psi_i\}$. By Lemma 2, $\{F^{-1}(U_i)\}$ is a finite cover of $\mathrm{supp}(F^*\omega) = F^{-1}(\mathrm{supp}\,\omega)$ in $N$ by positively-oriented charts, and $\{\psi_i\circ F\}$ is a subordinate partition of unity.
>
> **Step 1 — Single-chart equality (Lemma 1).** For each $i$, both $\int_M\psi_i\omega$ and $\int_N F^*(\psi_i\omega) = \int_N(\psi_i\circ F)F^*\omega$ are computed in the corresponding charts and give the same multiple Riemann integral. Hence $\int_M\psi_i\omega = \int_N(\psi_i\circ F)F^*\omega$.
>
> **Step 2 — Sum.** $\int_M\omega = \sum_i\int_M\psi_i\omega = \sum_i\int_N(\psi_i\circ F)F^*\omega = \int_N F^*\omega$.
>
> **Theorem (b).** The same argument with the orientation-reversing $F$ gives a sign flip: the chart $(F^{-1}(U_i), \varphi_i\circ F)$ on $N$ is now *negatively* oriented (since the Jacobian of the chart transition includes $\det DF^{-1} < 0$). By [[Def - Integral of a Compactly Supported Form on a Manifold]], a negatively-oriented chart contributes a $-1$ sign, so $\int_M\omega = -\int_N F^*\omega$.
>
> **Theorem (c).** By disjointness of the $W_i$, $\int_M\omega = \sum_i\int_{W_i}\omega + 0$ (the boundaries have measure zero). Each $\int_{W_i}\omega = \int_{D_i}F_i^*\omega$ by (a) applied to the orientation-preserving diffeomorphism $F_i : D_i \to W_i$.
>
> $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Numerical integration: Monte Carlo on a manifold.** To estimate $\int_M\omega$ for a high-dimensional $M$, sample points from a parametrization $F : D \to M$ uniformly in $D$; estimate by $\tfrac{|D|}{N}\sum_{i=1}^N F^*\omega(x_i)$. The change-of-variables theorem ensures this converges to the manifold integral.

**Lie theory: integration on a homogeneous space.** A homogeneous space $G/H$ inherits a $G$-invariant integration measure (up to scaling) from the Haar measure on $G$ via the quotient map. The change-of-variables theorem links the Haar integral on $G$ to the integral on $G/H$.

**Riemannian geometry: isometric embeddings and volume.** If $M$ embeds isometrically into a Riemannian manifold $N$, the volume of $M$ in $N$ equals its volume computed intrinsically. This is the diffeomorphism-invariance of $\omega_g$.

**Physics: covariance of action integrals.** Action integrals $S[\phi] = \int_M\mathcal{L}(\phi)\omega_g$ in field theory are required to be diffeomorphism-invariant (general covariance). The change-of-variables theorem is the mathematical statement: changes of coordinates preserve the action integral.

---

# Bridges

- **[[Thm - Integration is Well-Defined on Oriented Manifolds]]** — the well-definedness theorem is the input to this one. Once integration is well-defined chart by chart, diffeomorphism invariance follows by pulling back the charts.

- **[[Thm - The Change of Variables Formula]] (Multivariate Analysis)** — the Euclidean change-of-variables formula with $|\det DF|$ is the analytical input, applied chart by chart. This theorem is its manifold-level generalization, with the sign hidden in the orientation.

- **[[Def - Pullback of a Differential Form on a Manifold]]** — the pullback operation on forms is what carries the Jacobian factor. On top-forms, the pullback explicitly contains $\det DF$, which is why the manifold change-of-variables formula has no extra Jacobian — the pullback already supplied it.

- **[[Thm - Stokes' Theorem on Manifolds]]** — Stokes is preserved under pullback through orientation-preserving diffeomorphisms (both sides transform consistently). This is the *naturality* of Stokes: $\int_{F(M)}d\omega = \int_{\partial F(M)}\omega \iff \int_M F^*d\omega = \int_{\partial M}F^*\omega \iff \int_M d(F^*\omega) = \int_{\partial M}F^*\omega$, which is Stokes for $F^*\omega$ on $M$.

- **Degree theory for smooth maps** — for closed oriented $n$-manifolds $M, N$ and $f : M \to N$ smooth, $\deg(f) = \int_M f^*\omega / \int_N\omega$ for any volume form $\omega$ on $N$. The well-definedness of this ratio (independence of $\omega$) is by the change-of-variables theorem: changing $\omega$ by an exact form changes both integrals consistently.

---

# Unlocked by This

> [!tip] Degree of a Smooth Map *(from Differential Topology)*
> For a smooth map $f : M \to N$ between closed oriented $n$-manifolds, the **degree** is the integer $\deg(f) := \int_M f^*\omega / \int_N\omega$, well-defined by the change-of-variables theorem. The degree is a homotopy invariant and computes algebraically as the count of preimages of a regular value (with signs).

> [!tip] Diffeomorphism Invariance of Action Functionals *(from Mathematical Physics)*
> The change-of-variables theorem is the mathematical foundation of **general covariance** in physics: physical action integrals $S[\phi] = \int_M\mathcal{L}\omega_g$ are unchanged under orientation-preserving diffeomorphisms (changes of spacetime coordinates). This invariance is what underlies general relativity and any diffeomorphism-invariant field theory.

> [!tip] Pushforward of Densities *(from Probability / Measure Theory)*
> The change-of-variables theorem has a measure-theoretic analog: for a smooth bijection $F : N \to M$ of oriented manifolds, the pushforward measure $F_*\mu_N$ on $M$ has Radon–Nikodým derivative $|\det DF^{-1}|$ with respect to $\mu_M$. This is the manifold version of the probability-theoretic "change-of-variables for densities" formula.
