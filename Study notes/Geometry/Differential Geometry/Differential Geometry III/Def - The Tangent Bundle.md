---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - The Tangent Space"
  - "Def - Coordinate Tangent Vectors"
  - "Def - The Differential of a Smooth Map"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth $n$-manifold. $T_{p}M$ is the [[Def - The Tangent Space|tangent space]] at $p \in M$. The symbol $\bigsqcup_{p \in M} T_{p}M$ denotes the disjoint union — element-wise, $(p, v)$ with $p \in M$ and $v \in T_{p}M$, where the same vector $v$ at two distinct points is treated as two distinct elements. We write $\pi : TM \to M$ for the **projection**, $(p, v) \mapsto p$. Local charts on $TM$ are written $\tilde\varphi$. The full notation registry is on [[Differential Geometry III — Tangent Vectors and the Differential]].

---

# Axiom Motivation

The motivation is to assemble the tangent spaces $T_{p}M$, as $p$ varies over $M$, into a single coherent geometric object. There are three converging reasons we need this.

First, **vector fields are global sections**. A vector field on $M$ is a smooth assignment of a tangent vector $X_{p} \in T_{p}M$ to each $p \in M$. Without a manifold structure on the union $\bigsqcup_{p} T_{p}M$, "smoothness of $X$" has no formal meaning — one would have to define it chart by chart with consistency checks. With a manifold structure on the union, smoothness of $X$ is just smoothness of a map $M \to TM$.

Second, **velocities of curves live in different tangent spaces along the curve, and we want to track them simultaneously**. The velocity of $\gamma : J \to M$ at $t_{0}$ is $\gamma'(t_{0}) \in T_{\gamma(t_{0})}M$. As $t_{0}$ varies, the velocity is in a varying tangent space. To say "the velocity is a smooth function of $t_{0}$" requires the velocities to live in a single smooth manifold — the tangent bundle.

Third, **dynamical systems on manifolds are ODE systems on $TM$, not on $M$**. A second-order ODE on $M$ is, in chart coordinates, $\ddot{x} = F(x, \dot{x})$; the natural setting is the doubled space "$\{(x, \dot{x})\}$", which is locally $\mathbb{R}^{n} \times \mathbb{R}^{n}$ but globally is $TM$. The Hamiltonian and Lagrangian formalisms of classical mechanics both live in $TM$ (or its cotangent dual $T^{*}M$).

Now the construction. Take the disjoint union $TM = \bigsqcup_{p \in M} T_{p}M$ as a set — every element is a pair $(p, v)$ with $p \in M$ and $v \in T_{p}M$. There is a natural projection $\pi : TM \to M$, $(p, v) \mapsto p$. We give $TM$ a topology and smooth structure by reading both from the manifold $M$.

The recipe is to use the chart-induced [[Def - Isomorphism|isomorphisms]] $T_{p}M \cong \mathbb{R}^{n}$ to build local charts on $TM$. Given a chart $(U, \varphi)$ on $M$ with coordinates $x^{i}$, every $(p, v) \in \pi^{-1}(U)$ — that is, every tangent vector at every point of $U$ — has chart coordinates: $p$ has coordinates $\varphi(p) = (x^{1}(p), \dots, x^{n}(p))$, and $v$ has components $v^{i}$ in the coordinate basis $\partial/\partial x^{i}|_{p}$. The pair $(p, v)$ thus gets coordinates $(x^{1}(p), \dots, x^{n}(p), v^{1}, \dots, v^{n}) \in \mathbb{R}^{2n}$. This defines a chart $\tilde\varphi : \pi^{-1}(U) \to \varphi(U) \times \mathbb{R}^{n}$ on $TM$, with $2n$ coordinates.

The non-trivial check is that these charts are smoothly compatible — i.e., the transition functions between $\tilde\varphi$ and $\tilde\psi$ (for two overlapping charts $\varphi, \psi$ on $M$) are smooth. The "position" half of the transition is just the original transition $\psi \circ \varphi^{-1}$; the "velocity" half acts on $v^{i}$ by the Jacobian of $\psi \circ \varphi^{-1}$, so the full transition is $(x, v) \mapsto (\psi \circ \varphi^{-1}(x), D(\psi \circ \varphi^{-1})_{x} \cdot v)$. Both pieces are smooth since transition maps of $M$ are smooth. The smoothness check is the content of [[Thm - The Tangent Bundle is a Smooth Manifold]].

The resulting smooth structure on $TM$ has a critical feature: it is **locally trivial**. Every chart $(U, \varphi)$ on $M$ gives a [[Def - Diffeomorphism|diffeomorphism]] $\pi^{-1}(U) \cong U \times \mathbb{R}^{n}$, the chart restricted to the manifold piece combined with the fibre identification. Globally, $TM$ need not be a product $M \times \mathbb{R}^{n}$ — that is the genuine geometric content.

Why insist that the *velocity* coordinates be in the same chart as the position coordinates? Because the components of $v$ are *defined* with respect to the chart $\varphi$. Picking a different chart on the position side forces a different velocity-basis, hence different velocity coordinates. The pairing of position and velocity charts is what makes the construction coordinate-independent at the manifold level (the *abstract* point and the *abstract* vector are intrinsic; their components are chart-dependent in the standard tensorial way).

Why is the disjoint union the right starting point? Because $T_{p}M$ and $T_{q}M$ are *different vector spaces* for $p \neq q$, and there is no canonical way to identify them. Treating them as disjoint reflects this fact. The manifold structure on the union is what *glues* them while preserving their distinction — locally they look glued (smoothly varying fibres), globally the gluing can be non-trivial.

A reader who has never seen the tangent bundle could invent it by the following route. Notice that vector fields and curves' velocities need a common home where smoothness in the base point makes sense. Take the disjoint union of all tangent spaces. Build charts from the manifold's charts, with double the coordinates (position + velocity). Verify smoothness of transitions via the chain rule. Acknowledge the global non-triviality as content (not bug). This is the canonical construction.

---

# The Definition

Let $M$ be a smooth $n$-manifold. The **tangent bundle** of $M$ is the disjoint union of all tangent spaces:
$$TM \;=\; \bigsqcup_{p \in M} T_{p}M \;=\; \{(p, v) : p \in M, \; v \in T_{p}M\}.$$
Elements of $TM$ are written $(p, v)$ or sometimes $v_{p}$ — the same vector at two different points is treated as two distinct elements.

The **projection** is the map
$$\pi : TM \to M, \qquad \pi(p, v) = p.$$
The **fibre** over $p \in M$ is $\pi^{-1}(p) = \{p\} \times T_{p}M \cong T_{p}M$, naturally a real vector space.

**Smooth structure (proved in [[Thm - The Tangent Bundle is a Smooth Manifold]]).** $TM$ carries a natural topology and smooth structure making it a smooth manifold of [[Def - Dimension|dimension]] $2n$. The smooth structure is generated by the **natural charts**: given a chart $(U, \varphi)$ on $M$ with coordinates $x^{1}, \dots, x^{n}$, define the natural chart $(\pi^{-1}(U), \tilde\varphi)$ on $TM$ by
$$\tilde\varphi(p, v) \;=\; (x^{1}(p), \dots, x^{n}(p), v^{1}, \dots, v^{n}) \;\in\; \mathbb{R}^{2n},$$
where $v = v^{i}\,\partial/\partial x^{i}|_{p}$ is the expansion of $v$ in the coordinate basis at $p$. These charts are smoothly compatible, and with respect to this structure $\pi$ is a smooth submersion.

**Local triviality.** For each chart $(U, \varphi)$, the natural chart $\tilde\varphi$ provides a [[Def - Diffeomorphism|diffeomorphism]]
$$\pi^{-1}(U) \;\cong\; U \times \mathbb{R}^{n}.$$
Globally, $TM$ need not be diffeomorphic to $M \times \mathbb{R}^{n}$; if it is, $M$ is called **parallelizable**.

**Functoriality.** A smooth map $F : M \to N$ induces a smooth map $dF : TM \to TN$ between the tangent bundles, called the **global differential**. The restriction of $dF$ to each fibre $T_{p}M$ is the differential $dF_{p}$, see [[Def - The Differential of a Smooth Map]]. The chain rule $d(G \circ F) = dG \circ dF$ holds globally — see [[Thm - Chain Rule for the Differential]]. The assignments $M \mapsto TM$ and $F \mapsto dF$ form a covariant functor $T : \mathrm{Diff} \to \mathrm{Diff}$ from smooth manifolds to themselves.

---

# Categorical / Structural Definition

The tangent bundle is the **first non-trivial example of a vector bundle** — a geometric structure that consists of a base manifold, a total space, a projection, and fibres that are vector spaces, with local triviality and smooth gluing data.

Formally, a **(rank-$k$ real) vector bundle** over a smooth manifold $M$ is a triple $(E, M, \pi)$ where $E$ is a smooth manifold (the **total space**), $\pi : E \to M$ is a smooth surjection, each fibre $\pi^{-1}(p)$ is a real vector space of [[Def - Dimension|dimension]] $k$, and $E$ is **locally trivial**: every $p \in M$ has an open neighbourhood $U$ such that there is a diffeomorphism $\Phi : \pi^{-1}(U) \to U \times \mathbb{R}^{k}$ with $\Phi$ restricting to a linear isomorphism on each fibre and commuting with the projections $\pi_{U} : \pi^{-1}(U) \to U$ and $\mathrm{pr}_{1} : U \times \mathbb{R}^{k} \to U$.

The tangent bundle is the rank-$n$ vector bundle over $M$ given by $E = TM$, $\pi$ the natural projection, and local trivializations the natural charts $\tilde\varphi$.

**Why this is the right framework.** Three reasons.

First, it lets us cleanly speak of **sections**: a *section* of a vector bundle $\pi : E \to M$ is a smooth map $\sigma : M \to E$ with $\pi \circ \sigma = \mathrm{id}_{M}$ — assigning each $p$ a vector in the fibre $\pi^{-1}(p)$. Sections of $TM$ are *vector fields* — see [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket]]. The vector-bundle formalism gives the space of sections, $\Gamma(E)$, as a [[Def - Module|module]] over $C^{\infty}(M)$, with a clean algebraic structure.

Second, it lets us systematically construct **derived bundles**: the dual bundle $E^{*}$ (whose fibre at $p$ is the dual of the fibre at $p$), tensor product bundles $E \otimes F$, exterior power bundles $\Lambda^{k} E^{*}$, and so on. Each derived bundle has the same base $M$ and is built fibre-by-fibre with the same gluing data. The cotangent bundle $T^{*}M$, the tensor bundles $T^{p,q}M$, and the differential-form bundles $\Lambda^{k} T^{*}M$ are all derived from $TM$ in this way; see [[Differential Geometry VI — Vector Bundles and the Cotangent Bundle]], [[Differential Geometry VII — Tensors and Tensor Fields]], [[Differential Geometry VIII — Differential Forms]].

Third, it lets us recognize the tangent bundle as one instance of a wider class of objects. **Fibre bundles** generalize vector bundles by replacing the fibre vector space with an arbitrary manifold; **principal bundles** are fibre bundles whose fibre is a Lie [[Def - Group|group]] acting freely. The tangent bundle is the special case where the fibre is $\mathbb{R}^{n}$ and the structure group is $\mathrm{GL}(n, \mathbb{R})$ (the group of linear automorphisms of $\mathbb{R}^{n}$, acting via the Jacobian on transitions). This places $TM$ in the broader landscape of gauge theory and characteristic classes.

The **transition functions** of $TM$ are the Jacobians: for overlapping charts $(U, \varphi)$ and $(V, \psi)$ on $M$ with transition $\psi \circ \varphi^{-1}$, the transition between the natural charts on $TM$ is
$$(x, v) \;\mapsto\; \left( \psi \circ \varphi^{-1}(x),\; D(\psi \circ \varphi^{-1})_{x} \cdot v \right).$$
The velocity part transforms linearly in $v$ — the structure group is $\mathrm{GL}(n, \mathbb{R})$. This linear-fibre-with-$\mathrm{GL}(n)$-structure-group is the defining feature of a vector bundle.

---

# Relate to Other Fields / Compression

In **multivariate analysis**, when $M = U \subseteq \mathbb{R}^{n}$ is an open subset, $TU = U \times \mathbb{R}^{n}$ canonically — the tangent bundle is just the product. The construction is trivial in this special case, which is why one rarely sees explicit tangent-bundle language in basic calculus. The interesting case is when $M$ is a non-trivial manifold, like the sphere.

**True name:** The tangent bundle is "the natural home of vector fields and curve velocities — a smooth $2n$-manifold packaging all tangent spaces with their gluing data". The operational content is that smooth maps $M \to TM$ over $\mathrm{id}_{M}$ are *exactly* vector fields, and smooth curves $J \to TM$ over a curve in $M$ are *exactly* velocity-decorated curves.

In **classical mechanics**, the tangent bundle of the configuration manifold $Q$ is the **state space of Lagrangian mechanics**. A point of $TQ$ is a pair (position, velocity), and the Lagrangian $L : TQ \to \mathbb{R}$ assigns an action density to each state. The Euler–Lagrange equations are an ODE on $TQ$ — equivalently a second-order ODE on $Q$ — whose solutions are the dynamics. This is the natural setting in which the tangent bundle was physically motivated.

In **gauge theory**, the tangent bundle is one example of a **principal $\mathrm{GL}(n)$-bundle's associated vector bundle**: the principal frame bundle $FM$ has fibre at $p$ the set of ordered bases of $T_{p}M$, and $TM$ is associated to $FM$ via the defining representation of $\mathrm{GL}(n)$. This perspective is foundational for Yang–Mills theory and characteristic classes.

In **algebraic topology**, the topology of $TM$ encodes information about $M$ via characteristic classes — the **Euler class** $e(TM) \in H^{n}(M)$, the **Pontryagin classes** $p_{i}(TM) \in H^{4i}(M)$, the **Chern classes** (for complex structures). The non-triviality of $TM$ as a vector bundle is exactly the non-vanishing of these classes. For $M = S^{2}$, the Euler class of $TS^{2}$ is the generator of $H^{2}(S^{2}) \cong \mathbb{Z}$, with value $2$ (the Euler characteristic of $S^{2}$) — this is the *quantitative form* of the hairy ball theorem.

---

# Examples / Corollaries

**Tangent bundle of $\mathbb{R}^{n}$.** $T\mathbb{R}^{n} = \mathbb{R}^{n} \times \mathbb{R}^{n}$ canonically. An element is a pair (point, vector), and the projection is the first-coordinate map. This is the trivial example.

**Tangent bundle of the circle $S^{1}$.** $TS^{1} \cong S^{1} \times \mathbb{R}$ (the circle is parallelizable). The diffeomorphism uses the nowhere-vanishing vector field $\partial/\partial \theta$ on $S^{1}$: a tangent vector at $\theta$ is $a\,\partial/\partial \theta|_{\theta}$, and the map $(p, a\,\partial/\partial \theta|_{p}) \mapsto (p, a)$ is the trivialization. This is the canonical first non-trivial computation of a tangent bundle, and the natural trivialization above is the model for the broader **vector-bundle trivialization** machinery developed in [[Differential Geometry VI — Vector Bundles and the Cotangent Bundle]].

**Tangent bundle of $S^{2}$ is NOT a product.** $TS^{2} \not\cong S^{2} \times \mathbb{R}^{2}$ as a vector bundle. The proof uses the **hairy ball theorem**: every continuous vector field on $S^{2}$ has a zero. The product $S^{2} \times \mathbb{R}^{2}$ has a nowhere-zero section, e.g., the constant section $p \mapsto (p, (1, 0))$. If $TS^{2}$ were a product, it too would have a nowhere-zero section, but the hairy ball theorem forbids this. So $TS^{2}$ is a non-trivial rank-2 vector bundle.

**Tangent bundle of a Lie group is trivial.** Every Lie group $G$ has a trivializable tangent bundle $TG \cong G \times \mathfrak{g}$, where $\mathfrak{g} = T_{e}G$ is the Lie algebra. The trivialization uses the left-translation isomorphism $T_{g}G \cong T_{e}G$ given by $(dL_{g^{-1}})_{g}$, where $L_{g^{-1}}$ is left multiplication by $g^{-1}$. So Lie [[Def - Group|groups]] are parallelizable. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]].

**Tangent bundle of $\mathrm{GL}(n, \mathbb{R})$.** $\mathrm{GL}(n)$ is an open subset of $M_{n}(\mathbb{R})$, so its tangent bundle is $\mathrm{GL}(n) \times M_{n}(\mathbb{R})$ — every point has tangent space $M_{n}(\mathbb{R})$, and the bundle is trivial.

**Is NOT a trivial bundle: $TS^{n}$ for positive $n \notin \{1,3,7\}$.** The classical theorem of Bott, Milnor, and Kervaire is that the only parallelizable spheres are $S^{1}, S^{3}, S^{7}$. This is a deep result connecting tangent bundles to the algebra of normed division algebras (real, complex, quaternion, octonion) — these are the only normed division algebras over $\mathbb{R}$, and they provide trivializations $TS^{n-1} \cong S^{n-1} \times \mathbb{R}^{n-1}$ for $n = 1, 2, 4, 8$.

**Corollary — the projection $\pi : TM \to M$ is a smooth submersion.** $\pi$ in coordinates is the projection $(x, v) \mapsto x$ from $\mathbb{R}^{2n}$ to $\mathbb{R}^{n}$, which has surjective differential. Hence $\pi$ is a smooth submersion globally, with each fibre an $n$-dimensional submanifold.

**Corollary — $TM$ is connected if $M$ is connected.** The fibres $T_{p}M$ are connected (they are vector spaces); the base $M$ is connected. The projection $\pi$ is continuous and surjective with connected fibres, so $TM$ is connected.

**Calibration check.** Verify that $T\mathbb{R}^{2} \cong \mathbb{R}^{4}$ as a manifold, with the natural coordinates $(x, y, v^{1}, v^{2})$. Verify that the projection $\pi : TS^{1} \to S^{1}$ has 1-dimensional connected fibres. Verify that $\dim TM = 2 \dim M$ for any smooth manifold $M$. If you can also explain why $TS^{2}$ cannot be diffeomorphic to $S^{2} \times \mathbb{R}^{2}$ (using the hairy ball theorem and the existence of nowhere-zero sections of a product), you have understood the global content of the tangent bundle.

---

# Unlocked by This

> [!tip] Vector Field as a Section *(from Differential Geometry)*
> A **vector field** on $M$ is a smooth section of $\pi : TM \to M$ — equivalently, a smooth map $X : M \to TM$ with $\pi \circ X = \mathrm{id}_{M}$. The space of vector fields $\Gamma(TM)$ is a module over $C^{\infty}(M)$. The Lie bracket $[X, Y]$ makes $\Gamma(TM)$ a Lie algebra. See [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket]].

> [!tip] Cotangent Bundle *(from Differential Geometry)*
> The **dual bundle** to $TM$ is the **cotangent bundle** $T^{*}M$, with fibre at $p$ the dual $T^{*}_{p}M$ of $T_{p}M$. Sections of $T^{*}M$ are **1-forms** or **covector fields**. The cotangent bundle is the natural phase space for Hamiltonian mechanics — a point of $T^{*}M$ is a (position, momentum) pair. See [[Differential Geometry VI — Vector Bundles and the Cotangent Bundle]].

> [!tip] Tensor Bundles *(from Differential Geometry)*
> Taking tensor powers and dualities of $TM$ produces the **tensor bundles** $T^{p,q}M$ of $(p, q)$-tensors. Sections are tensor fields. The metric tensor on a Riemannian manifold is a section of $T^{0,2}M$. See [[Differential Geometry VII — Tensors and Tensor Fields]] and [[Def - Tensor Product of Vector Spaces]] for the fibre-level construction.

> [!tip] Characteristic Classes *(from Algebraic Topology)*
> The **Euler class**, **Pontryagin classes**, and (for complex tangent bundles) **Chern classes** of $TM$ are cohomology classes of $M$ that obstruct the triviality of $TM$. The Euler class of $TS^{2}$ is twice the generator of $H^{2}(S^{2})$, encoding the Euler characteristic $\chi(S^{2}) = 2$ — and this is the quantitative form of the hairy ball theorem.

> [!tip] Lagrangian Mechanics *(from Classical Mechanics)*
> A **Lagrangian** is a smooth function $L : TQ \to \mathbb{R}$ on the tangent bundle of the configuration manifold. The Euler–Lagrange equations are an ODE on $TQ$ — equivalently a second-order ODE on $Q$ — whose solutions are the trajectories of the mechanical system. This is the dynamical setting in which the tangent bundle was first physically motivated.
