---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Isometry of Riemannian Manifolds"
  - "Def - Riemannian Manifold"
  - "Def - Length of a Curve and Riemannian Distance"
tags: [geometry, differential-geometry, riemannian-geometry]
---

# Problem Statement

Let $F : (M, g) \to (N, h)$ be a Riemannian isometry between Riemannian manifolds (so $F$ is a smooth diffeomorphism with $F^* h = g$). Prove that $F$ sends geodesics of $g$ to geodesics of $h$ — equivalently, that geodesics are *invariants* of Riemannian isometries.

More precisely: a smooth curve $\gamma : I \to M$ is a geodesic of $g$ (with respect to the Levi-Civita connection $\nabla^g$) if and only if $F \circ \gamma : I \to N$ is a geodesic of $h$ (with respect to the Levi-Civita connection $\nabla^h$).

You may take the variational characterisation of geodesics: a curve $\gamma$ is a *constant-speed length-minimising* geodesic in a neighborhood of each parameter $t_0$ — meaning, $\gamma$ restricted to a small enough interval $[t_0 - \varepsilon, t_0 + \varepsilon]$ is a curve of minimum $g$-length among curves connecting its endpoints. (Equivalently, $\gamma$ has $\nabla^g_{\dot\gamma}\dot\gamma = 0$, but this is the content of the Levi-Civita connection of [[Thm - Fundamental Theorem of Riemannian Geometry (Statement)]] and may be invoked or used as the definition.)

**Recall:**

![[Def - Isometry of Riemannian Manifolds#The Definition]]

For a piecewise smooth curve $\gamma$ on $(M, g)$, the length is
$$
L_g(\gamma) \;=\; \int |\dot\gamma|_g\, dt.
$$
A geodesic (locally) minimises this functional among curves with the same endpoints.

---

# Convergent Strategy

**Problem class.** This is a *prove a quantity/structure is preserved by a structure-preserving map* problem. The [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds#Problem-Solving Strategy|problem-solving strategy]] identifies the route: properties that are *built from the metric* are preserved by isometries; geodesics are built from the metric (as critical points of the length functional, or via the metric-derived Levi-Civita connection), hence are preserved.

**Assumption pattern.** The hypothesis is $F : (M, g) \to (N, h)$ is a Riemannian isometry — $F$ is a diffeomorphism with $F^* h = g$. This single condition implies that *every* metric-derived quantity is preserved: lengths of curves, distances, angles, gradients, Christoffel symbols (in corresponding coordinates), the Riemann curvature tensor, the Laplace–Beltrami spectrum, *and* geodesics. The argument can be made at any of these levels; we use the length-functional characterisation because it is the most direct.

**Theorem routing.** Use the **isometry-preserves-length** property: for any piecewise smooth curve $\gamma$ in $M$, $L_g(\gamma) = L_h(F \circ \gamma)$. This follows by direct computation using $F^* h = g$. Then: if $\gamma$ is locally length-minimising in $(M, g)$, $F \circ \gamma$ is locally length-minimising in $(N, h)$ — because any competing curve in $N$ pulls back via $F^{-1}$ to a competing curve in $M$ with the same $g$-length, and the minimality on $M$ rules out a competitor with shorter length.

**Key decision point.** The non-obvious choice is *which characterisation of geodesic to use*. Three options: (1) variational (locally length-minimising), (2) ODE (the geodesic equation $\nabla^g_{\dot\gamma}\dot\gamma = 0$), (3) energy (critical point of the energy functional). The variational characterisation is the cleanest for an isometry argument because it requires only that isometries preserve length. The ODE characterisation requires showing that isometries intertwine the Levi-Civita connections (also true, but a longer argument: see Step 3 below for the connection-level version). We use the variational route as the primary, with the ODE route mentioned for completeness.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds#Legal Operations|the topic page's Legal Operations]]:

9. **Use an isometry to transport problems** (operation 9). The entire argument is built on this: an isometry preserves every metric-derived quantity, so to prove "geodesics are preserved", we use "lengths are preserved" plus "geodesic = locally length-minimising".

1. **Pull back an ambient metric along an immersion or embedding** (operation 1). Applied here as the pullback $F^* h$ along a diffeomorphism — the strongest version, which is required to be exactly equal to $g$ for $F$ to be an isometry.

---

# Hints

> [!note]- Hint 1
> The first step is to verify that isometries preserve curve lengths: $L_g(\gamma) = L_h(F \circ \gamma)$ for every piecewise smooth $\gamma$ in $M$. This follows from $F^* h = g$ together with the chain rule.

> [!note]- Hint 2
> Once you have length preservation, the geodesic property "$\gamma$ is locally length-minimising in $(M, g)$" transfers directly to "$F \circ \gamma$ is locally length-minimising in $(N, h)$". The argument: any curve $\tilde\gamma$ in $N$ between $F(\gamma(a))$ and $F(\gamma(b))$ pulls back via $F^{-1}$ to a curve in $M$ with the same length (by length preservation applied to $F^{-1}$), and a counterexample on $N$ would give a counterexample on $M$.

> [!note]- Hint 3
> If you prefer the ODE characterisation: an isometry intertwines the Levi-Civita connections, $F_*(\nabla^g_X Y) = \nabla^h_{F_* X}(F_* Y)$ for any vector fields $X, Y$ on $M$. Then if $\gamma$ is a geodesic of $g$ (i.e., $\nabla^g_{\dot\gamma}\dot\gamma = 0$), pushing forward gives $\nabla^h_{(F \circ \gamma)\cdot}\dot{(F \circ \gamma)} = 0$ — that is, $F \circ \gamma$ is a geodesic of $h$.

---

# Solution

The proof breaks into three steps. Step 1 establishes that isometries preserve curve lengths. Step 2 uses length preservation to transfer the local-length-minimising property. Step 3 (optional) gives the alternative argument via the Levi-Civita connection. The decisive insight is that the geodesic property is *defined* in terms of the metric, so any map preserving the metric preserves the property; the technical content is in making the chain rule work out.

**Step 1: Isometries preserve curve lengths, $L_g(\gamma) = L_h(F \circ \gamma)$.**

> [!note]- Derivation
> Let $\gamma : [a, b] \to M$ be a piecewise smooth curve. Define $\tilde\gamma = F \circ \gamma : [a, b] \to N$. We compute $L_h(\tilde\gamma)$:
> $$
> L_h(\tilde\gamma) = \int_a^b |\dot{\tilde\gamma}(t)|_h\, dt = \int_a^b \sqrt{h_{\tilde\gamma(t)}(\dot{\tilde\gamma}, \dot{\tilde\gamma})}\, dt.
> $$
>
> Now $\dot{\tilde\gamma}(t) = (F \circ \gamma)'(t) = dF_{\gamma(t)}(\dot\gamma(t))$ by the chain rule. So
> $$
> h_{\tilde\gamma(t)}(\dot{\tilde\gamma}, \dot{\tilde\gamma}) = h_{F(\gamma(t))}\bigl(dF_{\gamma(t)}\dot\gamma(t), dF_{\gamma(t)}\dot\gamma(t)\bigr).
> $$
>
> By definition of the pullback, $h_{F(p)}(dF_p u, dF_p v) = (F^* h)_p(u, v)$. By the isometry assumption $F^* h = g$, this equals $g_p(u, v)$. So
> $$
> h_{\tilde\gamma(t)}(\dot{\tilde\gamma}, \dot{\tilde\gamma}) = g_{\gamma(t)}(\dot\gamma, \dot\gamma) = |\dot\gamma(t)|_g^2.
> $$
>
> Hence $|\dot{\tilde\gamma}(t)|_h = |\dot\gamma(t)|_g$ for every $t$, and
> $$
> L_h(\tilde\gamma) = \int_a^b |\dot\gamma(t)|_g\, dt = L_g(\gamma).
> $$
> So $F$ preserves lengths of piecewise smooth curves.

**Step 2: Geodesics of $g$ map to geodesics of $h$.**

> [!note]- Derivation
> Suppose $\gamma : I \to M$ is a geodesic of $g$ — that is, for every $t_0 \in I$ there exists $\varepsilon > 0$ such that $\gamma|_{[t_0 - \varepsilon, t_0 + \varepsilon]}$ is the unique length-minimising curve between $\gamma(t_0 - \varepsilon)$ and $\gamma(t_0 + \varepsilon)$ in $(M, g)$ (with constant-speed parametrisation, which we assume after possible reparametrisation).
>
> Let $\tilde\gamma = F \circ \gamma$. We show $\tilde\gamma$ is a geodesic of $h$.
>
> Pick any $t_0 \in I$. Let $\tilde p = F(\gamma(t_0 - \varepsilon))$ and $\tilde q = F(\gamma(t_0 + \varepsilon))$ — the endpoints of $\tilde\gamma|_{[t_0 - \varepsilon, t_0 + \varepsilon]}$.
>
> Suppose for contradiction that some other piecewise smooth curve $\tilde\sigma : [t_0 - \varepsilon, t_0 + \varepsilon] \to N$ from $\tilde p$ to $\tilde q$ has length strictly less than $L_h(\tilde\gamma|_{[t_0 - \varepsilon, t_0 + \varepsilon]})$. Pull back: $\sigma := F^{-1} \circ \tilde\sigma$ is a curve in $M$ from $\gamma(t_0 - \varepsilon)$ to $\gamma(t_0 + \varepsilon)$. By length preservation applied to $F^{-1}$ (which is also an isometry, as the inverse of an isometry):
> $$
> L_g(\sigma) = L_h(\tilde\sigma) < L_h(\tilde\gamma|_{[t_0 - \varepsilon, t_0 + \varepsilon]}) = L_g(\gamma|_{[t_0 - \varepsilon, t_0 + \varepsilon]}),
> $$
> the last equality by Step 1. So $\sigma$ is a curve in $M$ between the same endpoints as $\gamma|_{[t_0 - \varepsilon, t_0 + \varepsilon]}$ but of strictly smaller $g$-length — contradicting the local minimality of $\gamma$ as a geodesic.
>
> Hence no such $\tilde\sigma$ exists, and $\tilde\gamma|_{[t_0 - \varepsilon, t_0 + \varepsilon]}$ is locally length-minimising in $(N, h)$. Since $t_0$ was arbitrary, $\tilde\gamma$ is a geodesic of $h$.
>
> The converse direction (a geodesic in $N$ pulls back to a geodesic in $M$) is the same argument applied to $F^{-1}$, also an isometry.

**Step 3 (alternative argument via the Levi-Civita connection).**

> [!note]- Derivation (optional, ODE characterisation)
> An alternative route uses the Levi-Civita connection. An isometry $F$ intertwines the Levi-Civita connections of $g$ and $h$:
> $$
> F_*(\nabla^g_X Y) = \nabla^h_{F_* X}(F_* Y) \qquad \text{for all vector fields } X, Y \text{ on } M.
> $$
> This is because the Levi-Civita connection is *uniquely* determined by the metric (the [[Thm - Fundamental Theorem of Riemannian Geometry (Statement)|fundamental theorem]]), and the pulled-back connection $F^*\nabla^h$ on $M$ is torsion-free and metric-compatible with $F^* h = g$, hence equal to $\nabla^g$ by uniqueness.
>
> Given this intertwining, if $\gamma : I \to M$ is a geodesic of $g$ — meaning $\nabla^g_{\dot\gamma}\dot\gamma = 0$ along $\gamma$ — then applying $F_*$ pointwise:
> $$
> \nabla^h_{\dot{\tilde\gamma}}\dot{\tilde\gamma} = F_*\bigl(\nabla^g_{\dot\gamma}\dot\gamma\bigr) = F_*(0) = 0,
> $$
> using the chain rule $\dot{\tilde\gamma} = F_*(\dot\gamma)$ along $\gamma$. So $\tilde\gamma$ satisfies the geodesic equation of $h$, hence is a geodesic of $h$.

> [!note]- Complete formal solution
> Let $F : (M, g) \to (N, h)$ be a Riemannian isometry, so $F$ is a diffeomorphism with $F^* h = g$.
>
> **Length preservation:** For any piecewise smooth curve $\gamma : [a, b] \to M$, applying the chain rule to $\tilde\gamma = F \circ \gamma$ gives $\dot{\tilde\gamma}(t) = dF_{\gamma(t)}\dot\gamma(t)$, and using $F^* h = g$:
> $$
> |\dot{\tilde\gamma}(t)|_h^2 = h(dF\dot\gamma, dF\dot\gamma) = (F^* h)(\dot\gamma, \dot\gamma) = g(\dot\gamma, \dot\gamma) = |\dot\gamma(t)|_g^2.
> $$
> So $L_h(\tilde\gamma) = L_g(\gamma)$.
>
> **Geodesic preservation:** Let $\gamma : I \to M$ be a geodesic of $g$ (locally length-minimising). Set $\tilde\gamma = F \circ \gamma$. For any $t_0 \in I$, $\gamma|_{[t_0 - \varepsilon, t_0 + \varepsilon]}$ is locally length-minimising for some $\varepsilon > 0$. If some curve $\tilde\sigma$ in $N$ between $\tilde\gamma(t_0 - \varepsilon)$ and $\tilde\gamma(t_0 + \varepsilon)$ had $L_h(\tilde\sigma) < L_h(\tilde\gamma|_{[t_0 - \varepsilon, t_0 + \varepsilon]})$, then $\sigma = F^{-1} \circ \tilde\sigma$ would be a curve in $M$ between $\gamma(t_0 - \varepsilon)$ and $\gamma(t_0 + \varepsilon)$ with $L_g(\sigma) = L_h(\tilde\sigma) < L_g(\gamma|_{[t_0 - \varepsilon, t_0 + \varepsilon]})$, contradicting the minimality of $\gamma$ as a geodesic.
>
> Hence $\tilde\gamma|_{[t_0 - \varepsilon, t_0 + \varepsilon]}$ is locally length-minimising in $(N, h)$. Since $t_0$ was arbitrary, $\tilde\gamma$ is a geodesic of $h$.
>
> Applying the same argument to $F^{-1}$ (also an isometry), every geodesic of $h$ pulls back to a geodesic of $g$. So geodesics are in bijection under $F$, and $F$ sends geodesics to geodesics. $\blacksquare$

> [!warning] Sanity check via the geodesic equation
> The same conclusion can be reached via the Levi-Civita connection: $F$ intertwines $\nabla^g$ and $\nabla^h$ (uniqueness of the Levi-Civita connection, [[Thm - Fundamental Theorem of Riemannian Geometry (Statement)]]), so $\nabla^g_{\dot\gamma}\dot\gamma = 0$ pushes forward to $\nabla^h_{\dot{\tilde\gamma}}\dot{\tilde\gamma} = 0$. Both arguments give the same conclusion, confirming the result.

---

# Key Takeaways

**Anything built from the metric alone is an isometry invariant.** This is the master principle of Riemannian geometry: the metric $g$ is the *only* structure beyond the smooth manifold, so any quantity computable from $g$ alone — without invoking additional non-canonical data — is preserved by isometries. The list is long and important: lengths of curves, Riemannian distances, angles between tangent vectors, gradients of smooth functions, Christoffel symbols (in corresponding coordinates), the Riemann curvature tensor, sectional/Ricci/scalar curvature, the Laplace–Beltrami eigenvalues, the volume of compact subsets, geodesics, parallel transport, the exponential map. Anything that depends *only* on $g$ is an isometry invariant. The reusable lesson: when you suspect a quantity is an isometry invariant, ask "is it computable from $g$ alone?" — if yes, it is invariant.

**Geodesics are the manifold-intrinsic notion of "straight line".** A "straight line" in Euclidean $\mathbb{R}^n$ has many equivalent characterisations: shortest path between endpoints, constant-velocity curve, curve with zero second derivative, curve in a fixed direction. On a Riemannian manifold, only some of these generalise: shortest path locally (length-minimising), zero covariant acceleration ($\nabla^g_{\dot\gamma}\dot\gamma = 0$), constant speed. These give a *manifold-intrinsic* notion of "straight": geodesics are the metric's choice of "straight lines", and they coincide with Euclidean straight lines exactly on flat manifolds. Isometries preserve geodesics because the notion is metric-intrinsic, not chart-dependent — this exercise is the formal expression of that fact. The reusable lesson: geodesics are intrinsic, distance is intrinsic, curvature is intrinsic — *but* coordinate-straight-lines are not. The chart's "straight line" is generally not a geodesic.

**Isometries are the same kind of map as group homomorphisms — they preserve the structure that defines the category.** A diffeomorphism preserves the smooth structure but not the metric; an isometry preserves both. In the language of category theory (see [[Def - Isometry of Riemannian Manifolds]]'s Categorical section), isometries are the isomorphisms in the category of Riemannian manifolds. Just as a group homomorphism preserves multiplication and identity (the structure of group), a Riemannian isometry preserves the metric (the structure of Riemannian manifold). Every property of a group that is "structural" — order of elements, conjugacy classes, abelianness — is preserved by homomorphisms; every property of a Riemannian manifold that is "structural" — curvature, geodesics, distance — is preserved by isometries. The parallel between algebraic and geometric structure-preserving maps is one of the unifying themes of modern mathematics.

**Cross-link to companion exercises:** This exercise establishes a key reusable fact (geodesic preservation under isometries) that will be invoked throughout Riemannian geometry. The fact that the Lorentz group acts on Minkowski space by isometries ([[Ex - Minkowski Space as the Flat Lorentzian Manifold]]) plus this exercise's conclusion implies that Lorentz transformations send geodesics (= straight lines in flat space) to geodesics — which is the geometric reason "inertial worldlines map to inertial worldlines under Lorentz boosts" in special relativity.
