---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Geodesic"
  - "Def - Jacobi Field"
  - "Def - Conjugate Point"
  - "Def - Length and Energy Functionals"
tags: [geometry, riemannian-geometry, variational-calculus, jacobi-fields, index-form]
---

# Notation

$(M, g)$ a Riemannian manifold, $\gamma : [a, b] \to M$ a unit-speed [[Def - Geodesic|geodesic]] with $T = \dot\gamma$. $V, W$ denote piecewise smooth vector fields along $\gamma$, with $V', V''$ etc the covariant derivatives along $\gamma$. The space of *normal* variation fields is $\mathcal V_0^\perp := \{V : V(a) = V(b) = 0, V \perp T \text{ everywhere}\}$, piecewise smooth. The Riemann curvature operator on $T^\perp$ is $w \mapsto R(w, T)T$. The full registry: [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]].

---

# Axiom Motivation

The motivating question is: **what bilinear form on variation fields along a geodesic detects whether the geodesic is a local length-minimiser, and what is the structure of its kernel and its negative eigenspaces?** The answer is the index form, and its derivation is the second variation of the length (or energy) functional.

The first variation tells us geodesics are *critical points* of length and energy. But criticality alone does not determine minimisation — a critical point can be a minimum, a saddle, or a maximum. To distinguish these we look at the **second variation**: the Hessian of the functional at the critical point. The second variation of energy at a geodesic $\gamma$, evaluated on a variation field $V$ along $\gamma$ vanishing at the endpoints, is
$$\frac{d^2}{ds^2}\bigg|_{s=0} E(\gamma_s) = \int_a^b \bigl(g(V', V') - g(R(V, T)T, V)\bigr)\, dt =: I(V, V).$$
This bilinear form $I$ is the **index form**, and it is the Hessian of the energy functional at the geodesic $\gamma$.

The structure of $I$ is exactly what we want from a Hessian:

1. **Sign of $I(V, V)$ = sign of the second-order change in length.** If $I(V, V) > 0$ for all $V$, the geodesic is a strict local minimum. If $I$ has a negative direction, it is not a local minimum.

2. **Kernel of $I$ = Jacobi fields vanishing at the endpoints**, which is precisely the conjugate-point obstruction. So a non-trivial kernel signals the transition from minimising to non-minimising.

3. **Index of $I$ (dimension of a maximal negative-definite subspace) = number of interior conjugate points counted with multiplicity** — the Morse index theorem.

Why the *minus* sign on the curvature term? It comes from the derivation: when you differentiate the geodesic equation $\nabla_T T = 0$ twice in the variation parameter, the curvature contribution appears with a definite sign depending on the convention for $R$. In the standard convention $R(X, Y)Z = \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z - \nabla_{[X,Y]}Z$, positive sectional curvature gives $\langle R(V, T)T, V\rangle > 0$, hence $-\langle R(V, T)T, V\rangle < 0$ — *positive curvature decreases the index form*, consistent with the geometric picture that positive curvature focuses geodesics (makes nearby geodesics come together, hence makes $\gamma$ not a strict local minimum past the first conjugate point).

The **kinetic term** $g(V', V')$ is always positive (when $V' \neq 0$), so it tends to keep $I$ positive. The **curvature term** $-g(R(V, T)T, V)$ has sign depending on the curvature. The index form is positive when the kinetic term dominates the curvature term — which is true for *short* geodesics (no time for the curvature to integrate up enough) and for non-positively-curved manifolds (curvature term is non-positive, helping positivity). It can become negative for *long* geodesics on positively-curved manifolds — which is exactly when conjugate points appear.

Why **normal** variations? A tangential variation $V = f(t) T$ corresponds to varying the parametrisation of $\gamma$ — to first order it does not change the *image*, hence (by reparametrisation invariance of length) does not change the length. The second variation of length on tangential variations vanishes identically. So tangential variations are a trivial $1$-dimensional kernel of any second-variation analysis, and to get a non-degenerate problem we restrict to *normal* variations. For the energy functional this is less crucial (energy is not reparametrisation-invariant), but the cleanest statements come from restricting to normal variations.

Why piecewise smooth? Variations through nearby geodesics produce smooth Jacobi fields; but for the Morse index theorem to give the correct count we need to include "broken Jacobi fields" — piecewise Jacobi fields with prescribed jumps at corner points — which correspond to variations through geodesics with corners. The broken class is the right setting for the Sobolev space the index form is defined on, and integrating by parts on a piecewise-smooth $V$ produces the standard boundary terms at corners.

The **integration-by-parts** identity is the workhorse of every index-form computation. For a normal variation field $V$ vanishing at the endpoints,
$$I(V, V) = \int_a^b \bigl(g(V', V') - g(R(V, T)T, V)\bigr)\, dt = -\int_a^b g(V'' + R(V, T)T, V)\, dt,$$
obtained by integration by parts on the kinetic term. The integrand on the right is exactly the Jacobi operator $\mathcal J(V) := V'' + R(V, T)T$ applied to $V$. So **the index form is the bilinear form associated to the Jacobi operator** — the Jacobi field equation is the variational equation of $I$. This makes the connection between (a) zeros of the Jacobi equation (conjugate points), (b) kernel of the index form (Morse-degenerate critical points), and (c) failure of $\exp_p$ to be a diffeomorphism (singular values of the exponential map) into a single statement.

---

# The Definition

Let $(M, g)$ be a Riemannian manifold and $\gamma : [a, b] \to M$ a unit-speed [[Def - Geodesic|geodesic]] with tangent $T = \dot\gamma$. The **index form** on piecewise smooth variation fields $V, W$ along $\gamma$ is the symmetric bilinear form
$$I(V, W) := \int_a^b \bigl(g(V', W') - g(R(V, T)T, W)\bigr)\, dt,$$
where $V' = \nabla_T V$, $W' = \nabla_T W$ are the covariant derivatives along $\gamma$ and $R$ is the Riemann curvature tensor.

The index form is typically restricted to the space $\mathcal V_0^\perp$ of piecewise smooth *normal* variation fields vanishing at the endpoints — $V(a) = V(b) = 0$ and $V \perp T$ everywhere. On this space:

- **Symmetry:** $I(V, W) = I(W, V)$.
- **Jacobi-operator form (by integration by parts):** $I(V, W) = -\int_a^b g(V'' + R(V, T)T, W)\, dt$ for $V$ piecewise smooth and $W$ piecewise smooth with $W(a) = W(b) = 0$.
- **Kernel:** $\ker(I|_{\mathcal V_0^\perp}) = \{V \in \mathcal V_0^\perp : V \text{ is a Jacobi field}\}$, which is non-trivial iff the endpoints are conjugate along $\gamma$.

The **index** of $\gamma$ on $[a, b]$ is the dimension of a maximal subspace of $\mathcal V_0^\perp$ on which $I$ is negative-definite:
$$\mathrm{ind}(\gamma) := \dim_{\max}\{W \subseteq \mathcal V_0^\perp : I|_W < 0\}.$$
By the **Morse index theorem**, $\mathrm{ind}(\gamma)$ equals the number of points strictly inside $(a, b)$ that are conjugate to $\gamma(a)$ along $\gamma$, counted with multiplicity.

The **nullity** of $I$ on $\mathcal V_0^\perp$ is the dimension of $\ker I = $ Jacobi fields in $\mathcal V_0^\perp$, equal to the multiplicity of the conjugate pair $(\gamma(a), \gamma(b))$ if it exists, else zero.

---

# Relate to Other Fields / Compression

**True name:** **the Hessian of the energy functional at a geodesic, restricted to normal variations vanishing at the endpoints**. The index form is "what would be called the second derivative if the energy were a function on a finite-dimensional manifold", except that here the domain is the infinite-dimensional space of curves with fixed endpoints. All the geometric content of the second variation of length and energy is contained in $I$.

**The index form is the bilinear form of the Jacobi operator $\mathcal J$.** Writing $\mathcal J(V) := V'' + R(V, T)T$ for the linear *Jacobi operator* on vector fields along $\gamma$, integration by parts gives $I(V, W) = -\int g(\mathcal J(V), W)\, dt$ for $V, W$ vanishing at the endpoints. So $I$ is the symmetric bilinear form associated to the second-order self-adjoint elliptic-like operator $\mathcal J$. This is the variational origin of the spectral theory of Jacobi fields: eigenvalues of $\mathcal J$ ↔ negative directions of $I$ ↔ conjugate-point count via Sturm comparison.

**The index form generalises to all variational geometric problems.** Harmonic maps, minimal surfaces, Yang–Mills connections, Einstein metrics — every variational problem has its own "index form" which is the Hessian of the functional at a critical point. The structure of the index form (signature, kernel, negative eigenvalues) governs the Morse theory of the variational problem. The geodesic index form is the simplest case and is the prototype.

---

# Examples / Corollaries

**Is an instance: a short geodesic in any Riemannian manifold.** For $|b - a|$ small enough (less than the injectivity radius), $I$ is positive-definite on $\mathcal V_0^\perp$, and $\gamma$ is a strict local minimum of length and energy. This is because the kinetic term $\int g(V', V')$ scales like $1/|b-a|$ for a fixed-size variation (by Wirtinger inequality), while the curvature term is bounded — so for small intervals the kinetic term dominates.

**Is an instance: a quarter-arc of the round great circle on $S^2$.** Geodesic from north pole to equator, parameter range $[0, \pi/2]$. The Jacobi field $J(t) = \sin t$ has $J(0) = 0$, $J(\pi/2) = 1 \neq 0$ — no interior conjugate points. The index form is positive on $\mathcal V_0^\perp$: $I(V, V) = \int_0^{\pi/2} (V'^2 - V^2)\, dt$ for $V = f e_\perp$, and integration by parts with $V(0) = V(\pi/2) = 0$ gives $I = \int_0^{\pi/2} (f'^2 - f^2) dt > 0$ by Wirtinger's inequality on $[0, \pi/2]$ (best constant: $f''/f = -\pi^2/(\pi/2)^2 = -4 > -1$). So this arc is length-minimising.

**Is an instance: a half-great-circle on $S^2$, parameter range $[0, \pi]$.** Now the conjugate point $J(\pi) = \sin \pi = 0$ is *at* the endpoint, and the kernel of $I$ is $1$-dimensional, spanned by the Jacobi field $V(t) = \sin t \cdot e_\perp$. This is the borderline case: $\gamma$ is a length-minimiser (not strict — there are other minimising geodesics, the other half-great-circle), and the index is $0$ but the nullity is $1$. See [[Ex - Computing the Index Form for a Pole-to-Pole Geodesic on S^2]].

**Is an instance: a geodesic on $S^2$ traversed $1.5$ times around.** Parameter $[0, 3\pi]$. Now there are *two* interior conjugate points (at $\pi$ and $2\pi$), each with multiplicity $1$. By the Morse index theorem, the index is $2$ — there is a $2$-dimensional subspace on which $I$ is negative-definite, so we can produce nearby curves with the same endpoints and strictly shorter length. This geodesic is *not* a local length-minimiser.

**Is an instance: any geodesic in hyperbolic space.** No conjugate points anywhere, so the index is $0$ and the nullity is $0$ for any parameter range. $I$ is positive-definite everywhere, and *every* geodesic between two points is the unique length-minimiser. This is consistent with [[Riemannian Geometry III — Riemann Curvature and Topology|Cartan–Hadamard]].

**Is NOT an instance: a non-normal variation.** If $V = f T$ is tangential ($V \parallel T$), then $V' = f' T$ (since $T' = 0$), so $g(V', V') = f'^2$. And $R(V, T)T = f R(T, T) T = 0$. So $I(V, V) = \int f'^2\, dt > 0$ for $f$ nonzero. The tangential variations always give positive contributions to $I$, but they are not "interesting" — they correspond to reparametrisation of $\gamma$ and do not change the image. Excluding them by restricting to $\mathcal V_0^\perp$ is essential for the right counting.

**Corollary (positivity for short geodesics).** If the parameter interval $[a, b]$ is short enough that no conjugate point lies in $(a, b]$, then $I|_{\mathcal V_0^\perp} > 0$, so $\gamma$ is a strict local length-minimiser. *Calibration check:* the Morse index is the count of interior conjugate points; if there are none, the index is zero and there is no negative direction.

**Corollary (nullity = multiplicity of conjugate pair).** If $\gamma(b)$ is the first conjugate point to $\gamma(a)$ along $\gamma$, then $\dim \ker I|_{\mathcal V_0^\perp} = $ multiplicity of the conjugate pair. *Calibration check:* the kernel is the space of Jacobi fields vanishing at both endpoints, which is by definition the multiplicity space.

**Corollary (index = sum of conjugate-point multiplicities).** $\mathrm{ind}(\gamma) = \sum_{t \in (a, b) : \text{conjugate}} \mathrm{mult}(\gamma(a), \gamma(t))$. *Calibration check:* this is the **Morse Index Theorem**, the main result connecting conjugate points to the variational analysis.

**Corollary (length-minimisation past first conjugate point fails).** If there is a conjugate point strictly inside $(a, b)$, then $\gamma|_{[a, b]}$ is not a local length-minimiser — there is a $V \in \mathcal V_0^\perp$ with $I(V, V) < 0$, hence a nearby curve with the same endpoints and strictly shorter length. *Calibration check:* by Morse index theorem the index is at least $1$, providing a negative direction; the negative direction is realised by a piecewise-Jacobi-field construction.

**Calibration check.** If you can verify (a) that for short enough geodesics $I$ is positive-definite, (b) that the kernel of $I$ on $\mathcal V_0^\perp$ is exactly the Jacobi fields vanishing at both endpoints, and (c) that the index counts interior conjugate points via the Morse theorem — then you have understood the definition.

---

# Unlocked by This

> [!tip] The Morse Index Theorem *(from Riemannian Geometry / Morse Theory)*
> The **Morse Index Theorem** states that the index of $I$ on a unit-speed geodesic equals the number of interior conjugate points counted with multiplicity. This is the prototype of all later Morse-theoretic counting results, including the Morse index for harmonic maps, the Maslov index for Lagrangian intersections, the Atiyah–Singer index theorem for elliptic operators, and the Conley–Zehnder index in symplectic geometry. See **Morse theory of the energy functional**.

> [!tip] **The Bonnet–Myers Diameter Bound** *(from Riemannian Geometry)*
> If the Ricci curvature is bounded below by $(n-1)K_0 g$ with $K_0 > 0$, every geodesic of length at least $\pi/\sqrt{K_0}$ has a conjugate point in its interior, hence index at least $1$, hence is not minimising. By [[Thm - Hopf-Rinow Theorem (Statement)|Hopf–Rinow]], the manifold's diameter is at most $\pi/\sqrt{K_0}$. The proof: pick orthonormal $(e_1, \ldots, e_{n-1})$ at $\gamma(0)$ along $T^\perp$, define test functions $V_i(t) = \sin(\pi t/L) e_i$, compute $\sum_i I(V_i, V_i)$ and use the Ricci-curvature trace identity. The index-form bookkeeping is the entire technical content of Myers' theorem. See [[Riemannian Geometry III — Riemann Curvature and Topology]].

> [!tip] **Spectral Theory of the Jacobi Operator** *(from Spectral Geometry)*
> The Jacobi operator $\mathcal J(V) = V'' + R(V, T)T$ is a self-adjoint second-order differential operator on the space of vector fields along $\gamma$. Its eigenvalues — the **conjugate distances along $\gamma$** — encode the spectrum of curvature concentrated near $\gamma$, and they are the foundation of all comparison and rigidity theorems in spectral Riemannian geometry. The index form is the associated quadratic form, and its index is the count of negative eigenvalues of $\mathcal J$ (with boundary conditions).
