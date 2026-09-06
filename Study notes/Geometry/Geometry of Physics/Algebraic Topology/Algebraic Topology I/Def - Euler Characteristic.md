---
type: definition
subject: algebraic-topology
prereqs:
  - "Def - Betti Numbers"
  - "Def - Singular Homology"
tags: [geometry, algebraic-topology, invariants]
---

# Notation

$M$ is a topological space (typically a compact manifold or finite CW complex). $b_p(M) = \dim_\mathbb{R} H_p(M; \mathbb{R})$ are the [[Def - Betti Numbers|Betti numbers]]. $\chi(M)$ denotes the Euler characteristic.

For a finite CW complex with $c_p$ cells of dimension $p$, the **cell count** is also denoted $c_p$, and we use the same symbol $\chi(M) = \sum_p (-1)^p c_p$ for the Euler characteristic computed from cells.

---

# Axiom Motivation

The Euler characteristic is the most-used single-number topological invariant. It compresses the entire Poincaré polynomial — the list of all Betti numbers — into a single integer by the alternating-sum operation $\sum (-1)^p b_p$. This compression is dramatic (an infinite list to one number), so there must be a good reason it produces a useful invariant.

The reason is that the alternating sum is **stable under exact sequences and short exact sequences of chain complexes**. Specifically: if $0 \to A_\bullet \to B_\bullet \to C_\bullet \to 0$ is a short exact sequence of chain complexes (of finite-dimensional vector spaces in each degree), then the alternating sums of dimensions satisfy
$$
\chi(B) = \chi(A) + \chi(C).
$$
So the Euler characteristic is *additive* under chain-complex extensions. By the long exact sequence in homology, this also gives the version for short exact sequences of spaces (Mayer–Vietoris, pairs, fibrations) — making the Euler characteristic an invariant that "respects gluing." If $M = U \cup V$ with $U \cap V$ tractable, then by Mayer–Vietoris and the additivity, $\chi(M) = \chi(U) + \chi(V) - \chi(U \cap V)$ — the inclusion-exclusion formula for the Euler characteristic.

The historical motivation comes from Euler's polyhedral formula $V - E + F = 2$ for the sphere $S^2$ (and more generally $V - E + F = 2 - 2g$ for a closed orientable surface of genus $g$). The pattern is: alternate signs by dimension, sum over cells, get a topological invariant. This pre-dated the modern theory of homology by a century, but Poincaré recognised that Euler's formula is the dimensional shadow of a deeper fact:
$$
\chi(M) = \sum_p (-1)^p (\text{number of $p$-cells}) = \sum_p (-1)^p \dim H_p(M).
$$
The first equality is computable from any cell structure; the second is invariant under the cell structure chosen; the equality between them is [[Thm - Euler Characteristic via Alternating Betti Numbers]]. So $\chi$ is *the* numerical invariant that bridges combinatorics (cell counts) and topology (homology dimensions).

Why is the Euler characteristic so prominent in geometry and physics? Three reasons.

**It is computable many ways.** $\chi(M)$ can be computed from a triangulation ($V - E + F$ for surfaces), from a CW structure ($\sum (-1)^p c_p$), from singular homology ($\sum (-1)^p b_p$), from de Rham cohomology ($\sum (-1)^p \dim H^p_{dR}$), or from a Riemannian metric (Gauss–Bonnet, $\chi = (1/2\pi) \int_M K\, dA$ for closed surfaces; Chern–Gauss–Bonnet for higher dimensions). The diversity of computation methods provides robustness and makes $\chi$ a privileged invariant in any geometric setting.

**It appears in many universal formulae.** Poincaré–Hopf: $\chi(M) = \sum_{p \in \mathrm{Zero}(X)} \mathrm{ind}_p(X)$ for a smooth vector field with isolated zeros. Lefschetz fixed-point: the number of fixed points of a generic self-map $f : M \to M$ (counted with sign) is $\sum (-1)^p \mathrm{tr}(f^* : H^p \to H^p)$, which for $f = \mathrm{id}$ specializes to $\chi(M)$. Riemann–Roch: the dimensions of various sheaf cohomologies on an algebraic curve are computed by formulas involving $\chi$ and other invariants. So $\chi$ is the "generic" multiplier in fixed-point and intersection-theoretic formulae.

**It is the simplest non-trivial invariant of homotopy type.** Among all the invariants definable from cell counts, $\chi$ is the *only* one (up to scalar) that is independent of the chosen cell structure — every other linear combination of cell counts fails to be a topological invariant. This is because the alternating sum is the unique one that respects the exact-sequence identities from elementary homological algebra. So $\chi$ is "forced" by the structure of homology theory: it is the unique homotopy invariant extractable from a cell complex by a linear count.

---

# The Definition

Let $M$ be a topological space whose Betti numbers $b_p(M)$ are finite and only finitely many are non-zero (e.g. $M$ is a compact manifold or a finite CW complex). The **Euler characteristic** of $M$ is the alternating sum
$$
\chi(M) \;=\; \sum_{p \geq 0} (-1)^p b_p(M),
$$
an integer.

Equivalent computations:
- **From homology:** $\chi(M) = \sum_p (-1)^p \dim_\mathbb{R} H_p(M; \mathbb{R})$.
- **From cohomology:** $\chi(M) = \sum_p (-1)^p \dim_\mathbb{R} H^p(M; \mathbb{R})$ (same since $\dim H^p = \dim H_p$ over a field).
- **From de Rham cohomology** (when $M$ is a smooth manifold): $\chi(M) = \sum_p (-1)^p \dim_\mathbb{R} H^p_{dR}(M)$.
- **From a CW structure with $c_p$ cells of dimension $p$:** $\chi(M) = \sum_p (-1)^p c_p$ (see [[Thm - Euler Characteristic via Alternating Betti Numbers]]).
- **From a triangulation with $V$ vertices, $E$ edges, $F$ faces (for a surface)**: $\chi(M) = V - E + F$.

The Euler characteristic is a **homotopy invariant**: $\chi(M) = \chi(N)$ whenever $M \simeq N$ are homotopy equivalent. It is a **multiplicative invariant** under products: $\chi(M \times N) = \chi(M) \cdot \chi(N)$. It is an **additive invariant** under disjoint unions and finite covers, with appropriate corrections via inclusion-exclusion.

The Euler characteristic is also the value at $t = -1$ of the **Poincaré polynomial** $P_M(t) = \sum b_p t^p$:
$$
\chi(M) = P_M(-1).
$$

---

# Relate to Other Fields / Compression

The Euler characteristic is the **alternating-sum compression of the Betti numbers**, the simplest single-number invariant extractable from the homology of $M$. It is the **topological avatar of the integer "$V - E + F$"** familiar from elementary geometry of polyhedra.

In Riemannian geometry, by the [[Riemannian Geometry IV — Classical Geometry of Surfaces in R^3|Gauss–Bonnet theorem]], $\chi(M)$ equals an integral of the Gaussian curvature for a closed surface: $\chi(M) = (1/2\pi) \int_M K\, dA$. The right-hand side is a smooth-form integral; the left-hand side is a topological invariant. The theorem's deep content is that the integral (depending on the metric) equals the topological invariant (depending only on the space). This generalises to the **Chern–Gauss–Bonnet** theorem in higher dimensions, expressing $\chi(M)$ as a curvature integral for any closed oriented even-dimensional Riemannian manifold (see [[Gauge Theory II — Principal Bundles, Representations, and Bundle Classification]]).

In differential topology, the **Poincaré–Hopf theorem** identifies $\chi(M)$ as the sum of indices of zeros of any generic vector field on $M$ — see [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection]]. So $\chi$ controls the topology of vector fields: $\chi(M) \neq 0$ means *every* vector field on $M$ must have a zero somewhere. The hairy ball theorem is the special case $\chi(S^2) = 2 \neq 0$.

In dynamics and ergodic theory, $\chi$ appears in the **Lefschetz fixed-point theorem**: for $f : M \to M$ a continuous self-map, $\sum_p (-1)^p \mathrm{tr}(f^* : H^p(M; \mathbb{R}) \to H^p(M; \mathbb{R}))$ counts the (signed) fixed points of $f$ when $f$ is generic. For $f = \mathrm{id}$, this reduces to $\sum (-1)^p \dim H^p = \chi(M)$.

In algebraic geometry, the **Riemann–Roch theorem** for a divisor $D$ on a smooth projective curve $X$ involves the Euler characteristic of the line bundle $\mathcal{O}(D)$: $\chi(\mathcal{O}(D)) = \deg(D) + 1 - g$, where $g$ is the genus. The arithmetic Riemann–Roch and Hirzebruch–Riemann–Roch generalise this to higher dimensions and other coefficient sheaves.

In statistical mechanics, the Euler characteristic of a configuration space encodes integrability and complexity of dynamical systems (Morse theory, persistence in TDA).

**True name:** the Euler characteristic is the **alternating cell count**, equivalently the **alternating Betti number sum**, equivalently **$P_M(-1)$**. It is the simplest topological invariant extractable from any cell complex by linear counting.

---

# Examples / Corollaries

**$\chi(S^n)$.** From Betti numbers $b_0 = 1$, $b_n = 1$ (others zero): $\chi(S^n) = 1 + (-1)^n$. So $\chi(S^n) = 2$ for $n$ even and $\chi(S^n) = 0$ for $n$ odd. The classical formula $\chi(S^2) = 2$ matches the polyhedral $V - E + F = 2$ for the boundary of a tetrahedron: $4 - 6 + 4 = 2$.

**$\chi(T^n)$.** From Betti numbers $b_k(T^n) = \binom{n}{k}$: $\chi(T^n) = \sum_k (-1)^k \binom{n}{k} = (1 - 1)^n = 0$ for $n \geq 1$. The torus and its higher-dimensional analogues all have Euler characteristic zero.

**$\chi(\mathbb{CP}^n)$.** From Betti numbers $b_{2k}(\mathbb{CP}^n) = 1$ for $0 \leq k \leq n$, all odd $b$ zero: $\chi(\mathbb{CP}^n) = \sum_{k=0}^n 1 = n + 1$. So $\chi(\mathbb{CP}^1) = 2$ (consistent with $\mathbb{CP}^1 = S^2$), $\chi(\mathbb{CP}^2) = 3$, $\chi(\mathbb{CP}^3) = 4$, and so on.

**$\chi(\mathbb{RP}^n)$.** With $\mathbb{R}$ coefficients, $b_0 = 1$, $b_n = 1$ if $n$ odd (else zero), all other $b$ zero. So $\chi(\mathbb{RP}^n) = 1 + (-1)^n$ when $n$ is odd, equals $0$. For $n$ even, $\chi(\mathbb{RP}^n) = 1$. Reconciled by the universal coefficient theorem: $\mathbb{RP}^n$ has lots of $\mathbb{Z}/2$ torsion in integer homology, which the Betti numbers don't see.

**$\chi(\Sigma_g) = 2 - 2g$.** A closed orientable surface of genus $g$ has Betti numbers $(1, 2g, 1)$, giving $\chi = 1 - 2g + 1 = 2 - 2g$. So $\chi(\Sigma_0) = \chi(S^2) = 2$, $\chi(\Sigma_1) = \chi(T^2) = 0$, $\chi(\Sigma_2) = -2$, and $\chi$ decreases linearly with genus.

**$\chi(K^2) = 0$ for the Klein bottle.** With $\mathbb{R}$ coefficients, $H_0 = \mathbb{R}$, $H_1 = \mathbb{R}$, $H_2 = 0$ (Frankel formula 13.26), so $\chi(K^2) = 1 - 1 + 0 = 0$. Same as the torus, even though the Klein bottle is non-orientable.

**Is NOT an instance: an arbitrary integer is the Euler characteristic of *every* manifold.** Different manifolds have wildly different Euler characteristics. For closed orientable surfaces, $\chi = 2 - 2g$ takes only the values $2, 0, -2, -4, \dots$. For closed non-orientable surfaces, $\chi = 2 - k$ where $k$ is the number of cross-caps, taking values $1, 0, -1, -2, \dots$. Not every integer arises from every manifold dimension — Euler characteristic comes with structural constraints.

**Corollary (multiplicativity).** $\chi(M \times N) = \chi(M) \cdot \chi(N)$. By the Künneth formula, $P_{M \times N}(t) = P_M(t) \cdot P_N(t)$; evaluating at $t = -1$ gives $\chi(M \times N) = P_M(-1) \cdot P_N(-1)$. Consequence: $\chi(S^2 \times S^2) = 2 \cdot 2 = 4$; $\chi(T^n) = 0^n = 0$ for $n \geq 1$.

**Corollary (Inclusion-exclusion via Mayer–Vietoris).** For an open cover $M = U \cup V$ with all spaces having finite Betti numbers, $\chi(M) = \chi(U) + \chi(V) - \chi(U \cap V)$. This is the alternating-sum identity applied to the long exact sequence of Mayer–Vietoris.

**Corollary (Euler characteristic vanishes for closed odd-dimensional orientable manifolds).** For a closed oriented $n$-manifold with $n$ odd, Poincaré duality gives $b_p = b_{n-p}$, and the alternating sum $\chi = \sum (-1)^p b_p = \sum (-1)^{n-p} b_p = -\chi$ forces $\chi = 0$. So $\chi(S^{2k+1}) = 0$, $\chi$ of any odd-dimensional closed orientable manifold is zero — and Gauss–Bonnet's "curvature integral" formula trivially gives zero.

**Corollary (Hairy ball theorem).** Since $\chi(S^2) = 2 \neq 0$, every continuous vector field on $S^2$ has at least one zero — the Poincaré–Hopf theorem says the sum of indices of zeros equals $\chi$, so there must be zeros if $\chi \neq 0$. In particular: "you cannot comb a hairy ball flat without a cowlick."

**Calibration check.** If you understand the definition you should be able to: (1) compute $\chi(M)$ for $M = T^2 \# T^2$ (a closed surface of genus $2$, the connect sum of two tori) using the Betti numbers; (2) verify $\chi(S^2 \times T^2) = 2 \cdot 0 = 0$ by Künneth; (3) explain why $\chi$ of a finite simplicial complex is well-defined (depends only on the underlying space, not the chosen triangulation) — this is essentially [[Thm - Euler Characteristic via Alternating Betti Numbers]].

---

# Unlocked by This

> [!tip] Gauss–Bonnet Theorem *(from Riemannian Geometry)*
> For a closed oriented Riemannian surface $M$, $\chi(M) = (1/2\pi) \int_M K\, dA$, where $K$ is the Gaussian curvature and $dA$ the area form. This is the **Gauss–Bonnet theorem** — a topological invariant equals a metric-dependent integral, and the equality is the deep content. See [[Riemannian Geometry IV — Classical Geometry of Surfaces in R^3]] for the surface case and [[Gauge Theory II — Principal Bundles, Representations, and Bundle Classification]] for the Chern generalisation.

> [!tip] Poincaré–Hopf Theorem *(from Differential Topology)*
> For a smooth vector field $X$ on a closed manifold $M$ with finitely many zeros $p_1, \dots, p_k$, $\chi(M) = \sum_{i=1}^k \mathrm{ind}_{p_i}(X)$, where $\mathrm{ind}_{p_i}(X)$ is the local index (winding number) of $X$ at $p_i$. So $\chi(M) \neq 0$ forces every vector field to have a zero. The hairy ball theorem is the case $M = S^2$, $\chi(S^2) = 2$. See [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection]].

> [!tip] **Lefschetz Fixed Point Theorem** *(from Algebraic Topology)*
> For a continuous self-map $f : M \to M$ of a compact space, the **Lefschetz number** $L(f) = \sum_p (-1)^p \mathrm{tr}(f_* : H_p(M; \mathbb{Q}) \to H_p(M; \mathbb{Q}))$ counts (with sign) the fixed points of $f$ when $f$ is sufficiently generic. For $f = \mathrm{id}$, $L(\mathrm{id}) = \chi(M)$ — so $\chi$ is the "fixed point count" of the identity. This is the prototype of the **Atiyah–Bott fixed point formula** and **Riemann–Roch–Hirzebruch** in algebraic geometry.

> [!tip] **Riemann–Roch and the Arithmetic Genus** *(from Algebraic Geometry)*
> For a smooth complex projective curve $X$ of genus $g$ and a divisor $D$ on $X$, the Riemann–Roch theorem expresses the dimensions of the cohomologies $H^0(\mathcal{O}(D))$ and $H^1(\mathcal{O}(D))$ as $h^0 - h^1 = \deg D + 1 - g = \chi(\mathcal{O}(D))$. So the Euler characteristic of the line bundle $\mathcal{O}(D)$ is a topological+geometric invariant. Hirzebruch–Riemann–Roch generalises this to higher-dimensional varieties and other coherent sheaves.

> [!tip] **Morse Theory and the Morse Inequalities** *(from Differential Topology)*
> For a Morse function $f : M \to \mathbb{R}$ with $m_p$ critical points of index $p$, the **Morse inequalities** assert $m_p \geq b_p(M)$ for all $p$, and the strong form $\sum (-1)^p m_p \geq \sum (-1)^p b_p = \chi(M)$ with equality for "perfect" Morse functions. The Euler characteristic is the topological lower bound on the alternating sum of critical-point counts of any smooth function.

> [!tip] **The Euler Class of a Vector Bundle** *(from Differential Topology / Characteristic Classes)*
> For a real oriented rank-$n$ vector bundle $E \to M$, the **Euler class** $e(E) \in H^n(M; \mathbb{Z})$ is a characteristic class whose integral over $M$ (when $M$ is a closed oriented $n$-manifold) equals the signed zero count of a generic section. For $E = TM$ the tangent bundle, $\int_M e(TM) = \chi(M)$ — recovering Poincaré–Hopf in the language of characteristic classes. See [[Gauge Theory II — Principal Bundles, Representations, and Bundle Classification]].
