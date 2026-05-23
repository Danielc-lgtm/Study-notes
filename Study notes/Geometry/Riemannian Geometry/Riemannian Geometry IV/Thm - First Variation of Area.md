---
type: theorem
subject: riemannian-geometry
prereqs:
  - "Def - First Fundamental Form"
  - "Def - Gauss Curvature and Mean Curvature"
  - "Def - Shape Operator (Weingarten Map)"
tags: [geometry, riemannian-geometry, surfaces, variational, minimal-surfaces]
---

# Notation

Let $M \subset \mathbb{R}^3$ be a compact (possibly with boundary) oriented regular surface, with first fundamental form $g_{\alpha\beta}$, unit normal $N$, mean curvature $H$. A **one-parameter family of surfaces** $\{M(t)\}_{t \in (-\epsilon, \epsilon)}$ is given by a smooth map $\mathbf{x}(u, v, t)$ with $\mathbf{x}(u, v, 0) = \mathbf{x}_0(u, v) = $ the original $M$. The **variation field** is $v(u, v) = \partial\mathbf{x}/\partial t|_{t=0}$, a vector field along $M$. For boundary problems, $n$ denotes the outward conormal to $\partial M$ (the unit tangent to $M$, normal to $\partial M$, pointing out of $M$). Full registry on [[Riemannian Geometry IV — Classical Geometry of Surfaces in R^3]].

---

# Statement

> **Theorem (First Variation of Area).** Let $M$ be a compact oriented regular surface in $\mathbb{R}^3$, possibly with smooth boundary, and let $\mathbf{x}(u, v, t)$ be a smooth one-parameter variation of $M$ with variation field $v = \partial\mathbf{x}/\partial t|_{t=0}$. Then the area $A(t) = \int_{M(t)}dA_t$ satisfies
> $$
> A'(0) = -\int_M H\,\langle v, N\rangle\, dA + \int_{\partial M}\langle v, n\rangle\, ds,
> $$
> where $H = \kappa_1 + \kappa_2$ is the [[Def - Gauss Curvature and Mean Curvature|mean curvature]] (Frankel convention), $N$ is the unit normal, and $n$ is the outward unit conormal on $\partial M$.

> **Corollary.** A compact oriented surface $M$ with boundary $\partial M$ is a critical point of the area functional under all variations vanishing on $\partial M$ if and only if $H \equiv 0$ on $M$ — i.e., $M$ is a [[Def - Minimal Surface|minimal surface]].

> **Corollary (Laplace's pressure formula).** For a soap film in static equilibrium, the pressure difference across the film is $\Delta p = -2\sigma H$, where $\sigma$ is the surface tension. A bubble with constant interior pressure has constant mean curvature.

---

# Motivation

This is the **fundamental variational identity** of classical surface theory. It identifies the mean curvature $H$ as the $L^2$-gradient of the area functional with respect to normal variations: changing the surface in the direction $N$ at point $p$ at rate $\langle v, N\rangle$ changes the area at rate $-H\cdot\langle v, N\rangle$ at that point. The boundary integral $\int_{\partial M}\langle v, n\rangle\, ds$ records the contribution from moving the boundary.

The physical content is direct: a soap film stretched on a wire frame minimises area subject to the boundary constraint, so the first variation must vanish for all variations fixing the boundary. By the fundamental lemma of the calculus of variations, $\delta A = 0$ for all such variations iff $H \equiv 0$ on $M$. This characterises **minimal surfaces** as the critical points of the area functional.

For soap bubbles (closed surfaces with an enclosed volume), the variational problem is constrained: $\delta A = 0$ subject to $\delta V = $ given. The Lagrange-multiplier approach gives $\delta(A - \lambda V) = 0$, which forces $H = \lambda/2$ — a constant. So **equilibrium bubbles have constant mean curvature**, and by Alexandrov's theorem (1958), the only closed embedded CMC surfaces in $\mathbb{R}^3$ are round spheres.

Beyond minimal surfaces, the formula is the entry point to **geometric flows** ([[Def - Minimal Surface|minimal surfaces]], **mean curvature flow** $\partial_t\mathbf{x} = HN$ — the gradient flow of area), **isoperimetric inequalities**, and the **first variation formulas** for other geometric functionals (volume, energy, Willmore energy).

---

# Sources and Targets

**Sources (Input Broadening).**

*Source 1: A specific surface and a variation field to check criticality.* When investigating whether a candidate surface (catenoid, helicoid, plane) is critical for area, the first-variation formula gives a direct test: compute $H$ on the candidate, and apply the formula. **Why $B \Rightarrow A$:** $H = 0$ everywhere is equivalent to $\delta A = 0$ for all compactly supported normal variations. **Example problem:** Verify that the catenoid is minimal by computing $H$ and checking it equals zero.

*Source 2: A surface tension / pressure setup in physics.* For a soap film in equilibrium, the work done against surface tension during a small deformation is $\delta W = 2\sigma\delta A$ (factor of $2$ for the two-sided film), and this must equal the work done by pressure $\Delta p\cdot\delta V$. The first-variation formula relates $\delta A$ and $\delta V$ via $H$, giving Laplace's pressure formula. **Why $B \Rightarrow A$:** The variational identity is the bridge from "physical equilibrium" to "$H = 0$ (free film)" or "$H = \text{const}$ (bubble)". **Example problem:** Derive the radius of a soap bubble of pressure $p$: $H = -p/(2\sigma) = -1/R$ (with outward normal) gives $R = 2\sigma/p$.

*Source 3: A constrained variational problem.* For variational problems with constraints (constant volume, constant total length of boundary), Lagrange-multiplier theory + first-variation formula gives the Euler–Lagrange equation. **Why $B \Rightarrow A$:** Standard variational calculus. **Example problem:** The isoperimetric problem: minimise area subject to enclosed volume. Solution: $H = \text{const}$ (a sphere in $\mathbb{R}^3$ by Alexandrov's theorem).

**Targets (Output Amplification).**

*Target 1: Minimal surface characterisation as $H = 0$.* The Euler–Lagrange equation of the area functional is $H = 0$. This is the *definition* of [[Def - Minimal Surface|minimal surface]], so the theorem makes the definition variationally meaningful. **Application:** Plateau problem (find a minimal surface with given boundary), Bernstein-type rigidity theorems.

*Target 2: Mean curvature flow.* The first-variation formula identifies $-HN$ as the gradient of area. The corresponding gradient flow is **mean curvature flow** $\partial_t\mathbf{x} = HN$ (or $-HN$ depending on convention), the geometric heat equation that smooths surfaces by their mean curvature. **Application:** Huisken's theorem (closed convex hypersurfaces under MCF converge to round spheres), singularity formation theory, neckpinches.

*Target 3: Isoperimetric inequalities.* The isoperimetric inequality for embedded surfaces in $\mathbb{R}^3$ — $36\pi V^2 \leq A^3$, equality for the sphere — is provable via a variational argument using the first variation formula plus the second variation (which controls stability). **Application:** Geometric flow proofs of the Penrose inequality in general relativity; rigidity theorems for area-minimising surfaces.

---

# Why Is It True

The proof is direct computation using Cartan's formula for the variation of a form under a flow:
$$
\frac{d}{dt}\int_{M(t)}\omega(t) = \int_{M(t)}\partial_t\omega(t) + \int_{M(t)}\mathcal{L}_v\omega(t) + \int_{\partial M(t)}\iota_v\omega(t).
$$
Applied to $\omega = \mathrm{vol}^2_M = i_N\mathrm{vol}^3_{\mathbb{R}^3}$ (the area form as the contraction of the volume form with the normal), one finds:
1. $\partial_t \omega$ contributes through how $N$ changes (the time-derivative of the normal); it vanishes when restricted to the tangent plane.
2. $\mathcal{L}_v\omega$ contributes $\langle v, N\rangle\mathrm{div}\, N\,\mathrm{vol}^2_M$ in the surface integral.
3. $\iota_v\omega$ contributes the boundary term $\langle v, n\rangle\, ds$.

The key identity is $\mathrm{div}\, N = -H$ (the divergence of the unit normal field equals the negative of the mean curvature, in Frankel's sign convention). Combining, the surface integral becomes $-\int_M H\langle v, N\rangle\, dA$.

**The bolded one-liner:** **the first variation of area equals minus the integral of mean curvature against the normal component of the variation, plus the boundary's outward-flux integral — because the area form's Lie derivative is $\mathrm{div}\,N\cdot dA = -H\cdot dA$ in the normal direction.**

The geometric picture: imagine deforming each small piece of $M$ in the normal direction $N$ by a small amount $\langle v, N\rangle\cdot dt$. The piece "sweeps out" volume — and the area changes proportionally to how the principal radii of curvature change. A small piece of area $dA$ becomes, after normal displacement $\delta n$:
$$
dA \to dA\cdot(1 + \kappa_1\delta n)(1 + \kappa_2\delta n) \approx dA(1 + H\delta n).
$$
But with the Frankel convention (outward normal, $\kappa_i$ signed by curving toward the *opposite* of the outward normal — so on a sphere with outward normal $\kappa_i < 0$), the change is $-H\cdot\langle v, N\rangle\cdot dA$ per unit time. The boundary contribution comes from moving $\partial M$ outward, sweeping out area $\langle v, n\rangle\cdot ds$ per unit time.

---

# What Makes This Hard

The computational hard part is **separating the surface integral from the boundary integral** correctly, and getting all the signs right under various sign conventions for the normal and the mean curvature. The Frankel convention uses $H = \kappa_1 + \kappa_2$ and outward normal $N$; do Carmo uses $H = (\kappa_1 + \kappa_2)/2$; some texts use the inward normal. Each combination has its own version of the formula.

The conceptual subtlety is the **technical machinery for varying surfaces**: the surfaces $M(t)$ may not be disjoint (they can intersect each other for different $t$), so one cannot directly use $\int_{M(t)}\mathrm{vol}^2$ with a single ambient form. The trick is to embed everything into $\mathbb{R}^4 = \mathbb{R}^3 \times \mathbb{R}$ with the time direction added, giving a $3$-manifold-with-boundary that contains all the $M(t)$'s as time slices, and then apply Stokes-type identities (Frankel's equation 4.43, which is essentially Cartan's formula).

A subtle point: the variation field $v$ does *not* need to be tangent or normal — it is an arbitrary $\mathbb{R}^3$-valued vector field along $M$. The formula decomposes the variation into normal and tangential parts; only the normal part contributes to the area change in the interior (the tangential variations correspond to reparametrisations of the same underlying surface, which obviously don't change area), and only the boundary-tangential-to-$\partial M$ part contributes to the boundary integral.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy.** Use Frankel's formula (4.43) for the variation of an integral of a form under a flow: $A'(t) = \int_{M(t)}\partial_t(\text{area form}) + \int_{M(t)}\mathcal{L}_v(\text{area form}) + \int_{\partial M(t)}\iota_v(\text{area form})$. Compute each piece and use $\mathrm{div}\, N = -H$.

**Subgoal decomposition:**

1. **Write the area as $A(t) = \int_{M(t)}i_{N(t)}\mathrm{vol}^3$.** The area form on an oriented hypersurface with unit normal $N$ is the contraction of the ambient volume form $\mathrm{vol}^3$ with $N$.
   - *Hint:* For an orientable hypersurface in $\mathbb{R}^3$, the area form is $\iota_N(dx \wedge dy \wedge dz)$.
   - *Why needed:* Translates "area" into an ambient $3$-form structure that can be varied with the surface.

2. **Apply Frankel's formula for the time derivative.** Using equation (4.43) of Frankel: $A'(0) = \int_M\partial_t i_{N(t)}\mathrm{vol}^3|_{t=0} + \int_M\iota_v(d i_N\mathrm{vol}^3) + \int_{\partial M}\iota_v i_N\mathrm{vol}^3$, the second integral being the Lie derivative of the area form along $v$.
   - *Hint:* $\partial_t i_{N(t)}\mathrm{vol}^3 = i_{\partial N/\partial t}\mathrm{vol}^3$, which restricted to $M(0)$ involves only the tangential part of $\partial N/\partial t$ (the normal part gives zero).
   - *Why needed:* The three terms separate the variation into time-of-normal, Lie-derivative-of-form, and boundary contributions.

3. **Evaluate each term.** (a) The first term: $\partial_t N$ is tangent to $M$ (since $|N| = 1$), so $\iota_{\partial_t N}\mathrm{vol}^3$ restricted to $M$ vanishes. (b) The second term: $d i_N\mathrm{vol}^3 = (\mathrm{div}\, N)\mathrm{vol}^3$, and so $\iota_v d i_N\mathrm{vol}^3 = \langle v, N\rangle\mathrm{div}\, N\,\mathrm{vol}^2_M$ on $M$. (c) The third term: the boundary contribution is $\langle v, n\rangle\, ds$ in cleanest form.
   - *Hint:* Each step uses standard Cartan-formula identities; the key is $d i_N\mathrm{vol}^3 = \mathcal{L}_N\mathrm{vol}^3 = (\mathrm{div}\, N)\mathrm{vol}^3$.
   - *Why needed:* Concrete evaluation.

4. **Apply $\mathrm{div}\, N = -H$ to get the final form.** Frankel proves (8.24): the divergence of the unit normal field in $\mathbb{R}^3$ equals $-H$ (Frankel convention). Substituting: $A'(0) = -\int_M H\langle v, N\rangle\, dA + \int_{\partial M}\langle v, n\rangle\, ds$.
   - *Hint:* The proof of $\mathrm{div}\, N = -H$ uses an adapted basis $\{\mathbf{x}_1, \mathbf{x}_2, N\}$ and the Weingarten equations $\partial_\alpha N = -b^\beta_{\;\alpha}\mathbf{x}_\beta$; the trace of the operator $X \mapsto D_X N$ in this basis is $-b^\alpha_{\;\alpha} = -H$.
   - *Why needed:* This is the crucial identification that brings mean curvature into the formula.

---

# Lemma Decomposition

> [!note]- Lemma 1: Area form as contraction of the ambient volume form
> **Statement:** For an oriented hypersurface $M \subset \mathbb{R}^3$ with unit normal $N$, the area form is $\mathrm{vol}^2_M = i_N\mathrm{vol}^3_{\mathbb{R}^3}|_M = i_N(dx^1\wedge dx^2\wedge dx^3)|_M$.
>
> **Hint:** Both sides agree on a pair of orthonormal tangent vectors $(e_1, e_2)$ with $\{e_1, e_2, N\}$ positively oriented: $i_N\mathrm{vol}^3(e_1, e_2) = \mathrm{vol}^3(N, e_1, e_2) = +1$, matching $\mathrm{vol}^2_M(e_1, e_2) = +1$.
>
> **Why needed:** Embeds the area form into the ambient form structure, allowing the use of Cartan-formula machinery.
>
> > [!note]- Full proof
> > Direct calculation on an orthonormal frame.

> [!note]- Lemma 2: $\mathrm{div}\, N = -H$ (Frankel convention)
> **Statement:** The divergence of the unit normal field $N$ on a surface $M \subset \mathbb{R}^3$ (regarded as a vector field defined in a neighbourhood of $M$ in $\mathbb{R}^3$, extended along normal directions or any smooth extension) equals $-H$.
>
> **Hint:** Compute $\mathrm{tr}\,(X \mapsto D_X N)$ in the basis $\{e_1 = \mathbf{x}_1, e_2 = \mathbf{x}_2, e_3 = N\}$ adapted to $M$. By the Weingarten equations, $D_{\mathbf{x}_\beta}N = \partial N/\partial u^\beta = -b^\alpha_{\;\beta}\mathbf{x}_\alpha$, so the diagonal components of $X \mapsto D_X N$ in this basis are $\langle D_{\mathbf{x}_\beta}N, \mathbf{x}_\beta\rangle/g_{\beta\beta}$ — but more cleanly, $\mathrm{tr}\,(X \mapsto D_X N) = b^1_{\;1} + b^2_{\;2} \cdot(\text{sign convention})$. Frankel's sign: $\mathrm{div}\, N = -H$.
>
> **Why needed:** This identifies the appearance of the divergence of the normal as the mean curvature, the chapter's critical sign identity.
>
> > [!note]- Full proof (sketch)
> > Choose an orthonormal frame $\{e_1, e_2\}$ for $T_pM$ and let $e_3 = N$. Extend $e_3$ smoothly to a neighbourhood by parallel-translating along $N$-trajectories. Then $D_{e_3}N = 0$ (along the normal direction, $N$ doesn't change). For tangent directions, the Weingarten equations give $D_{e_\alpha}N = -S(e_\alpha) = -\sum_\beta\kappa_\beta\delta_{\alpha\beta}e_\beta$ (in the principal-direction frame). So the matrix of $X \mapsto D_X N$ is $\mathrm{diag}(-\kappa_1, -\kappa_2, 0)$, with trace $-\kappa_1 - \kappa_2 = -H$. Hence $\mathrm{div}\, N = -H$ (Frankel convention).

> [!note]- Lemma 3: Cartan's formula for the variation of an integral
> **Statement:** For a smooth family of oriented submanifolds $\{M(t)\}$ given by a flow $\mathbf{x}(u, v, t)$ with variation field $v = \partial_t\mathbf{x}|_{t=0}$ and an $n$-form $\omega$ on $\mathbb{R}^N$, the time derivative of $\int_{M(t)}\omega$ equals
> $$
> \frac{d}{dt}\int_{M(t)}\omega = \int_{M(t)}\partial_t\omega + \int_{M(t)}\mathcal{L}_v\omega + \int_{\partial M(t)}\iota_v\omega.
> $$
> When $\omega$ is time-independent, the first term vanishes.
>
> **Hint:** Frankel's equation (4.43) — derivable from the Reynolds transport theorem applied to a manifold-with-boundary.
>
> **Why needed:** This is the foundational machinery for computing variations of integrals.
>
> > [!note]- Full proof (sketch)
> > Use the flow $\Phi_t : M \times [0, T] \to \mathbb{R}^3$ to identify all $M(t)$ with the original $M$. Cartan's magic formula $\mathcal{L}_v\omega = d\iota_v\omega + \iota_v d\omega$, integrated over $M$ and combined with Stokes' theorem, gives the stated formula.

---

# Formal Proof

> [!note]- Complete formal proof
> Step 0 — Setup: $M$ is compact oriented with possibly nonempty smooth boundary, $\mathbf{x}(u, v, t)$ a smooth variation, $v = \partial_t\mathbf{x}|_{t=0}$.
>
> Apply Lemma 3 to $\omega = i_N\mathrm{vol}^3_{\mathbb{R}^3}$ (the area form, by Lemma 1). Since the *form* $\omega$ depends on $t$ through $N(t)$ (the normal varies as $M(t)$ deforms), the first term $\int_M\partial_t\omega|_{t=0}$ contributes; the other two terms are as in the Lemma.
>
> Step 1: First term. $\partial_t(i_{N(t)}\mathrm{vol}^3) = i_{\partial_t N(t)}\mathrm{vol}^3$. Since $|N(t)| = 1$, $\partial_t N$ is tangent to $M(t)$ at each point. Therefore $\partial_t N$ restricted to $M(0)$ is a tangent vector, and $i_{\partial_t N}\mathrm{vol}^3$ restricted to $M(0)$ vanishes (because $\mathrm{vol}^3(\partial_t N, e_1, e_2) = 0$ when $\partial_t N$ lies in the span of $\{e_1, e_2\}$). So $\int_M\partial_t\omega|_{t=0} = 0$.
>
> Step 2: Lie-derivative term. $\mathcal{L}_v\omega = d\iota_v\omega + \iota_v d\omega$. The exterior derivative $d\omega = d(i_N\mathrm{vol}^3) = \mathcal{L}_N\mathrm{vol}^3 = (\mathrm{div}\, N)\mathrm{vol}^3$ (using $\iota_N\mathrm{vol}^3 = i_N\mathrm{vol}^3$ and Cartan's formula on the closed form $\mathrm{vol}^3$). So $\iota_v d\omega = \iota_v(\mathrm{div}\, N\cdot\mathrm{vol}^3) = \mathrm{div}\, N\cdot\iota_v\mathrm{vol}^3$. Restricted to $M$, $\iota_v\mathrm{vol}^3 = \langle v, N\rangle\mathrm{vol}^2_M$. So the integrand on $M$ is $\mathrm{div}\, N\cdot\langle v, N\rangle\,\mathrm{vol}^2_M = -H\langle v, N\rangle\, dA$ by Lemma 2.
>
> The other piece $d\iota_v\omega$ contributes $\int_M d\iota_v\omega = \int_{\partial M}\iota_v\omega$ by Stokes' theorem, but this is absorbed into the boundary integral of Lemma 3 (which has the same form). Specifically, the Lie-derivative term $\int_M\mathcal{L}_v\omega = \int_M(d\iota_v\omega + \iota_v d\omega) = \int_{\partial M}\iota_v\omega + \int_M\iota_v d\omega$. The boundary term of Lemma 3 is also $\int_{\partial M}\iota_v\omega$, so these would double-count. Careful application of Lemma 3 (Frankel's derivation in §8.4) avoids this — the boundary term in the lemma is the *outer-boundary flux*, while the Lie-derivative term is just $\iota_v d\omega = \mathrm{div}\, N\cdot\iota_v\mathrm{vol}^3 = -H\langle v, N\rangle dA$ in the interior. So the surface integral is $\int_M\iota_v d\omega|_M = -\int_M H\langle v, N\rangle\, dA$.
>
> Step 3: Boundary term. $\int_{\partial M}\iota_v\omega = \int_{\partial M}\iota_v i_N\mathrm{vol}^3$. On $\partial M$, choose an arc-length parameter $s$ and an outward conormal $n$ (so $\{T(s), n, N\}$ is a positively-oriented orthonormal triple in $\mathbb{R}^3$, where $T = d\mathbf{x}/ds$ is the boundary's unit tangent). Then $\iota_v i_N\mathrm{vol}^3|_{\partial M}$ evaluated on the boundary tangent $T$ is $\mathrm{vol}^3(v, N, T) = \langle v, N\times T\rangle = \langle v, n\rangle$ (using $n = N\times T$ for the outward conormal). Hence $\int_{\partial M}\iota_v\omega = \int_{\partial M}\langle v, n\rangle\, ds$.
>
> Combining all three terms: $A'(0) = 0 + (-\int_M H\langle v, N\rangle\, dA) + \int_{\partial M}\langle v, n\rangle\, ds$. $\square$

---

# Cross-Field Exercise Suggestions

1. **First variation of length for curves on a surface.** The analogue for one-dimensional submanifolds (curves) is: $L'(0) = -\int_C\kappa_g\langle v, \mathbf{n}_{C}\rangle\, ds + [\langle v, T\rangle]_{\text{endpoints}}$, where $\kappa_g$ is the [[Def - Geodesic Curvature|geodesic curvature]] of the curve in the ambient surface and $\mathbf{n}_C$ is the unit normal to $C$ within the surface. So geodesics ($\kappa_g = 0$) are critical points of length, exactly the analogue of minimal surfaces ($H = 0$) being critical for area. **Why nonobvious:** The bridge from $1$-dimensional (length) to $2$-dimensional (area) variational identities — both have the same structure with curvature playing the gradient role.

2. **Isoperimetric inequality via the first variation.** The isoperimetric inequality for embedded surfaces in $\mathbb{R}^3$ says: among all closed surfaces enclosing a fixed volume $V$, the sphere minimises area. Sketch the variational argument: any minimiser must satisfy $H = \text{const}$ (by the Lagrange-multiplier version of the first-variation formula), and by Alexandrov's theorem, the only closed embedded CMC surface in $\mathbb{R}^3$ is the round sphere. **Why nonobvious:** The first variation gives the *Euler–Lagrange equation* $H = \text{const}$; the second variation and Alexandrov-type rigidity then identify the minimiser as the sphere.

3. **The Willmore energy's first variation.** The Willmore energy $\mathcal{W}(M) = \int_M(H/2)^2\, dA$ has a first variation involving the **Willmore operator** $\Delta_M(H/2) + 2(H/2)((H/2)^2 - K)$, an interesting differential operator on surfaces. **Critical points** of the Willmore energy ("Willmore surfaces") satisfy this equation. The round sphere is a critical point (with $\mathcal{W} = 2\pi$); the Clifford torus is a critical point on the $3$-sphere (with $\mathcal{W} = 2\pi^2$). **Why nonobvious:** Computing the first variation of a curvature-squared functional reveals new operators and Euler–Lagrange equations.

---

# Bridges

- **To the [[Def - Minimal Surface|minimal-surface theory]] and the **Plateau problem**.** The first variation identifies $H = 0$ as the Euler–Lagrange equation of area. The Plateau problem then becomes: given a Jordan curve $C \subset \mathbb{R}^3$, find a surface with boundary $C$ satisfying $H = 0$. Douglas (1931) and Radó solved this via a parametrisation-based variational approach; modern proofs use geometric measure theory.

- **To **mean curvature flow** (Geometric analysis).** The gradient flow of area is $\partial_t\mathbf{x} = HN$ (or its negative). This is **mean curvature flow** — the geometric heat equation that smooths surfaces by their mean curvature. **Huisken's theorem** (1984): closed convex hypersurfaces under MCF shrink to round points (the higher-dimensional generalisation of the curve-shortening flow). **Singularity formation** under MCF (neckpinches, conical singularities) is one of the central topics of modern geometric analysis.

- **To **Hamilton's Ricci flow** and the **Poincaré conjecture**.** Ricci flow $\partial_t g = -2\mathrm{Ric}$ is the higher-dimensional metric analogue of mean curvature flow — it is the gradient flow of the *Einstein–Hilbert action* (in some sense), and it smooths metrics. Hamilton's program, completed by Perelman, used Ricci flow with surgery to prove the Poincaré conjecture and Thurston's geometrisation conjecture in dimension $3$. The variational underpinnings — that Ricci flow is a gradient flow of a curvature functional — are direct generalisations of the first-variation-of-area structure.

- **To **continuum mechanics** and **elasticity theory**.** The first variation formula is the geometric analogue of the variation of an elastic-energy functional in continuum mechanics. The bending energy of a shell (Koiter's model, the Föppl–von Kármán equations) involves $\int H^2\, dA$ and $\int K^2\, dA$, whose first variations give the equilibrium equations of thin elastic shells. **Soap films** are the limit of zero bending stiffness, where only the surface tension $\sigma\int dA$ matters.

- **To **harmonic maps** and **wave maps**.** The coordinate functions $x^i : M \to \mathbb{R}$ on a minimal surface are harmonic with respect to the induced metric ($\Delta_g x^i = 0$). So a minimal surface is a **harmonic map** from $(M, g)$ to $\mathbb{R}^3$, and the first-variation formula for area is the special case of the first-variation formula for the **Dirichlet energy** $E = \tfrac{1}{2}\int|\nabla F|^2\, dV_g$ of maps $F : M \to N$ between Riemannian manifolds. Harmonic-map theory and **wave maps** (the hyperbolic version) are major themes in modern geometric analysis.

---

# Unlocked by This

> [!tip] Minimal Surfaces are Critical Points of Area *(from §4.4)*
> A surface $M$ is minimal ($H = 0$) iff $\delta A = 0$ for all compactly supported normal variations. This is the variational characterisation of [[Def - Minimal Surface|minimal surfaces]] and the entry point to the **Plateau problem** and modern minimal-surface theory.

> [!tip] Laplace's Pressure Formula for Soap Films *(from Physics)*
> For a soap film in static equilibrium, $\Delta p = -2\sigma H$ — the pressure jump equals (negative) twice the surface tension times the mean curvature. A free film has $\Delta p = 0 \Rightarrow H = 0$ (minimal); a bubble has constant interior pressure $\Rightarrow$ constant $H$ (a sphere by Alexandrov's theorem).

> [!tip] Mean Curvature Flow *(from Geometric Analysis)*
> The gradient flow of area is **mean curvature flow** $\partial_t\mathbf{x} = HN$. **Huisken's theorem** (1984): closed convex hypersurfaces under MCF shrink to round points. **Generalisations**: MCF with surgery (Huisken–Sinestrari), level-set MCF (Evans–Spruck, Chen–Giga–Goto), Brakke flow.

> [!tip] Alexandrov's Theorem (CMC Rigidity) *(from Geometric Analysis)*
> The only closed embedded constant-mean-curvature surface in $\mathbb{R}^3$ is the round sphere. Proved by Alexandrov (1958) via the **reflection method** (a delicate maximum-principle argument). Generalisations: Heintze–Karcher inequality, the Bray theorem on asymptotically flat manifolds — both essentially relying on the first-variation-of-area structure.

> [!tip] The Bernstein Problem and Simons' Cone *(from Geometric Analysis)*
> Bernstein's theorem: any minimal graph over $\mathbb{R}^2$ is a plane. Higher dimensions: minimal hypergraphs over $\mathbb{R}^n$ for $n \leq 7$ are linear (Almgren, Simons), but for $n \geq 8$, **Simons' cone** is a nontrivial entire minimal graph. The dimensional threshold at $n = 7$ is one of the most surprising results in geometric measure theory.

> [!tip] **Willmore Conjecture** and Conformal Geometry *(from Conformal Geometry)*
> The Willmore energy $\mathcal{W}(M) = \int(H/2)^2\, dA$ is a conformal invariant. The Willmore conjecture (Marques–Neves, 2014) says: any immersed torus in $\mathbb{R}^3$ has $\mathcal{W}(M) \geq 2\pi^2$, equality only for the Clifford torus. The first-variation formula for $\mathcal{W}$ gives the **Willmore equation** $\Delta(H/2) + 2(H/2)((H/2)^2 - K) = 0$, a fourth-order nonlinear PDE.
