---
type: exercise
subject: differential-geometry
difficulty: "⭐"
prereqs:
  - "Def - Cotangent Space and Cotangent Bundle"
  - "Def - Local Frame"
  - "Def - Dual Basis"
  - "Def - Covector Field and Differential 1-Form"
tags: [geometry, differential-geometry, coordinate-frame, dual-frame]
---

# Problem Statement

Let $(U, \varphi)$ be a smooth chart on a smooth $n$-manifold $M$, with coordinate functions $x^1, \dots, x^n$ and coordinate vector fields $\partial/\partial x^1, \dots, \partial/\partial x^n$. The **coordinate covector fields** $dx^j$ are defined by the property
$$dx^j_p \left( \frac{\partial}{\partial x^i}\bigg|_p \right) = \delta^j_i \quad \text{for every } p \in U \text{ and every } i, j \in \{1, \dots, n\}.$$
Show that:
(a) Each $dx^j$ is a smooth local section of the cotangent bundle $T^*M$ over $U$.
(b) $(dx^1, \dots, dx^n)$ is a smooth local frame for $T^*M$ over $U$.

**Recall:**

$T^*M$ is the [[Def - Cotangent Space and Cotangent Bundle|cotangent bundle]]; smooth sections are [[Def - Covector Field and Differential 1-Form|1-forms]]. A [[Def - Local Frame|local frame]] for a rank-$n$ bundle on $U$ is an $n$-tuple of smooth local sections whose values are a basis of each fibre on $U$.

By [[Def - Dual Basis]], the dual basis $(\varphi^j)$ to a basis $(v_i)$ of a finite-dimensional vector space is uniquely characterized by $\varphi^j(v_i) = \delta^j_i$. So the $dx^j|_p$ are the dual basis to $\partial/\partial x^i|_p$ at each $p \in U$.

---

# Convergent Strategy

**Problem class:** Verification that a candidate frame is a smooth local frame for a vector bundle. The strategy is: (1) verify each member is a smooth local section; (2) verify they are pointwise linearly independent.

**Assumption pattern:** The coordinate vector fields $(\partial/\partial x^i)$ are known to be a smooth local frame for $TM$ over $U$ (a basic property of charts). By duality, the $dx^j$ should be a smooth local frame for $T^*M$ over $U$. The proof formalizes this expectation.

**Theorem routing:** Use the dual-basis identity $dx^j(\partial/\partial x^i) = \delta^j_i$ to verify both smoothness (which reduces to the smoothness of the inverse of the smooth $\mathrm{GL}(n, \mathbb{R})$-valued function defining the coordinate frame on $TM$) and pointwise linear independence (which reduces to the linear-algebraic fact that the dual basis to a basis is linearly independent).

**Key decision point:** The substantive step is recognizing that "$dx^j$ is a smooth section" requires more than the pointwise definition — it requires checking that the function $p \mapsto dx^j_p$ varies smoothly. The argument uses the smoothness of matrix inversion on $\mathrm{GL}(n, \mathbb{R})$, in line with [[Thm - Local Frames Span Sections]].

---

# Legal Operations Used

1. **Operation 4 from the topic page (write a section in a local frame).** Use the coordinate frame $(\partial/\partial x^i)$ on $TM$ as the input frame; the dual coframe is what we're constructing.

2. **Operation 10 from the topic page (take the dual bundle to flip variance).** $T^*M$ is the dual of $TM$; the dual frame is the natural local frame.

3. **Pointwise linear independence as a consequence of dual-basis biorthogonality.** Standard linear algebra.

---

# Hints

> [!note]- Hint 1
> First check that each $dx^j_p$ is uniquely well-defined as a covector at $p$ — this follows from the linear-map extension lemma applied to the basis $\partial/\partial x^i|_p$.

> [!note]- Hint 2
> For smoothness of $dx^j$ as a section: in the chart-induced trivialization $\Phi$ of $T^*M$ over $U$, the dual coframe corresponds to the standard basis of $\mathbb{R}^n$ at each point — the trivialization is built precisely so that this is the case.

> [!note]- Hint 3
> For the frame property: the $(dx^j|_p)$ are the dual basis to the basis $(\partial/\partial x^i|_p)$ at each $p$, hence a basis of $T_p^*M$ by the standard linear-algebraic theorem on dual bases.

---

# Solution

**Plan:** Show that each $dx^j$ is well-defined pointwise as a covector. Verify smoothness by showing $dx^j$ corresponds to the constant section $p \mapsto (p, e_j)$ in the cotangent-bundle trivialization induced by the chart. The frame property follows from the standard duality of bases in linear algebra.

**Step 1: Each $dx^j_p$ is a well-defined covector at $p$.**

> [!note]- Derivation
> At each $p \in U$, the coordinate vector fields evaluated at $p$ — $\partial/\partial x^1|_p, \dots, \partial/\partial x^n|_p$ — form a basis of $T_pM$. By [[Def - Dual Basis]] (applied to the finite-dimensional vector space $T_pM$ with this basis), there exists a unique dual basis $(\omega^1_p, \dots, \omega^n_p)$ of $T_p^*M$ satisfying $\omega^j_p(\partial/\partial x^i|_p) = \delta^j_i$. By construction, $dx^j_p := \omega^j_p$ is precisely this dual basis element. So $dx^j_p$ is a well-defined covector at $p$.

**Step 2: The cotangent-bundle trivialization induced by the chart sends $dx^j$ to a constant section.**

> [!note]- Derivation
> The cotangent bundle $T^*M$ has the smooth structure given by [[Thm - The Cotangent Bundle is a Smooth Manifold]]. In the chart $(U, x^i)$, the canonical trivialization
> $$\Phi : \pi^{-1}(U) \to U \times \mathbb{R}^n, \quad \omega_i \, dx^i|_p \mapsto (p, \omega_1, \dots, \omega_n)$$
> is exactly the assignment of components in the dual coframe basis. Applying this to the covector field $dx^j$: at each $p$, $dx^j|_p$ has component $1$ in the $j$-th slot and $0$ elsewhere (by definition of the dual basis), so $\Phi(dx^j|_p) = (p, 0, \dots, 1, \dots, 0)$ with $1$ in the $j$-th position. As a map $p \mapsto \Phi(dx^j|_p) = (p, e_j)$, this is the constant section over the trivialization — manifestly smooth.

**Step 3: $dx^j$ is a smooth section of $T^*M$ over $U$.**

> [!note]- Derivation
> By Step 2, the composition $\Phi \circ dx^j : U \to U \times \mathbb{R}^n$, $p \mapsto (p, e_j)$, is smooth (the second component is constant). Since $\Phi$ is a [[Def - Diffeomorphism|diffeomorphism]] (by the local-trivialization condition on $T^*M$), $dx^j = \Phi^{-1} \circ (p \mapsto (p, e_j))$ is also smooth. So $dx^j \in \Gamma(U, T^*M) = \Omega^1(U)$.

**Step 4: $(dx^1, \dots, dx^n)$ is a smooth local frame for $T^*M$ over $U$.**

> [!note]- Derivation
> At each $p \in U$, the values $dx^1|_p, \dots, dx^n|_p$ are the dual basis to $\partial/\partial x^1|_p, \dots, \partial/\partial x^n|_p$ (by Step 1). By the standard linear-algebraic theorem ([[Thm - Dimension of Dual Space]]), the dual basis of a basis is itself a basis of the dual space. So $dx^1|_p, \dots, dx^n|_p$ form a basis of $T_p^*M$ at every $p \in U$.
>
> Combined with Step 3 ($dx^j$ are smooth), the $n$-tuple $(dx^1, \dots, dx^n)$ is a smooth local frame for $T^*M$ over $U$ — see [[Def - Local Frame]].

> [!note]- Complete formal solution
> **Setup.** $(U, \varphi)$ is a smooth chart on $M$ with coordinates $x^1, \dots, x^n$. The coordinate vector fields $(\partial/\partial x^i)$ are a smooth local frame for $TM$ over $U$. We construct the dual coframe.
>
> **Step 1: Pointwise definition.** At each $p \in U$, $(\partial/\partial x^i|_p)$ is a basis of $T_pM$. By [[Def - Dual Basis]], the dual basis $(dx^j|_p)$ of $T_p^*M$ exists and is uniquely determined by $dx^j|_p(\partial/\partial x^i|_p) = \delta^j_i$.
>
> **Step 2: Smoothness.** The chart-induced trivialization $\Phi : \pi^{-1}(U) \to U \times \mathbb{R}^n$ of the cotangent bundle (see [[Thm - The Cotangent Bundle is a Smooth Manifold]]) sends $\omega_i dx^i|_p$ to $(p, \omega_1, \dots, \omega_n)$. So $\Phi(dx^j|_p) = (p, e_j)$ — the constant assignment of the $j$-th standard basis vector. The map $p \mapsto (p, e_j)$ is smooth (the second component is constant). Composing with $\Phi^{-1}$ (smooth, as $\Phi$ is a diffeomorphism), the section $dx^j : U \to T^*M$, $p \mapsto dx^j|_p$ is smooth.
>
> **Step 3: Frame property.** At every $p \in U$, the $(dx^j|_p)$ are the dual basis to $(\partial/\partial x^i|_p)$, hence a basis of $T_p^*M$ ([[Thm - Dimension of Dual Space]]). So $(dx^1, \dots, dx^n)$ is a smooth local frame for $T^*M$ over $U$ — pointwise basis-of-fibre, smoothly varying.
> $\qquad\blacksquare$

---

# Key Takeaways

**The dual coframe is the canonical local frame for the cotangent bundle in any chart.** Every chart on $M$ provides simultaneously a local frame $(\partial/\partial x^i)$ for $TM$ and a dual local coframe $(dx^j)$ for $T^*M$, with the duality relation $dx^j(\partial/\partial x^i) = \delta^j_i$ at every point. This pairing is what makes coordinate-based computations possible: every vector field expands uniquely in $(\partial/\partial x^i)$ with smooth components $X^i$, every 1-form expands uniquely in $(dx^j)$ with smooth components $\omega_j$, and the pairing $\omega(X) = \omega_j X^j$ is the contraction of components.

**The dual coframe smoothness reduces to the smoothness of matrix inversion.** Although the pointwise definition of $dx^j$ as the dual basis is purely linear-algebraic, the *smoothness* of $dx^j$ as a section of $T^*M$ requires the dual basis to vary smoothly with $p$. This is exactly the content of [[Thm - Local Frames Span Sections]]: extracting components from a frame requires the inverse of a smooth $\mathrm{GL}(n, \mathbb{R})$-valued matrix, which is smooth by Cramer's rule. The dual coframe inherits its smoothness from this fact.

**The dual coframe is the natural source of 1-forms expressed in local coordinates.** Every 1-form on $U$ has a unique expression $\omega = \omega_j \, dx^j$ for smooth coefficient functions $\omega_j \in C^\infty(U)$. This is the "tensor calculus index notation" of physics, made rigorous: lower-index components $\omega_j$ are the coefficients in the dual coframe, upper-index components $X^i$ are coefficients in the coordinate frame. The contraction $\omega(X) = \omega_j X^j$ is the pairing of these dual structures.

**Companion exercises:** [[Ex - Computing the Differential in Local Coordinates]] in [[Differential Geometry III — Tangent Vectors and the Differential]] uses the dual basis of the coordinate frame to compute the differential of a smooth map in local coordinates — the same dual-basis tool, applied differently.
