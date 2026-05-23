---
type: definition
subject: algebraic-topology
prereqs: []
tags: [geometry, algebraic-topology, simplex]
---

# Notation

$p \geq 0$ is a non-negative integer. $\Delta^p$ denotes the standard $p$-simplex. We use two realisations interchangeably:

- The **affine realisation in $\mathbb{R}^p$**: $\Delta^p = \mathrm{conv}(P_0, P_1, \dots, P_p)$ where $P_0 = 0$ and $P_k = e_k$ (the $k$-th standard basis vector) for $k \geq 1$. This is Frankel's convention.
- The **barycentric realisation in $\mathbb{R}^{p+1}$**: $\Delta^p = \{(t_0, \dots, t_p) \in \mathbb{R}^{p+1} : t_i \geq 0,\ \sum_i t_i = 1\}$. The coordinates $(t_0, \dots, t_p)$ are the **barycentric coordinates**.

The two realisations are affinely equivalent: the bijection sends $(t_0, \dots, t_p) \in \mathbb{R}^{p+1}$ to $\sum_{i=0}^p t_i P_i \in \mathbb{R}^p$. We write a $p$-simplex with vertex labels in either notation: $(P_0, \dots, P_p) = (v_0, \dots, v_p)$ is the standard simplex with the vertex labels $v_i$.

The **$k$-th face** of $\Delta^p$ is the $(p-1)$-dimensional face opposite the vertex $P_k$ (i.e. with $P_k$ omitted), denoted $\Delta^{p-1}_{(k)} = (P_0, \dots, \widehat{P_k}, \dots, P_p)$ where the hat means omission.

---

# Axiom Motivation

We want to build a theory of "$p$-dimensional pieces of a space" that is uniform across all dimensions and across all topological spaces. The starting point must be a single, canonical "model" $p$-dimensional object — a *universal* $p$-dimensional shape — into which we then map our space. Every later construction (singular simplex, singular chain, boundary operator) is built by referring back to this canonical model.

What should the model object look like? Three requirements pin it down.

First, **it should be the simplest non-degenerate $p$-dimensional shape.** A non-degenerate $p$-dimensional region in $\mathbb{R}^N$ is determined by $p+1$ affinely independent points (any fewer points span a lower-dimensional affine subspace; any more are redundant). The convex hull of $p+1$ affinely independent points is the unique simplest convex body of dimension $p$ — the $p$-simplex. So the model object has $p+1$ vertices, and combinatorially is just "all non-negative real combinations of $p+1$ things, summing to one." Drop the requirement of $p+1$ vertices and one would have either degenerate flat pieces or higher-codimension corners — neither suitable as a universal building block.

Second, **the faces of the model object should be (copies of) lower-dimensional models.** A $p$-simplex has $p+1$ codimension-one faces, each of which is again a $(p-1)$-simplex — obtained by omitting one vertex. This recursive structure is crucial: when we define the boundary operator $\partial$ on singular simplices, the boundary will be a formal sum of $(p-1)$-dimensional faces, and each face will itself be a singular $(p-1)$-simplex with its own boundary. If the faces of the model were not lower-dimensional models, the boundary operator would not iterate. The standard simplex has this self-similar structure built into its definition by convex-hull-of-vertices.

Third, **the model object should carry a canonical ordering of vertices that allows orientation tracking.** When we define the boundary $\partial \Delta^p = \sum_{k=0}^p (-1)^k \Delta^{p-1}_{(k)}$, the alternating signs come from a *consistent* choice of how to orient each face relative to the parent. The ordered tuple $(P_0, \dots, P_p)$ — vertices listed in a specific order — supplies the orientation: the face $\Delta^{p-1}_{(k)}$ inherits an orientation from $\Delta^p$, and the sign $(-1)^k$ records whether omitting the $k$-th vertex flips or preserves it. Without an ordering, the alternating sum would not be well-defined, $\partial^2 = 0$ would fail, and there would be no singular homology. So the model object is **an ordered set of vertices** with the convex hull viewed as a geometric realisation.

There is one more design choice. Why the *specific* affine realisation $P_0 = 0$, $P_k = e_k$? The answer is convenience, not necessity — any two non-degenerate $p$-simplices in any Euclidean space are affinely equivalent, so the choice does not change the theory. Frankel's realisation in $\mathbb{R}^p$ makes the simplex sit in the smallest possible ambient space, with $P_0$ at the origin. The barycentric realisation in $\mathbb{R}^{p+1}$ makes the symmetry between vertices manifest: the $p+1$ vertices are the $p+1$ standard basis vectors, and the symmetric group $S_{p+1}$ acts on the simplex by permuting them. Both are useful; we use whichever is convenient for the calculation at hand.

The recursive face structure is what makes the simplex the right shape for building a *complex* — a structure where simplices of all dimensions are glued together. If we had used cubes instead (the standard $p$-cube $[0,1]^p$), the faces of a $p$-cube are $2p$ different $(p-1)$-cubes (the $2p$ faces of an $n$-cube), which would give a "cubical" homology theory — entirely valid, and historically also developed (Bott and Tu use cubes for some of their constructions), but conventionally less common. The simplex's advantage is that the number of $k$-faces of a $p$-simplex is just $\binom{p+1}{k+1}$, simpler than the cube's analogous count, and the resulting boundary algebra is correspondingly cleaner.

---

# The Definition

The **standard $p$-simplex** for $p \geq 0$ is the topological space
$$
\Delta^p \;=\; \left\{ (t_0, t_1, \dots, t_p) \in \mathbb{R}^{p+1} \;:\; t_i \geq 0 \text{ for all } i,\ \text{ and } \sum_{i=0}^p t_i = 1 \right\},
$$
equipped with the subspace topology from $\mathbb{R}^{p+1}$. The coordinates $(t_0, \dots, t_p)$ are the **barycentric coordinates**. The **vertices** of $\Delta^p$ are the $p+1$ points $v_i = (0, \dots, 0, 1, 0, \dots, 0)$ (with the $1$ in the $i$-th position).

For each $0 \leq k \leq p$, the **$k$-th face** of $\Delta^p$ is the $(p-1)$-dimensional sub-simplex
$$
\Delta^{p-1}_{(k)} \;=\; \{(t_0, \dots, t_p) \in \Delta^p : t_k = 0\},
$$
obtained by setting the $k$-th barycentric coordinate to zero (equivalently, omitting the $k$-th vertex). The **$k$-th face map** $f_k : \Delta^{p-1} \to \Delta^p$ is the unique affine embedding sending $(s_0, \dots, s_{p-1}) \mapsto (s_0, \dots, s_{k-1}, 0, s_k, \dots, s_{p-1})$ — its image is $\Delta^{p-1}_{(k)}$.

Equivalently, in Frankel's affine realisation in $\mathbb{R}^p$ with $P_0 = 0$ and $P_k = e_k$ for $k \geq 1$, $f_k$ is the unique affine map $\mathbb{R}^{p-1} \to \mathbb{R}^p$ sending $P_j \mapsto P_j$ for $j < k$ and $P_j \mapsto P_{j+1}$ for $j \geq k$.

The standard simplex is **ordered**: the tuple $(v_0, v_1, \dots, v_p)$ has a fixed linear order on its vertices. This order is used in defining the alternating-sign boundary operator.

---

# Categorical / Structural Definition

The standard simplices $\Delta^p$, together with the face maps $f_k : \Delta^{p-1} \to \Delta^p$ (and certain "degeneracy" maps in the simplicial-set context), form a category — the **simplex category** $\Delta$. Its objects are the finite ordered sets $[p] = \{0 < 1 < \cdots < p\}$, one for each $p \geq 0$; its morphisms are the order-preserving maps. A **simplicial set** is then defined as a contravariant functor $\Delta^{\mathrm{op}} \to \mathbf{Set}$ — equivalently, a sequence $X_0, X_1, X_2, \dots$ of sets equipped with face and degeneracy maps satisfying simplicial identities.

The geometric realisation functor $|\cdot| : \mathbf{sSet} \to \mathbf{Top}$ converts a simplicial set into a topological space by gluing copies of the standard simplices along the face/degeneracy maps. The singular complex of a topological space $M$ is the simplicial set $\mathrm{Sing}(M)$ with $\mathrm{Sing}(M)_p = \mathrm{Maps}(\Delta^p, M)$ — the set of all singular $p$-simplices — and the face maps $d_k : \mathrm{Sing}(M)_p \to \mathrm{Sing}(M)_{p-1}$ are precomposition with the face maps $f_k$ of the standard simplex.

This perspective unifies singular homology with simplicial homology: both come from applying a chain-complex functor to a simplicial set, and the resulting homology is a topological invariant of the geometric realisation. From this categorical viewpoint, the standard simplex is the *representable* object in $\mathbf{sSet}$ corresponding to the singleton functor, and every simplicial structure is built up from copies of it.

---

# Relate to Other Fields / Compression

The standard $p$-simplex is the **convex hull of $p+1$ affinely independent points** — the simplest non-degenerate convex body of dimension $p$. From this viewpoint it is the analogue, for general $p$, of the line segment ($p=1$), the triangle ($p=2$), the tetrahedron ($p=3$).

It is also the **probability $p$-simplex**: in probability theory, the set of probability distributions over $p+1$ outcomes is exactly $\Delta^p$, with the $i$-th barycentric coordinate $t_i$ being the probability of outcome $i$. The constraint $t_i \geq 0$, $\sum t_i = 1$ is the definition of a discrete probability distribution. The vertices are the deterministic outcomes; the interior consists of all strictly mixed distributions. This identification makes the standard simplex one of the most-studied objects in probability theory, information theory, and statistics.

**True name:** the standard $p$-simplex is the **probability simplex on $p+1$ vertices** — the set of weight vectors $(t_0, \dots, t_p)$ with $t_i \geq 0$ and $\sum t_i = 1$. The "convex hull of $p+1$ affinely independent points" definition is the geometric one; the "weight vectors that sum to one" definition is the operational one for both topology (every point is a barycentric combination of vertices) and probability (every point is a probability distribution over $p+1$ outcomes).

---

# Examples / Corollaries

**$\Delta^0$** is a single point — the convex hull of $0+1 = 1$ point. It is the only $0$-simplex up to affine equivalence.

**$\Delta^1$** is a closed line segment, the convex hull of two points $v_0, v_1$. It is homeomorphic to $[0, 1]$, with $v_0 = 0$ and $v_1 = 1$ as the two boundary vertices.

**$\Delta^2$** is a (closed) triangle, the convex hull of three non-collinear points. Its three faces are the three edges, each a copy of $\Delta^1$. The face maps $f_0, f_1, f_2 : \Delta^1 \to \Delta^2$ embed the standard interval as the three edges of the triangle (face opposite $v_0$, face opposite $v_1$, face opposite $v_2$).

**$\Delta^3$** is a closed tetrahedron, the convex hull of four non-coplanar points. It has four triangular faces (each a $\Delta^2$), six edges (each a $\Delta^1$), and four vertices.

**Is NOT an instance: a square $[0,1]^2$.** The unit square in the plane is *not* a $2$-simplex — it is the convex hull of *four* points, not three. It is the standard $2$-*cube*, the building block of cubical homology, a related but different theory. The two cohomology theories agree (both compute singular cohomology of the underlying space), but the chain complexes and computations differ.

**Is NOT an instance: a circle $S^1$.** The circle is one-dimensional, so one might wonder if it is "the boundary of $\Delta^2$" or some such. It is *not* a simplex: a simplex is a convex set, while the circle is not convex (it is a curve, not a disk). The closed disk $D^2$ is homeomorphic to $\Delta^2$; the circle $S^1 = \partial D^2$ is the boundary, which is a $1$-sphere, not a $1$-simplex. The standard simplices are all *contractible* (convex sets are star-shaped about any interior point); spheres are not.

**Corollary (number of faces).** The standard $p$-simplex has $\binom{p+1}{k+1}$ codimension-$(p-k)$ faces for each $0 \leq k \leq p$. In particular: $p+1$ vertices ($\binom{p+1}{1}$), $\binom{p+1}{2}$ edges, $\binom{p+1}{3}$ $2$-faces, and so on. For $\Delta^3$: $4$ vertices, $6$ edges, $4$ triangular faces, $1$ tetrahedral interior — matching the count of any tetrahedron.

**Corollary (the simplex is compact).** $\Delta^p \subset \mathbb{R}^{p+1}$ is closed (intersection of finitely many closed half-spaces with the hyperplane $\sum t_i = 1$) and bounded (contained in $[0,1]^{p+1}$), hence compact by Heine–Borel. Consequence: any continuous map $\sigma : \Delta^p \to M$ has compact image in $M$, which is the reason singular simplices behave well with respect to integration and partition-of-unity arguments.

**Corollary (the simplex is contractible).** $\Delta^p$ is convex, hence star-shaped about any interior point, hence contractible via the straight-line homotopy $H((t_0, \dots, t_p), s) = (1-s)(t_0, \dots, t_p) + s\,(1/(p+1), \dots, 1/(p+1))$ to the barycentre. Consequence: $\Delta^p$ has trivial singular homology in positive degrees, with $H_0(\Delta^p; G) = G$.

**Calibration check.** If you understand the definition you should be able to: (1) describe the four faces of $\Delta^3$ explicitly as sub-simplices of the standard tetrahedron, listing the vertices of each; (2) write down the $k$-th face map $f_k : \Delta^1 \to \Delta^2$ as an explicit affine formula for $k = 0, 1, 2$; (3) verify that $f_0$ sends $(s_0, s_1) \mapsto (0, s_0, s_1)$ in barycentric coordinates.

---

# Unlocked by This

> [!tip] Singular Simplex *(from Algebraic Topology — this same topic)*
> Once you have the standard $p$-simplex as a universal model, a **singular $p$-simplex** in any topological space $M$ is simply a continuous map $\sigma : \Delta^p \to M$. This is the building block of singular homology — see [[Def - Singular Simplex]]. The flexibility of allowing *any* continuous map (not requiring embedding, smoothness, or full rank) is what makes singular homology defined for arbitrary topological spaces.

> [!tip] Simplicial Complex *(from Combinatorial Topology)*
> A **simplicial complex** is a set glued from copies of standard simplices along their faces, subject to the rule that the intersection of any two simplices is a face of each. Every triangulable space (every smooth manifold, every CW complex) admits a simplicial complex structure, and the resulting simplicial homology agrees with singular homology — see [[Thm - Singular and Simplicial Homology Agree on Triangulable Spaces]]. The combinatorial finiteness of a simplicial complex is what makes explicit computation tractable.

> [!tip] **Simplicial Set** *(from Algebraic Topology and Higher Category Theory)*
> Replacing the geometric standard simplex by its categorical shadow — the simplex category $\Delta$ — gives the notion of a **simplicial set**, a contravariant functor $\Delta^{\mathrm{op}} \to \mathbf{Set}$. Every topological space gives rise to a simplicial set (its singular complex), and the homotopy category of simplicial sets is equivalent to that of topological spaces. This is the foundation of higher category theory, where the standard simplex $\Delta^p$ becomes the universal "$p$-morphism," and homotopy theory becomes a purely combinatorial subject.

> [!tip] **Probability Simplex and Information Geometry** *(from Probability and Information Theory)*
> Recognising the standard $p$-simplex as the space of probability distributions over $p+1$ outcomes opens a connection to **information geometry**: $\Delta^p$ is a Riemannian manifold under the **Fisher information metric**, and the geodesics of this metric correspond to one-parameter families of distributions interpolating between two given ones. The KL divergence, the Shannon entropy, and the relative entropy are all defined as functions on $\Delta^p$, and information theory becomes geometry of the probability simplex.
