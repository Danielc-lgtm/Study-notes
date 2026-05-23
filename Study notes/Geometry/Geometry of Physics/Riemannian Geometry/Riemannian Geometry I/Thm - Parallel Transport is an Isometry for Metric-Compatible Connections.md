---
type: theorem
subject: riemannian-geometry
prereqs:
  - "Def - Metric-Compatible Connection"
  - "Def - Parallel Transport"
  - "Def - Covariant Derivative along a Curve"
  - "Def - Riemannian Metric"
tags: [geometry, riemannian-geometry, connections, parallel-transport]
---

# Notation

$(M, g)$ — a Riemannian or semi-Riemannian manifold. $\nabla$ — a connection on $TM$. $\gamma : [a, b] \to M$ — a smooth curve from $p = \gamma(a)$ to $q = \gamma(b)$. $P_\gamma : T_pM \to T_qM$ — the [[Def - Parallel Transport|parallel transport operator]] along $\gamma$. $V, W$ — vector fields along $\gamma$, with $V(t), W(t) \in T_{\gamma(t)}M$. Full notation registry on [[Riemannian Geometry I — Connections and Covariant Differentiation]].

---

# Statement

> **Theorem (Parallel Transport is an Isometry).** Let $(M, g)$ be a Riemannian or semi-Riemannian manifold with connection $\nabla$ on $TM$. The following conditions are equivalent:
>
> (i) $\nabla$ is [[Def - Metric-Compatible Connection|metric-compatible]]: $X g(Y, Z) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z)$ for all vector fields $X, Y, Z$;
>
> (ii) for every smooth curve $\gamma$ from $p$ to $q$, the parallel transport operator $P_\gamma : T_pM \to T_qM$ is a **linear isometry**: $g_q(P_\gamma v, P_\gamma w) = g_p(v, w)$ for all $v, w \in T_pM$;
>
> (iii) for every smooth curve $\gamma$ and every pair of parallel vector fields $V, W$ along $\gamma$ (i.e., $\nabla_t V = \nabla_t W = 0$), the inner product $g_{\gamma(t)}(V(t), W(t))$ is constant in $t$.

---

# Motivation

Metric-compatibility is one of the two conditions characterising the Levi-Civita connection — the other being torsion-freeness. The formal definition (a Leibniz rule for the metric, $X g(Y, Z) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z)$) is computationally clean, but its **geometric meaning** is unclear at first reading. This theorem provides the geometric interpretation: metric-compatibility is *exactly* the condition that parallel transport preserves the metric — i.e., parallel transport is an isometry between tangent spaces.

The motivation for this characterisation. The whole point of having a connection is to be able to compare tangent vectors at different points via parallel transport. If the connection preserves the metric, parallel transport carries lengths and angles unchanged — it is a *rigid* motion between the tangent spaces, exactly the kind of comparison one wants for Riemannian geometry. If the connection does not preserve the metric, parallel transport could rescale or shear vectors, in which case "constant velocity along a curve" would not mean "constant speed" and the entire variational picture of geodesics would fail.

The theorem makes precise that the three forms of the condition — (i) the infinitesimal Leibniz rule, (ii) the global isometry of parallel transport, (iii) the constancy of inner products along parallel vectors — are equivalent. The infinitesimal form (i) is what is easy to *verify* (it is a local condition checkable in coordinates); the global form (ii) is what gives the *geometric picture*; the in-between form (iii) is the bridge.

The bridge from (i) to (iii) is the **integrated Leibniz rule**: if $V, W$ are parallel along $\gamma$ ($\nabla_t V = \nabla_t W = 0$), then $\frac{d}{dt}g(V, W) = g(\nabla_t V, W) + g(V, \nabla_t W) = 0$, so $g(V, W)$ is constant. The bridge from (iii) to (ii) is the definition of parallel transport: $P_\gamma v$ is the value at $b$ of the parallel section starting at $v$, so the inner product at $b$ equals the inner product at $a$. The bridge from (ii) to (i) is differentiating the isometry condition with respect to a one-parameter family of curves at $t = 0$.

---

# Sources and Targets

**Sources (Input Broadening)**

*Source 1: the Levi-Civita connection of any Riemannian or semi-Riemannian manifold.* The Levi-Civita connection is metric-compatible by definition, so this theorem applies and tells us parallel transport along any curve is an isometry. This is the most-used application.

*Source 2: any connection on a vector bundle with a fibre metric, where the connection is compatible with the fibre metric.* The same theorem applies in this generality: for $(E, h) \to M$ a vector bundle with fibre metric $h$, and $\nabla$ an $h$-compatible connection (meaning $X h(s, t) = h(\nabla_X s, t) + h(s, \nabla_X t)$), parallel transport along any curve is a linear isometry of $(E_p, h_p) \to (E_q, h_q)$.

*Source 3: the spin connection on a spin manifold.* The Levi-Civita connection lifts to the spinor bundle via the homomorphism $\mathrm{Spin}(n) \to \mathrm{SO}(n)$, and the resulting **spin connection** is compatible with the spinor inner product. Parallel transport of spinors along a curve is therefore a unitary transformation — this is what makes "spin angular momentum" parallel-transportable in general relativity (e.g., for the Dirac equation in curved spacetime).

**Targets (Output Amplification)**

*Target combination 1: Parallel-transport-is-isometry + holonomy ⟹ holonomy is in $O(n)$.* The holonomy group at a point $p$ is the group of parallel-transport maps around loops at $p$. By this theorem, all these maps are isometries of $(T_pM, g_p)$, so the holonomy group is a subgroup of $O(T_pM, g_p) \cong O(n)$ (or $O(p, q)$ in indefinite signature). This is the structural fact behind **Berger's classification**: the holonomy of an irreducible Levi-Civita connection on a simply-connected complete manifold is one of $\mathrm{SO}(n), U(n), SU(n), \mathrm{Sp}(n), \mathrm{Sp}(n)\mathrm{Sp}(1), G_2, \mathrm{Spin}(7)$.

*Target combination 2: Parallel-transport-is-isometry + geodesic equation ⟹ constant speed of geodesics.* A geodesic is a curve with $\nabla_t\dot\gamma = 0$, i.e., $\dot\gamma$ is parallel along $\gamma$. By the theorem, $g(\dot\gamma, \dot\gamma)$ is constant along $\gamma$. So **geodesics have constant speed** — they are uniformly parametrised by their natural parameter (e.g., arc length for unit-speed geodesics).

*Target combination 3: Parallel-transport-is-isometry + Killing fields ⟹ Killing fields give parallel-transport-invariant directions.* A **Killing field** $K$ is a vector field whose flow consists of isometries. Combining with parallel transport being an isometry: along any geodesic, the inner product $g(\dot\gamma, K)$ is conserved, yielding a **Noether-type conservation law** for spacetime symmetries. In Schwarzschild this gives conserved energy and angular momentum used in deriving perihelion precession.

*Target combination 4: Parallel-transport-is-isometry + sectional curvature ⟹ angle deficit equals integrated curvature.* On a 2-dimensional Riemannian manifold, the angle of rotation of a vector parallel-transported around a small closed loop equals the integrated Gaussian curvature over the enclosed region (the local version of Gauss-Bonnet). This is a direct consequence of parallel transport being an isometric rotation in 2-dimensional tangent spaces.

---

# Why Is It True

**Mechanism summary:** **metric-compatibility says $\nabla$ "satisfies the Leibniz rule for $g$", so applying $\frac{d}{dt}$ to the inner product of two parallel vector fields gives $g(\nabla_t V, W) + g(V, \nabla_t W) = 0 + 0 = 0$; integrating, the inner product is constant along the curve.**

The intuition. The Leibniz rule $X g(Y, Z) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z)$ says the derivative of an inner product is the sum of two terms: the derivative of the first factor (paired with the second) plus the derivative of the second factor (paired with the first). This is exactly the product rule of calculus for inner products. Now if $V, W$ are *parallel* — meaning $\nabla_t V = \nabla_t W = 0$ — both terms on the right vanish, leaving $\frac{d}{dt}g(V, W) = 0$. Constant function. So the inner product of parallel vectors is preserved.

Since parallel transport is the operator $P_\gamma : T_pM \to T_qM$ sending $v$ to $V(b)$ (value at end) where $V$ is parallel starting at $v$, and similarly $P_\gamma w = W(b)$ where $W$ is parallel starting at $w$, the inner product preservation reads $g_q(P_\gamma v, P_\gamma w) = g(V(b), W(b)) = g(V(a), W(a)) = g_p(v, w)$. This is the isometry condition.

The converse direction — isometry of parallel transport implies metric-compatibility — is obtained by differentiating: take a one-parameter family of curves and differentiate the isometry condition at $t = 0$ to obtain the infinitesimal Leibniz rule.

---

# What Makes This Hard

The conceptual difficulty is **seeing that the infinitesimal condition (Leibniz rule for $g$) and the global condition (isometric parallel transport) are equivalent**. The Leibniz rule is a *pointwise* condition involving vector fields and a Lie derivative; the isometry of parallel transport is a *global* condition involving the entire curve. The bridge is the integrated Leibniz rule applied to parallel vector fields — which is a clever but non-obvious move. Students often understand both conditions separately without seeing they are the same.

The mechanical hard part is **the converse direction (ii) ⟹ (i)**, which requires differentiating the isometry condition with respect to the curve. This involves choosing the right one-parameter family of curves (typically curves with a common starting point but varying velocity, so that the derivative picks out the infinitesimal Leibniz rule) and carefully tracking the chain rule through parallel transport. The "forward" direction (i) ⟹ (iii) ⟹ (ii) is essentially a one-line argument; the "backward" direction is more delicate.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove (i) ⟹ (iii) by the integrated Leibniz rule. Prove (iii) ⟹ (ii) by the definition of parallel transport. Prove (ii) ⟹ (i) by differentiating the isometry condition with respect to a one-parameter family of curves.

**Subgoal decomposition:**

1. **(i) ⟹ (iii).** For parallel $V, W$ along $\gamma$: $\frac{d}{dt}g(V, W) = g(\nabla_t V, W) + g(V, \nabla_t W) = 0$, by Leibniz rule and the parallel condition. So $g(V, W)$ is constant.
   - *Hint:* Apply the Leibniz rule directly with $X = \dot\gamma$ and parallel $Y = V, Z = W$.
   - *Why needed:* Establishes that parallel vector fields have constant inner product.

2. **(iii) ⟹ (ii).** $P_\gamma v$ is the value at $b$ of the parallel section starting at $v$ at $a$. If $V, W$ are parallel with $V(a) = v, W(a) = w$, then $g(V(b), W(b)) = g(V(a), W(a))$ by (iii), i.e., $g_q(P_\gamma v, P_\gamma w) = g_p(v, w)$. So $P_\gamma$ is an isometry.
   - *Hint:* Directly from the definition of parallel transport.
   - *Why needed:* Establishes the isometry property.

3. **(ii) ⟹ (i).** Take vector fields $X, Y, Z$. At a point $p$, consider the curve $\gamma$ with $\dot\gamma(0) = X_p$, and consider $Y, Z$ as vector fields on $M$. Apply $X g(Y, Z) = \frac{d}{dt}\big|_{t=0} g(Y(\gamma(t)), Z(\gamma(t)))$. Using parallel-transport coordinates (a frame parallel-transported along $\gamma$), $Y$ and $Z$ have components $Y^a(t), Z^a(t)$, and $g_{ab}(\gamma(t)) = g_{ab}(p) = $ constant by the isometry condition (parallel transport is isometric). So $\frac{d}{dt}g(Y, Z) = \frac{d}{dt}(g_{ab}Y^a Z^b) = g_{ab}(\dot Y^a Z^b + Y^a \dot Z^b) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z)$ — the Leibniz rule.
   - *Hint:* Work in parallel-transport coordinates; the metric components are constant in such coordinates.
   - *Why needed:* Establishes metric-compatibility from the isometry condition.

---

# Lemma Decomposition

> [!note]- Lemma 1: The integrated Leibniz rule for parallel vector fields
> **Statement:** If $\nabla$ is metric-compatible and $V, W$ are vector fields along a smooth curve $\gamma$ satisfying $\nabla_t V = \nabla_t W = 0$, then $\frac{d}{dt}g(V(t), W(t)) = 0$.
>
> **Hint:** Apply the metric-compatibility Leibniz rule with $X = \dot\gamma$, $Y = V$, $Z = W$ (extended locally as vector fields) and use the parallel conditions.
>
> **Why needed:** This is the bridge from metric-compatibility to inner-product preservation along parallel sections.
>
> > [!note]- Full proof
> > Locally extend $V, W$ to vector fields $\tilde V, \tilde W$ in a neighbourhood of $\gamma$. The function $f(t) = g_{\gamma(t)}(V(t), W(t)) = g(\tilde V, \tilde W)(\gamma(t))$. Its derivative is $f'(t) = \dot\gamma g(\tilde V, \tilde W) = g(\nabla_{\dot\gamma}\tilde V, \tilde W) + g(\tilde V, \nabla_{\dot\gamma}\tilde W)$ by metric-compatibility. Evaluated at $\gamma(t)$, $\nabla_{\dot\gamma}\tilde V$ at $\gamma(t)$ equals $\nabla_t V(t)$, which is zero by the parallel condition. Similarly for $W$. Hence $f'(t) = 0$, so $f$ is constant. $\blacksquare$

> [!note]- Lemma 2: Parallel-transport coordinates
> **Statement:** Along any smooth curve $\gamma : [a, b] \to M$, there exists a parallel orthonormal frame $(E_1(t), \ldots, E_n(t))$ with $\nabla_t E_a = 0$ and $g(E_a, E_b) = $ constant (in fact $= \delta_{ab}$ or $\eta_{ab}$).
>
> **Hint:** Choose any orthonormal frame at $p = \gamma(a)$ and parallel-transport each member along $\gamma$. Use Lemma 1 to verify the orthonormality is preserved along the curve.
>
> **Why needed:** Provides a coordinate system in which the metric components are constant along $\gamma$, which is what underlies the proof of (ii) ⟹ (i).
>
> > [!note]- Full proof
> > Pick any orthonormal basis $(E_1(a), \ldots, E_n(a))$ of $(T_{\gamma(a)}M, g_{\gamma(a)})$. Parallel-transport each $E_b(a)$ along $\gamma$ via the parallel-transport ODE — this gives parallel vector fields $E_b(t)$ along $\gamma$. By Lemma 1 (which uses metric-compatibility), $g(E_a(t), E_b(t)) = g(E_a(a), E_b(a)) = \delta_{ab}$ (the orthonormality is preserved). So the parallel-transported frame is everywhere orthonormal. Independence is also preserved since parallel transport is a linear isomorphism.

---

# Formal Proof

> [!note]- Complete formal proof
> We prove the cycle (i) ⟹ (iii) ⟹ (ii) ⟹ (i).
>
> **(i) ⟹ (iii).** Suppose $\nabla$ is metric-compatible. Let $V, W$ be parallel along $\gamma$. By Lemma 1, $\frac{d}{dt}g(V(t), W(t)) = 0$, so $g(V, W)$ is constant.
>
> **(iii) ⟹ (ii).** Suppose every pair of parallel vector fields along any curve has constant inner product. Let $\gamma : [a, b] \to M$ be a curve from $p$ to $q$, and let $v, w \in T_pM$. Let $V(t), W(t)$ be the parallel sections along $\gamma$ with $V(a) = v, W(a) = w$. By (iii), $g_{\gamma(b)}(V(b), W(b)) = g_{\gamma(a)}(V(a), W(a))$. But $V(b) = P_\gamma v$ and $W(b) = P_\gamma w$ by definition of parallel transport, so $g_q(P_\gamma v, P_\gamma w) = g_p(v, w)$.
>
> **(ii) ⟹ (i).** Suppose parallel transport along every curve is an isometry. Let $X, Y, Z$ be vector fields on $M$ and let $p \in M$. We want to show $X_p g(Y, Z) = g_p(\nabla_X Y, Z) + g_p(Y, \nabla_X Z)$ at $p$.
>
> Choose a curve $\gamma$ with $\gamma(0) = p$, $\dot\gamma(0) = X_p$. Pick a parallel orthonormal frame $(E_a)$ along $\gamma$ (existence by Lemma 2 — but we should not use metric-compatibility yet; we use only the isometric parallel transport hypothesis to verify orthonormality is preserved). Write $Y(\gamma(t)) = Y^a(t)E_a(t)$ and $Z(\gamma(t)) = Z^a(t)E_a(t)$. Then
> $$
> g(Y, Z)(\gamma(t)) = g_{ab}(\gamma(t))\,Y^a(t)Z^b(t) = \delta_{ab}\,Y^a(t)Z^b(t) = Y^a(t)Z^a(t),
> $$
> using the orthonormality of $E_a$ (constant in $t$ by parallel transport being isometric).
>
> Differentiate at $t = 0$:
> $$
> X_p g(Y, Z) = \frac{d}{dt}\Big|_{t=0}\bigl(Y^a(t)Z^a(t)\bigr) = \dot Y^a(0)Z^a(0) + Y^a(0)\dot Z^a(0).
> $$
> Now we identify $\dot Y^a(0)$ with the components of $\nabla_X Y$ at $p$. Since $E_a$ is parallel ($\nabla_t E_a = 0$),
> $$
> \nabla_t Y = \nabla_t(Y^a E_a) = \dot Y^a E_a + Y^a \nabla_t E_a = \dot Y^a E_a.
> $$
> So $(\nabla_t Y)^a = \dot Y^a$ in this frame. At $t = 0$, $\nabla_t Y = \nabla_{\dot\gamma(0)}Y = \nabla_X Y$ at $p$, so $\dot Y^a(0) = (\nabla_X Y)^a$ in the parallel frame at $p$. Similarly $\dot Z^a(0) = (\nabla_X Z)^a$.
>
> Substituting:
> $$
> X_p g(Y, Z) = (\nabla_X Y)^a(p) Z^a(p) + Y^a(p)(\nabla_X Z)^a(p) = g_p(\nabla_X Y, Z) + g_p(Y, \nabla_X Z),
> $$
> using the orthonormality of $E_a$ at $p$. This is the Leibniz rule, i.e., metric-compatibility at $p$. Since $p$ was arbitrary, metric-compatibility holds globally. $\blacksquare$
>
> **Note on circularity.** The proof of (ii) ⟹ (i) uses Lemma 2 to choose a parallel orthonormal frame, but Lemma 2 was proved assuming metric-compatibility (it uses Lemma 1 / (i) ⟹ (iii)). To avoid circularity, in the (ii) ⟹ (i) direction we use only the isometric parallel-transport hypothesis (ii) directly: parallel-transport an orthonormal basis $(E_a(p))$ along $\gamma$ to get parallel sections $E_a(t)$, then verify $g(E_a(t), E_b(t)) = \delta_{ab}$ for all $t$ by the isometry condition (ii) applied at parameter $t$. This avoids the need for Lemma 2's proof and breaks the apparent circularity.

---

# Cross-Field Exercise Suggestions

**1. Verify the round 2-sphere has isometric parallel transport.** Parallel-transport a vector along a great-circle arc on $S^2$ (a geodesic) and verify the transported vector has the same length and the same angle to the great circle as the starting vector. Then verify the same for parallel transport around a triangle and check the rotation angle matches the holonomy formula.

**2. Non-metric-compatible connections give non-isometric parallel transport.** On $\mathbb{R}^2$ with the flat metric, define a non-metric-compatible connection by $\Gamma^x_{xx} = 1$ (and all others zero). Compute the parallel transport of a vector along the $x$-axis and verify it changes length, in contrast to the Levi-Civita parallel transport.

**3. Holonomy as an isometry.** Take the holonomy of the Levi-Civita connection of $S^2$ around a circle of latitude $\theta_0$. By the theorem, this holonomy is an isometry $T_pS^2 \to T_pS^2$ at the starting point $p$ — i.e., a rotation. Verify directly that the holonomy is rotation by the angle $2\pi(1 - \cos\theta_0)$, and show this is consistent with the integrated Gauss-Bonnet formula $\int_{D}K\,dA$ for the spherical cap of area $2\pi(1 - \cos\theta_0)$. See [[Ex - Parallel Transport around a Geodesic Triangle on the Sphere]].

**4. Spinor parallel transport on a spin manifold.** The Levi-Civita connection lifts to the spinor bundle as the spin connection, which is compatible with the spinor inner product. Apply the theorem to conclude that spinor parallel transport is a *unitary* transformation of the fibre. This is what makes the Dirac equation in curved spacetime well-posed: spinor states evolve unitarily along worldlines. See [[Spinors and the Dirac Equation]].

---

# Bridges

- **[[Def - Metric-Compatible Connection]]** — This theorem provides the equivalent characterisations of metric-compatibility. The three forms (infinitesimal Leibniz, isometric parallel transport, constant inner products along parallel sections) are all useful in different contexts; choose the one that best matches the problem.

- **[[Def - Parallel Transport]]** — The structural fact "parallel transport along any curve is a linear isomorphism" is upgraded by metric-compatibility to "linear isometry". This is what makes parallel transport a *rigid* comparison between tangent spaces — preserving lengths and angles, as one wants for a Riemannian comparison.

- **Holonomy groups** — As a corollary, the holonomy group of a metric-compatible connection at a point is a subgroup of $O(n)$ (or $O(p, q)$). This is the structural input to **Berger's classification** of irreducible Riemannian holonomy groups: $\mathrm{SO}(n)$ generic, with special holonomies $U(n), SU(n), \mathrm{Sp}(n), \mathrm{Sp}(n)\mathrm{Sp}(1), G_2, \mathrm{Spin}(7)$ corresponding to additional geometric structures (Kähler, Calabi-Yau, etc.).

- **Constant speed of geodesics** — A direct corollary applied to $V = W = \dot\gamma$ for a geodesic ($\nabla_t\dot\gamma = 0$): $g(\dot\gamma, \dot\gamma)$ is constant along $\gamma$. So geodesics of a metric-compatible connection have constant speed — they are uniformly parametrised by their natural parameter.

- **Killing fields and conservation laws** — For a Killing field $K$ along a geodesic $\gamma$, the inner product $g(\dot\gamma, K)$ is conserved (a Noether-type conservation law for spacetime symmetries). The proof uses metric-compatibility plus the antisymmetry of $\nabla K$ from Killing's equation. This is the geometric basis of energy and angular momentum conservation in general relativity, used for example in the perihelion-precession calculation in Schwarzschild.

---

# Unlocked by This

> [!tip] Holonomy Groups and Berger's Classification *(from Riemannian Geometry)*
> A corollary of this theorem is that the holonomy group of a metric-compatible connection is a subgroup of $O(n)$ (or $O(p, q)$ in indefinite signature). For the Levi-Civita connection of an orientable Riemannian manifold, the holonomy is a subgroup of $\mathrm{SO}(n)$. **Berger's classification** (1955) lists the possible irreducible holonomy groups: $\mathrm{SO}(n), U(n), SU(n), \mathrm{Sp}(n), \mathrm{Sp}(n)\mathrm{Sp}(1), G_2, \mathrm{Spin}(7)$. Each special holonomy corresponds to a reduction of the orthonormal frame bundle and to additional parallel tensor fields (the Kähler form for $U(n)$, holomorphic volume form for $SU(n)$, etc.). The **Ambrose-Singer theorem** identifies the Lie algebra of the holonomy with the span of curvature tensor values, completing the bridge from local curvature to global holonomy.

> [!tip] The Geometric Phase / Foucault Pendulum *(from Geometric Mechanics)*
> The most striking physical manifestation of the theorem: the **Foucault pendulum** experiment. A pendulum at latitude $\theta_0$ on Earth has its swing direction parallel-transported (approximately) along the daily latitude circle. By this theorem, the parallel transport is an isometry of the local tangent plane — a rotation. The rotation angle per day is the holonomy angle $2\pi(1 - \cos\theta_0)$ of the latitude circle on the unit 2-sphere, which gives the observed precession of the pendulum's plane. This is one of the cleanest physical demonstrations of the geometric meaning of parallel transport and metric-compatibility.

> [!tip] The Bochner Technique *(from Riemannian Geometry / Hodge Theory)*
> Combined with the **Weitzenböck formula** relating the Laplacian and the rough Laplacian via curvature, the theorem leads to **Bochner's technique** for proving rigidity results: on a compact Riemannian manifold with positive Ricci curvature, every harmonic 1-form is identically zero (Bochner 1946). The argument uses metric-compatibility essentially in integrating the curvature-Laplacian identity over the compact manifold. See [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition]].
