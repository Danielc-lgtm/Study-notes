---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Principal G-Bundle"
  - "Def - Lie Group"
  - "Def - Homogeneous Space"
  - "Def - Smooth Action of a Lie Group"
tags: [geometry, gauge-theory, homogeneous-spaces, principal-bundles]
---

# Notation

A **homogeneous bundle** is a principal $H$-bundle of the form $H \to G \to G/H$, where $H$ is a closed Lie subgroup of a Lie group $G$. The coset space is written $G/H$ and consists of left cosets $gH = \{gh : h \in H\}$. The projection $\pi : G \to G/H$ sends $g \mapsto [g] = gH$. The right $H$-action on $G$ is right multiplication $(g, h) \mapsto gh$. See [[Gauge Theory II — Fibre Bundles, Principal Bundles, and Gauss–Bonnet]] for the registry and [[Def - Homogeneous Space]] for the underlying coset construction.

---

# Axiom Motivation

The homogeneous-bundle construction is the **simplest, most automatic way to manufacture principal bundles**: take any Lie group $G$ and any closed Lie subgroup $H$, and the right $H$-action on $G$ by right multiplication is automatically free, fibre-preserving, and produces a smooth principal $H$-bundle $G \to G/H$. No extra data, no constructions, no hypotheses beyond closedness of $H$. The dual significance: every coset space $G/H$ comes with a natural principal $H$-bundle structure over it, and most "named" manifolds in geometry (spheres, projective spaces, Grassmannians, Stiefel manifolds, flag manifolds, symmetric spaces) are coset spaces of compact Lie groups, hence all carry natural principal bundles.

Why is the right action of $H$ on $G$ automatically **free**? If $gh = g$ for some $g \in G$ and $h \in H$, then group cancellation gives $h = e$. This is the only freeness condition needed for a right group action to define a principal bundle, and it is automatic for any group acting on itself by multiplication. The point is that the group cancellation property (left or right) of any group is exactly the freeness of left or right translation by group elements — a structural feature of groups, not an additional axiom we need to verify.

Why is the **quotient smooth** when $H$ is closed? This is Frankel Theorem 17.11 (a version of the Cartan / quotient manifold theorem): for a Lie group $G$ and a closed Lie subgroup $H$, the coset space $G/H$ has a unique smooth manifold structure of dimension $\dim G - \dim H$ such that the quotient map $\pi : G \to G/H$ is a smooth submersion. The closedness of $H$ is essential: if $H$ is dense (e.g., an irrational winding in the torus), the quotient is non-Hausdorff and not a manifold. The proof uses a "transverse slice" $V \subset G$ at the identity, with $V$ complementary to $H$ and small enough that each coset $gH$ either misses $V$ or hits it once — closedness of $H$ is exactly what makes the local "miss or one hit" property hold for small enough $V$.

Why does this make $G \to G/H$ a **principal $H$-bundle**? Three checks. First, the fibre over $[g] \in G/H$ is the coset $gH = \{gh : h \in H\}$, which is diffeomorphic to $H$ via $h \mapsto gh$ — i.e., diffeomorphic to the structure group. Second, the right $H$-action on $G$ is fibre-preserving: $\pi(gh) = [gh] = [g] = \pi(g)$. Third, local triviality follows from the transverse-slice construction: in a small neighborhood of any coset, choose a slice $V$ transverse to $H$, and the map $V \times H \to G$, $(v, h) \mapsto vh$, is a local diffeomorphism onto a neighborhood of the coset, providing a local trivialization of $G$ over a neighborhood of the corresponding point in $G/H$.

The connection to the **associated-bundle construction** is essential: every $H$-representation $\rho : H \to \mathrm{GL}(V)$ gives a vector bundle $G \times_H V \to G/H$, the **induced bundle**. Conversely, every $G$-equivariant vector bundle over $G/H$ arises this way (for some $H$-representation $V$). So the entire representation theory of $H$ becomes the bundle theory over $G/H$, and questions about $G$-equivariant differential operators, sections, harmonic analysis on $G/H$ all reduce to representation theory of $H$.

What would go wrong if we **dropped closedness of $H$**? The quotient might fail to be Hausdorff, hence not a manifold; the bundle structure would not exist. The standard counterexample: $G = \mathbb{T}^2$, $H = \{(t, \alpha t) : t \in \mathbb{R}\}$ with $\alpha$ irrational. The subgroup $H$ is a dense 1-parameter subgroup, the quotient $\mathbb{T}^2/H$ is a non-Hausdorff "long line"-like object, and there is no principal-bundle structure.

---

# The Definition

Let $G$ be a Lie group and $H \leq G$ a **closed** Lie subgroup. The **homogeneous bundle** associated to $H \subseteq G$ is the principal $H$-bundle
$$H \to G \overset{\pi}{\to} G/H,$$
where:

- The **total space** is $G$, with its smooth manifold structure.
- The **base** is the coset space $G/H$, with the smooth structure of dimension $\dim G - \dim H$ guaranteed by Frankel Theorem 17.11 (the closed subgroup theorem / quotient manifold theorem).
- The **projection** $\pi : G \to G/H$ sends $g \mapsto gH$.
- The **typical fibre** is $H$ itself (each fibre $\pi^{-1}([g]) = gH$ is diffeomorphic to $H$).
- The **right $H$-action** is right multiplication $G \times H \to G$, $(g, h) \mapsto gh$. This is free, smooth, fibre-preserving, and transitive on fibres.
- **Local trivializations** come from local transverse slices: for any neighborhood $V$ of $e$ in $G$ that meets each coset $gH$ at most once (which exists by closedness of $H$), the map $V \times H \to G$, $(v, h) \mapsto vh$, is a diffeomorphism onto an open subset of $G$ projecting onto an open neighborhood $U \subset G/H$, giving the trivialization $G|_U \cong U \times H$.

More generally, a **homogeneous bundle** is any principal bundle of the form $G \to G/H$ for some closed $H \leq G$, or any associated bundle $G \times_H F \to G/H$ for a smooth $H$-action on $F$.

---

# Relate to Other Fields / Compression

The homogeneous-bundle construction is **the bundle-theoretic shadow of the closed subgroup theorem (Cartan)**: a closed subgroup is automatically embedded Lie, and the quotient automatically inherits a smooth structure. The principal bundle is the natural geometric object accompanying every closed-subgroup pair $(H, G)$.

A homogeneous bundle is also **the universal source of induced representations**: for a finite-dimensional $H$-representation $V$, the associated vector bundle $G \times_H V \to G/H$ carries the induced representation $\mathrm{Ind}_H^G V$ via the $G$-action $g \cdot [g', v] = [gg', v]$. Harmonic analysis on $G/H$ (i.e., the decomposition of $L^2(G/H)$ into $G$-irreducibles) is the decomposition of the induced representation $\mathrm{Ind}_H^G \mathbf{1}$, and Frobenius reciprocity governs the multiplicities.

The reduction-of-structure-group viewpoint: a principal $H$-bundle over a manifold $M$ is the same data as a section of the associated bundle $\mathrm{Fr}(TM) / H$, which is itself a fibre bundle with fibre $\mathrm{GL}(n)/H$ — i.e., the typical *homogeneous space* of the group quotient. So *every* $G$-structure (where $G = \mathrm{GL}(n)$, $H \leq G$) is a section of a bundle with homogeneous fibre. The classification of $G$-structures on $M$ is the classification of sections of these homogeneous bundles.

**True name:** a homogeneous bundle is **the principal bundle of a coset space, with the group acting on itself by right multiplication**. Operationally, whenever a manifold $M$ is presented as $G/H$ for a closed subgroup $H \leq G$, the principal $H$-bundle $G \to G/H = M$ is the natural source of all $G$-equivariant geometric structures on $M$.

---

# Examples / Corollaries

**Is an instance: $\mathrm{SO}(2) \to \mathrm{SO}(3) \to S^2$.** $\mathrm{SO}(3)$ acts transitively on $S^2$ by rotations, with stabilizer $\mathrm{SO}(2)$ at any point (the rotations fixing that axis). So $S^2 = \mathrm{SO}(3)/\mathrm{SO}(2)$, and the principal bundle is $\mathrm{SO}(3) \to S^2$ with fibre $\mathrm{SO}(2) \cong S^1$. This is also the orthonormal frame bundle of $S^2$ (cf. [[Def - Orthonormal Frame Bundle]]).

**Is an instance: $\mathrm{SO}(n) \to \mathrm{SO}(n+1) \to S^n$ for any $n$.** $S^n = \mathrm{SO}(n+1)/\mathrm{SO}(n)$.

**Is an instance: $U(n) \to U(n+1) \to S^{2n+1}$ (and the quotient $S^{2n+1}/U(1) = \mathbb{CP}^n$).** The unitary group acts transitively on the unit sphere of $\mathbb{C}^{n+1}$, with stabilizer $U(n)$; further quotient by $U(1)$ gives complex projective space.

**Is an instance: $U(1) \to S^3 \to S^2$, the Hopf bundle.** $S^3 = U(2)/U(1) = \mathrm{SU}(2)$ and $S^2 = \mathrm{SU}(2)/U(1)$; equivalently $\mathbb{CP}^1 = U(2)/(U(1) \times U(1)) = S^2$. See [[Def - The Hopf Bundle]].

**Is an instance: $\mathrm{O}(k) \times \mathrm{O}(n-k) \to \mathrm{O}(n) \to \mathrm{Gr}(k, n)$.** The Grassmannian of $k$-planes in $\mathbb{R}^n$, of dimension $k(n-k)$. The principal bundle expresses how $\mathrm{O}(n)$ acts transitively on the set of $k$-planes, with stabilizer $\mathrm{O}(k) \times \mathrm{O}(n-k)$ (rotations within the chosen $k$-plane and within its orthogonal complement). See [[Ex - The Grassmannian is a Smooth Manifold]] for the smooth structure.

**Is an instance: $\mathrm{O}(n-k) \to \mathrm{O}(n) \to V(k, n)$, the Stiefel manifold of $k$-frames in $\mathbb{R}^n$.** $V(k, n) = \mathrm{O}(n)/\mathrm{O}(n-k)$, of dimension $\sum_{j=n-k+1}^n j - 1 = nk - k(k+1)/2$. For $k = n$, $V(n, n) = \mathrm{O}(n)$ itself (all orthonormal frames); for $k = 1$, $V(1, n) = S^{n-1}$.

**Is an instance: the universal cover $\widetilde{G} \to G$ for a Lie group with nontrivial $\pi_1(G)$.** The universal cover is a principal $\pi_1(G)$-bundle (with discrete fibre), realizing $G = \widetilde{G}/\pi_1(G)$ as a homogeneous space of the universal cover. The example: $\mathrm{Spin}(n) \to \mathrm{SO}(n)$ is a principal $\mathbb{Z}/2$-bundle for $n \geq 3$, the universal double cover.

**Is NOT an instance: $\mathbb{T}^2 / H$ for $H$ an irrational dense 1-parameter subgroup.** The non-closed $H$ produces a non-Hausdorff quotient, not a smooth manifold, hence no principal bundle.

**Corollary (dimension formula).** $\dim(G/H) = \dim G - \dim H$. This makes coset spaces a primary source of manifolds of prescribed dimension.

**Corollary (every transitive $G$-action on a manifold $M$ exhibits $M$ as $G/H$).** Frankel's "Fundamental Principle 17.10": given a transitive action of $G$ on $M$ and a basepoint $x_0 \in M$, the stabilizer $H = \mathrm{Stab}(x_0)$ is a closed Lie subgroup of $G$, and $M \cong G/H$ via $g \mapsto g \cdot x_0$. So *every* homogeneous space is automatically a homogeneous bundle's base.

**Corollary (every $H$-representation gives an induced vector bundle on $G/H$).** The associated-bundle construction $V \mapsto G \times_H V$ converts $H$-representations into vector bundles on $G/H$. This is the bridge between representation theory and bundle geometry.

**Calibration check.** Verify (i) the dimension formula $\dim(G/H) = \dim G - \dim H$ for $S^2 = \mathrm{SO}(3)/\mathrm{SO}(2)$ (giving $3 - 1 = 2$); (ii) the right $H$-action on $G$ is free by group cancellation; (iii) the Grassmannian $\mathrm{Gr}(k, n)$ has the expected dimension $k(n-k)$.

---

# Unlocked by This

> [!tip] Induced Representation $\mathrm{Ind}_H^G$ *(from Lie Group Representation Theory)*
> Given an $H$-representation $V$, the **induced representation** $\mathrm{Ind}_H^G V$ is the space of sections of the associated vector bundle $G \times_H V \to G/H$, with the natural $G$-action by left translation. Frobenius reciprocity: $\mathrm{Hom}_G(\mathrm{Ind}_H^G V, W) = \mathrm{Hom}_H(V, \mathrm{Res}_H^G W)$, the algebraic reflection of the bundle-theoretic adjunction between induction (left adjoint) and restriction (right adjoint).

> [!tip] Symmetric Space *(from Riemannian Geometry / Lie Theory)*
> A **symmetric space** is a homogeneous space $G/H$ together with an involution $\sigma : G \to G$ (a Lie group automorphism with $\sigma^2 = \mathrm{id}$) such that $H$ is the fixed-point group of $\sigma$. Symmetric spaces inherit canonical $G$-invariant Riemannian metrics with parallel curvature, and the classification (Cartan) reduces to the classification of orthogonal involutions on real semisimple Lie algebras. Examples: $S^n = \mathrm{SO}(n+1)/\mathrm{SO}(n)$, $\mathbb{H}^n = \mathrm{SO}(n,1)^+/\mathrm{SO}(n)$, all the compact and noncompact simple Riemannian symmetric spaces.

> [!tip] Classifying Space via $EG = G$ for $G$ Contractible *(from Algebraic Topology)*
> For a Lie group $G$ with discrete topology, $BG = K(G, 1)$ and $EG$ is the universal cover of $BG$. For continuous $G$, $EG$ is a contractible space on which $G$ acts freely, and $BG = EG/G$. The geometry of $BG$ is what classifies principal $G$-bundles: $[M, BG] = \{$principal $G$-bundles on $M\}/\cong$. Homogeneous bundles $G \to G/H$ are the "model" examples that build $BG$ via the Milnor construction $BG = G * G * G * \cdots / G$ (join construction).
