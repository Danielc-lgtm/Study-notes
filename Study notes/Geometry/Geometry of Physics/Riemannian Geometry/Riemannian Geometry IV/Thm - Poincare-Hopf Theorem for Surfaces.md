---
type: theorem
subject: differential-topology
prereqs:
  - "Def - Kronecker Index of a Vector Field"
  - "Def - Brouwer Degree of a Map"
  - "Def - Vector Field on a Manifold"
tags: [topology, differential-topology, vector-fields, euler-characteristic]
---

# Notation

Let $M$ be a closed (compact, no boundary) oriented smooth $n$-manifold (we focus on $n = 2$, the surface case), and $v$ a smooth tangent vector field on $M$ with isolated zeros. For each zero $p$ of $v$, $\mathrm{Ind}_p(v)$ is the [[Def - Kronecker Index of a Vector Field|Kronecker (Poincaré–Hopf) index]] — the Brouwer degree of $v/|v|$ on a small sphere around $p$. $\chi(M)$ is the Euler characteristic of $M$. Full registry on [[Riemannian Geometry IV — Classical Geometry of Surfaces in R^3]].

---

# Statement

> **Theorem (Poincaré–Hopf, surface version).** Let $M$ be a closed oriented smooth $2$-manifold, and let $v$ be a smooth tangent vector field on $M$ with only isolated zeros $p_1, \ldots, p_k$. Then the sum of indices equals the Euler characteristic:
> $$
> \sum_{i=1}^k \mathrm{Ind}_{p_i}(v) = \chi(M).
> $$
> In particular, the sum is independent of the choice of vector field $v$.

> **Corollary (Existence of zeros).** If $\chi(M) \neq 0$, every smooth tangent vector field on $M$ has at least one zero. So no nowhere-vanishing tangent vector field exists on $S^2$ (the [[Ex - Hairy Ball Theorem from Poincare-Hopf|hairy ball theorem]]) or any closed orientable surface of positive Euler characteristic.

> **Corollary (Higher-dimensional version).** For any closed oriented smooth $n$-manifold $M^n$ and any tangent vector field $v$ with isolated zeros, $\sum_p\mathrm{Ind}_p(v) = \chi(M)$. The same proof structure works, with $\chi$ given by the alternating Betti-number sum.

---

# Motivation

This is the prototypical **topological-obstruction-from-zero-sum** theorem. The index of a vector field at a zero is a *local* topological invariant — how the field's direction rotates around the zero. The theorem says that summing these local invariants over *all* zeros of a vector field on a closed manifold gives a *global* topological invariant — the Euler characteristic of $M$ — which is the same for all vector fields.

The immediate consequence is the **hairy ball theorem**: $\chi(S^2) = 2 \neq 0$ forces every tangent vector field on $S^2$ to have at least one zero. You cannot comb a hairy ball flat. This is a topological obstruction, not a geometric one: it doesn't matter what metric you use or how you continuously deform the field, there must be a zero. The hairy ball theorem has applications in meteorology (there is always a point on Earth where the wind is calm), fluid dynamics (vortex shedding from spherical bodies), and physics (the magnetic field of a hairy sphere must have a singularity).

The conceptual content is that **the Euler characteristic measures, among other things, the algebraic complexity of vector-field zero structures**. A surface with $\chi = 0$ (torus) can support a non-vanishing vector field (e.g., a constant translation in the universal cover). A surface with $\chi \neq 0$ cannot. The theorem gives a clean topological criterion.

Historically, Poincaré (1885) proved the formula for surfaces in his famous "Sur les courbes définies par les équations différentielles", studying dynamical-system flows on surfaces. Hopf (1926) extended the result to higher [[Def - Dimension|dimensions]] via a careful argument using the Gauss map and degree theory. The theorem is foundational for **Morse theory** (Marston Morse, 1925–1934), where one applies it to gradient vector fields of generic smooth functions, obtaining the **Morse inequalities** as refinements.

---

# Sources and Targets

**Sources (Input Broadening).**

*Source 1: A specific vector field on a known closed surface.* Given $v$ with isolated zeros, the theorem computes $\sum\mathrm{Ind}$ for free if $\chi(M)$ is known; or computes $\chi(M)$ from the index sum if $\chi$ is unknown. **Why $B \Rightarrow A$:** Direct application. **Example problem:** On $S^2$, the field "flow toward the north pole" has indices $+1$ at the south pole (source) and $+1$ at the north pole (sink); sum $= 2 = \chi(S^2)$. Confirmed.

*Source 2: A Morse function $f : M \to \mathbb{R}$.* The gradient field $\nabla f$ has nondegenerate critical points (Morse condition: the Hessian $\nabla^2 f$ is invertible at each critical point), and the index at a critical point of Morse index $k$ is $(-1)^k$. So Poincaré–Hopf gives $\sum_p(-1)^{\mathrm{ind}_M(p)} = \chi(M)$ — the **Morse equality**. **Why $B \Rightarrow A$:** Morse functions provide vector fields with computable indices. **Example problem:** For a torus $T^2$ with a "saddle Morse function" having $1$ min, $2$ saddles, $1$ max — indices $+1, -1, -1, +1$, sum $= 0 = \chi(T^2)$. Confirmed.

*Source 3: A flow with isolated periodic orbits or fixed points.* Dynamical systems on closed surfaces have flows with fixed-point indices controlled by Poincaré–Hopf. **Why $B \Rightarrow A$:** The index sum bounds the topology of the dynamical system; if $\chi \neq 0$, fixed points must exist. **Example problem:** Any flow on $S^2$ must have a fixed point (because $\chi(S^2) = 2 \neq 0$); flows on $T^2$ can be fixed-point-free (e.g., constant translation).

**Targets (Output Amplification).**

*Target 1: Existence of vector-field zeros (the hairy ball theorem and analogues).* When $\chi(M) \neq 0$, every smooth tangent vector field has at least one zero. For $S^{2n}$, $\chi = 2$ forces zeros; for $S^{2n-1}$ ($n \geq 1$), $\chi = 0$ permits non-vanishing fields. **Application:** The hairy ball theorem and its consequences in fluid dynamics, meteorology, electromagnetism.

*Target 2: Topological invariants from any vector-field computation.* If you have *any* vector field on a closed oriented manifold and can compute its zero indices, you have computed $\chi$. This is the dual of "given $\chi$, vector fields must satisfy the index-sum constraint". **Application:** Compute $\chi$ of unfamiliar surfaces by constructing a clever vector field; this is sometimes easier than direct topological computation.

*Target 3: Morse-theoretic inequalities.* For a Morse function $f$, the alternating sum of critical-point counts $\sum_k(-1)^k c_k = \chi(M)$ (the Morse equality). The strict **Morse inequalities** $c_k \geq b_k$ (Betti number) refine this; combined, they give $\sum c_k \geq \sum b_k$, a quantitative bound on the minimum number of critical points of any Morse function on $M$. **Application:** Lower bounds on critical points, Morse-theoretic constructions of manifold decompositions.

---

# Why Is It True

The theorem is true because of a beautiful interplay between local index data and global topological structure, captured by the following picture: **every vector field's zeros can be "perturbed" without changing the index sum, and any two vector fields can be connected by a smooth deformation**. Combined, these mean $\sum\mathrm{Ind}$ is a homotopy-invariant integer attached to $M$ alone — and on a closed oriented manifold, this homotopy-invariant integer is $\chi(M)$.

**The bolded one-liner:** **the sum of vector-field indices is homotopy-invariant — because zeros can be created or destroyed only in cancelling pairs (sums of $\pm 1$) — and the homotopy invariant equals the Euler characteristic of $M$, computed for instance from the gradient field of any Morse function.**

The proof has two components:
1. **Independence of $v$.** Given two vector fields $v_0, v_1$ on $M$, consider the linear interpolation $v_t = (1-t)v_0 + tv_1$ (or any smooth homotopy). At generic $t$, $v_t$ has isolated zeros (by transversality); the sum of indices changes only when the homotopy passes through a non-generic configuration where two zeros collide and annihilate (or appear) — and such an event involves a $+1$ and $-1$ pair (by the local model of the collision). So $\sum\mathrm{Ind}(v_t)$ is constant in $t$.

2. **Computation of the invariant.** Choose a specific vector field whose indices you can compute. The cleanest choice is the **gradient field of a Morse function** $f : M \to \mathbb{R}$. For a Morse function (one whose critical points are nondegenerate), the gradient $\nabla f$ has isolated zeros at the critical points, and the index at a critical point of Morse index $k$ (the number of negative eigenvalues of the Hessian) is $(-1)^k$. The **CW-complex structure** on $M$ given by handle attachments at critical points realises $M$ as a complex with $c_k$ cells of dimension $k$, so $\chi(M) = \sum_k(-1)^kc_k = \sum_p(-1)^{\mathrm{ind}(p)} = \sum_p\mathrm{Ind}_p(\nabla f)$. This matches the invariant.

A geometric picture for surfaces in $\mathbb{R}^3$: choose the vector field $v(p) = \mathbf{e} - \langle\mathbf{e}, N(p)\rangle N(p)$ (the projection of a fixed direction $\mathbf{e}$ onto the tangent plane). Zeros are at $N^{-1}(\pm\mathbf{e})$, and indices count signed preimages of $\pm\mathbf{e}$ under the Gauss map. Sum $= 2\deg(N) = \chi(M)$ via [[Thm - The Gauss Normal Map has Degree Half the Euler Characteristic]].

---

# What Makes This Hard

The proof has two genuinely substantial parts. The **homotopy invariance of the index sum** requires a careful transversality argument: as $v$ deforms, zeros can be born and die, but only in $\pm 1$ pairs that cancel. The local model of such an event is the "fold" or "Morse" singularity in the space of vector fields, and the technical analysis of this requires the implicit function theorem and Sard-type arguments.

The **identification of the invariant with $\chi(M)$** requires either a direct Morse-function-and-CW-complex argument (relating critical points to cell counts and then to Betti numbers via the chain complex) or an alternative argument via the Gauss map (for embedded surfaces) or via the Hopf vector-field construction (for general manifolds). Each requires its own machinery.

A common confusion: the theorem says the index sum equals the *Euler characteristic*, not the *number of zeros* or the *number of regular preimages of a generic point*. The index can be any integer, not just $\pm 1$ — for a "higher-order" zero (e.g., the field $z^n\partial_z$ has index $n$ at the origin), the index counts the algebraic multiplicity. So the **algebraic** sum is locked at $\chi$, but the *number* of zeros can be anything: for a generic vector field on a surface of genus $g$, there are $|2 - 2g|$ + (extra cancelling pairs) zeros, with index sum $2 - 2g$.

The higher-dimensional Hopf version requires the **degree of the Gauss map for hypersurfaces** to be related to $\chi$, which is itself a substantial calculation.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy.** Two steps: (1) prove the index sum $\sum\mathrm{Ind}(v)$ is independent of $v$ by a homotopy argument; (2) compute the invariant via the gradient field of a Morse function, identifying it with $\chi(M)$.

**Subgoal decomposition:**

1. **Homotopy invariance of the index sum.** Given two vector fields $v_0, v_1$ with isolated zeros on $M$, construct a smooth homotopy $v_t$ that is transverse to zero on $M \times [0, 1]$ (so the zero set $\{(p, t) : v_t(p) = 0\}$ is a smooth $1$-manifold). The index sum changes only when a zero is born or dies — i.e., at a critical point of the projection to $t$. At each birth/death, the local model is a fold and contributes $+1, -1$ canceling pair. So $\sum\mathrm{Ind}(v_0) = \sum\mathrm{Ind}(v_1)$.
   - *Hint:* Use Sard's theorem to perturb the homotopy to be transverse; then analyse the resulting smooth zero curves; folds contribute paired indices.
   - *Why needed:* Establishes that $\sum\mathrm{Ind}$ depends only on $M$, not on $v$.

2. **Evaluate the invariant for a specific $v$ — the gradient of a Morse function.** For any Morse function $f$ on $M$, the gradient field $\nabla f$ has isolated zeros at critical points, and the index at a critical point of Morse index $k$ is $(-1)^k$. Hence $\sum\mathrm{Ind}(\nabla f) = \sum_p(-1)^{\mathrm{ind}_M(p)} = c_0 - c_1 + c_2 - \cdots = \chi(M)$, where $c_k$ is the number of critical points of Morse index $k$ and the last equality is the **Morse equality** $\chi(M) = \sum(-1)^k c_k$.
   - *Hint:* For a Morse function on a surface ($n = 2$), critical points are minima (index $0$), saddles (index $1$), maxima (index $2$); indices in the vector-field sense are $+1, -1, +1$ respectively. So $\sum\mathrm{Ind}(\nabla f) = \#(\text{min}) - \#(\text{saddle}) + \#(\text{max}) = \chi(M)$.
   - *Why needed:* Computes the invariant directly as $\chi(M)$.

3. **Combine.** $\sum\mathrm{Ind}(v) = \sum\mathrm{Ind}(\nabla f) = \chi(M)$ for any $v$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Index sum is locally additive and cancels in birth/death pairs
> **Statement:** If a smooth homotopy $v_t$ of vector fields has a birth/death event at $(p_0, t_0)$ — where two zeros appear or disappear as $t$ varies through $t_0$ — the indices of the appearing/disappearing pair sum to zero.
>
> **Hint:** The local model of a birth/death event near $(p_0, t_0)$ is the "fold" or "Whitney" model: $v_t(p) = (p^2 + (t - t_0), p)$ in suitable local coordinates (where $p \in \mathbb{R}^2$). For $t > t_0$, no zeros; for $t < t_0$, two zeros at $p = \pm\sqrt{t_0 - t}$ with indices $+1, -1$.
>
> **Why needed:** This is the technical fact underlying homotopy invariance.
>
> > [!note]- Full proof (sketch)
> > The local fold model has the desired indices by direct computation; the general case follows by transversality and a normal-form argument (Sard plus implicit function theorem reduces the local structure to the fold model).

> [!note]- Lemma 2: Gradient field of a Morse function has index $(-1)^{\mathrm{ind}}$ at each critical point
> **Statement:** For a smooth function $f : M \to \mathbb{R}$ with nondegenerate critical point at $p$ (Morse index = number of negative Hessian eigenvalues), the gradient field $\nabla f$ has isolated zero at $p$ with $\mathrm{Ind}_p(\nabla f) = (-1)^{\mathrm{ind}_M(p)}$.
>
> **Hint:** Linearise $\nabla f$ at $p$: $d(\nabla f)|_p = \nabla^2 f|_p$ (the Hessian, as a self-adjoint operator on $T_pM$). The Brouwer degree of the unit-vector map of a linear isomorphism $L : V \to V$ is $\mathrm{sign}\det L$. For the Hessian, $\det\nabla^2 f|_p = (-1)^{\mathrm{ind}}\cdot|\det|$ (with $\mathrm{ind}$ negative eigenvalues), so $\mathrm{sign}\det = (-1)^{\mathrm{ind}}$.
>
> **Why needed:** Provides the explicit index computation for the Morse-function gradient.
>
> > [!note]- Full proof
> > The differential $d(\nabla f)|_p$ is the Hessian $H = \nabla^2 f|_p$, a symmetric (hence self-adjoint) bilinear form on $T_pM$. By the spectral theorem, choose an orthonormal eigenbasis with eigenvalues $\lambda_1, \ldots, \lambda_n$; $\mathrm{ind}_M(p) =$ number of $\lambda_i < 0$. The determinant is $\prod\lambda_i$, with sign $(-1)^{\mathrm{ind}}$. The Brouwer degree of the unit-vector map of the linear isomorphism $H$ is $\mathrm{sign}\det H = (-1)^{\mathrm{ind}}$, hence $\mathrm{Ind}_p(\nabla f) = (-1)^{\mathrm{ind}_M(p)}$.

> [!note]- Lemma 3: Morse equality $\sum(-1)^kc_k = \chi(M)$
> **Statement:** For a Morse function $f$ on a closed manifold $M$ with $c_k$ critical points of Morse index $k$, $\sum_k(-1)^k c_k = \chi(M)$.
>
> **Hint:** Build a CW-complex structure on $M$ using the Morse function: attach a $k$-cell at each critical point of Morse index $k$ (the descending manifold of the critical point). Then $\chi(M)$ — the alternating sum of cell counts in a CW-decomposition — equals $\sum_k(-1)^kc_k$.
>
> **Why needed:** Connects the gradient-field index sum to the Euler characteristic.
>
> > [!note]- Full proof (sketch)
> > For a Morse function on a closed manifold, the descending manifolds of critical points stratify $M$ into a CW-complex with $c_k$ cells of dimension $k$ (Smale's theorem on stable manifolds, plus the Morse–Smale transversality condition for a generic gradient). The Euler characteristic of a CW-complex is the alternating sum of cell counts, $\chi(M) = \sum_k(-1)^kc_k$. Alternatively, via the **Morse chain complex** $C_*$ with $C_k$ generated by index-$k$ critical points and differential counting flow lines, $\chi(M) = \chi(C_*) = \sum(-1)^k c_k$.

---

# Formal Proof

> [!note]- Complete formal proof
> Step 0 — Setup: $M$ is closed oriented smooth $2$-manifold (or $n$-manifold for the general case); $v$ is a smooth tangent vector field on $M$ with isolated zeros.
>
> Step 1: Homotopy invariance. Let $v_0 = v$ and $v_1 = \nabla f$ for a Morse function $f$ on $M$ (which exists by perturbation arguments — Morse functions are dense in $C^\infty(M)$). Take the homotopy $v_t = (1-t)v_0 + tv_1$, and perturb it (in the space of [[Def - Homotopy|homotopies]]) to be transverse to the zero section in $TM \times [0, 1]$. By Sard's theorem, a generic perturbation is transverse, and the zero set $\{(p, t) : v_t(p) = 0\}$ is a smooth $1$-manifold in $M \times [0, 1]$ with boundary consisting of $(p, 0)$ for zeros of $v_0$ and $(p, 1)$ for zeros of $v_1$. By Lemma 1, the indices at birth/death points cancel in pairs. So $\sum\mathrm{Ind}(v_0) = \sum\mathrm{Ind}(v_1)$.
>
> Step 2: Evaluate at $v = \nabla f$. By Lemma 2, $\mathrm{Ind}_p(\nabla f) = (-1)^{\mathrm{ind}_M(p)}$ for each critical point $p$ of $f$. Summing: $\sum_p\mathrm{Ind}_p(\nabla f) = \sum_p(-1)^{\mathrm{ind}_M(p)} = \sum_k(-1)^kc_k$ where $c_k$ is the number of critical points of Morse index $k$.
>
> Step 3: Apply Lemma 3. $\sum_k(-1)^kc_k = \chi(M)$, hence $\sum\mathrm{Ind}(v) = \chi(M)$. $\square$
>
> **Alternative proof for embedded surfaces in $\mathbb{R}^3$ (via the Gauss map).** Take the vector field $v(p) = \mathbf{e} - \langle\mathbf{e}, N(p)\rangle N(p)$ for a generic unit vector $\mathbf{e} \in S^2$. By [[Thm - The Gauss Normal Map has Degree Half the Euler Characteristic]] (proved separately), $\sum\mathrm{Ind}(v) = 2\deg(N) = \chi(M)$.

---

# Cross-Field Exercise Suggestions

1. **Hairy ball theorem on $S^2$.** Use Poincaré–Hopf to conclude $S^2$ has no nowhere-vanishing tangent vector field: $\chi(S^2) = 2$, and if a nowhere-vanishing field existed, the index sum would be $0$ (no zeros, trivially), contradicting $\chi = 2$. So every continuous tangent field on $S^2$ has a zero. **Why nonobvious:** This is a topological obstruction with no analogue on $S^1$ or $T^2$ (both have $\chi = 0$ and admit nowhere-vanishing fields). See [[Ex - Hairy Ball Theorem from Poincare-Hopf]].

2. **Morse theory of the height function on the torus.** Embed the torus $T^2$ in $\mathbb{R}^3$ as a doughnut and use the height function $f(p) =$ "$z$-coordinate" as a Morse function. It has $4$ critical points: $1$ minimum (bottom), $2$ saddles (inner top and outer bottom of the doughnut hole? No — more carefully: $2$ saddles at the "shoulders" of the donut hole), $1$ maximum (top). Indices: $+1, -1, -1, +1$. Sum: $0 = \chi(T^2)$. **Why nonobvious:** The explicit picture of Morse indices on a torus is a classical illustration that builds intuition for the more general Morse theory.

3. **Vector-field index on the genus-$g$ surface.** For a closed orientable surface of genus $g$, $\chi = 2 - 2g$, so any vector field has $\sum\mathrm{Ind} = 2 - 2g$. For $g = 2$ (double torus), $\chi = -2$; one can realise this via a vector field with $2$ sinks and $4$ saddles ($+2 - 4 = -2$) or $1$ sink, $1$ source, and $4$ saddles ($+1 + 1 - 4 = -2$), etc. **Why nonobvious:** The flexibility of choices (any combination summing to $\chi$) but the rigidity of the *sum* is the substance of the theorem.

---

# Bridges

- **To **Morse theory** ([[Algebraic Topology I — Singular Homology and the de Rham Theorem]]).** The gradient-field interpretation of Poincaré–Hopf is the entry point to Morse theory: for a Morse function on a closed manifold, the alternating sum of critical-point counts is $\chi(M)$ (Morse equality), and the strict **Morse inequalities** $c_k \geq b_k(M)$ (the $k$th Betti number) provide more refined bounds. Morse theory uses the gradient flow to construct CW decompositions of $M$ from any Morse function, giving handle decompositions, the **Morse chain complex**, and the **Smale–Lefschetz** theorems on cobordism.

- **To the [[Thm - Gauss-Bonnet Theorem for Surfaces|Gauss–Bonnet theorem]].** The two theorems together say: for a closed oriented Riemannian surface, $\sum\mathrm{Ind}(v) = \chi(M) = (1/2\pi)\int K\, dA$. Three different perspectives on the same topological invariant — vector-field indices, total curvature, Euler characteristic. The cleanest way to see they all agree: the projection vector field $v(p) = \mathbf{e} - \langle\mathbf{e}, N\rangle N$ has index sum $2\deg(N)$, and $\int K\, dA = 4\pi\deg(N)$ via change of area.

- **To the **Lefschetz fixed-point theorem** ([[Algebraic Topology I — Singular Homology and the de Rham Theorem]]).** For a self-map $\phi : M \to M$ on a closed oriented manifold, the **Lefschetz number** $L(\phi) = \sum_k(-1)^k\mathrm{tr}(\phi_* : H_k \to H_k)$ equals the sum of indices of fixed points. The identity case $\phi = \mathrm{id}$ has $L(\mathrm{id}) = \chi(M)$, and Lefschetz reduces to Poincaré–Hopf. The higher-dimensional, more refined Lefschetz fixed-point counting is a generalisation of the vector-field index argument.

- **To the **Atiyah–Singer index theorem** ([[Algebraic Topology III — Higher Homotopy and Chern Forms]]).** Poincaré–Hopf is the simplest "index = topology" theorem: the analytical index (number of zeros, signed) of a vector field equals the topological index (Euler characteristic). The Atiyah–Singer index theorem generalises: for any elliptic operator, the analytical index (dim ker − dim cokernel) equals the topological index, a polynomial in characteristic classes. Poincaré–Hopf is the case of the de Rham operator (whose index is $\chi$).

- **To **dynamical systems** on surfaces.** Every smooth flow on a closed surface has fixed points whose indices sum to $\chi$. On the torus ($\chi = 0$), fixed-point-free flows exist (the **irrational flow** $\phi_t(\theta, \varphi) = (\theta + \alpha t, \varphi + \beta t)$ for $\alpha/\beta$ irrational). On the sphere ($\chi = 2$), every flow has at least one fixed point; the dynamical-systems community uses this to constrain the possible dynamics on $S^2$ (Poincaré–Bendixson theorem).

---

# Unlocked by This

> [!tip] The Hairy Ball Theorem *(from §4.4 Exercises)*
> No nowhere-vanishing continuous tangent vector field exists on $S^2$ — because $\chi(S^2) = 2 \neq 0$. Generalisations: $S^{2n}$ has $\chi = 2$, so the same conclusion; $S^{2n-1}$ has $\chi = 0$ and *does* admit nowhere-vanishing fields (e.g., the Hopf flow on $S^3$). See [[Ex - Hairy Ball Theorem from Poincare-Hopf]].

> [!tip] The Morse Inequalities *(from Algebraic Topology)*
> For a Morse function $f$ on a closed manifold, $c_k \geq b_k(M)$ where $b_k$ is the $k$th Betti number — the **strict Morse inequalities**. Combined with the Morse equality, they provide quantitative bounds on the minimum number of critical points of any Morse function. **Application:** The **Morse–Smale theorem** that every closed manifold admits a Morse function with exactly $\sum b_k$ critical points (a "perfect" Morse function) when the cohomology has no torsion.

> [!tip] The Lefschetz Fixed-Point Theorem *(from Algebraic Topology)*
> For a self-map $\phi : M \to M$ on a closed oriented manifold, the **Lefschetz number** $L(\phi) = \sum(-1)^k\mathrm{tr}(\phi_* : H_k \to H_k)$ equals the sum of fixed-point indices. If $L(\phi) \neq 0$, $\phi$ has a fixed point. Identity case: $L(\mathrm{id}) = \chi(M)$, recovering Poincaré–Hopf.

> [!tip] The Lefschetz Hyperplane Theorem and Algebraic-Geometric Generalisations *(from Algebraic Geometry)*
> For a smooth projective algebraic variety, the Euler characteristic is computable via the Chern classes of the tangent bundle. The **Lefschetz hyperplane theorem** and **Hodge–Riemann bilinear relations** are higher-codimension generalisations of the index-theoretic content of Poincaré–Hopf.

> [!tip] The Atiyah–Singer Index Theorem *(from Algebraic Topology III)*
> The grand generalisation: for any elliptic operator $D$ on a closed manifold, the analytical index $\mathrm{ind}_a(D) = \dim\ker D - \dim\mathrm{coker}\, D$ equals a topological index $\mathrm{ind}_t(D)$ computed from characteristic classes. Special cases: Poincaré–Hopf (de Rham operator), the Riemann–Roch–Hirzebruch theorem (Dolbeault operator on Kähler manifolds), the signature theorem (signature operator). Poincaré–Hopf is the cleanest, most concrete special case of one of $20$th-century mathematics' greatest theorems.
