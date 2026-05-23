---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Differential k-Form on a Manifold"
  - "Def - Orientation of a Smooth Manifold"
tags: [geometry, differential-geometry, orientation, volume-form]
---

# Notation

Throughout, $M$ is a smooth $n$-manifold of dimension $n \geq 1$, possibly with boundary. $\Omega^n(M)$ denotes the space of smooth $n$-forms on $M$ (top-degree forms); $\Omega^n_c(M)$ those with compact support. A form $\omega \in \Omega^n(M)$ is **nowhere-vanishing** if $\omega_p \neq 0$ in the one-dimensional vector space $\Lambda^n(T^*_pM)$ for every $p \in M$. The notation registry for the topic is at [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem]].

---

# Axiom Motivation

We want an object that **measures $n$-dimensional volume** on an $n$-manifold — something one can integrate to get a number that means "the size of a region". The pointwise requirement is clear: at each $p \in M$, we want an alternating multilinear function $T_pM \times \cdots \times T_pM \to \mathbb{R}$ that takes $n$ tangent vectors $v_1, \ldots, v_n$ and returns "the signed $n$-dimensional volume of the parallelepiped they span". By multilinearity of the parallelepiped's volume (in each input separately) and alternation (linearly dependent vectors give zero volume), this is exactly the data of an element of $\Lambda^n(T^*_pM)$ — that is, a top-degree covector.

So pointwise, a "volume meter" on $M$ is a top-degree covector at each point. To make it useful — to make it integrate to give the volume of a region — we need it to vary *smoothly* across $M$. A smooth choice of top-covector at each point is an element of $\Omega^n(M)$, a smooth $n$-form.

The crucial extra requirement is that the volume meter be **nowhere zero**. Why? Because a vanishing volume meter at a point $p$ would mean "no $n$-tuple of tangent vectors at $p$ has nonzero volume", which contradicts what we want a volume meter to do. More importantly, a nowhere-vanishing top-form is what makes orientation possible: each $\omega_p \in \Lambda^n(T^*_pM) \setminus \{0\}$ picks out one of the two rays of $\Lambda^n(T^*_pM) \setminus \{0\}$, and smoothness plus nowhere-vanishing means this choice is continuous. Conversely, if $\omega$ vanishes at $p$, then any candidate orientation at $p$ is undetermined by $\omega$, breaking the link between volume forms and orientations. The two requirements — *smooth* and *nowhere-vanishing* — are exactly what is needed to make a top-form into a "volume meter that orients".

**Per-axiom failure analysis: what breaks if we drop "nowhere-vanishing"?** A smooth top-form $\omega$ that vanishes at some points $Z = \{p : \omega_p = 0\}$ still defines an integral $\int_M\omega$ (the vanishing set is typically measure-zero), but it does not define an orientation: at points in $Z$ the form is zero and so cannot pick out a positive ray of $\Lambda^n(T^*_pM)$. So the link "volume form ↔ orientation" breaks. Also, important quantities like the inverse volume form $1/\omega$ (used in defining the divergence operator) become singular at $Z$.

**What if we drop "smooth"?** A merely continuous top-form is fine for elementary integration but cannot be differentiated; one cannot apply $d$ to it or define $\mathcal{L}_X\omega$, which closes off most of the relevant machinery (Stokes's theorem, the divergence operator, the Hodge star). Smoothness is the right hypothesis for differential-geometric applications.

**What if we strengthen by demanding $\omega$ be *parallel* (in a Riemannian sense)?** This is much stronger: it requires the manifold to carry a metric, the metric to be flat (so the parallel transport of $\omega$ is consistent), and $\omega$ to be the volume form of this flat metric. This recovers only $\mathbb{R}^n$ and flat tori — most manifolds do not admit parallel volume forms but do admit nowhere-vanishing ones.

**What if we strengthen by demanding $\omega$ be *closed*, $d\omega = 0$?** This is automatic: $\omega$ is a top-form, so $d\omega$ is an $(n+1)$-form, of which there are none on an $n$-manifold ($\Omega^{n+1}(M) = 0$). So $d\omega = 0$ for free, and this is not a real extra condition. Note however that "closed-and-not-exact" is not automatic — the area form on $S^2$ is closed but not exact, giving a nontrivial element of $H^2_{dR}(S^2) = \mathbb{R}$.

---

# The Definition

Let $M$ be a smooth manifold of [[Def - Dimension|dimension]] $n \geq 1$.

**Volume form.** A **volume form** (also called an **orientation form** or a **top-degree form**) on $M$ is a smooth nowhere-vanishing $n$-form $\omega \in \Omega^n(M)$.

**Equivalence relation: same orientation.** Two volume forms $\omega_1, \omega_2$ on $M$ are **equivalent** (or determine the same orientation) iff there exists an everywhere-positive smooth function $f \in C^\infty(M, \mathbb{R}_{>0})$ with $\omega_1 = f\omega_2$. The equivalence classes are exactly the orientations of $M$ — this is the content of the equivalence $\mathrm{(orientation)} \leftrightarrow \mathrm{(nowhere-vanishing\ top-form\ up\ to\ positive\ scaling)}$ from [[Def - Orientation of a Smooth Manifold]].

**Positively oriented volume form.** If $M$ is oriented, a volume form $\omega$ is **positively oriented** (with respect to the chosen orientation) iff for every positively-oriented basis $(E_1, \ldots, E_n)$ of $T_pM$, $\omega_p(E_1, \ldots, E_n) > 0$.

**Volume of a compact subset.** If $M$ is oriented with positively-oriented volume form $\omega$, and $K \subseteq M$ is a compact region whose boundary has measure zero (a "domain of integration"), the **volume of $K$** (relative to $\omega$) is $\mathrm{vol}_\omega(K) := \int_K\omega$.

**Special case: $n = 0$.** A 0-form is a function $f : M \to \mathbb{R}$; a nowhere-vanishing 0-form is a nowhere-vanishing function; "volume form" on a 0-manifold is then just an assignment of nonzero numbers to each point.

---

# Categorical / Structural Definition

A volume form is a **nowhere-vanishing section of the line bundle $\Lambda^n(T^*M) \to M$**. This line bundle is the **orientation line bundle** (also called the **determinant bundle** of $T^*M$). $M$ is orientable iff this line bundle is trivial (admits a nowhere-vanishing global section), and the space of volume forms up to positive rescaling is in bijection with the set of orientations.

**The space of all volume forms (with no orientation chosen)** has the structure of a $C^\infty(M, \mathbb{R}^*)$-torsor — any two are related by a nowhere-vanishing scalar function. Restricting to *positively oriented* volume forms gives a $C^\infty(M, \mathbb{R}_{>0})$-torsor — the convex cone of positive volume forms.

In the language of **affine bundles** / **principal bundles**: choosing a volume form on an oriented manifold is a section of a principal $\mathbb{R}_{>0}$-bundle. Demanding the integral of the volume form to be 1 (when $M$ is compact) cuts this down to a single canonical representative — this is what produces the [[#Unlocked by This|Haar volume form]] on a compact Lie [[Def - Group|group]].

---

# Relate to Other Fields / Compression

A volume form is the natural pointwise "signed-volume measurer", and the *signed* nature is what distinguishes it from a [[Def - Density on a Manifold|density]] (which is unsigned, transforming by $|\det DF|$, and exists on any manifold, orientable or not). The compression achieved by volume forms is that a *single* signed object simultaneously encodes (a) the orientation of $M$ (its sign), and (b) the volume measure on $M$ (its absolute value). The density $|\omega|$ throws away (a) and keeps (b).

On a **Riemannian manifold**, the metric singles out a canonical equivalence class of volume forms — the class containing the Riemannian volume form $\omega_g = \sqrt{\det g_{ij}}\,dx^1\wedge\cdots\wedge dx^n$ (see [[Def - Riemannian Volume Form]] and [[Thm - Existence of the Riemannian Volume Form]]). This is the natural choice of representative within the orientation, and it is what makes "the volume of a region on a Riemannian manifold" a well-defined number (rather than just well-defined up to a positive function).

**True name:** A volume form is a smooth, nowhere-vanishing top-degree differential form — equivalently, a smooth trivialization of the orientation line bundle. This is the operational form: every concrete construction of a volume form (the area form on a sphere via outward normal, the Riemannian volume form $\sqrt{\det g}\,dx^1\wedge\cdots\wedge dx^n$, the wedge of a left-invariant coframe on a Lie group) is a recipe for producing such a trivialization.

---

# Examples / Corollaries

**Is an instance — $dx^1 \wedge \cdots \wedge dx^n$ on $\mathbb{R}^n$.** The standard volume form, never zero (its value on the standard basis is $1$). It induces the standard orientation. Integration of an $n$-form against this volume form is the ordinary multiple Riemann integral.

**Is an instance — the area form on $S^2$.** The 2-form $\omega = x\,dy\wedge dz + y\,dz\wedge dx + z\,dx\wedge dy$, restricted to the unit sphere $S^2 \subseteq \mathbb{R}^3$, is nowhere zero. Its value on a tangent basis at $p \in S^2$ equals the signed area of the parallelogram they span, measured in the outward-normal direction. Total area: $\int_{S^2}\omega = 4\pi$.

**Is an instance — the angular form $d\theta$ on $S^1$.** On the circle $S^1$, the 1-form $d\theta$ (locally well-defined, although $\theta$ itself is only defined modulo $2\pi$) is nowhere zero. It is the standard volume form / length form on $S^1$, with total integral $\int_{S^1}d\theta = 2\pi$.

**Is an instance — the wedge of a left-invariant coframe on a Lie [[Def - Group|group]].** If $G$ is a Lie group of [[Def - Dimension|dimension]] $n$ with basis of left-invariant 1-forms $\theta^1, \ldots, \theta^n$, then $\omega_{Haar} = \theta^1\wedge\cdots\wedge\theta^n$ is left-invariant, nowhere zero, hence a volume form. On compact $G$, normalizing $\int_G\omega_{Haar} = 1$ singles it out canonically — this is the **Haar volume form**.

**Is an instance — the symplectic top-power $\omega^n / n!$ on a symplectic manifold.** If $(M^{2n}, \omega)$ is a symplectic manifold (closed nondegenerate 2-form), then $\omega^n = \omega\wedge\cdots\wedge\omega$ ($n$ factors) is a volume form on $M^{2n}$ — the **symplectic volume form** or **Liouville volume**. Nondegeneracy of $\omega$ is exactly what guarantees $\omega^n$ is nowhere zero.

**Is NOT an instance — any top-form on the Möbius strip.** The Möbius strip admits no nowhere-vanishing 2-form, because of the orientation obstruction (any candidate, transported once around the core circle, returns with reversed sign and must vanish along the way). So the Möbius strip has *no* volume form; it has only a density.

**Is NOT an instance — any top-form on $\mathbb{RP}^2$.** Same obstruction as Möbius: $\mathbb{RP}^2$ is non-orientable, and the orientation line bundle is the canonical non-trivial line bundle.

**Is NOT an instance — $f\,dx^1\wedge\cdots\wedge dx^n$ on $\mathbb{R}^n$ for $f$ vanishing on a set.** If $f \in C^\infty(\mathbb{R}^n)$ vanishes at some point $p$, then $f\,dx^1\wedge\cdots\wedge dx^n$ vanishes at $p$ and is *not* a volume form (despite being a smooth $n$-form with the correct degree). To be a volume form one needs $f$ to be everywhere nonzero — and (if one wants $f$ positively oriented) everywhere positive.

**Corollary — volume forms on a connected manifold form two "rays".** Up to multiplication by an everywhere-positive function, an orientable connected manifold has exactly two equivalence classes of volume forms — corresponding to its two orientations. The set of all volume forms is therefore a disjoint union of two convex cones (positive and negative for the chosen orientation), each cone parametrized by $C^\infty(M, \mathbb{R}_{>0})$.

**Corollary — products of volume forms.** If $\omega_M$ is a volume form on $M$ and $\omega_N$ on $N$, then $\pi_M^*\omega_M \wedge \pi_N^*\omega_N$ is a volume form on $M \times N$ — the **product volume form**.

**Corollary — restriction to open subsets.** A volume form on $M$ restricts to a volume form on any open subset $U \subseteq M$. In particular, every open subset of $\mathbb{R}^n$, of a Lie group, or of any orientable manifold has a volume form inherited from the larger space.

**Calibration check.** Verify that $dx \wedge dy$ is a volume form on $\mathbb{R}^2$ but $x\,dx\wedge dy$ is not (it vanishes on the $y$-axis); that the area form $\omega = x\,dy\wedge dz + y\,dz\wedge dx + z\,dx\wedge dy$ on $S^2$ never vanishes (check at the north pole $(0, 0, 1)$); that any two volume forms on $\mathbb{R}^n$ inducing the same orientation differ by a positive function; and that the Möbius strip admits a *density* even though it admits no volume form. If you can also explain why on a symplectic manifold the volume form $\omega^n/n!$ is automatically closed (and hence not exact when $M$ is closed), you have understood the structural relationship between orientation, volume, and cohomology.

---

# Unlocked by This

> [!tip] Riemannian Volume Form *(continued in this topic)*
> On an oriented Riemannian manifold, the metric singles out a *canonical* volume form $\omega_g = \sqrt{\det g_{ij}}\,dx^1\wedge\cdots\wedge dx^n$ in oriented coordinates. See [[Def - Riemannian Volume Form]] and [[Thm - Existence of the Riemannian Volume Form]].

> [!tip] Integration of Functions on a Manifold *(continued in this topic)*
> A volume form $\omega$ allows one to integrate *functions* (not just top-forms): $\int_M f := \int_M f\omega$. The result depends on the choice of $\omega$ within its orientation class — change $\omega$ by a positive factor $h$ and the integral changes by integrating $fh$ instead. The canonical choice on a Riemannian manifold is $\omega_g$.

> [!tip] Haar Measure on a Lie Group *(from Lie Theory)*
> On a Lie group, the wedge of a left-invariant coframe is a left-invariant volume form, unique up to positive scaling. On a compact Lie group, normalization to total integral 1 picks out the **Haar volume form**; this is the unique left-invariant probability measure, the foundation of representation theory of compact groups (Peter–Weyl, character theory).

> [!tip] Symplectic Volume / Liouville Measure *(from Symplectic Geometry)*
> On a $2n$-dimensional symplectic manifold $(M, \omega)$, the form $\omega^n/n!$ is a volume form — the **Liouville volume**. Its preservation by Hamiltonian flows is **Liouville's theorem** in classical mechanics: phase-space volume is preserved.

> [!tip] Top Chern Class and the Volume Form on a Complex Manifold *(from Complex Geometry)*
> On a Kähler manifold $(M, \omega)$ — a complex manifold with a compatible closed Hermitian 2-form $\omega$ — the form $\omega^n/n!$ is a volume form, and its de Rham class is the top Chern class $c_n$ paired with the tangent bundle. The integral of this form over a closed Kähler manifold gives a topological invariant.
