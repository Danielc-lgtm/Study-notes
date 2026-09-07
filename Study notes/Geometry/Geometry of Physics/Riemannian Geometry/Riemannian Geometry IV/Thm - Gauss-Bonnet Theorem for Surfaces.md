---
type: theorem
subject: riemannian-geometry
prereqs:
  - "Def - Gauss Curvature and Mean Curvature"
  - "Def - Gauss Normal Map"
  - "Thm - The Gauss Normal Map has Degree Half the Euler Characteristic"
  - "Def - Geodesic Curvature"
tags: [geometry, riemannian-geometry, surfaces, gauss-bonnet, topology]
---

# Notation

Let $M$ be a closed (compact, no boundary) oriented Riemannian $2$-manifold with Gauss curvature $K$ and area form $dA$. For surfaces with boundary, $\kappa_g$ denotes the [[Def - Geodesic Curvature|geodesic curvature]] of $\partial M$. The Euler characteristic is $\chi(M) = 2 - 2g$ for closed orientable surfaces of genus $g$. Full registry on [[Riemannian Geometry IV — Classical Geometry of Surfaces in R^3]].

---

# Statement

> **Theorem (Gauss–Bonnet, closed orientable surfaces).** Let $M$ be a closed oriented Riemannian $2$-manifold. Then
> $$
> \int_M K\, dA = 2\pi\chi(M),
> $$
> where $K$ is the [[Def - Gauss Curvature and Mean Curvature|Gauss curvature]] of the metric and $\chi(M) = 2 - 2g$ is the Euler characteristic.

> **Theorem (Gauss–Bonnet, with boundary and corners).** Let $M$ be a compact oriented Riemannian $2$-manifold with piecewise smooth boundary $\partial M$ consisting of smooth arcs meeting at corners with exterior angles $\alpha_1, \ldots, \alpha_k$. Then
> $$
> \int_M K\, dA + \int_{\partial M}\kappa_g\, ds + \sum_{i=1}^k \alpha_i = 2\pi\chi(M),
> $$
> where $\kappa_g$ is the [[Def - Geodesic|geodesic]] curvature of $\partial M$ (taken with the outward-pointing tangent orientation).

> **Corollary.** The integral $\int_M K\, dA$ is invariant under any smooth deformation of the metric, even though $K$ itself changes pointwise.

> **Corollary.** A closed orientable surface admits a Riemannian metric of constant positive Gauss curvature only if $\chi > 0$ (sphere); of zero Gauss curvature only if $\chi = 0$ (torus); of constant negative Gauss curvature only if $\chi < 0$ (higher-genus surfaces). This is the rough form of the **uniformisation theorem**.

---

# Motivation

This is the prototypical **local-to-global theorem**: a pointwise local geometric quantity (curvature) integrates over a closed surface to a topological invariant (Euler characteristic). The left side depends on the *metric* (the geometry of $M$); the right side depends only on the *topology*. So the integral is "metric-independent" in the strong sense that any smooth deformation of the metric preserves it, even though it changes $K$ pointwise.

Historically, this is the first theorem of its kind in mathematics, due to Bonnet (1848) building on Gauss's local results. It became the template for many subsequent "local equals global topological" theorems: the higher-dimensional Chern–Gauss–Bonnet (the **[[Def - Pfaffian|Pfaffian]] of the curvature** integrates to $\chi$ on any even-dimensional closed oriented Riemannian manifold), the **Hirzebruch–Riemann–Roch theorem** (the genus of a holomorphic line bundle equals a curvature integral plus the Chern character), the **Atiyah–Singer index theorem** (the analytical index of an elliptic operator equals the topological index, computed from characteristic classes of the underlying bundle).

The conceptual punchline is that **geometry and topology are linked through curvature**. On a closed orientable surface, the total curvature is locked by the genus — you can redistribute it (concentrate $K$ in small regions or spread it uniformly), but the total $\int K\, dA$ is fixed at $2\pi\chi(M)$. This is why the sphere ($\chi = 2$) can support metrics of positive curvature, the torus ($\chi = 0$) only flat or curvature-zero-on-average metrics, and the higher-genus surfaces ($\chi < 0$) only hyperbolic (constant negative curvature) metrics on the constant-curvature side.

---

# Sources and Targets

**Sources (Input Broadening).**

*Source 1: A closed oriented Riemannian surface of known topology.* If the genus $g$ is known, Gauss–Bonnet gives $\int K\, dA$ for free without computing the integrand. **Why $B \Rightarrow A$:** The theorem provides the formula. **Example problem:** A sphere ($\chi = 2$) of any Riemannian metric: $\int K\, dA = 4\pi$. A torus: $\int K\, dA = 0$.

*Source 2: A surface with given curvature distribution.* If $K$ is constant on a known surface, then $K\cdot\mathrm{Area}(M) = 2\pi\chi(M)$, giving $\mathrm{Area}(M) = 2\pi\chi(M)/K$. **Why $B \Rightarrow A$:** Direct substitution. **Example problem:** A sphere of constant curvature $K = 1/a^2$ has area $4\pi a^2$ (verify directly).

*Source 3: A piecewise smooth surface with corners (polyhedral surface).* For a triangulated surface, the curvature concentrates at vertices, and Gauss–Bonnet becomes a *discrete* identity: $\sum_v (\text{angle defect at }v) = 2\pi\chi(M)$, where the angle defect is $2\pi$ minus the sum of angles at $v$ in the incident faces. This is the **Descartes–Gauss–Bonnet** discrete version, predating the smooth case. **Why $B \Rightarrow A$:** The boundary-corrected smooth version with degenerate metrics reduces to the angle-defect formula. **Example problem:** A regular tetrahedron has $4$ vertices each with $3$ equilateral triangle corners ($60°$ each), so the angle defect at each vertex is $2\pi - 3\cdot\pi/3 = \pi$. Sum: $4\pi = 2\pi\cdot 2$, matching $\chi(S^2) = 2$.

**Targets (Output Amplification).**

*Target 1: Topological obstruction to metrics of specified curvature.* A closed surface of genus $\geq 2$ cannot admit a metric of everywhere positive curvature, because $\int K\, dA = 2\pi\chi < 0$. This is a sharp obstruction. **Why nonobvious:** Locally one can always make $K > 0$ on a small piece, but the *integral* is locked by topology. **Application:** Rules out elliptic Riemannian metrics on high-genus surfaces; forces hyperbolic ones (the uniformisation theorem).

*Target 2: Constraints on minimal surfaces, harmonic functions, and other curvature-dependent objects.* Many estimates and inequalities for surfaces involve $\int K\, dA$ as a topological hard upper or lower bound. **Application:** **Heintze–Karcher inequality**, **Bray's mass inequality** for asymptotically flat hypersurfaces — all reduce in $2$ dimensions to combinations involving the Gauss–Bonnet bound.

*Target 3: Computing $\int K\, dA$ on specific surfaces without computing $K$ pointwise.* For a closed oriented surface, you can read off the curvature integral from genus alone. This is sometimes the cleanest way to do the integral, especially when the metric is complicated. **Why nonobvious:** Direct computation might be intractable; the topological shortcut gives the answer immediately.

---

# Why Is It True

The Gauss–Bonnet theorem has multiple proofs, each illuminating a different mechanism. The cleanest is via the **Gauss normal map and Brouwer degree**:

1. For a closed oriented surface $M^2 \subset \mathbb{R}^3$, the [[Def - Gauss Normal Map|Gauss map]] $N : M \to S^2$ has Brouwer degree $\deg(N) = 1 - g = \chi(M)/2$ (see [[Thm - The Gauss Normal Map has Degree Half the Euler Characteristic]]).
2. The change-of-area formula $N^*\mathrm{vol}^2_{S^2} = K\, dA$ holds pointwise (the Jacobian of $N$ at $p$ equals $K(p)$).
3. Integrating: $\int_M K\, dA = \int_M N^*\mathrm{vol}^2_{S^2} = (\deg N)\int_{S^2}\mathrm{vol}^2_{S^2} = 4\pi\cdot(\chi(M)/2) = 2\pi\chi(M)$.

**The bolded one-liner:** **the Gauss curvature is the Jacobian of the Gauss normal map, and the Gauss map's Brouwer degree is half the Euler characteristic — so integrating $K$ gives $4\pi$ times the degree, which equals $2\pi\chi$.**

This proof is *intrinsic on the embedded version* but extends to abstract surfaces (any closed oriented Riemannian $2$-manifold) by a different argument — namely, by triangulating $M$ and applying the boundary-corrected version to each triangle, then summing. The triangle contributions involve geodesic-curvature integrals (zero for geodesic triangles) and angle sums (the **Gauss spherical excess** formula: a geodesic triangle on a unit-curvature surface has angle sum $= \pi + \mathrm{area}$). Summing over a triangulation gives $\sum\text{(angle excesses)} + \sum\text{(boundary integrals)} = 2\pi\chi(M)$, which after cancellation of internal boundary terms reduces to $\int K\, dA = 2\pi\chi$.

An even more abstract perspective via **Cartan's structural equations**: choose a local orthonormal frame $(e_1, e_2)$ on $M$ with dual coframe $(\theta^1, \theta^2)$. The connection $1$-form $\omega^1_{\;2}$ satisfies $d\theta^a + \omega^a_{\;b}\wedge\theta^b = 0$, and the curvature $2$-form is $\Omega^1_{\;2} = d\omega^1_{\;2} = K\theta^1\wedge\theta^2 = K\, dA$. So $K\, dA = d\omega^1_{\;2}$ — *the Gauss curvature density is the differential of the connection $1$-form*. Integrating over $M$ would be zero by Stokes if there were a global $\omega^1_{\;2}$, but on a closed surface of nontrivial topology, a global $\omega^1_{\;2}$ does not exist (the obstruction is exactly $\chi(M)$), and the integral picks up topological contributions.

---

# What Makes This Hard

The conceptual hard part is **connecting the local geometric quantity $K$ to the global topological invariant $\chi$**. Each by itself is straightforward — $K$ is a function on $M$, $\chi$ is a single integer — but their equality is one of the deepest facts in mathematics. The mechanisms (Gauss map degree, triangulation + angle excess, Cartan's curvature $2$-form + Stokes) are each technical, and the cleanest single proof depends on which framework one chooses.

The technical hard part of the **boundary-corrected version** is the **corner contribution**: at each corner of $\partial M$, the tangent turns abruptly by the exterior angle $\alpha_i$, which must be accounted for. A smooth tangent's turning rate is exactly $\kappa_g$; a discontinuous turn at a corner contributes the angle $\alpha_i$ as an additional term. The combined "total turning" of the tangent along $\partial M$ is $\int\kappa_g\, ds + \sum\alpha_i$, and this equals $2\pi\chi(M) - \int K\, dA$ by the corrected Gauss–Bonnet — which expresses that the total turning of a closed loop on $M$ equals $2\pi$ times the Euler characteristic minus the enclosed curvature.

A common confusion: students sometimes try to apply Gauss–Bonnet to non-orientable surfaces (Klein bottle, $\mathbb{RP}^2$). The formula does hold in modified form ($\int K\, dA$ on the orientable double cover equals $2\pi\chi$ of the double cover, then divide by $2$), but the direct formula $\int_M K\, dA = 2\pi\chi(M)$ is not valid on non-orientable surfaces without specifying integration via densities or the orientable cover.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy.** Use the Gauss-map proof (cleanest for embedded surfaces): combine the pointwise change-of-area $N^*\mathrm{vol}^2_{S^2} = K\, dA$ with the degree formula $\deg(N) = \chi(M)/2$.

**Subgoal decomposition:**

1. **Recall the change-of-area formula.** For an oriented surface $M \subset \mathbb{R}^3$ with Gauss map $N : M \to S^2$, $N^*\mathrm{vol}^2_{S^2} = K\,\mathrm{vol}^2_M$.
   - *Hint:* The Jacobian of $N$ at $p$ is the determinant of $dN_p = -S_p$, which equals $\det S_p = K(p)$ up to sign (the sign is positive since both $\mathrm{vol}^2_M$ and $\mathrm{vol}^2_{S^2}$ are oriented).
   - *Why needed:* Translates the curvature integral into an integral of a pullback form.

2. **Apply the definition of Brouwer degree.** $\int_M N^*\mathrm{vol}^2_{S^2} = \deg(N)\cdot\int_{S^2}\mathrm{vol}^2_{S^2}$. (Note: the [[Def - Brouwer Degree of a Map|definition of degree]] involves normalised forms; for the unnormalised $\mathrm{vol}^2_{S^2}$, scale by $1/4\pi$.)
   - *Hint:* $\mathrm{vol}^2_{S^2}/4\pi$ is the normalised form; the degree is $\int_M N^*(\mathrm{vol}^2/4\pi) = (1/4\pi)\int_M N^*\mathrm{vol}^2$.
   - *Why needed:* Converts the integral into "(degree) times (total area of $S^2$)".

3. **Use $\int_{S^2}\mathrm{vol}^2 = 4\pi$ and $\deg(N) = \chi(M)/2$.** Combining: $\int_M K\, dA = \int_M N^*\mathrm{vol}^2_{S^2} = \deg(N)\cdot 4\pi = (\chi(M)/2)\cdot 4\pi = 2\pi\chi(M)$.
   - *Hint:* Substitute the degree formula from [[Thm - The Gauss Normal Map has Degree Half the Euler Characteristic]] and the area of the unit sphere.
   - *Why needed:* Concludes the proof.

---

# Lemma Decomposition

> [!note]- Lemma 1: $N^*\mathrm{vol}^2_{S^2} = K\,\mathrm{vol}^2_M$ (change-of-area for the Gauss map)
> **Statement:** For a closed oriented surface $M \subset \mathbb{R}^3$ with Gauss map $N : M \to S^2$, the pullback of the spherical area form equals the Gauss curvature times the surface area form: $N^*\mathrm{vol}^2_{S^2} = K\, dA$, where $dA = \mathrm{vol}^2_M$.
>
> **Hint:** Compute $N^*\mathrm{vol}^2_{S^2}$ at a point $p$ in local coordinates: $N^*\mathrm{vol}^2_{S^2}(\mathbf{x}_u, \mathbf{x}_v) = \mathrm{vol}^2_{S^2}(N_u, N_v) = \det[(N_u, N_v)\text{ as columns relative to oriented basis at }N(p)] = \det(-dN|_{T_pM}) = \det S = K$. So $N^*\mathrm{vol}^2_{S^2} = K\,du\wedge dv \cdot |\mathbf{x}_u \times \mathbf{x}_v| = K\,\mathrm{vol}^2_M$.
>
> **Why needed:** This is the local-to-global bridge: integrating both sides over $M$ converts a curvature integral into a Gauss-map integral.
>
> > [!note]- Full proof
> > Choose local coordinates $(u, v)$ on $M$ with $\mathbf{x}_u, \mathbf{x}_v$ a positively oriented basis. At $p$, identify $T_{N(p)}S^2 \cong T_pM$ via parallel translation. Then $\mathrm{vol}^2_M(\mathbf{x}_u, \mathbf{x}_v) = |\mathbf{x}_u\times\mathbf{x}_v| = \sqrt{EG - F^2}$. And $\mathrm{vol}^2_{S^2}(N_u, N_v) = \det(\text{matrix of }(N_u, N_v)\text{ in orthonormal basis of }T_{N(p)}S^2)$. Since $-N_u = b^\alpha_{\;1}\mathbf{x}_\alpha$ and $-N_v = b^\alpha_{\;2}\mathbf{x}_\alpha$ (Weingarten equations), and the matrix $b^\alpha_{\;\beta}$ has determinant $K = \det b/\det g$, the determinant of $(-N_u, -N_v)$ in the $(\mathbf{x}_u, \mathbf{x}_v)$ basis is $K$, and in the *parallel-translated* orthonormal basis of $T_{N(p)}S^2$ it is also $K$ (since the bases are orthonormal and the area form is invariant). Thus $\mathrm{vol}^2_{S^2}(N_u, N_v) = K\,\sqrt{EG - F^2}$, so $N^*\mathrm{vol}^2_{S^2} = K\,\mathrm{vol}^2_M$.

> [!note]- Lemma 2: $\deg(N) = \chi(M)/2$
> **Statement:** For a closed oriented surface $M^2 \subset \mathbb{R}^3$ with outward Gauss map $N : M \to S^2$, the Brouwer degree is $\deg(N) = \chi(M)/2 = 1 - g$.
>
> **Hint:** This is [[Thm - The Gauss Normal Map has Degree Half the Euler Characteristic]] — proved via the projection vector field $v(p) = \mathbf{e} - \langle\mathbf{e}, N(p)\rangle N(p)$ and Poincaré–Hopf.
>
> **Why needed:** This is the topological input that converts the Gauss-map integral into a topological count.
>
> > [!note]- Full proof
> > See [[Thm - The Gauss Normal Map has Degree Half the Euler Characteristic]].

> [!note]- Lemma 3: $\int_{S^2}\mathrm{vol}^2_{S^2} = 4\pi$
> **Statement:** The total area of the unit sphere is $4\pi$.
>
> **Hint:** Standard formula from calculus.
>
> **Why needed:** Numerical constant appearing in the final answer.
>
> > [!note]- Full proof
> > $\int_{S^2}\mathrm{vol}^2_{S^2} = \int_0^{2\pi}\int_0^\pi\sin\theta\, d\theta\, d\varphi = 2\pi\cdot[-\cos\theta]_0^\pi = 2\pi\cdot 2 = 4\pi$.

---

# Formal Proof

> [!note]- Complete formal proof (closed orientable surface in $\mathbb{R}^3$)
> Step 0 — Setup: $M^2 \subset \mathbb{R}^3$ is closed, oriented, with outward unit normal $N : M \to S^2$. Combine Lemmas 1–3.
>
> By Lemma 1, $N^*\mathrm{vol}^2_{S^2} = K\, dA$. Integrating over $M$:
> $$
> \int_M K\, dA = \int_M N^*\mathrm{vol}^2_{S^2}.
> $$
> By the definition of Brouwer degree applied to the (un-normalised) form $\mathrm{vol}^2_{S^2}$ (which has total $\int_{S^2}\mathrm{vol}^2 = 4\pi$ by Lemma 3):
> $$
> \int_M N^*\mathrm{vol}^2_{S^2} = \deg(N)\cdot\int_{S^2}\mathrm{vol}^2_{S^2} = \deg(N)\cdot 4\pi.
> $$
> By Lemma 2, $\deg(N) = \chi(M)/2$. Substituting:
> $$
> \int_M K\, dA = 4\pi\cdot\frac{\chi(M)}{2} = 2\pi\chi(M).\qquad\square
> $$
>
> **For an abstract closed oriented Riemannian $2$-manifold** (not necessarily embedded), the proof goes by triangulating $M$ and applying the boundary-corrected Gauss–Bonnet to each triangle:
> $$
> \int_T K\, dA + \int_{\partial T}\kappa_g\, ds + \sum\alpha_i = 2\pi\chi(T) = 2\pi,
> $$
> where $\alpha_i$ are exterior angles. Summing over all triangles in the triangulation: internal-edge $\kappa_g$ contributions cancel in pairs (opposite orientations on adjacent triangles); internal-vertex angle contributions sum to $2\pi - (\text{angle defect at vertex})$; using the Euler formula $V - E + F = \chi(M)$, the angle defects sum to $2\pi\chi(M) - \int K\, dA$, yielding the result.

**Proof of the boundary-corrected version (sketch).** For a compact $M$ with smooth $\partial M$ (no corners), the equation $K\, dA = d\omega^1_{\;2}$ (where $\omega^1_{\;2}$ is the connection $1$-form of the Levi-Civita connection in an orthonormal frame) gives, by Stokes' theorem,
$$
\int_M K\, dA = \int_{\partial M}\omega^1_{\;2}.
$$
The boundary integral $\int_{\partial M}\omega^1_{\;2}$ has two pieces: the **rotation of the tangent relative to parallel transport** (which is $\int_{\partial M}\kappa_g\, ds$ for a smooth boundary) and the **topological holonomy obstruction** (which is $2\pi\chi(M)$ when $M$ has Euler characteristic $\chi$ and the frame is chosen with appropriate singularity structure). The corner contributions $\sum\alpha_i$ enter when $\partial M$ has corners — at each corner, the tangent rotates discontinuously by $\alpha_i$.

---

# Cross-Field Exercise Suggestions

1. **Hyperbolic surfaces of genus $g \geq 2$.** A closed hyperbolic surface (genus $\geq 2$, constant Gauss curvature $K = -1$) has area $\mathrm{Area}(M) = -\int K\, dA = -2\pi\chi(M) = 4\pi(g-1)$. So **every hyperbolic surface of genus $g$ has area $4\pi(g-1)$**. The genus-$2$ "double torus" with hyperbolic metric has area $4\pi$; the genus-$3$ has $8\pi$. This is a beautiful illustration of how Gauss–Bonnet locks the geometry to the topology. **Why nonobvious:** One might think a hyperbolic surface could have arbitrary area, but topology fixes it.

2. **Triangulated polyhedra (Descartes–Gauss–Bonnet).** For a convex polyhedron with $V$ vertices, $E$ edges, $F$ faces, the sum of angle defects at all vertices equals $2\pi(V - E + F) = 2\pi\chi(M) = 4\pi$ for the sphere. **Verification:** For the cube ($8$ vertices, each with $3$ square corners of $90°$, angle defect $= 2\pi - 3\cdot\pi/2 = \pi/2$ per vertex), sum is $8\cdot\pi/2 = 4\pi$. For the tetrahedron, dodecahedron, icosahedron — same result. **Why nonobvious:** Topology determines the angle defect total, independent of the polyhedron's shape.

3. **Cosmological topology (toy general relativity).** In a $(2+1)$-dimensional spacetime with cosmological constant $\Lambda$, the spatial slice $\Sigma$ at any time is a closed orientable $2$-manifold of constant curvature $K = \Lambda$. Gauss–Bonnet then forces: $\Lambda > 0 \Rightarrow \chi > 0 \Rightarrow \Sigma = S^2$; $\Lambda = 0 \Rightarrow \chi = 0 \Rightarrow \Sigma = T^2$; $\Lambda < 0 \Rightarrow \chi < 0 \Rightarrow \Sigma$ is a higher-genus surface. So the **sign of the cosmological constant determines the topology of $(2+1)$-dimensional spatial slices**. This is a toy version of the deep cosmological-topology questions in $4$ [[Def - Dimension|dimensions]]. **Why nonobvious:** A purely topological consequence of a purely physical constant.

---

# Bridges

- **To the **uniformisation theorem** of Riemann surfaces.** Every closed orientable Riemannian $2$-manifold is, after a conformal change of metric, of constant Gauss curvature: $+1$ if $\chi > 0$ ($S^2$), $0$ if $\chi = 0$ ($T^2$), $-1$ if $\chi < 0$ (higher genus). The Gauss–Bonnet theorem is what forces the curvature sign to match the topology: a closed surface of $\chi < 0$ cannot have $K \equiv +1$ because then $\int K\, dA > 0$, contradicting $2\pi\chi < 0$. So the *sign* of the constant curvature is topologically determined. Uniformisation then says the existence of such a metric is guaranteed.

- **To the [[Gauge Theory VI — Chern–Weil Theory, Characteristic Classes, and the Chern–Simons Functional|Chern–Gauss–Bonnet theorem]].** The higher-dimensional generalisation: for a closed oriented Riemannian $2n$-manifold $M$, $\chi(M) = (1/(2\pi)^n)\int_M\mathrm{Pf}(\Omega)$, where $\Omega$ is the curvature $2$-form of the Levi-Civita connection and $\mathrm{Pf}$ is the Pfaffian (a polynomial in the components of $\Omega$). For $n = 1$, $\mathrm{Pf}(\Omega) = K\, dA$, recovering the surface case. The general theorem was proved by Chern in 1944 using the **transgression form** on the principal $SO(2n)$-bundle, and is the gateway to all of characteristic-class theory.

- **To the [[Algebraic Topology I — Singular Homology and the de Rham Theorem|de Rham theorem]].** The form $K\, dA = (1/2\pi)\cdot e(TM)$ (a representative of the Euler class of $TM$ via the Chern–Weil construction); Gauss–Bonnet then expresses $\int_M e(TM) = \chi(M)$, which is the **Euler class formula** for the tangent bundle of a closed oriented surface. The de Rham theorem makes this rigorous: cohomology classes can be evaluated by integration against representative forms.

- **To **scalar curvature and the Yamabe problem**.** On higher-dimensional Riemannian manifolds, the analogue of $K$ is the **scalar curvature** $R$, and the Yamabe problem asks whether every conformal class of metrics on a closed manifold contains one with constant scalar curvature. In dimension $2$, this is exactly the uniformisation theorem and is "easy" via Gauss–Bonnet's topological lock; in higher dimensions, it is much harder (resolved by Trudinger, Aubin, Schoen in the 1980s). The surface case is the prototype.

- **To **knot theory** (the Gauss looping integral).** Gauss's linking integral for two disjoint curves in $\mathbb{R}^3$ is mathematically a Brouwer degree of a $T^2 \to S^2$ map (Frankel §8.3e). The surface-level Gauss–Bonnet for compact orientable surfaces with boundary, applied to a **Seifert surface** of a knot, gives the **self-linking number** invariants of the knot. This is the surface-level precursor of the Witten–Chern–Simons connection between $3$-dimensional quantum field theory and knot invariants.

---

# Unlocked by This

> [!tip] Gauss–Bonnet with Boundary and Corners *(from §4.3)*
> The boundary-corrected version $\int_M K\, dA + \int_{\partial M}\kappa_g\, ds + \sum\alpha_i = 2\pi\chi(M)$ is the natural statement for surfaces with boundary. The corner term $\sum\alpha_i$ accounts for the discontinuous turning of the tangent at corners; the smooth-boundary integral $\int\kappa_g\, ds$ accounts for the continuous turning. Special cases: a hemisphere of the unit sphere has $\int K\, dA = 2\pi$, $\int\kappa_g\, ds = 0$ (the equator is a geodesic), no corners, so $2\pi = 2\pi\chi = 2\pi\cdot 1 = 2\pi$. A geodesic triangle on a unit sphere with angles $A, B, C$ has $\int K\, dA = A + B + C - \pi$ (the **spherical excess** formula, derivable from Gauss–Bonnet).

> [!tip] The Chern–Gauss–Bonnet Theorem *(from Gauge Theory II)*
> The higher-dimensional generalisation $\chi(M^{2n}) = (1/(2\pi)^n)\int_M\mathrm{Pf}(\Omega)$ for a closed oriented Riemannian $2n$-manifold. The Pfaffian of the curvature $2$-form generalises $K\, dA$ to higher dimensions; the integral is intrinsic and equals the Euler characteristic. This is the prototype of all "local geometric quantity integrates to topological invariant" results.

> [!tip] The Uniformisation Theorem of Riemann Surfaces *(from Complex Analysis / Riemannian Geometry)*
> Every closed Riemann surface admits a metric of constant Gauss curvature, of sign determined by the genus: $+1$ for $S^2$, $0$ for $T^2$, $-1$ for higher genus. Equivalently, every Riemann surface is conformally equivalent to $S^2$, $T^2 = \mathbb{C}/\Lambda$, or $\mathbb{H}^2/\Gamma$ for some discrete group $\Gamma$. The sign is forced by Gauss–Bonnet.

> [!tip] The Atiyah–Singer Index Theorem *(from Algebraic Topology III)*
> The grand generalisation: for any elliptic operator $D$ on a closed manifold, the analytical index $\mathrm{ind}_a(D) = \dim\ker D - \dim\mathrm{coker}\, D$ equals a topological index $\mathrm{ind}_t(D)$ computed from characteristic classes of the underlying bundles. Special cases include Gauss–Bonnet (for the de Rham operator), the Riemann–Roch–Hirzebruch theorem (for the Dolbeault operator on Kähler manifolds), and the signature theorem. Gauss–Bonnet is the $2$-dimensional baby case of one of the most important theorems of $20$th-century mathematics.

> [!tip] The Willmore Conjecture *(from Conformal Geometry)*
> The **Willmore energy** $\mathcal{W}(M) = \int_M(H/2)^2\, dA$ is a conformal invariant of immersed closed surfaces in $\mathbb{R}^3$, satisfying $\mathcal{W}(M) - 2\pi\chi(M) \geq 0$ with equality iff $\kappa_1 = \kappa_2$ (umbilic). The Willmore conjecture (Marques–Neves, 2014): for any immersed torus, $\mathcal{W}(M) \geq 2\pi^2$, equality only for the Clifford torus. This is the most spectacular descendant of Gauss–Bonnet in modern $21$st-century conformal geometry.
