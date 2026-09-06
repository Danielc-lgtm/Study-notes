---
type: theorem
subject: riemannian-geometry
prereqs:
  - "Def - Gauss Normal Map"
  - "Def - Brouwer Degree of a Map"
  - "Def - Gauss Curvature and Mean Curvature"
tags: [geometry, riemannian-geometry, surfaces, gauss-bonnet, topology]
---

# Notation

Let $M^2 \subset \mathbb{R}^3$ be a closed (compact, no boundary) oriented regular surface with the outward unit normal $N$. The [[Def - Gauss Normal Map|Gauss normal map]] is $N : M \to S^2$. We write $\chi(M)$ for the Euler characteristic and $g$ for the genus (for an orientable closed surface, $\chi(M) = 2 - 2g$). Full registry on [[Riemannian Geometry IV — Classical Geometry of Surfaces in R^3]].

---

# Statement

> **Theorem.** Let $M^2 \subset \mathbb{R}^3$ be a closed oriented regular surface with outward unit normal $N : M \to S^2$. Then the [[Def - Brouwer Degree of a Map|Brouwer degree]] of the Gauss normal map is
> $$
> \deg(N) = \tfrac{1}{2}\chi(M) = 1 - g,
> $$
> where $\chi(M) = 2 - 2g$ is the Euler characteristic and $g$ is the genus.

> **Corollary (curvature integral formula).** Combining with the change-of-area formula $N^*\mathrm{vol}^2_{S^2} = K\, dA$,
> $$
> \int_M K\, dA = \int_M N^*\mathrm{vol}^2_{S^2} = (\deg N)\int_{S^2}\mathrm{vol}^2 = 4\pi\,\deg(N) = 4\pi(1 - g) = 2\pi\chi(M).
> $$
> This is the [[Thm - Gauss-Bonnet Theorem for Surfaces|Gauss–Bonnet theorem]] derived purely from the topological degree of the Gauss map.

---

# Motivation

The Gauss normal map $N : M \to S^2$ is the cleanest piece of data extracted from a closed oriented surface in $\mathbb{R}^3$: a smooth map between closed oriented $2$-manifolds. As such, it has a [[Def - Brouwer Degree of a Map|Brouwer degree]], an integer measuring "how many times $N$ wraps $M$ around $S^2$, with signs". The remarkable theorem asserts: this integer is *not* a function of the embedding, the metric, the curvature — it depends *only on the genus of $M$*, equalling $1 - g$.

This is the deepest topological fact about the Gauss map and the conceptual heart of the surface-level Gauss–Bonnet theorem. Without this theorem, the Gauss–Bonnet integral formula $\int_M K\, dA = 2\pi\chi(M)$ would be a remarkable coincidence; with this theorem, it is just a consequence of the change-of-area formula $N^*\mathrm{vol}^2_{S^2} = K\, dA$ combined with $\deg(N) = 1 - g$.

The theorem can be proved in two complementary ways: **(a) by direct computation** for model surfaces (sphere, torus, etc.) and topological deformation, using the fact that any closed orientable surface of genus $g$ is smoothly deformable to a "standard" surface (a sphere with $g$ handles) on which the Gauss-map degree can be counted explicitly; **(b) by relating $\deg(N)$ to the Euler characteristic** via the **vector-field intersection** formulation, which we touch on below.

---

# Sources and Targets

**Sources (Input Broadening).**

*Source 1: A closed orientable surface of known genus.* If $g$ is known (e.g., from a topological classification), the theorem immediately gives $\deg(N) = 1 - g$ — no computation needed. **Why $B \Rightarrow A$:** The theorem provides the formula. **Example problem:** For the genus-$2$ surface, $\deg(N) = -1$ — the Gauss map covers $S^2$ "minus once" net, with the negative contributions from saddle regions exceeding positive contributions by one.

*Source 2: An explicit Gauss map for a parametrised surface.* Sometimes one wants to compute $\deg(N)$ directly to *determine* the genus (i.e., use the theorem in the reverse direction). For an explicit parametrisation, one can compute $\deg(N)$ by counting signed preimages of a generic point on $S^2$, or by computing the integral $\int_M K\, dA$ and dividing by $4\pi$. **Why $B \Rightarrow A$:** The two computations agree by the theorem; either can be used. **Example problem:** For a deformed sphere (e.g., a peanut shape), verify that $\deg(N) = 1$ by inspection — the Gauss map covers $S^2$ once.

*Source 3: A vector field on $M$ with known isolated zeros.* By the [[Thm - Poincare-Hopf Theorem for Surfaces|Poincaré–Hopf theorem]], $\sum_p\mathrm{Ind}_p(v) = \chi(M) = 2\deg(N)$, so the Gauss-map degree can be deduced from any vector field's index sum. **Why $B \Rightarrow A$:** Poincaré–Hopf bridges the vector-field index data and the topology. **Example problem:** The vector field "flow toward the north pole" on $S^2$ has indices $+1$ at each pole, sum $= 2 = \chi(S^2) = 2\deg(N) = 2\cdot 1$. Confirmed.

**Targets (Output Amplification).**

*Target 1: Gauss–Bonnet integral formula.* Combined with the change-of-area $N^*\mathrm{vol}^2_{S^2} = K\, dA$, the theorem gives $\int_M K\, dA = 4\pi\deg(N) = 2\pi\chi(M)$. **Why nonobvious:** The change-of-area formula is a local pointwise fact (the Jacobian of $N$ equals $K$); the theorem converts the global integral into a topological invariant. **Application:** the modern proof of Gauss–Bonnet — the cleanest derivation, which requires only the local change-of-area and the topological degree fact.

*Target 2: Topological obstruction to embedding.* If a closed surface $M$ has $\chi(M) = 2$, then $\deg(N) = 1$, meaning the Gauss map wraps $S^2$ once. Surfaces with negative $\chi$ (high genus) have negative-degree Gauss maps, meaning $N$ is "more reverse-oriented than positively-oriented" net — a peculiar geometric situation reflecting the high saddle content. **Application:** Heuristic check on whether a candidate embedded surface is plausible — the genus determined from $\deg(N)$ must match the topological genus.

*Target 3: A purely topological theorem about the Gauss normal map's degree, independent of any geometric features.* The remarkable fact is that two surfaces with the same genus have Gauss maps of the same degree, even if their geometries (metric, curvature, embedding) differ wildly. **Why nonobvious:** Geometric invariants typically depend on the embedding; this one depends only on topology. **Application:** Universal calibration — every embedded sphere in $\mathbb{R}^3$ (no matter how distorted) has Gauss-map degree $+1$.

---

# Why Is It True

The theorem is true because the Gauss map's degree is a **topological invariant of the embedded oriented surface**, and any two oriented closed surfaces of the same genus are smoothly isotopic (in the sense of bordism — they bound the same handlebody-like region) via embeddings in $\mathbb{R}^3$. Hence their Gauss maps' degrees are equal. The degree is then read off from any convenient model — the standard sphere ($\deg = 1$), the standard torus ($\deg = 0$), the standard genus-$g$ surface ($\deg = 1 - g$).

**The bolded one-liner:** **the Gauss-map degree equals $1 - g$ because, on a topologically standard model surface of genus $g$, the Gauss map covers $S^2$ positively $1$ time on a "front-of-the-sphere" region and negatively $g$ times around the $g$ handle "saddles" — net degree $1 - g$.**

A direct picture for the genus-$g$ surface. Imagine the standard embedding: a sphere with $g$ "handles" attached. The sphere contributes positively (the Gauss map there is essentially the identity, degree $+1$). Each handle contributes negatively: the inner side of a handle has $K < 0$ (saddle), and the Gauss map there covers $S^2$ in the *reverse* orientation, contributing $-1$ to the degree. So the total is $+1 - g$. This is the heuristic argument; the rigorous version uses degree-as-signed-preimage-count of a regular value and an explicit computation on the model surface.

The deeper reason is the equivalence between two characterisations of $\chi(M)$:
- **Topological:** $\chi(M) = 2 - 2g$ from the classification of orientable closed surfaces.
- **Geometric / Gauss-map:** $\chi(M)/2 = \deg(N)$ as proved here.

These two definitions agree because both compute the same topological invariant — the Euler number of the tangent bundle $TM$, which is $\chi(M)$ for any closed orientable manifold and which equals twice the Gauss-map degree on a $2$-manifold in $\mathbb{R}^3$.

---

# What Makes This Hard

The hard part is bridging the **degree** (a topological invariant of a map) and the **Euler characteristic** (a topological invariant of the source manifold). They are *both* topological, but defined via different machinery — degree via signed preimage counts, $\chi$ via the alternating sum of Betti numbers or the index sum of a vector field. The theorem asserts a specific numerical relation between them in the special case of the Gauss normal map.

The cleanest proof is via the **Poincaré–Hopf bridge** + a vector-field construction:
1. Construct on $M$ a vector field $v$ whose indices can be related to the Gauss-map's preimage counts.
2. Show that $\sum\mathrm{Ind}_p(v) = 2\deg(N)$.
3. Apply Poincaré–Hopf: $\sum\mathrm{Ind}_p(v) = \chi(M)$.
Combining: $2\deg(N) = \chi(M)$.

Step 1–2 is the substantial content: choose $v$ to be the projection of a fixed unit vector $\mathbf{e} \in \mathbb{R}^3$ onto $TM$ (i.e., $v(p) = \mathbf{e} - \langle\mathbf{e}, N(p)\rangle N(p)$). The zeros of $v$ are exactly the preimages $N^{-1}(\pm\mathbf{e})$ — i.e., points where $N(p) = \pm\mathbf{e}$. There are $\deg(N) + \deg(-N) = 2\deg(N)$ such preimages (counted with sign), and each zero of $v$ has index equal to the sign of its preimage in the Gauss-map count.

A direct proof using the change-of-area formula plus the topological fact $\int K\, dA = 2\pi\chi(M)$ (proved by other means, e.g., Cartan's structural equations on a triangulation) is also possible — but it inverts the logic, taking Gauss–Bonnet as input and deriving the degree.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy.** Use the vector-field bridge: construct $v(p) = \mathbf{e} - \langle\mathbf{e}, N(p)\rangle N(p)$ for a generic fixed $\mathbf{e} \in S^2$ (the projection of $\mathbf{e}$ onto $T_pM$). The zeros of $v$ are exactly the preimages of $\pm\mathbf{e}$ under $N$ — generically $\deg(N) + \deg(-N) = 2\deg(N)$ many, with signs matching the orientation-preserving/reversing pattern of $N$. By Poincaré–Hopf, $\sum\mathrm{Ind}_p(v) = \chi(M)$. Hence $2\deg(N) = \chi(M)$.

**Subgoal decomposition:**

1. **Construct the vector field $v$.** For a generic $\mathbf{e} \in S^2$ (which exists by Sard applied to $N$ and to $-N$), define $v(p) = \mathbf{e} - \langle\mathbf{e}, N(p)\rangle N(p)$ — the orthogonal projection of $\mathbf{e}$ onto $T_pM$.
   - *Hint:* This is a tangent vector at every $p$ (orthogonal to $N$, by construction).
   - *Why needed:* Provides a vector field whose zeros we can analyse.

2. **Identify the zeros of $v$.** $v(p) = 0$ iff $\mathbf{e} = \langle\mathbf{e}, N(p)\rangle N(p)$, iff $\mathbf{e} = \pm N(p)$, iff $N(p) = \pm\mathbf{e}$. So zeros of $v$ are exactly preimages of $\pm\mathbf{e}$ under $N$.
   - *Hint:* $\mathbf{e} = \lambda N(p)$ for some scalar $\lambda$, but $|\mathbf{e}| = |N(p)| = 1$ forces $\lambda = \pm 1$.
   - *Why needed:* Establishes a bijection between zeros of $v$ and preimages under $N$ of $\pm\mathbf{e}$.

3. **Compute indices at zeros via signs of $N$'s preimages.** At a zero $p$ with $N(p) = \mathbf{e}$, the index of $v$ at $p$ equals $\mathrm{sign}\,N(p)$ (the sign in the Brouwer degree formula at the regular preimage $p$). At a zero with $N(p) = -\mathbf{e}$, the index equals $\mathrm{sign}\,(-N)(p) = \mathrm{sign}\,N(p)$ as well (the sign is the same because reversing the source orientation under $p \mapsto -N(p)$ matches reversing the orientation of $\mathbf{e}$).
   - *Hint:* The unit-vector map $v/|v|$ near a zero $p$ is essentially the differential of $N$ projected, and the orientation behaviour matches that of $N$ at the preimage.
   - *Why needed:* Connects the index sum to the Gauss-map degree.

4. **Sum the indices.** $\sum\mathrm{Ind}_p(v) = \sum_{p : N(p) = \mathbf{e}}\mathrm{sign}\,N(p) + \sum_{p : N(p) = -\mathbf{e}}\mathrm{sign}\,N(p) = \deg(N) + \deg(N) = 2\deg(N)$.
   - *Hint:* Both sums count the signed preimages of regular values of $N$, hence both equal $\deg(N)$ (with appropriate orientation conventions on $S^2$).
   - *Why needed:* Identifies $\sum\mathrm{Ind} = 2\deg(N)$.

5. **Apply Poincaré–Hopf.** $\sum\mathrm{Ind}_p(v) = \chi(M)$. Combining with step 4: $2\deg(N) = \chi(M) = 2 - 2g$, hence $\deg(N) = 1 - g$.
   - *Hint:* [[Thm - Poincare-Hopf Theorem for Surfaces|Poincaré–Hopf theorem]].
   - *Why needed:* Concludes the proof.

---

# Lemma Decomposition

> [!note]- Lemma 1: The vector field $v(p) = \mathbf{e} - \langle\mathbf{e}, N(p)\rangle N(p)$ is tangent to $M$
> **Statement:** For any $\mathbf{e} \in S^2$, the field $v(p) = \mathbf{e} - \langle\mathbf{e}, N(p)\rangle N(p) \in \mathbb{R}^3$ lies in $T_pM$ for every $p \in M$.
>
> **Hint:** Take the dot product of $v(p)$ with $N(p)$ — it gives zero, since the projection onto $T_pM$ is the identity minus the projection onto $N(p)$.
>
> **Why needed:** Confirms $v$ is a well-defined tangent vector field on $M$, with values in $TM$.
>
> > [!note]- Full proof
> > $\langle v(p), N(p)\rangle = \langle\mathbf{e}, N(p)\rangle - \langle\mathbf{e}, N(p)\rangle\langle N(p), N(p)\rangle = \langle\mathbf{e}, N(p)\rangle(1 - 1) = 0$.

> [!note]- Lemma 2: Zeros of $v$ are exactly preimages of $\pm\mathbf{e}$ under $N$
> **Statement:** $v(p) = 0$ if and only if $N(p) = \pm\mathbf{e}$.
>
> **Hint:** $v(p) = 0$ means $\mathbf{e} = \langle\mathbf{e}, N(p)\rangle N(p)$, so $\mathbf{e}$ is a scalar multiple of $N(p)$; both are unit vectors, so the scalar is $\pm 1$.
>
> **Why needed:** Translates "zero of $v$" into "preimage of $\pm\mathbf{e}$ under $N$".
>
> > [!note]- Full proof
> > $v(p) = 0$ iff $\mathbf{e} = \langle\mathbf{e}, N(p)\rangle N(p)$. Taking norms: $|\mathbf{e}| = |\langle\mathbf{e}, N(p)\rangle|\cdot|N(p)|$, i.e., $1 = |\langle\mathbf{e}, N(p)\rangle|$. So $\langle\mathbf{e}, N(p)\rangle = \pm 1$, meaning $\mathbf{e}$ and $N(p)$ are parallel (with sign $+1$ for $N(p) = \mathbf{e}$, sign $-1$ for $N(p) = -\mathbf{e}$).

> [!note]- Lemma 3: Index of $v$ at a zero $p$ equals $\mathrm{sign}\,N(p)$
> **Statement:** At an isolated zero $p$ of $v$ where $N(p) = \mathbf{e}$ is a regular value of $N$, $\mathrm{Ind}_p(v) = \mathrm{sign}\,N(p) = \pm 1$ (the sign as in the Brouwer-degree preimage count of $N$ at $\mathbf{e}$).
>
> **Hint:** Near $p$, the map $v$ has differential $dv_p = (I - \mathbf{e}\otimes\mathbf{e})\cdot dN_p$ (the projection composed with $dN_p$); the determinant of this on $T_pM \cong \mathbf{e}^\perp$ equals $\det(dN_p|_{T_pM})$ up to a positive factor.
>
> **Why needed:** Identifies the index of $v$ with the sign of $N$'s preimage — the bridge between vector-field indices and degree.
>
> > [!note]- Full proof (sketch)
> > Choose local coordinates around $p$ adapted to $T_pM$, and a coordinate frame on $S^2$ around $\mathbf{e}$. The linearisation of $v$ at $p$ is $dv_p : T_pM \to T_pM$, given by $dv_p(X) = -\langle\mathbf{e}, dN_p(X)\rangle\mathbf{e} - \langle\mathbf{e}, N(p)\rangle dN_p(X) = -dN_p(X)$ (using $\langle\mathbf{e}, N(p)\rangle = 1$ at this zero and $\langle\mathbf{e}, dN_p(X)\rangle = 0$ because $dN_p(X) \in T_{\mathbf{e}}S^2$ is orthogonal to $\mathbf{e}$). So $dv_p = -dN_p|_{T_pM}$, and the sign of the index of $v$ at $p$ equals $\mathrm{sign}\det(-dN_p|_{T_pM}) = (-1)^2\mathrm{sign}\det(dN_p|_{T_pM}) = \mathrm{sign}\det(dN_p)$, which is exactly the sign $N$ contributes to the Brouwer degree at the regular preimage $p$.

---

# Formal Proof

> [!note]- Complete formal proof
> By Sard's theorem applied to $N : M \to S^2$, the regular values of $N$ are dense in $S^2$. Pick a regular value $\mathbf{e}$ such that $-\mathbf{e}$ is also regular (this is possible because the regular values are dense and the antipodal map is a homeomorphism, so the intersection of regular values of $N$ with $-(\text{regular values})$ is dense). By Lemma 1, the field $v(p) = \mathbf{e} - \langle\mathbf{e}, N(p)\rangle N(p)$ is a smooth tangent vector field on $M$. By Lemma 2, its zeros are exactly the preimages $N^{-1}(\mathbf{e}) \cup N^{-1}(-\mathbf{e})$, all of which are isolated (since $\mathbf{e}, -\mathbf{e}$ are regular values).
>
> By Lemma 3, the index at each zero equals the sign with which that preimage contributes to the Brouwer degree of $N$. Summing:
> $$
> \sum_{p : v(p) = 0}\mathrm{Ind}_p(v) = \sum_{p : N(p) = \mathbf{e}}\mathrm{sign}\,N(p) + \sum_{p : N(p) = -\mathbf{e}}\mathrm{sign}\,N(p) = \deg(N) + \deg(N) = 2\deg(N).
> $$
> By the [[Thm - Poincare-Hopf Theorem for Surfaces|Poincaré–Hopf theorem]], $\sum_p\mathrm{Ind}_p(v) = \chi(M) = 2 - 2g$. Combining:
> $$
> 2\deg(N) = 2 - 2g \quad\Longrightarrow\quad \deg(N) = 1 - g = \tfrac{1}{2}\chi(M).\qquad\square
> $$

**Alternative proof (direct, via model surfaces and isotopy invariance of degree).** Every closed oriented surface of genus $g$ is isotopic to a standard model embedded in $\mathbb{R}^3$ (a sphere with $g$ handles). For each model, compute $\deg(N)$ directly by counting preimages of a generic point on $S^2$: the model sphere gives $\deg(N) = 1$; the model torus gives $\deg(N) = 0$; the genus-$g$ model gives $\deg(N) = 1 - g$. By isotopy invariance of degree (a special case of homotopy invariance, since isotopy is smooth homotopy of embeddings), this is the degree for any oriented closed surface of the same genus. $\square$

---

# Cross-Field Exercise Suggestions

1. **Gauss map of a deformed sphere.** Take a "lumpy" sphere — a sphere with small bumps and dents — embedded in $\mathbb{R}^3$. Although the principal curvatures vary wildly, the genus is $0$ and so $\deg(N) = 1$. Verify by direct computation: count preimages of the north pole, accounting for signs. **Why nonobvious:** The detailed geometry varies but the degree is invariant.

2. **Gauss map of a "many-holed" surface.** Take a surface of genus $g$ realised as a sphere with $g$ handles (a "pretzel"). Compute $\deg(N) = 1 - g$ by counting saddle vs. non-saddle preimages of the "up" direction. **Why nonobvious:** Each handle contributes a saddle region with negative-degree contribution, exactly cancelling out one unit of the original sphere's positive degree.

3. **Gauss map and **regular homotopy** of immersions.** An *immersed* (but not necessarily embedded) closed orientable surface in $\mathbb{R}^3$ also has a Gauss map, and its degree need not equal $1 - g$ — for an immersion that is *regularly homotopic* to an embedding, the degree is the same as the embedding; but regularly inequivalent immersions can have different degrees. This is the **Smale–Hirsch theorem** territory: the set of regular homotopy classes of immersions $M^2 \looparrowright \mathbb{R}^3$ is $\pi_2(V_2(\mathbb{R}^3)) = \pi_2(\mathrm{SO}(3)/\mathrm{SO}(1)) = \pi_2(S^2) = \mathbb{Z}$, with the degree of the **frame Gauss map** as the invariant. **Why nonobvious:** The immersed-surface case is much richer than the embedded case.

---

# Bridges

- **To the [[Thm - Gauss-Bonnet Theorem for Surfaces|Gauss–Bonnet theorem]].** Combined with the change-of-area formula $N^*\mathrm{vol}^2_{S^2} = K\, dA$, this theorem gives the Gauss–Bonnet integral formula $\int_M K\, dA = 4\pi\deg(N) = 2\pi\chi(M)$. Without the degree-equals-$\chi/2$ identification, the curvature integral would not have a clean topological meaning.

- **To the [[Thm - Poincare-Hopf Theorem for Surfaces|Poincaré–Hopf theorem]].** The proof above is essentially Poincaré–Hopf applied to a particular tangent vector field $v(p) = \mathbf{e} - \langle\mathbf{e}, N(p)\rangle N(p)$, with the indices of $v$ at its zeros tracking the signs of $N$'s preimages. So the present theorem and Poincaré–Hopf are essentially the same fact viewed from two angles: "Gauss-map degree = $\chi/2$" and "vector-field index sum = $\chi$".

- **To **characteristic class theory** ([[Algebraic Topology III — Higher Homotopy and Chern Forms]] and [[Gauge Theory II — Principal Bundles, Representations, and Bundle Classification]]).** The Gauss map's degree is the *Euler number* of the tangent bundle, $e(TM) \in H^2(M; \mathbb{Z}) = \mathbb{Z}$ (for $M$ a closed oriented $2$-manifold). The Euler number can be computed as $\int_M e(TM, \nabla)$ for any connection $\nabla$ — the **Chern–Gauss–Bonnet formula**. In higher dimensions, the Euler class is computed as an integral of the **Pfaffian** of the curvature form of the Levi-Civita connection; this is the Chern generalisation of Gauss–Bonnet.

- **To the **classifying map** of the tangent bundle.** The Gauss normal map is the classifying map of the tangent bundle of $M$ as a subbundle of $T\mathbb{R}^3|_M$ — specifically, it classifies $TM$ as the pullback of the tautological line bundle over $\mathrm{Gr}(2, 3) \cong \mathbb{RP}^2$ along the unoriented Gauss map. The *oriented* version (with $S^2$ in place of $\mathbb{RP}^2$) is the degree we computed. This is the precursor to the universal-bundle perspective: every characteristic class of $TM$ pulls back from a universal class on the appropriate Grassmannian via the Gauss map.

---

# Unlocked by This

> [!tip] Gauss–Bonnet Theorem *(from §4.3)*
> Combined with $N^*\mathrm{vol}^2_{S^2} = K\, dA$ and $\int_{S^2}\mathrm{vol}^2 = 4\pi$, the theorem gives $\int_M K\, dA = 2\pi\chi(M)$ — the [[Thm - Gauss-Bonnet Theorem for Surfaces|Gauss–Bonnet theorem]]. This is the cleanest proof of the surface-level Gauss–Bonnet.

> [!tip] The Euler Class and Stiefel–Whitney Class *(from Algebraic Topology III)*
> For any oriented rank-$n$ real vector bundle $E \to M$ over a closed manifold, the **Euler class** $e(E) \in H^n(M; \mathbb{Z})$ encodes obstructions to non-vanishing sections. For $TM$ on a closed oriented $2$-manifold, $e(TM) = \chi(M)$, recovering the present theorem. For higher-rank bundles, the Stiefel–Whitney classes $w_k(E) \in H^k(M; \mathbb{Z}/2)$ generalise the orientability ($w_1$) and spin ($w_2$) obstructions.

> [!tip] The Generalised Gauss Map *(from Submanifold Theory)*
> For a $k$-dimensional submanifold $M^k \subset \mathbb{R}^n$, the **generalised Gauss map** $\gamma : M \to \mathrm{Gr}(k, n)$ sends $p$ to its tangent plane $T_pM$. The pullback of the tautological $k$-plane bundle over the Grassmannian is $TM$, and the pullback of universal characteristic classes gives the Pontryagin, Stiefel–Whitney, and (for orientable submanifolds) Euler classes of $TM$. This is the universal perspective on characteristic classes of submanifolds — see [[Algebraic Topology III — Higher Homotopy and Chern Forms]].
