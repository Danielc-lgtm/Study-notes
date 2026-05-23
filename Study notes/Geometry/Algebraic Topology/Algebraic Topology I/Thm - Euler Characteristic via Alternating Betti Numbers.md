---
type: theorem
subject: algebraic-topology
prereqs:
  - "Def - Betti Numbers"
  - "Def - Euler Characteristic"
  - "Def - Singular Homology"
tags: [geometry, algebraic-topology, invariants]
---

# Notation

$(C_\bullet, \partial)$ is a chain complex of finite-dimensional vector spaces over a field $K$ — that is, $C_p$ is a finite-dimensional $K$-vector space for each $p$, $\dim C_p < \infty$, and $C_p = 0$ for all but finitely many $p$.

- $Z_p = \ker(\partial : C_p \to C_{p-1})$, $B_p = \mathrm{im}(\partial : C_{p+1} \to C_p)$, $H_p = Z_p / B_p$.
- $c_p = \dim_K C_p$, $z_p = \dim_K Z_p$, $b_p = \dim_K B_p$, $h_p = \dim_K H_p$ (the "Betti number" of the complex).

For a topological space $M$ with a finite cell structure (CW complex, triangulation, etc.), $c_p$ is the number of cells/simplices in dimension $p$, and $h_p = \dim_K H_p(M; K)$.

---

# Statement

> **Theorem (Euler characteristic identity).** Let $(C_\bullet, \partial)$ be a chain complex of finite-dimensional vector spaces over a field $K$, with $C_p = 0$ for all but finitely many $p$. Then
> $$
> \sum_{p \geq 0} (-1)^p \dim_K C_p \;=\; \sum_{p \geq 0} (-1)^p \dim_K H_p(C_\bullet).
> $$
>
> The alternating sum of the chain dimensions equals the alternating sum of the homology dimensions — both equal the **Euler characteristic** $\chi$ of the chain complex.

> **Corollary (Euler characteristic of a triangulated space).** For a topological space $M$ admitting a finite triangulation $K$ with $c_p$ simplices of dimension $p$, the Euler characteristic is
> $$
> \chi(M) \;=\; \sum_p (-1)^p c_p \;=\; \sum_p (-1)^p b_p(M),
> $$
> where $b_p(M) = \dim_\mathbb{R} H_p(M; \mathbb{R})$ are the Betti numbers. In particular, $\sum (-1)^p c_p$ is a topological invariant — independent of the triangulation chosen.

> **Corollary (Euler's polyhedral formula).** For any triangulation of a closed surface $\Sigma$ with $V$ vertices, $E$ edges, $F$ faces,
> $$
> V - E + F \;=\; \chi(\Sigma) \;=\; 2 - 2g \text{ (orientable)} \text{ or } 2 - k \text{ (non-orientable with $k$ cross-caps)}.
> $$
> In particular, for $\Sigma = S^2$, $V - E + F = 2$.

The proof is a piece of linear algebra: the chain complex is a sequence of vector spaces with rank-nullity-style identities at each spot, and the alternating sums telescope to give the equality.

---

# Motivation

The Euler characteristic $\chi(M)$ is defined as $\sum (-1)^p b_p$, an alternating sum of homology dimensions. This is a topological invariant, but it is hard to compute directly: it requires knowing the homology of $M$ in every degree.

A much more practical formula computes $\chi$ from a *cell structure*: $\chi(M) = \sum (-1)^p c_p$, where $c_p$ counts the cells in dimension $p$. For a triangulation: count the vertices, subtract the edges, add the faces, and so on. For a CW structure: count the cells in each dimension with alternating signs. This is much faster than computing the full homology.

The theorem says these two computations always give the same answer. So the alternating cell count — *a priori* dependent on the triangulation — is in fact a topological invariant. This is the deepest content of the formula $V - E + F = 2$ for the sphere: not just that some specific triangulation gives $2$, but that *every* triangulation does, because the alternating cell count equals the alternating Betti number sum, which is topologically intrinsic.

The proof is essentially a piece of linear algebra: for each $p$, the rank-nullity theorem gives $\dim C_p = \dim Z_p + \dim B_{p-1}$ (the image of $\partial_p$ in $C_{p-1}$). Combined with $h_p = z_p - b_p$, the alternating sums telescope:
$$
\sum_p (-1)^p c_p = \sum_p (-1)^p (z_p + b_{p-1}) = \sum_p (-1)^p z_p + \sum_p (-1)^p b_{p-1}.
$$
The second sum re-indexes to $-\sum_p (-1)^p b_p$ (with the sign flip from the index shift), so
$$
\sum_p (-1)^p c_p = \sum_p (-1)^p (z_p - b_p) = \sum_p (-1)^p h_p.
$$
This is the identity.

The historical and pedagogical motivation: Euler observed in 1758 that for any convex polyhedron, $V - E + F = 2$. He had no general theory of homology, but he had stumbled onto a topological invariant. Poincaré, a century later, recognised that Euler's formula is the dimensional shadow of a deeper fact about the homology of $S^2$: the alternating sum of cell counts in any triangulation equals the alternating sum of homology dimensions, which for $S^2$ is $1 - 0 + 1 = 2$.

The theorem generalises to **any** alternating sum of dimensions in a chain complex, not just topological. This makes it a piece of homological algebra: any time you have an exact-sequence-of-chain-complexes structure, the Euler characteristic adds. This is why $\chi$ shows up in Riemann–Roch, the Atiyah–Singer index theorem, characteristic-class identities — all of which involve alternating sums of dimensions of vector spaces appearing in some chain complex.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition $A$ is: *a chain complex of finite-dimensional vector spaces with only finitely many non-zero terms.*

The first disguised source is **a finite simplicial complex.** Property $B$: a triangulated space $M$ with finite simplicial complex $K$. The bridge: the simplicial chain complex $C_*^{\mathrm{simp}}(K; K)$ has $\dim C_p = c_p$, the number of $p$-simplices; the simplicial homology agrees with singular homology over $K$ (by [[Thm - Singular and Simplicial Homology Agree on Triangulable Spaces]]). So $\sum (-1)^p c_p = \sum (-1)^p b_p(M) = \chi(M)$. *Example application:* compute $\chi$ of any triangulated surface by counting $V - E + F$.

The second disguised source is **a CW complex.** Property $B$: a finite CW complex with $c_p$ cells of dimension $p$. The bridge: the cellular chain complex has $\dim C_p = c_p$, and cellular homology agrees with singular. *Example application:* $\chi(\mathbb{CP}^n) = 1 + 0 + 1 + 0 + 1 + \cdots = n + 1$ (one cell in each even dimension up to $2n$).

The third disguised source is **a de Rham complex on a compact manifold.** Property $B$: the de Rham complex $(\Omega^\bullet(M), d)$ on a compact manifold (where each $\Omega^p$ is infinite-dimensional but $H^p_{dR}(M)$ is finite-dimensional). The bridge: the formula does *not* directly apply to the infinite-dimensional chain groups, but the alternating sum of *homology* dimensions still makes sense and equals $\chi(M)$ (by the topological identification). *Example application:* $\chi(M) = \sum (-1)^p \dim H^p_{dR}(M)$, computed by finding the dimensions of the de Rham groups directly.

The fourth disguised source is **a Koszul complex or any algebraic chain complex.** Property $B$: a chain complex of vector spaces arising from a commutative-algebra construction (Koszul resolution, etc.). The bridge: same identity. *Example application:* the Euler characteristic of a Koszul complex is the determinant of a Jacobian — a classical relation between algebra and geometry.

**Targets (Output Amplification)**

The conclusion $C$: *$\sum (-1)^p \dim C_p = \sum (-1)^p \dim H_p$.*

Combine $C$ with **topological invariance of homology.** The right side is determined by the topological space $M$ (or by the homotopy type, by [[Thm - Homotopy Invariance of Singular Homology|homotopy invariance]]). The further result $E$: the left side — the alternating cell count of any triangulation/CW structure of $M$ — is a topological invariant, independent of the choice of cell structure. This is the cornerstone of "Euler's formula": $V - E + F = 2$ holds for *every* triangulation of $S^2$, not just specific ones.

Combine $C$ with **inclusion-exclusion for the cell count.** For a cover $M = U \cup V$, the cells in $M$ are either in $U$ alone, in $V$ alone, or in $U \cap V$ (counted twice). The alternating sum then satisfies $\chi(M) = \chi(U) + \chi(V) - \chi(U \cap V)$ — Mayer–Vietoris for the Euler characteristic. The further result $E$: $\chi$ is an additive invariant under open covers, with the same identity as on the homology side.

Combine $C$ with **the Künneth formula.** For a product space $M \times N$, the cellular chains satisfy $C_n^{\mathrm{CW}}(M \times N) = \bigoplus_{p+q=n} C_p^{\mathrm{CW}}(M) \otimes C_q^{\mathrm{CW}}(N)$. The alternating sum then gives $\chi(M \times N) = \chi(M) \cdot \chi(N)$. The further result $E$: the Euler characteristic is multiplicative under products, both at the cellular level and (consequently) at the homology level — recovering $\chi(T^n) = \chi(S^1)^n = 0$ for $n \geq 1$.

---

# Why Is It True

**The single sentence: rank-nullity at each degree gives $\dim C_p = \dim Z_p + \dim B_{p-1}$, and combined with $\dim H_p = \dim Z_p - \dim B_p$, the alternating sums telescope to give the identity.**

The intuition is purely linear-algebraic. A chain complex is a sequence
$$
\cdots \to C_{p+1} \xrightarrow{\partial} C_p \xrightarrow{\partial} C_{p-1} \to \cdots
$$
of vector spaces. At each spot $C_p$, the rank-nullity theorem applied to $\partial : C_p \to C_{p-1}$ gives
$$
\dim C_p = \dim \ker \partial + \dim \mathrm{im}\, \partial = z_p + b_{p-1}.
$$
Here we are interpreting $b_{p-1}$ as $\dim \mathrm{im}(\partial : C_p \to C_{p-1})$ — these are the $(p-1)$-boundaries arising as $\partial$ of $p$-chains. By the definition of homology, $h_p = z_p - b_p$.

Now compute the alternating sum:
$$
\sum_p (-1)^p c_p = \sum_p (-1)^p (z_p + b_{p-1}).
$$
The $b_{p-1}$ terms shift index: $\sum_p (-1)^p b_{p-1} = -\sum_p (-1)^p b_p$ (substituting $p \to p+1$). So
$$
\sum_p (-1)^p c_p = \sum_p (-1)^p z_p - \sum_p (-1)^p b_p = \sum_p (-1)^p (z_p - b_p) = \sum_p (-1)^p h_p.
$$
Done. The proof is essentially three lines of linear algebra.

The deeper reason is that **the alternating sum of dimensions is additive under short exact sequences**: if $0 \to A \to B \to C \to 0$ is exact, then $\dim B = \dim A + \dim C$, so $-\dim A + \dim B - \dim C = 0$ — the alternating sum is zero. The chain complex's homology then "accounts for the failure of exactness," and the alternating sum of homology dimensions equals the alternating sum of chain dimensions because both equal the same total "tally."

This is the algebraic content of the Euler characteristic: it is the unique numerical invariant of chain complexes that adds under short exact sequences. The topological Euler characteristic inherits this property from the algebraic one via the chain complexes of triangulations.

---

# What Makes This Hard

The proof is short and there is nothing genuinely difficult. The most common error is to write $\dim C_p = \dim Z_p + \dim B_p$ instead of $\dim C_p = \dim Z_p + \dim B_{p-1}$ — the boundary subgroup at level $p$ is $\mathrm{im}(\partial : C_{p+1} \to C_p)$, *not* $\mathrm{im}(\partial : C_p \to C_{p-1})$. The latter (image of $\partial$ leaving $C_p$) is $B_{p-1}$, not $B_p$.

This off-by-one is the only subtlety in the proof, and it is the one that determines the sign-shifting in the alternating-sum telescoping. Getting it right gives the theorem; getting it wrong gives a non-cancellation.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Use the rank-nullity theorem at each degree of the chain complex to write $\dim C_p$ as $\dim Z_p + \dim B_{p-1}$. Substitute into the alternating sum and re-index the $B$ terms. The result telescopes to $\sum (-1)^p \dim H_p$.

**Subgoal decomposition:**

1. **Apply rank-nullity to $\partial : C_p \to C_{p-1}$.** $\dim C_p = \dim \ker \partial + \dim \mathrm{im}\, \partial$. The kernel is $Z_p$ (cycles); the image is the boundary group at level $p-1$, namely $B_{p-1} = \mathrm{im}(\partial : C_p \to C_{p-1})$.
   - *Hint:* Standard rank-nullity for a linear map between finite-dimensional vector spaces.
   - *Why needed:* Express $\dim C_p$ in terms of cycle and boundary dimensions.

2. **Substitute into the alternating sum.** $\sum (-1)^p \dim C_p = \sum (-1)^p (\dim Z_p + \dim B_{p-1})$.
   - *Hint:* Direct substitution from Step 1.
   - *Why needed:* This is the starting point of the calculation.

3. **Re-index the $B$ sum.** $\sum_p (-1)^p \dim B_{p-1} = \sum_p (-1)^{p+1} \dim B_p = -\sum_p (-1)^p \dim B_p$.
   - *Hint:* Substitute $p \to p + 1$ in the index.
   - *Why needed:* Aligns the indices to allow telescoping.

4. **Telescope.** $\sum (-1)^p \dim C_p = \sum (-1)^p \dim Z_p - \sum (-1)^p \dim B_p = \sum (-1)^p (\dim Z_p - \dim B_p) = \sum (-1)^p \dim H_p$, using $\dim H_p = \dim Z_p - \dim B_p$ from $H_p = Z_p / B_p$.
   - *Hint:* Dimension of a quotient equals the difference of dimensions.
   - *Why needed:* Final step of the identity.

---

# Lemma Decomposition

> [!note]- Lemma 1: Rank-Nullity at Each Degree
> **Statement:** For each $p$, $\dim C_p = \dim Z_p + \dim B_{p-1}$, where $Z_p = \ker(\partial : C_p \to C_{p-1})$ and $B_{p-1} = \mathrm{im}(\partial : C_p \to C_{p-1})$.
>
> **Hint:** Standard rank-nullity for the linear map $\partial : C_p \to C_{p-1}$.
>
> **Why needed:** This is the key identity that converts dimensions of chain groups into dimensions of cycle/boundary groups.
>
> > [!note]- Full proof
> > The linear map $\partial : C_p \to C_{p-1}$ has kernel $Z_p = \ker \partial$ and image $\mathrm{im}\, \partial \subseteq C_{p-1}$. The rank-nullity theorem of linear algebra says
> > $$
> > \dim C_p = \dim \ker \partial + \dim \mathrm{im}\, \partial.
> > $$
> > Now $\mathrm{im}(\partial : C_p \to C_{p-1})$ is the set of $(p-1)$-boundaries arising from $p$-chains — this is exactly $B_{p-1}$ by definition. So $\dim C_p = \dim Z_p + \dim B_{p-1}$.

> [!note]- Lemma 2: Dimension of Homology Quotient
> **Statement:** $\dim H_p = \dim Z_p - \dim B_p$, where $H_p = Z_p / B_p$.
>
> **Hint:** Dimension of a quotient vector space equals the difference of dimensions of numerator and denominator.
>
> **Why needed:** Converts between dimensions of cycles/boundaries and dimensions of homology.
>
> > [!note]- Full proof
> > $B_p$ is a subspace of $Z_p$ (by $\partial^2 = 0$). The quotient $Z_p / B_p$ is a vector space of dimension $\dim Z_p - \dim B_p$, by the standard fact that $\dim(V/W) = \dim V - \dim W$ for finite-dimensional $V$ and a subspace $W$.

> [!note]- Lemma 3: Index Shift in Alternating Sum
> **Statement:** For any sequence $\{a_p\}$ with finite support, $\sum_p (-1)^p a_{p-1} = -\sum_p (-1)^p a_p$.
>
> **Hint:** Substitute $p \to p + 1$.
>
> **Why needed:** Aligns the indices in the calculation.
>
> > [!note]- Full proof
> > Let $q = p - 1$, so $p = q + 1$. Then $\sum_p (-1)^p a_{p-1} = \sum_q (-1)^{q+1} a_q = -\sum_q (-1)^q a_q$. Renaming $q$ back to $p$ gives the identity.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** For a chain complex $(C_\bullet, \partial)$ of finite-dimensional vector spaces over a field, with $C_p = 0$ for all but finitely many $p$,
> $$
> \sum_{p \geq 0} (-1)^p \dim C_p = \sum_{p \geq 0} (-1)^p \dim H_p(C_\bullet).
> $$
>
> *Proof.*
>
> By Lemma 1, $\dim C_p = \dim Z_p + \dim B_{p-1}$ for each $p$. So
> $$
> \sum_p (-1)^p \dim C_p = \sum_p (-1)^p (\dim Z_p + \dim B_{p-1}) = \sum_p (-1)^p \dim Z_p + \sum_p (-1)^p \dim B_{p-1}.
> $$
>
> By Lemma 3, $\sum_p (-1)^p \dim B_{p-1} = -\sum_p (-1)^p \dim B_p$. Substituting,
> $$
> \sum_p (-1)^p \dim C_p = \sum_p (-1)^p \dim Z_p - \sum_p (-1)^p \dim B_p = \sum_p (-1)^p (\dim Z_p - \dim B_p).
> $$
>
> By Lemma 2, $\dim Z_p - \dim B_p = \dim H_p$. So
> $$
> \sum_p (-1)^p \dim C_p = \sum_p (-1)^p \dim H_p.
> $$
> $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Euler's formula $V - E + F = 2$ for the sphere.** For any triangulation of $S^2$, $V - E + F = \chi(S^2) = \sum (-1)^p \dim H_p(S^2; \mathbb{R}) = 1 - 0 + 1 = 2$. So every triangulation gives the same answer. Specific examples: tetrahedron ($4 - 6 + 4 = 2$), cube triangulated into $12$ triangles ($8 - 18 + 12 = 2$), octahedron ($6 - 12 + 8 = 2$).

**Genus from Euler characteristic.** For a closed orientable surface $\Sigma_g$, $\chi(\Sigma_g) = 2 - 2g$. Given a triangulation with $V, E, F$ counts, the genus is $g = (2 - V + E - F)/2$. This lets you read off the genus of any triangulated surface from elementary cell-counting.

**Multiplicativity of $\chi$ from cellular tensor products.** For finite CW complexes $X, Y$, $\chi(X \times Y) = \chi(X) \cdot \chi(Y)$. Proof: the product CW structure has cells $\{e_i \times f_j\}$ for cells $e_i$ of $X$ and $f_j$ of $Y$, with $\dim(e_i \times f_j) = \dim e_i + \dim f_j$. The alternating sum factors. Consequence: $\chi(T^n) = \chi(S^1)^n = 0^n = 0$ for $n \geq 1$.

**Inclusion-exclusion via Mayer–Vietoris.** For a cover $M = U \cup V$, $\chi(M) = \chi(U) + \chi(V) - \chi(U \cap V)$. Proof: apply the alternating-sum identity to the Mayer–Vietoris long exact sequence (which has $0$ overall Euler characteristic by exactness). Consequence: compute $\chi$ of complicated spaces by combining simpler pieces.

**$\chi$ of a connected sum.** For closed $n$-manifolds $M_1, M_2$, the connected sum $M_1 \# M_2$ has $\chi(M_1 \# M_2) = \chi(M_1) + \chi(M_2) - \chi(S^n)$. Reason: $M_1 \# M_2$ is obtained by removing an open ball from each and gluing along the boundary sphere $S^{n-1}$. By inclusion-exclusion: $\chi(M_1 \# M_2) = \chi(M_1 \setminus \mathrm{ball}) + \chi(M_2 \setminus \mathrm{ball}) - \chi(S^{n-1} \text{ collar}) = (\chi(M_1) - \chi(\text{ball})) + (\chi(M_2) - \chi(\text{ball})) - \chi(S^{n-1})$. After simplification using $\chi(\text{ball}) = 1$, $\chi(S^{n-1}) = 1 + (-1)^{n-1}$, this gives $\chi(M_1 \# M_2) = \chi(M_1) + \chi(M_2) - \chi(S^n)$.

---

# Bridges

- **[[Def - Euler Characteristic|Euler characteristic]]** — this theorem is the bridge between the homology-side definition $\chi = \sum (-1)^p b_p$ and the cell-side definition $\chi = \sum (-1)^p c_p$. Both are equal, and both are topological invariants.

- **[[Def - Betti Numbers|Betti numbers]]** — the alternating sum of Betti numbers is the Euler characteristic; the theorem says this also equals the alternating cell count.

- **[[Thm - Singular and Simplicial Homology Agree on Triangulable Spaces|Simplicial = singular homology]]** — used implicitly: the cell counts come from a simplicial triangulation, and the homology agreement ensures the cellular Euler characteristic equals the singular one.

- **The Lefschetz fixed-point formula** — the trace identity $L(f) = \sum (-1)^p \mathrm{tr}(f_* : H_p \to H_p)$ generalises the Euler characteristic to traces of non-identity maps. For $f = \mathrm{id}$, $\mathrm{tr}(\mathrm{id}_{H_p}) = \dim H_p = b_p$, so $L(\mathrm{id}) = \sum (-1)^p b_p = \chi$. The same chain-complex algebra (alternating sum of traces) underlies both.

- **The Riemann–Roch theorem** — for a divisor $D$ on a smooth projective curve $X$, $\chi(\mathcal{O}(D)) = h^0 - h^1 = \deg D + 1 - g$. The left side is an alternating sum of cohomology dimensions (Euler characteristic of a coherent sheaf); the right side is a "topological + degree" formula. The classical Riemann–Roch is a vast generalisation of the Euler characteristic identity, computing $\chi$ of more general sheaves.

- **The Atiyah–Singer index theorem** — the analytic index of an elliptic operator equals its topological index. The "analytic index" is an alternating sum of dimensions of solution spaces; the "topological index" is computed from characteristic classes. The agreement is a vast generalisation of the Euler-characteristic identity to non-trivial chain complexes (of solutions to elliptic equations).

---

# Unlocked by This

> [!tip] Topological Invariance of the Alternating Cell Count *(from this same topic)*
> The cell count $\sum (-1)^p c_p$ for any triangulation (or CW structure) of a space $M$ is a topological invariant — independent of the triangulation chosen. This is the algebraic content of "$V - E + F = 2$ for every triangulation of $S^2$."

> [!tip] **Lefschetz Fixed Point Theorem** *(from Algebraic Topology)*
> $L(f) = \sum (-1)^p \mathrm{tr}(f_* : H_p \to H_p)$ counts (with sign) the fixed points of a generic self-map $f : M \to M$. For $f = \mathrm{id}$, $L(\mathrm{id}) = \chi(M)$ — the Euler characteristic is the "fixed-point count" of the identity. The Atiyah–Bott extension generalises this to traces of more exotic operators.

> [!tip] **Riemann–Roch–Hirzebruch** *(from Algebraic Geometry)*
> For a coherent sheaf $\mathcal{F}$ on a smooth projective variety $X$, the Euler characteristic $\chi(\mathcal{F}) = \sum (-1)^p \dim H^p(X; \mathcal{F})$ is computed by a "topological + algebraic" formula involving the Chern classes of $\mathcal{F}$ and $TX$. This is the Riemann–Roch–Hirzebruch theorem — the deepest classical generalisation of the Euler characteristic identity.

> [!tip] **Atiyah–Singer Index Theorem** *(from Differential Geometry)*
> For an elliptic differential operator $D : \Gamma(E) \to \Gamma(F)$ between sections of vector bundles on a closed manifold, the **analytic index** $\dim \ker D - \dim \mathrm{coker}\, D$ equals a **topological index** computed from characteristic classes. This generalises the Euler characteristic identity in the most spectacular way — the chain complex is replaced by an elliptic complex, and the alternating sum of dimensions becomes an analytic invariant equal to a topological invariant.
