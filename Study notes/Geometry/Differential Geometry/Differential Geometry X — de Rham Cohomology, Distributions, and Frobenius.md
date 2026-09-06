---
type: topic
subject: differential-geometry
chapter: "10.1-10.4"
title: "Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius"
tags: [geometry, differential-geometry, cohomology, frobenius]
---

# Notation Registry

Throughout this topic $M$ is a smooth manifold (Hausdorff, second countable, possibly with boundary). All forms, distributions, and submanifolds are smooth. The standing convention from Lee — *all manifolds are second countable Hausdorff* — is in force, since both partition-of-unity arguments (used by the homotopy operator) and the patching arguments for Mayer–Vietoris need it.

- $M, N$ — smooth manifolds; $\dim M = n$.
- $\Omega^k(M)$ — smooth $k$-forms on $M$; $\Omega^0(M) = C^\infty(M)$.
- $d : \Omega^k(M) \to \Omega^{k+1}(M)$ — the [[Def - Exterior Derivative on a Manifold|exterior derivative]], satisfying $d^2 = 0$.
- $Z^k(M) = \ker(d : \Omega^k \to \Omega^{k+1})$ — the **closed** $k$-forms.
- $B^k(M) = \mathrm{im}(d : \Omega^{k-1} \to \Omega^k)$ — the **exact** $k$-forms.
- $H^k_{dR}(M) = Z^k(M) / B^k(M)$ — the $k$-th **de Rham cohomology group**, a real vector space (we use additive notation but it is in fact an $\mathbb{R}$-vector space — every cohomology group in this topic is a quotient of $\mathbb{R}$-vector spaces).
- $[\omega] \in H^k_{dR}(M)$ — the cohomology class of a closed form $\omega$.
- $F^* : \Omega^k(N) \to \Omega^k(M)$ — pullback by a smooth map $F : M \to N$; commutes with $d$ and so descends to $F^* : H^k_{dR}(N) \to H^k_{dR}(M)$.
- $TM$ — the [[Def - The Tangent Bundle|tangent bundle]] of $M$; $T_pM$ — the tangent space at $p$.
- $D \subseteq TM$ — a **distribution**: a smooth rank-$k$ [[Def - Subbundle|subbundle]] of $TM$. Equivalently a smoothly varying choice of $k$-plane $D_p \subseteq T_pM$.
- $[X, Y]$ — the [[Def - The Lie Bracket of Vector Fields|Lie bracket]] of vector fields, $[X, Y]f = X(Yf) - Y(Xf)$ on $f \in C^\infty(M)$.
- $\Gamma(D)$ — smooth (local or global) sections of the distribution $D$.
- $\mathcal{I}(D) \subseteq \Omega^*(M)$ — the graded ideal of forms that annihilate $D$, i.e. $\omega \in \mathcal{I}^p(D)$ iff $\omega(X_1, \dots, X_p) = 0$ whenever every $X_i \in D$.
- "Annihilating $1$-forms" — local defining $1$-forms $\omega^1, \dots, \omega^{n-k}$ with $D_p = \bigcap_i \ker \omega^i_p$.
- "Star-shaped" — $U \subseteq \mathbb{R}^n$ is star-shaped about $c \in U$ if for every $x \in U$ the segment $\{c + t(x-c) : t \in [0,1]\}$ lies in $U$.
- "Contractible" — a space $X$ is contractible if the identity is homotopic to a constant map.
- "Homotopic" maps $F, G : M \to N$ — there is a continuous (here we take smooth, by Whitney approximation) $H : M \times [0, 1] \to N$ with $H(\cdot, 0) = F$ and $H(\cdot, 1) = G$.

---

# Motivation

Here is the entire topic in one sentence: **closed forms minus exact forms is a real vector space whose [[Def - Dimension|dimension]] counts the holes in the manifold.** This compresses two of the four most important ideas in modern geometry — that local data (closedness, a differential equation) can have global obstructions (exactness, the topology of the underlying space), and that the obstructions are themselves a computable invariant.

Three problems motivate the chapter, and each is solved by a different aspect of the same machinery. The first is **when can a closed form be globally integrated?** A closed $1$-form $\omega$ on $\mathbb{R}^n$ is always a gradient — this is the Euclidean [[Thm - The Poincaré Lemma|Poincaré lemma]] from `Multivariate Analysis IV`. On the punctured plane $\mathbb{R}^2 \setminus \{0\}$ the angular form $d\theta = (-y\,dx + x\,dy)/(x^2 + y^2)$ is closed but not exact — the obstruction is the single hole at the origin. The chapter's first task is to compute the size of this obstruction on a general manifold, and the answer is the de Rham group $H^1_{dR}(M)$, whose [[Def - Dimension|dimension]] equals the number of independent "loops the form can detect."

The second problem is **when does a smoothly varying $k$-plane field admit a $k$-dimensional integral submanifold through every point?** Given a rank-$k$ subbundle $D$ of the tangent bundle, we ask whether there is a $k$-dimensional submanifold tangent to $D$ at every point. For rank-$1$ [[Def - Subbundle|subbundles]] — a single vector field, up to scaling — the answer is yes by [[Thm - Existence and Uniqueness of Integral Curves|the existence-uniqueness theorem for integral curves]]. For rank-$k \ge 2$, the answer is *not always*. The **Frobenius theorem** identifies the exact obstruction: a smooth distribution is integrable if and only if it is *involutive*, meaning closed under the Lie bracket. The same condition can be expressed equivalently in forms language — using local annihilating $1$-forms and the exterior derivative — and the bridge between the two formulations is the content of half this chapter.

The third problem is **when do constraints come from a potential?** In classical mechanics, constraints on a configuration space come in two flavors. *Holonomic* constraints — wires, surfaces, gear ratios — restrict motion to a submanifold; *nonholonomic* constraints — rolling without slipping, a skate on ice — restrict only the allowed velocities at each point, defining a distribution that may have no integral submanifolds at all. Frobenius's theorem is precisely the criterion that separates these: a constraint distribution is holonomic (comes from a submanifold-shaped potential) if and only if it is involutive. The non-involutive distribution $\ker(dz - y\,dx)$ on $\mathbb{R}^3$ is the prototype, and it is the standard contact form whose helical twist is the geometric meaning of nonholonomy.

The structural backbone of the chapter is the diagram

$$
\Omega^0(M) \xrightarrow{d} \Omega^1(M) \xrightarrow{d} \Omega^2(M) \xrightarrow{d} \cdots \xrightarrow{d} \Omega^n(M) \xrightarrow{d} 0
$$

with $d^2 = 0$. de Rham cohomology is the failure of this sequence to be exact, measured by the quotient $\ker d / \mathrm{im}\,d$ at each spot. The dual viewpoint — distributions and their annihilating [[Def - Ideal|ideals]] — is the same diagram read at the level of [[Def - Subbundle|subbundles]], and Frobenius is the statement that involutivity of $D$ matches differential-ideal closure of $\mathcal{I}(D)$.

What the reader should bring: comfort with smooth manifolds and maps ([[Differential Geometry I — Smooth Manifolds and Atlases]], [[Differential Geometry II — Smooth Maps and Partitions of Unity]]), the tangent bundle and vector fields ([[Differential Geometry III — Tangent Vectors and the Differential]], [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket]]), vector bundles and subbundles ([[Differential Geometry VI — Vector Bundles and the Cotangent Bundle]]), differential forms and the exterior derivative ([[Differential Geometry VIII — Differential Forms]]), Stokes's theorem ([[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem]]), and the Euclidean Poincaré lemma ([[Thm - The Poincaré Lemma]] in `Multivariate Analysis IV`). The chapter relies critically on the Lie bracket, on partitions of unity, and on the algebraic identity $d^2 = 0$.

---

# Concept Map

## §10.1 de Rham Cohomology

- **[[Def - de Rham Cohomology]]**
	- For a smooth manifold $M$, the $k$-th de Rham cohomology group is the real vector space $H^k_{dR}(M) = Z^k(M) / B^k(M)$, where $Z^k = \ker(d : \Omega^k \to \Omega^{k+1})$ is the space of closed $k$-forms and $B^k = \mathrm{im}(d : \Omega^{k-1} \to \Omega^k)$ is the space of exact $k$-forms; the quotient makes sense because $d^2 = 0$ forces $B^k \subseteq Z^k$. An element $[\omega]$ is a closed form, identified with any other closed form that differs from $\omega$ by an exact form. The fundamental theorem of the chapter is that $H^k_{dR}(M)$ is a smooth invariant of $M$ (in fact a topological one, even a [[Def - Homotopy|homotopy]] invariant), and the basic computations are $H^0_{dR}(M) = \mathbb{R}^{\#\text{components}}$ and $H^k_{dR}(\mathbb{R}^n) = 0$ for $k \geq 1$ (the Poincaré lemma).

- **Functoriality of $H^k_{dR}$**
	- A smooth map $F : M \to N$ induces a linear map $F^* : H^k_{dR}(N) \to H^k_{dR}(M)$ by pulling back closed forms and taking cohomology classes; this is well-defined because $F^*$ commutes with $d$, so it carries closed to closed and exact to exact. The assignment is functorial — $(G \circ F)^* = F^* \circ G^*$ and $\mathrm{id}^* = \mathrm{id}$ — making $H^k_{dR}$ a contravariant functor from smooth manifolds to real vector spaces. As an immediate corollary, diffeomorphic manifolds have isomorphic de Rham cohomology, and more is true: homotopy equivalent manifolds do (see [[Thm - Homotopy Invariance of de Rham Cohomology]]).

- **Cohomology in degree $0$**
	- $H^0_{dR}(M)$ is the space of locally constant real functions, equivalently the product $\prod_{C\in\pi_0(M)}\mathbb{R}$. If $M$ has finitely many connected components, say $c$, this is $\mathbb{R}^c$ and has dimension $c$. A closed $0$-form is a function $f$ with $df=0$, hence constant on each connected component. There are no $(-1)$-forms, so $B^0(M) = 0$ and the quotient is all of $Z^0(M)$. This single fact is why $H^0_{dR}$ is the most "topological" of all the de Rham [[Def - Group|groups]]: it counts components directly, and it sees a manifold's coarse structure without any sophisticated machinery.

- **[[Ex - Holomorphic Forms and the Cauchy–Riemann Equations]]** (⭐⭐)
	- Translate holomorphicity into the closedness of the complex $1$-form $f(z)\,dz$, with the Cauchy–Riemann equations providing the coefficient cancellation that makes Stokes and complex integration meet.

- **[[Ex - The de Rham Cohomology of R^n is Trivial in Positive Degrees]]** (⭐)
	- Show $H^k_{dR}(\mathbb{R}^n) = 0$ for $k \geq 1$ by appealing to the Poincaré lemma on a star-shaped domain. Computes $H^0_{dR}(\mathbb{R}^n) = \mathbb{R}$ along the way.

> [!tip] Unlocked: [[Def - Singular Cohomology|Singular Cohomology]] *(from Algebraic Topology)*
> The de Rham complex computes a real-coefficient version of the **singular cohomology** $H^k(M; \mathbb{R})$, which is defined for arbitrary topological spaces from formal sums of continuous maps from simplices into $M$. The de Rham theorem (below) is the bridge between these two seemingly unrelated constructions, and it is the model for every later "two definitions of cohomology agree" theorem in algebraic topology.

> [!tip] Unlocked: Sheaf Cohomology *(from Algebraic Geometry and Complex Geometry)*
> The construction "closed sections modulo exact sections of a differential complex" is the prototype for **sheaf cohomology** — a single machine that produces de Rham cohomology, singular cohomology, Čech cohomology, and Dolbeault cohomology as special cases. Every "obstruction theory" in modern geometry is sheaf cohomology of some sheaf.

> [!note] Exercise Index — §10.1
> [[Exercise Index - §10.1 de Rham Cohomology]]

## §10.2 The Poincaré Lemma and Homotopy Invariance

- **[[Def - Smooth Homotopy of Maps]]**
	- Two smooth maps $F, G : M \to N$ are **smoothly homotopic** if there is a smooth map $H : M \times [0,1] \to N$ (more precisely $M \times \mathbb{R}$, restricted) with $H(\cdot, 0) = F$ and $H(\cdot, 1) = G$. A space $X$ is **contractible** if $\mathrm{id}_X$ is homotopic to a constant map. Convex open sets in $\mathbb{R}^n$, star-shaped open sets, and Euclidean spaces are all contractible — the straight-line homotopy $H(x,t) = c + t(x-c)$ does the job. Two manifolds are **homotopy equivalent** if there are smooth maps between them whose compositions are each homotopic to the identity.

- **[[Thm - The Poincaré Lemma on a Star-Shaped Region]]**
	- If $U \subseteq \mathbb{R}^n$ (or the upper half-space $\mathbb{H}^n$) is star-shaped, then $H^k_{dR}(U) = 0$ for every $k \geq 1$ — every closed $k$-form is exact. The proof uses a homotopy operator $h : \Omega^k \to \Omega^{k-1}$ satisfying $dh + hd = \mathrm{id}$, built by integrating along the straight-line contraction. The Euclidean $1$-form version is [[Thm - The Poincaré Lemma]] in `Multivariate Analysis IV`; the manifold version generalizes from $1$-forms to all degrees and to contractible (rather than just star-shaped) domains.

- **[[Thm - Homotopy Invariance of de Rham Cohomology]]**
	- If $F, G : M \to N$ are smoothly homotopic, then $F^* = G^* : H^k_{dR}(N) \to H^k_{dR}(M)$ for every $k$. The proof constructs a *chain homotopy* $h$ between the pullbacks $F^*$ and $G^*$, satisfying $G^* - F^* = dh + hd$ at the form level; on cohomology classes the right side vanishes, since the $hd$ term kills closed forms and the $dh$ term is exact. The consequence — homotopy equivalent manifolds have isomorphic de Rham cohomology — is the result that makes $H^k_{dR}$ a topological invariant despite being defined from a smooth structure.

- **Cohomology of contractible manifolds**
	- A contractible smooth manifold has $H^k_{dR} = 0$ for all $k \geq 1$ and $H^0_{dR} = \mathbb{R}$. This is immediate from homotopy invariance: the inclusion of a point $\{q\} \hookrightarrow M$ is a homotopy equivalence when $M$ is contractible, and a point has $H^k = 0$ for $k \geq 1$. The Poincaré lemma is the case $M =$ star-shaped, but the manifold-level statement applies, for instance, to $\mathbb{R}^n$ minus a single ray (contractible but not convex), or to the open Möbius strip's universal cover.

- **[[Ex - Computing H^1 of S^1 via Mayer-Vietoris]]** (⭐⭐)
	- Use the Mayer–Vietoris sequence with the cover of $S^1$ by two arcs to compute $H^1_{dR}(S^1) = \mathbb{R}$, identifying the generator as the cohomology class of an arc-length form $d\theta$ that does not extend globally as $df$.

> [!tip] Unlocked: Spectral Sequence *(from Algebraic Topology and Homological Algebra)*
> The argument "compute cohomology of $M$ from cohomology of an open cover by repeatedly applying Mayer–Vietoris" generalizes to the **Čech-to-derived-functor spectral sequence** (and more generally to any double complex), which converts local information into global cohomology through a sequence of approximations. Every modern cohomology computation in algebraic geometry, complex geometry, and algebraic topology runs through some spectral sequence.

> [!tip] Unlocked: Hodge Theory *(from Riemannian and Complex Geometry)*
> On a compact oriented Riemannian manifold, **Hodge theory** picks out a *canonical* representative in each de Rham cohomology class — the unique harmonic form, satisfying $\Delta \omega = 0$ for the [[Def - Hodge Laplacian|Hodge Laplacian]]. de Rham cohomology becomes the kernel of an elliptic operator, and the dimension counts can be read off from the Hodge decomposition $\Omega^k = \mathcal{H}^k \oplus d\Omega^{k-1} \oplus d^*\Omega^{k+1}$. The Kähler case is even sharper: complex cohomology decomposes by bidegree, and the Hodge numbers $h^{p,q}$ are the master invariants of complex manifolds.

> [!note] Exercise Index — §10.2
> [[Exercise Index - §10.2 The Poincaré Lemma and Homotopy Invariance]]

## §10.3 Distributions and the Frobenius Theorem

- **[[Def - Distribution on a Manifold]]**
	- A **distribution of rank $k$** on $M$ is a rank-$k$ smooth [[Def - Subbundle|subbundle]] $D$ of the tangent bundle $TM$ — equivalently, a smoothly varying choice of $k$-dimensional [[Def - Subspace|subspace]] $D_p \subseteq T_pM$ at every point. Smoothness can be checked locally: $D$ is smooth iff each point has a neighborhood on which there are $k$ smooth vector fields $X_1, \dots, X_k$ whose values span $D$ pointwise. Distributions appear in mechanics as constraint sets, in geometry as plane fields (rank $2$ on a $3$-manifold gives a contact or [[Def - Foliation|foliation]] structure), and in PDE theory as integrability conditions on overdetermined systems.

- **[[Def - Integral Manifold of a Distribution]]**
	- An **integral manifold** of a rank-$k$ distribution $D$ is a $k$-dimensional immersed submanifold $N \subseteq M$ such that $T_pN = D_p$ at every $p \in N$. For rank-$1$ distributions integral manifolds are precisely the images of [[Def - Integral Curve of a Vector Field|integral curves]] of any spanning vector field, and they always exist by ODE theory. For higher rank, integral manifolds can fail to exist — the standard contact distribution on $\mathbb{R}^3$ has *no* integral surface through any point.

- **[[Def - Involutive Distribution]]**
	- A smooth distribution $D$ is **involutive** if for every pair of smooth vector fields $X, Y$ that are sections of $D$, the Lie bracket $[X, Y]$ is also a section of $D$. Equivalently, $\Gamma(D)$ is a Lie subalgebra of the space of all vector fields. The condition need only be checked on a local frame — if $V_1, \dots, V_k$ is a local frame for $D$ and every $[V_i, V_j]$ is a section of $D$, then $D$ is involutive everywhere on that neighborhood. Involutivity is the necessary condition for $D$ to admit integral manifolds: if integral manifolds exist, the bracket of two sections (both tangent to the same integral manifold) must remain tangent.

- **[[Def - Integrable Distribution]]**
	- A smooth distribution $D$ is **integrable** if every point of $M$ lies in some integral manifold of $D$. A stronger condition, **complete integrability**, requires the existence of a *flat chart* through every point — coordinates $(x^1, \dots, x^n)$ in which $D$ is spanned by $\partial/\partial x^1, \dots, \partial/\partial x^k$ and the integral manifolds are the slices $x^{k+1} = c^{k+1}, \dots, x^n = c^n$. Every integrable distribution is involutive (easy); the Frobenius theorem is the converse.

- **[[Thm - The Frobenius Theorem]]**
	- A smooth distribution $D$ on $M$ is completely integrable if and only if it is involutive. In particular, integrable $\iff$ involutive $\iff$ completely integrable. The "if" direction is the deep one: from the bracket-closure condition $[\Gamma(D), \Gamma(D)] \subseteq \Gamma(D)$, the theorem produces a flat chart through every point. The proof uses [[Thm - Canonical Form for a Nonvanishing Vector Field|canonical form for commuting vector fields]] applied to a local frame that has been re-engineered (via a coordinate projection) to consist of commuting fields — a construction that is itself a miniature dance between the Lie bracket and the flow.

- **[[Thm - Frobenius Theorem in Forms Language]]**
	- Let $D$ be a smooth distribution and $\omega^1, \dots, \omega^{n-k}$ local annihilating $1$-forms (defining $D$ as $\bigcap_i \ker \omega^i$). The following are equivalent: (i) $D$ is involutive; (ii) for every $1$-form $\theta$ that annihilates $D$, $d\theta$ also annihilates $D$ — equivalently the graded ideal $\mathcal{I}(D)$ generated by the $\omega^i$ is a *differential ideal* ($d\mathcal{I}(D) \subseteq \mathcal{I}(D)$); (iii) there exist $1$-forms $\alpha^i_j$ such that $d\omega^i = \sum_j \omega^j \wedge \alpha^i_j$; (iv) $d\omega^i \wedge \omega^1 \wedge \cdots \wedge \omega^{n-k} = 0$ for each $i$. The forms-language criterion is often the most computable version of involutivity in practice — for a rank-$(n-1)$ distribution defined by a single $1$-form $\omega$, the criterion is just $\omega \wedge d\omega = 0$.

- **[[Ex - A Non-Involutive Distribution from Three Vector Fields]]** (⭐⭐)
	- Verify that a specific distribution on $\mathbb{R}^4$ given by three vector fields is involutive, by computing all three Lie brackets and expressing each as a linear combination of the spanning fields.

- **[[Ex - A Non-Integrable Distribution on R^3 from the Standard Contact Form]]** (⭐⭐)
	- For $\alpha = dz - y\,dx$ on $\mathbb{R}^3$, show that the rank-$2$ distribution $D = \ker \alpha$ is everywhere non-involutive by computing $\alpha \wedge d\alpha \neq 0$. Find $[X, Y] \notin D$ for explicit $X, Y \in \Gamma(D)$. Picture the helical twist.

- **[[Ex - Frobenius Theorem Applied to an Overdetermined PDE]]** (⭐⭐⭐)
	- Solve a system $\partial u/\partial x = \alpha(x,y,u)$, $\partial u/\partial y = \beta(x,y,u)$ by recognizing the compatibility condition $\alpha_y + \beta\,\alpha_z = \beta_x + \alpha\,\beta_z$ as the involutivity of a distribution on $\mathbb{R}^3$ whose integral manifolds are graphs of solutions.

> [!tip] Unlocked: Contact Manifold *(from Symplectic and Contact Geometry)*
> A **contact manifold** is the *opposite* of an integrable distribution: a rank-$(2n)$ distribution $D$ on a $(2n+1)$-manifold that is *maximally non-involutive*, meaning the $1$-form $\alpha$ defining it satisfies $\alpha \wedge (d\alpha)^n \neq 0$ everywhere. The standard example is $\ker(dz - y\,dx)$ on $\mathbb{R}^3$, the same form whose non-involutivity we use as our worked counterexample. Contact geometry is the odd-dimensional analogue of symplectic geometry and the natural home of geometric optics, thermodynamics, and the [[Def - Geodesic|geodesic]] flow on the cosphere bundle.

> [!note] Exercise Index — §10.3
> [[Exercise Index - §10.3 Distributions and the Frobenius Theorem]]

## §10.4 Foliations

- **[[Def - Foliation]]**
	- A **foliation** of dimension $k$ on $M$ is a partition $\mathcal{F}$ of $M$ into disjoint connected immersed $k$-dimensional submanifolds (the **leaves**), together with the requirement that every point has a flat chart for $\mathcal{F}$ — coordinates $(x^1, \dots, x^n)$ with $\varphi(U)$ a cube in $\mathbb{R}^n$ such that each leaf meets $U$ in a countable union of $k$-dimensional slices $x^{k+1} = c^{k+1}, \dots, x^n = c^n$. The **Global [[Thm - The Frobenius Theorem|Frobenius Theorem]]** says [[Def - Foliation|foliations]] correspond bijectively to involutive distributions: the leaves are exactly the maximal connected integral manifolds.

- **The Mayer–Vietoris sequence**
	- For an open cover $M = U \cup V$, the **Mayer–Vietoris sequence** is the long exact sequence
	$$0 \to \Omega^p(M) \to \Omega^p(U) \oplus \Omega^p(V) \to \Omega^p(U \cap V) \to 0$$
	at the form level, which descends to the cohomology long exact sequence
	$$\cdots \to H^{p-1}(U \cap V) \xrightarrow{\delta} H^p(M) \to H^p(U) \oplus H^p(V) \to H^p(U \cap V) \xrightarrow{\delta} H^{p+1}(M) \to \cdots$$
	The proof at the form level uses a partition of unity subordinate to $\{U, V\}$ to split forms from $U \cap V$ as a difference of restrictions; the cohomology version then follows from the standard zigzag lemma. Mayer–Vietoris is the inductive tool that computes $H^*$ from local pieces, each contributing nothing by the Poincaré lemma.

- **[[Thm - The Mayer-Vietoris Sequence]]**
	- The above long exact sequence is exact for every smooth manifold $M$ and every open cover $M = U \cup V$. Applications: $H^*(S^n) = \mathbb{R}$ in degrees $0$ and $n$ and zero otherwise (cover $S^n$ by two contractible open hemispheres, $U \cap V$ is homotopy equivalent to $S^{n-1}$, induct); $H^*(T^n)$ is computed by iterating with the Künneth-style decomposition; $H^*(\mathbb{R}^n \setminus \{0\}) \cong H^*(S^{n-1})$ by a deformation retract. The exactness is the engine; the Poincaré lemma is the fuel.

- **[[Thm - The de Rham Theorem (Statement)]]**
	- For every smooth manifold $M$, the de Rham cohomology $H^k_{dR}(M)$ is naturally isomorphic to the singular cohomology $H^k(M; \mathbb{R})$ with real coefficients. The isomorphism is given by the **de Rham homomorphism**: a closed form $\omega$ pairs with a smooth singular $k$-cycle $c$ via $\int_c \omega$, descending to a well-defined pairing $H^k_{dR}(M) \times H_k(M) \to \mathbb{R}$, hence a map $H^k_{dR}(M) \to \mathrm{Hom}(H_k(M), \mathbb{R}) = H^k(M; \mathbb{R})$. The proof reduces by Mayer–Vietoris to the case of Euclidean balls, where both sides are computed directly from the Poincaré lemma. The upshot is that de Rham cohomology — defined purely from the smooth structure — is in fact a *topological* invariant, computable from cellular or singular methods on the underlying topological space.

- **[[Ex - The de Rham Cohomology of the Torus]]** (⭐⭐⭐)
	- Show $H^k_{dR}(T^n) = \mathbb{R}^{\binom{n}{k}}$ by induction on $n$ using Mayer–Vietoris (or the Künneth formula, stated as a forward result). Identify each cohomology class with a wedge of coordinate $1$-forms $d\theta^{i_1} \wedge \cdots \wedge d\theta^{i_k}$.

- **Holonomic and nonholonomic constraints**
	- In classical mechanics, a constraint on configuration space $Q$ is **holonomic** if it can be expressed as a submanifold ($\Sigma \subseteq Q$) — equivalently, as the level set of some constraint functions $f_1 = \cdots = f_r = 0$. It is **nonholonomic** if it only restricts admissible velocities at each point — i.e. a distribution $D \subseteq TQ$. By Frobenius, a velocity constraint $D$ is *integrably* (holonomically) realizable as a configuration constraint exactly when $D$ is involutive. The skate on ice (the constraint that velocity is parallel to the blade) and the rolling ball without slipping are the classical *non*-involutive examples — they constrain *how* you can move at each point but not *where* you can ultimately go.

> [!tip] Unlocked: Hodge Theory and the Hodge Decomposition *(from Riemannian Geometry)*
> On a compact oriented Riemannian manifold, the de Rham complex acquires an adjoint $d^*$ via the metric, and the **[[Def - Hodge Laplacian|Hodge Laplacian]]** $\Delta = dd^* + d^*d$ gives a canonical orthogonal decomposition $\Omega^k = \ker\Delta \oplus d(\Omega^{k-1}) \oplus d^*(\Omega^{k+1})$. The harmonic forms $\ker\Delta$ are the *canonical* representatives of de Rham cohomology classes — every class has a unique harmonic representative. This is the bridge from de Rham theory to elliptic operator theory.

> [!note] Exercise Index — §10.4
> [[Exercise Index - §10.4 Foliations]]

---

# Sources and Targets

**Targets — what do we usually try to prove?**

Cohomology-flavored exercises in this chapter cluster around five recurring goals. The most common is to **compute $H^k_{dR}(M)$ for a specific manifold** — a sphere, a torus, a punctured Euclidean space, a projective space — typically by an inductive Mayer–Vietoris argument starting from contractible pieces. A second target is to **decide whether a particular closed form is exact**, which on a non-contractible manifold reduces to integrating it over generators of $H_k(M)$ and checking that all such integrals vanish. A third is to **construct or characterize integral manifolds of a distribution**, which means either applying Frobenius to certify their existence (involutivity check) or producing them explicitly by integrating commuting vector fields. A fourth is to **certify or refute integrability of a constraint** — a question that arises in mechanics, control theory, and PDE compatibility — via the algebraic test $\omega \wedge d\omega = 0$ or the bracket test $[X, Y] \in D$. A fifth is to **identify the leaves of a foliation** explicitly when the involutive distribution is given. These five — compute $H^*$, decide exactness, construct integral manifolds, certify involutivity, identify leaves — are the recurring problems, and they recur because each is a way of pinning down a cohomological or geometric obstruction to a global integration.

**Sources — what assumptions do we usually leverage?**

The hypotheses in these problems are equally stereotyped. **A specific manifold whose topology is known or can be analyzed by covers** — the manifold is given as a sphere, torus, projective space, or product, and the cover decomposing it is the route. **A closed form with explicit local formulas** — the form $\omega$ is given, often built from local coordinates, and the question is whether it is also globally exact, which Stokes's theorem turns into an integration check. **A rank-$k$ distribution given by spanning vector fields or by annihilating $1$-forms** — every exercise about distributions gives one of these two presentations and asks for the involutivity check. **A homotopy or homotopy equivalence between two spaces or maps** — homotopy invariance then forces $H^*$ of both to be equal, instantly converting a hard computation into an easy one when the homotopy-equivalent target is contractible. **Two open sets covering a manifold whose intersection is well-understood** — this is the input to Mayer–Vietoris, with the "well-understood intersection" usually being a disjoint union of contractibles, or homotopy equivalent to a sphere of lower dimension. The recurring move is to **route a source to a target**: a given form is closed plus a non-contractible domain routes through the cohomology of that domain to a (non)exactness conclusion; a given distribution routes through involutivity to integrability via Frobenius; an open cover routes through Mayer–Vietoris to a long exact sequence whose terms are simpler manifolds' cohomology.

---

# Legal Operations

These are the moves that almost every problem in this chapter is assembled from. Read them as a checklist: when stuck, scan and try each one.

**Legal operations:**

1. **Pull a closed form back along a smooth map.** If $\omega \in Z^k(N)$ and $F : M \to N$ is smooth, then $F^*\omega \in Z^k(M)$ and $[F^*\omega] = F^*[\omega] \in H^k_{dR}(M)$. *Trigger:* you have a closed form on the target of a smooth map and want one on the source, or you want to compare cohomology of two manifolds via a map. *Pattern:* pulling back commutes with $d$, so it carries closed to closed and exact to exact; check what your favourite generator restricts to.

2. **Apply the Poincaré lemma on a contractible open set.** On any open ball, half-ball, star-shaped or contractible region, every closed form of degree $\geq 1$ is exact. *Trigger:* a closed form locally; you need a *local* primitive. *Pattern:* shrink the domain to a chart (which is diffeomorphic to a ball), invoke the lemma, get a local primitive. The local primitives are the building blocks of every Mayer–Vietoris computation and every Čech-style argument.

3. **Detect a non-trivial cohomology class by integration over a cycle.** If $\omega$ is closed and there exists a smooth closed submanifold (or smooth singular cycle) $S$ of dimension $k$ with $\int_S \omega \neq 0$, then $[\omega] \neq 0$ in $H^k_{dR}(M)$. *Trigger:* you suspect a closed form is *not* exact, or you want to show a cohomology generator is non-trivial. *Pattern:* by [[Thm - Stokes' Theorem on Manifolds|Stokes]], an exact form integrates to zero over a boundaryless cycle; producing one with non-zero integral certifies non-exactness.

4. **Test involutivity by Lie brackets on a local frame.** If $V_1, \dots, V_k$ is a smooth local frame for a distribution $D$, then $D$ is involutive iff every $[V_i, V_j]$ is a section of $D$ on the same neighborhood — checking just the frame is enough. *Trigger:* a distribution is given by spanning vector fields. *Pattern:* compute all $\binom{k}{2}$ brackets, express each in the frame, and verify membership.

5. **Test involutivity by $1$-forms.** If $\omega^1, \dots, \omega^{n-k}$ locally define $D$ via $D = \bigcap_i \ker \omega^i$, then $D$ is involutive iff $d\omega^i \wedge \omega^1 \wedge \cdots \wedge \omega^{n-k} = 0$ for each $i$ — equivalently, $d\omega^i = \sum_j \omega^j \wedge \alpha^i_j$ for some $1$-forms $\alpha^i_j$. *Trigger:* a distribution is given by annihilating $1$-forms (a "[[Def - Pfaffian|Pfaffian]] system"). *Pattern:* compute $d\omega^i$, wedge with the constraint forms, check whether the result is zero. For a rank-$(n-1)$ distribution defined by a single $1$-form $\omega$, the test is just $\omega \wedge d\omega = 0$.

6. **Invoke Frobenius to manufacture integral manifolds.** If $D$ is involutive, there is a flat chart through every point — coordinates in which $D = \mathrm{span}(\partial_1, \dots, \partial_k)$ and the integral manifolds are slices. *Trigger:* you know involutivity and want a concrete description of integral submanifolds. *Pattern:* find $n - k$ functions $f^{k+1}, \dots, f^n$ that are constant on each integral manifold (i.e. annihilated by every section of $D$), and the integral manifolds are level sets.

7. **Use homotopy invariance to replace $M$ with a homotopy-equivalent simpler space.** If $M \simeq N$ (homotopy equivalent), then $H^*_{dR}(M) \cong H^*_{dR}(N)$. *Trigger:* the manifold of interest is hard to handle, but a deformation retract or homotopy-equivalent quotient is easy. *Pattern:* $\mathbb{R}^n \setminus \{0\} \simeq S^{n-1}$ by radial projection; the Möbius strip $\simeq S^1$ by the core circle; a thickened submanifold $\simeq$ the submanifold itself.

8. **Cut into pieces and assemble via Mayer–Vietoris.** Express $M = U \cup V$ with $U$, $V$, and $U \cap V$ each cohomologically tractable; the long exact sequence then determines $H^*(M)$ from the simpler groups. *Trigger:* the manifold has an obvious "two-piece" decomposition, like the two-hemisphere cover of a sphere or the strip decomposition of a torus. *Pattern:* set up the sequence, use exactness to fill in unknown terms from the known ones, often using that flanking groups vanish on contractible $U, V$.

9. **Read $H^0_{dR}$ as a connected-components count.** $H^0_{dR}(M)$ is the space of locally constant functions, with dimension equal to the number of connected components of $M$. *Trigger:* you want to know whether $M$ is connected, or you want a quick sanity check on a cohomology computation. *Pattern:* compute $H^0$ first; if it does not match the expected number of components, your other groups are also wrong.

10. **Use a partition of unity to split a global form into local pieces.** Given $\omega \in \Omega^k(M)$ and a cover $\{U_\alpha\}$ with subordinate partition $\{\rho_\alpha\}$, write $\omega = \sum_\alpha \rho_\alpha \omega$, so each $\rho_\alpha \omega$ is supported in a single chart. *Trigger:* you need to integrate, differentiate, or extend a global object locally. *Pattern:* every Mayer–Vietoris construction and every "smooth partition" argument runs on this — the partition is the bridge between local pieces and global existence.

**Illegal but tempting operations:**

> [!warning] 1. Concluding a closed form is exact just because it is closed
> The temptation is reasonable on $\mathbb{R}^n$, where the [[Thm - The Poincaré Lemma|Poincaré lemma]] does say closed implies exact. But on a non-contractible manifold the implication fails sharply. The standard counterexample is $d\theta = (-y\,dx + x\,dy)/(x^2+y^2)$ on $\mathbb{R}^2 \setminus \{0\}$: closed everywhere, yet $\oint_{S^1} d\theta = 2\pi \neq 0$ proves it is not exact. The operation becomes legal exactly when $H^k_{dR}(M) = 0$ — for instance when $M$ is contractible, or when restricted to a contractible chart of any manifold.

> [!warning] 2. Treating a rank-$k$ distribution as if it always has integral submanifolds
> For a single vector field (rank $1$) integral curves always exist by ODE theory. It is tempting to assume the same works for higher rank, but it fails dramatically. The standard contact distribution $\ker(dz - y\,dx)$ on $\mathbb{R}^3$ has rank $2$ but admits no integral surface at any point — the helical twist of the plane field as you move in the $x$-direction is what destroys integrability. The operation becomes legal exactly when the distribution is involutive, in which case Frobenius produces the integral submanifolds; without involutivity all attempts to glue local solutions into a $k$-dimensional surface fail.

> [!warning] 3. Forgetting that $H^k_{dR}(M)$ depends only on the homotopy type
> The temptation is to compute $H^*$ of a complicated manifold by direct integration of forms, treating it as a smooth-structure-dependent invariant. This works, but it is almost always the wrong route. The Möbius strip and the cylinder are both homotopy equivalent to $S^1$, so $H^* = \mathbb{R}, \mathbb{R}, 0, \dots$ — the same as $H^*(S^1)$, regardless of the strip's topology of non-orientability. The lesson: before computing, deform-retract. The operation "compute directly" is legal but wasteful; the operation "deform-retract first" is always the right opener.

> [!warning] 4. Confusing involutivity with integrability of vector fields
> A *single* smooth vector field is always "integrable" in the sense that it has integral curves — this follows from ODE theory and uses no bracket condition. For higher-rank distributions, "integrability" requires a global statement about bracket-closure, not pointwise existence. The single vector field $X$ also trivially satisfies $[X, X] = 0$, so the rank-$1$ Frobenius condition is vacuous. The lesson: rank $1$ is too small a case for the Frobenius story to teach anything; the action is at rank $\geq 2$.

> [!warning] 5. Believing Mayer–Vietoris works for any covering family
> The Mayer–Vietoris sequence requires a cover by *two open sets* $U \cup V = M$. It does not directly generalize to three or more open sets; the multi-cover version is a spectral sequence (Čech–de Rham), not an exact sequence. The standard counterexample-temptation: covering a non-contractible $M$ by three contractibles in a way that should "obviously" force $H^* = 0$ — this would give wrong answers because the three-way overlap data is more subtle. Stick to two-piece covers, or upgrade to the spectral sequence.

---

# Problem-Solving Strategy

The problems in this chapter divide into two camps that look unrelated but share a common structure: computational cohomology problems, and integrability problems for distributions. Begin by classifying which camp you are in.

If the problem **asks you to compute $H^k_{dR}(M)$** for some specific manifold, the routine has four steps and the first one decides everything. Step one is to **find the homotopy type of $M$**: is it contractible? Homotopy-equivalent to a sphere? A wedge of spheres? A product? The dimension of every cohomology group is fixed by the homotopy type, so the answer is already determined the moment you identify it. Step two, if step one did not immediately resolve, is to **choose a Mayer–Vietoris cover**: pick $U$, $V$ open with $U \cup V = M$, each individually as simple as possible (ideally contractible or known), and such that $U \cap V$ is also tractable. The cover that decomposes $S^n$ as two open hemispheres meeting in a thickened equator $\simeq S^{n-1}$ is the standard template, and it generalizes: any compact manifold has a finite "good cover" by contractibles whose finite intersections are also contractible. Step three is to **write the long exact sequence and fill in the unknowns** using exactness — if you know all but one term, you know that one too. Step four, when the answer is non-zero, is to **identify an explicit generator**: a closed form whose cohomology class spans the group. The generator is what lets you check by integration that your answer is correct.

If the problem **asks whether a closed form $\omega$ is exact**, the routine is even shorter. Either (a) $\omega$ lives on a contractible domain, in which case the [[Thm - The Poincaré Lemma|Poincaré lemma]] settles it instantly — yes, exact, with an explicit primitive constructible by the homotopy operator; or (b) $\omega$ lives on a manifold whose $H^k_{dR}$ has a known basis, in which case exactness reduces to checking that the cohomology class of $\omega$ is zero in that basis — typically by integrating $\omega$ over each generating cycle and verifying the integral is zero. Stokes's theorem is the workhorse: $[\omega] = 0$ iff $\int_S \omega = 0$ for every closed $S$ in the homology basis, by [[Thm - Stokes' Theorem on Manifolds|Stokes]].

If the problem **asks whether a distribution $D$ is integrable**, [[Thm - The Frobenius Theorem|Frobenius]] settles it. Decide first which formulation of the distribution you have: a spanning frame $V_1, \dots, V_k$ (then check all brackets $[V_i, V_j]$ are sections of $D$), or annihilating $1$-forms $\omega^1, \dots, \omega^{n-k}$ (then check $d\omega^i \wedge \omega^1 \wedge \cdots \wedge \omega^{n-k} = 0$). The frame test is the right one for distributions defined as the image of a map; the form test is the right one for distributions defined as the kernel of constraints. The two are equivalent, but each can be dramatically more efficient than the other depending on presentation.

If the problem **asks for an explicit integral manifold or foliation** when one is known to exist, the constructive part of the [[Thm - The Frobenius Theorem|Frobenius proof]] gives the procedure. Pick a coordinate projection $\pi : U \subseteq \mathbb{R}^n \to \mathbb{R}^k$ such that $d\pi|_{D_p}$ is an isomorphism onto $\mathbb{R}^k$; this projection makes a canonical basis of $\partial_i$'s in the image, and pulling back yields a *commuting* frame for $D$. The flows of these commuting fields composed in any order trace out a flat chart, and the slices of the projection in this chart are the integral manifolds. In simple problems an alternative is to **guess functions $f^{k+1}, \dots, f^n$ whose level sets are the integral manifolds** — equivalently, functions annihilated by every section of $D$ — and verify by direct computation that the level sets are tangent to $D$ everywhere.

If the problem **asks about overdetermined PDEs**, recognize the system $\partial u/\partial x^i = \alpha^i(x, u)$ as the question "is the graph of $u$ an integral manifold of the distribution spanned by $\partial_i + \alpha^i \partial_z$?" The compatibility condition (existence of a solution) is precisely the involutivity of this distribution, which after expansion is the system of equations $\partial_j \alpha^i + \alpha^j \partial_z \alpha^i = \partial_i \alpha^j + \alpha^i \partial_z \alpha^j$ — these are the mixed-partial conditions $\partial^2 u/\partial x^i \partial x^j = \partial^2 u/\partial x^j \partial x^i$ in disguise. The take-away: PDE compatibility conditions in this style are *always* involutivity conditions for some distribution, and the proof of solvability is *always* an application of Frobenius.

The meta-strategy that threads through everything: **every question in this chapter is the question "what local condition has a global obstruction, and what is its size?"** Closedness is local, exactness is global, and the gap is $H^k_{dR}$. Tangency to a distribution is local, integral submanifolds are global, and the gap is bracket non-closure. Whenever a local-to-global obstruction appears, ask what its size is and whether it is computable by a long exact sequence.

---

# Most Reusable Properties

- **[[Thm - The Poincaré Lemma on a Star-Shaped Region|Poincaré Lemma]]**: on a star-shaped or contractible domain, every closed form is exact, with an *explicit* primitive given by the homotopy operator $h\omega = \int_0^1 \iota_{R}(\phi_t^*\omega)\,dt$ along the radial contraction. **Typical use:** local exactness on chart domains — the Poincaré lemma converts any closedness condition into a local primitive, which is then patched globally via partitions of unity or Mayer–Vietoris. The single most-reached-for fact in cohomology computations: every "obstruction is purely global" argument starts here. Its disguised use is *negative* — when something fails to be exact on a non-contractible domain, the failure measures the topology of the hole.

- **Homotopy invariance of $H^k_{dR}$**: smoothly homotopic maps induce equal maps on cohomology, so homotopy equivalent manifolds have isomorphic de Rham cohomology. **Typical use:** before computing $H^*(M)$ directly, deform-retract $M$ onto a simpler homotopy-equivalent space ($\mathbb{R}^n \setminus \{0\} \to S^{n-1}$, $T^n \to T^n$ itself, $\mathrm{M\ddot{o}bius\ strip} \to S^1$). The disguised use: a smooth invariant turns out to be a topological one, because every homotopy equivalence — including non-smooth ones — preserves it via the Whitney approximation theorem.

- **[[Thm - The Mayer-Vietoris Sequence|Mayer–Vietoris]]**: for any open cover $M = U \cup V$, the cohomology of $M$ sits in a long exact sequence with the cohomology of $U$, $V$, and $U \cap V$. **Typical use:** induction on the number of contractible pieces in a "good cover" — start with two open sets and chain. Every computation of $H^*(S^n)$, $H^*(T^n)$, $H^*(\mathbb{CP}^n)$, and the general "compute $H^*$ from a CW decomposition" argument runs on iterated Mayer–Vietoris. The disguised use: it shows that local cohomology completely determines global cohomology, with the "stitching" data living in the connecting maps $\delta$.

- **[[Thm - The Frobenius Theorem|Frobenius's Theorem]]**: a smooth distribution is integrable iff it is involutive iff its annihilating ideal is differential. **Typical use:** *certifying* the existence of integral submanifolds when direct construction is hard — involutivity is an algebraic Lie-bracket check, integrability is a geometric existence claim, and Frobenius turns the second into the first. The disguised use is in PDE: every "compatibility condition" for an overdetermined system is the involutivity of an associated distribution.

- **The de Rham theorem (statement)**: $H^k_{dR}(M) \cong H^k(M; \mathbb{R})$, identifying smooth-cohomological invariants with topological ones. **Typical use:** convert a question "what is $H^k_{dR}$" into a question about loops, surfaces, and higher cycles in the underlying topological space, computable by cellular methods. The disguised use: every Euler characteristic, Betti number, and Poincaré polynomial computed by combinatorial means is also computable from forms.

---

# Bridges

1. **Algebraic topology — de Rham cohomology is singular cohomology with real coefficients.** The de Rham theorem (a smooth-manifold result, with a hands-on proof by Mayer–Vietoris induction) says that for every smooth manifold $M$, $H^k_{dR}(M) \cong H^k_{\mathrm{sing}}(M; \mathbb{R})$. The isomorphism sends a closed form $\omega$ to the functional $[c] \mapsto \int_c \omega$ on $k$-cycles. Singular cohomology, in turn, dualizes to the singular homology $H_k(M; \mathbb{R})$, and the dimensions $\beta_k = \dim H_k$ are the **Betti numbers** — the central topological invariants. So computing de Rham cohomology *is* computing Betti numbers, by an entirely smooth route. The Euler characteristic $\chi(M) = \sum (-1)^k \beta_k$ is then encoded in the alternating sum of $\dim H^k_{dR}$.

2. **Algebraic geometry and complex geometry — Hodge theory and the Hodge decomposition.** On a compact Kähler manifold, de Rham cohomology refines into a bigraded decomposition $H^k_{dR}(M; \mathbb{C}) = \bigoplus_{p+q=k} H^{p,q}(M)$ via the choice of complex structure, where $H^{p,q}$ consists of cohomology classes representable by forms of bidegree $(p, q)$. The **Hodge numbers** $h^{p,q} = \dim H^{p,q}$ are the master invariants of complex projective varieties; for compact Kähler manifolds they satisfy $h^{p,q} = h^{q,p}$ (Hodge symmetry) and $h^{p,q} = h^{n-p,n-q}$ (Serre duality, with $n$ the complex dimension). The de Rham cohomology of this topic is the real (or complex) Hodge diamond projected onto its "total degree" diagonals.

3. **Classical mechanics — Frobenius and the holonomic/nonholonomic dichotomy.** A constraint on the configuration space $Q$ of a mechanical system is **holonomic** if it can be written as a submanifold ($f_1(q) = \cdots = f_r(q) = 0$ for some functions $f_i$) and **nonholonomic** if it only restricts velocities ($\omega^1(\dot{q}) = \cdots = \omega^r(\dot{q}) = 0$ for some $1$-forms $\omega^i$ on $Q$). [[Thm - The Frobenius Theorem|Frobenius]] is the precise criterion: a velocity constraint $D = \bigcap_i \ker \omega^i$ is equivalent to a holonomic one iff $D$ is involutive. The skate on ice (constraint: velocity is along the blade), the rolling ball without slipping, and parallel parking are all *non*-involutive — they constrain *how* you move at each instant but not *where* you can end up. The non-involutivity is precisely why you can park a car despite the steering wheel having only one degree of freedom: by repeated bracket-like maneuvers (forward-turn-back-turn) you generate motion in directions not in the original distribution. In control theory this is the **Chow–Rashevskii theorem**: a bracket-generating distribution is *globally* controllable.

4. **Partial differential equations — overdetermined systems and integrability conditions.** The question "does the system $\partial u/\partial x^i = \alpha^i(x, u)$ have a solution with $u(0) = u_0$?" is the question "is the graph of $u$ an integral manifold of the distribution spanned by $X_i = \partial_{x^i} + \alpha^i \partial_u$ on $\mathbb{R}^{n+1}$?" The compatibility condition $\partial_j \alpha^i + \alpha^j \partial_u \alpha^i = \partial_i \alpha^j + \alpha^i \partial_u \alpha^j$ is exactly the involutivity $[X_i, X_j] = 0$ of the spanning fields. So the **classical PDE compatibility theorem of Frobenius** for first-order overdetermined systems is just the Frobenius theorem applied with this specific distribution. The same identification works for nonlinear systems and in higher generality with the Cartan–Kähler theorem, the modern descendant.

5. **Special relativity and electromagnetism — Maxwell's equations as closed/exact form statements.** In Minkowski space ($\mathbb{R}^4$ with [[Def - Minkowski Space and the Metric|the Lorentzian metric]]), the electromagnetic field is a $2$-form $F$ on spacetime. The homogeneous Maxwell equations are $dF = 0$ (closed), and the inhomogeneous are $d{*F} = J$ where $*$ is the Hodge star and $J$ is the current $3$-form. The Poincaré lemma on contractible spacetime regions then guarantees $F = dA$ for a $1$-form $A$ — the four-potential — and the gauge freedom $A \mapsto A + d\chi$ is precisely the cohomological non-uniqueness of primitives. The existence of the vector and scalar potentials of electromagnetism *is* the Poincaré lemma, and electromagnetic field topology — Aharonov–Bohm, magnetic monopoles — is the failure of the lemma on non-contractible regions.

6. **Group theory and quotient construction — cohomology groups are abelian groups by addition.** The de Rham cohomology $H^k_{dR}(M)$ is more than a real vector space — it is in particular an [[Def - Abelian Group|abelian group]] under addition of cohomology classes, defined as the quotient $Z^k / B^k$ of two abelian groups. The quotient structure is precisely the [[Def - Quotient Group|quotient group]] construction from [[Group Theory I — §1.1–1.2]] applied to $(Z^k, +)$ by the normal subgroup $B^k$. The induced map $F^* : H^*(N) \to H^*(M)$ from a smooth $F : M \to N$ is a [[Def - Homomorphism|group homomorphism]] (in fact $\mathbb{R}$-linear), and the Mayer–Vietoris long exact sequence is a sequence of abelian groups and homomorphisms whose [[Def - Kernel and Image|kernels and images]] match at each spot. The entire theory is built on the elementary algebra of quotients applied to specific chain-complex pieces.

---

# Insights

**The unifying frame: closed/exact and involutive/integrable are the same idea twice.** Look at the two main objects of the chapter side by side. The de Rham complex $\Omega^0 \xrightarrow{d} \Omega^1 \xrightarrow{d} \Omega^2 \xrightarrow{d} \cdots$ asks when a closed form is exact, and the obstruction is cohomology. A distribution $D \subseteq TM$ asks when its sections close under the Lie bracket, and the obstruction is non-involutivity. These look like different problems, but they are the same diagram read twice. A closed $1$-form $\omega$ defines a *distribution* $D = \ker \omega$, and the question "is $\omega$ exact" is the question "are the level sets of the would-be primitive $f$ (so $\omega = df$) the integral submanifolds of $D$." On a contractible domain, both questions have the same trivial answer (yes); on a manifold with topology, both can fail, and they fail in exactly the same way — by a non-trivial cohomology class. The forms-language Frobenius theorem makes this exact: $D = \ker(\omega^1, \dots, \omega^{n-k})$ is involutive iff $d\omega^i$ lies in the ideal generated by the $\omega^j$, which is the differential-ideal closure condition — directly an exterior-derivative computation, the same machinery that computes de Rham cohomology. The bridge between the two viewpoints, made flesh in problems like [[Ex - A Non-Integrable Distribution on R^3 from the Standard Contact Form]], is the central insight of the chapter.

**The true name of $H^k_{dR}$ is "the failure of $d^2 = 0$ to be exact."** The textbook formula $H^k = Z^k / B^k$ is the right thing to compute but the wrong thing to *think*. The operational viewpoint is that the de Rham complex is *almost* exact — $d^2 = 0$ is the necessary condition for exactness to even be a sensible question — and cohomology measures the precise gap. Every theorem about $H^*$ in this chapter is a statement about that gap. The Poincaré lemma says the gap vanishes on contractible domains; homotopy invariance says the gap depends only on homotopy type; Mayer–Vietoris says the gap is computable from local gaps; the de Rham theorem says the gap is computable purely topologically. So when you see "compute $H^k_{dR}(M)$" the operational reading is "measure how much $d^2 = 0$ fails to be the only obstruction, on $M$" — and that quantity is intrinsically global.

**Inheritance: cohomological obstructions are inherited from the topology of the underlying space.** $H^k_{dR}$ is defined entirely from smooth structure — forms, derivatives, integrals — and yet by the de Rham theorem it agrees with singular cohomology, defined purely topologically. The smooth structure is *not* leaving any fingerprint on the answer. The Whitney approximation theorem is what makes this possible: every continuous map is homotopic to a smooth one, so the singular cohomology computed from continuous simplices is the same as that computed from smooth ones, and the de Rham–smooth-singular isomorphism then bridges to the smooth-singular–continuous-singular isomorphism. The inheritance: a smooth invariant turns out to be a topological one because the smooth structure is "rich enough" to compute the same answer as continuity, and the answer in turn comes from the underlying combinatorial topology of cell complexes.

**A trigger-reaction pattern for distributions: see a $1$-form $\omega$ defining a constraint, compute $\omega \wedge d\omega$.** If $\omega$ is a single nowhere-vanishing $1$-form on a manifold, the rank-$(n-1)$ distribution $D = \ker \omega$ is involutive iff $\omega \wedge d\omega = 0$ everywhere — a single algebraic identity that subsumes the entire involutivity check. If the identity holds, Frobenius produces a function $f$ (or a multiplicative integrating factor $\lambda$ with $\omega = \lambda \, df$) whose level sets are integral hypersurfaces; if it fails, no integral hypersurface exists at any point. The same wedge product is the contact-non-degeneracy condition $\omega \wedge (d\omega)^n \neq 0$ in odd dimensions $2n+1$ — Frobenius says "integrability iff $\omega \wedge d\omega = 0$," and contact geometry says "maximal non-integrability iff $\omega \wedge (d\omega)^n$ is a volume form." The two extremes share the same algebraic invariant, evaluated at opposite ends of the spectrum.

**Local-to-global propagation is the entire chapter.** The Poincaré lemma is purely local — it says every closed form has a *local* primitive. The whole chapter is then the story of how local primitives fail to globalize. Mayer–Vietoris is the precise accounting of that failure: the connecting map $\delta : H^{p}(U \cap V) \to H^{p+1}(M)$ is constructed by taking a class on the overlap, extending its representative to local primitives on $U$ and $V$, and recording the difference — a local mismatch that obstructs global glueing, hence sits in the next cohomology group. Likewise, Frobenius is the precise accounting of when local tangent planes glue into a global submanifold: involutivity says the local pieces *do* glue, non-involutivity says they don't, and the obstruction (the bracket leaving the distribution) is again a local computation whose global meaning is the existence-or-not of an integral submanifold. The chapter teaches that the gap between local solvability and global existence is always cohomological, and always computable.

**Density as a strategic lever: smooth approximation lets you import topological results into the smooth category.** The de Rham theorem statement compares two cohomology theories — one defined from smooth forms, one from continuous singular simplices — and the proof's hardest step is reconciling these. The Whitney approximation theorem says every continuous map is homotopic to a smooth one, and every continuous homotopy is homotopic (in the space of homotopies) to a smooth one. So the space of smooth simplices is *dense* in the space of continuous simplices in a homotopy-theoretic sense, and the dense-subclass strategy applies: prove a statement for smooth representatives (where calculus is available), use density to extend to continuous representatives (where the topological invariance holds). The same density argument runs in reverse to import topological computations into the smooth category — Mayer–Vietoris for singular cohomology was proven first, and the smooth version pulls it back via density. This pattern recurs whenever a smooth invariant turns out to be a topological one.
