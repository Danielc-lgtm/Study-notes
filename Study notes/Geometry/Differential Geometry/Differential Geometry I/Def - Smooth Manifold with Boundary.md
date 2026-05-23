---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Topological Manifold"
  - "Def - Smooth Manifold"
  - "Def - Smooth Atlas and Smooth Structure"
tags: [geometry, differential-geometry]
---

# Notation

Throughout, $\mathbb{H}^n = \{(x^1, \dots, x^n) \in \mathbb{R}^n : x^n \geq 0\}$ is the **closed upper half-space** of $\mathbb{R}^n$, equipped with the subspace topology. Its interior and boundary as a subset of $\mathbb{R}^n$ are
$$\operatorname{Int} \mathbb{H}^n = \{x^n > 0\}, \qquad \partial \mathbb{H}^n = \{x^n = 0\}.$$
In dimension $n = 0$, $\mathbb{H}^0 = \mathbb{R}^0 = \{0\}$, $\operatorname{Int} \mathbb{H}^0 = \{0\}$, $\partial \mathbb{H}^0 = \emptyset$.

For a manifold $M$ with boundary, the **interior** $\operatorname{Int} M$ and the **boundary** $\partial M$ refer to the *manifold* interior and boundary (defined below), which in general differ from the topological interior and boundary of $M$ as a subset of any ambient space. For a non-empty smooth manifold *without* boundary, $\partial M = \emptyset$ and $\operatorname{Int} M = M$.

> [!warning] Convention: "manifold" vs. "manifold with boundary"
> Following Lee, "manifold" without qualification means *smooth manifold without boundary*. When we want to allow boundary points, we say "smooth manifold with boundary". A smooth manifold (without boundary) is automatically a smooth manifold with boundary whose boundary is empty; the converse holds iff the boundary is in fact empty. This is the **Lee convention**; some authors (especially in topology of manifolds) use "manifold" to mean "manifold with boundary" by default. We always disambiguate when context matters.

---

# Axiom Motivation

The whole apparatus of [[Def - Smooth Manifold|smooth manifolds]] excludes spaces with edges or corners: a closed interval $[0, 1]$ is not a smooth 1-manifold, because the endpoints have no neighbourhood homeomorphic to an *open* subset of $\mathbb{R}$. Yet for many constructions — most notably, **integration** ([[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem|DG IX]]) — we need to integrate over regions *with boundary*: the unit ball $\overline{\mathbb{B}^n}$, a closed hemisphere $S^n_+$, a manifold-with-corners that arises in optimization. The fundamental theorem of calculus — and its higher-dimensional incarnations Green, Gauss, Stokes — relates an integral over a domain to an integral over its boundary, and this requires a notion of "domain with smooth boundary."

The simplest extension is to allow chart targets to be open subsets of *either* $\mathbb{R}^n$ or the closed upper half-space $\mathbb{H}^n$. Points in the manifold with charts into $\operatorname{Int} \mathbb{H}^n = \{x^n > 0\}$ behave just like points in a smooth manifold; the new thing is points with charts into a neighbourhood of $\partial \mathbb{H}^n = \{x^n = 0\}$ — these are the *boundary points*. The local model "$\mathbb{R}^n$ or $\mathbb{H}^n$" captures the topological picture: a manifold with boundary looks locally like $\mathbb{H}^n$ near its boundary and like $\mathbb{R}^n$ in its interior.

Why $\mathbb{H}^n$ rather than other shapes — a half-space cut by a curved boundary, or a corner $\{x, y \geq 0\}$? Two reasons.

- *Topological universality*: any "domain in $\mathbb{R}^n$ with smooth boundary" — e.g., $\overline{\mathbb{B}^n}$ — is locally diffeomorphic to $\mathbb{H}^n$ near every boundary point. This follows from the implicit function theorem: a smooth function $f$ near a point where $\nabla f \neq 0$ can be straightened so that $f$ becomes the last coordinate, turning $\{f \leq 0\}$ into $\mathbb{H}^n$ near the point. So $\mathbb{H}^n$ is the universal local model.

- *Calculus respects the half-space structure*. The notion of "smooth function on $\mathbb{H}^n$" is well-defined: a function $f : U \to \mathbb{R}^k$ on an open $U \subseteq \mathbb{H}^n$ is *smooth* if it admits a smooth extension to some open neighbourhood $\widetilde{U} \subseteq \mathbb{R}^n$ of every point of $U$ — equivalently (by Borel's theorem), if all its partial derivatives extend continuously to $U$ including the boundary. With this definition, transition functions between $\mathbb{H}^n$-charts and $\mathbb{R}^n$-charts in the same atlas can be checked for smoothness in the usual way.

Corner-type spaces (e.g., the closed square $[0,1]^2$ in dimension 2, or the unit cube in higher dimensions) are *not* covered by this definition — they have boundary points where two boundary faces meet at a corner. These spaces are **manifolds with corners**, and Lee covers them in his chapter 16. For the purposes of this chapter we restrict to "smooth boundary" — manifolds where every boundary point has a chart from $\mathbb{H}^n$ (not from $\{x_1 \geq 0\} \cap \{x_2 \geq 0\}$).

Why the *closed* upper half-space rather than the open? Because we want the boundary points to be *in* the manifold. The "interior" upper half-space $\operatorname{Int} \mathbb{H}^n = \{x^n > 0\}$ is itself a manifold (an open subset of $\mathbb{R}^n$); only the closed $\mathbb{H}^n$ has a boundary.

The definition of "smoothness for maps with $\mathbb{H}^n$ as domain" deserves a remark. Lee's convention (which we follow) is: $F : U \to \mathbb{R}^k$ on $U \subseteq \mathbb{H}^n$ is smooth if it admits, locally near every point of $U$, a smooth extension $\widetilde{F}$ defined on an open neighbourhood $\widetilde{U} \subseteq \mathbb{R}^n$. By a result of Borel, this is equivalent to all partial derivatives of $F$ existing and being continuous up to the boundary. Notice the example: $g(x, y) = \sqrt{y}$ on $\mathbb{H}^2$ is *not* smooth in this sense — its $y$-derivative blows up as $y \to 0$.

The next subtlety is whether the "boundary" of a manifold with boundary is well-defined — i.e., does the notion of "boundary point" depend on which chart we chose? The answer is no, but the proof is nontrivial: it requires the *Theorem on Topological Invariance of the Boundary* (Lee Theorem 1.37; proved in chapter 17 using algebraic topology), or its weaker smooth cousin the *Smooth Invariance of the Boundary* (Lee Theorem 1.46; proved via the inverse function theorem). Both say: a point is either a boundary point with respect to *every* chart containing it, or with respect to *no* chart containing it. With this guarantee, the boundary $\partial M$ becomes a well-defined subset of $M$.

Finally, two important structural properties: $\partial M$ is itself a smooth $(n-1)$-manifold (without boundary!), and $\operatorname{Int} M = M \setminus \partial M$ is a smooth $n$-manifold (without boundary). This is the *boundary-of-a-boundary* structure: $\partial \partial M = \emptyset$, a fact mirrored in cohomology by $d^2 = 0$ for the exterior derivative on differential forms. The smooth structure on $\partial M$ is induced by restricting boundary charts: if $(U, \varphi)$ is a boundary chart of $M$ with $\varphi(U) \subseteq \mathbb{H}^n$, then $(U \cap \partial M, \varphi|_{U \cap \partial M})$ is a chart of $\partial M$ with image in $\partial \mathbb{H}^n \cong \mathbb{R}^{n-1}$.

---

# The Definition

**Topological manifold with boundary.** A **topological $n$-manifold with boundary** is a Hausdorff, second-countable topological space $M$ in which every point has an open neighbourhood homeomorphic to one of:
- An open subset of $\mathbb{R}^n$ (such a point is called an **interior point**), or
- A (relatively) open subset of $\mathbb{H}^n = \{x^n \geq 0\} \subseteq \mathbb{R}^n$ that meets $\partial \mathbb{H}^n$ (such a point is called a **boundary point**, provided the chart sends it to $\partial \mathbb{H}^n$).

An **interior chart** is a chart $(U, \varphi)$ with $\varphi(U) \subseteq \mathbb{R}^n$ open (no boundary); a **boundary chart** is a chart with $\varphi(U) \subseteq \mathbb{H}^n$ relatively open and $\varphi(U) \cap \partial \mathbb{H}^n \neq \emptyset$.

The **boundary** of $M$ is
$$\partial M = \{p \in M : \exists \text{ boundary chart } (U, \varphi) \text{ with } p \in U \text{ and } \varphi(p) \in \partial \mathbb{H}^n\}.$$

The **interior** of $M$ is $\operatorname{Int} M = M \setminus \partial M$.

By Lee's Theorem 1.37 (topological invariance of the boundary), this partition is well-defined — independent of the choice of charts.

**Smooth manifold with boundary.** A **smooth manifold with boundary** is a topological manifold with boundary $M$ equipped with a **smooth structure** — a maximal smooth atlas whose charts are charts of $M$ as above and whose transition functions are smooth in the Lee-Borel sense (admitting smooth extensions to open subsets of $\mathbb{R}^n$ across the boundary $\partial \mathbb{H}^n$).

By Lee's Theorem 1.46 (smooth invariance of the boundary), in a smooth manifold with boundary the partition $M = \operatorname{Int} M \sqcup \partial M$ is intrinsic — a point $p$ is in $\partial M$ iff every smooth chart containing $p$ sends $p$ to $\partial \mathbb{H}^n$.

**Standard consequences (Lee Proposition 1.38).**

- $\partial M$ is a closed subset of $M$ and is itself a topological $(n-1)$-manifold without boundary. In the smooth case, $\partial M$ inherits a smooth structure: boundary charts restrict to charts of $\partial M$.
- $\operatorname{Int} M$ is an open subset of $M$ and is a topological $n$-manifold without boundary, inheriting a smooth structure.
- $M$ has empty boundary iff $M$ is a manifold without boundary in the usual sense.
- In dimension $n = 0$: $\partial M = \emptyset$ for every $M$, and a $0$-manifold with boundary is just a $0$-manifold.

A smooth manifold without boundary is a smooth manifold with boundary whose boundary is empty.

---

# Categorical / Structural Definition

The category $\mathbf{Man}^\infty_{\partial}$ of smooth manifolds with boundary has manifolds with boundary as objects and smooth maps as morphisms (extending the notion of smooth map from boundary-less manifolds — see [[Differential Geometry II — Smooth Maps and Partitions of Unity|DG II]]). It contains $\mathbf{Man}^\infty$ as the full subcategory of objects with empty boundary.

The **boundary functor** $\partial : \mathbf{Man}^\infty_{\partial} \to \mathbf{Man}^\infty$, $M \mapsto \partial M$, is a (covariant) functor from manifolds with boundary to manifolds without boundary (the boundary of a manifold has empty boundary itself). A morphism $f : M \to N$ in $\mathbf{Man}^\infty_{\partial}$ restricts to a morphism $\partial f : \partial M \to \partial N$ provided $f(\partial M) \subseteq \partial N$ — a condition that does *not* hold for arbitrary smooth maps but is the relevant restriction in many contexts (especially **cobordism theory** in topology).

The structural picture: a manifold with boundary is a smooth manifold "modelled on $\mathbb{R}^n$ or $\mathbb{H}^n$". The class of local models has been doubled, and the transition functions take values in the *pseudogroup of $C^\infty$-local-diffeomorphisms of $\mathbb{R}^n$ or $\mathbb{H}^n$*. This is the prototype of a manifold with **corners** or **stratified structure**: replace the model "$\mathbb{R}^n$ or $\mathbb{H}^n$" by a richer hierarchy of strata (e.g., $\{x_1, \dots, x_k \geq 0\}$ for various $k$ giving corners of codimension $k$).

The **double** $DM$ of a manifold with boundary $M$ is the manifold without boundary obtained by gluing two copies of $M$ along $\partial M$:
$$DM = (M \sqcup M) / \sim, \quad p \sim p' \text{ for } p \in \partial M = \partial M'.$$
This is a useful technical device: any question about $M$ that respects the boundary can be lifted to a question about the boundary-less $DM$, which is often easier. For instance, smooth bump functions on $M$ are restrictions of smooth functions on $DM$, simplifying their construction.

---

# Relate to Other Fields / Compression

**True name:** A smooth manifold with boundary is "a smooth manifold whose charts may map into either $\mathbb{R}^n$ or the closed half-space $\mathbb{H}^n$." Whenever you need to integrate by parts, apply Stokes's theorem, or work with a region whose boundary is itself a smooth submanifold, you are working with a smooth manifold with boundary.

In **integration theory** (Riemann or Lebesgue), the domain of integration in $\mathbb{R}^n$ is typically a closed bounded region with smooth boundary — a manifold with boundary. Green's theorem $\oint_{\partial D} P \, dx + Q \, dy = \iint_D (\partial_x Q - \partial_y P) \, dA$ on a planar domain $D$ with smooth boundary is exactly Stokes's theorem for a 2-manifold with boundary; the divergence theorem $\int_\Omega \mathrm{div}\, F \, dV = \int_{\partial \Omega} F \cdot n \, dS$ is Stokes for a 3-manifold with boundary. The general Stokes's theorem $\int_M d\omega = \int_{\partial M} \omega$ on a smooth oriented $n$-manifold with boundary unifies all of these.

In **physics**, a *bounded domain* in a physical theory — a fluid in a container, a heat-equation problem on a finite interval, a quantum system in a confining potential — is modelled as a manifold with boundary. The boundary conditions of a PDE problem are conditions on $\partial M$. Without a notion of manifold with boundary, even the simplest variational principles cannot be set up.

In **algebraic topology**, **cobordism theory** is the study of manifolds with boundary up to the equivalence relation "$M_1 \sim M_2$ iff there exists a manifold-with-boundary $W$ with $\partial W = M_1 \sqcup (-M_2)$ (disjoint union with reversed orientation)." Cobordism groups $\Omega_n$ are the resulting invariants of $n$-manifolds, and they connect manifold theory to stable homotopy and characteristic-class theory.

In **gauge theory** (Donaldson, Seiberg–Witten), the moduli spaces of solutions to gauge-theoretic PDEs on a compact 4-manifold with boundary depend delicately on the boundary structure, and one studies how the moduli space behaves as the boundary varies. **Floer theory** is the differential geometry of paths in moduli spaces with controlled boundary.

In **optimization and physics**, *manifolds with corners* arise as feasible regions for constrained optimization or as the parameter spaces of constrained physical systems (e.g., a particle confined to a region with multiple walls meeting at corners). The category $\mathbf{Man}^\infty_{\partial}$ does not include corners, but extending to corners is a natural next step (Lee Chapter 16).

---

# Examples / Corollaries

**Is an instance: the closed unit ball $\overline{\mathbb{B}^n} = \{x \in \mathbb{R}^n : |x| \leq 1\}$.** A smooth $n$-manifold with boundary, with $\partial \overline{\mathbb{B}^n} = S^{n-1}$ and $\operatorname{Int} \overline{\mathbb{B}^n} = \mathbb{B}^n$. The construction (Lee Problem 1-11) uses an inversion to identify the closed ball with a "polar cap" that admits both an interior chart (the standard one on the open ball) and a boundary chart near the sphere. The smooth structure agrees with the smooth structure on the open ball and gives $S^{n-1}$ its standard smooth structure as the boundary.

**Is an instance: the closed unit interval $[0, 1]$.** A smooth 1-manifold with boundary, with $\partial[0, 1] = \{0, 1\}$ — a 0-manifold (two points). The interior is the open interval $(0, 1)$.

**Is an instance: the closed upper hemisphere $S^n_+ = \{x \in S^n : x^{n+1} \geq 0\}$.** A smooth $n$-manifold with boundary, with $\partial S^n_+ = S^{n-1}$ (the equator) and $\operatorname{Int} S^n_+$ the open upper hemisphere.

**Is an instance: the closed half-space $\mathbb{H}^n$ itself.** A smooth $n$-manifold with boundary, with $\partial \mathbb{H}^n = \{x^n = 0\} \cong \mathbb{R}^{n-1}$ and $\operatorname{Int} \mathbb{H}^n = \{x^n > 0\}$. This is the universal local model.

**Is an instance: a compact smooth manifold $M$ with $\partial M$ a copy of the boundary of a model thickened smooth handle attached at $\partial M$.** Morse-theory and handle-decomposition arguments produce a wealth of examples; any compact smooth manifold with boundary can be built by attaching handles to a ball.

**Is an instance: the Möbius band (with boundary).** The smooth quotient $[0, 1] \times [-1, 1] / \sim$ where $(0, y) \sim (1, -y)$. The result is a smooth 2-manifold with boundary; its boundary is a single circle (not two!), which is what makes the Möbius band non-orientable. The Möbius band *without boundary* (the open Möbius band) is a smooth 2-manifold without boundary, obtained by replacing $[-1, 1]$ with the open interval $(-1, 1)$.

**Is an instance: a *product* of a smooth manifold with a smooth manifold-with-boundary.** By Lee Proposition 1.45, if $M_1, \dots, M_k$ are smooth manifolds (without boundary) and $N$ is a smooth manifold with boundary, then $M_1 \times \cdots \times M_k \times N$ is a smooth manifold with boundary, with $\partial(M_1 \times \cdots \times M_k \times N) = M_1 \times \cdots \times M_k \times \partial N$.

**Is NOT an instance: the product $\mathbb{H}^2 \times \mathbb{H}^2$.** A product of two half-spaces is a *corner* — $\{(x_1, x_2, x_3, x_4) : x_2 \geq 0, x_4 \geq 0\}$ — and is not a smooth manifold with boundary in the sense of this definition. It is a smooth manifold with *corners*, a more general structure treated in Lee Chapter 16. The lesson: products preserve smoothness with boundary only if at most one factor has boundary.

**Is NOT an instance: the closed square $[0, 1]^2$.** Same reason: the corners $\{(0,0), (0,1), (1,0), (1,1)\}$ are points where two boundary arcs meet at a right angle, locally modelled on $\{x, y \geq 0\}$, not on $\mathbb{H}^2$. A smooth manifold with corners, not a smooth manifold with boundary.

**Is NOT an instance: an open subset of $\mathbb{H}^n$ that doesn't meet the boundary.** Such a set is just an open subset of $\mathbb{R}^n$ (since $\operatorname{Int} \mathbb{H}^n$ is open in $\mathbb{R}^n$), so it is a smooth manifold without boundary. A manifold-with-boundary needs *some* point sent to $\partial \mathbb{H}^n$.

**Corollary (boundary is closed).** $\partial M$ is closed in $M$: its complement $\operatorname{Int} M$ is open (every interior point has an interior chart, which is itself open in $M$).

**Corollary ($\partial M$ is a manifold of dimension $n-1$ without boundary).** Boundary charts restrict to charts of $\partial M$ via $(U, \varphi) \mapsto (U \cap \partial M, \varphi|_{U \cap \partial M})$, with image in $\partial \mathbb{H}^n \cong \mathbb{R}^{n-1}$. Hausdorff and second-countable inherited.

**Corollary ($\partial \partial M = \emptyset$).** The boundary of a boundary is empty: $\partial M$ is itself a manifold *without* boundary, so it has no further boundary. This is the topological content of "$d^2 = 0$" (the exterior derivative squares to zero), and is the boundary version of the chain-complex axiom in homology.

**Calibration check.** Verify that the closed disk $\overline{\mathbb{B}^2}$ is a smooth 2-manifold with boundary whose boundary is the circle $S^1$. Verify that $\partial([0, 1] \times S^1) = \{0, 1\} \times S^1$ — two disjoint circles, the two ends of the cylinder. Verify that the Möbius band (with boundary) has a *connected* boundary — one circle, not two — and explain why this is consistent with the Möbius band being non-orientable.

---

# Unlocked by This

> [!tip] Integration on Manifolds with Boundary *(from [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem|DG IX]])*
> The whole apparatus of integration on manifolds — compactly supported forms, the integral $\int_M \omega$ for an $n$-form $\omega$ on an oriented $n$-manifold-with-boundary — is built on the manifold-with-boundary framework. The **induced orientation on $\partial M$** is a piece of geometric data essential to Stokes's theorem.

> [!tip] Stokes's Theorem on Manifolds with Boundary *(from [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem|DG IX]])*
> For an oriented smooth $n$-manifold-with-boundary $M$ and a smooth compactly-supported $(n-1)$-form $\omega$ on $M$,
> $$\int_M d\omega = \int_{\partial M} \omega.$$
> This is *the* fundamental theorem of calculus on manifolds, encompassing Green, Gauss, and classical Stokes as special cases. Without manifolds-with-boundary, the right-hand side has nothing to integrate over and the theorem trivializes.

> [!tip] Cobordism Theory *(from Algebraic Topology)*
> Two closed smooth $n$-manifolds $M_1$ and $M_2$ are **cobordant** if there exists a compact smooth $(n+1)$-manifold-with-boundary $W$ with $\partial W = M_1 \sqcup (-M_2)$. Cobordism classes form a graded ring $\Omega_*$ (the **cobordism ring**), one of the fundamental invariants of manifolds. **Thom's theorem** computes the unoriented cobordism ring as a polynomial algebra. Cobordism is the bridge between manifold theory and stable homotopy theory.

> [!tip] Manifolds with Corners *(from Lee Chapter 16)*
> Allowing boundary points where multiple "boundary faces" meet at corners (e.g., the closed square, the simplex, the closed cube) requires a more general structure: *manifolds with corners*. The model is $\{x_1, \dots, x_k \geq 0\} \subseteq \mathbb{R}^n$ for various $k$, and the boundary acquires a stratified structure. This is essential for **simplicial structures**, for **optimization** with constraints, and for the **face structure** of polytopes.

> [!tip] Surgery Theory and Handle Decompositions *(from Differential Topology)*
> Every closed smooth manifold can be obtained from the empty manifold by a sequence of **handle attachments** — each step replacing a small region by a "handle" $D^k \times D^{n-k}$ attached along its boundary. This is the foundational technique of **surgery theory**, which classifies smooth manifolds in dimensions $\geq 5$ via algebraic invariants. The manifold-with-boundary framework is essential for setting up surgery.
