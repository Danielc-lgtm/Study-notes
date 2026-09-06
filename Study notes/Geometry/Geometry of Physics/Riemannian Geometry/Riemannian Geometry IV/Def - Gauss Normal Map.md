---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Embedded Submanifold"
  - "Def - Orientation of a Smooth Manifold"
  - "Def - The Sphere as a Smooth Manifold via Stereographic Projection"
tags: [geometry, riemannian-geometry, surfaces, normal-map, gauss-bonnet]
---

# Notation

Let $M \subset \mathbb{R}^3$ be an oriented regular $2$-dimensional submanifold. A choice of **orientation** on $M$ is equivalent (in $\mathbb{R}^3$) to a continuous choice of unit normal field; we denote this field $\hat n$ or $N$. The unit sphere $S^2 = \{\mathbf{x} \in \mathbb{R}^3 : |\mathbf{x}| = 1\}$ carries its standard "outward normal" orientation. Full registry on [[Riemannian Geometry IV — Classical Geometry of Surfaces in R^3]].

---

# Axiom Motivation

The desideratum is to convert the **extrinsic embedding of $M$ in $\mathbb{R}^3$** into a smooth map between manifolds we can analyse with the full machinery of differential topology. Two key features need to be captured: how the surface curves in space (which direction is "normal"?), and how this normal direction varies from point to point. The cleanest way to package both at once is to view the unit normal as a function from $M$ to the set of possible unit vectors in $\mathbb{R}^3$ — which is the unit sphere $S^2$ — and to study the resulting map's differential and degree.

**Why a *unit* normal?** A general normal vector lives in $\mathbb{R}^3$ and has variable length; the length is unimportant for "where it points" and gets in the way of subsequent constructions. Normalising to unit length collapses all normal vectors at a point to a single direction, an element of $S^2$. Once normalised, $N(p) \in S^2$ becomes a *point* on the sphere, not just a vector, and the assignment $p \mapsto N(p)$ is a map between manifolds of the same dimension — exactly the setting in which Brouwer-degree theory operates.

**Why does the orientation matter?** Every $p \in M$ has *two* possible unit normals: $\pm N(p)$. Locally one can always choose one continuously; globally, this continuous choice is precisely an **orientation** of $M$. Non-orientable surfaces like the Möbius strip do not admit a continuous unit normal — walking along the central circle returns the normal to its negative — and so the Gauss normal map cannot be defined on them. The orientation of $M$ and the orientation of $S^2$ together determine whether $N$ is orientation-preserving or -reversing at each regular point, which feeds into the sign convention for the Brouwer degree.

**Why does identifying $T_{N(p)}S^2$ with $T_pM$ work?** Both are $2$-dimensional subspaces of $\mathbb{R}^3$. By construction, both are orthogonal complements of the same vector $N(p)$ — $T_pM$ because $N(p)$ is normal to $M$ at $p$, and $T_{N(p)}S^2$ because $N(p)$ is the position vector of a sphere point and hence outward-normal to $S^2$ there. So these two tangent planes are *parallel translates of each other* in $\mathbb{R}^3$. We identify them via parallel translation in $\mathbb{R}^3$, which lets the differential $dN_p$ be viewed as a linear map $T_pM \to T_pM$ — exactly the [[Def - Shape Operator (Weingarten Map)|shape operator]] $-dN$. Without this identification, $dN_p$ would land in a different vector space at each $p$ and would be much less tractable.

**The forced form of the definition.** Once one accepts that the relevant data is "which way is normal, smoothly as a function of $p$, on an oriented surface", the only natural construction is the map $p \mapsto N(p) \in S^2$. There is essentially no choice — except the choice of orientation, which is the choice of which of the two normals to use. The construction is so natural that it appears (with various names) all the way up to high-codimension submanifold theory: there one studies the **normal bundle** $\nu M \to M$, and the Gauss-type maps are sections of bundles of Grassmannians.

A forward reference for motivation: the [[Thm - The Gauss Normal Map has Degree Half the Euler Characteristic|degree of the Gauss map]] turns out to equal $\chi(M)/2 = 1 - g$ for a closed orientable surface of genus $g$ in $\mathbb{R}^3$ — an integer topological invariant. The Gauss-normal-map construction is what makes this theorem statable: without packaging "normal-direction-as-a-function-of-point" as a map between manifolds, there would be no Brouwer degree to compute, and no bridge from extrinsic curvature to topology. The definition is shaped to *make this theorem available*.

---

# The Definition

> **Definition (Gauss Normal Map).** Let $M \subset \mathbb{R}^3$ be an oriented regular surface with continuous (equivalently, smooth) unit normal field $\hat n : M \to \mathbb{R}^3$, $|\hat n(p)| = 1$ for every $p \in M$. The **Gauss normal map** is
> $$
> N : M \to S^2, \qquad N(p) := \hat n(p),
> $$
> where the right side is interpreted as a point on the unit sphere $S^2 \subset \mathbb{R}^3$.

The differential $dN_p : T_pM \to T_{N(p)}S^2$ is a linear map. Both $T_pM$ and $T_{N(p)}S^2$ are the orthogonal complement of $N(p)$ in $\mathbb{R}^3$, so we identify them via parallel translation. Under this identification, $-dN_p$ is the [[Def - Shape Operator (Weingarten Map)|shape operator]] $S_p : T_pM \to T_pM$, and the second fundamental form is recovered as $\mathrm{II}(X, Y) = -\langle dN(X), Y\rangle$.

In local coordinates $\mathbf{x}(u, v)$, the unit normal is
$$
N(u, v) = \frac{\mathbf{x}_u \times \mathbf{x}_v}{|\mathbf{x}_u \times \mathbf{x}_v|},
$$
and the Gauss map is given explicitly by this formula. The differential in coordinates is $\partial N/\partial u^\alpha$, which by Weingarten's equation $\partial N/\partial u^\alpha = -b^\beta_{\;\alpha}\mathbf{x}_\beta$ (the principal computational identity of the chapter) expresses the change in $N$ in terms of the shape operator's matrix components.

**Change-of-area formula.** If $\mathrm{vol}^2_M$ and $\mathrm{vol}^2_{S^2}$ are the area forms on $M$ and $S^2$, then
$$
N^* \mathrm{vol}^2_{S^2} = K\, \mathrm{vol}^2_M,
$$
where $K$ is the Gauss curvature. So the Jacobian determinant of $N$ at $p$ equals $K(p)$, and one can read $K(p) = \lim_{U \to p}(\text{signed area of }N(U))/\text{area of }U$ — Gauss's original definition.

---

# Categorical / Structural Definition

The Gauss normal map is, structurally, a **classifying map for the tangent bundle's $SO(2)$-reduction**. The unit-normal-field choice on $M \subset \mathbb{R}^3$ is equivalent to an orientation, and the tangent space $T_pM$ is determined by $N(p) \in S^2$ (it is the orthogonal complement). So $N : M \to S^2$ classifies the tangent bundle of $M$ as a sub-bundle of the trivial $\mathbb{R}^3$-bundle: the pullback of the tautological $2$-plane bundle over $S^2$ (whose fibre over $\hat n$ is $\hat n^\perp$) is exactly $TM$.

This is the surface-level case of the general construction: a Gauss map $M^k \to \mathrm{Gr}(k, n)$ for a submanifold $M^k \subset \mathbb{R}^n$ assigns to $p$ the tangent plane $T_pM$ viewed as a point of the Grassmannian $\mathrm{Gr}(k, n)$ of $k$-planes in $\mathbb{R}^n$. The case $k = n - 1$ specialises to a map into $\mathrm{Gr}(n-1, n) = \mathbb{RP}^{n-1}$, and orientability lifts this to $S^{n-1}$, recovering the unit-normal version. The pullback of the tautological $k$-plane bundle is always $TM$, so any characteristic class of $TM$ pulls back from the universal classes on $\mathrm{Gr}(k, n)$ — the source of the **Stiefel–Whitney**, **Chern**, and **Pontryagin** classes.

Functorially: an orientation-preserving smooth embedding $M \hookrightarrow \mathbb{R}^3$ produces a Gauss map $N$; reversing the orientation negates $N$. The mapping is contravariant in the embedding's chirality but covariant in homotopies of the embedding (when these preserve orientation), so the homotopy class of $N$, and hence $\deg(N)$, is an invariant of the *oriented* embedded surface.

---

# Relate to Other Fields / Compression

The Gauss normal map is the **simplest map between closed orientable surfaces** that arises naturally from geometry, and it is the prototypical example for **Brouwer degree theory** ([[Def - Brouwer Degree of a Map]]). Every introduction to degree theory uses the Gauss map of an embedded sphere or torus as the calibration example, because the degree is computable from the genus (it is $1 - g$) and verifiable from a single picture.

In **complex analysis**, the analogous construction is the **derivative-of-a-holomorphic-map** as a map $\mathbb{C} \to \mathbb{C}^*$ (or its compactification $\mathbb{CP}^1 \to \mathbb{CP}^1$). For a polynomial $P : \mathbb{CP}^1 \to \mathbb{CP}^1$ of degree $n$, the Brouwer degree of $P$ as a map of surfaces is exactly $n$, recovering the fundamental theorem of algebra via degree theory.

In **gauge theory**, the natural higher-dimensional analogue is the **classifying map** $M \to BG$ from a manifold to the classifying space of a Lie group $G$, which is the principal-bundle perspective on connections and characteristic classes; see [[Gauge Theory II — Principal Bundles, Representations, and Bundle Classification]].

**True name:** The Gauss normal map is *the parametrisation of $M$ by its normal direction*. The official "$p \mapsto \hat n(p)$" is the right definition, but the operational picture is "view $M$ from the outside and watch the normal direction rotate as you move on $M$" — the Brouwer degree of $N$ is exactly the integer count of how many times $N$ wraps $M$ around $S^2$. This rotational-wrap picture is what makes Gauss–Bonnet ($4\pi\deg(N) = 2\pi\chi(M)$) feel obvious in retrospect: a closed surface of genus $g$ has the normal "wrap" $1 - g$ times, with negative contributions from the saddle regions and positive from convex regions, and the sum is a topological count.

---

# Examples / Corollaries

**Is an instance — the round sphere.** For $S^2 \subset \mathbb{R}^3$ with outward normal, $N(p) = p/|p| = p$ (since $|p| = 1$ on the unit sphere). So $N = \mathrm{id}_{S^2}$, the identity map. Its differential is the identity, so $dN = \mathrm{id}$, $S = -dN = -\mathrm{id}$ as a map $T_pM \to T_pM$. **Wait** — with outward normal we expect the shape operator to give *positive* principal curvatures $\kappa_1 = \kappa_2 = 1$ for the unit sphere, but $S = -\mathrm{id}$ gives $-1$. The resolution is the sign convention: Frankel's $S = -dN$ together with outward normal gives $\kappa_i = -1$ on the *unit outward sphere*, and $K = (-1)(-1) = 1 > 0$. The do Carmo convention is $S = dN$ (so $\kappa_i = +1$ on the unit sphere); under either convention the Gauss curvature $K = \det S = +1/a^2$ on the sphere of radius $a$. [Note: the topic's convention is Frankel's $S = -dN$, which makes $K = \kappa_1\kappa_2$ positive on convex surfaces with outward normal.]

For the sphere of radius $a$ with outward normal, $N(p) = p/a$, so $N : aS^2 \to S^2$ is "shrink by factor $a$", with $\deg(N) = 1$. The Gauss–Bonnet integral is $\int_{aS^2} K\, dA = 4\pi\cdot 1 = 4\pi$, matching $2\pi\chi(S^2) = 4\pi$.

**Is an instance — the torus of revolution.** Take a torus $T^2 \subset \mathbb{R}^3$ with major radius $R$ and minor radius $r$. The outward normal rotates through every direction on $S^2$ as one traverses the torus, but at certain points it rotates "backwards" (the inner equator), giving a $-1$ contribution. The signed count is $\deg(N) = 0$, matching $\chi(T^2)/2 = 0$. Equivalently, $\int_{T^2} K\, dA = 0$ — the positive contributions from the outer half of the torus exactly cancel the negative contributions from the inner half.

**Is an instance — the genus-$g$ surface.** For an orientable closed surface of genus $g \geq 1$, $\deg(N) = 1 - g$, so $\int K\, dA = 4\pi(1 - g) = 2\pi\chi$. The surface of genus $2$ (a "double torus") has $\deg(N) = -1$ — meaning the Gauss map covers $S^2$ "minus one time" net — and the curvature integral is $-4\pi$, consistent with $\chi = -2$.

**Is NOT an instance — the Möbius strip.** A non-orientable surface does not admit a continuous unit normal field globally, so the Gauss normal map is not defined. One can attempt to define it locally — and the local formula $N = \mathbf{x}_u \times \mathbf{x}_v/|\cdot|$ still works on each chart — but the local definitions cannot be glued globally because walking the central circle returns the normal to its negative. The Möbius strip is the simplest non-orientable surface and the canonical example of why orientability is essential to the Gauss map construction.

**Is NOT an instance — a surface with self-intersection.** An immersed (rather than embedded) surface like the immersed Klein bottle in $\mathbb{R}^3$ has self-intersection, so at a self-intersection point there is no well-defined tangent plane (there are two tangent planes from the two sheets meeting there). The Gauss map then has a removable discontinuity at the self-intersection. This is why we typically restrict to *embedded* surfaces.

**Corollary — the differential of the Gauss map is the negative of the shape operator.** This is the link between the Gauss map (an extrinsic geometric object) and the shape operator (an algebraic invariant). Specifically, $-dN_p$ is self-adjoint with respect to the first fundamental form (by symmetry of $\mathrm{II}$), so its eigenvalues $\kappa_1, \kappa_2$ are real and its eigenvectors are orthogonal — the [[Def - Principal Curvatures and Directions|principal directions]].

**Corollary — Gauss's original definition of $K$.** From the change-of-area formula $N^*\mathrm{vol}^2_{S^2} = K\, \mathrm{vol}^2_M$, we have
$$
K(p) = \lim_{U \to p}\frac{\text{signed area of }N(U) \text{ on }S^2}{\text{area of }U \text{ on }M},
$$
i.e., $K(p)$ is the local area-magnification factor of the Gauss map. Where $N$ is locally orientation-preserving, $K > 0$; where orientation-reversing, $K < 0$. This is Gauss's 1827 definition — the modern algebraic $K = \kappa_1\kappa_2$ came later.

**Calibration check.** If you have understood the definition, you should be able to verify: (i) the Gauss map of a flat plane $\{z = 0\}$ is constant (a single point on $S^2$), so $\deg(N) = 0$ on any compact region of a plane — consistent with $K = 0$ on flat surfaces; (ii) the Gauss map of a cylinder of radius $a$ centred on the $z$-axis sends each circle of constant $z$ to a single point on $S^2$ (the unit normal rotates around the equator of $S^2$ as you go around the cylinder), so the image is the equator — a $1$-dimensional set in $S^2$, of $S^2$-area zero, consistent with $K = 0$ on the cylinder; (iii) the Gauss map of the standard torus has critical points (where $K = 0$) precisely at the top and bottom circles, where the normal direction is purely "up" or "down" in some sense.

---

# Unlocked by This

> [!tip] The Shape Operator and Second Fundamental Form *(from §4.1)*
> The differential $-dN : T_pM \to T_pM$ is the [[Def - Shape Operator (Weingarten Map)|shape operator]]. Its associated bilinear form $\mathrm{II}(X, Y) = \langle SX, Y\rangle = -\langle dN(X), Y\rangle$ is the [[Def - Second Fundamental Form|second fundamental form]]. Both objects extract from the Gauss map the linear-algebraic structure needed to compute curvature.

> [!tip] The Gauss–Bonnet Theorem via Degree Theory *(from §4.3)*
> Because the Gauss map is between closed oriented surfaces of the same dimension, it has a Brouwer degree $\deg(N) \in \mathbb{Z}$ which is a homotopy invariant. The fact that $\deg(N) = 1 - g$ (see [[Thm - The Gauss Normal Map has Degree Half the Euler Characteristic]]) and the change-of-area formula $\int_M K\, dA = 4\pi\deg(N)$ combine to give the [[Thm - Gauss-Bonnet Theorem for Surfaces|Gauss–Bonnet theorem]]: $\int_M K\, dA = 2\pi\chi(M)$. This is the cleanest derivation of the theorem from a single conceptual fact (degree-of-Gauss-map = $\chi/2$).

> [!tip] Generalised Gauss Maps and Characteristic Classes *(from Algebraic Topology III)*
> For a submanifold $M^k \subset \mathbb{R}^n$, the generalised Gauss map $\gamma : M \to \mathrm{Gr}(k, n)$ sends $p$ to its tangent plane $T_pM$. This is the universal construction: every characteristic class of $TM$ pulls back from a universal class on the Grassmannian. The Stiefel–Whitney classes, Pontryagin classes, and (for oriented even-dimensional submanifolds) the Euler class all arise this way. See [[Algebraic Topology III — Higher Homotopy and Chern Forms]] for the gauge-theoretic perspective.
