---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Lorentzian Manifold"
  - "Def - Semi-Riemannian Metric and Signature"
  - "Def - Minkowski Space and the Metric"
  - "Def - The Lorentz Group"
  - "Def - Isometry of Riemannian Manifolds"
tags: [geometry, differential-geometry, lorentzian-geometry, special-relativity]
---

# Problem Statement

Verify that the pair $(\mathbb{R}^4, \eta)$ — the smooth manifold $\mathbb{R}^4$ equipped with the constant tensor field
$$
\eta \;=\; dt^2 - dx^2 - dy^2 - dz^2 \;=\; \eta_{\mu\nu}\, dx^\mu \otimes dx^\nu, \qquad \eta_{\mu\nu} = \mathrm{diag}(1, -1, -1, -1)
$$
(using Lee's "mostly minus" convention, with coordinates $x^\mu = (t, x, y, z)$ for $\mu = 0, 1, 2, 3$) — is a [[Def - Lorentzian Manifold|Lorentzian manifold]] in the sense of [[Def - Semi-Riemannian Metric and Signature|signature]] $(1, 3)$, and identify its [[Def - Isometry of Riemannian Manifolds|isometry group]] as the **Poincaré [[Def - Group|group]]** $O(1, 3) \ltimes \mathbb{R}^{1, 3}$, with the **Lorentz [[Def - Group|group]]** $O(1, 3)$ as the part fixing the origin.

This is the bridge between [[Special Relativity I — Lorentz Transformations and Minkowski Space|special relativity]] and the abstract theory of Lorentzian manifolds in this chapter: the entire content of SR is the geometry of this single flat Lorentzian manifold.

**Recall:**

![[Def - Semi-Riemannian Metric and Signature#The Definition]]

![[Def - Lorentzian Manifold#The Definition]]

The **Lorentz group** $O(1, 3)$ is the set of $4 \times 4$ real matrices $\Lambda$ satisfying $\Lambda^T \eta \Lambda = \eta$ — exactly the linear maps preserving the Minkowski metric. See [[Def - The Lorentz Group]].

The **Poincaré group** is the semidirect product $O(1, 3) \ltimes \mathbb{R}^{1, 3}$ — Lorentz transformations together with translations, the full isometry group of Minkowski space.

---

# Convergent Strategy

**Problem class.** This is a *verify that a specific tensor field is a (semi-)Riemannian metric of a given signature, then identify its isometry group* problem. The [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds#Problem-Solving Strategy|problem-solving strategy]] for verification problems is mechanical: check smoothness, symmetry, non-degeneracy, and the signature. For the isometry identification, the route is: characterise [[Def - Isometry|isometries]] as [[Def - Diffeomorphism|diffeomorphisms]] preserving the metric; for a constant tensor field, this is the same as linear maps preserving the bilinear form plus translations.

**Assumption pattern.** The setup is explicit: $M = \mathbb{R}^4$ as a smooth manifold (the standard one), and $\eta$ is a *constant* tensor field — its components $\eta_{\mu\nu}$ do not depend on position. Constant tensor fields are automatically smooth (zero derivatives). Symmetry follows from $\eta_{\mu\nu} = \eta_{\nu\mu}$ as a matrix. The signature is computed by diagonalising the (already diagonal) matrix and counting positive and negative entries.

**Theorem routing.** The verification is direct: $\eta$ is smooth, symmetric, non-degenerate ($\det \eta = -1 \neq 0$), with signature $(1, 3)$ (one positive eigenvalue $+1$ on the $t$-direction, three negative eigenvalues $-1$ on the spatial directions). For the isometry group, the route runs through the definition of isometry: a [[Def - Diffeomorphism|diffeomorphism]] $F : \mathbb{R}^4 \to \mathbb{R}^4$ with $F^* \eta = \eta$. The differential $dF_p$ must be a linear isometry of the pseudo-Euclidean space $(\mathbb{R}^4, \eta_p) = (\mathbb{R}^4, \eta)$ — that is, $dF_p \in O(1, 3)$. By a classical rigidity argument, any isometry between flat spaces with constant metric is *affine* — a linear map composed with a translation. So $\mathrm{Isom}(\mathbb{R}^4, \eta) = O(1, 3) \ltimes \mathbb{R}^{1, 3}$, the Poincaré group.

**Key decision point.** The non-obvious choice is *which [[Def - Isometry|isometries]] to enumerate*. The candidates are: linear maps preserving $\eta$ (the Lorentz group $O(1, 3)$); translations (which preserve $\eta$ because it is constant); and combinations of the two. The argument that *every* isometry is of this form requires showing that the differential of an isometry at every point is the same Lorentz matrix (since $d F_p$ depends smoothly on $p$ and takes values in $O(1, 3)$, a discrete group up to connectedness considerations). This is the Lee-style rigidity argument: an isometry of a flat space is determined by its value and differential at one point.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds#Legal Operations|the topic page's Legal Operations]]:

5. **Verify positive-definiteness or non-degeneracy in coordinates** (operation 5). The metric $\eta$ in Cartesian coordinates has determinant $-1$ (nonzero), so it is non-degenerate. The signature is $(1, 3)$, the diagonal entries.

6. **Read off the signature in any convenient basis** (operation 6). The canonical basis $\{\partial_t, \partial_x, \partial_y, \partial_z\}$ is already pseudo-orthonormal: $\eta(\partial_t, \partial_t) = 1$, $\eta(\partial_i, \partial_i) = -1$ for $i = 1, 2, 3$. The signature $(1, 3)$ is then immediate.

9. **Use an isometry to transport problems** (operation 9). The identification of $\mathrm{Isom}(\mathbb{R}^4, \eta)$ with the Poincaré group means that the symmetries of Minkowski space are exactly what physics uses: Lorentz transformations and spacetime translations.

10. **Classify a Lorentzian vector by the sign of its norm** (operation 10). The causal classification (timelike, spacelike, null) is available at every tangent space because $\eta$ is Lorentzian.

---

# Hints

> [!note]- Hint 1
> To verify smoothness: a constant tensor field is smooth (its components are constants, hence $C^\infty$ in any coordinate). Symmetry: $\eta_{\mu\nu} = \eta_{\nu\mu}$ as a diagonal matrix. Non-degeneracy: $\det\eta = 1 \cdot (-1) \cdot (-1) \cdot (-1) = -1 \neq 0$. Signature: the matrix is already diagonal with entries $(+1, -1, -1, -1)$, so one positive and three negative.

> [!note]- Hint 2
> To identify the isometry group: an isometry is a diffeomorphism $F : \mathbb{R}^4 \to \mathbb{R}^4$ with $F^*\eta = \eta$. Pointwise, $dF_p$ must satisfy $\eta(dF_p u, dF_p v) = \eta(u, v)$ for all $u, v$ — that is, $dF_p \in O(1, 3)$, the Lorentz group of $\eta$.

> [!note]- Hint 3
> A classical rigidity result: any diffeomorphism of $\mathbb{R}^n$ whose differential at every point lies in a fixed orthogonal group $O(p, q)$ must be **affine** — a linear map composed with a translation. So an isometry of Minkowski space is of the form $F(x) = \Lambda x + a$ for some $\Lambda \in O(1, 3)$ and $a \in \mathbb{R}^4$. The set of all such pairs is the **Poincaré group** $O(1, 3) \ltimes \mathbb{R}^{1, 3}$.

> [!note]- Hint 4
> The rigidity comes from the fact that $\eta$ has no curvature — there is no obstruction to "straightening out" an isometry into an affine map. Equivalently: the Lorentz group acts transitively on pseudo-orthonormal frames, and any isometry $F$ determines $\Lambda = dF_p$ at any chosen point $p$ and then $a = F(0) - \Lambda \cdot 0 = F(0)$ if the chosen point is $0$.

---

# Solution

The proof breaks into two main steps. Step 1 verifies $(\mathbb{R}^4, \eta)$ is a Lorentzian manifold by checking the four conditions (smoothness, symmetry, non-degeneracy, signature). Step 2 identifies the isometry group by showing every isometry is affine and identifying the linear part as a Lorentz transformation. The non-obvious move is the affine rigidity (Step 2), which uses the flatness of $\eta$ essentially.

**Step 1: $(\mathbb{R}^4, \eta)$ is a Lorentzian manifold.**

$\eta$ is smooth, symmetric, non-degenerate, with signature $(1, 3)$, hence a Lorentzian metric on $\mathbb{R}^4$.

> [!note]- Derivation
> **Smoothness.** $\eta = dt^2 - dx^2 - dy^2 - dz^2$ has constant components $\eta_{\mu\nu} = \mathrm{diag}(1, -1, -1, -1)$ in Cartesian coordinates. Constants are $C^\infty$, so $\eta$ is a smooth tensor field.
>
> **Symmetry.** As a matrix, $\eta_{\mu\nu} = \eta_{\nu\mu}$ (the diagonal matrix is symmetric). Tensorially, $\eta(X, Y) = \eta_{\mu\nu}X^\mu Y^\nu$ and $\eta(Y, X) = \eta_{\mu\nu}Y^\mu X^\nu = \eta_{\nu\mu}X^\nu Y^\mu = \eta_{\mu\nu}X^\mu Y^\nu$ by symmetry of the matrix.
>
> **Non-degeneracy.** $\det\eta_{\mu\nu} = 1 \cdot (-1)^3 = -1 \neq 0$. Equivalently: if $\eta(v, w) = 0$ for all $w$, taking $w = v$ gives $\eta(v, v) = (v^0)^2 - \sum_i (v^i)^2 = 0$; taking $w = (v^0, 0, 0, 0)$ gives $\eta(v, w) = v^0 \cdot v^0 = (v^0)^2 = 0$, so $v^0 = 0$; taking $w = (0, v^1, 0, 0)$ gives $-(v^1)^2 = 0$, so $v^1 = 0$; similarly $v^2 = v^3 = 0$. Hence $v = 0$.
>
> **Signature.** The matrix $\eta_{\mu\nu}$ is diagonal with entries $(1, -1, -1, -1)$: one positive entry, three negative. So the signature is $(1, 3)$ in Lee's convention.
>
> Therefore $\eta$ is a semi-Riemannian metric of signature $(1, 3)$, that is, a Lorentzian metric.

**Step 2: The isometry group is the Poincaré group $O(1, 3) \ltimes \mathbb{R}^{1, 3}$.**

An isometry $F : \mathbb{R}^4 \to \mathbb{R}^4$ has the form $F(x) = \Lambda x + a$ with $\Lambda \in O(1, 3)$ and $a \in \mathbb{R}^4$. The set of all such $F$ is the Poincaré group.

> [!note]- Derivation
> **The Poincaré group acts by isometries.** First, verify that linear Lorentz transformations and translations preserve $\eta$. For a linear map $F(x) = \Lambda x$ with $\Lambda \in O(1, 3)$: the differential is $dF_p = \Lambda$ at every $p$, and $\eta(\Lambda u, \Lambda v) = \eta(u, v)$ by definition of $\Lambda \in O(1, 3)$. So $F^*\eta = \eta$ pointwise, and $F$ is an isometry. For a translation $F(x) = x + a$: the differential is $dF_p = \mathrm{id}$ at every $p$, and $\eta(\mathrm{id}\, u, \mathrm{id}\, v) = \eta(u, v)$. So translations are isometries.
>
> Composing: any map $F(x) = \Lambda x + a$ is an isometry, being the composition of a translation and a Lorentz transformation. The set of such maps, under composition, is the Poincaré group $O(1, 3) \ltimes \mathbb{R}^{1, 3}$ (semidirect product because translations and Lorentz transformations do not commute in general).
>
> **Every isometry is in the Poincaré group.** Let $F : \mathbb{R}^4 \to \mathbb{R}^4$ be an isometry. The differential $dF_p$ at each $p$ is a linear isometry of $(T_p\mathbb{R}^4, \eta_p) \cong (\mathbb{R}^4, \eta)$ — so $dF_p \in O(1, 3)$.
>
> Set $\Lambda := dF_0$ (the differential at the origin) and $a := F(0)$. Define $G(x) := F(x) - \Lambda x - a$; we will show $G$ is identically zero, hence $F(x) = \Lambda x + a$.
>
> The differential of $G$ at any point $p$ is $dG_p = dF_p - \Lambda$. We want $dG_p = 0$ for all $p$ — equivalently $dF_p = \Lambda$ for all $p$.
>
> *Argument:* the map $p \mapsto dF_p$ is a smooth function from $\mathbb{R}^4$ to $GL(4, \mathbb{R})$ taking values in $O(1, 3)$ — the orthogonal group of the indefinite form $\eta$. But $O(1, 3)$ is a discrete [[Def - Subgroup|subgroup]] of $GL(4, \mathbb{R})$ in the sense that *as a Lie group*, the connected components of $O(1, 3)$ are open. Wait — this is not quite right: $O(1, 3)$ is a 6-dimensional Lie [[Def - Subgroup|subgroup]] of $GL(4, \mathbb{R})$.
>
> The correct argument: take any geodesic $\gamma(t) = t v$ from the origin through a point $p = v$. The image $F(\gamma)$ is a curve in $\mathbb{R}^4$. By isometry, $F$ preserves [[Def - Geodesic|geodesics]], so $F(\gamma(t))$ is a geodesic. The [[Def - Geodesic|geodesics]] of $(\mathbb{R}^4, \eta)$ are straight lines (the Christoffel symbols of the constant metric $\eta$ vanish in Cartesian coordinates, so the geodesic equation becomes $\ddot\gamma = 0$). So $F(\gamma(t))$ is a straight line in $\mathbb{R}^4$, of the form $F(0) + tw = a + tw$ for some $w \in \mathbb{R}^4$. Differentiating at $t = 0$: $w = dF_0 \cdot v = \Lambda v$. So $F(tv) = a + t\Lambda v$. Setting $t = 1$, $F(v) = a + \Lambda v = \Lambda v + a$.
>
> Since $v$ was arbitrary, $F(x) = \Lambda x + a$ for all $x \in \mathbb{R}^4$, with $\Lambda \in O(1, 3)$ and $a \in \mathbb{R}^4$. Hence $F$ is in the Poincaré group.

> [!note]- Complete formal solution
> **Part 1: $(\mathbb{R}^4, \eta)$ is a Lorentzian manifold.**
>
> The tensor field $\eta = dt^2 - dx^2 - dy^2 - dz^2$ on $\mathbb{R}^4$ has constant components $\eta_{\mu\nu} = \mathrm{diag}(1, -1, -1, -1)$ in Cartesian coordinates.
>
> - **Smoothness**: constant components are $C^\infty$.
> - **Symmetry**: $\eta_{\mu\nu} = \eta_{\nu\mu}$.
> - **Non-degeneracy**: $\det\eta_{\mu\nu} = -1 \neq 0$.
> - **Signature**: $(1, 3)$, the count of positive and negative entries.
>
> Hence $\eta$ is a semi-Riemannian metric of signature $(1, 3)$, and $(\mathbb{R}^4, \eta)$ is a Lorentzian manifold.
>
> **Part 2: $\mathrm{Isom}(\mathbb{R}^4, \eta) = O(1, 3) \ltimes \mathbb{R}^{1, 3}$, the Poincaré group.**
>
> *Inclusion ($\supseteq$).* For $\Lambda \in O(1, 3)$ and $a \in \mathbb{R}^4$, the map $F(x) = \Lambda x + a$ is smooth, has differential $dF_p = \Lambda$ at every $p$, and $\eta(\Lambda u, \Lambda v) = \eta(u, v)$ by definition of $\Lambda \in O(1, 3)$. So $F^*\eta = \eta$ pointwise, and $F$ is an isometry.
>
> *Inclusion ($\subseteq$).* Let $F : \mathbb{R}^4 \to \mathbb{R}^4$ be an isometry. Set $\Lambda = dF_0$ and $a = F(0)$. The geodesics of $(\mathbb{R}^4, \eta)$ are straight lines (the Levi-Civita connection of a constant metric in Cartesian coordinates is the trivial connection, with vanishing Christoffel symbols, so the geodesic equation $\ddot\gamma = 0$ has straight lines as solutions). Isometries send geodesics to geodesics, so for any $v \in \mathbb{R}^4$, the map $t \mapsto F(tv)$ is a straight line, equal to $F(0) + t \cdot (dF_0 v) = a + t\Lambda v$. Setting $t = 1$: $F(v) = \Lambda v + a$. So $F$ is affine with linear part $\Lambda \in O(1, 3)$ and translation part $a \in \mathbb{R}^4$.
>
> Together: $\mathrm{Isom}(\mathbb{R}^4, \eta) = O(1, 3) \ltimes \mathbb{R}^{1, 3}$.
>
> The Lorentz group $O(1, 3) \subseteq \mathrm{Isom}(\mathbb{R}^4, \eta)$ is the subgroup of isometries fixing the origin: $F(x) = \Lambda x$ for $\Lambda \in O(1, 3)$. $\blacksquare$

> [!warning] Frame-invariance check
> Two observers in different inertial frames will assign different *coordinate components* to the same event, but they will agree on every Lorentz-invariant quantity — the spacetime interval, the norm of any four-vector, the causal classification of any tangent vector. This is the geometric content of "physics is Lorentz-invariant", and it is automatic from the structure of $(\mathbb{R}^4, \eta)$ as a Lorentzian manifold: the metric $\eta$ is invariant under the Lorentz group, so any quantity built from $\eta$ is Lorentz-invariant. The Lorentz group is *exactly* the group of changes between inertial frames.

---

# Key Takeaways

**Special relativity is the geometry of one specific Lorentzian manifold.** The entire content of [[Special Relativity I — Lorentz Transformations and Minkowski Space|special relativity]] is the geometry of $(\mathbb{R}^4, \eta)$ — the flat Lorentzian manifold. Every formula of SR — time dilation, length contraction, velocity addition, mass-energy equivalence — is a consequence of (i) $\eta$ being a Lorentzian metric and (ii) physical laws being Lorentz-invariant. The abstract framework of this chapter generalises SR by allowing the metric $g$ to *vary* from point to point — which is the move from special to general relativity. Recognising that SR is "one flat case" of a vastly more general theory clarifies both subjects: SR's apparent paradoxes (twin paradox, length contraction, etc.) are geometric facts about the indefinite metric, and they generalise naturally to curved spacetimes once one accepts the formal framework.

**Isometries of flat spaces are affine — rigidity from no curvature.** A general principle: on a *flat* (semi-)Riemannian manifold (zero curvature tensor), isometries are determined by their value and differential at one point, and they extend to affine maps. This is the rigidity of flat geometry: the metric carries no local information beyond the constant inner product, so any local isometry extends globally. For Euclidean $\mathbb{R}^n$, the isometry group is $E(n) = O(n) \ltimes \mathbb{R}^n$; for Minkowski $\mathbb{R}^{1, 3}$, it is the Poincaré group $O(1, 3) \ltimes \mathbb{R}^{1, 3}$. The same rigidity fails for curved manifolds: an isometry of $S^2$ is determined by its value and differential at one point and extends to a global isometry (rotations of $S^2$), but the explicit form is constrained by the curvature.

**The Lorentz group is exactly the linear isometries of $\eta$.** A clean way to state the symmetry content of SR: the **Lorentz group** $O(1, 3)$ is *defined* as the orthogonal group of the indefinite form $\eta$ — the linear maps preserving $\eta$. Every consequence of SR follows from this characterisation: time dilation comes from the matrix elements of a boost, length contraction comes from the inverse boost, velocity addition comes from the multiplicative structure of $O(1, 3)$. The Lorentz group is not "the group of physical transformations between inertial frames" by fiat; it is the orthogonal group of $\eta$, and physics being Lorentz-invariant is the same as physics depending only on $\eta$. The same picture generalises to curved spacetimes: at each tangent space, the Lorentz group acts as the **local Lorentz group**, even though there is no global Lorentz transformation between distant tangent spaces in a curved manifold.

**Cross-link to companion exercises:** [[Ex - The Hyperbolic Plane as a Riemannian Manifold]] is the Riemannian counterpart — also a flat-in-some-sense example of a homogeneous space (in this case constant negative curvature, with a 3-dimensional isometry group $\mathrm{PSL}(2, \mathbb{R})$). [[Ex - The Round Metric on the Sphere via Restriction]] gives the round sphere as an example with positive constant curvature and $O(n+1)$ as isometry group. The triple {flat, constant positive curvature, constant negative curvature} — Minkowski/Euclidean, sphere, hyperbolic — gives the three model geometries of (pseudo-)Riemannian geometry, each with its own large isometry group.
