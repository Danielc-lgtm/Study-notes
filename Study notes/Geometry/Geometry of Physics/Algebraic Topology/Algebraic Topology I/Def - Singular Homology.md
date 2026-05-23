---
type: definition
subject: algebraic-topology
prereqs:
  - "Def - Singular Chain"
  - "Def - The Boundary Operator"
  - "Def - Quotient Group"
  - "Def - Kernel and Image"
tags: [geometry, algebraic-topology, homology]
---

# Notation

$M$ is a topological space, $G$ an abelian coefficient group, $p \geq 0$ an integer.

- $C_p(M; G)$ — the [[Def - Singular Chain|singular $p$-chain group]].
- $\partial : C_p \to C_{p-1}$ — the [[Def - The Boundary Operator|boundary operator]], satisfying $\partial^2 = 0$.
- $Z_p(M; G) = \ker(\partial : C_p \to C_{p-1})$ — the group of **$p$-cycles**.
- $B_p(M; G) = \mathrm{im}(\partial : C_{p+1} \to C_p)$ — the group of **$p$-boundaries**.
- $H_p(M; G) = Z_p / B_p$ — the **$p$-th singular homology group**.
- $[z] \in H_p(M; G)$ — the homology class of a cycle $z$. Two cycles $z, z'$ are **homologous** ($z \sim z'$) if $z - z' \in B_p$.
- $f_* : H_p(M; G) \to H_p(N; G)$ — the homomorphism induced by a continuous map $f : M \to N$.

---

# Axiom Motivation

We have built the singular chain complex $(C_\bullet(M; G), \partial)$ with $\partial^2 = 0$. The single most important thing to do with a chain complex is to compute its **homology** — the failure of the sequence to be exact, measured at each spot. This gives a sequence of abelian groups $\{H_p\}_{p \geq 0}$ that captures the topological invariants of $M$.

Why the specific construction $H_p = \ker \partial / \mathrm{im}\, \partial$? Two demands force it.

First, **we want to capture "$p$-dimensional things in $M$ that have no boundary," modulo "things that are already a boundary of one dimension higher."** The cycle group $Z_p = \ker \partial$ consists of chains with vanishing boundary — these are the candidate "closed" $p$-dimensional pieces, the things that look like closed surfaces, closed loops, closed manifolds-without-boundary embedded in $M$. The boundary group $B_p = \mathrm{im}\, \partial$ consists of chains that arise as the boundary of something one dimension higher — these are the "obviously trivial" cycles, the ones that bound. The quotient $Z_p / B_p$ is exactly the group of cycles up to homology — non-trivial $p$-dimensional structures in $M$, identified when they differ by a boundary.

Why is "modulo boundaries" the right equivalence? Because intuitively, if a cycle $z$ bounds something — if $z = \partial b$ for some $(p+1)$-chain $b$ — then $z$ "wraps around" the $(p+1)$-dimensional region $b$ rather than around any "hole" in $M$. The cycle is unwrapped by the chain $b$, and so it should not count as a non-trivial topological feature. The quotient $H_p$ identifies all such "unwrapped" cycles to zero, leaving only the cycles that really do wrap around holes.

Second, **the quotient must be well-defined.** For $H_p = Z_p / B_p$ to make sense as an abelian group, $B_p$ must be a subgroup of $Z_p$ — every boundary must be a cycle. This is precisely the consequence of $\partial^2 = 0$: if $b = \partial c$, then $\partial b = \partial \partial c = 0$, so $b \in \ker \partial = Z_p$. Without $\partial^2 = 0$ the construction would not even be meaningful as a quotient of groups, and there would be no homology theory. This is why $\partial^2 = 0$ is the *axiom* of chain complexes — it is the minimum requirement that makes the homology quotient well-defined.

What information does $H_p$ carry? The dimension of $H_p(M; \mathbb{R})$ — the [[Def - Betti Numbers|Betti number]] $b_p$ — counts the number of independent $p$-dimensional "holes" in $M$. For $S^1$: $b_0 = 1$ (one component), $b_1 = 1$ (one independent loop), $b_p = 0$ for $p \geq 2$. For $S^2$: $b_0 = 1$, $b_1 = 0$ (no loops survive — every loop on the sphere bounds a disk), $b_2 = 1$ (one independent void). For $T^2$: $b_0 = 1$, $b_1 = 2$ (two independent loops, the meridian and the longitude), $b_2 = 1$. The pattern: $H_p$ encodes the "$p$-dimensional holes" in a way that is invariant under continuous deformation.

Why does the construction give a *topological* invariant? Because the boundary operator $\partial$ is natural with respect to continuous maps: $f_\# \partial = \partial f_\#$. This means $f_\#$ carries cycles to cycles and boundaries to boundaries, hence descends to a well-defined map $f_* : H_p(M; G) \to H_p(N; G)$ on homology. Functoriality $(f \circ g)_* = f_* g_*$ then makes $H_p$ a covariant functor $\mathbf{Top} \to \mathbf{Ab}$. Homeomorphisms induce isomorphisms on $H_p$, so homeomorphic spaces have isomorphic homology. The deeper fact — [[Thm - Homotopy Invariance of Singular Homology|homotopy invariance]] — says even homotopy equivalent spaces have isomorphic homology, making $H_p$ an invariant of homotopy type rather than just homeomorphism type.

What about coefficient groups? The freedom to choose $G$ is built into the definition. With $G = \mathbb{Z}$, the homology $H_p(M; \mathbb{Z})$ is the most refined: it sees both the free rank (Betti numbers) and the torsion. With $G = \mathbb{R}$ (or any field of characteristic zero), torsion vanishes — by the universal coefficient theorem, $H_p(M; \mathbb{R}) = H_p(M; \mathbb{Z}) \otimes \mathbb{R}$, so we only see the free part. With $G = \mathbb{Z}/p\mathbb{Z}$, we see $p$-torsion and free parts modulo $p$ — useful for detecting subtle algebraic structures. The general principle: $\mathbb{Z}$-homology is universal, and other coefficient choices project out specific information.

---

# The Definition

Let $M$ be a topological space, $G$ an abelian group, $p \geq 0$ an integer.

The **group of singular $p$-cycles** is
$$
Z_p(M; G) \;=\; \ker(\partial : C_p(M; G) \to C_{p-1}(M; G)) \;=\; \{c \in C_p(M; G) : \partial c = 0\}.
$$

The **group of singular $p$-boundaries** is
$$
B_p(M; G) \;=\; \mathrm{im}(\partial : C_{p+1}(M; G) \to C_p(M; G)) \;=\; \{\partial b : b \in C_{p+1}(M; G)\}.
$$

By $\partial \circ \partial = 0$, every boundary is a cycle: $B_p \subseteq Z_p$.

The **$p$-th singular homology group** of $M$ with coefficients in $G$ is the quotient
$$
H_p(M; G) \;=\; Z_p(M; G) / B_p(M; G).
$$

Two cycles $z, z' \in Z_p(M; G)$ are **homologous** if $z - z' \in B_p$ (i.e. their difference is a boundary), written $z \sim z'$. The **homology class** of $z$ is the equivalence class $[z] = z + B_p \in H_p(M; G)$.

When $G = K$ is a field, $Z_p$, $B_p$, and $H_p$ are all $K$-vector spaces, with $H_p$ finite-dimensional when $M$ is a compact manifold (or more generally a finite CW complex).

For a continuous map $f : M \to N$, the induced chain map $f_\# : C_p(M; G) \to C_p(N; G)$ commutes with $\partial$, hence carries $Z_p(M) \to Z_p(N)$ and $B_p(M) \to B_p(N)$, hence descends to the **induced map on homology**
$$
f_* : H_p(M; G) \to H_p(N; G), \qquad f_*[z] = [f_\# z].
$$
This assignment is functorial: $(g \circ f)_* = g_* \circ f_*$ and $\mathrm{id}_* = \mathrm{id}$.

---

# Categorical Definition

Singular homology in degree $p$ is the composite of three functors:
$$
H_p \;=\; H_p(C_\bullet) \;\circ\; C_\bullet(-; G) \;\circ\; \mathrm{Sing} \;:\; \mathbf{Top} \to \mathbf{Ab},
$$
where:

1. $\mathrm{Sing} : \mathbf{Top} \to \mathbf{sSet}$ is the **singular simplicial set** functor, sending $M$ to the simplicial set $\mathrm{Sing}(M)$ with $\mathrm{Sing}(M)_p = \mathrm{Maps}(\Delta^p, M)$.
2. $C_\bullet(-; G) : \mathbf{sSet} \to \mathbf{Ch}(\mathbf{Ab})$ is the **free $G$-module on a simplicial set** functor, with the boundary operator induced by the alternating sum of face maps.
3. $H_p : \mathbf{Ch}(\mathbf{Ab}) \to \mathbf{Ab}$ is the **$p$-th homology of a chain complex** functor, sending $(C_\bullet, \partial)$ to $\ker \partial_p / \mathrm{im}\, \partial_{p+1}$.

Each step is functorial in the appropriate sense, and the composition gives the functor
$$
H_p(-; G) \;:\; \mathbf{Top} \to \mathbf{Ab}.
$$

This is a **covariant functor**: a continuous map $f : M \to N$ in $\mathbf{Top}$ induces a homomorphism $f_* : H_p(M; G) \to H_p(N; G)$ in $\mathbf{Ab}$, and this assignment respects composition and identities. Singular homology is therefore an object of the functor category $[\mathbf{Top}, \mathbf{Ab}]$.

By the **Eilenberg–Steenrod axioms**, singular homology is the unique (up to natural isomorphism) functor $\mathbf{Top} \to \mathbf{Ab}$ satisfying five axioms: (i) homotopy invariance — homotopic maps induce equal homology maps; (ii) the long exact sequence of a pair $(X, A)$; (iii) excision — removing a "small" subset of $A$ from both $X$ and $A$ does not change $H_*(X, A)$; (iv) additivity — homology of a disjoint union is the direct sum of the homologies; (v) the dimension axiom — $H_p(\text{point}) = G$ for $p = 0$ and zero for $p > 0$.

This characterisation reveals singular homology as the "ordinary" homology theory: any other functor satisfying the same five axioms agrees with singular homology on CW complexes. Dropping the dimension axiom and allowing $H_*(\text{point})$ to be any graded abelian group gives the more general notion of a **generalised homology theory** — K-theory, cobordism, stable homotopy — which take values in graded abelian groups beyond the singular case.

---

# Relate to Other Fields / Compression

Singular homology is the **abelianisation of homotopy theory**, dimension-stratified. The Hurewicz theorem makes this precise in the first non-zero degree: for simply connected $M$, $H_n(M; \mathbb{Z}) = \pi_n(M)$ when $n$ is the first non-trivial dimension. Above that, $H_p$ continues to detect "$p$-dimensional sphere-like things in $M$ up to filling," in the abelianised world of formal sums.

In differential geometry, singular homology with real coefficients is the **dual of de Rham cohomology** by the de Rham theorem: $H_p(M; \mathbb{R}) \cong H^p_{dR}(M)^*$, with the pairing being integration $\int_c \omega$. So $H_p(M; \mathbb{R})$ can be computed by smooth-form methods, and the Betti numbers $b_p$ are the dimensions of either side.

In algebraic geometry, singular cohomology of complex projective varieties decomposes by Hodge type into $H^{p,q}$ pieces, refining the Betti numbers into the more sensitive **Hodge numbers**. The Hodge decomposition is one of the deepest theorems in complex algebraic geometry, and it relies on identifying singular cohomology with de Rham cohomology to bring in the complex structure.

In mathematical physics, integer-valued topological charges (winding numbers, Chern numbers, instanton numbers) are pairings of integer cohomology classes against integer homology cycles — the integrality of the charge is exactly the statement that the relevant cohomology class lifts from $H^*(M; \mathbb{R})$ to $H^*(M; \mathbb{Z})$.

**True name:** singular homology is the **dimension-stratified count of cycles up to bounding** in $M$. The textbook formula $H_p = Z_p / B_p$ is the right computational definition, but the meaning is: "how many independent $p$-dimensional closed objects sit inside $M$, after we declare two equivalent when one is the boundary of one dimension up." The Betti numbers count these for each $p$; the full integer homology refines them by detecting torsion.

---

# Examples / Corollaries

**$H_*(\text{point})$.** The chain complex of a point has one singular $p$-simplex in each degree (the constant map), and the boundary maps alternate between $0$ (odd $p$) and the identity (even $p \geq 2$). The homology is
$$
H_p(\text{point}; G) = \begin{cases} G & p = 0 \\ 0 & p \geq 1. \end{cases}
$$
A point has no $p$-dimensional holes for $p \geq 1$, and one connected component in degree zero.

**$H_*(\mathbb{R}^n)$.** Euclidean space is contractible (homotopy equivalent to a point), so by [[Thm - Homotopy Invariance of Singular Homology|homotopy invariance]] $H_p(\mathbb{R}^n; G) = H_p(\text{point}; G)$, which is $G$ in degree zero and zero elsewhere.

**$H_*(S^n)$.** The $n$-sphere has $H_0 = G$, $H_n = G$, and $H_p = 0$ for $p \neq 0, n$ (see [[Thm - Singular Homology of the Sphere]]). The generator of $H_n(S^n; \mathbb{Z}) = \mathbb{Z}$ is the **fundamental class** $[S^n]$, the standard orientation cycle.

**$H_*(T^n)$.** The $n$-torus has $H_k(T^n; G) = G^{\binom{n}{k}}$ for $0 \leq k \leq n$, generated by products of the basic $1$-cycles. The Betti numbers are $b_k = \binom{n}{k}$ and the Euler characteristic is $\chi(T^n) = 0$ for $n \geq 1$.

**$H_*(\mathbb{RP}^n; \mathbb{Z})$.** Integer homology of real projective space is sensitive to parity: $H_0 = \mathbb{Z}$, $H_n = \mathbb{Z}$ if $n$ odd or $\mathbb{Z}/2$ in degree $n-1$ if $n$ even (due to non-orientability), $H_k = \mathbb{Z}/2$ for odd $k$ with $1 \leq k < n$, zero in even positive degrees. With $\mathbb{R}$ coefficients, all the $\mathbb{Z}/2$ torsion vanishes, leaving $\mathbb{R}$ in degrees $0$ and (when odd) $n$, zero elsewhere — $\mathbb{RP}^n$ has the same Betti numbers as a point for even $n$ and as $S^n$ for odd $n$.

**$H_*(\mathbb{CP}^n; \mathbb{Z})$.** Complex projective space has $H_{2k}(\mathbb{CP}^n; \mathbb{Z}) = \mathbb{Z}$ for $0 \leq k \leq n$ and zero in odd degrees. Betti numbers $b_{2k} = 1$ for $0 \leq k \leq n$, all odd Betti numbers zero. The generator of $H_{2k}$ is the class of an embedded $\mathbb{CP}^k \subset \mathbb{CP}^n$.

**Is NOT an instance: $H_*$ as a homotopy classification.** $H_*(M) \cong H_*(N)$ does *not* force $M \simeq N$. The lens spaces $L(7, 1)$ and $L(7, 2)$ have isomorphic homology in all degrees but are not homotopy equivalent — they are distinguished by the cup product structure on cohomology, or equivalently by the linking form on torsion homology.

**Corollary ($H_0$ counts components).** For any space $M$, $H_0(M; G) = G^{\#\text{path components}}$. A path component contributes one copy of $G$, generated by any point in that component. So $b_0 =$ number of path components.

**Corollary ($H_p = 0$ above dimension).** For an $n$-dimensional CW complex (or a topological $n$-manifold), $H_p(M; G) = 0$ for $p > n$ — there are no cells of dimension higher than $n$ to support non-trivial cycles. For singular homology, this requires some care (one has to use a triangulation), but the conclusion holds.

**Corollary (top homology and orientability).** For a closed connected $n$-manifold $M$:
$$
H_n(M; \mathbb{Z}) = \begin{cases} \mathbb{Z} & M \text{ orientable} \\ 0 & M \text{ non-orientable}. \end{cases}
$$
The generator (when non-zero) is the **fundamental class** $[M]$. With $\mathbb{Z}/2$ coefficients, $H_n(M; \mathbb{Z}/2) = \mathbb{Z}/2$ for every closed connected $n$-manifold, orientable or not — the $\mathbb{Z}/2$ fundamental class always exists.

**Corollary (homology is a homotopy invariant).** By [[Thm - Homotopy Invariance of Singular Homology|homotopy invariance]], if $f : M \to N$ is a homotopy equivalence, then $f_* : H_*(M; G) \to H_*(N; G)$ is an isomorphism. Consequently, $H_*(M; G) \cong H_*(N; G)$ whenever $M$ and $N$ are homotopy equivalent. The converse fails: there exist non-homotopy-equivalent spaces with the same homology in all degrees.

**Calibration check.** If you have understood the definition you should be able to: (1) compute $H_0(M; G)$ for a discrete space $M = \{p_1, p_2, p_3\}$ of three points; (2) explain why $H_n(\mathbb{R}^n; G) = 0$ for $n \geq 1$ (despite $\mathbb{R}^n$ being $n$-dimensional); (3) identify the generators of $H_1(T^2; \mathbb{Z}) = \mathbb{Z}^2$ as the meridian and longitude loops.

---

# Unlocked by This

> [!tip] Betti Numbers and Euler Characteristic *(from Algebraic Topology — this same topic)*
> The dimensions $b_p = \dim_\mathbb{R} H_p(M; \mathbb{R})$ are the **Betti numbers**, the central numerical topological invariants of $M$. Their alternating sum $\chi(M) = \sum_p (-1)^p b_p$ is the **Euler characteristic**, the most-used single-number invariant. See [[Def - Betti Numbers]] and [[Def - Euler Characteristic]].

> [!tip] Singular Cohomology *(from Algebraic Topology — this same topic)*
> Dualising via $\mathrm{Hom}(-, G)$ gives **singular cohomology** $H^p(M; G)$. Over a field, $H^p(M; K) = \mathrm{Hom}_K(H_p(M; K), K)$ — the dual vector space. Cohomology has an additional structure not visible to homology: the **cup product** makes $H^*(M; G)$ into a graded-commutative ring. See [[Def - Singular Cohomology]].

> [!tip] The de Rham Theorem *(from Algebraic Topology / Differential Geometry)*
> For smooth manifolds, singular cohomology with real coefficients agrees with de Rham cohomology: $H^p(M; \mathbb{R}) \cong H^p_{dR}(M)$. The isomorphism is given by integration of forms against cycles. This is the bridge between the topological invariants computed here and the smooth-form invariants from `Differential Geometry X`. See [[Thm - The de Rham Theorem (Full Proof)]].

> [!tip] Eilenberg–Steenrod Axioms *(from Algebraic Topology)*
> Singular homology is the unique homology theory on $\mathbf{Top}$ satisfying five axioms (homotopy invariance, long exact sequence of a pair, excision, additivity, dimension). Any "ordinary" homology theory — cellular, simplicial, Čech — satisfies all five and is therefore naturally isomorphic to singular homology on CW complexes. Dropping the dimension axiom gives generalised homology theories like **K-theory** and **cobordism**.

> [!tip] **Hurewicz Theorem and the Relation to Homotopy** *(from Algebraic Topology)*
> The **Hurewicz theorem** relates homology to homotopy: for a simply connected space, the first non-zero homotopy group $\pi_n(M)$ is isomorphic to the first non-zero homology group $H_n(M; \mathbb{Z})$. Above $n$, the two diverge — homology is "abelianised homotopy" and loses non-abelian information. The map $\pi_n(M) \to H_n(M; \mathbb{Z})$ — the **Hurewicz homomorphism** — sends a homotopy class $[f : S^n \to M]$ to the homology class $f_*[S^n]$.

> [!tip] **Poincaré Duality** *(from Algebraic Topology)*
> For a compact oriented $n$-manifold $M$, the cap product with the fundamental class $[M] \in H_n(M; \mathbb{Z})$ gives an isomorphism $H^k(M; G) \cong H_{n-k}(M; G)$ — **Poincaré duality**. The Betti-number version is $b_k = b_{n-k}$, the "palindrome" property visible in the Betti polynomials of $S^n$, $T^n$, $\mathbb{CP}^n$. Poincaré duality is the topological avatar of Hodge duality $\star : \Omega^k \to \Omega^{n-k}$ on a Riemannian manifold (see [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition]]).
