---
type: definition
subject: algebraic-topology
prereqs:
  - "Def - The Standard p-Simplex"
tags: [geometry, algebraic-topology]
---

# Notation

$M$ is a topological space (or a smooth manifold, when we want to integrate forms over the simplex). $\Delta^p$ is the [[Def - The Standard p-Simplex|standard p-simplex]] with vertices $v_0, \dots, v_p$ in barycentric coordinates (or $P_0, \dots, P_p$ in Frankel's affine realisation). $\sigma$, $\tau$ denote singular simplices.

Smooth versus continuous: a **continuous singular simplex** is a continuous map $\Delta^p \to M$; a **smooth singular simplex** in a smooth manifold $M$ is a smooth map $\Delta^p \to M$, where smoothness means the map extends to a smooth map on an open neighborhood of $\Delta^p$ in $\mathbb{R}^{p+1}$ (the simplex itself has a boundary, so the standard definition of smoothness via charts requires the extension). Both versions give the same homology, by smoothing arguments (Whitney approximation), but the smooth version is what is needed to define $\int_\sigma \omega$ for differential forms.

---

# Axiom Motivation

We want to model "an arbitrary $p$-dimensional piece of $M$" — something we can integrate forms over, take boundaries of, and combine into formal sums. What is the most permissive notion that still supports a well-defined boundary operator?

The first instinct might be to require an embedded $p$-dimensional submanifold of $M$. This is too restrictive on two fronts. First, the boundary of an embedded $p$-submanifold need not be an embedded $(p-1)$-submanifold — it might be a manifold with corners (consider a square in $\mathbb{R}^2$, whose boundary has four corners), or have self-intersections. Second, requiring submanifolds restricts us to manifolds — but we want a theory that works for arbitrary topological spaces (CW complexes, polyhedra, fractal sets, finite point sets).

The second instinct might be to require an embedded copy of $\Delta^p$ — a homeomorphism from the standard simplex onto its image. This is still too restrictive. A constant map (every point of $\Delta^p$ sent to a single point of $M$) is not an embedding, but it is needed for the homology theory to work: constant simplices give the generators in the chain complex of a point, and the homology of a point is the base case of every Mayer–Vietoris induction.

The third instinct — and the right one — is to require nothing more than continuity. A **singular $p$-simplex** is simply a continuous map $\sigma : \Delta^p \to M$, with no restrictions on rank, injectivity, or smoothness. The word "singular" warns the reader: the image of $\sigma$ may be smaller than $p$-dimensional (the map can be constant, sending the whole simplex to a single point), may have self-intersections, may fail to be a submanifold. The simplex is "singular" in the sense that it can have singularities (low-rank points, self-crossings, collapsings) — anything continuous is allowed.

Why is this the right level of generality? Three reasons.

First, **continuity is exactly the right structure to compose with face maps.** The face maps $f_k : \Delta^{p-1} \to \Delta^p$ are continuous (in fact affine), so the $k$-th face $\sigma \circ f_k : \Delta^{p-1} \to M$ of a singular simplex $\sigma : \Delta^p \to M$ is automatically a continuous map again — a singular $(p-1)$-simplex. The boundary operator $\partial \sigma = \sum (-1)^k (\sigma \circ f_k)$ then lives in the same category. If we had instead required smoothness or transversality conditions, the composition might fail to satisfy them (the face $\sigma \circ f_k$ might not be smooth at vertices, or might not be transverse to anything in particular), and the boundary operator would land outside our chosen class.

Second, **continuity is preserved by continuous maps of the target space.** If $f : M \to N$ is continuous, then for any singular $p$-simplex $\sigma : \Delta^p \to M$, the composition $f \circ \sigma : \Delta^p \to N$ is a singular $p$-simplex of $N$. This makes singular simplices *functorial* — singular homology becomes a functor $\mathbf{Top} \to \mathbf{Ab}$. Smoothness, embedding, immersion, and similar restrictions are *not* preserved by arbitrary continuous maps (a continuous map can collapse a smooth submanifold to a single point), so they would not give a functorial theory on $\mathbf{Top}$.

Third, **the homology of singular simplices agrees with simplicial or cellular homology when applicable.** The "small replacement" theorem ([[Thm - Singular and Simplicial Homology Agree on Triangulable Spaces]]) says that for spaces admitting a triangulation or CW structure, the homology of all singular simplices equals the homology of just the simplicial or cellular ones. So we lose nothing by being permissive: the singular theory contains the simplicial theory as a sub-theory (with the same homology), and additionally extends to spaces that admit no triangulation. This is the model of "make the category large enough to be flexible, then prove that the homology cares only about a small subcategory."

What about constant simplices? It is sometimes objected that allowing constant maps $\sigma : \Delta^p \to \{q\}$ introduces redundancy — they should be "trivial" but they are not zero in the chain complex. The resolution is that constant simplices *do* contribute to the chain complex, but their boundaries cancel: $\partial(\sigma_p) = \sum_{k=0}^p (-1)^k \sigma_{p-1}$, where each face $\sigma \circ f_k$ is again the constant map to $q$, equal to $\sigma_{p-1}$. So $\partial \sigma_p = (\sum_{k=0}^p (-1)^k) \sigma_{p-1} = \sigma_{p-1}$ if $p$ is even and $0$ if $p$ is odd. The chain complex of a single point therefore alternates $\mathbb{Z} \xleftarrow{0} \mathbb{Z} \xleftarrow{1} \mathbb{Z} \xleftarrow{0} \mathbb{Z} \xleftarrow{1} \cdots$, with homology $\mathbb{Z}$ in degree zero and $0$ in higher degrees — exactly what we want for a point. The constant simplices are necessary, but they cancel correctly.

A smooth singular simplex is an additional restriction needed when we want to *integrate* forms over the simplex. The integration $\int_\sigma \omega = \int_{\Delta^p} \sigma^* \omega$ requires the pullback $\sigma^* \omega$ to be a smooth form on $\Delta^p$, which requires $\sigma$ to be smooth. The Whitney approximation theorem then says every continuous singular simplex is homotopic to a smooth one, so the smooth-simplex sub-complex computes the same homology as the all-continuous-simplex complex — this is what makes the de Rham pairing well-defined on all of singular homology, not just the smooth part.

---

# The Definition

Let $M$ be a topological space and let $p \geq 0$. A **singular $p$-simplex** in $M$ is a continuous map
$$
\sigma : \Delta^p \to M,
$$
where $\Delta^p$ is the [[Def - The Standard p-Simplex|standard p-simplex]]. No further restrictions: $\sigma$ need not be injective, need not be of full rank, need not be a submersion or immersion, need not be smooth.

The **$k$-th face** of $\sigma$ (for $0 \leq k \leq p$) is the singular $(p-1)$-simplex
$$
\partial_k \sigma \;=\; \sigma \circ f_k : \Delta^{p-1} \to M,
$$
where $f_k : \Delta^{p-1} \to \Delta^p$ is the [[Def - The Standard p-Simplex|k-th face map]] of the standard simplex.

If $M$ is a smooth manifold, a **smooth singular $p$-simplex** is a singular $p$-simplex $\sigma : \Delta^p \to M$ that is the restriction of a smooth map defined on a neighborhood of $\Delta^p$ in $\mathbb{R}^{p+1}$ (equivalently, $\sigma$ extends smoothly across the boundary of $\Delta^p$). Smooth singular simplices form a subset of all singular simplices, closed under taking faces and under post-composition with smooth maps.

---

# Relate to Other Fields / Compression

A singular simplex is **a parameterisation of a $p$-dimensional region of $M$ by the standard model $\Delta^p$**. The phrase "parameterised subset" is Frankel's term (Section 3.1b), and that section's discussion of integration over parameterised subsets generalises directly to integration of forms over singular simplices: $\int_\sigma \omega = \int_{\Delta^p} \sigma^* \omega$.

It is also **the algebraic-topology analogue of an embedded chart**. In differential geometry, a chart $(\varphi, U)$ on $M$ is a homeomorphism $\varphi : U \to V \subseteq \mathbb{R}^n$ from an open set of $M$ to an open set of Euclidean space — a parameterisation of $U$ by a model open set. A singular simplex is an analogous parameterisation, but with the model object being the standard simplex (a compact, non-open set with boundary) rather than an open set, and with no restriction to homeomorphism.

**True name:** a singular simplex is a **continuous map from the standard simplex** — nothing more, nothing less. The geometric picture of "an embedded triangle in $M$" is misleading; the correct picture is "any continuous function whatsoever from $\Delta^p$ to $M$," up to and including constant functions, low-rank maps, and self-intersecting maps. The word "singular" is a warning against geometric over-specialisation.

---

# Examples / Corollaries

**Is an instance: a continuous path.** A continuous path $\gamma : [0, 1] \to M$ in $M$ is a singular $1$-simplex (after identifying $[0, 1]$ with $\Delta^1$). Its boundary is $\partial \gamma = \gamma(1) - \gamma(0)$, the difference of the endpoint and starting point as $0$-simplices. This is the prototypical singular $1$-simplex; paths assembled into cycles give the $1$-dimensional homology.

**Is an instance: an embedded triangle.** A homeomorphism of $\Delta^2$ onto an embedded triangle in $M$ is a singular $2$-simplex — this matches the geometric picture of a "triangle in $M$." The faces are the three edges of the triangle, themselves singular $1$-simplices (continuous paths along the edges).

**Is an instance: a constant map.** For any point $q \in M$, the constant map $\sigma_p : \Delta^p \to \{q\} \subset M$, $x \mapsto q$, is a singular $p$-simplex. Every face $\sigma_p \circ f_k$ is again the constant map to $q$, namely $\sigma_{p-1}$. The boundary $\partial \sigma_p = \sum_k (-1)^k \sigma_{p-1} = \begin{cases} \sigma_{p-1} & p \text{ even} \\ 0 & p \text{ odd} \end{cases}$. Constant simplices are non-trivial elements of the chain complex but their alternating-sum boundaries cancel.

**Is an instance: a low-rank or degenerate map.** A continuous map $\sigma : \Delta^2 \to M$ that collapses an edge to a point — for instance, send $(t_0, t_1, t_2)$ with $t_2 = 0$ all to a single point $q$, and the rest of the simplex into $M$ continuously — is a perfectly valid singular $2$-simplex. The resulting boundary chain has unexpected structure (one face collapsed to a constant), but the chain complex absorbs this without difficulty.

**Is an instance: a smooth map (when $M$ is smooth).** Any smooth map $\sigma : \Delta^p \to M$ is a singular simplex. Smooth singular simplices are the subclass over which we can integrate differential forms, $\int_\sigma \omega = \int_{\Delta^p} \sigma^* \omega$.

**Is NOT an instance: a discontinuous map.** A function $\sigma : \Delta^p \to M$ that fails to be continuous (e.g. a jump function) is *not* a singular simplex — continuity is the one non-negotiable requirement.

**Is NOT an instance: an immersed submanifold of $M$.** An immersion $\iota : N \hookrightarrow M$ from a $p$-dimensional manifold $N$ is not by itself a singular simplex (its domain is not $\Delta^p$). To convert it into singular chains, one triangulates $N$ and pre-composes each triangulation simplex with $\iota$; the result is a singular $p$-chain (a formal sum of singular simplices), not a single singular simplex.

**Corollary (post-composition).** If $f : M \to N$ is continuous and $\sigma : \Delta^p \to M$ is a singular $p$-simplex of $M$, then $f \circ \sigma : \Delta^p \to N$ is a singular $p$-simplex of $N$. This is the functorial action: continuous maps induce maps on the set of singular simplices, hence on the chain complex, hence on homology.

**Corollary (the image is compact and connected).** Since $\Delta^p$ is compact and path-connected, the image of any singular simplex $\sigma : \Delta^p \to M$ is a compact, path-connected subset of $M$. Consequence: singular chains have compact support — they only "see" compact subsets of $M$, which is why singular homology behaves well even for non-compact manifolds where the manifold itself is not compact.

**Calibration check.** If you have understood the definition you should be able to: (1) explain why a non-injective continuous map $\Delta^2 \to M$ is still a valid singular $2$-simplex; (2) compute the boundary of a constant singular $3$-simplex and verify it is zero; (3) write down a singular $2$-simplex in $S^2$ that is not the embedding of a triangle (e.g. a continuous map whose image is the entire sphere).

---

# Unlocked by This

> [!tip] Singular Chain *(from Algebraic Topology — this same topic)*
> A finite formal sum of singular simplices with coefficients in an abelian group $G$ is a **singular chain** — see [[Def - Singular Chain]]. The collection of all $p$-chains is the singular chain group $C_p(M; G)$, a free $G$-module on the (uncountable) set of singular $p$-simplices.

> [!tip] Functoriality of Singular Homology *(from Algebraic Topology — this same topic)*
> Since continuous maps induce maps on singular simplices, they induce chain maps on chain groups and hence homomorphisms on singular homology. Singular homology is a covariant functor $H_p : \mathbf{Top} \to \mathbf{Ab}$ — see [[Def - Singular Homology]]. This functoriality is what makes singular homology a topological invariant: homeomorphic spaces have isomorphic homology, and (deeper) homotopy equivalent spaces do too.

> [!tip] **Geometric Realisation of a Simplicial Set** *(from Algebraic Topology and Higher Category Theory)*
> When we collect together all singular simplices of $M$ into a single combinatorial structure — the **singular simplicial set** $\mathrm{Sing}(M)$ — we have built a complete functorial bridge $\mathbf{Top} \to \mathbf{sSet}$, with a left adjoint $|\cdot| : \mathbf{sSet} \to \mathbf{Top}$ (geometric realisation). The unit $M \to |\mathrm{Sing}(M)|$ is a weak homotopy equivalence, so the homotopy theory of topological spaces is faithfully captured by the combinatorial structure of singular simplices. This is the foundation of model categories and higher category theory.
