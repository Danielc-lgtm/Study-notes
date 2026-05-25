---
type: theorem
subject: algebraic-topology
prereqs:
  - "Def - Singular Homology"
  - "Def - The Standard p-Simplex"
tags: [geometry, algebraic-topology, simplicial]
---

# Notation

$M$ is a topological space admitting a finite **simplicial triangulation** $K$ — a finite simplicial complex whose geometric realisation $|K|$ is homeomorphic to $M$. The simplicial complex $K$ has a finite set of vertices and a collection of simplices (subsets of vertices) satisfying the "downward closed" property: any face of a simplex is also a simplex.

- $C_p^{\mathrm{simp}}(K; G)$ — the **simplicial $p$-chain group**: the free $G$-module on the set of $p$-simplices of $K$ (just the explicit simplices in the triangulation, not all continuous maps).
- $\partial^{\mathrm{simp}} : C_p^{\mathrm{simp}}(K; G) \to C_{p-1}^{\mathrm{simp}}(K; G)$ — the simplicial boundary, defined on each $p$-simplex as the alternating sum of its codimension-$1$ faces.
- $H_p^{\mathrm{simp}}(K; G) = \ker \partial^{\mathrm{simp}} / \mathrm{im}\, \partial^{\mathrm{simp}}$ — the **simplicial homology** of $K$.
- $C_p(M; G)$, $H_p(M; G)$ — the [[Def - Singular Homology|singular homology]] of $M$.

The natural inclusion $\iota : C_p^{\mathrm{simp}}(K; G) \to C_p(M; G)$ sends a $p$-simplex of $K$ to itself viewed as a singular $p$-simplex (a continuous map from $\Delta^p$ to $M$).

---

# Statement

> **Theorem (Equivalence of Simplicial and Singular Homology).** Let $K$ be a finite simplicial complex with geometric realisation $|K| = M$. For every $p \geq 0$ and every abelian coefficient group $G$, the inclusion $\iota : C_p^{\mathrm{simp}}(K; G) \to C_p(M; G)$ induces an isomorphism on homology:
> $$
> \iota_* : H_p^{\mathrm{simp}}(K; G) \xrightarrow{\cong} H_p(M; G).
> $$

> **Corollary (Finite-generation of singular homology of triangulable spaces).** If $M$ admits a finite triangulation, then $H_p(M; G)$ is finitely generated for every $G$, and in particular has finite rank as a $G$-module when $G = \mathbb{Z}$ — making the Betti numbers and Euler characteristic finite.

> **Corollary (Computability).** $H_p(M; G)$ for a triangulable $M$ is computable from a triangulation by linear algebra: write the boundary maps as matrices in the basis of simplices, compute kernels and images by Gaussian elimination.

The proof uses an inductive argument on the skeletons of $K$, applying [[Thm - Mayer-Vietoris for Singular Homology|Mayer–Vietoris]] (or, equivalently, the long exact sequence of a pair) at each step.

---

# Motivation

Singular homology is conceptually clean — defined for any topological space, intrinsically functorial, satisfying all the Eilenberg–Steenrod axioms. But it is computationally a nightmare: the chain group $C_p(M; G)$ is uncountable (free on uncountably many singular simplices), and there is no obvious basis. How is one supposed to actually *compute* a singular homology group?

The answer is: replace the singular chain complex by something smaller, with the same homology. Simplicial homology — defined from a finite triangulation — does exactly this. The simplicial chain group $C_p^{\mathrm{simp}}(K; G)$ has one generator per $p$-simplex in $K$, hence is finitely generated. The boundary maps are explicit matrices, and computing the homology becomes a finite linear-algebra problem.

The equivalence theorem says: when $M$ admits a triangulation, the simplicial homology computes the singular homology. So all the computational machinery for simplicial homology (matrix-based Gaussian elimination, etc.) gives the right singular-homology answer. This is the bridge between the conceptually clean singular theory and the explicitly computable simplicial theory.

The deeper content is **invariance**: simplicial homology of $K$ is shown to be a topological invariant (i.e. independent of the specific triangulation chosen). Without the agreement with singular homology, simplicial homology would depend on the triangulation. The theorem says they don't — refining a triangulation, or choosing a different triangulation, gives the same simplicial homology, because both agree with the singular homology, which is intrinsic to the space.

Historically, the theorem was the first major result of algebraic topology (Poincaré, 1895; Alexander, 1915). It showed that the combinatorial invariants of a triangulation are actually invariants of the underlying topological space — making homology a genuine topological theory rather than a combinatorial one.

The same logic applies to **CW complexes** and **cellular homology**. Every topological space admitting a CW structure (which includes all smooth manifolds and all simplicial complexes) has its singular homology computable from the cellular chain complex — one generator per cell, with boundary maps determined by incidence numbers. Cellular homology is vastly more efficient than simplicial homology for spaces like $\mathbb{CP}^n$ that have a minimal CW structure with one cell per even dimension.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition $A$ is: *$M$ admits a finite simplicial triangulation $K$.*

The first disguised source is **a smooth manifold of finite type.** Property $B$: $M$ is a compact smooth manifold. The bridge: every smooth manifold admits a smooth triangulation (Whitehead, Whitney). So compact smooth manifolds are triangulable, and the theorem applies. *Example application:* singular homology of $T^n$ is finitely generated and computable from the standard cube-triangulation.

The second disguised source is **a finite CW complex.** Property $B$: $M$ has a finite CW structure. Every finite CW complex admits a triangulation (refining the CW structure to subdivisions of cells gives a simplicial complex). The bridge: triangulability + the theorem. *Example application:* $\mathbb{CP}^n$ has a finite CW structure with $n + 1$ even-dimensional cells; refining to a triangulation and applying the theorem (or using cellular homology directly) computes $H_*(\mathbb{CP}^n)$.

The third disguised source is **a polyhedron in Euclidean space.** Property $B$: $M$ is the underlying space of a finite polyhedron — vertices, edges, faces, glued together. Polyhedra are by definition simplicial complexes (or refinements thereof), so the theorem applies directly. *Example application:* the boundary of a $5$-simplex is a triangulation of $S^4$; the boundary of a hypercube is a polyhedral but non-simplicial structure that can be refined to a triangulation.

**Targets (Output Amplification)**

The conclusion $C$: *$H_p^{\mathrm{simp}}(K; G) \cong H_p(M; G)$ via the natural inclusion.*

Combine $C$ with **finite-dimensional linear algebra.** If $G = K$ is a field, then $C_p^{\mathrm{simp}}(K; K)$ is a finite-dimensional $K$-vector space, and the boundary maps are linear transformations. The further result $E$: $H_p^{\mathrm{simp}}(K; K)$ can be computed by Gaussian elimination — finding the kernel and image of each $\partial$. This is the standard algorithmic method for computing the singular homology of a triangulated space.

Combine $C$ with **the Euler characteristic identity.** $\chi(M) = \sum_p (-1)^p \dim H_p(M; K)$ by [[Thm - Euler Characteristic via Alternating Betti Numbers]], and on the other side $\chi^{\mathrm{simp}}(K) = \sum_p (-1)^p (\text{number of }p\text{-simplices})$. By the agreement of homologies and the alternating-sum identity, these two expressions are equal: $\chi(M) = \sum (-1)^p (\text{number of }p\text{-simplices in any triangulation})$. The further result $E$: the alternating cell-count is a topological invariant — independent of the triangulation chosen. This is Euler's polyhedral formula $V - E + F = 2$ for the sphere generalised.

Combine $C$ with **the Eilenberg–Steenrod uniqueness theorem.** Any cohomology theory satisfying the Eilenberg–Steenrod axioms agrees with singular cohomology on CW complexes. Simplicial cohomology — defined as the dual of simplicial homology — satisfies the axioms (homotopy invariance via simplicial approximation, etc.). The further result $E$: every "ordinary" homology/cohomology theory on simplicial complexes agrees with the singular theory.

---

# Why Is It True

**The single sentence: simplicial chains form a sub-complex of singular chains, and an inductive argument on the skeletons (via Mayer–Vietoris or the pair sequence) shows the inclusion is a chain-homotopy equivalence — equivalently, every singular cycle is homologous to a simplicial one.**

The intuition is twofold.

**First, every simplicial chain is a singular chain.** A $p$-simplex $\sigma$ in $K$ is literally a continuous map $\sigma : \Delta^p \to |K| = M$ (the natural inclusion of $\sigma$ as an embedded simplex in $M$). So $C_p^{\mathrm{simp}}(K; G) \subseteq C_p(M; G)$, and the inclusion is a chain map.

**Second, every singular chain is homologous to a simplicial one.** This is the non-trivial direction. Given a singular $p$-cycle $c$ in $M$, we want to find a simplicial $p$-cycle $c'$ in $K$ with $[c] = [c']$ in $H_p(M; G)$. The strategy uses **simplicial approximation**: every continuous map from a simplex to $M$ can be replaced (up to chain homotopy) by a map that is simplicial — i.e. linear on each subsimplex of a suitable subdivision. The chain homotopy preserves the cycle's homology class.

The formal proof proceeds by induction on the skeletons. Let $K^k$ be the $k$-skeleton of $K$ (the union of all simplices of dimension $\leq k$). We prove that $H_p^{\mathrm{simp}}(K^k; G) \cong H_p(K^k; G)$ for each $k$, by induction on $k$.

**Base case ($k = 0$):** $K^0$ is a finite set of points. Both simplicial and singular homology give $G$ in degree zero (one copy per point) and zero elsewhere. The inclusion is the identity.

**Inductive step ($k - 1 \to k$):** $K^k$ is obtained from $K^{k-1}$ by attaching $k$-dimensional simplices. Each attachment is a "cone over the boundary," and the long exact sequence of the pair $(K^k, K^{k-1})$ — in both simplicial and singular homology — has identical structure (the connecting maps match up to chain homotopy). By the five lemma, the simplicial-to-singular comparison map is an isomorphism on $K^k$ when it is an isomorphism on $K^{k-1}$ and on the relative pair.

The relative pair $H_*(K^k, K^{k-1})$ in simplicial homology is just the direct sum of $H_*$ of all the $k$-disks attached (each $\cong G$ in degree $k$, zero elsewhere). The singular relative homology gives the same answer (by excision and the explicit computation of $H_*$ of a disk modulo its boundary). So the relative pair contributes the same on both sides, and the inductive step succeeds.

After $\dim K$ steps, we have $K = K^{\dim K}$, and the isomorphism is established on all of $K$.

---

# What Makes This Hard

The technical heart of the proof is **simplicial approximation**: given a continuous singular simplex $\sigma : \Delta^p \to M$, after sufficiently fine subdivision of $\Delta^p$, $\sigma$ is homotopic (relative to the boundary) to a map that sends each subsimplex linearly to a face of $K$. This requires the continuity of $\sigma$ plus a Lebesgue-number argument on the cover of $M$ by the open stars of vertices of $K$.

The most common error is to assume that the simplicial homology depends on the triangulation chosen, leading to the (incorrect) belief that we need to compare two simplicial homologies (for two triangulations) and show they agree. The theorem bypasses this by going through singular homology — singular is *intrinsically* invariant, so by the theorem, simplicial homology is too.

A subtle conceptual point: the theorem applies only to *triangulable* spaces — those admitting a simplicial complex structure. Not every topological space is triangulable; spaces with "wild" embeddings (like Antoine's necklace) may not admit any simplicial triangulation. For non-triangulable spaces, the singular theory works but the simplicial theory does not.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Show the inclusion $\iota : C_p^{\mathrm{simp}}(K) \to C_p(M)$ is a chain map. Prove by induction on the dimension of the skeleton $K^k$ that the induced map $\iota_* : H_p^{\mathrm{simp}}(K^k) \to H_p(K^k)$ is an isomorphism. The inductive step uses the long exact sequence of the pair $(K^k, K^{k-1})$ in both theories, plus the five lemma.

**Subgoal decomposition:**

1. **Establish the inclusion as a chain map.** The map $\iota$ sends each $p$-simplex of $K$ (viewed as a continuous map $\Delta^p \to M$) to itself as a singular $p$-simplex. Verify $\iota \circ \partial^{\mathrm{simp}} = \partial \circ \iota$.
   - *Hint:* Both boundaries are alternating sums of face restrictions; they agree by direct comparison.
   - *Why needed:* This gives the candidate comparison map on homology.

2. **Base case (skeleton dimension $0$).** $K^0$ is a finite set of points. $H_0^{\mathrm{simp}}(K^0) = G^{|K^0|}$ (one $G$ per point) = $H_0(K^0)$ (same). Higher degrees vanish in both. $\iota_*$ is the identity on $G^{|K^0|}$, an isomorphism.
   - *Hint:* Direct computation; both theories agree on a discrete set.
   - *Why needed:* Base case.

3. **Long exact sequence of the pair.** For the pair $(K^k, K^{k-1})$, both simplicial and singular homology give long exact sequences relating $H_*(K^{k-1})$, $H_*(K^k)$, and $H_*(K^k, K^{k-1})$. The inclusion $\iota$ gives a commutative ladder of these two exact sequences (naturality of the pair sequence).
   - *Hint:* Standard pair sequence for both simplicial and singular homology.
   - *Why needed:* Sets up the five-lemma argument.

4. **Simplicial relative homology.** $H_p^{\mathrm{simp}}(K^k, K^{k-1}; G)$ is $G^{c_k}$ in degree $k$ (one $G$ per $k$-cell) and zero elsewhere, where $c_k$ is the number of $k$-simplices.
   - *Hint:* The quotient chain complex $C_*^{\mathrm{simp}}(K^k) / C_*^{\mathrm{simp}}(K^{k-1})$ has only $k$-simplices left, with no boundaries.
   - *Why needed:* Computes the relative simplicial homology.

5. **Singular relative homology agrees.** $H_p(K^k, K^{k-1}; G) \cong H_p^{\mathrm{simp}}(K^k, K^{k-1}; G)$ — also $G^{c_k}$ in degree $k$ and zero elsewhere. This uses **excision** to reduce to the wedge of $k$-disks attached, and the explicit computation of $H_*(D^k, S^{k-1}) = H_*(S^k)$ shifted.
   - *Hint:* Excision says $H_*(K^k, K^{k-1}) = \bigoplus_\alpha H_*(D^k_\alpha, \partial D^k_\alpha) = \bigoplus_\alpha G[\delta_{pk}]$.
   - *Why needed:* Shows the relative homologies match on both sides.

6. **Inductive step via five lemma.** Assume $\iota_*$ is an isomorphism on $K^{k-1}$. By Steps 4 and 5, the relative pair has matching homology. By the long exact sequence in both theories (Step 3) and the commutative ladder, by the **five lemma**, $\iota_*$ is an isomorphism on $K^k$.
   - *Hint:* Standard five-lemma argument applied to the comparison of pair sequences.
   - *Why needed:* This is the inductive step.

7. **Iterate to $K = K^{\dim K}$.** After $\dim K$ steps, $\iota_*$ is an isomorphism on $K = K^{\dim K}$, completing the proof.
   - *Hint:* Finiteness of $K$ ensures only finitely many steps.
   - *Why needed:* Completes the proof.

---

# Lemma Decomposition

> [!note]- Lemma 1: Simplicial Relative Homology of a Skeleton Step
> **Statement:** For a simplicial complex $K$ with $k$-skeleton $K^k$, $H_p^{\mathrm{simp}}(K^k, K^{k-1}; G) = G^{c_k}$ for $p = k$ and zero otherwise, where $c_k$ is the number of $k$-simplices in $K$.
>
> **Hint:** The quotient chain complex $C_*^{\mathrm{simp}}(K^k) / C_*^{\mathrm{simp}}(K^{k-1})$ has $C_k^{\mathrm{simp}}/C_k^{\mathrm{simp}}(K^{k-1}) = G^{c_k}$ in degree $k$ (one generator per $k$-simplex not in $K^{k-1}$) and zero in all other degrees. The boundary maps to and from degree $k$ in the quotient are zero (the boundary of a $k$-simplex lands in $C_{k-1}^{\mathrm{simp}}(K^{k-1})$, which is zero in the quotient; nothing maps to $C_k^{\mathrm{simp}}/C_k^{\mathrm{simp}}(K^{k-1})$ except via the zero map from $C_{k+1}^{\mathrm{simp}}(K^k) = C_{k+1}^{\mathrm{simp}}(K^{k-1}) = 0$).
>
> **Why needed:** Computes the simplicial relative homology, the left side of the comparison.
>
> > [!note]- Full proof
> > The simplicial chain complex of the pair $(K^k, K^{k-1})$ is the quotient
> > $$
> > C_p^{\mathrm{simp}}(K^k) / C_p^{\mathrm{simp}}(K^{k-1}).
> > $$
> > For $p < k$: $C_p^{\mathrm{simp}}(K^k) = C_p^{\mathrm{simp}}(K^{k-1})$ (no new simplices in dimension $< k$ since $K^k$ adds only $k$-simplices). So the quotient is zero.
> >
> > For $p = k$: $C_k^{\mathrm{simp}}(K^{k-1}) = 0$ (no $k$-simplices in the $(k-1)$-skeleton). So the quotient is $C_k^{\mathrm{simp}}(K^k) = G^{c_k}$.
> >
> > For $p > k$: $C_p^{\mathrm{simp}}(K^k) = 0$ (no simplices of dimension $> k$ in $K^k$). So the quotient is zero.
> >
> > Boundary maps in the quotient: $\partial^{\mathrm{simp}} : C_k^{\mathrm{simp}}(K^k) / C_k^{\mathrm{simp}}(K^{k-1}) \to C_{k-1}^{\mathrm{simp}}(K^k) / C_{k-1}^{\mathrm{simp}}(K^{k-1})$. The target is zero (since $C_{k-1}^{\mathrm{simp}}(K^k) = C_{k-1}^{\mathrm{simp}}(K^{k-1})$). So $\partial^{\mathrm{simp}}$ is zero.
> >
> > Homology: $H_k^{\mathrm{simp}}(K^k, K^{k-1}) = G^{c_k}$; all other degrees zero.

> [!note]- Lemma 2: Singular Relative Homology of a Skeleton Step
> **Statement:** $H_p(K^k, K^{k-1}; G) = G^{c_k}$ for $p = k$ and zero otherwise.
>
> **Hint:** Use **excision** to identify $H_p(K^k, K^{k-1}) \cong H_p(\bigsqcup_\alpha D^k_\alpha, \bigsqcup_\alpha \partial D^k_\alpha) = \bigoplus_\alpha H_p(D^k, S^{k-1})$. Compute $H_p(D^k, S^{k-1}) = \tilde H_{p-1}(S^{k-1}) = G$ for $p = k$ and zero otherwise.
>
> **Why needed:** Computes the singular relative homology, the right side of the comparison.
>
> > [!note]- Sketch
> > By excision, removing the interior of $K^{k-1}$ from both $K^k$ and $K^{k-1}$ leaves $K^k \setminus \mathrm{int}(K^{k-1}) = \bigsqcup_\alpha \overline{D^k_\alpha}$ (the union of the closed $k$-disks attached, with their boundaries identified appropriately). The pair $(K^k \setminus \mathrm{int}(K^{k-1}), K^k \setminus K^{k-1}) = (\bigsqcup_\alpha \overline{D^k_\alpha}, \bigsqcup_\alpha \partial D^k_\alpha)$ has the same relative homology as $(K^k, K^{k-1})$ by excision.
> >
> > Then $H_*(\bigsqcup_\alpha D^k, \bigsqcup_\alpha S^{k-1}) = \bigoplus_\alpha H_*(D^k, S^{k-1})$ by additivity.
> >
> > For each piece: the long exact sequence of $(D^k, S^{k-1})$ gives $H_*(D^k, S^{k-1}) = \tilde H_{*-1}(S^{k-1})$ by the contractibility of $D^k$. By [[Thm - Singular Homology of the Sphere]], $\tilde H_{p-1}(S^{k-1}) = G$ for $p - 1 = k - 1$ (i.e. $p = k$) and zero otherwise.
> >
> > So $H_p(K^k, K^{k-1}; G) = G^{c_k}$ for $p = k$, zero otherwise — matching the simplicial computation.

> [!note]- Lemma 3: Five Lemma Application
> **Statement:** In a commutative diagram of long exact sequences with four out of five vertical maps being isomorphisms, the fifth is also an isomorphism.
>
> **Hint:** Standard fact of homological algebra. Apply to the comparison of simplicial and singular pair sequences for $(K^k, K^{k-1})$.
>
> **Why needed:** This is the inductive engine.
>
> > [!note]- Sketch
> > See any homological algebra textbook (Hatcher Ch 2, Weibel Ch 1). The five lemma is a diagram chase: given commuting squares $A \to B \to C \to D \to E$ horizontally (top row) and similarly $A' \to B' \to C' \to D' \to E'$ (bottom row), with vertical maps $f_A, f_B, f_C, f_D, f_E$ and rows exact, if $f_A, f_B, f_D, f_E$ are isomorphisms, then $f_C$ is also an isomorphism.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** For a finite simplicial complex $K$ with geometric realisation $|K| = M$, $\iota_* : H_p^{\mathrm{simp}}(K; G) \to H_p(M; G)$ is an isomorphism for every $p$ and every abelian group $G$.
>
> *Proof.* By induction on the dimension of $K$.
>
> **Base case ($\dim K = 0$).** $K = K^0$ is a finite set of points. $H_0^{\mathrm{simp}}(K) = G^{|K|}$, $H_p^{\mathrm{simp}}(K) = 0$ for $p \geq 1$. Same for singular: $H_0(M) = G^{|K|}$ (component count), $H_p(M) = 0$ for $p \geq 1$ (discrete set). The inclusion $\iota_*$ in degree $0$ is the identity $G^{|K|} \to G^{|K|}$, an isomorphism.
>
> **Inductive step.** Assume the theorem for all simplicial complexes of dimension $< n$. Let $K$ have dimension $n$, so $K = K^n = K^{n-1} \cup (n\text{-cells})$.
>
> By the inductive hypothesis, $\iota_*$ is an isomorphism on $K^{n-1}$ in every degree.
>
> By Lemmas 1 and 2, $H_p^{\mathrm{simp}}(K^n, K^{n-1}) = H_p(K^n, K^{n-1}) = G^{c_n}$ for $p = n$ and zero otherwise. The natural map $\iota_*$ between these is an isomorphism (both are $G^{c_n}$ with the obvious basis — one $G$ per $n$-cell — and $\iota$ preserves this basis).
>
> The simplicial pair sequence and the singular pair sequence for $(K^n, K^{n-1})$ are both long exact:
> $$
> \cdots \to H_p^{\mathrm{simp}}(K^{n-1}) \to H_p^{\mathrm{simp}}(K^n) \to H_p^{\mathrm{simp}}(K^n, K^{n-1}) \to H_{p-1}^{\mathrm{simp}}(K^{n-1}) \to \cdots
> $$
> $$
> \cdots \to H_p(K^{n-1}) \to H_p(K^n) \to H_p(K^n, K^{n-1}) \to H_{p-1}(K^{n-1}) \to \cdots
> $$
> Naturality of $\iota_*$ with respect to inclusions gives a commutative ladder between them.
>
> By the inductive hypothesis, the maps $H_p^{\mathrm{simp}}(K^{n-1}) \to H_p(K^{n-1})$ and $H_{p-1}^{\mathrm{simp}}(K^{n-1}) \to H_{p-1}(K^{n-1})$ are isomorphisms. By Lemmas 1 and 2 plus the obvious map, $H_p^{\mathrm{simp}}(K^n, K^{n-1}) \to H_p(K^n, K^{n-1})$ is an isomorphism. By the **five lemma** applied to the ladder, $\iota_* : H_p^{\mathrm{simp}}(K^n) \to H_p(K^n) = H_p(M)$ is an isomorphism. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Computing $H_*(S^n)$ via simplicial homology.** Triangulate $S^n$ as the boundary of the standard $(n+1)$-simplex — i.e. the union of the $n+1$ codimension-$1$ faces of $\Delta^{n+1}$, glued along their common boundaries. This gives a simplicial complex with $n + 2$ vertices, $\binom{n+2}{2}$ edges, $\dots$, $\binom{n+2}{n+1} = n + 2$ top-dimensional $n$-simplices. Compute the simplicial homology by Gaussian elimination on the explicit boundary matrices and verify $H_p(S^n; \mathbb{Z}) = \mathbb{Z}$ for $p = 0, n$ and zero otherwise.

**Computing $H_*(T^2)$ from a triangulation.** Triangulate the torus as a rectangle with identifications, divided into $18$ triangles (Frankel Figure 13.12). The $1$-skeleton consists of the boundary loops $A, B$ and additional interior edges from the triangulation. Compute the simplicial chain complex matrices explicitly and verify $H_0 = H_2 = \mathbb{Z}$ and $H_1 = \mathbb{Z}^2$ — generated by the loops $A$ and $B$.

**Computing $H_*$ of a polygon with identifications.** For any closed surface presented as a polygon with edge identifications (an orientable genus-$g$ surface has a $4g$-gon presentation with all vertices identified), triangulate, write down the simplicial chain complex, and compute the homology directly. Verify $\chi(\Sigma_g) = 2 - 2g$ by the Euler characteristic formula and by direct alternating sum of simplex counts.

**Computing $H_*$ of a CW complex via cellular homology.** Cellular homology is the same as simplicial homology after refining a CW structure to a triangulation (or directly using the cellular chain complex). For $\mathbb{CP}^n$ with its CW structure ($n + 1$ even cells, one per dimension $0, 2, 4, \dots, 2n$), the cellular boundary maps are all zero, and $H_{2k}(\mathbb{CP}^n; \mathbb{Z}) = \mathbb{Z}$ for $0 \leq k \leq n$, all others zero — vastly faster than triangulating and computing simplicially.

---

# Bridges

- **[[Def - Singular Homology|Singular homology]]** — the theorem makes singular homology computable via simplicial triangulations. Without this, singular homology would be a conceptual but not a computational tool.

- **Cellular homology** — for CW complexes, the cellular chain complex (one generator per cell) computes singular homology via a parallel argument (cellular approximation, etc.). The same skeletal-induction-plus-five-lemma argument shows cellular ≅ singular.

- **[[Thm - Euler Characteristic via Alternating Betti Numbers|Euler characteristic via alternating Betti numbers]]** — combined with this theorem, gives $\chi(M) = \sum (-1)^p c_p$ where $c_p$ is the number of $p$-simplices in any triangulation. This is the topological invariance of the alternating cell count — Euler's polyhedral formula generalised.

- **[[Thm - The de Rham Theorem (Full Proof)|de Rham theorem]]** — uses this theorem implicitly: the proof reduces to a finite good cover (by contractibles) and applies Mayer–Vietoris. The "finite" aspect comes from the existence of finite good covers on compact triangulable manifolds.

- **Simplicial approximation theorem** — a closely related result asserts that every continuous map $|K| \to |L|$ between triangulated spaces is homotopic to a *simplicial* map (after refining $K$). This is the dynamic version of the static "simplicial = singular" theorem, and it underpins the cellular approximation theorem for CW complexes.

---

# Unlocked by This

> [!tip] Computational Algebraic Topology *(from Algebraic Topology)*
> Every explicit computation of singular homology on a finite triangulable space goes through this theorem. Modern computational topology — persistent homology, topological data analysis, computational topology of manifolds — all relies on simplicial complexes (or their generalisations like CW complexes, cubical complexes, alpha complexes) and the algorithmic computation of their simplicial homology.

> [!tip] Finite-Generation of Homology *(from Algebraic Topology)*
> Triangulable spaces have finitely generated singular homology, with computable rank (Betti numbers) and torsion. This is what makes the homological invariants of compact manifolds tractable — without the theorem, one could not compute Betti numbers algorithmically.

> [!tip] **The Eilenberg–Steenrod Uniqueness Theorem** *(from Algebraic Topology)*
> The theorem that any "ordinary" homology theory on CW complexes agrees with singular homology relies on this comparison: simplicial homology satisfies the Eilenberg–Steenrod axioms, and the agreement with singular homology then forces uniqueness on CW complexes.

> [!tip] **Combinatorial Differential Topology** *(from Differential Topology)*
> Smooth manifolds admit smooth triangulations (Whitehead, Whitney), and the simplicial structure can be used to compute smooth invariants. **Combinatorial differential topology** (e.g. Forman's discrete Morse theory) uses simplicial structures to define discrete analogues of smooth invariants — discrete Morse functions, discrete vector fields, discrete Riemannian geometry.

> [!tip] **Triangulability Failure and Wild Topology** *(from Algebraic Topology / Geometric Topology)*
> Not every topological space is triangulable! In dimensions $\geq 4$, there exist topological manifolds that admit no smooth structure and no triangulation (proved by Casson, Freedman, and others). For non-triangulable spaces, singular homology is still defined and meaningful, but the simplicial computational shortcut does not apply. This is the boundary between "tame" topology (manifolds with PL or smooth structures, where simplicial homology works) and "wild" topology (where it doesn't).
