---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Lie Group"
  - "Def - Smooth Action of a Lie Group"
  - "Def - Lie Subgroup"
  - "Def - Smooth Manifold"
tags: [geometry, differential-geometry, lie-groups]
---

# Notation

$G$ is a Lie group; $M$ is a smooth manifold equipped with a transitive smooth left action of $G$. For $p \in M$, the stabilizer is $H = G_p$, a closed Lie subgroup of $G$. The quotient $G/H$ is the set of left cosets $\{gH : g \in G\}$ with the smooth manifold structure from [[Thm - Homogeneous Space is a Smooth Manifold]]. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]] for the full notation registry.

---

# Axiom Motivation

A homogeneous space is a manifold $M$ with a transitive smooth Lie group action: every point looks like every other, with the symmetry transporting one to the other. The motivating examples are abundant — spheres, projective spaces, Grassmannians, flag manifolds, hyperbolic spaces, Minkowski space, the moduli spaces of various structures — and they all share the feature that a single Lie group acts transitively, making the manifold "homogeneous" in the literal sense: no point is geometrically distinguished from any other.

Why **transitivity** and not just "smooth action"? Because transitivity is what makes the manifold "homogeneous". A non-transitive action has multiple orbits, and the orbits are then the natural "homogeneous pieces" of $M$, each itself a homogeneous space for $G$ via the restricted action. Transitivity is the condition that there is exactly one orbit; equivalently, every point can be moved to every other point by some group element. This is what we mean by "$G$ acts homogeneously on $M$".

Once $G$ acts transitively and smoothly on $M$, the structure is completely determined by the stabilizer at any point. Pick $p \in M$; the stabilizer $H = G_p = \{g \in G : g \cdot p = p\}$ is a closed Lie subgroup (closed by continuity, Lie subgroup by the closed subgroup theorem). The orbit map $\theta^{(p)} : G \to M$, $g \mapsto g \cdot p$, is $G$-equivariant (for left translation on $G$) with image $M$ (by transitivity) and stabilizer $H$ — so it descends to a $G$-equivariant bijection $G/H \to M$. This is the **orbit-stabilizer correspondence at the smooth level**, and it identifies every homogeneous space $M$ with a coset space $G/H$.

Why **closed** $H$? Because of the closed subgroup theorem, any stabilizer is closed — automatic, not a choice. But closedness is essential: it is what ensures that $G/H$ is Hausdorff (without closedness of $H$, the quotient topology on $G/H$ is not Hausdorff), and hence that $G/H$ has any chance of being a smooth manifold.

**The two-sided picture.**

- A **manifold with a transitive $G$-action** is a homogeneous space.
- **Quotient $G/H$ for a closed subgroup $H$** is a homogeneous space.

These two descriptions are equivalent — Lee Thm 21.17 says that for any closed subgroup $H \leq G$, the quotient $G/H$ inherits a unique smooth manifold structure of dimension $\dim G - \dim H$ such that $\pi : G \to G/H$ is a smooth submersion, and conversely every smooth transitive action $G \times M \to M$ produces $M \cong G/G_p$ via the orbit map. So homogeneous spaces are in bijection with closed [[Def - Subgroup|subgroups]] of Lie [[Def - Group|groups]], up to choice of basepoint and conjugation of $H$.

**Why does the quotient $G/H$ inherit smooth structure?** Because $H$ is closed (hence embedded by the closed subgroup theorem), and the projection $\pi : G \to G/H$ is built from the orbit structure of $H$ acting on $G$ by right translation — a free, smooth, proper action when $H$ is closed. The quotient manifold theorem (Lee Thm 21.10) provides smooth manifold structure for any free proper smooth action; applying it to right $H$-action on $G$ gives $G/H$ as a manifold.

**What goes wrong without closedness?** If $H$ is a non-closed Lie subgroup of $G$ — say the irrational winding $\mathbb{R} \hookrightarrow T^2$ — then $G/H$ as a topological space is non-Hausdorff (because $H$ is dense in some larger subgroup), and there is no compatible smooth manifold structure. The closed subgroup theorem and its homogeneous-space corollary are exactly the rigidity statements that close this gap when $H$ is required closed.

**Why care about homogeneous spaces specifically?** Because they form the simplest class of manifolds on which Lie-group methods are maximally effective. On a homogeneous space, every geometric object that is "$G$-invariant" — Riemannian metrics, connections, volume forms, differential operators — is determined by its value at a single point and the $H$-action on the tangent space there. This converts global geometry into linear algebra (representation theory of $H$ on $T_p M \cong \mathfrak{g}/\mathfrak{h}$), and is the foundation of the geometric analysis of symmetric spaces, the Borel–Weil construction in representation theory, and the calculus of orbits in Lie theory.

---

# The Definition

A **homogeneous space** of a Lie group $G$ is a smooth manifold $M$ equipped with a transitive smooth left action of $G$.

For any choice of basepoint $p \in M$, the **stabilizer** $H = G_p = \{g \in G : g \cdot p = p\}$ is a closed Lie subgroup of $G$ (closed by continuity of the action, hence an embedded Lie subgroup by [[Thm - The Closed Subgroup Theorem|the closed subgroup theorem]]).

The **orbit map** $\theta^{(p)} : G \to M$, $g \mapsto g \cdot p$, factors through the quotient $\pi : G \to G/H$ to give a $G$-equivariant [[Def - Diffeomorphism|diffeomorphism]]

$$\bar\theta^{(p)} : G/H \xrightarrow{\;\sim\;} M.$$

So every homogeneous space is canonically a coset space (with the choice of $p$ corresponding to choice of $H$ up to conjugation), with the smooth manifold structure on $G/H$ provided by [[Thm - Homogeneous Space is a Smooth Manifold]].

Conversely, for any closed Lie subgroup $H \leq G$, the coset space $G/H$ carries a unique smooth manifold structure of dimension $\dim G - \dim H$ such that $\pi : G \to G/H$ is a smooth submersion, and the natural left $G$-action $g \cdot (g'H) = (gg')H$ is smooth and transitive.

The dimension of a homogeneous space is

$$\dim M = \dim G - \dim H,$$

the smooth analogue of $|G \cdot p| = |G|/|G_p|$ in [[Thm - Orbit-Stabiliser Theorem|finite group theory]].

---

# Relate to Other Fields / Compression

A homogeneous space is **a manifold whose symmetry is large enough to move any point to any other** — a manifold on which "all points are equivalent" under a Lie group action. It is the smooth-manifold version of a transitive [[Def - Group Action|group action]] in abstract group theory, with all the additional structure (smoothness, manifold quotient, dimension equation) that the smooth setting provides.

From the [[Def - Smooth Action of a Lie Group|smooth-action side]], a homogeneous space is exactly a smooth $G$-manifold with one orbit. From the quotient side, it is $G/H$ for a closed subgroup $H$.

**True name:** A homogeneous space is **a manifold whose geometric structure is determined at a single point and propagated by a transitive group of symmetries**. Operationally, this means: all $G$-invariant geometric objects on $M$ (Riemannian metrics, connections, differential operators) are in bijection with $H$-invariant linear-algebraic objects on $T_p M \cong \mathfrak{g}/\mathfrak{h}$ — the tangent space at the basepoint, viewed as the quotient of Lie algebras. The geometry of $M$ reduces to representation theory of $H$ on $\mathfrak{g}/\mathfrak{h}$.

---

# Examples / Corollaries

**Is an instance: $S^n = \mathrm{SO}(n+1)/\mathrm{SO}(n)$.** The unit $n$-sphere with the natural action of $\mathrm{SO}(n+1)$ by rotations. Transitive (any unit vector can be rotated to any other), stabilizer of the north pole $e_{n+1}$ is the block-diagonal copy of $\mathrm{SO}(n)$. [[Def - Dimension|Dimension]]: $\dim \mathrm{SO}(n+1) - \dim \mathrm{SO}(n) = \binom{n+1}{2} - \binom{n}{2} = n$, correct. See [[Ex - S^2 as a Homogeneous Space of SO(3)]].

**Is an instance: $\mathbb{RP}^n = \mathrm{SO}(n+1)/(\mathrm{O}(n) \cap \mathrm{SO}(n+1))$.** Real projective space as a homogeneous space of $\mathrm{SO}(n+1)$. Note that the stabilizer of a line through the origin (rather than a point on $S^n$) is larger than the sphere's stabilizer — it includes the $\pm 1$ ambiguity in the line direction.

**Is an instance: $\mathrm{Gr}_k(\mathbb{R}^n) = \mathrm{O}(n)/(\mathrm{O}(k) \times \mathrm{O}(n - k))$.** The Grassmannian of $k$-planes in $\mathbb{R}^n$, as a homogeneous space of $\mathrm{O}(n)$. Transitive because any two $k$-planes can be rotated to each other; stabilizer of a fixed $k$-plane $V \subseteq \mathbb{R}^n$ is the subgroup preserving $V$, which is $\mathrm{O}(V) \times \mathrm{O}(V^\perp) = \mathrm{O}(k) \times \mathrm{O}(n - k)$. Dimension: $\binom{n}{2} - \binom{k}{2} - \binom{n - k}{2} = k(n - k)$.

**Is an instance: hyperbolic space $H^n = \mathrm{SO}^+(n, 1)/\mathrm{SO}(n)$.** The unit hyperboloid of timelike vectors in Minkowski space, with the proper-orthochronous Lorentz group acting transitively. The stabilizer of a fixed timelike vector is the rotation group $\mathrm{SO}(n)$ preserving its time-axis. This is a noncompact homogeneous space, the Riemannian model of hyperbolic geometry.

**Is an instance: $T^n = \mathbb{R}^n/\mathbb{Z}^n$.** The torus as a homogeneous space of $\mathbb{R}^n$ acting on itself by translation, modulo the discrete subgroup $\mathbb{Z}^n$. Dimension: $n - 0 = n$.

**Is an instance: a single point.** $\{*\}$ is the trivial homogeneous space, equal to $G/G$ — the full group acting transitively on itself modulo itself.

**Is NOT an instance: a manifold with a non-transitive group action.** $\mathbb{R}^n$ under the action of $\mathrm{SO}(n)$: the orbits are concentric spheres (and the origin), and $\mathbb{R}^n$ is *not* a homogeneous $\mathrm{SO}(n)$-space because the action is not transitive. However, each individual sphere (and the origin) is a homogeneous space for $\mathrm{SO}(n)$.

**Is NOT an instance: $G/H$ for non-closed $H$.** For the irrational winding $\mathbb{R} \hookrightarrow T^2$, the "quotient" $T^2/\mathbb{R}$ is a topological space but not a smooth manifold — it is non-Hausdorff with trivial topology. So $T^2/\mathbb{R}$ does not qualify as a homogeneous space in the smooth sense. The closedness condition on $H$ is essential.

**Corollary (dimension equation).** $\dim M = \dim G - \dim H$ for $M = G/H$. This is the smooth orbit-stabilizer dimension formula.

**Corollary (every closed subgroup gives a homogeneous space).** For any closed Lie subgroup $H \leq G$, $G/H$ is a smooth manifold of dimension $\dim G - \dim H$ on which $G$ acts smoothly and transitively. See [[Thm - Homogeneous Space is a Smooth Manifold]].

**Corollary (invariant structures).** A $G$-invariant Riemannian metric on $M = G/H$ is in bijection with an $H$-invariant inner product on $T_p M \cong \mathfrak{g}/\mathfrak{h}$, where $H$ acts on $\mathfrak{g}/\mathfrak{h}$ via the adjoint representation. Existence reduces to a representation-theoretic question: does $H$ admit an invariant inner product on $\mathfrak{g}/\mathfrak{h}$? For $H$ compact, yes (average over $H$); for general $H$, may fail.

**Corollary (homogeneous spaces are Lie groups iff $H \trianglelefteq G$).** $G/H$ is itself a Lie group (rather than just a homogeneous $G$-space) iff $H$ is a normal Lie subgroup of $G$ (so that left and right [[Def - Coset|cosets]] coincide). The quotient is then the quotient Lie group.

**Calibration check.** If you can (i) verify $S^n \cong \mathrm{SO}(n+1)/\mathrm{SO}(n)$ as a homogeneous space; (ii) compute $\dim \mathrm{Gr}_k(\mathbb{R}^n) = k(n-k)$ from the orbit-stabilizer dimension equation; and (iii) explain why $H$ must be closed for $G/H$ to be a smooth manifold — you have understood the definition correctly.

---

# Unlocked by This

> [!tip] Symmetric Spaces *(from Riemannian Geometry, Advanced)*
> A **symmetric space** is a homogeneous space $G/H$ where $H$ is the fixed-point set of an involution $\sigma : G \to G$ — a Lie group involution. Symmetric spaces carry canonical Riemannian metrics that are bi-invariant with respect to the symmetry, and they include spheres, hyperbolic spaces, projective spaces, Grassmannians, and the bounded symmetric domains of complex analysis. The classification (Cartan, 1926) is parallel to the classification of semisimple Lie algebras.

> [!tip] Principal Bundles *(from Gauge Theory)*
> A **principal $H$-bundle** is a smooth map $P \to B$ that locally looks like $H \times B \to B$, with $H$ acting freely on the fibres. The simplest example is $G \to G/H$ for a closed subgroup $H \leq G$: the projection is a principal $H$-bundle. Principal bundles are the geometric objects encoding gauge symmetries in physics.

> [!tip] Borel–Weil Theorem *(from Representation Theory)*
> For a compact connected Lie group $G$ with maximal torus $T$, the **homogeneous space** $G/T$ is a complex projective manifold (a flag manifold), and the **Borel–Weil theorem** identifies the irreducible representations of $G$ with spaces of holomorphic sections of equivariant line bundles on $G/T$. This is the geometric construction of all irreducible representations of a compact Lie group.

> [!tip] Klein Geometry *(from Differential Geometry, Historical)*
> **Klein's Erlangen program** (1872) characterizes a geometry as the study of a homogeneous space $G/H$ together with the invariants of the $G$-action. Euclidean geometry is $\mathrm{Isom}(\mathbb{R}^n)/\mathrm{O}(n)$, spherical geometry is $\mathrm{O}(n+1)/\mathrm{O}(n)$, hyperbolic geometry is $\mathrm{SO}^+(n, 1)/\mathrm{O}(n)$, projective geometry is $\mathrm{PGL}(n+1)/(\text{a parabolic subgroup})$. This unifies the classical geometries and is the philosophical foundation of modern geometric structures.
