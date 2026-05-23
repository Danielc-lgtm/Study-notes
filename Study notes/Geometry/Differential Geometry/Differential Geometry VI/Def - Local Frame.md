---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Vector Bundle"
  - "Def - Section of a Vector Bundle"
  - "Def - Local Trivialization"
  - "Def - Basis"
tags: [geometry, differential-geometry, bundles, frames]
---

# Notation

$\pi : E \to M$ is a smooth vector bundle of rank $k$. The local frame is a tuple $(\sigma_1, \dots, \sigma_k)$ of smooth local sections of $E$ defined on an open set $U \subseteq M$ — see [[Def - Section of a Vector Bundle]] for sections. At each $p \in U$, $\sigma_i(p) \in E_p$, and the requirement is that $(\sigma_1(p), \dots, \sigma_k(p))$ is a basis of $E_p$ (in the sense of [[Def - Basis]] for finite-dimensional vector spaces). For the tangent bundle, the standard local frame in a chart $(U, x^i)$ is the coordinate frame $(\partial/\partial x^1, \dots, \partial/\partial x^n)$.

---

# Axiom Motivation

A local frame is a smooth field of bases for the fibres of $E$, parametrized by a piece of $M$. The motivating need is computational: every concrete calculation in vector-bundle theory benefits from picking a basis on each fibre, but the basis must vary smoothly with $p$ for the computation to be a smooth-bundle calculation rather than a pointwise one. A frame is the data of "a smoothly varying choice of basis", and it converts every section over the frame's domain into a $k$-tuple of smooth scalar functions — its **components** in the frame.

The defining conditions are tightly linked. We need $k$ local sections (one for each desired basis vector), each defined on $U$ — that is the "$k$-tuple of smooth local sections" condition. And we need their pointwise values to be linearly independent, in fact a basis, at every point of $U$ — that is the "$(\sigma_1(p), \dots, \sigma_k(p))$ is a basis of $E_p$" condition. The combination is exactly "a smooth choice of basis for $E_p$ for every $p \in U$".

What is forced by demanding the values are a **basis** (linearly independent and spanning) at every point, rather than merely linearly independent? Spanning is automatic given linear independence: any $k$ linearly independent vectors in a $k$-dimensional vector space form a basis. So "basis" and "linearly independent" coincide for $k$-tuples in a $k$-dimensional fibre. The choice of $k$ matches the rank by construction.

What is forced by demanding **pointwise** linear independence rather than just "linearly independent as smooth sections in the $C^\infty(U)$-[[Def - Module|module]] $\Gamma(U, E)$"? This is a subtler point. Smooth sections $\sigma_1, \dots, \sigma_k$ over $U$ are linearly independent as $C^\infty(U)$-module elements if $f^i \sigma_i = 0$ implies $f^i = 0$ for $f^i \in C^\infty(U)$. The frame condition is *pointwise* linear independence: at every $p$, the values $\sigma_i(p)$ are linearly independent in $E_p$. The pointwise condition is **strictly stronger** than the module condition in general. For example, on $U = \mathbb{R}$ with $E = U \times \mathbb{R}^2$, take $\sigma_1 = (x, 0)$ and $\sigma_2 = (0, 1)$: at $x = 0$, $\sigma_1(0) = 0$, so they are not pointwise linearly independent — yet $f \sigma_1 + g \sigma_2 = 0$ forces $f(x) \cdot x = 0$ and $g \equiv 0$, giving $f(x) = 0$ everywhere except possibly at $x = 0$, hence $f \equiv 0$ by smoothness. So module-wise linear independence holds even though pointwise basis fails at one point. The frame definition demands pointwise, because the operational content of a frame is fibrewise: every fibre's vectors should be expressible in terms of the frame.

What is forced by demanding **smoothness** of each $\sigma_i$? Smoothness of the frame is what makes the component functions of a smooth section smooth. If the $\sigma_i$ were only continuous, the components of a smooth section in the frame would be continuous but not necessarily smooth, and the frame would be useless for differential calculus.

What if we **strengthened** to require a global frame on all of $M$? A global frame is precisely the data of a global trivialization (the trivialization $\Phi^{-1}(p, e_i) = \sigma_i(p)$ recovers the bundle from the frame). Global frames exist if and only if the bundle is trivial, so demanding a global frame would restrict the theory to trivial bundles, eliminating the interesting case.

What if we **weakened** to require only $m < k$ sections that are pointwise linearly independent? This gives a **partial frame**, equivalent to an $m$-dimensional [[Def - Subbundle|subbundle]] $\mathrm{span}(\sigma_1, \dots, \sigma_m) \subseteq E$ over $U$. Partial frames are useful (they parametrize [[Def - Subbundle|subbundles]]); a full frame is the special case $m = k$ where the subbundle is the entire bundle.

What if we **weakened** further to allow pointwise linear *dependence* at some points? Then the $k$-tuple does not span $E_p$ at those points, and the components of a section in the "frame" would not be uniquely determined there. The pointwise-basis condition is essential for unique components.

---

# The Definition

Let $\pi : E \to M$ be a smooth vector bundle of rank $k$, and let $U \subseteq M$ be an open subset. A **smooth local frame** for $E$ over $U$ is an ordered $k$-tuple $(\sigma_1, \dots, \sigma_k)$ of smooth local sections of $E$ over $U$ (each $\sigma_i \in \Gamma(U, E)$) such that for every $p \in U$, the values $\sigma_1(p), \sigma_2(p), \dots, \sigma_k(p)$ form a basis of the fibre $E_p$.

A frame is **global** if $U = M$. Frames over open sets are written interchangeably "frame on $U$" or "frame for $E|_U$".

For the tangent bundle $TM$, a coordinate chart $(U, \varphi)$ with coordinate functions $x^1, \dots, x^n$ gives the **coordinate frame** $\left(\frac{\partial}{\partial x^1}, \dots, \frac{\partial}{\partial x^n}\right)$ for $TM$ over $U$. For the cotangent bundle $T^*M$, the same chart gives the **dual coordinate coframe** $(dx^1, \dots, dx^n)$, characterized by $dx^j(\partial/\partial x^i) = \delta^j_i$.

Given a smooth local frame $(\sigma_1, \dots, \sigma_k)$ on $U$, every smooth local section $\tau \in \Gamma(U, E)$ has a unique expression
$$\tau = f^i \sigma_i \qquad (\text{summation over } i = 1, \dots, k)$$
for smooth functions $f^i \in C^\infty(U)$, called the **components of $\tau$ in the frame** (see [[Thm - Local Frames Span Sections]]). Conversely, every $k$-tuple of smooth functions on $U$ assembles into a smooth section by this formula.

---

# Relate to Other Fields / Compression

A local frame is **the bundle-theoretic analogue of a basis of a vector space**, made to vary smoothly with $p \in U$. The connection to [[Def - Local Trivialization|local trivializations]] is exact: a smooth local frame on $U$ is equivalent to a smooth local trivialization on $U$, via
$$\Phi^{-1}(p, v) = v^i \sigma_i(p) \quad \text{(trivialization from frame)}, \qquad \sigma_i(p) = \Phi^{-1}(p, e_i) \quad \text{(frame from trivialization)}.$$
Either piece of data determines the other, and the choice between them is a matter of computational convenience: trivializations emphasize the diffeomorphism with $U \times \mathbb{R}^k$, frames emphasize the basis at each fibre.

A local frame is also **a local section of the frame bundle** $\mathrm{Fr}(E) \to M$: $\mathrm{Fr}(E)$ has fibre over $p$ equal to the set of ordered bases of $E_p$, and a smooth local section of $\mathrm{Fr}(E)$ over $U$ is exactly a smooth local frame of $E$ over $U$. The frame bundle is a principal $\mathrm{GL}(k, \mathbb{R})$-bundle, and the structure-group action permutes frames at each point.

**True name:** the true name of a local frame is "**a smooth field of bases on $U$, in which every section becomes a tuple of smooth functions**". The operational consequence is that local-frame computations *are* multivariable-calculus computations. Once a frame is fixed, the bundle disappears and is replaced by $C^\infty(U)^k$ — the space of $k$-tuples of smooth functions on $U$.

A useful slogan: **bases live at a point; frames live on an open set; trivializations live as diffeomorphisms; cocycles live on overlaps**. Each piece of data refines the previous: a basis at every point of $U$ is a frame; a frame is a trivialization (a diffeomorphism with $U \times \mathbb{R}^k$); collections of trivializations are cocycles of transition functions on overlaps.

---

# Examples / Corollaries

**Is an instance — coordinate frame on a chart.** For $TM$ and a chart $(U, \varphi)$ with coordinate functions $x^i$, the coordinate vector fields $\partial/\partial x^i$ form a smooth local frame for $TM$ over $U$. At each $p \in U$, $\partial/\partial x^1|_p, \dots, \partial/\partial x^n|_p$ are linearly independent (a basis of $T_pM$ by the construction of the tangent space). Smoothness in $p$ is built into the definition of coordinate vector fields.

**Is an instance — dual coordinate coframe.** Dually, for $T^*M$ and the same chart, the coordinate covector fields $dx^i$ are a smooth local frame for $T^*M$ over $U$, with $dx^j(\partial/\partial x^i) = \delta^j_i$. See [[Ex - The Dual Frame on a Coordinate Chart]].

**Is an instance — global frame on a parallelizable manifold.** A manifold $M$ is called **parallelizable** if $TM$ admits a global frame; equivalently, $TM$ is trivial. The circle $S^1$, the $3$-sphere $S^3$, the $7$-sphere $S^7$, and every Lie [[Def - Group|group]] are parallelizable. For $S^1$, the angular velocity field $\partial/\partial\theta$ is a global frame.

**Is an instance — frame on a trivial bundle from a constant trivialization.** If $E = M \times \mathbb{R}^k$ and $(e_1, \dots, e_k)$ is the standard basis of $\mathbb{R}^k$, then $\sigma_i(p) := (p, e_i)$ is a smooth global frame for $E$. Every smooth global section $\tau = f^i \sigma_i$ corresponds to a smooth function $(f^1, \dots, f^k) : M \to \mathbb{R}^k$.

**Is NOT a frame — sections that vanish at some point.** On $TS^2$, no global frame exists (hairy ball theorem). Any candidate $(\sigma_1, \sigma_2)$ of smooth global sections has at least one component vanishing at some point — say $\sigma_1(p) = 0$ — and then $(\sigma_1(p), \sigma_2(p))$ does not form a basis of $T_pS^2$.

**Is NOT a frame — coordinate frame outside the chart.** The coordinate frame $(\partial/\partial x^i)$ on a chart $U$ is defined only on $U$; it does not extend to all of $M$ unless $M$ is parallelizable. Even on a single sphere $S^2$, the polar-coordinate frame breaks down at the poles where the coordinate system fails.

**Corollary — frames and trivializations are equivalent data.** Specifying a smooth local frame on $U$ is the same as specifying a smooth local trivialization on $U$. So every chart-induced trivialization of $TM$ (or $T^*M$) corresponds to the coordinate frame (or coframe), and conversely.

**Corollary — global frame exists if and only if bundle is trivial.** A global frame on $M$ gives a global trivialization (as the [[Def - Diffeomorphism|diffeomorphism]] $\Phi : E \to M \times \mathbb{R}^k$, $\sigma_i(p) v^i \mapsto (p, v^1, \dots, v^k)$), and conversely. So existence of a global frame is the operational characterization of triviality.

**Corollary — every point has a neighborhood with a smooth local frame.** By the definition of vector bundle, $M$ admits a cover by trivializing open sets, each carrying a local trivialization. Each trivialization gives a local frame. So local frames exist everywhere, even though global frames may not.

**Corollary — restriction of a frame is a frame.** If $(\sigma_1, \dots, \sigma_k)$ is a smooth local frame on $U$ and $V \subseteq U$ is open, then $(\sigma_1|_V, \dots, \sigma_k|_V)$ is a smooth local frame on $V$. Frames restrict to smaller opens.

**Calibration check.** Verify that the coordinate frame $(\partial/\partial x^i)$ on a chart is linearly independent at every point — this is essentially the construction of the tangent space, where the coordinate vectors are *defined* to be a basis. Verify that the dual coframe $(dx^i)$ satisfies the duality relation $dx^j(\partial/\partial x^i) = \delta^j_i$ at every point. Convince yourself that on a global-frame-admitting manifold, every smooth section has a globally defined component vector.

---

# Unlocked by This

> [!tip] Connection in a Frame *(from Riemannian Geometry)*
> Given a connection $\nabla$ on $E$ and a local frame $(\sigma_i)$, the **connection coefficients** $\Gamma^k_{ij}$ (or **Christoffel symbols** when $E = TM$ and the connection is the Levi-Civita connection) are defined by $\nabla_{\partial/\partial x^j} \sigma_i = \Gamma^k_{ij} \sigma_k$. The frame is the data structure that converts a connection from an abstract operator into a set of smooth functions, and parallel transport, geodesics, and curvature are all computed using connection coefficients in chosen frames.

> [!tip] Moving Frames in Differential Geometry *(from Cartan's Method)*
> Élie Cartan's method of moving frames is the systematic use of local frames adapted to the geometric problem at hand — orthonormal frames on Riemannian manifolds, Darboux frames on surfaces, principal frames at boundaries. The structure equations $d\theta^i = -\Gamma^i_j \wedge \theta^j$ and $\Omega^i_j = d\Gamma^i_j + \Gamma^i_k \wedge \Gamma^k_j$ relate frames, connection forms, and curvature forms in a single coordinate-free computational framework. This is the foundation of modern differential geometry, including gauge theory and exterior calculus.

> [!tip] Orthonormal Frame Bundle *(from Riemannian Geometry)*
> When $E = TM$ is the tangent bundle of a Riemannian manifold, the orthonormal frames (frames where each $\sigma_i(p)$ is an orthonormal basis of $T_pM$) form the **orthonormal frame bundle** $\mathrm{Fr}_O(M)$, a principal $\mathrm{O}(n)$-bundle over $M$. Reduction of the structure group of $TM$ from $\mathrm{GL}(n, \mathbb{R})$ to $\mathrm{O}(n)$ is exactly the choice of a Riemannian metric, and the orthonormal frame bundle is the principal bundle realising this reduction.
