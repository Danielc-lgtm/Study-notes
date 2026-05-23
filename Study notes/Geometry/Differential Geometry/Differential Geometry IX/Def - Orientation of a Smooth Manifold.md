---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Orientation of a Vector Space"
  - "Def - Differential k-Form on a Manifold"
  - "Def - Coordinate Chart and Atlas"
tags: [geometry, differential-geometry, orientation]
---

# Notation

Throughout, $M$ is a smooth $n$-manifold (Hausdorff, second-countable), possibly with boundary. For each point $p \in M$, $T_pM$ is its tangent space, of dimension $n$ ([[Def - The Tangent Space]]). A **pointwise orientation** is the data of an orientation $\mathcal{O}_p$ of each $T_pM$, in the sense of [[Def - Orientation of a Vector Space]]. A **local frame** on an open set $U \subseteq M$ is a tuple $(E_1, \ldots, E_n)$ of smooth vector fields on $U$ such that $(E_1|_p, \ldots, E_n|_p)$ is a basis of $T_pM$ for every $p \in U$. The notation registry for the topic lives at [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem]].

This page is a compound page: it covers three equivalent formulations of orientation on a smooth manifold — *via pointwise orientations made continuous*, *via oriented atlases*, and *via a nowhere-vanishing top-degree form* — because they are introduced together and none is fully usable without the others.

---

# Axiom Motivation

We have orientation on a vector space — a choice of "positive basis class" — and the natural question is whether this can be done *consistently for all the tangent spaces of a manifold at once*. The point-by-point data is easy: for each $p$, the tangent space $T_pM$ is a real $n$-dimensional vector space, so it has exactly two orientations. The hard question is the global one: can these pointwise choices be made coherent across nearby points?

The naive answer "just make the choice at every point" — what Lee calls a *pointwise orientation* — is too weak. Nothing prevents the choice from being incoherent: in $\mathbb{R}^n$, a pointwise orientation might switch randomly from the standard orientation to its opposite, with no continuity. Such a thing is mathematically a function but not a geometric object — it has no use in integration, in measuring volumes, in any of the things orientations are *for*. We need a continuity condition that ties nearby orientations together.

The continuity condition should say: *around every point there is some way of writing the orientation that varies smoothly across a neighborhood*. The natural such "way of writing" is via a local frame — an ordered $n$-tuple of smooth vector fields giving a basis at each point. A pointwise orientation is **continuous** if every point lies in the domain of a local frame that is positively oriented at every point in its domain. This is the right definition because (a) it is local (we only need to check it in a neighborhood of each point); (b) it is automatically smooth in the relevant sense (local frames are smooth, the orientation they pick out varies smoothly); (c) it is equivalent to the other natural notions (oriented atlas, nowhere-vanishing top-form), which we now examine.

The **oriented atlas** formulation is forced by asking: when do two coordinate charts give *consistent* orientations on their overlap? In a chart $(U, \varphi)$ with coordinates $x^1, \ldots, x^n$, the coordinate vector fields $\partial/\partial x^1, \ldots, \partial/\partial x^n$ form a local frame. Calling this frame positively oriented assigns the orientation $[\partial/\partial x^1, \ldots, \partial/\partial x^n]$ at each point of $U$. Now consider two such charts $(U, \varphi)$ and $(\widetilde U, \widetilde\varphi)$ with overlap. At a point $p \in U \cap \widetilde U$, the coordinate frames are related by the Jacobian matrix of the transition map $\widetilde\varphi \circ \varphi^{-1}$: each $\widetilde\partial_j = \sum_i (\partial x^i / \partial\widetilde x^j)\,\partial_i$. The two frames pick out the same orientation of $T_pM$ iff this Jacobian has positive determinant. So a smooth atlas in which every transition map has positive Jacobian determinant on its domain — an **oriented atlas** — defines a continuous pointwise orientation, and conversely every continuous pointwise orientation has such an atlas (just take all charts whose coordinate frames are positively oriented). The two formulations are equivalent.

The **nowhere-vanishing top-form** formulation is the most concise. By the [[Def - Orientation of a Vector Space|vector-space picture]], an orientation of $T_pM$ is a choice of generator-up-to-positive-scalar for the one-dimensional space $\Lambda^n(T^*_pM)$. A globally smooth choice of such generators — that is, a *nowhere-vanishing smooth section of the line bundle* $\Lambda^n(T^*M)$ — is a nowhere-vanishing smooth $n$-form $\omega \in \Omega^n(M)$. Such a form determines a pointwise orientation: declare a basis $(E_1, \ldots, E_n)$ of $T_pM$ positive iff $\omega_p(E_1, \ldots, E_n) > 0$. Continuity is automatic because $\omega$ is smooth. So a nowhere-vanishing top-form gives a continuous pointwise orientation, and the converse is the theorem [[Thm - A Manifold is Orientable iff it Admits a Nowhere-Vanishing Top Form]] — provable via a partition-of-unity gluing argument. The three formulations are equivalent.

**Per-axiom failure analysis: what breaks if we drop continuity?** Without the continuity condition, a "pointwise orientation" is just an arbitrary function $M \to \{+, -\}$, with no relation to the smooth structure. Such a function has no use: one cannot pull back to a chart in a consistent way (the chart's coordinate frame might be positive at some points and negative at others), the integral of a top-form depends on which pointwise choice is made at each point, and integration becomes ill-defined. The continuity is what links the pointwise data to the smooth structure of $M$. Dropping it would make orientation a pointwise-algebra question with no analytic consequences.

**What if we strengthen by demanding existence of a *global* oriented frame?** This is strictly stronger than orientability and is called **parallelizability**: $M$ is parallelizable iff there is a global frame on $M$. Every parallelizable manifold is orientable (just take the orientation determined by the global frame), but the converse is false — $S^2$ is orientable but not parallelizable (by the [[Thm - Existence and Uniqueness of Integral Curves|hairy ball theorem]], any continuous vector field on $S^2$ vanishes somewhere, hence there is no global frame). Demanding parallelizability would exclude $S^2$, $\mathbb{CP}^n$ for $n \neq 1$, and most other interesting examples, so the right level is "local frame at every point", which is automatic, plus the much weaker "positively oriented local frame at every point", which is the continuity condition.

**What if we demand existence of a *global* nowhere-vanishing top-form?** This is exactly the orientability criterion ([[Thm - A Manifold is Orientable iff it Admits a Nowhere-Vanishing Top Form|orientability ⟺ existence of a top-form]]). So the "strengthening" turns out to be equivalent to the original; this is the theorem and is the most useful operational form of the definition.

**What if we work over $\mathbb{C}$?** A complex manifold has a complexified tangent bundle with structure [[Def - Group|group]] $\mathrm{GL}(n, \mathbb{C})$ — which is *connected*, so there is no two-component story. Every complex manifold's underlying real manifold is canonically oriented. The interesting orientation theory is therefore a *real* phenomenon, tied to the disconnectedness of $\mathrm{GL}(n, \mathbb{R})$.

---

# The Definition

Let $M$ be a smooth $n$-manifold, possibly with boundary.

**(Pointwise via continuous frame.)** A **pointwise orientation** on $M$ is a choice of orientation $\mathcal{O}_p$ of each tangent space $T_pM$ ($p \in M$). A pointwise orientation is **continuous** if every point $p \in M$ lies in the domain of a local frame $(E_1, \ldots, E_n)$ such that $(E_1|_q, \ldots, E_n|_q)$ is positively oriented in $T_qM$ for every $q$ in the frame's domain.

An **orientation** of $M$ is a continuous pointwise orientation. $M$ is **orientable** if it admits an orientation, and **oriented** if equipped with one. An **oriented manifold** is a pair $(M, \mathcal{O})$ with $\mathcal{O}$ an orientation of $M$. The opposite orientation, denoted $-\mathcal{O}$ or $\overline{\mathcal{O}}$, reverses the pointwise choice at every point.

**(Atlas formulation.)** Equivalently, an orientation of $M$ corresponds to an **oriented atlas**: a smooth atlas $\{(U_\alpha, \varphi_\alpha)\}$ in which every transition map $\varphi_\beta \circ \varphi_\alpha^{-1} : \varphi_\alpha(U_\alpha \cap U_\beta) \to \varphi_\beta(U_\alpha \cap U_\beta)$ has positive Jacobian determinant everywhere on its domain. Two oriented atlases define the same orientation iff their union is again an oriented atlas. (See [[Def - Oriented Atlas]].)

**(Top-form formulation.)** Equivalently, an orientation of $M$ corresponds to an equivalence class of nowhere-vanishing smooth $n$-forms $\omega \in \Omega^n(M)$, where two such forms are equivalent iff $\omega_1 = f\,\omega_2$ for some everywhere-positive smooth function $f \in C^\infty(M, \mathbb{R}_{>0})$. (See [[Def - Volume Form]] and [[Thm - A Manifold is Orientable iff it Admits a Nowhere-Vanishing Top Form]].)

**Special case: 0-manifolds.** A 0-manifold is a discrete set of points; an orientation assigns $\pm 1$ to each point. This is forced by the convention that the boundary orientation must work in [[Def - Dimension|dimension]] 1: $\partial[0, 1] = \{1\} - \{0\}$ with the right endpoint positive and the left negative.

**Connectedness.** A connected orientable manifold of positive [[Def - Dimension|dimension]] has exactly two orientations. If $M$ is not connected, the number of orientations is $2^k$ where $k$ is the number of connected components: an orientation may be chosen independently on each component.

---

# Categorical / Structural Definition

The tangent bundle $TM \to M$ of any smooth $n$-manifold $M$ is a rank-$n$ real vector bundle with structure [[Def - Group|group]] $\mathrm{GL}(n, \mathbb{R})$ (the transition functions of $TM$ are the Jacobians of the chart transitions). An **orientation** of $M$ is precisely a reduction of this structure group from $\mathrm{GL}(n, \mathbb{R})$ to the index-2 [[Def - Subgroup|subgroup]] $\mathrm{GL}_+(n, \mathbb{R})$ of positive-determinant matrices.

Equivalently: the **orientation line bundle** $\det(T^*M) = \Lambda^n(T^*M)$ is a real line bundle over $M$. $M$ is orientable iff this line bundle is *trivial* (admits a nowhere-vanishing global section), and an orientation is exactly a choice of trivialization up to positive rescaling.

Equivalently: from the **classifying space** viewpoint, the rank-$n$ tangent bundle is classified by a [[Def - Homotopy|homotopy]] class of maps $M \to BO(n)$; orientability is the lift to $BSO(n)$, and the obstruction to such a lift is a single $\mathbb{Z}/2$-cohomology class — the first Stiefel–Whitney class $w_1(TM) \in H^1(M; \mathbb{Z}/2)$. $M$ is orientable iff $w_1(TM) = 0$, and the set of orientations is a torsor over $H^0(M; \mathbb{Z}/2) = (\mathbb{Z}/2)^{\#\text{components}}$.

---

# Relate to Other Fields / Compression

The manifold-level notion of orientation is the **global assembly of the pointwise vector-space notion**, with the gluing condition forced by the dual roles of $d$ and $\det$. The obstruction to assembly is exactly that the tangent bundle's structure group $\mathrm{GL}(n, \mathbb{R})$ has two connected components — and the obstruction class is the first Stiefel–Whitney class, the prototype of all characteristic-class obstructions.

In **physics**, orientability has a concrete operational meaning: a spacetime is *space-orientable* iff the notion of "right-hand" can be transported coherently around any closed loop, and *time-orientable* iff a "future" direction can be similarly chosen. Lorentzian manifolds in general relativity are typically assumed both orientable and time-orientable; a non-time-orientable Lorentzian manifold has closed causal curves and is pathological.

**True name:** An orientation of $M$ is a *choice of trivialization of the orientation line bundle* $\Lambda^n(T^*M)$ — equivalently, a coherent global choice of "positive top-form direction". This is the operational form: most concrete checks of orientability come down to building (or refuting) a global section of this line bundle.

---

# Examples / Corollaries

**Is an instance — $\mathbb{R}^n$.** The standard orientation: the class of $dx^1\wedge\cdots\wedge dx^n$, equivalently the class of the standard coordinate frame $(\partial_1, \ldots, \partial_n)$. Every open subset inherits an orientation from $\mathbb{R}^n$.

**Is an instance — the sphere $S^n$ for any $n \geq 1$.** $S^n$ embeds in $\mathbb{R}^{n+1}$ as a hypersurface, with outward normal $N = x^i\partial_i$. The form $\iota_N(dx^1\wedge\cdots\wedge dx^{n+1})$ restricts to a nowhere-vanishing $n$-form on $S^n$, giving its **standard orientation**. Explicitly, for $S^2$ this is $x\,dy\wedge dz + y\,dz\wedge dx + z\,dx\wedge dy$. All spheres are orientable.

**Is an instance — $\mathbb{CP}^n$.** Complex projective space is orientable for every $n$, because it is a complex manifold and complex manifolds are canonically oriented (their structure group is $\mathrm{GL}(n, \mathbb{C})$, which is connected, lying inside the orientation-preserving real $\mathrm{GL}_+(2n, \mathbb{R})$). Concretely, the top power of the Fubini–Study Kähler form, $\omega^n_{FS}$, is a nowhere-vanishing $(2n)$-form.

**Is an instance — every Lie group.** A Lie group $G$ of dimension $n$ has a global frame given by a basis of left-invariant vector fields (a basis of the Lie algebra, left-translated everywhere). Hence $G$ is parallelizable, hence orientable. The induced orientation is left-invariant.

**Is NOT an instance — the Möbius strip.** The Möbius strip $E$ admits no nowhere-vanishing 2-form: any candidate, transported once around the core circle, returns with its sign reversed and must therefore pass through zero. So $E$ is non-orientable. The orientation line bundle of $E$ is the canonical non-trivial real line bundle over $S^1$.

**Is NOT an instance — $\mathbb{RP}^n$ for $n$ even.** Real projective space $\mathbb{RP}^n$ is orientable iff $n$ is odd. The obstruction: $\mathbb{RP}^n = S^n/\{\pm 1\}$, and the antipodal map $\alpha : S^n \to S^n$ has degree $(-1)^{n+1}$, so it preserves orientation iff $n$ is odd. Quotienting by an orientation-preserving free action gives an orientable quotient; quotienting by an orientation-reversing one gives a non-orientable quotient. In particular $\mathbb{RP}^2$ is non-orientable.

**Is NOT an instance — the Klein bottle.** The Klein bottle $K = T^2 / \mathbb{Z}_2$ (where the involution flips one factor and reflects the other) is non-orientable, by the same kind of orientation-reversing-deck-transformation argument as the Möbius strip and $\mathbb{RP}^2$.

**Corollary — open subsets of orientable manifolds are orientable.** Restrict the orientation: a nowhere-vanishing $\omega$ on $M$ restricts to a nowhere-vanishing $\omega|_U$ on any open $U \subseteq M$. So every open subset of $\mathbb{R}^n$, of a sphere, of a Lie group, etc., is automatically orientable.

**Corollary — products of orientable manifolds are orientable.** If $\omega_M$ and $\omega_N$ are orientations of $M$ and $N$, then $\pi_M^*\omega_M \wedge \pi_N^*\omega_N$ is an orientation of $M \times N$ — the **product orientation**. The converse also holds: $M \times N$ orientable iff both $M$ and $N$ are (assuming both nonempty positive-dimensional).

**Corollary — orientability is preserved by smooth covering maps in one direction.** If $\pi : \widetilde M \to M$ is a smooth covering map and $M$ is orientable, then $\widetilde M$ inherits the pullback orientation $\pi^*\mathcal{O}$ and is orientable. The converse can fail: $S^n \to \mathbb{RP}^n$ has orientable total space, but $\mathbb{RP}^n$ is non-orientable when $n$ is even.

**Calibration check.** Verify that $S^2$ is orientable via the outward normal; that $\mathbb{R}^n \setminus \{0\}$ is orientable for every $n$ (it inherits from $\mathbb{R}^n$); that the Möbius strip's failure to be orientable is exactly the failure of $dx \wedge dy$ to glue under the identification $(0, y) \sim (1, -y)$; and that "orientable + connected" implies "exactly two orientations". If you can also explain why $\mathbb{CP}^n$ is orientable but $\mathbb{RP}^{2k}$ is not, you have understood the structural picture.

---

# Unlocked by This

> [!tip] Integration of Top-Forms *(continued in this topic)*
> An orientation is the *exact* extra data needed to integrate a top-degree form on a manifold in a chart-independent way; see [[Def - Integral of a Compactly Supported Form on a Manifold]]. The change-of-variables sign $\det DF$ matches positive-Jacobian transitions exactly.

> [!tip] Stokes's Theorem *(continued in this topic)*
> Stokes's theorem $\int_M d\omega = \int_{\partial M}\omega$ requires both $M$ and $\partial M$ to be oriented, with $\partial M$ carrying the *induced* orientation. See [[Thm - Stokes' Theorem on Manifolds]] and [[Def - Manifold with Boundary and Induced Orientation]].

> [!tip] Orientation Double Cover *(from Algebraic Topology)*
> Every non-orientable connected manifold $M$ has a canonical 2-sheeted covering space $\widetilde M$, the **orientation double cover**, on which the pullback orientation exists. The deck involution $\widetilde M \to \widetilde M$ is orientation-reversing. For the Möbius strip the double cover is the cylinder $S^1 \times \mathbb{R}$; for $\mathbb{RP}^{2k}$ it is $S^{2k}$.

> [!tip] First Stiefel–Whitney Class *(from Algebraic Topology)*
> Orientability is detected by a single $\mathbb{Z}/2$-cohomology class, $w_1(M) \in H^1(M; \mathbb{Z}/2)$. $M$ is orientable iff $w_1(M) = 0$. This is the first of the **Stiefel–Whitney classes**, characteristic classes that obstruct geometric constructions on bundles.

> [!tip] Time Orientability and Spacetime *(from General Relativity)*
> In general relativity, a Lorentzian 4-manifold is **time-orientable** iff it admits a continuous timelike vector field — a continuous choice of "future" at every point. Time-orientability is independent of space-orientability; physically reasonable spacetimes are typically assumed both, but examples of non-time-orientable Lorentzian manifolds exist and feature closed timelike curves.
