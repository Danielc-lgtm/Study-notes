---
type: definition
subject: special-relativity
prereqs:
  - "Def - Classification of Restricted Lorentz Transformations"
  - "Def - Boosts as Hyperbolic Rotations"
  - "Def - Classification of Four-Vectors"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. A **null plane** is a two-dimensional subspace $\Pi$ on which the induced metric is degenerate. We use a null pair $\ell, k$ ($\ell\cdot\ell = k\cdot k = 0$, $\ell\cdot k = 2$) and the orthonormal frame $(e_0, e_1, e_2, e_3)$ with $e_0 = \tfrac12(\ell+k)$, $e_1 = \tfrac12(\ell-k)$; $\Pi_0 = \mathrm{Span}(e_0,e_1) = \mathrm{Span}(\ell,k)$ is timelike, $\Pi_1 = \mathrm{Span}(e_2,e_3)$ spacelike, $\Pi_3 = \mathrm{Span}(\ell,e_3)$ null. Parameters $\psi$ (rapidity), $\theta$ (rotation angle), $\alpha \in \mathbb{R}^+$ (null-rotation parameter). Full registry on [[Special Relativity IX — The Lorentz Group, Structure and Classification]].

This is a compound page: it defines two interlocking notions — the **null rotation** and the **four-screw** — because they are the two irreducible types into which [[Def - Classification of Restricted Lorentz Transformations|the classification]] resolves every restricted Lorentz transformation, and the boundary between them (one invariant null direction versus two) is best understood by contrast.

---

# Axiom Motivation

The [[Def - Classification of Restricted Lorentz Transformations|three-parameter normal form]] shows that a restricted Lorentz transformation is governed by a rapidity $\psi$, a rotation angle $\theta$, and a shear parameter $\alpha$, and that the four named types arise by switching parameters off. Two of these types — the boost and the spatial rotation — are familiar from [[Special Relativity IV — The Invariant Interval, Rapidity and the Lorentz Group|Special Relativity IV]]. This page motivates and defines the two *structural* types that organise the whole classification: the four-screw, which contains boosts and rotations as special cases, and the null rotation, the one genuinely unfamiliar element.

The motivation for the **four-screw** is the realisation that a boost and a rotation can act *simultaneously* in orthogonal planes without interfering. A boost lives in a timelike plane $\Pi_0$; a rotation lives in a spacelike plane. If the rotation's plane is exactly $\Pi_0^\perp$, the two commute — their matrices are block-diagonal in complementary blocks — and the composite is a single restricted transformation parametrised by $(\psi, \theta)$. This is the general four-screw, and the reason boosts ($\theta = 0$) and rotations ($\psi = 0$) are its special cases is that they are the four-screws with one block trivial. The name "screw" is borrowed from rigid-body kinematics, where a screw motion is a rotation about an axis combined with a translation along it; here the "translation" along the boost axis is replaced by a hyperbolic boost in the timelike plane. The design decision is to require the two planes to be *orthogonal complements* — if they were not, the composition would generally be a four-screw of some third plane, or a null rotation, and the clean commuting structure would be lost.

The motivation for the **null rotation** is subtler, and it is where the Lorentzian story departs entirely from the Euclidean one. The summary of the classification says a transformation has a *unique* invariant null direction precisely when $\psi = \theta = 0$ with $\alpha \ne 0$. What kind of transformation fixes exactly one light ray and nothing timelike or spacelike of interest? The answer is a transformation that leaves invariant a *null plane* — a two-plane $\Pi_3 = \mathrm{Span}(\ell, e_3)$ whose induced metric is *degenerate*. This is the crucial new object. A timelike plane has induced signature $(+,-)$ and a spacelike plane $(-,-)$; both are non-degenerate, and a transformation strictly invariant on such a plane is a boost or a rotation. But a null plane has signature $(0,-)$: the null vector $\ell$ lies in it and is orthogonal to everything in it, including itself. A transformation fixing such a degenerate plane cannot be a rotation or a boost — those preserve non-degenerate planes — so it is a new type. The null rotation is the transformation that *shears* along the light cone, sliding the null plane along itself while fixing the single null line $\mathrm{Span}(\ell)$.

Why must this type exist at all? Because the parameter $\alpha$ in the normal form has nowhere else to go. If $\psi$ or $\theta$ is nonzero, a second invariant null direction appears and forces $\alpha = 0$; the only way to keep $\alpha$ alive is to set $\psi = \theta = 0$, and then the transformation is a pure null rotation. The existence of the null plane — a feature unique to indefinite signature, since a positive-definite metric has no degenerate subspaces — is what makes room for this third structural possibility. In Euclidean geometry there is no null plane, hence no null rotation, hence the isometry classification has only the rotation-type (elliptic) and translation-type elements. The minus signs of the metric create the null plane, and the null plane creates the null rotation.

The defining property "leaves a null plane strictly invariant" must be stated carefully. *Strictly* invariant means $\Lambda$ restricted to the plane is the identity? No — for a null rotation $\Lambda$ does *not* fix the null plane pointwise; rather it maps the null plane to itself (stably invariant), and within it fixes only the line $\mathrm{Span}(\ell)$. The contrast with boosts and rotations, whose invariant planes are non-degenerate and where the orthogonal complement is also invariant, is sharpened by a structural fact: for a null plane $\Pi_3$, one *cannot* decompose $E = \Pi_3 \oplus \Pi_3^\perp$, because $\Pi_3 \cap \Pi_3^\perp = \mathrm{Span}(\ell) \ne \{0\}$. The null vector is orthogonal to its own plane. This failure of orthogonal decomposition is the algebraic signature of degeneracy and the reason the null rotation behaves like nothing else.

---

# The Definition

**Four-screw.** Given a timelike plane $\Pi \subset E$, a **four-screw** (or **4-screw**) of plane $\Pi$ is a restricted Lorentz transformation that is the composition
$$
\Lambda = S \circ R = R \circ S
$$
of a [[Def - Boosts as Hyperbolic Rotations|Lorentz boost]] $S$ of plane $\Pi$ (rapidity $\psi$) and a spatial rotation $R$ of the orthogonal plane $\Pi^\perp$ (angle $\theta$). The two factors commute because their matrices are block-diagonal in the complementary planes $\Pi$ and $\Pi^\perp$. In an adapted orthonormal basis with $\Pi = \mathrm{Span}(e_0, e_1)$, $\Pi^\perp = \mathrm{Span}(e_2,e_3)$,
$$
\Lambda^\alpha{}_\beta =
\begin{pmatrix}
\cosh\psi & \sinh\psi & 0 & 0 \\
\sinh\psi & \cosh\psi & 0 & 0 \\
0 & 0 & \cos\theta & -\sin\theta \\
0 & 0 & \sin\theta & \cos\theta
\end{pmatrix}.
$$
A four-screw has exactly **two** invariant null directions, the two null lines $\mathrm{Span}(e_0\pm e_1)$ of its plane $\Pi$. Boosts ($\theta = 0$) and spatial rotations ($\psi = 0$) are the degenerate four-screws.

**Characterisation.** A restricted Lorentz transformation is a four-screw if and only if it leaves invariant **two distinct null directions**.

**Null rotation.** A **null rotation** is a restricted Lorentz transformation that leaves invariant a **null plane** — a two-plane $\Pi_3$ on which the induced metric is degenerate (signature $(0,-)$). Equivalently, it has parameters $\psi = \theta = 0$, $\alpha \in \mathbb{R}^+$, with matrix, in the non-orthonormal basis $(\ell, k, e_2, e_3)$,
$$
(\Lambda^*)^\alpha{}_\beta =
\begin{pmatrix}
1 & 4\alpha^2 & 2\alpha & 0 \\
0 & 1 & 0 & 0 \\
0 & 4\alpha & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix},
\qquad
\Lambda^\alpha{}_\beta =
\begin{pmatrix}
1 + 2\alpha^2 & -2\alpha^2 & 2\alpha & 0 \\
2\alpha^2 & 1 - 2\alpha^2 & 2\alpha & 0 \\
2\alpha & -2\alpha & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
$$
in the orthonormal basis. It leaves $\ell = e^*_0$ and $e_3 = e^*_3$ invariant, hence fixes the null plane $\Pi_3 = \mathrm{Span}(\ell, e_3)$, and has exactly **one** invariant null direction, $\mathrm{Span}(\ell)$. The matrix $N = \Lambda - \mathrm{Id}$ is nilpotent: $N^3 = 0$ but $N^2 \ne 0$ (a single Jordan block of size three on $\mathrm{Span}(\ell, k, e_2)$, plus a trivial block on $e_3$).

**Null plane.** A two-plane $\Pi_3$ is a null plane iff it contains exactly one null direction $\mathrm{Span}(\ell)$, with every other nonzero vector spacelike, and $\ell$ is orthogonal to all of $\Pi_3$. It is tangent to the light cone (meeting it only along $\mathrm{Span}(\ell)$), and one cannot write $E = \Pi_3 \oplus \Pi_3^\perp$, since $\Pi_3 \cap \Pi_3^\perp = \mathrm{Span}(\ell)$.

---

# Categorical / Structural Definition

In terms of Jordan structure over $\mathbb{C}$, the two types are the two possibilities for an element of $SO^+(1,3)$:
- a **four-screw** is *semisimple* (diagonalisable over $\mathbb{C}$): eigenvalues $e^{\psi}, e^{-\psi}, e^{i\theta}, e^{-i\theta}$, with eigenvectors the two null directions $e_0\pm e_1$ (real eigenvalues) and two complex combinations of $e_2, e_3$ (complex eigenvalues);
- a **null rotation** is *unipotent* with a nontrivial nilpotent part: its only eigenvalue is $1$, with one Jordan block of size three (on $\mathrm{Span}(\ell, k, e_2)$) and one of size one (on $e_3$).

Every element of $SO^+(1,3)$ has a unique **multiplicative Jordan decomposition** $\Lambda = \Lambda_s\Lambda_u$ into a commuting semisimple part $\Lambda_s$ and unipotent part $\Lambda_u$, both in $SO^+(1,3)$. For a four-screw $\Lambda_u = \mathrm{Id}$ (it is already semisimple); for a null rotation $\Lambda_s = \mathrm{Id}$ (it is already unipotent). The general restricted transformation is a commuting product of the two — a four-screw times a null rotation in compatible planes — which is the abstract reason the three-parameter form is exhaustive: $\psi, \theta$ parametrise the semisimple part, $\alpha$ the unipotent part, and they commute. Through the [[Thm - SL(2,C) is the Double Cover of the Restricted Lorentz Group|spinor map]] this is the Jordan decomposition in $SL(2,\mathbb{C})$: a loxodromic element is semisimple ($2\times 2$ diagonalisable), a parabolic element is unipotent (a single $2\times 2$ Jordan block, trace $\pm 2$).

---

# Relate to Other Fields / Compression

The four-screw/null-rotation dichotomy is the Lorentzian incarnation of the elliptic-hyperbolic-parabolic trichotomy that pervades mathematics. On the Riemann sphere, Möbius transformations split into elliptic (rotation-like, two fixed points, $|\mathrm{tr}| < 2$), hyperbolic/loxodromic (scaling-like, two fixed points, $|\mathrm{tr}| > 2$), and parabolic (shear-like, one fixed point, $|\mathrm{tr}| = 2$). The four-screw is the loxodromic case (a complex eigenvalue ratio combining scaling and rotation), and the **null rotation is the parabolic case** — the shear with a single fixed point on the sphere. The same trichotomy appears in the classification of conics (ellipse/hyperbola/parabola, the parabola being the degenerate boundary), in second-order linear PDEs (elliptic/hyperbolic/parabolic, the heat equation being parabolic), and in the dynamics of one-parameter subgroups. The null rotation is always the parabolic, boundary, shear-type member.

**True name:** a four-screw is "a semisimple (diagonalisable) restricted Lorentz transformation," and a null rotation is "a unipotent one with a size-three Jordan block." The geometric definitions (which plane is invariant) are official, but the operational test is the Jordan structure: diagonalisable means four-screw, a nontrivial nilpotent part means null rotation. The fastest computation is the trace of the $SL(2,\mathbb{C})$ lift — $\pm 2$ signals parabolic (null rotation), anything else signals loxodromic (four-screw).

---

# Examples / Corollaries

**Is an instance (four-screw) — boost-plus-rotation.** Compose a boost along $x$ of rapidity $\psi$ with a rotation in the $(y,z)$-plane of angle $\theta$. Since $\mathrm{Span}(e_0,e_1) \perp \mathrm{Span}(e_2,e_3)$, the two commute and the composite is a four-screw with the displayed block-diagonal matrix. Its two invariant null directions are $\mathrm{Span}(e_0\pm e_1)$.

**Is an instance (null rotation) — the explicit shear.** With $\alpha = 1$, the matrix $\begin{pmatrix} 3 & -2 & 2 & 0 \\ 2 & -1 & 2 & 0 \\ 2 & -2 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$ in the orthonormal basis fixes the null direction $\mathrm{Span}(e_0+e_1)$ and the null plane $\mathrm{Span}(e_0+e_1, e_3)$. One checks $(\Lambda - \mathrm{Id})^2 \ne 0$ but $(\Lambda - \mathrm{Id})^3 = 0$.

**Is NOT an instance (four-screw) — boost and rotation in non-orthogonal planes.** A boost along $x$ composed with a rotation in the $(x,y)$-plane (which is *not* orthogonal to the boost plane $\mathrm{Span}(e_0,e_1)$) is generally not a four-screw of either plane — it must be re-classified, and is typically a four-screw of a tilted plane or, in degenerate cases, a null rotation. The four-screw definition strictly requires orthogonal complementary planes.

**Is NOT an instance (null plane) — a timelike or spacelike plane.** The plane $\mathrm{Span}(e_0, e_1)$ (timelike, signature $(+,-)$) and the plane $\mathrm{Span}(e_2,e_3)$ (spacelike, signature $(-,-)$) are both non-degenerate, so neither is a null plane and a transformation strictly invariant on them is a boost or a rotation, not a null rotation. A null plane must contain a null vector orthogonal to the whole plane.

**Corollary — the null rotation has no inverse-square-root within its type that is a boost or rotation.** Because $\Lambda - \mathrm{Id}$ is nilpotent, $\log\Lambda = N - \tfrac12 N^2 + \cdots = N - \tfrac12 N^2$ (the series terminates), and the generator $\log\Lambda$ is a nilpotent element of the Lie algebra — neither a boost generator nor a rotation generator, but the specific combination $K_x + J_y$ (in suitable axes). This is the algebraic fingerprint of the null rotation: its Lie-algebra generator is nilpotent.

**Calibration check.** The reader who has understood these definitions should be able to: (i) verify that the displayed null-rotation matrix fixes $\ell = e_0 + e_1$ and $e_3$ but moves $k = e_0 - e_1$; (ii) confirm that $\mathrm{Span}(\ell, e_3)$ is a null plane by checking $\ell\cdot\ell = 0$, $\ell\cdot e_3 = 0$, $e_3\cdot e_3 = -1$ (signature $(0,-)$); (iii) explain why a four-screw is diagonalisable but a null rotation is not, in terms of the number of invariant null directions.

---

# Unlocked by This

> [!tip] The Massless Little Group ISO(2) and Helicity *(from Special Relativity XII)*
> The null rotations, together with the rotations about a null direction, form the **little group** of a null vector — the subgroup of $SO^+(1,3)$ fixing a chosen light-ray direction — and this group is isomorphic to $ISO(2)$, the Euclidean group of the plane (two "translations" that are the null rotations, plus one rotation). Wigner's classification identifies the unitary representations of this little group with the states of a *massless* particle: the rotation gives the **helicity**, and the null rotations act trivially on physical states (the "continuous spin" representations, where they act nontrivially, do not occur in nature). The null rotation, the odd element of this chapter's classification, is thus the precise group-theoretic object behind the masslessness of the photon and the graviton. See [[Special Relativity XII — Inertial Observers and the Poincaré Group]] and [[Def - Casimir Invariants of the Poincaré Group]].

> [!tip] Parabolic Elements and the Cusps of Hyperbolic Geometry *(from the geometry of SL(2,ℝ) and number theory)*
> The null rotation, as a parabolic element of $SL(2,\mathbb{C})$, is the same type of transformation that produces the **cusps** of hyperbolic surfaces and modular curves. In the theory of the modular group $SL(2,\mathbb{Z})$, parabolic elements (like $z \mapsto z+1$) fix a single point on the boundary at infinity and generate the cusp stabilisers; the quotient hyperbolic surface has a funnel-shaped cusp at each such point. The null rotation fixing a single null direction is the relativistic analogue: it slides along the boundary of the light cone the way a parabolic Möbius map slides along the boundary circle, and the connection is exact through the identification of the celestial sphere with the boundary of hyperbolic three-space.
