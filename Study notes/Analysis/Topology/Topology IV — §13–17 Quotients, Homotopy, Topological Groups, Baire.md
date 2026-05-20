---
type: topic
subject: topology
chapter: "13-17"
title: "Topology IV — §13–17 Quotients, Homotopy, Topological Groups, Baire"
tags: [analysis, topology]
---

# Notation Registry

- $X, Y, Z$ — topological spaces
- $X/{\sim}$ — quotient of $X$ by an equivalence relation
- $X/A$ — quotient of $X$ by collapsing the subspace $A$ to a point
- $\pi : X \to X/{\sim}$ — the canonical projection
- $Y \cup_f X$ — adjunction space (attach $X$ to $Y$ along $f : A \to Y$ with $A \subseteq X$ closed)
- $M_f$ — mapping cylinder of $f : X \to Y$
- $C_f$ — mapping cone of $f : X \to Y$
- $X \vee Y$ — one-point (wedge) union
- $f \simeq g$ — $f$ and $g$ are homotopic (relative to $A$ if "rel A" is appended)
- $X \simeq Y$ — $X$ and $Y$ are homotopy equivalent (NOTE: this conflicts with the homeomorphism notation $\cong$ — Bredon uses $\simeq$ for homotopy equivalence and $\approx$ or $\cong$ for homeomorphism)
- $F : X \times I \to Y$ — a homotopy; $I = [0, 1]$
- $F * G$ — concatenation of two homotopies
- $G$ — a topological group
- $L_g, R_g$ — left/right translation by $g \in G$
- $e$ — identity element of a group
- $H \leq G, H \trianglelefteq G$ — subgroup, normal subgroup
- $G/H$ — quotient group (and quotient topological space when $G$ is a topological group)
- $C \subseteq \mathbb{R}^n$ — a convex body (closed convex set with interior assumed nonempty)
- $\operatorname{Sym}(X)$ — symmetric group on $X$
- $\operatorname{GL}_n(\mathbb{R}), \operatorname{O}(n), \operatorname{SO}(n), \operatorname{U}(n)$ — matrix groups
- "first category" / "meager" — a countable union of nowhere dense sets

---

# Motivation

§13–17 develop the *constructive* and *qualitative* sides of topology. §13–14 give the standard machinery for *building* spaces — quotients, attachments, mapping cylinders and cones, and the homotopy relation that puts maps and spaces into equivalence classes. §15 specializes to groups carrying a topology, the most important class of "spaces with extra structure" in geometry. §16 proves that compact convex bodies in $\mathbb{R}^n$ are homeomorphic to disks, the prototype "topological classification" result. §17 is the **Baire category theorem**, an existence result of a different kind — it produces points not in any of a countable collection of "small" sets, and is the engine of every genericity argument in functional analysis.

§13 introduces **quotient spaces**. Take a topological space $X$ and an equivalence relation $\sim$, form the set of equivalence classes $X/{\sim}$, and ask: what is the natural topology? The answer is the *finest* topology making the projection $\pi : X \to X/{\sim}$ continuous. Equivalently, a set $V \subseteq X/{\sim}$ is open iff $\pi^{-1}(V)$ is open in $X$. This is the quotient topology, and it has a universal property: a function $g : X/{\sim} \to Z$ is continuous iff $g \circ \pi$ is continuous. From this one builds: the torus as $\mathbb{R}^2/\mathbb{Z}^2$ (or as $[0,1]^2$ with edges glued), the projective plane as $S^2$ with antipodes identified (or as $D^2$ with boundary antipodes identified), the Klein bottle, the mapping cylinder $M_f = Y \sqcup (X \times I) / \sim$ where $(x, 0) \sim f(x)$. Quotient spaces are how one *builds* topology — every interesting space in the rest of the book is constructed by gluing pieces.

§14 introduces **homotopy**. Two maps $f_0, f_1 : X \to Y$ are *homotopic* (written $f_0 \simeq f_1$) if there is a continuous family of maps interpolating between them — a continuous $F : X \times I \to Y$ with $F(\cdot, 0) = f_0$ and $F(\cdot, 1) = f_1$. Homotopy is an equivalence relation on the set of maps $X \to Y$, and the equivalence classes are the homotopy classes $[X, Y]$. Two spaces are **homotopy equivalent** ($X \simeq Y$) if there are maps $f : X \to Y, g : Y \to X$ with $gf \simeq 1_X$ and $fg \simeq 1_Y$. Homotopy equivalence is the equivalence relation under which **algebraic topology** classifies spaces — much coarser than homeomorphism, but exactly captures the "shape" information that fundamental groups and homology see. A space is **contractible** if it is homotopy equivalent to a point; $\mathbb{R}^n$ is contractible, $S^n$ is not. This section is the gateway to the entire next chapter of Bredon and to algebraic topology in general.

§15 introduces **topological groups**: a group $G$ equipped with a topology such that multiplication $G \times G \to G$ and inversion $G \to G$ are continuous. Examples: $\mathbb{R}, \mathbb{Z}, S^1$ under their natural topologies, $\operatorname{GL}_n(\mathbb{R})$ as an open subset of $\mathbb{R}^{n^2}$, $\operatorname{O}(n), \operatorname{SO}(n), \operatorname{U}(n)$ as closed subspaces of matrix groups, every Lie group. The topology and the group structure interact: left and right translations are homeomorphisms, so the topology is *homogeneous* (every point looks like every other), the closure of a subgroup is a subgroup, the connected component of the identity is a closed normal subgroup. The interaction between algebra (subgroups, homomorphisms, quotients) and topology (closure, continuity, connectedness) makes topological groups exceptionally rigid and exceptionally well-behaved — every standard topological hypothesis (regular, Hausdorff, locally compact) is automatic given one of them.

§16 proves a single classification theorem: every **compact convex body** $C \subseteq \mathbb{R}^n$ with nonempty interior is homeomorphic to the closed unit disk $D^n$. The proof projects $C$ radially onto the unit sphere $S^{n-1}$ from an interior point; the radial map is a homeomorphism between the boundary $\partial C$ and $S^{n-1}$, which extends to a homeomorphism of $C$ with $D^n$. This is the prototype of a *classification by homeomorphism* — when the topology is rigid enough (compact, convex, full-dimensional), every example is homeomorphic to a canonical model. The theorem is the topological underpinning of every "all convex bodies behave the same" argument in convex analysis and optimization.

§17 is the **Baire category theorem**: in a complete metric space (or a locally compact Hausdorff space), the intersection of a countable family of dense open sets is dense. Equivalently, such a space is *not* a countable union of nowhere dense sets — it is *not* "meager" or "of first category". The theorem is a structural existence statement: given countably many "small" sets, one can always find a point outside them. The applications are profound — in functional analysis, the open mapping theorem and closed graph theorem rest on Baire; in dynamics, the generic property of an orbit holds on a residual set; in real analysis, "most" continuous functions are nowhere differentiable. The "third corollary" in Bredon notes the existence of a connected 2-manifold and of a continuous nowhere-differentiable function on $[0, 1]$ — both produced by Baire as the "generic" element of a complete metric space.

The unifying frame: **topology gives the language for both construction and classification**. §13–14 are about *building* spaces (quotients, attachments, mapping cylinders) and *equating* maps and spaces up to deformation (homotopy). §15 adds algebra to topology, generating examples and constraints. §16 classifies a specific class. §17 supplies the structural existence theorem that makes "generic" arguments work. By the end of Topology IV, you have the toolkit not just for analysis (which §1–12 supplied) but for *geometry* — manifolds, Lie groups, fundamental groups, and the algebraic invariants that the rest of Bredon's book develops.

---

# Concept Map

## §13 Quotient Spaces

- **[[Def - Quotient Topology and Identification Map]]**
	- Given $f : X \to Y$ onto, the **quotient topology** on $Y$ has $V \subseteq Y$ open iff $f^{-1}(V)$ is open in $X$. This is the *finest* (largest collection of opens) topology making $f$ continuous. A surjection equipped with the quotient topology on its target is an **identification map**. Universal property: $g : Y \to Z$ is continuous iff $g \circ f$ is continuous. The standard example: $X/{\sim} = X / R$ for an equivalence relation $R$, with $f = \pi$ the projection.

- **[[Def - Mapping Cylinder and Mapping Cone]]**
	- For $f : X \to Y$, the **mapping cylinder** is $M_f = (X \times I \sqcup Y) / \sim$ where $(x, 0) \sim f(x)$. The **mapping cone** is $C_f = M_f / (X \times \{1\})$, collapsing the top of the cylinder to a point. The cylinder is homotopy equivalent to $Y$ (deformation retract), and the inclusion $X \hookrightarrow M_f$ is the homotopical replacement of $f$. The cone $C_f$ is contractible iff $f$ extends over the cone $CX$ — a homotopy-theoretic measure of "how nontrivial $f$ is".

- **[[Def - Adjunction Space]]**
	- For $X \supseteq A$ closed and $f : A \to Y$, the **adjunction space** $Y \cup_f X$ is the quotient of $X \sqcup Y$ by $a \sim f(a)$ for $a \in A$. Geometrically: glue $X$ to $Y$ along $A$ via $f$. Universal property: a map out of $Y \cup_f X$ is the same data as compatible maps from $X$ and $Y$. The CW-complex construction (attaching cells one dimension at a time) is iterated adjunction.

- **[[Thm - Universal Property of the Quotient]]**
	- For $X \to Y = X/{\sim}$ the quotient, a function $g : Y \to Z$ is continuous if and only if $g \circ \pi$ is continuous. This is the defining property that uniquely characterizes the quotient topology. Practical consequence: to define a continuous map out of $X/{\sim}$, define a continuous map $X \to Z$ that is constant on equivalence classes; it factors uniquely.

- **[[Thm - The Sphere as Quotient of the Disk]]**
	- $D^n / S^{n-1} \cong S^n$: collapsing the boundary of the $n$-disk to a point yields the $n$-sphere. The proof factors the projection $D^n \to S^n$ (radial-ish) through the quotient, applies the compact-to-Hausdorff continuous bijection theorem ([[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism]]) to upgrade to a homeomorphism. The classical example of building higher-dimensional spheres from disks.

- **[[Ex - The torus has four definitions, all equivalent]]** (⭐⭐⭐)
	- Show $T^2 := \mathbb{R}^2/\mathbb{Z}^2 \cong [0,1]^2/{\sim} \cong S^1 \times S^1 \cong \text{anchor ring in } \mathbb{R}^3$, where the equivalence on the square identifies opposite edges. Each homeomorphism uses the compact-to-Hausdorff bijection upgrade.

- **[[Ex - Projective plane as a quotient of disk and sphere]]** (⭐⭐)
	- Show $\mathbb{R}P^2 := S^2/\{\pm x\} \cong D^2/\{\text{antipodes on } S^1\}$. The upper hemisphere viewed inside $D^2$ gives a continuous map to the quotient of $S^2$; check it descends to the quotient of $D^2$ and is a homeomorphism via compact-to-Hausdorff bijection.

- **[[Ex - A quotient with trivial topology]]** (⭐⭐)
	- Take $\mathbb{R}$ with equivalence $x \sim y$ iff $x - y \in \mathbb{Q}$. Show the quotient $\mathbb{R}/\mathbb{Q}$ has uncountably many points but the trivial (indiscrete) topology — every nonempty open set in the quotient pulls back to a $\mathbb{Q}$-saturated open set in $\mathbb{R}$, which is all of $\mathbb{R}$.

> [!note] Exercise Index — §13
> [[Exercise Index - §13 Quotient Spaces]]

## §14 Homotopy

- **[[Def - Homotopy]]**
	- A **homotopy** from $f_0 : X \to Y$ to $f_1 : X \to Y$ is a continuous $F : X \times I \to Y$ with $F(x, 0) = f_0(x), F(x, 1) = f_1(x)$. Two maps are **homotopic** ($f_0 \simeq f_1$) if such a homotopy exists. Homotopy is an equivalence relation on the set of maps $X \to Y$, and the equivalence classes are denoted $[X, Y]$. A **homotopy rel $A$** is one fixing every $a \in A$ throughout. The relation is closed under composition: $f \simeq g$ and $h \simeq k$ imply $hf \simeq kg$.

- **[[Def - Homotopy Equivalence and Contractible Space]]**
	- $f : X \to Y$ is a **homotopy equivalence** with homotopy inverse $g$ if $gf \simeq 1_X$ and $fg \simeq 1_Y$. $X$ and $Y$ are **homotopy equivalent** ($X \simeq Y$, but careful with the homeomorphism notation) if such $f, g$ exist. A space is **contractible** if it is homotopy equivalent to a point — equivalently, $1_X \simeq c_{x_0}$ for some constant map. $\mathbb{R}^n$ and any star-shaped set are contractible; $S^n$ for $n \geq 0$ is not (a nontrivial fact requiring algebraic topology).

- **[[Def - Deformation Retract]]**
	- $A \subseteq X$ is a **deformation retract** of $X$ if there is a homotopy $F : X \times I \to X$ with $F(x, 0) = x$ and $F(x, 1) \in A$ for all $x$, plus $F(a, 1) = a$ for $a \in A$. It is a **strong deformation retract** if also $F(a, t) = a$ for all $a \in A$ and $t$ (fixed throughout). A deformation retract is homotopy equivalent to its parent: $S^{n-1}$ is a strong deformation retract of $\mathbb{R}^n \setminus \{0\}$, so $S^{n-1} \simeq \mathbb{R}^n \setminus \{0\}$.

- **[[Thm - Mapping Cylinder is Deformation Retract of Target]]**
	- For any $f : X \to Y$, the canonical projection $r : M_f \to Y$ is a strong deformation retract — slide everything down the cylinder to $Y$. Consequence: $M_f \simeq Y$ for every $f$. The mapping cylinder is the "homotopical replacement" of the map $f$ by an inclusion $X \hookrightarrow M_f$: every map is homotopy-equivalent to an inclusion into a slightly bigger space.

- **[[Thm - Reparametrization Lemma]]**
	- Let $\phi_1, \phi_2 : (I, \partial I) \to (I, \partial I)$ agree on $\partial I$. If $F : X \times I \to Y$ is a homotopy, then $G_i(x, t) = F(x, \phi_i(t))$ for $i = 1, 2$ give homotopies $G_1 \simeq G_2$ rel $X \times \partial I$. This is the technical lemma that lets one reparametrize the time parameter of a homotopy without changing its homotopy class. Used to prove associativity and identity laws for concatenation of paths in the fundamental group.

- **[[Thm - Concatenation of Homotopies is Associative up to Homotopy]]**
	- For homotopies $F, G, H$ with the right compatibility, $(F * G) * H \simeq F * (G * H)$ rel $X \times \partial I$. Concatenation has identity (the constant homotopy) and inverses (running backward) up to homotopy. This is the algebraic content of homotopies: they form a *groupoid*, not just an equivalence relation. When restricted to paths ($X$ a point), this is the fundamental groupoid of a space.

- **[[Ex - Rn is contractible]]** (⭐)
	- Construct the contraction $F : \mathbb{R}^n \times I \to \mathbb{R}^n$ by $F(x, t) = (1 - t)x$. Verify $F(\cdot, 0) = 1$, $F(\cdot, 1) = c_0$ (the constant map to $0$). So $\mathbb{R}^n$ is contractible.

- **[[Ex - Sphere is a deformation retract of punctured Euclidean space]]** (⭐⭐)
	- Show $S^{n-1}$ is a strong deformation retract of $\mathbb{R}^n \setminus \{0\}$ via the homotopy $F(x, t) = tx + (1-t)x/|x|$. Verify: $F(x, 0) = x$, $F(x, 1) = x/|x| \in S^{n-1}$, and $F(x, t) = x$ for $x \in S^{n-1}$.

- **[[Ex - A retract of a contractible space is contractible]]** (⭐⭐)
	- If $A$ is a retract of contractible $X$ (i.e. there is a retraction $r : X \to A$, $r|_A = 1_A$), show $A$ is contractible. Hint: contractibility of $X$ gives $1_X \simeq c_{x_0}$. Restrict to $A$ via inclusion and retract.

> [!tip] Unlocked: Fundamental Group *(from Algebraic Topology)*
> The **fundamental group** $\pi_1(X, x_0)$ is the group of homotopy classes of loops at $x_0$ under concatenation. The reparametrization lemma is what makes the group structure well-defined; the fact that mapping cylinders are deformation retracts is the input to many of its properties. $\pi_1(S^1) = \mathbb{Z}$ (winding numbers), and this is what distinguishes $S^1$ from $\mathbb{R}^2$ and underwrites the Fundamental Theorem of Algebra.

> [!note] Exercise Index — §14
> [[Exercise Index - §14 Homotopy]]

## §15 Topological Groups

- **[[Def - Topological Group]]**
	- A **topological group** is a Hausdorff topological space $G$ with a group structure such that multiplication $\mu : G \times G \to G$ and inversion $\iota : G \to G$ are continuous. Examples: $\mathbb{R}, \mathbb{Z}, S^1$ (as $\mathbb{R}/\mathbb{Z}$ or unit complex numbers), $\operatorname{GL}_n(\mathbb{R})$ (open subset of $\mathbb{R}^{n^2}$), $\operatorname{O}(n), \operatorname{SO}(n), \operatorname{U}(n)$ (closed subspaces of matrix groups), every Lie group. The continuity of multiplication is a joint continuity condition on $G \times G$.

- **[[Def - Topological Subgroup, Homomorphism, Action]]**
	- A **topological subgroup** $H \leq G$ is a subgroup carrying the subspace topology. A **continuous homomorphism** is a group homomorphism that is also continuous. A **continuous action** of $G$ on $X$ is a continuous $G \times X \to X$ satisfying the group action axioms. The *quotient* $G/H$ for $H \leq G$ closed normal is again a topological group with the quotient topology.

- **[[Thm - Translations are Homeomorphisms]]**
	- For $g \in G$, the left translation $L_g(h) = gh$ and right translation $R_g(h) = hg^{-1}$ are homeomorphisms of $G$. Hence $G$ is **homogeneous**: every point looks like every other point. Inversion $\iota$ is also a homeomorphism (its own inverse). Conjugation $h \mapsto ghg^{-1}$ is a homeomorphism, in fact a continuous automorphism. These are the structural rigidities of topological groups.

- **[[Thm - Symmetric Neighborhoods Form a Basis at the Identity]]**
	- In a topological group $G$, the symmetric open neighborhoods (sets $U = U^{-1}$) of the identity $e$ form a neighborhood basis at $e$. Proof: any nbhd $V$ of $e$ contains a symmetric one, namely $V \cap V^{-1}$. Combined with $L_g$ being a homeomorphism, this localizes the topology entirely to the identity: the topology is determined by neighborhoods of $e$, and via translation by $g$ these become neighborhoods of $g$.

- **[[Thm - Closure of a Subgroup is a Subgroup]]**
	- If $H \leq G$ is a subgroup, then $\overline{H} \leq G$ is also a subgroup. Proof: the multiplication and inversion are continuous, so $\overline{H} \cdot \overline{H} \subseteq \overline{H \cdot H} \subseteq \overline{H}$ and $(\overline{H})^{-1} = \overline{H^{-1}} = \overline{H}$. Together with the fact that the connected component of $e$ is closed and normal (proved by similar continuity arguments), this is the source of the rigidity of topological groups.

- **[[Thm - Topological Group is Regular]]**
	- Every topological group is regular (in fact, completely regular). Proof: for $x \neq C$ closed, choose a symmetric nbhd $V$ of $e$ with $xV \cap C = \emptyset$; choose another symmetric $W$ with $WW \subseteq V$; then $xW$ and $C \cdot W$ are disjoint open neighborhoods of $x$ and $C$. This is automatic — no extra separation axiom needed once the group structure is in place.

- **[[Ex - SO(n) is connected]]** (⭐⭐⭐)
	- Show $\operatorname{SO}(n)$ is path-connected by inductively constructing paths to the identity: every rotation is a product of plane rotations, and each plane rotation is connected to the identity by a path in the rotation parameter. Then use [[Thm - Continuous Image of a Connected Space]] applied to the product of such paths.

- **[[Ex - The orthogonal group has two components]]** (⭐⭐)
	- Show $\operatorname{O}(n) = \operatorname{SO}(n) \sqcup \operatorname{SO}(n) \cdot D$ where $D$ is a reflection (any matrix with determinant $-1$). Each piece is path-connected (path through $\operatorname{SO}(n)$ extended by $D$), and they are disjoint clopen sets distinguished by the continuous function $\det : \operatorname{O}(n) \to \{\pm 1\}$.

- **[[Ex - S1 and SO(2) are homeomorphic as topological groups]]** (⭐) 
	- Explicit isomorphism: $\theta \mapsto \begin{pmatrix}\cos\theta & -\sin\theta \\ \sin\theta & \cos\theta\end{pmatrix}$ from $S^1 = \mathbb{R}/2\pi\mathbb{Z}$ to $\operatorname{SO}(2)$. Continuous, bijective, group homomorphism; compact-to-Hausdorff continuous bijection upgrade.

> [!tip] Unlocked: Lie Group *(from Differential Geometry)*
> A **Lie group** is a topological group that is also a smooth manifold, with multiplication and inversion smooth. The matrix groups $\operatorname{GL}_n(\mathbb{R}), \operatorname{O}(n), \operatorname{SO}(n), \operatorname{U}(n), \operatorname{SU}(n)$ are all Lie groups. The Lie algebra $\mathfrak{g}$ is the tangent space at the identity, and the exponential map $\exp : \mathfrak{g} \to G$ is a local diffeomorphism near $0$ by the [[Thm - The Inverse Function Theorem|inverse function theorem]]. Lie groups are *the* setting for continuous symmetry — every classical and quantum mechanical symmetry is a Lie group action.

> [!tip] Unlocked: Haar Measure *(from Measure Theory)*
> A **locally compact topological group** admits a (left) translation-invariant Radon measure, unique up to scaling, called **Haar measure**. The existence uses Tychonoff (extract a weak limit of averages) and local compactness (compact neighborhoods of identity). Haar measure is the source of every group-symmetric integration construction in harmonic analysis and probability on groups.

> [!note] Exercise Index — §15
> [[Exercise Index - §15 Topological Groups]]

## §16 Convex Bodies

- **[[Def - Convex Body]]**
	- A **convex body** $C \subseteq \mathbb{R}^n$ is a closed convex set with nonempty interior. The standard examples are the closed unit ball $D^n$, the standard $n$-cube $[0,1]^n$, the standard $n$-simplex. Convexity gives a single algebraic property — closure under convex combinations — and the consequence for topology is that the body is "star-shaped" from any interior point, making it amenable to a radial parametrization.

- **[[Thm - Compact Convex Body is Homeomorphic to a Disk]]**
	- Every compact convex body $C \subseteq \mathbb{R}^n$ with nonempty interior is homeomorphic to the closed unit disk $D^n$. The homeomorphism is the radial projection from an interior point: send $x \in \partial C$ to $x / r_C(x) \in S^{n-1}$ where $r_C$ is the support function, and extend radially. This is the cleanest topological classification result of the chapter and the prototype for "every example is the model".

- **[[Ex - Every n-simplex is homeomorphic to the disk]]** (⭐⭐)
	- The standard $n$-simplex $\Delta^n = \{(x_0, \dots, x_n) : x_i \geq 0, \sum x_i = 1\}$ is a compact convex body of dimension $n$. Apply the theorem to get $\Delta^n \cong D^n$. Use this to show every triangle is homeomorphic to a disk, every tetrahedron homeomorphic to a 3-ball, etc.

- **[[Ex - The cube and the ball]]** (⭐) 
	- $[-1, 1]^n \cong D^n$. Construct an explicit homeomorphism via radial scaling: for $x \neq 0$, send $x$ to $x \cdot \lVert x\rVert_\infty / \lVert x\rVert_2$, with the origin mapped to itself.

- **[[Ex - The Brouwer fixed-point theorem]]** (⭐⭐⭐)
	- (Forward reference to algebraic topology) Every continuous $f : D^n \to D^n$ has a fixed point. The proof uses degree theory or simplicial methods; outline the proof for $n = 1$ (intermediate value theorem) and $n = 2$ (no-retraction argument using $\pi_1(S^1)$).

> [!note] Exercise Index — §16
> [[Exercise Index - §16 Convex Bodies]]

## §17 The Baire Category Theorem

- **[[Def - Nowhere Dense and Meager]]**
	- $A \subseteq X$ is **nowhere dense** if $\overline{A}$ has empty interior. $A$ is **meager** (or **of first category**) if it is a countable union of nowhere dense sets; otherwise it is **of second category**. The intuition: a nowhere dense set is "very thin" — every open set contains a sub-open set disjoint from $A$. A meager set is a countable union of thin sets, still "thin" overall.

- **[[Thm - Baire Category Theorem]]**
	- In a complete metric space (or a locally compact Hausdorff space), the intersection of any countable collection of dense open sets is dense. Equivalently, the space is not the countable union of nowhere dense sets — it is "of second category in itself". The proof: take dense opens $U_n$, want to show $\bigcap U_n$ meets every open $V$. Recursively find balls $\overline{B_n} \subseteq U_n \cap B_{n-1}$ with shrinking radii; the centers form a Cauchy sequence converging into all $U_n$ and $V$.

- **[[Thm - Banach–Steinhaus and Open Mapping (Application of Baire)]]**
	- Two cornerstone theorems of functional analysis depend on Baire. **Banach–Steinhaus**: a family of bounded linear operators on a Banach space that is pointwise bounded is uniformly bounded. **Open mapping theorem**: a surjective continuous linear map between Banach spaces is open. Both proofs hinge on the Baire category theorem applied to the family of (nowhere-dense-or-not?) subsets defined by the operator norms.

- **[[Ex - The rationals are first category in R]]** (⭐) 
	- Show $\mathbb{Q} \subseteq \mathbb{R}$ is meager: $\mathbb{Q} = \bigcup_{q \in \mathbb{Q}} \{q\}$, and each singleton is nowhere dense in $\mathbb{R}$. By Baire, $\mathbb{R}$ is not meager in itself, so $\mathbb{R} \setminus \mathbb{Q}$ is non-meager — and in particular non-empty (this is silly for $\mathbb{R}$, but the same argument in a Banach space gives interesting density of "irrational" elements).

- **[[Ex - A continuous nowhere differentiable function exists]]** (⭐⭐⭐)
	- The set $\mathcal{D}_n \subseteq C[0, 1]$ of functions differentiable at *some* point in some interval $[k/n, (k+1)/n]$ is closed with empty interior (every continuous function is approximated by a "kinky" one). Each $\mathcal{D}_n$ is nowhere dense; by Baire, $\bigcup \mathcal{D}_n$ is meager, so its complement is non-meager — and contains a continuous nowhere differentiable function. The Weierstrass function is an explicit example.

- **[[Ex - Pointwise limit of continuous functions has dense continuity set]]** (⭐⭐⭐)
	- If $f_n : X \to \mathbb{R}$ are continuous and $f_n \to f$ pointwise on a complete metric space $X$, then $f$ is continuous on a dense $G_\delta$ subset of $X$. Proof: the discontinuity set of $f$ is meager, by writing it as a union of sets $\{x : \text{osc}(f, x) \geq 1/n\}$, each of which is closed with empty interior (by Baire applied to the $f_n$).

> [!tip] Unlocked: Open Mapping and Closed Graph Theorems *(from Functional Analysis)*
> The **open mapping theorem** (a surjective continuous linear map between Banach spaces is open) and the **closed graph theorem** (a linear map between Banach spaces with closed graph is continuous) are equivalent to each other and both rest on Baire. These are the genuine compactness-free existence theorems of functional analysis: they produce continuity / openness from purely structural hypotheses.

> [!note] Exercise Index — §17
> [[Exercise Index - §17 Baire Category]]

---

# Sources and Targets

**Targets — What do we usually try to prove?**

§13's targets are *homeomorphism statements*: "the torus is the quotient of the square by the identification of opposite edges", "the sphere is the quotient of the disk by the boundary", "$\mathbb{R}P^n$ is $S^n / \{\pm x\}$". The standard route is to factor an obviously continuous map through the quotient, then use the compact-to-Hausdorff continuous bijection upgrade theorem from [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness|Topology II]].

§14's targets are *homotopy equivalence statements*: "$\mathbb{R}^n$ is contractible", "$S^{n-1}$ is a deformation retract of $\mathbb{R}^n \setminus \{0\}$", "$M_f \simeq Y$", "$X \vee Y$ has a particular homotopy type". The route is constructing an explicit homotopy or deformation, then verifying the composition relations $gf \simeq 1$ and $fg \simeq 1$.

§15's targets are *topological-algebraic structure theorems*: "$\operatorname{SO}(n)$ is connected", "$\operatorname{O}(n)$ has two components", "$\mathbb{R}P^n \cong \operatorname{O}(n+1)/(\operatorname{O}(n) \times \operatorname{O}(1))$", "the closure of a subgroup is a subgroup". The route combines algebra (subgroup, kernel, image arguments) with continuity (the multiplication map preserves closure, the closure of a subgroup is a subgroup).

§16's target is the single classification: every compact convex body $\cong D^n$. The route is the radial projection construction.

§17's targets are *existence statements producing "generic" objects*: a nowhere differentiable continuous function, a transcendental number, a residual set of nice elements. The route is to write the "bad" set as a meager union of nowhere-dense sets, then Baire produces the "good" complement.

**Sources — What assumptions do we usually leverage?**

The standard sources are: a *quotient structure* (an equivalence relation on a known space), a *continuous map* (whose mapping cylinder or cone we want to study), a *group structure* (with continuity of multiplication and inversion), a *convexity hypothesis* (for §16), or a *completeness hypothesis* (for §17). Each routes to its specific target through a single principal theorem:

- Quotient + continuous map ⇒ universal property ⇒ continuous descended map
- Homotopy + deformation retract ⇒ homotopy equivalence
- Group structure ⇒ homogeneity + closure-of-subgroup-is-subgroup
- Convex body ⇒ radial projection ⇒ homeomorphic to disk
- Complete metric ⇒ Baire ⇒ generic property holds

---

# Legal Operations

1. **Build a quotient by an equivalence relation.** Define an equivalence relation $\sim$ on $X$, take $X/{\sim}$ with the quotient topology — opens are sets whose preimage is open. *Trigger:* you want to glue, fold, or collapse a subspace. *Pattern:* explicit equivalence relation, verify topology is the intended one via universal property.

2. **Upgrade a continuous bijection from compact to Hausdorff to a homeomorphism.** This is the [[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism|compact-Hausdorff upgrade]] from [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness|Topology II]]. The combination "$X$ compact, $Y$ Hausdorff, $f$ continuous bijection" is enough for $f^{-1}$ to be continuous. *Trigger:* you have a continuous bijection, the source is compact, the target is Hausdorff.

3. **Replace a continuous map by an inclusion via the mapping cylinder.** Any map $f : X \to Y$ is homotopy-equivalent to the inclusion $X \hookrightarrow M_f$. *Trigger:* you want to apply a theorem about inclusions to a general map. *Pattern:* form $M_f$, use deformation retract $M_f \simeq Y$, apply the inclusion-theorem.

4. **Construct a homotopy by a parameter sweep.** Given two maps, construct a homotopy by interpolating linearly in some coordinate. *Trigger:* you want to show $f \simeq g$. *Pattern:* $F(x, t) = (1-t) f(x) + t g(x)$ when values lie in a convex set; "rotate" or "shrink" when in a curved one.

5. **Exploit homogeneity of a topological group.** Any topological argument about a topological group reduces to a neighborhood of the identity via translation. *Trigger:* you want a local-to-global argument in a group. *Pattern:* check at $e$, translate via $L_g$ to any other point. This is why the topology of a topological group is so much more rigid than that of an arbitrary space.

6. **Use Baire to produce a "generic" object.** Write the bad set as a countable union of nowhere-dense (typically closed-with-empty-interior) sets; conclude its complement is non-meager and hence non-empty. *Trigger:* you want a point with some property and the property holds "for typical" elements. *Pattern:* identify the bad set, prove each piece nowhere dense, apply Baire.

7. **Verify continuity in a quotient via the universal property.** To check $g : X/{\sim} \to Z$ is continuous, lift it to $g \circ \pi : X \to Z$ and check continuity there. *Trigger:* a map out of a quotient. *Pattern:* the universal property reduces the question to the (usually easier) one about $X$.

8. **Use compact-Hausdorff continuous bijection in quotient contexts.** When you've constructed a continuous bijection from a compact quotient (e.g. $S^n / S^{n-1}$, $[0,1]^2/{\sim}$) to a Hausdorff target, the homeomorphism is automatic. *Trigger:* a continuous bijection out of a compact quotient.

**Illegal but tempting operations:**

> [!warning] 1. Treating "homotopy equivalent" as "homeomorphic"
> $\mathbb{R}^n$ is contractible, hence homotopy equivalent to a point. But $\mathbb{R}^n \neq $ a point (and is not homeomorphic to one). Homotopy equivalence is *much* coarser than homeomorphism — it forgets dimension, manifold-ness, properness, almost everything except "shape information seen by fundamental groups and homology". Always check the kind of equivalence relevant to the conclusion you want.

> [!warning] 2. Treating "deformation retract" without checking $A \subseteq X$
> A deformation retract requires $A$ to be a subspace of $X$, with the retraction $r$ satisfying $r|_A = 1_A$. Without this, the conclusion $X \simeq A$ may still hold but for a different reason (homotopy equivalence in general). The setup matters — sometimes the inclusion $A \hookrightarrow X$ does not factor through a retraction at all.

> [!warning] 3. Forgetting Hausdorffness in topological groups
> Bredon's definition of topological group requires the underlying topological space to be Hausdorff. Some sources drop this and rederive it from continuity of multiplication; others keep it as an axiom. Without Hausdorff, many of the standard theorems fail in subtle ways. Always assume Hausdorff for topological groups unless told otherwise.

> [!warning] 4. Using Baire in incomplete metric spaces
> Baire fails in $\mathbb{Q}$ (which is a metric space): $\mathbb{Q}$ is itself a countable union of nowhere dense sets (its singletons). The Baire conclusion requires *completeness* (or local compactness). When applying Baire, always verify which version of completeness is in play.

> [!warning] 5. Confusing the quotient topology and the box topology in a product
> The quotient topology on $X/{\sim}$ has the finest (largest) topology making the projection continuous. This is *different* from the product topology, which is the coarsest. Quotients and products are *dual* constructions, and switching them silently is a common error.

---

# Problem-Solving Strategy

The problems in §13–17 cluster into five families: building quotient spaces and identifying them with known objects, constructing homotopies and homotopy equivalences, verifying topological-algebraic structure of groups, classifying convex bodies, and producing generic objects via Baire.

For **quotient identifications** (showing $X/{\sim} \cong Y$ for some known $Y$), the universal recipe is: (1) construct a continuous map $X \to Y$ that respects the equivalence — i.e., is constant on equivalence classes; (2) use the universal property to descend to $X/{\sim} \to Y$; (3) check it is a bijection; (4) if $X$ is compact and $Y$ is Hausdorff, the compact-to-Hausdorff continuous bijection upgrade makes it a homeomorphism for free. The most common error is forgetting step (1) — the map must respect the equivalence to descend.

For **homotopy equivalences**, the standard tools are: linear interpolation in a convex setting (the contractibility of $\mathbb{R}^n$ is this); radial projection onto a "core" subspace (the sphere is a deformation retract of $\mathbb{R}^n \setminus \{0\}$); the mapping cylinder $M_f \simeq Y$ (replacing any map by an inclusion). When constructing a homotopy between specific maps $f_0, f_1$, look for a path of intermediate values $F(x, t)$ that is continuous in $(x, t)$ and equals $f_0, f_1$ at $t = 0, 1$.

For **topological group structure**, exploit homogeneity: any local property near the identity propagates everywhere via translation, so reduce all questions to neighborhoods of $e$. For connectivity, exhibit explicit paths; for closure-of-subgroups, use continuity of multiplication; for separation, use symmetric neighborhoods.

For **convex body classification**, the radial projection is the only tool. Choose an interior point as origin, parametrize the boundary by direction, extend to the interior radially. The resulting map is a homeomorphism by the compactness-Hausdorffness upgrade.

For **Baire applications**, the recipe is: identify the "bad" set, write it as a countable union of nowhere-dense (typically closed-with-empty-interior) sets, apply Baire to conclude the complement is non-meager, hence non-empty. The standard non-meager statement "the space is not a countable union of nowhere-dense sets" is enough to produce a witness; the stronger statement "the intersection of countably many dense opens is dense" gives more information about *how many* good elements there are.

A non-obvious general principle: **the constructions of §13 are universal constructions in the category of topological spaces**. The quotient is the coequalizer of two maps; the disjoint union is the coproduct; the product is the product; the mapping cylinder is the "homotopy pushout". When you recognize a construction as a universal one, the relevant properties (universal property, functoriality, homotopy invariance) follow from the abstract setup rather than ad-hoc verification.

---

# Most Reusable Properties

- **[[Thm - Universal Property of the Quotient|Quotient universal property]]**: A map out of $X/{\sim}$ is the same data as a $\sim$-respecting map out of $X$. This is the foundational tool for working with quotients — every homeomorphism, every continuous function on a quotient, every identification proof routes through it. Recognize it any time the source is a quotient.

- **[[Thm - Mapping Cylinder is Deformation Retract of Target|Mapping cylinder retraction]]**: Every map $f : X \to Y$ factors as $X \hookrightarrow M_f \simeq Y$, where the first arrow is an inclusion and the second is a homotopy equivalence. This is the homotopy-theoretic replacement of "every map is an inclusion up to homotopy", and it underlies the construction of fibrations, cofibrations, and the homotopy lifting and extension properties.

- **[[Thm - Closure of a Subgroup is a Subgroup]]**: In a topological group, $\overline{H}$ is a subgroup whenever $H$ is. The same holds for normal subgroups, and the identity component is a closed normal subgroup. This is the algebraic-topological rigidity that makes topological groups so well-behaved; it is the bridge between subgroups (algebra) and closure (topology).

- **[[Thm - Compact Convex Body is Homeomorphic to a Disk|Convex bodies are disks]]**: The radial projection makes every compact convex body of full dimension homeomorphic to $D^n$. This collapses convex-body classification to dimension counting — a powerful structural simplification.

- **[[Thm - Baire Category Theorem|Baire category]]**: A complete metric (or LCH) space is not a countable union of nowhere-dense sets; equivalently, intersections of countably many dense opens are dense. This is the structural existence theorem for "generic" objects, the engine of Banach–Steinhaus and the open mapping theorem in functional analysis.

---

# Bridges

1. **Algebraic Topology — Fundamental group from homotopy classes of loops.** The fundamental group $\pi_1(X, x_0)$ is the set of homotopy classes of based loops at $x_0$, with group operation given by concatenation. The reparametrization lemma (§14) is exactly what makes the group axioms work up to homotopy. $\pi_1$ is the first algebraic invariant of $X$ and the gateway to the rest of algebraic topology: $\pi_1(S^1) = \mathbb{Z}$ (winding numbers) distinguishes $S^1$ from $\mathbb{R}^2$, gives the Fundamental Theorem of Algebra, and underwrites every nontriviality argument for surfaces.

2. **Differential Geometry — Lie groups.** A **Lie group** is a topological group that is also a smooth manifold, with the group operations smooth. The matrix groups $\operatorname{GL}_n, \operatorname{O}(n), \operatorname{SO}(n), \operatorname{U}(n)$ are Lie groups; every connected Lie group is a quotient of its universal cover (a simply-connected Lie group) by a discrete normal subgroup. The Lie algebra $\mathfrak{g}$ is the tangent space at $e$; the **exponential map** $\exp : \mathfrak{g} \to G$ is a local diffeomorphism near $0$ by the [[Thm - The Inverse Function Theorem|inverse function theorem]]. Lie groups are the setting for every continuous symmetry in physics and geometry.

3. **Measure Theory — Haar measure on locally compact groups.** Every **locally compact** topological group admits a unique-up-to-scaling left-translation-invariant Radon measure, called **Haar measure**. The construction uses Tychonoff (compactness of $[0, \infty)^G$ for averaging arguments) and local compactness (compact neighborhoods of $e$ for the support of approximations). Haar measure underwrites every group-symmetric integration in harmonic analysis, including the Fourier transform on abelian groups and the regular representation of compact groups. See [[Measure Theory I — §1 Measure Spaces]].

4. **Functional Analysis — Banach–Steinhaus and the open mapping theorem.** The Baire category theorem of §17 is the foundation of every general theorem in functional analysis that converts pointwise hypotheses to uniform ones, or continuity of an inverse to continuity of the original. **Banach–Steinhaus**: a pointwise-bounded family of bounded operators is uniformly bounded. **Open mapping**: a surjective continuous linear map between Banach spaces is open. **Closed graph**: a closed-graph linear map between Banach spaces is continuous. Each is proved by writing the relevant "bad" set as a countable union of nowhere-dense sets and applying Baire.

5. **Group Theory — quotients in algebra match quotients in topology.** When $G$ is a topological group and $H \trianglelefteq G$ is a closed normal subgroup, the algebraic quotient $G/H$ inherits a topological group structure via the quotient topology, and the canonical projection $G \to G/H$ is continuous and open. This is the topological refinement of [[Group Theory I — §1.1–1.2|the standard group quotient]] — the algebra and topology agree, and the universal property of the quotient applies in both categories simultaneously. The first isomorphism theorem ($G/\ker \varphi \cong \operatorname{im}\varphi$) holds at the topological level if the kernel is closed and the map is open.

---

# Insights

The **unifying frame** of §13–17 is *building with continuity*. Quotients, attachments, mapping cylinders are the tools for constructing new spaces; homotopy is the equivalence relation under which the constructions are studied; topological groups are the constructed spaces with algebraic structure; convex bodies are the simplest classified examples; Baire produces generic constructions. Each section adds a different *kind* of construction, and the whole assembles into the standard toolkit of geometric topology.

The **true name** of homotopy equivalence is "isomorphism in the homotopy category" — two spaces are homotopy equivalent if they become equal once we identify maps that differ by a homotopy. The naive definition ("there exist $f, g$ with $gf \simeq 1, fg \simeq 1$") is technically correct but obscures the point: homotopy equivalence is the equivalence relation under which the algebraic invariants of topology — fundamental group, homology, cohomology, K-theory — are defined. Homeomorphism is too fine for these invariants; homotopy equivalence is exactly the right coarseness.

A **density-as-strategy** observation: in §17, the Baire category theorem is precisely the statement that "generic" elements of a complete metric space exist and are *dense*. The strategy is the same as the density-as-approximation lever throughout analysis: prove a property holds for "most" elements, find a specific element in the dense subset. Baire is the existence half of the strategy; the approximation half is the density of the simpler elements (rationals, polynomials, simple functions) inside which the generic property is verified.

A **trigger-reaction pattern**: when you want to identify a quotient space with a familiar one, the trigger is "is there a continuous map factoring through the equivalence?" and the reaction is "construct it, descend to the quotient, apply the compact-Hausdorff bijection upgrade". This pattern proves $D^n / S^{n-1} \cong S^n$, $T^2 = \mathbb{R}^2/\mathbb{Z}^2$, $\mathbb{R}P^n = S^n / \{\pm x\}$, $S^1 \cong \operatorname{SO}(2)$ — virtually every classical identification in topology is this pattern.

An **inheritance observation**: topological groups inherit their structure from the identity element. Every property a group has — separation axioms, local compactness, connectedness, metrizability — is determined by neighborhoods of $e$. This makes them one of the few classes of topological spaces where local behavior strictly determines global behavior, and it is why Lie theory works: the local structure (Lie algebra, smooth structure near $e$) determines the global structure (Lie group, up to discrete quotient).

A final pragmatic observation: the constructions of §13 — quotients, products, disjoint unions, mapping cylinders, adjunction spaces — are *the* constructions used throughout the rest of algebraic topology and geometry. CW-complexes are built by iteratively attaching cells via maps from spheres into the lower-dimensional skeleton, which is exactly the adjunction construction. Manifolds are built from coordinate charts that are products (locally) glued by quotient maps (transitions). Sheaves are gluings of presheaves on open sets. The §13 vocabulary is the language in which the rest of geometry is spoken.
