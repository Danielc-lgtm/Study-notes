---
type: definition
subject: algebraic-topology
prereqs:
  - "Def - Singular Simplex"
  - "Def - Abelian Group"
  - "Def - Free Module"
tags: [geometry, algebraic-topology]
---

# Notation

$M$ is a topological space. $G$ is an abelian group, the **coefficient group**. The most common choices are $G = \mathbb{Z}$ (integer chains, the universal case), $G = \mathbb{R}$ (real chains, used in de Rham comparison), $G = \mathbb{Q}$ (rational chains), and $G = \mathbb{Z}/n\mathbb{Z}$ (chains mod $n$).

$\sigma_1, \sigma_2, \dots$ denote individual singular $p$-simplices in $M$. $g_1, g_2, \dots$ are elements of $G$.

A chain is written as a formal sum $c_p = g_1 \sigma_1 + g_2 \sigma_2 + \cdots + g_r \sigma_r$, with the understanding that all but finitely many terms have coefficient zero. Equivalently, $c_p$ is a function $\sigma \mapsto c_p(\sigma)$ from the set of all singular $p$-simplices to $G$, with $c_p(\sigma_i) = g_i$ and $c_p(\sigma) = 0$ for $\sigma$ not on the list.

$C_p(M; G)$ is the **singular $p$-chain group** of $M$ with coefficients in $G$.

---

# Axiom Motivation

We have defined singular simplices — continuous maps $\sigma : \Delta^p \to M$ — as the geometric building blocks. To do *algebra* with them (sum cycles, take quotients, define homology as $\ker / \mathrm{im}$), we need to embed them in an algebraic structure where the operations are well-defined.

The most flexible such embedding is the **free abelian group** on the set of singular simplices. Recall (analogous to [[Def - Free Module|free modules]] over $\mathbb{Z}$) that the free abelian group on a set $S$ is the set of finite formal $\mathbb{Z}$-linear combinations $\sum_i n_i s_i$ with $s_i \in S$ and $n_i \in \mathbb{Z}$, with addition defined termwise. Replacing $\mathbb{Z}$ by an arbitrary abelian group $G$ gives the free $G$-module on $S$: finite formal $G$-linear combinations.

Why this structure? Three demands force it.

First, **we need to add two singular simplices.** If $\sigma_1$ and $\sigma_2$ are two singular $1$-simplices (paths) in $M$, their sum $\sigma_1 + \sigma_2$ should be a meaningful object — for instance, the "concatenation" of the two paths viewed as a $1$-chain whose boundary is $(\partial \sigma_1) + (\partial \sigma_2)$. The set of singular simplices is not a group (there is no natural way to "add" two continuous maps), so we have to *formally* adjoin sums. The free abelian group does exactly this: it adjoins all finite formal sums without imposing any relations beyond commutativity and associativity of addition.

Second, **we need to multiply a singular simplex by a scalar.** The chain $2\sigma$ should mean "the simplex $\sigma$ counted twice," and $-\sigma$ should mean "the simplex $\sigma$ traversed in the opposite orientation." Allowing integer coefficients lets us write the boundary $\partial \sigma = \sum_k (-1)^k (\sigma \circ f_k)$ as a literal sum with $\pm 1$ coefficients — the alternating signs are integer coefficients on the formal sum. So $G = \mathbb{Z}$ is the minimal coefficient group that supports the alternating-sign boundary operator.

Third, **the coefficient group $G$ should be allowed to vary.** Why not just always use $G = \mathbb{Z}$? Because different choices of $G$ reveal different topological information about $M$.

- $G = \mathbb{R}$ (or any field of characteristic zero) gives **real chains** $C_p(M; \mathbb{R})$ which are real vector spaces. The chain group becomes infinite-dimensional but the homology $H_p(M; \mathbb{R})$ is finite-dimensional for compact $M$, and its dimension is the **Betti number** $b_p$. The de Rham theorem then identifies $H^p_{dR}(M) \cong H^p(M; \mathbb{R})$ via integration of forms, and the de Rham comparison only makes sense with real coefficients (you cannot integrate a real-valued form over an integer-weighted chain to get an integer; the answer is real).

- $G = \mathbb{Z}/2\mathbb{Z}$ gives **mod-$2$ chains** where signs vanish ($+1 = -1$ in $\mathbb{Z}/2$). This is useful for non-orientable spaces, where the orientation signs in the boundary operator cause trouble: the Möbius band has $[Mö]$ as a non-trivial $\mathbb{Z}/2$-cycle but its $\mathbb{Z}$-boundary is $2A \neq 0$. With $\mathbb{Z}/2$ coefficients, $2A = 0$ and $[Mö]$ is a cycle. So $\mathbb{Z}/2$-coefficients "see" non-orientable phenomena that $\mathbb{Z}$-coefficients hide as torsion.

- $G = \mathbb{Z}$ is the **universal** choice. The universal coefficient theorem then computes $H_p(M; G)$ for any $G$ from $H_p(M; \mathbb{Z})$ via tensor and torsion products. So $\mathbb{Z}$-coefficients encode the most information; other coefficients are derived.

What about non-finite formal sums? Why do we require chains to be *finite* sums? Two reasons. First, the boundary operator $\partial \sigma$ is a finite alternating sum of $p+1$ faces, so $\partial$ takes finite sums to finite sums — extending $\partial$ to infinite sums would force us to handle convergence questions, which are unwelcome in a purely algebraic theory. Second, the homology of a space is a topological invariant of a "local-to-global" character — every homology class is represented by a chain with compact support, since every cycle is built from finitely many simplices each with compact image. Allowing infinite chains would either give a different (and less useful) theory, or would have to be controlled by support conditions that complicate the formalism.

The choice of *free* abelian group, rather than some quotient, is also important. We do *not* identify two simplices that are reparameterisations of each other, or that have the same image. The free abelian group on the set of singular simplices treats every distinct continuous map $\sigma : \Delta^p \to M$ as a distinct generator. This is the right level of freedom: the *homology* (after quotienting cycles by boundaries) ends up identifying things that should be identified — homotopic simplices give homologous chains — but the chain complex itself is wildly redundant before the quotient.

---

# The Definition

Let $M$ be a topological space, $G$ an abelian group, and $p \geq 0$ an integer. A **singular $p$-chain** in $M$ with coefficients in $G$ is a finite formal $G$-linear combination of singular $p$-simplices,
$$
c \;=\; g_1 \sigma_1 + g_2 \sigma_2 + \cdots + g_r \sigma_r,
$$
where each $\sigma_i : \Delta^p \to M$ is a [[Def - Singular Simplex|singular $p$-simplex]] and each $g_i \in G$. Equivalently, a singular $p$-chain is a function $c : \{\text{singular $p$-simplices}\} \to G$ that takes the value $0$ except on finitely many simplices.

Two chains are added termwise:
$$
\left(\sum_i g_i \sigma_i\right) + \left(\sum_i g_i' \sigma_i\right) \;=\; \sum_i (g_i + g_i') \sigma_i,
$$
with the addition on the right taking place in $G$. (We may always pad either sum with zero terms to use the same indexing.)

The set of all singular $p$-chains is an abelian group under termwise addition, denoted
$$
C_p(M; G) \;=\; \bigoplus_{\sigma : \Delta^p \to M} G \cdot \sigma \;\cong\; G^{(\text{singular $p$-simplices})},
$$
the **singular $p$-chain group**. It is the free $G$-module on the set of singular $p$-simplices. By convention $C_p(M; G) = 0$ for $p < 0$.

When $G = K$ is a field, $C_p(M; K)$ is a $K$-vector space. It is always infinite-dimensional (as long as $M$ has infinitely many singular $p$-simplices, which is true for any non-empty $M$ when $p \geq 0$).

---

# Categorical / Structural Definition

The singular chain group $C_p$ is the free $G$-module functor applied to the set of singular $p$-simplices. Formally, let $\mathrm{Sing}_p : \mathbf{Top} \to \mathbf{Set}$ be the functor assigning to a space $M$ the set $\mathrm{Sing}_p(M) = \mathrm{Maps}(\Delta^p, M)$ of singular $p$-simplices. Let $F_G : \mathbf{Set} \to \mathbf{Ab}$ (or to $G$-$\mathbf{Mod}$) be the free-abelian-group functor with coefficients in $G$. Then
$$
C_p(-; G) \;=\; F_G \circ \mathrm{Sing}_p : \mathbf{Top} \to G\text{-}\mathbf{Mod}.
$$

This makes $C_p(-; G)$ a covariant functor: a continuous map $f : M \to N$ induces the chain map $f_\# : C_p(M; G) \to C_p(N; G)$ sending $g \cdot \sigma$ to $g \cdot (f \circ \sigma)$. The categorical interpretation makes the universal property of $C_p$ transparent: a homomorphism from $C_p(M; G)$ to any abelian group $A$ is the same as a function from singular simplices to $A$. This is what makes the boundary operator $\partial$ definable — it is just the extension of "boundary of a simplex" from singular simplices to chains by linearity.

---

# Relate to Other Fields / Compression

A singular $p$-chain is a **finitely-supported $G$-valued function on the set of singular $p$-simplices**. It is exactly the same algebraic object as a formal $\mathbb{Z}$-linear combination of vectors in linear algebra, or a divisor on an algebraic variety: a finite formal sum with coefficients.

The construction "free abelian group on a set" is one of the most reusable in algebra. It appears as: the **free $\mathbb{Z}$-module on a set** in module theory; **formal divisors** on an algebraic variety (where the underlying set is the set of irreducible subvarieties); **formal linear combinations of currents** in geometric measure theory; **multisets** in combinatorics; **formal sums of conjugacy classes** in representation theory; **the Burnside ring** of a group, built from finite $G$-sets. In every case, the algebraic move is the same: take a set of "atomic objects," form all finite linear combinations with coefficients in a chosen ring or group, and use the resulting algebraic structure to do calculations.

**True name:** a singular chain is a **formal finite sum** of singular simplices with coefficients in $G$. The word "formal" is key: we are not actually combining the simplices into a single geometric object (that would require some notion of gluing or addition of continuous maps), but recording them in a list with bookkeeping coefficients. The chain $\sigma_1 + \sigma_2 - \sigma_3$ is just the data "$\sigma_1$ with weight $1$, $\sigma_2$ with weight $1$, $\sigma_3$ with weight $-1$."

---

# Examples / Corollaries

**Is an instance: a single simplex with unit coefficient.** Every singular $p$-simplex $\sigma$ defines a $p$-chain $1 \cdot \sigma$ (just $\sigma$ with coefficient $1 \in G$). When the coefficient is clear we write just $\sigma$ for the chain. Most explicit cycles encountered in computations look like this — a single named simplex.

**Is an instance: the standard simplex as a chain in itself.** $\Delta^p \in C_p(\Delta^p; \mathbb{Z})$ — the identity map $\mathrm{id} : \Delta^p \to \Delta^p$ is a singular $p$-simplex in the space $\Delta^p$, and viewed as a chain with coefficient $1$ it is a generator of $C_p(\Delta^p; \mathbb{Z})$. Its boundary is the alternating sum of the $p+1$ faces.

**Is an instance: a fundamental class of a triangulated surface.** For the $2$-torus $T^2$, the triangulation into eighteen oriented triangles (Frankel Figure 13.12) gives a chain $[T^2] = \sum_{i=1}^{18} \tau_i \in C_2(T^2; \mathbb{Z})$, where the $\tau_i$ are the eighteen singular $2$-simplices. This chain represents the **fundamental class** of the torus; its boundary is zero, certifying that $T^2$ is orientable.

**Is an instance: a real-coefficient chain.** $c = (1/2) \sigma_1 + (-\pi) \sigma_2 \in C_2(M; \mathbb{R})$ is a perfectly valid real chain. Real coefficients allow us to take linear combinations of cycles in the homology vector space $H_p(M; \mathbb{R})$ — this is what lets the de Rham pairing $\int_c \omega$ produce arbitrary real numbers.

**Is NOT an instance: an infinite sum.** The "chain" $\sigma_1 + \sigma_2 + \sigma_3 + \cdots$ summing over countably many simplices is *not* a singular chain — the definition requires finite support. Allowing infinite sums would yield a different (and topologically different) theory; the finiteness is built into the algebra.

**Is NOT an instance: an embedded submanifold.** A submanifold $N \subseteq M$ is not by itself a singular chain — it lacks a triangulation. To convert it into a singular chain, one chooses a triangulation $K$ of $N$ and pre-composes with the inclusion to get a sum of singular simplices $\sum_\tau (i \circ \tau) \in C_p(M; \mathbb{Z})$. Different triangulations give different chains, but the homology class is the same.

**Corollary (chain groups form a chain complex).** The chain groups $C_\bullet(M; G) = \{C_p(M; G)\}_{p \geq 0}$ together with the boundary operators $\partial : C_p \to C_{p-1}$ form a **chain complex** in the category of abelian groups (or $G$-modules). Specifically, $\partial \circ \partial = 0$ ([[Thm - d-Squared-is-Zero for Singular Boundaries]]), so the kernels of $\partial$ contain the images of $\partial$, and the quotient $\ker \partial / \mathrm{im}\,\partial$ makes sense.

**Corollary (functoriality).** A continuous map $f : M \to N$ induces a chain map $f_\# : C_p(M; G) \to C_p(N; G)$ for every $p$, defined by $f_\#(\sum g_i \sigma_i) = \sum g_i (f \circ \sigma_i)$. This commutes with $\partial$ (because boundaries are built from compositions with face maps, which commute with post-composition), so $f_\#$ descends to homology $f_* : H_p(M; G) \to H_p(N; G)$. Composition: $(g \circ f)_\# = g_\# \circ f_\#$ and $\mathrm{id}_\# = \mathrm{id}$, making $C_p(-; G)$ a functor.

**Corollary (the chain group is uncountable for non-trivial $M$).** As long as $M$ has more than one point (so there are uncountably many continuous maps $\Delta^p \to M$ for any $p \geq 0$), the chain group $C_p(M; G)$ is uncountable as a set. Yet $H_p(M; G)$ can be finitely generated (e.g. for compact $M$). The dramatic compression from chains to homology is the central computational fact about singular homology.

**Calibration check.** If you understand the definition you should be able to: (1) explain why the sum of two singular $2$-chains is a single singular $2$-chain (not two separate things); (2) describe explicitly the boundary of $2\sigma_1 - \sigma_2$ in terms of the boundaries $\partial \sigma_1$ and $\partial \sigma_2$; (3) verify that $C_p(M; G) = 0$ for any $p < 0$, and that $C_0(M; G)$ is the free $G$-module on the set of points of $M$ (since a singular $0$-simplex $\Delta^0 \to M$ is just a choice of point in $M$).

---

# Unlocked by This

> [!tip] The Singular Chain Complex *(from Algebraic Topology — this same topic)*
> The collection $C_\bullet(M; G) = \{C_p(M; G), \partial_p\}_{p \geq 0}$ is a **chain complex**: a sequence of abelian groups with boundary maps $\partial^2 = 0$. The homology of this chain complex is the **singular homology** $H_p(M; G)$ — see [[Def - Singular Homology]]. Every later construction in the chapter (cycles, boundaries, homology classes, the de Rham pairing) is built from this chain complex.

> [!tip] Cellular Chain Complex *(from Algebraic Topology)*
> For a **CW complex** $X$, the cellular chain group $C_p^{\mathrm{CW}}(X) = \mathbb{Z}^{\#p\text{-cells}}$ is a *much* smaller free abelian group: one generator per $p$-cell, rather than one per continuous map $\Delta^p \to X$. The cellular boundary uses incidence numbers between cells, and the resulting cellular homology agrees with singular homology by a theorem of J.H.C. Whitehead. This makes explicit computation of $H_*(\mathbb{CP}^n)$, $H_*(\mathbb{RP}^n)$, $H_*(\text{Grassmannian})$ tractable.

> [!tip] Simplicial Chains for a Triangulated Space *(from Combinatorial Topology)*
> For a triangulated space, the **simplicial chain group** uses only the finitely many simplices of the triangulation as generators, not all singular simplices. The simplicial homology agrees with the singular homology by [[Thm - Singular and Simplicial Homology Agree on Triangulable Spaces]]. The simplicial chain complex is finite-dimensional in each degree, making linear algebra (Gaussian elimination, computation of kernels and images) directly applicable.
