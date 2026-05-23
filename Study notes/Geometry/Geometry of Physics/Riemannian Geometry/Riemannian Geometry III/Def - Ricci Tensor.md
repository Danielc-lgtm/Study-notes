---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Riemann Curvature Tensor"
  - "Def - Sectional Curvature"
tags: [geometry, riemannian-geometry, curvature]
---

# Notation

$(M, g)$ is a Riemannian manifold with [[Def - Riemann Curvature Tensor|Riemann curvature tensor]] $R$. In a local frame $(e_a)$, the components of $R$ are $R^a_{\;bcd}$ defined by $R(e_c, e_d)e_b = R^a_{\;bcd}e_a$. The metric is $g_{ab} = \langle e_a, e_b\rangle$ and its inverse is $g^{ab}$. We use the **Einstein summation convention**: repeated upper/lower indices are summed.

---

# Axiom Motivation

The Riemann tensor is a $(1, 3)$-tensor with many components and a hard-to-visualise structure. We want to extract from it a simpler, lower-rank invariant — one that still carries enough geometric information to support major theorems but is small enough to wield directly in calculations. The natural operation on a tensor is **trace**: pair up one upper and one lower index and sum, producing a lower-rank tensor.

The Riemann tensor $R^a_{\;bcd}$ has one upper index and three lower indices, so a single trace produces a $(0, 2)$-tensor. Of the three possible traces, two give $0$ by the antisymmetry $R^a_{\;bcd} = -R^a_{\;bdc}$:

$$g^{ab}R^a_{\;bcd} = 0 \quad (\text{by antisymmetry in } a, b \text{ of } R_{abcd}), \qquad R^c_{\;bcd} \quad (\text{vanishes if we hit the antisymmetry incorrectly}).$$

The unique non-vanishing trace is $\mathrm{Ric}_{bd} := R^a_{\;bad}$, obtained by contracting the upper index against the *first* lower index. This is the **Ricci tensor**.

The desiderata: the Ricci tensor should be a *symmetric* $(0, 2)$-tensor (so it can be compared to the metric directly via inequalities like $\mathrm{Ric} \ge \lambda g$), and it should have a *transparent geometric interpretation*. Symmetry follows from the pair-swap symmetry of the Riemann tensor: $R_{abcd} = R_{cdab}$ gives $R^a_{\;bad} = R^a_{\;dab}$, i.e., $\mathrm{Ric}_{bd} = \mathrm{Ric}_{db}$. This is *the* place in Riemannian geometry where the pair-swap symmetry is critical — it is what makes "Ricci curvature" the same as "Ricci tensor with both indices in the same position," and what lets us state Bonnet–Myers as a comparison of two symmetric $(0, 2)$-tensors.

The geometric interpretation comes from the orthonormal-frame formula. Choose an orthonormal frame $(e_1, \ldots, e_n)$ at $p$ and consider the unit vector $v = e_i$. Then

$$\mathrm{Ric}(v, v) = R^a_{\;iai} = \sum_{a} \langle R(e_a, e_i)e_i, e_a\rangle = \sum_{a \neq i} K(e_i \wedge e_a),$$

using $\langle R(e_i, e_i)e_i, e_i\rangle = 0$ for the diagonal term and the antisymmetry of $R$ in the first pair. So **the Ricci curvature in the direction $v$ is the sum of the sectional curvatures of the $n-1$ $2$-planes containing $v$.** This is the operational picture: $\mathrm{Ric}(v, v)$ averages curvature over directions transverse to $v$, telling you how a small cloud of geodesics emanating in direction $v$ contracts ($\mathrm{Ric} > 0$) or expands ($\mathrm{Ric} < 0$) relative to flat space.

Why is the Ricci tensor "the right" first trace to consider — why not iterate further to a scalar? Because the global theorems of Riemannian geometry distinguish curvature controls of different strengths. Sectional curvature gives the strongest control (Synge, Cartan–Hadamard); Ricci curvature gives weaker but still substantial control (Bonnet–Myers diameter bound, Bochner vanishing); scalar curvature gives the weakest (Yamabe problem, positive mass theorem in GR). Many theorems hold only at the Ricci-curvature level, not at the scalar-curvature level — for instance, no analogue of Bonnet–Myers holds with scalar curvature.

What if we *strengthened* the definition — say, demanded that $\mathrm{Ric}$ commute with the curvature operator? Doing so would exclude all but the most special manifolds. The Ricci tensor as defined is the universal symmetric bilinear form built from one trace of the Riemann tensor, and that universality is what makes it appear in every comparison and existence theorem.

What if we *weakened* it — say, took only the antisymmetric part of $R^a_{\;bad}$? The antisymmetric part vanishes by the symmetries; only the symmetric part is meaningful. So the definition is essentially forced once you ask for a single trace producing a symmetric tensor.

---

# The Definition

> **Definition (Ricci tensor).** Let $(M, g)$ be a Riemannian manifold with Levi-Civita connection $\nabla$ and Riemann curvature tensor $R$. The **Ricci tensor** is the $(0, 2)$-tensor field
>
> $$\mathrm{Ric}(X, Y) := \mathrm{tr}\bigl(Z \mapsto R(Z, X)Y\bigr).$$
>
> In components, $\mathrm{Ric}_{bd} = R^a_{\;bad}$. The Ricci tensor is **symmetric**: $\mathrm{Ric}(X, Y) = \mathrm{Ric}(Y, X)$.

In an orthonormal frame $(e_1, \ldots, e_n)$ at $p$,

$$\mathrm{Ric}(e_i, e_i) = \sum_{j \neq i} K(e_i \wedge e_j).$$

The **Ricci quadratic form** $v \mapsto \mathrm{Ric}(v, v)$ is the most common form in which the Ricci tensor appears in theorem statements. Bonnet–Myers's hypothesis "$\mathrm{Ric} \ge (n-1)\kappa\, g$" is shorthand for "$\mathrm{Ric}(v, v) \ge (n-1)\kappa\, |v|^2$ for all $v \in TM$."

---

# Relate to Other Fields / Compression

In **general relativity**, the Ricci tensor is one of the two main building blocks of Einstein's field equations. Combined with the metric and scalar curvature, it forms the **Einstein tensor** $G_{ab} = \mathrm{Ric}_{ab} - \tfrac{1}{2}g_{ab}S$, which by the second Bianchi identity is divergence-free. The Einstein equation $G_{ab} = 8\pi T_{ab}$ relates this geometric object to the matter stress-energy. In vacuum ($T = 0$), Einstein's equations reduce to $\mathrm{Ric} = 0$ — the vacuum Einstein equations, which Schwarzschild solves.

In **comparison geometry**, the Ricci tensor controls the Bonnet–Myers diameter bound and Bishop–Gromov volume comparison; positive Ricci curvature on a compact manifold rules out harmonic 1-forms (Bochner).

In **Ricci flow**, the Ricci tensor is the right-hand side of Hamilton's evolution equation $\partial_t g = -2\,\mathrm{Ric}(g)$, the geometric heat equation that drove Perelman's proof of the Poincaré conjecture. The minus sign is chosen so that positively-curved manifolds (with positive Ricci) shrink, and negatively-curved manifolds expand — the flow tries to make Ricci curvature uniform.

**True name:** *The Ricci tensor in the direction $v$ is the sum of sectional curvatures of all $2$-planes containing $v$.* Operationally, $\mathrm{Ric}(v, v)$ is a "directional average" of sectional curvature transverse to $v$. When you have a Ricci hypothesis and want intuition, picture a small cloud of geodesics emanating in direction $v$ from a point: $\mathrm{Ric}(v, v) > 0$ means the cloud focuses faster than in flat space; $\mathrm{Ric}(v, v) < 0$ means it spreads faster.

---

# Examples / Corollaries

**Example 1 (constant sectional curvature).** If $K \equiv K_0$, then $\mathrm{Ric}(v, v) = (n-1)K_0 |v|^2$ for any unit $v$, so $\mathrm{Ric} = (n-1)K_0\, g$ — the Ricci tensor is a scalar multiple of the metric. In particular, $S^n$ has $\mathrm{Ric} = (n-1)g$, $\mathbb{R}^n$ has $\mathrm{Ric} = 0$, $H^n$ has $\mathrm{Ric} = -(n-1)g$.

**Example 2 ($S^2 \times S^2$).** Both factors of the product have sectional curvature $1$ within themselves, but mixed $2$-planes have curvature $0$. For a unit vector $v = (v_1, v_2)$ tangent to the product with $|v_1|^2 + |v_2|^2 = 1$: $\mathrm{Ric}(v, v) = |v_1|^2 \cdot 1 + |v_2|^2 \cdot 1 = 1$. So $\mathrm{Ric} = g$ on $S^2 \times S^2$ — it is an **Einstein manifold**, but *not* of constant sectional curvature.

**Example 3 (a Ricci-flat manifold that is not flat).** **Calabi–Yau** manifolds are compact Kähler manifolds with $\mathrm{Ric} = 0$; the simplest is the **K3 surface** in complex dimension $2$ (real dimension $4$). Their existence was conjectured by Calabi and proved by Yau in $1976$. A Ricci-flat manifold need not have $R = 0$; only the Ricci-trace of $R$ vanishes, while the full $R$ can be highly nontrivial. Calabi–Yau manifolds are the geometric setting for **string compactification** in theoretical physics.

**Example 4 (Schwarzschild).** The **Schwarzschild metric** (a vacuum solution of Einstein's equations) has $\mathrm{Ric} = 0$ in the region $r > 2M$, even though the spacetime is curved (the Riemann tensor is nonzero, with components of order $M/r^3$ — these are the tidal forces near a black hole). This is the prototypical example of a non-flat Ricci-flat manifold (in Lorentzian signature).

**Non-example.** $\mathrm{Ric} > 0$ does **not** imply $K > 0$. The product $S^2 \times S^2$ has $\mathrm{Ric} = g > 0$ but $K = 0$ on mixed $2$-planes. So you cannot upgrade a Ricci bound to a sectional bound; theorems requiring positive sectional curvature (Synge, the sphere theorem) need it explicitly.

**Calibration check.** If you have understood this definition correctly you should be able to: (a) verify $\mathrm{Ric}(v, v) = \sum_{j \neq i} K(e_i \wedge e_j)$ in an orthonormal frame with $v = e_i$; (b) compute $\mathrm{Ric}$ on $S^n$ from $R(X, Y)Z = \langle Y, Z\rangle X - \langle X, Z\rangle Y$ and get $(n-1)g$; (c) prove the Ricci tensor is symmetric using the pair-swap symmetry of the Riemann tensor.

---

# Unlocked by This

> [!tip] Bonnet–Myers Theorem *(from Riemannian Geometry III)*
> The fundamental positive-Ricci global theorem: $\mathrm{Ric} \ge (n-1)\kappa\, g$ on a complete manifold forces compactness, $\mathrm{diam}(M) \le \pi/\sqrt{\kappa}$, and finite fundamental group. See [[Thm - Bonnet-Myers Theorem]].

> [!tip] Einstein Manifolds *(from Riemannian Geometry III)*
> A manifold satisfying $\mathrm{Ric} = \lambda g$ for a constant $\lambda$ is called **Einstein**. These are the "homogeneous in Ricci" manifolds — natural generalisations of constant-curvature manifolds. See [[Def - Einstein Manifold]].

> [!tip] Ricci Flow and the Poincaré Conjecture *(from Geometric Analysis)*
> Hamilton's **Ricci flow** $\partial_t g = -2\,\mathrm{Ric}(g)$ is a geometric heat equation that evolves a Riemannian metric to "homogenise" its Ricci curvature. **Perelman**'s 2002–2003 proof of the **Poincaré conjecture** and **Thurston's geometrization conjecture** for closed $3$-manifolds uses Ricci flow with surgery as the central tool. Every closed $3$-manifold can be decomposed into pieces, each admitting one of eight model geometries, and Ricci flow finds this decomposition.

> [!tip] Bochner Vanishing Theorem *(from Hodge Theory)*
> The Ricci tensor is the curvature term in the **Bochner formula** for harmonic $1$-forms: $\tfrac{1}{2}\Delta|\omega|^2 = |\nabla\omega|^2 + \mathrm{Ric}(\omega^\sharp, \omega^\sharp)$ for harmonic $\omega$. On a compact manifold with $\mathrm{Ric} > 0$, integration gives $0 = \int |\nabla\omega|^2 + \int \mathrm{Ric}(\omega^\sharp, \omega^\sharp)$; both terms are nonnegative, so both vanish, forcing $\omega = 0$. Result: $b_1(M) = 0$ when $\mathrm{Ric} > 0$. See [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition]].

> [!tip] Einstein's Field Equations *(from General Relativity)*
> In **general relativity**, the Ricci tensor enters Einstein's field equations $\mathrm{Ric}_{ab} - \tfrac{1}{2}g_{ab}S = 8\pi T_{ab}$ as the geometric quantity equal to (a combination of) the matter stress-energy. See [[General Relativity I — Einstein's Equations and Schwarzschild]].
