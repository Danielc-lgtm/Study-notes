---
type: exercise
subject: hodge-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Bochner's Theorem"
  - "Def - Riemannian Manifold"
  - "Thm - Harmonic Forms Represent de Rham Cohomology"
tags: [geometry, hodge-theory, riemannian-geometry, curvature]
---

# Problem Statement

(a) Show that the round $n$-sphere $S^n$ (with the standard round metric of constant sectional curvature $1$) has Ricci tensor $\operatorname{Ric}_{S^n} = (n - 1)g$ (where $g$ is the round metric). Conclude that $\operatorname{Ric} > 0$ on $S^n$. Apply [[Thm - Bochner's Theorem|Bochner's theorem]] to conclude $b_1(S^n) = 0$. Verify directly from the de Rham complex on $S^n$ that $H^1_{dR}(S^n) = 0$ for $n \geq 2$.

(b) Show that the flat $n$-torus $T^n$ has $\operatorname{Ric} = 0$ (Ricci-flat) but $b_1(T^n) = n$. Discuss why this does *not* contradict Bochner: positive Ricci is needed, not just nonnegative. Verify that the harmonic $1$-forms on $T^n$ (the constant-coefficient $1$-forms $\sum c_i dx^i$) are **parallel** ($\nabla h = 0$), consistent with the nonnegative-Ricci corollary of Bochner.

(c) Discuss why the hyperbolic space form $\mathbb{H}^n/\Gamma$ (for a closed orientable hyperbolic $n$-manifold) is *not* covered by Bochner's theorem. Closed hyperbolic surfaces have $b_1 = 2g$ (the genus contribution), which can be arbitrarily large. Show that the hyperbolic space $\mathbb{H}^n$ has $\operatorname{Ric} = -(n-1)g$ (negative Ricci), so Bochner does not apply. The example shows positivity of $\operatorname{Ric}$ is essential.

(d) State and outline the proof of a Bochner-type sharpness: a closed Riemannian $n$-manifold with $\operatorname{Ric} \geq 0$ and $b_1 = n$ is a flat torus quotient.

**Recall:**

[[Thm - Bochner's Theorem|Bochner's theorem]]: a closed Riemannian manifold with $\operatorname{Ric} > 0$ has $b_1 = 0$. The corollary: if $\operatorname{Ric} \geq 0$ (nonnegative), harmonic $1$-forms are parallel, and $b_1 \leq n$ with equality forcing a flat torus quotient.

![[Thm - Bochner's Theorem#Statement]]

The Ricci tensor $\operatorname{Ric}$ of a Riemannian manifold is a symmetric $(0, 2)$-tensor obtained by tracing the Riemann curvature tensor on the first and third indices: $R_{ij} = R^k{}_{ikj}$. **Positive Ricci** means $\operatorname{Ric}(X, X) > 0$ for all $X \neq 0$ at every point; **nonnegative Ricci** means $\operatorname{Ric}(X, X) \geq 0$.

For a Riemannian manifold of constant sectional curvature $K$, the Riemann tensor is $R_{ijkl} = K(g_{ik}g_{jl} - g_{il}g_{jk})$, and the Ricci tensor is $\operatorname{Ric} = (n - 1)K\cdot g$. So $S^n$ ($K = +1$) has $\operatorname{Ric} = (n-1)g > 0$; the flat $\mathbb{R}^n/T^n$ ($K = 0$) has $\operatorname{Ric} = 0$; hyperbolic $\mathbb{H}^n$ ($K = -1$) has $\operatorname{Ric} = -(n-1)g < 0$.

---

# Convergent Strategy

**Problem class:** Application of Bochner's theorem to specific manifolds, with the goal of understanding the sharpness of the curvature hypothesis. The chapter's problem-solving strategy on "curvature-Betti inequalities via Weitzenböck + integration" (operation 10 from the topic page) applies directly.

**Assumption pattern:** Specific Riemannian manifolds with explicit curvature: $S^n$ (positive Ricci), $T^n$ (zero Ricci), $\mathbb{H}^n/\Gamma$ (negative Ricci). The Ricci tensor is computed from the constant sectional curvature in each case. The Betti numbers are known topologically.

**Theorem routing:** Apply [[Thm - Bochner's Theorem]] directly to $S^n$: positive Ricci forces $b_1 = 0$. Verify topologically. For $T^n$, apply the corollary of Bochner: nonnegative Ricci forces parallel $1$-forms, $b_1 \leq n$. For $\mathbb{H}^n/\Gamma$, observe that Bochner does *not* apply (negative Ricci), so no Bochner-style restriction on $b_1$. The arbitrarily large $b_1$ of hyperbolic manifolds is consistent.

**Key decision point:** Recognize that **the sharpness of Bochner's theorem is in the strict-positivity hypothesis**. Without positivity ($\operatorname{Ric} = 0$ on the torus), the theorem gives only parallelism, not vanishing — and parallel $1$-forms have dimension $\leq n$ but can saturate the bound. The torus is the rigidity case: $b_1 = n$ exactly, with the flat structure being forced. Anything with $\operatorname{Ric} < 0$ somewhere or strictly negative gives no Bochner constraint — explaining why hyperbolic manifolds can have arbitrarily large $b_1$.

---

# Legal Operations Used

1. **Compute the Ricci tensor from constant sectional curvature** (operation: $\operatorname{Ric} = (n-1)K\cdot g$ for constant sectional curvature $K$). Direct application for each manifold.

2. **Apply Bochner's theorem to positive-Ricci manifolds** (operation 10 from the topic page). For $S^n$ ($n \geq 2$), positive Ricci gives $b_1 = 0$.

3. **Verify by direct topological computation** when possible. $H^1_{dR}(S^n) = 0$ for $n \geq 2$ from the de Rham cohomology of spheres.

4. **Use the corollary for nonnegative Ricci**: harmonic $1$-forms are parallel, $b_1 \leq n$. For $T^n$, this is saturated.

5. **Recognize when Bochner does NOT apply** (negative Ricci) and provide examples (hyperbolic surfaces) showing the necessity of the positivity hypothesis.

---

# Hints

> [!note]- Hint 1
> For part (a), use $\operatorname{Ric} = (n-1)K\cdot g$ with $K = 1$ on $S^n$. Verify positivity is strict, then apply Bochner. For the direct cohomology check: the de Rham cohomology of $S^n$ is $\mathbb{R}$ in degrees $0$ and $n$, zero elsewhere — in particular $H^1 = 0$ for $n \geq 2$.

> [!note]- Hint 2
> For part (b), $T^n$ has $K = 0$ (flat), so $\operatorname{Ric} = 0$. Bochner with strict positivity does not apply. The corollary (nonnegative Ricci, harmonic $1$-forms parallel) gives $b_1 \leq n$, and from [[Ex - Harmonic 1-Forms on the Torus]] we know $b_1(T^n) = n$. The harmonic $1$-forms are constant-coefficient $\sum c_i dx^i$, which are parallel (constant components, flat connection).

> [!note]- Hint 3
> For part (c), $\mathbb{H}^n$ has $K = -1$, so $\operatorname{Ric} = -(n-1)g < 0$. Bochner does not apply. Closed hyperbolic surfaces $\Sigma_g$ of genus $g$ have $b_1 = 2g$; for $g \geq 2$ they admit a hyperbolic metric, and $b_1 = 2g$ can be arbitrarily large. So negative Ricci is consistent with large $b_1$, confirming the necessity of positivity in Bochner.

---

# Solution

The exercise has four parts. Part (a) applies Bochner directly to the sphere. Part (b) shows the torus saturates the nonnegative-Ricci corollary. Part (c) shows negative Ricci gives no constraint. Part (d) discusses the rigidity case.

**Step 1: Bochner on the sphere (part (a)).**

> [!note]- Derivation
> The round $S^n$ has constant sectional curvature $K = 1$. The Ricci tensor for constant sectional curvature $K$ is $\operatorname{Ric} = (n-1)K\cdot g$. So $\operatorname{Ric}_{S^n} = (n-1)g$.
>
> For $n \geq 2$, $(n - 1) \geq 1 > 0$, so $\operatorname{Ric}(X, X) = (n-1)g(X, X) = (n-1)|X|^2_g > 0$ for $X \neq 0$. Strictly positive Ricci.
>
> By [[Thm - Bochner's Theorem|Bochner's theorem]], $b_1(S^n) = 0$ for $n \geq 2$.
>
> Direct topological verification: The de Rham cohomology of $S^n$ is
> $$H^k_{dR}(S^n) = \begin{cases}\mathbb{R} & k = 0\text{ or }k = n,\\ 0 & 0 < k < n.\end{cases}$$
> In particular, $H^1_{dR}(S^n) = 0$ for $n \geq 2$. ✓ This is consistent with Bochner.
>
> The case $n = 1$ ($S^1$): $\operatorname{Ric} = 0\cdot g = 0$ (no positivity), and indeed $b_1(S^1) = 1$. Bochner does not apply, consistent.

**Step 2: Torus saturates nonnegative Bochner (part (b)).**

> [!note]- Derivation
> The flat $n$-torus $T^n = \mathbb{R}^n/\mathbb{Z}^n$ inherits the flat Euclidean metric, which has $K = 0$ (flat). So $\operatorname{Ric} = (n-1)\cdot 0\cdot g = 0$ — Ricci-flat.
>
> The strict Bochner does not apply ($\operatorname{Ric} = 0$ is not strictly positive). The nonnegative corollary: harmonic $1$-forms are parallel, $b_1(T^n) \leq n$.
>
> From [[Ex - Harmonic 1-Forms on the Torus]], $\mathcal{H}^1(T^n) = \{$ constant-coefficient $1$-forms $\sum c_i dx^i : c_i \in \mathbb{R}\}$, with dimension $n$. So $b_1(T^n) = n$, *saturating* the Bochner bound.
>
> Verify parallel: the constant-coefficient $1$-form $h = \sum c_i dx^i$ on the flat torus has covariant derivative $\nabla h = 0$, since the Levi-Civita connection of the flat metric has zero Christoffel symbols and the coefficients are constants. ✓
>
> No contradiction with Bochner: the strict version of Bochner requires $\operatorname{Ric} > 0$, which excludes the Ricci-flat case. The torus is the rigidity example for the nonnegative version.

**Step 3: Hyperbolic spaces beyond Bochner (part (c)).**

> [!note]- Derivation
> Hyperbolic $n$-space $\mathbb{H}^n$ has constant sectional curvature $K = -1$ (negative). So $\operatorname{Ric}_{\mathbb{H}^n} = (n-1)(-1)g = -(n-1)g$. Negative-definite Ricci.
>
> A closed hyperbolic $n$-manifold $\mathbb{H}^n/\Gamma$ (for $\Gamma$ a torsion-free cocompact discrete subgroup of $\mathrm{Isom}(\mathbb{H}^n)$) inherits the negative-Ricci metric: $\operatorname{Ric}_{\mathbb{H}^n/\Gamma} = -(n-1)g < 0$.
>
> Bochner's theorem (which requires $\operatorname{Ric} > 0$) does *not* apply. There is no Bochner-style restriction on $b_1$.
>
> Example: closed hyperbolic surfaces $\Sigma_g$ (genus $g \geq 2$) have $b_1 = 2g$, which can be arbitrarily large by varying $g$. As $g \to \infty$, $b_1\to\infty$, with all of these being closed Riemannian $2$-manifolds with strictly negative Ricci. This shows that positive Ricci is *essential* for Bochner — without it, $b_1$ is unconstrained.
>
> Sharpness conclusion: Bochner is tight in the sense that
> - $\operatorname{Ric} > 0 \Rightarrow b_1 = 0$ (strict Bochner).
> - $\operatorname{Ric} \geq 0 \Rightarrow b_1 \leq n$ with equality iff flat torus quotient (nonnegative corollary).
> - $\operatorname{Ric} \not\geq 0$ somewhere $\Rightarrow$ no Bochner constraint, $b_1$ can be arbitrarily large.
>
> The three cases ($S^n$, $T^n$, hyperbolic) exhibit all three regimes.

**Step 4: Rigidity case (part (d)).**

> [!note]- Derivation
> **Claim:** A closed Riemannian $n$-manifold with $\operatorname{Ric} \geq 0$ and $b_1 = n$ is a flat torus quotient $T^n/\Gamma$ for a finite group $\Gamma$.
>
> **Outline:** By the nonnegative-Bochner corollary, harmonic $1$-forms are parallel. The space of parallel $1$-forms has dimension $\leq n$ (since parallel sections of $T^*M$ are determined by their value at one point). If $b_1 = n$, equality, so the space of parallel $1$-forms is all of $T^*_p M$ at each $p$ — the cotangent bundle is **parallelizable** with a parallel frame.
>
> A parallel frame implies the Levi-Civita connection is *flat* (curvature tensor is zero). A closed Riemannian manifold with flat connection is locally isometric to Euclidean $\mathbb{R}^n$ (by the **Cartan structure theorem**), hence its universal cover is $\mathbb{R}^n$ with the flat metric. The fundamental group $\pi_1(M)$ acts on $\mathbb{R}^n$ by isometries (Euclidean motions: translations and rotations).
>
> Since $M$ is closed and $\pi_1(M)$ acts freely and cocompactly on $\mathbb{R}^n$, and the action is by Euclidean motions, $\pi_1(M)$ is a **crystallographic group** (Bieberbach group). By **Bieberbach's first theorem**, $\pi_1(M)$ has a normal subgroup of finite index consisting of translations — a finite-index lattice in $\mathbb{R}^n$. Hence $M$ is finitely covered by a flat torus $T^n$, i.e., $M = T^n/\Gamma$ for a finite group $\Gamma$.
>
> Conversely, every flat torus quotient $T^n/\Gamma$ has $\operatorname{Ric} = 0$ and $b_1 = n$ (the first by flatness, the second by the same Fourier-analysis argument as on the torus, suitably modified).

> [!note]- Complete formal solution
> **Part (a):** $\operatorname{Ric}_{S^n} = (n-1)g > 0$ for $n \geq 2$. By Bochner, $b_1(S^n) = 0$. Verified topologically: $H^1_{dR}(S^n) = 0$ for $n \geq 2$ (from the de Rham complex of the sphere).
>
> **Part (b):** $\operatorname{Ric}_{T^n} = 0$. Strict Bochner does not apply; nonnegative corollary gives $b_1 \leq n$. Direct computation from [[Ex - Harmonic 1-Forms on the Torus]]: $b_1(T^n) = n$, saturating the bound. Harmonic $1$-forms (constant-coefficient) are parallel, consistent with the corollary.
>
> **Part (c):** $\operatorname{Ric}_{\mathbb{H}^n} = -(n-1)g < 0$. Bochner does not apply. Closed hyperbolic surfaces $\Sigma_g$ have $b_1 = 2g$, arbitrarily large. Confirms necessity of positive Ricci in Bochner.
>
> **Part (d):** Closed Riemannian manifold with $\operatorname{Ric} \geq 0$ and $b_1 = n$ has parallelizable cotangent bundle (parallel frame), hence flat connection. By Cartan structure + Bieberbach, $M = T^n/\Gamma$ for finite $\Gamma$. $\qquad\blacksquare$

---

# Key Takeaways

**Bochner's theorem is sharp at the strict-positivity boundary.** The sharpness of Bochner is well-illustrated by the three examples: strict $\operatorname{Ric} > 0$ (sphere) forces $b_1 = 0$; nonnegative $\operatorname{Ric} \geq 0$ (torus) allows $b_1 \leq n$ with equality forced; mixed-sign or strictly negative $\operatorname{Ric}$ (hyperbolic) gives no constraint. The transition from "vanishing" to "bounded" to "unconstrained" mirrors the transition from strict positivity to nonnegativity to negativity in the curvature hypothesis. This is the prototype of "curvature determines topology" theorems: a strict curvature inequality gives a vanishing theorem, a weak inequality gives a rigidity theorem, no inequality gives no theorem.

**Negative Ricci is fundamentally different from positive Ricci.** The standard model for closed manifolds with positive Ricci is the sphere (simply connected, $b_1 = 0$, finite $\pi_1$); for closed manifolds with negative Ricci, it is the hyperbolic space form (with large $\pi_1$, large $b_1$). The dichotomy: positive Ricci forces topology to be "small" (Myers + Bochner: compact, finite $\pi_1$, $b_1 = 0$); negative Ricci is consistent with arbitrarily complicated topology. The geometric reason: positive Ricci is a "convexity" condition that constrains manifolds to be simply connected and small; negative Ricci is a "hyperbolic spreading" that allows arbitrary complexity. The Bochner technique is one-sided: it works for positivity, not for negativity.

**Rigidity cases — saturating an inequality forces a flat structure.** The corollary "if $\operatorname{Ric} \geq 0$ and $b_1 = n$, then $M$ is a flat torus quotient" is a **rigidity theorem**. Among closed Riemannian manifolds with nonnegative Ricci and maximal $b_1$, only flat structures are allowed. This is a general pattern in geometric analysis: an inequality is an obstruction, and the equality case is a rigidity statement — the only spaces that *achieve* the bound are highly constrained. The deformation theory of metrics near a flat torus is then constrained: any small perturbation that maintains $\operatorname{Ric} \geq 0$ either keeps the manifold flat or drops $b_1$. Rigidity theorems are how geometric analysis identifies the extremal cases of its inequalities.

This exercise complements [[Thm - Bochner's Theorem]] (the abstract statement) and [[Ex - Harmonic 1-Forms on the Torus]] (the rigidity-case computation on the flat torus). The Bochner technique generalizes to higher-degree harmonic forms (with Riemann curvature constraints), to harmonic spinors (with scalar curvature constraints — Lichnerowicz), and to bundle-valued harmonic forms (with Hermitian curvature constraints — Kodaira vanishing). The general pattern is "Weitzenböck + integration on closed manifold + curvature positivity → vanishing".
