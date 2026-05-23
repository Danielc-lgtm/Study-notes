---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Coordinate Chart and Atlas"
  - "Def - Smooth Atlas and Smooth Structure"
  - "Def - Orientation of a Smooth Manifold"
tags: [geometry, differential-geometry, orientation, atlas]
---

# Notation

Throughout, $M$ is a smooth $n$-manifold, possibly with boundary. A chart is $(U, \varphi)$ with $\varphi : U \to \widehat U \subseteq \mathbb{R}^n$ (or $\mathbb{H}^n$ for a boundary chart). A transition map between two charts $(U, \varphi)$ and $(\widetilde U, \widetilde\varphi)$ is $\widetilde\varphi \circ \varphi^{-1} : \varphi(U \cap \widetilde U) \to \widetilde\varphi(U \cap \widetilde U)$. Its Jacobian matrix at $\varphi(p)$ is $D(\widetilde\varphi \circ \varphi^{-1})_{\varphi(p)} \in \mathrm{GL}(n, \mathbb{R})$. The full notation registry for the topic is at [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem]].

---

# Axiom Motivation

The pointwise-orientation formulation of [[Def - Orientation of a Smooth Manifold]] says "choose an orientation of each tangent space continuously". This is geometric and clean, but it is not the formulation in which one *computes*. When one actually works with a manifold — defining integrals, checking whether a chart is "compatible with the chosen orientation", building examples — one works in charts, and the orientation must be expressible in chart language. The oriented-atlas formulation does this.

The bridge is the **coordinate frame**. In a chart $(U, \varphi)$ with coordinates $x^1, \ldots, x^n$, each tangent space $T_pM$ for $p \in U$ has a distinguished basis $\big(\partial/\partial x^1|_p, \ldots, \partial/\partial x^n|_p\big)$ — the coordinate frame of the chart. Declaring this frame "positively oriented" assigns a specific orientation to $T_pM$. Doing this consistently across all $p \in U$ assigns an orientation to every tangent space in $U$ — and it does so continuously (the coordinate frame is smooth, hence the induced pointwise orientation is continuous). So *a chart determines an orientation on its domain*.

The question is then: when do two charts give *consistent* orientations on their overlap? At $p \in U \cap \widetilde U$, the two charts give two coordinate frames $(\partial/\partial x^i)$ and $(\partial/\partial\widetilde x^j)$. The change-of-basis matrix between them is the Jacobian of the transition map $\widetilde\varphi \circ \varphi^{-1}$:
$$\frac{\partial}{\partial\widetilde x^j} = \frac{\partial x^i}{\partial\widetilde x^j}\,\frac{\partial}{\partial x^i}.$$
The two frames define the same orientation of $T_pM$ iff this matrix has positive determinant. So *two charts give consistent orientations iff their transition map has positive Jacobian determinant*. An atlas in which this holds for every pair of overlapping charts — an **oriented atlas** — defines a coherent global orientation; conversely, every orientation arises from such an atlas.

**Per-axiom failure analysis: what breaks if we drop the positive-Jacobian condition?** Without it, two charts in the atlas might assign opposite orientations to the same tangent space. Then a vector field that is positively-oriented in one chart's frame is negatively-oriented in the other; the partition-of-unity sum defining $\int_M\omega$ gives different answers depending on which chart is used; the integral is not well-defined. The condition $\det D(\widetilde\varphi \circ \varphi^{-1}) > 0$ is precisely the condition that makes the partition-of-unity definition work.

**What if we instead demand positive Jacobian *everywhere* on $M$, not just on overlaps?** This is meaningless: the Jacobian is the Jacobian of a *transition map*, which is only defined on the overlap of two charts. The condition is local to overlaps and there is no global Jacobian to require positivity of.

**What if we strengthen to all transitions being *constant* with positive Jacobian — i.e. linear?** Then $M$ is locally affine and inherits a flat structure. This is a much stronger condition ("affine manifold") and includes only tori and other very specific examples. Most orientable manifolds are not affine.

**What if we weaken to "nonzero Jacobian"?** Every transition map is a [[Def - Diffeomorphism|diffeomorphism]], so its Jacobian is automatically nonzero. The nonzero-determinant condition is automatic; what matters is the *sign*. Demanding positive sign is exactly the index-2 reduction $\mathrm{GL}(n, \mathbb{R}) \to \mathrm{GL}_+(n, \mathbb{R})$ on transitions.

**Why a *maximal* oriented atlas?** Two different oriented atlases may describe the same orientation. The equivalence is: their union is again an oriented atlas. The unique maximal element of an equivalence class is the **maximal oriented atlas** — all charts whose coordinate frame is positively oriented. This is the canonical representative, in the same way that the smooth structure on $M$ is given by a maximal smooth atlas.

---

# The Definition

Let $M$ be a smooth $n$-manifold, possibly with boundary.

**Oriented atlas.** A smooth atlas $\mathcal{A} = \{(U_\alpha, \varphi_\alpha)\}_{\alpha \in I}$ on $M$ is **oriented** (or **consistently oriented**) if for every pair of charts $(U_\alpha, \varphi_\alpha), (U_\beta, \varphi_\beta) \in \mathcal{A}$ with $U_\alpha \cap U_\beta \neq \emptyset$, the transition map
$$\varphi_\beta \circ \varphi_\alpha^{-1} : \varphi_\alpha(U_\alpha \cap U_\beta) \to \varphi_\beta(U_\alpha \cap U_\beta)$$
has positive Jacobian determinant everywhere on its domain.

**Equivalence to orientation.** $M$ admits an oriented atlas iff $M$ is orientable in the sense of [[Def - Orientation of a Smooth Manifold]]. Given an oriented atlas $\mathcal{A}$, the corresponding orientation of $M$ is the one in which the coordinate frame $(\partial/\partial x^1, \ldots, \partial/\partial x^n)$ of each chart in $\mathcal{A}$ is positively oriented at every point. Conversely, given an orientation of $M$, the set of all charts whose coordinate frames are positively oriented forms an oriented atlas — the **maximal oriented atlas** compatible with the given orientation.

**Equivalence of oriented atlases.** Two oriented atlases $\mathcal{A}, \mathcal{B}$ define the same orientation iff $\mathcal{A} \cup \mathcal{B}$ is again an oriented atlas. Equivalently, iff for every $(U_\alpha, \varphi_\alpha) \in \mathcal{A}$ and $(V_\beta, \psi_\beta) \in \mathcal{B}$ with $U_\alpha \cap V_\beta \neq \emptyset$, the transition $\psi_\beta \circ \varphi_\alpha^{-1}$ has positive Jacobian.

**Positively / negatively oriented chart.** Once an orientation of $M$ is fixed, a chart $(U, \varphi)$ is **positively oriented** if its coordinate frame is positively oriented at every point of $U$, and **negatively oriented** otherwise. On a connected $U$, exactly one of these holds.

**Repairing a negatively oriented chart.** If $\varphi = (x^1, \ldots, x^n)$ is negatively oriented, the chart $\widetilde\varphi = (-x^1, x^2, \ldots, x^n)$ has Jacobian $-1$ times that of $\varphi$, hence is positively oriented. So every chart is either positively oriented or can be made so by negating one coordinate.

---

# Categorical / Structural Definition

An oriented atlas is a **reduction of the structure [[Def - Group|group]] of $TM$ from $\mathrm{GL}(n, \mathbb{R})$ to $\mathrm{GL}_+(n, \mathbb{R})$**. Concretely: the transition functions of the tangent bundle $TM$ are exactly the Jacobians of the chart transition maps; demanding positive Jacobian everywhere is demanding that these transition functions take values in $\mathrm{GL}_+(n, \mathbb{R}) \subset \mathrm{GL}(n, \mathbb{R})$.

In the **principal bundle** language: $TM$ is associated to a principal $\mathrm{GL}(n, \mathbb{R})$-bundle $\mathrm{Fr}(M)$ — the frame bundle of $M$, whose fiber over $p$ is the set of ordered bases of $T_pM$. An orientation of $M$ corresponds to a connected component of $\mathrm{Fr}(M)$, equivalently a reduction of $\mathrm{Fr}(M)$ to a principal $\mathrm{GL}_+(n, \mathbb{R})$-bundle. An oriented atlas is the explicit chart-level data realizing this reduction.

---

# Relate to Other Fields / Compression

The oriented-atlas formulation is the version of orientation that translates *directly* into computation: every concrete check of orientability, every concrete integration, every concrete change-of-variables proof, works chart-by-chart and refers back to the sign of the Jacobian. The pointwise-orientation formulation is more conceptual; the oriented-atlas formulation is more operational.

This is the same pattern as **smooth structure** ([[Def - Smooth Atlas and Smooth Structure]]): the pointwise definition (a smooth real-valued function on $M$ is one that is smooth in every chart) and the atlas definition (smooth-overlap charts) are equivalent, but the atlas version is what one uses in practice. An oriented atlas is the atlas version of "smooth oriented manifold".

**True name:** An oriented atlas is a smooth atlas in which all transition Jacobians lie in the identity component $\mathrm{GL}_+(n, \mathbb{R})$ of $\mathrm{GL}(n, \mathbb{R})$. Equivalently: a coherent choice of "positive frame" in every chart. This is what one *checks* when proving orientability constructively.

---

# Examples / Corollaries

**Is an instance — the standard atlas on $\mathbb{R}^n$.** The single chart $\varphi = \mathrm{id} : \mathbb{R}^n \to \mathbb{R}^n$ is trivially an oriented atlas (there are no overlapping charts to check). It induces the standard orientation $[dx^1\wedge\cdots\wedge dx^n]$.

**Is an instance — the stereographic atlas on $S^n$, with appropriate sign-correction.** The two stereographic projections from the north and south poles cover $S^n$; their transition map on the overlap $S^n \setminus \{N, S\}$ is the inversion $x \mapsto x/|x|^2$, which has Jacobian determinant $(-1)^n / |x|^{2n}$ — *negative* for $n$ odd, positive for $n$ even. To make this an oriented atlas, one negates the first coordinate of one of the two charts when $n$ is odd. This gives an oriented atlas, confirming that $S^n$ is orientable.

**Is an instance — affine charts on $\mathbb{CP}^n$.** The standard $n+1$ affine charts $U_j = \{[z_0 : \cdots : z_n] : z_j \neq 0\}$ with $\varphi_j([z]) = (z_0/z_j, \ldots, \widehat{z_j/z_j}, \ldots, z_n/z_j) \in \mathbb{C}^n \cong \mathbb{R}^{2n}$ have transition maps that are *complex-analytic* (Möbius transformations on each component), and complex-analytic maps have *positive* real Jacobian. So the affine atlas is automatically oriented, confirming that $\mathbb{CP}^n$ is orientable.

**Is NOT an instance — the natural atlas on the Möbius strip.** The Möbius strip can be covered by two charts (think of it as $[0, 1] \times (-1, 1)$ with identification $(0, y) \sim (1, -y)$). Any two-chart cover of this manifold must include a transition map with the identification $y \mapsto -y$ in some component, contributing a negative Jacobian factor. *No oriented atlas exists* — and this is the operational proof that the Möbius strip is non-orientable: try as you might, you cannot arrange every transition to have positive Jacobian.

**Is NOT an instance — the standard atlas on $\mathbb{RP}^2$.** $\mathbb{RP}^2 = S^2/\{\pm 1\}$, and the three affine charts (with coordinates corresponding to $z_i \neq 0$) have transition maps which, upon detailed computation, include an orientation-reversing component. No oriented atlas exists; $\mathbb{RP}^2$ is non-orientable.

**Corollary — every smooth manifold has a *smooth* atlas, but only orientable ones have an *oriented* smooth atlas.** Smoothness is a property of *each transition map individually* (it must be $C^\infty$). Orientability is a *coherence* condition on the *signs* of all transition Jacobians together. The smoothness condition is local; the orientation condition is global, and is what creates the obstruction.

**Corollary — orientability is checkable on any single atlas.** To check $M$ is orientable, one need not consider every smooth chart; it suffices to find *one* atlas, examine its transition Jacobians, and either confirm they are all positive (and the atlas is oriented) or attempt to repair negative ones by negating coordinates. If repair is impossible (some transition flips sign on a loop), $M$ is non-orientable.

**Corollary — the boundary atlas of $\partial M$.** If $\mathcal{A}$ is an oriented atlas on $M$ with boundary, the restriction of each boundary chart to $\partial M$ — using the convention "outward normal first" to convert ($M$-orientation) into ($\partial M$-orientation) — gives an oriented atlas on $\partial M$. See [[Def - Manifold with Boundary and Induced Orientation]].

**Calibration check.** Verify that the standard atlas on $\mathbb{R}^n$ is oriented; that any two of its charts (open balls with embedded inclusions) have positive-Jacobian transitions; that the stereographic atlas on $S^2$ has a sign-correctable transition; and that the Möbius strip's two-chart cover has an unavoidable negative-Jacobian transition. If you can also explain why an oriented atlas is "a reduction of $\mathrm{GL}(n, \mathbb{R})$-structure to $\mathrm{GL}_+(n, \mathbb{R})$", you have understood the structural picture.

---

# Unlocked by This

> [!tip] Orientation Computations via Charts *(continued in this topic)*
> Every concrete proof that a specific manifold is orientable — sphere, torus, Lie group, $\mathbb{CP}^n$, etc. — uses the oriented-atlas formulation: build an atlas, check the signs of the Jacobians. See exercises in §9.1.

> [!tip] Structure-Group Reductions *(from Differential Geometry / Gauge Theory)*
> The reduction $\mathrm{GL}(n, \mathbb{R}) \to \mathrm{GL}_+(n, \mathbb{R})$ for orientability is the simplest of a hierarchy of structure-group reductions on $TM$: a Riemannian metric is a reduction to $\mathrm{O}(n)$, an orientation plus a Riemannian metric to $\mathrm{SO}(n)$, a spin structure to $\mathrm{Spin}(n)$, an almost-complex structure to $\mathrm{GL}(k, \mathbb{C})$ (for $n = 2k$), etc. Each reduction encodes a geometric structure on $M$, and each comes with characteristic-class obstructions.
