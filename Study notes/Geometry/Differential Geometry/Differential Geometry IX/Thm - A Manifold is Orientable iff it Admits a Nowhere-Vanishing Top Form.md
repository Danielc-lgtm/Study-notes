---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Orientation of a Smooth Manifold"
  - "Def - Volume Form"
  - "Def - Differential k-Form on a Manifold"
  - "Def - Partition of Unity on a Manifold"
  - "Thm - Existence of Smooth Partitions of Unity"
tags: [geometry, differential-geometry, orientation, volume-form]
---

# Notation

Throughout, $M$ is a smooth $n$-manifold ($n \geq 1$), possibly with boundary. $\Omega^n(M)$ is the space of smooth $n$-forms; an element $\omega \in \Omega^n(M)$ is **nowhere vanishing** if $\omega_p \neq 0$ in $\Lambda^n(T^*_pM)$ for every $p \in M$. The notation registry is at [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem]].

---

# Statement

> **Orientability Criterion.** A smooth $n$-manifold $M$ ($n \geq 1$) is orientable if and only if there exists a nowhere-vanishing smooth $n$-form $\omega \in \Omega^n(M)$.

> **Refinement.** Given an orientation of $M$, there exists a *positively oriented* smooth volume form (one for which $\omega_p$ determines the chosen orientation at every $p$). Two positively oriented volume forms differ by a smooth positive function: $\omega_1 = f\omega_2$ with $f \in C^\infty(M, \mathbb{R}_{>0})$. The set of orientations of $M$ is therefore in bijection with the set of equivalence classes of nowhere-vanishing $n$-forms under positive scalar multiplication.

---

# Motivation

The definition of orientation in [[Def - Orientation of a Smooth Manifold]] has three equivalent formulations: continuous pointwise orientation, oriented atlas, and (the one this theorem establishes) nowhere-vanishing top-degree form. The theorem proves the equivalence of the last formulation with the first two, and it is the most operationally useful of the three: to check orientability of a specific manifold, the most direct route is to *exhibit* a nowhere-vanishing top-form, or to *refute* its existence.

The forward direction (orientation $\Rightarrow$ existence of $\omega$) is the substantive content: starting from an orientation (a continuous pointwise choice), construct a single globally smooth nowhere-vanishing top-form. The construction uses a partition of unity to glue together local volume forms, which are obvious to construct chart-by-chart but require care to combine without zeros.

The reverse direction ($\omega \Rightarrow$ orientation) is the easy direction: a nowhere-vanishing $\omega$ picks out one of the two rays of $\Lambda^n(T^*_pM) \setminus \{0\}$ at each $p$ — a pointwise orientation — and smoothness of $\omega$ guarantees continuity of this pointwise choice.

The theorem is the bridge between the *qualitative* notion of orientation (an abstract choice in each tangent space) and the *quantitative* / *computable* version (a concrete top-form). Every concrete orientability proof — for $S^n$, $\mathbb{CP}^n$, Lie [[Def - Group|groups]], products — uses the reverse direction (exhibit $\omega$). Every non-orientability proof — for the Möbius strip, $\mathbb{RP}^{2k}$, the Klein bottle — uses the contrapositive of the forward direction (no $\omega$ can exist).

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis "$M$ has a nowhere-vanishing top-form" can arrive disguised.

The first source is **$M$ is a parallelizable manifold** — admits a global frame $(E_1, \ldots, E_n)$. The bridge: the dual coframe $(\varepsilon^1, \ldots, \varepsilon^n)$ gives a nowhere-vanishing top-form $\varepsilon^1\wedge\cdots\wedge\varepsilon^n$. Non-obvious: parallelizability is a *strong* condition (most manifolds are not parallelizable — $S^2$ is the canonical non-parallelizable but orientable example), but when it holds it instantly gives orientability. Lie groups and the spheres $S^1, S^3, S^7$ are all parallelizable, hence all orientable, via this route.

The second source is **$M$ is a hypersurface of an oriented manifold $N$ with a nowhere-vanishing normal vector field**. The bridge: if $\omega_N$ is a volume form on $N$ and $\nu$ is a smooth nowhere-vanishing vector field along $M$ that is nowhere tangent to $M$, then $\iota^*(\iota_\nu\omega_N)$ is a nowhere-vanishing top-form on $M$. Non-obvious: a one-dimensional structure (the normal direction) gives a top-degree structure (the volume form) by the contraction trick. This is how the standard orientation of $S^n$ is constructed: $\nu = x^i\partial_i$ (the position vector) is the outward normal, $\omega_{\mathbb{R}^{n+1}} = dx^1\wedge\cdots\wedge dx^{n+1}$, and the resulting top-form on $S^n$ is the "area form".

The third source is **$M$ is the regular level set of a smooth function** $f : N \to \mathbb{R}$ on an oriented manifold $N$. The bridge: by the regular value theorem ([[Thm - Regular Value Theorem on Manifolds]]), $f^{-1}(c)$ is a smooth submanifold of $N$. With a Riemannian metric on $N$, the gradient $\nabla f$ is nowhere-tangent to the level set (it is normal), so by the previous source, $M$ inherits a nowhere-vanishing top-form via contraction. Non-obvious: orientability of a level set of a function — a *codimension-1* condition — gives an *intrinsic* orientability of the level set itself.

The fourth source is **$M$ is a product** $M_1 \times M_2$ of oriented manifolds. The bridge: $\pi_1^*\omega_1\wedge\pi_2^*\omega_2$ is a nowhere-vanishing top-form on $M_1 \times M_2$. Non-obvious: orientability of factors implies orientability of the product, and the converse also holds (a non-orientable factor would obstruct a nowhere-vanishing form in the product).

**Targets (Output Amplification)**

The conclusion of the theorem is: *the set of orientations of $M$ is in bijection with the set of equivalence classes of nowhere-vanishing top-forms under positive-function scaling.* This concrete identification has several non-obvious uses.

Combine $C$ with **a metric structure on $M$**. The Riemannian volume form $\omega_g = \sqrt{\det g_{ij}}\,dx^1\wedge\cdots\wedge dx^n$ provides a *canonical* representative in the positively-oriented equivalence class (see [[Def - Riemannian Volume Form]] and [[Thm - Existence of the Riemannian Volume Form]]). The further result: an oriented Riemannian manifold has a canonical volume form, hence a canonical integration of functions. This is non-obvious because nothing in the orientability criterion itself singles out a specific volume form within the equivalence class.

Combine $C$ with **the de Rham cohomology of $M$**. A nowhere-vanishing top-form is automatically closed (since $\Omega^{n+1}(M) = 0$). If $M$ is a closed orientable manifold ($\partial M = \emptyset$, compact), then $\omega$ is *not exact*: if $\omega = d\eta$, Stokes gives $\int_M\omega = \int_{\partial M}\eta = 0$, contradicting $\int_M\omega > 0$ (a positively-oriented volume form has positive integral). The further result: every closed orientable manifold has nontrivial top de Rham cohomology, $H^n_{dR}(M) \neq 0$. This is non-obvious because the obstruction "$\omega$ exists" and the obstruction "$H^n_{dR} \neq 0$" sound unrelated, but Stokes plus the theorem ties them together.

Combine $C$ with **non-orientability obstructions in algebraic topology**. The first Stiefel–Whitney class $w_1(TM) \in H^1(M; \mathbb{Z}/2)$ is the obstruction to orientability. The further result: $w_1(TM) = 0 \iff M$ orientable $\iff$ (by this theorem) $\exists\omega \in \Omega^n(M)$ nowhere vanishing. So a *cohomology computation* in $H^1(M; \mathbb{Z}/2)$ can prove or refute the existence of a nowhere-vanishing top-form. Non-obvious: a $\mathbb{Z}/2$-cohomology condition controls a differential-geometric condition.

---

# Why Is It True

The intuition is in two parts: **why a nowhere-vanishing top-form gives an orientation** (easy direction) and **why an orientation gives a nowhere-vanishing top-form via gluing** (hard direction).

**Easy direction.** A top-covector $\omega_p \in \Lambda^n(T^*_pM)$, *if nonzero*, picks out one of the two connected components of $\Lambda^n(T^*_pM) \setminus \{0\}$ — equivalently, an orientation of $T_pM$ in the sense of [[Def - Orientation of a Vector Space]]. If $\omega$ is a smooth nowhere-vanishing $n$-form on $M$, then at every point $p$, $\omega_p \neq 0$, so it picks out an orientation; smoothness of $\omega$ guarantees this pointwise choice is continuous (in the local-frame sense): around any $p$, choose a smooth local frame $(E_1, \ldots, E_n)$ and observe that $\omega(E_1, \ldots, E_n)$ is a continuous function, nowhere zero on a connected neighborhood of $p$, hence of constant sign; the orientation determined by $\omega$ on that neighborhood is the one in which the frame is positive (if the sign is positive) or negative (if negative). Either way, the chosen frame (possibly with one vector negated) is positively oriented in a neighborhood. So $\omega$ defines a continuous pointwise orientation — an orientation in the sense of the definition.

**Hard direction.** Conversely, suppose $M$ is oriented. We want to *construct* a nowhere-vanishing global top-form. The natural local construction works chart-by-chart: in any positively-oriented chart $(U_\alpha, \varphi_\alpha)$, the coordinate form $dx^1\wedge\cdots\wedge dx^n$ (pulled back to $U_\alpha$) is a nowhere-vanishing top-form on $U_\alpha$. The problem is gluing: different charts give different local forms, and their values on a common overlap might not match. They will, however, all be *positive multiples* of each other on overlaps, by the positive-Jacobian condition of the oriented atlas. So we need to combine them via a positive convex combination — exactly what a partition of unity provides.

In detail: take an oriented atlas $\{(U_\alpha, \varphi_\alpha)\}$ and a smooth partition of unity $\{\psi_\alpha\}$ subordinate to this cover. In each $U_\alpha$, define $\omega_\alpha := \varphi_\alpha^*(dx^1\wedge\cdots\wedge dx^n) = dx^1_\alpha\wedge\cdots\wedge dx^n_\alpha$. Each $\omega_\alpha$ is a nowhere-vanishing $n$-form on $U_\alpha$, and on overlaps $U_\alpha \cap U_\beta$, $\omega_\alpha = J_{\alpha\beta}\omega_\beta$ where $J_{\alpha\beta} = \det D(\varphi_\beta\circ\varphi_\alpha^{-1})$ is a smooth *positive* function.

Define
$$\omega := \sum_\alpha\psi_\alpha\omega_\alpha,$$
extending each $\psi_\alpha\omega_\alpha$ by zero outside $U_\alpha$. This is a smooth $n$-form on $M$. We claim it is nowhere vanishing. At any $p \in M$, pick any $\alpha$ with $p \in U_\alpha$ and compute $\omega$ at $p$ in coordinates around $p$, say in $U_\beta$ (with $p \in U_\beta$):
$$\omega_p = \sum_{\gamma : p \in U_\gamma}\psi_\gamma(p)\,\omega_\gamma(p) = \omega_\beta(p)\sum_{\gamma : p \in U_\gamma}\psi_\gamma(p)\,J_{\gamma\beta}(p).$$
The sum $\sum\psi_\gamma(p)J_{\gamma\beta}(p)$ is a sum of non-negative numbers (each $\psi_\gamma(p) \geq 0$, each $J_{\gamma\beta}(p) > 0$) with at least one strictly positive term (the one with $\psi_\gamma(p) > 0$, which must exist by the partition of unity). So the sum is strictly positive, $\omega_\beta(p) \neq 0$ (it is the coordinate top-form), and the product is nonzero. Hence $\omega_p \neq 0$ for every $p$.

**The one-liner mechanism: *the positive-Jacobian compatibility of an oriented atlas turns local volume forms into a convex-combination global form, which is automatically nowhere vanishing because all the coefficients are non-negative with a strictly positive one.*** Without orientation, the Jacobians could be negative; convex combinations would not protect against cancellation; and zeros would appear.

---

# What Makes This Hard

The genuinely substantive step is the **partition-of-unity gluing argument with the observation that positive Jacobians prevent cancellation**: a sum $\sum\psi_\alpha\omega_\alpha$ of local top-forms, with $\psi_\alpha$ non-negative, is nowhere zero precisely because all the $\omega_\alpha$ "point the same way" via the positive-Jacobian condition. The most common error is treating "nowhere vanishing" as automatic from the partition-of-unity construction — without checking that the sign coherence (positive Jacobians) prevents cancellation, the construction could give a form that vanishes on overlap regions.

A second source of confusion is the dual nature of the equivalence: the theorem says *orientable iff nowhere-vanishing top-form exists*, but on a *connected* manifold there are *exactly two* orientations, corresponding to two equivalence classes of nowhere-vanishing top-forms (a form and its negative). On a manifold with $k$ connected components, the count is $2^k$, but the existence/non-existence dichotomy is the same in each component.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Reverse direction is by pointwise extraction of orientations from $\omega_p \neq 0$, with smoothness automatic. Forward direction is partition-of-unity gluing: take coordinate top-forms on an oriented atlas, multiply by a partition of unity, and sum; the positive-Jacobian condition guarantees the sum is nowhere zero because all summands point the same way.

**Subgoal decomposition:**

1. **(Reverse) Extract orientation from $\omega$.** At each $p$, $\omega_p \in \Lambda^n(T^*_pM) \setminus \{0\}$ picks out a connected component of the punctured fiber, equivalently an orientation of $T_pM$. Show this is continuous via local frames.
   - *Hint:* Around any $p$, choose a smooth local frame $(E_i)$. The function $f(p) := \omega(E_1, \ldots, E_n)$ is smooth, nowhere zero on the frame's domain (by nowhere-vanishing $\omega$); hence locally of constant sign; hence (modulo sign-correction of the frame) a positively-oriented local frame exists at every point.
   - *Why needed:* It establishes the easy direction of the equivalence.

2. **(Forward) Build $\omega$ from an oriented atlas via partition of unity.** Take an oriented atlas $\{(U_\alpha, \varphi_\alpha)\}$, with each chart's coordinate top-form $\omega_\alpha = dx^1_\alpha\wedge\cdots\wedge dx^n_\alpha$. Subordinate a smooth partition of unity $\{\psi_\alpha\}$ to the cover. Define $\omega := \sum_\alpha\psi_\alpha\omega_\alpha$.
   - *Hint:* Each $\omega_\alpha$ is nowhere-vanishing on $U_\alpha$; $\psi_\alpha$ is non-negative; the cover is locally finite, so the sum is well-defined and smooth.
   - *Why needed:* It produces a candidate global top-form via the standard manifold-glue mechanism.

3. **(Forward) Verify $\omega$ is nowhere vanishing.** At any $p \in M$, fix any $\beta$ with $p \in U_\beta$. Compute $\omega_p$ in coordinates around $p$: each $\omega_\alpha(p) = J_{\alpha\beta}(p)\omega_\beta(p)$ with $J_{\alpha\beta}(p) > 0$ by orientation. So $\omega_p = \omega_\beta(p)\big(\sum_\alpha\psi_\alpha(p)J_{\alpha\beta}(p)\big)$. The factor in parentheses is a positive sum (at least one $\psi_\alpha(p) > 0$, and all $J_{\alpha\beta}(p) > 0$), so $\omega_p \neq 0$.
   - *Hint:* The positive-Jacobian condition is the load-bearing fact; without it, the partition-of-unity sum could have cancellation.
   - *Why needed:* This is the substantive content of the forward direction.

---

# Lemma Decomposition

> [!note]- Lemma 1: A nowhere-vanishing top-form determines a continuous pointwise orientation
> **Statement:** If $\omega \in \Omega^n(M)$ is smooth and $\omega_p \neq 0$ for every $p \in M$, then the assignment $p \mapsto \mathcal{O}_p$ — where $\mathcal{O}_p$ is the orientation of $T_pM$ determined by $\omega_p$ via [[Def - Orientation of a Vector Space]] — is a continuous pointwise orientation.
>
> **Hint:** Continuity means: at each $p$, there is a local frame $(E_i)$ with $\omega(E_1, \ldots, E_n) > 0$ on an entire neighborhood.
>
> **Why needed:** It establishes the reverse direction of the theorem.
>
> > [!note]- Full proof
> > Given $p \in M$, choose any smooth local frame $(E_1, \ldots, E_n)$ on a connected neighborhood $V$ of $p$ (exists because $TM$ is locally trivial). The function $f(q) := \omega(E_1, \ldots, E_n)|_q$ is smooth and nowhere zero on $V$ (since $\omega$ is nowhere zero and $(E_i)$ is a basis at each $q$). On the connected $V$, $f$ has constant sign. If $f > 0$ throughout $V$, $(E_1, \ldots, E_n)$ is positively oriented at every $q \in V$ in the orientation determined by $\omega$. If $f < 0$ throughout $V$, replace $E_1$ by $-E_1$ to obtain a frame with $f > 0$. Either way, every $p$ has a neighborhood with a positively-oriented frame. This is the continuity condition. $\square$

> [!note]- Lemma 2: Partition-of-unity sum of locally positive top-forms is nowhere vanishing
> **Statement:** Let $\{U_\alpha\}$ be a locally finite open cover of $M$, with smooth nowhere-vanishing $n$-forms $\omega_\alpha$ on each $U_\alpha$, such that on each overlap $U_\alpha \cap U_\beta$, $\omega_\alpha = J_{\alpha\beta}\omega_\beta$ for some smooth *positive* function $J_{\alpha\beta}$. Let $\{\psi_\alpha\}$ be a smooth partition of unity subordinate to $\{U_\alpha\}$. Then $\omega := \sum_\alpha\psi_\alpha\omega_\alpha$ is a smooth nowhere-vanishing $n$-form on $M$.
>
> **Hint:** At each $p$, factor out $\omega_\beta(p)$ for some $\beta$ with $p \in U_\beta$; the remaining sum has all non-negative terms with at least one positive.
>
> **Why needed:** It establishes the forward direction, using the positive-Jacobian condition.
>
> > [!note]- Full proof
> > Smoothness of $\omega$ is automatic from local finiteness of $\{\psi_\alpha\}$ and smoothness of each $\psi_\alpha\omega_\alpha$. For nowhere-vanishing: fix $p \in M$ and pick any $\beta$ with $p \in U_\beta$. On a neighborhood $V$ of $p$ in $U_\beta$, every $\omega_\alpha$ (for $\alpha$ such that $p \in U_\alpha$) equals $J_{\alpha\beta}\omega_\beta$, where $J_{\alpha\beta} : U_\alpha \cap U_\beta \to \mathbb{R}_{>0}$ is positive. At $p$,
> > $$\omega_p = \sum_{\alpha : p \in U_\alpha}\psi_\alpha(p)\omega_\alpha(p) = \omega_\beta(p)\sum_{\alpha : p \in U_\alpha}\psi_\alpha(p)J_{\alpha\beta}(p).$$
> > Each $\psi_\alpha(p) \geq 0$, each $J_{\alpha\beta}(p) > 0$, and at least one $\psi_\alpha(p) > 0$ (since $\sum_\alpha\psi_\alpha(p) = 1$). So the bracketed sum is strictly positive, $\omega_\beta(p)$ is a nonzero element of $\Lambda^n(T^*_pM)$, and the product is nonzero. Hence $\omega_p \neq 0$. $\square$

> [!note]- Lemma 3: An oriented atlas gives positive-Jacobian overlaps for coordinate top-forms
> **Statement:** If $\{(U_\alpha, \varphi_\alpha)\}$ is an oriented atlas on $M$ and $\omega_\alpha := \varphi_\alpha^*(dx^1\wedge\cdots\wedge dx^n)$ is the coordinate top-form pulled back to $U_\alpha$, then on each overlap $U_\alpha \cap U_\beta$, $\omega_\alpha = J_{\alpha\beta}\omega_\beta$ with $J_{\alpha\beta} = \det D(\varphi_\beta\circ\varphi_\alpha^{-1})^{-1}$, a smooth positive function.
>
> **Hint:** Pullback of $dx^1\wedge\cdots\wedge dx^n$ under a linear (or differentiable) map is the determinant of the map times the same volume form, and an oriented atlas has positive transition Jacobians by definition.
>
> **Why needed:** It supplies the hypothesis of Lemma 2 in the natural case where the local $\omega_\alpha$ come from coordinate top-forms.
>
> > [!note]- Full proof
> > In the overlap, let $\widetilde\varphi := \varphi_\beta\circ\varphi_\alpha^{-1}$, an orientation-preserving [[Def - Diffeomorphism|diffeomorphism]] between open subsets of $\mathbb{R}^n$ (positive Jacobian by the oriented atlas condition). For any $n$-form $\alpha$ on $\mathbb{R}^n$, $\widetilde\varphi^*(\alpha) = (\det D\widetilde\varphi^{-1})\alpha$ when both are written in the standard basis $dx^1\wedge\cdots\wedge dx^n$ (this is the standard pullback computation for top-forms). Writing $\omega_\alpha = \varphi_\alpha^*(dx^1\wedge\cdots\wedge dx^n)$ and similarly for $\omega_\beta$, and using $\varphi_\alpha = \widetilde\varphi^{-1}\circ\varphi_\beta$, we get $\omega_\alpha = \varphi_\beta^*(\widetilde\varphi^*)^{-1}(dx^1\wedge\cdots\wedge dx^n) = (\det D\widetilde\varphi)^{-1}\omega_\beta$ in components, so $J_{\alpha\beta} = (\det D\widetilde\varphi)^{-1} > 0$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** A smooth $n$-manifold $M$ ($n \geq 1$) is orientable iff there exists a nowhere-vanishing smooth $n$-form $\omega \in \Omega^n(M)$.
>
> **($\Leftarrow$) Assume $\omega \in \Omega^n(M)$ is smooth and nowhere vanishing.** By Lemma 1, the assignment $p \mapsto \mathcal{O}_p :=$ (the orientation of $T_pM$ determined by $\omega_p$) is a continuous pointwise orientation, hence an orientation of $M$ in the sense of [[Def - Orientation of a Smooth Manifold]].
>
> **($\Rightarrow$) Assume $M$ is orientable, with a chosen orientation $\mathcal{O}$.** By the equivalence in [[Def - Oriented Atlas]], there is an oriented atlas $\{(U_\alpha, \varphi_\alpha)\}$ — a smooth atlas with all transition Jacobians positive. By [[Thm - Existence of Smooth Partitions of Unity]] (using paracompactness, which follows from second-countability and Hausdorff), there is a smooth partition of unity $\{\psi_\alpha\}$ subordinate to this cover.
>
> Define $\omega_\alpha := \varphi_\alpha^*(dx^1\wedge\cdots\wedge dx^n)$ on $U_\alpha$. Each $\omega_\alpha$ is a smooth nowhere-vanishing $n$-form on $U_\alpha$. By Lemma 3, on overlaps $U_\alpha \cap U_\beta$, $\omega_\alpha = J_{\alpha\beta}\omega_\beta$ with $J_{\alpha\beta} > 0$ smooth.
>
> Define
> $$\omega := \sum_\alpha\psi_\alpha\omega_\alpha \in \Omega^n(M),$$
> the sum extended by zero outside each $U_\alpha$. By Lemma 2, $\omega$ is smooth and nowhere vanishing.
>
> Finally, $\omega$ determines the *original* orientation $\mathcal{O}$ (not its opposite): at each $p$ in the domain of a positively-oriented chart $U_\beta$, $\omega_p$ is a positive multiple of $\omega_\beta(p) = (dx^1\wedge\cdots\wedge dx^n)_p$, which is the positively-oriented coordinate top-form. Hence $\omega_p$ determines the orientation $[\mathcal{O}_p]$ on $T_pM$. So $\omega$ is a positively-oriented volume form for $\mathcal{O}$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Algebraic topology: $w_1$ as the orientation obstruction.** The first Stiefel–Whitney class $w_1(M) \in H^1(M; \mathbb{Z}/2)$ classifies the orientability of $M$: $w_1(M) = 0$ iff $M$ is orientable. Computing $w_1$ for specific manifolds (often via the line bundle $\Lambda^n(T^*M)$) is a cohomology exercise that, by this theorem, computes the existence of a nowhere-vanishing top-form. *Application:* compute $w_1$ for $\mathbb{RP}^n$ and verify it is nonzero exactly when $n$ is even.

**Complex geometry: orientation from complex structure.** Every complex manifold $M^{2n}$ (real [[Def - Dimension|dimension]] $2n$, with a $\mathrm{GL}(n, \mathbb{C})$ structure) is orientable, because $\mathrm{GL}(n, \mathbb{C}) \subset \mathrm{GL}_+(2n, \mathbb{R})$. Construct an explicit nowhere-vanishing $(2n)$-form on $\mathbb{C}^n$ and on $\mathbb{CP}^n$. The form on $\mathbb{C}^n$ is $dz^1\wedge d\bar z^1\wedge\cdots\wedge dz^n\wedge d\bar z^n$ (up to a real-imaginary normalization); on $\mathbb{CP}^n$ it is the top power of the Fubini–Study Kähler form.

**Group theory and Lie [[Def - Group|groups]]: parallelizability of Lie groups.** Every Lie group has a global frame given by a basis of left-invariant vector fields (a basis of the Lie algebra, left-translated). The wedge of the dual coframe is a nowhere-vanishing top-form. *Application:* explicitly construct the Haar form on $\mathrm{SO}(3)$ or $\mathrm{SU}(2)$ from a basis of left-invariant 1-forms (using the matrix entries).

**Topology: orientability of quotient manifolds.** A quotient $M/G$ by a free, properly discontinuous group action is orientable iff $M$ is orientable and $G$ acts by orientation-preserving [[Def - Diffeomorphism|diffeomorphisms]]. *Application:* the cylinder $\mathbb{R}^2 / \mathbb{Z}$ (acting by $(x, y) \mapsto (x + 1, y)$) is orientable; the Möbius strip $\mathbb{R}^2 / \mathbb{Z}$ (acting by $(x, y) \mapsto (x + 1, -y)$) is non-orientable.

---

# Bridges

- **[[Def - Orientation of a Smooth Manifold]]** — this theorem is the **proof of the equivalence** between the pointwise-orientation definition and the top-form definition of orientation. The two formulations are sometimes used interchangeably, but the proof of their equivalence is non-trivial in the forward direction (it requires partition of unity). Without this theorem, the three formulations would be three separate hypotheses; with it, they are one.

- **[[Def - Volume Form]]** — a volume form is by definition a nowhere-vanishing smooth top-form. This theorem says: the manifold admits a volume form iff it is orientable. So "volume form" and "orientation" are essentially the same data, differing only in that orientations are equivalence classes (under positive function multiplication) of volume forms.

- **[[Thm - Existence of the Riemannian Volume Form]]** — adding a Riemannian metric to an oriented manifold uniquely picks out a *canonical* representative within the orientation class — the Riemannian volume form $\omega_g$. So the orientability criterion plus a metric gives a canonical volume form, not just an equivalence class.

- **First Stiefel–Whitney class $w_1$** *(from algebraic topology)* — orientability of $M$ is equivalent to the vanishing of a single cohomology class $w_1(TM) \in H^1(M; \mathbb{Z}/2)$. This theorem provides the differential-geometric translation: $w_1 = 0$ iff a nowhere-vanishing top-form exists. The two formulations are different views of the same obstruction.

- **Orientation double cover** *(from algebraic topology)* — every non-orientable manifold has a canonical 2-sheeted covering on which the pullback orientation does exist. By this theorem, the pullback orientation corresponds to a nowhere-vanishing top-form *on the cover*, even though no such form exists downstairs. The deck transformation swaps the two equivalence classes of top-forms on the cover.

- **Parallelizability** *(strictly stronger condition)* — a parallelizable manifold (one admitting a global frame) automatically gives a global nowhere-vanishing top-form (wedge the dual coframe). The converse fails: $S^2$ admits a nowhere-vanishing 2-form (the area form) but no global frame, by the hairy ball theorem. So parallelizability implies orientability, but not conversely.

---

# Unlocked by This

> [!tip] de Rham Cohomology of Closed Orientable Manifolds *(from Algebraic Topology)*
> For a compact orientable manifold $M^n$ without boundary, the integral of a positively-oriented volume form is positive, so by Stokes the form is not exact. Hence $H^n_{dR}(M) \neq 0$ for every closed orientable $M$. This is the topological consequence: the top de Rham cohomology of a closed orientable manifold is at least one-dimensional, generated by the volume form.

> [!tip] Poincaré Duality *(from Algebraic Topology)*
> On a closed oriented $n$-manifold, the wedge-and-integrate pairing $H^k_{dR}(M) \times H^{n-k}_{dR}(M) \to \mathbb{R}$ is non-degenerate — **Poincaré duality**. The non-vanishing of the integration functional, established by the existence of a positively-oriented volume form (this theorem) plus Stokes, is what makes this pairing work.

> [!tip] Hodge Star *(from Differential Geometry / Hodge Theory)*
> On an oriented Riemannian $n$-manifold, the Hodge star $\star : \Omega^k \to \Omega^{n-k}$ is defined by $\alpha\wedge\star\beta = \langle\alpha,\beta\rangle_g\omega_g$, where $\omega_g$ is the Riemannian volume form. The existence of $\omega_g$ — and thereby of $\star$ — requires the orientation, which (by this theorem) is the existence of a nowhere-vanishing top-form.
