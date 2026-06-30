---
type: definition
subject: special-relativity
prereqs:
  - "Thm - Invariant Null Direction of a Restricted Lorentz Transformation"
  - "Def - Subgroups and Components of the Lorentz Group"
  - "Def - Boosts as Hyperbolic Rotations"
  - "Def - Classification of Four-Vectors"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. $\Lambda \in SO^+(1,3)$ is a [[Def - Subgroups and Components of the Lorentz Group|restricted Lorentz transformation]]. We build adapted frames from a future null eigenvector $\ell$ ($\ell\cdot\ell = 0$, $\Lambda\ell = e^\psi\ell$) and a partner future null vector $k$ ($k\cdot k = 0$) normalised by $\ell\cdot k = 2$; from these, $e_0 = \tfrac12(\ell+k)$ (timelike, $e_0\cdot e_0 = +1$) and $e_1 = \tfrac12(\ell-k)$ (spacelike, $e_1\cdot e_1 = -1$). The basis $(\ell, k, e_2, e_3)$ is denoted $(e^*_\alpha)$ and is *not* orthonormal; $(e_0,e_1,e_2,e_3)$ is the associated orthonormal basis. Parameters: $\psi \in \mathbb{R}$ (rapidity), $\theta \in [0,2\pi)$ (rotation angle), $\alpha \in \mathbb{R}^+$ (null-rotation parameter). Full registry on [[Special Relativity IX — The Lorentz Group, Structure and Classification]].

This is a compound page: it defines five interlocking notions — the general **three-parameter normal form** of a restricted Lorentz transformation, and its four named special cases (**spatial rotation**, **Lorentz boost**, **null rotation**, **four-screw**) — because they are introduced together as the complete classification and each is a degeneration of the general form.

---

# Axiom Motivation

By [[Thm - Invariant Null Direction of a Restricted Lorentz Transformation|the existence theorem]], every restricted $\Lambda$ fixes a null direction. The motivation for this page is to exploit that single fixed direction to the hilt: to build, from one invariant null vector, an entire frame in which $\Lambda$'s matrix is as simple as possible — and then to read the classification off the matrix. The design question is: *what frame makes a transformation that fixes a null direction look simplest?*

The naive answer — an orthonormal frame with $e_0$ timelike — is wrong, and seeing why is the whole motivation. A transformation that fixes a *null* direction does not fix any timelike or spacelike direction in general, so a frame anchored on $e_0$ is not adapted to the transformation's symmetry. The right frame is anchored on the *null* structure: take the fixed null vector $\ell$ as a basis vector. But a single null vector cannot anchor a frame, because $\ell\cdot\ell = 0$ — it has no length to normalise against. So one needs a *partner*: a second null vector $k$, future-pointing, not collinear with $\ell$. Two future null vectors always have a definite-sign inner product (the reversed Cauchy–Schwarz inequality gives $\ell\cdot k > 0$ in our signature), so $k$ can be rescaled to set $\ell\cdot k = 2$. The pair $(\ell, k)$ spans a *timelike plane* $\Pi_0$ — it contains timelike directions like $e_0 = \tfrac12(\ell+k)$ — and the constant $2$ is chosen precisely so that $e_0 = \tfrac12(\ell+k)$ and $e_1 = \tfrac12(\ell-k)$ come out orthonormal: $e_0\cdot e_0 = \tfrac14(\ell\cdot\ell + 2\ell\cdot k + k\cdot k) = \tfrac14(0+4+0) = 1$, and $e_1\cdot e_1 = \tfrac14(0 - 4 + 0) = -1$, with $e_0\cdot e_1 = \tfrac14(\ell\cdot\ell - k\cdot k) = 0$.

Why does this make the matrix simple? Because $\ell$ is an eigenvector, the first column of $\Lambda$ in the basis $(e^*_\alpha) = (\ell, k, e_2, e_3)$ is almost trivial — $\Lambda\ell = e^\psi\ell$. Forcing $\Lambda$ to preserve the scalar products $\ell\cdot k = 2$, $\ell\cdot e_i = 0$, $e_i\cdot e_j = -\delta_{ij}$ then pins down every other entry up to three free numbers: the eigenvalue exponent $\psi$, a rotation angle $\theta$ in the spacelike plane $\mathrm{Span}(e_2, e_3)$, and a "shear" parameter $\alpha$ measuring how much $\Lambda$ tilts $k$ toward $\ell$ and $e_2$. These three parameters are forced — no fewer suffice to satisfy the constraints, no more are allowed by them — which is why the normal form has exactly three parameters, matching the dimension count $\dim SO^+(1,3) = 6$ minus the three parameters of the choice of frame.

The classification into named types is then the bookkeeping of which parameters vanish. Setting $\psi = 0$ and $\alpha = 0$ leaves only $\theta$: a pure rotation of the spacelike plane $\Pi_1 = \mathrm{Span}(e_2,e_3)$, fixing the timelike plane $\Pi_0$ — a **spatial rotation**. Setting $\alpha = 0$ and $\theta = 0$ leaves only $\psi$: a hyperbolic rotation of $\Pi_0$, fixing $\Pi_1$ pointwise — a **boost**. Setting $\psi = 0$ and $\theta = 0$ leaves only $\alpha$: a shear that fixes the single null direction $\mathrm{Span}(\ell)$ and a degenerate *null plane* — a **null rotation**. The general case with $\psi, \theta$ both nonzero and $\alpha = 0$ is a commuting boost-and-rotation in orthogonal planes — a **four-screw**. The reason there is no fifth type is that the parameter $\alpha$ cannot coexist with $\psi$ or $\theta$ as an independent third option: the summary analysis shows $\Lambda$ has a *unique* invariant null direction precisely when $\psi = \theta = 0$ (the null-rotation case), and *two* whenever $\psi$ or $\theta$ is nonzero (forcing $\alpha = 0$, the four-screw case). The would-be "general three-parameter" transformation with all of $\psi, \theta, \alpha$ nonzero does not exist as a new type — it is always conjugate to a four-screw.

---

# The Definition

Let $\Lambda \in SO^+(1,3)$, and let $\ell$ be a future null eigenvector ($\Lambda\ell = e^\psi\ell$), $k$ a partner future null vector with $\ell\cdot k = 2$, and $(e_0, e_1, e_2, e_3)$ the orthonormal frame with $e_0 = \tfrac12(\ell+k)$, $e_1 = \tfrac12(\ell-k)$, $(e_2, e_3)$ a right-handed orthonormal basis of $\mathrm{Span}(e_2,e_3) = \{e_0,e_1\}^\perp$.

**General normal form.** In the basis $(e^*_\alpha) = (\ell, k, e_2, e_3)$ the matrix of $\Lambda$ is
$$
(\Lambda^*)^\alpha{}_\beta =
\begin{pmatrix}
e^{\psi} & 4\alpha^2 e^{-\psi} & 2\alpha\cos\theta & -2\alpha\sin\theta \\
0 & e^{-\psi} & 0 & 0 \\
0 & 4\alpha e^{-\psi} & \cos\theta & -\sin\theta \\
0 & 0 & \sin\theta & \cos\theta
\end{pmatrix},
$$
and in the orthonormal basis $(e_0,e_1,e_2,e_3)$ (via $e_0 = \tfrac12(\ell+k)$, $e_1 = \tfrac12(\ell-k)$),
$$
\Lambda^\alpha{}_\beta =
\begin{pmatrix}
\cosh\psi + 2\alpha^2 e^{-\psi} & \sinh\psi - 2\alpha^2 e^{-\psi} & 2\alpha\cos\theta & -2\alpha\sin\theta \\
\sinh\psi + 2\alpha^2 e^{-\psi} & \cosh\psi - 2\alpha^2 e^{-\psi} & 2\alpha\cos\theta & -2\alpha\sin\theta \\
2\alpha e^{-\psi} & -2\alpha e^{-\psi} & \cos\theta & -\sin\theta \\
0 & 0 & \sin\theta & \cos\theta
\end{pmatrix},
$$
depending on the three parameters $\psi \in \mathbb{R}$, $\alpha \in \mathbb{R}^+$, $\theta \in [0,2\pi)$. This is the most general restricted Lorentz transformation.

The four named cases are:

**Spatial rotation** ($\psi = 0$, $\alpha = 0$): the matrix reduces to $\mathrm{diag}\big(1, 1, \begin{smallmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{smallmatrix}\big)$. It fixes the timelike plane $\Pi_0 = \mathrm{Span}(e_0, e_1)$ pointwise and acts on the spacelike plane $\Pi_1 = \mathrm{Span}(e_2, e_3)$ as an ordinary rotation of angle $\theta$. A **spatial rotation** is any restricted transformation leaving a *timelike* plane strictly invariant; its orthogonal complement (spacelike) is the **plane of the rotation**. The angle satisfies $\cos\theta = \tfrac12\mathrm{tr}\,\Lambda - 1$.

**Lorentz boost** ($\alpha = 0$, $\theta = 0$): the matrix reduces to $\mathrm{diag}\big(\begin{smallmatrix}\cosh\psi & \sinh\psi\\ \sinh\psi & \cosh\psi\end{smallmatrix}, 1, 1\big)$. It acts on the timelike plane $\Pi_0$ as a hyperbolic rotation and fixes the spacelike plane $\Pi_1$ pointwise. A [[Def - Boosts as Hyperbolic Rotations|Lorentz boost]] is any restricted transformation leaving a *spacelike* plane strictly invariant; its orthogonal complement (timelike) is the **plane of the boost**. The rapidity satisfies $\cosh\psi = \tfrac12\mathrm{tr}\,\Lambda - 1$.

**Null rotation** ($\psi = 0$, $\theta = 0$): the matrix in $(e^*_\alpha)$ is $\begin{pmatrix} 1 & 4\alpha^2 & 2\alpha & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 4\alpha & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$. It fixes the null direction $\mathrm{Span}(\ell)$ and leaves invariant the *null plane* $\Pi_3 = \mathrm{Span}(\ell, e_3)$, whose induced metric is degenerate. A **null rotation** is any restricted transformation leaving a null plane strictly invariant; see [[Def - Null Rotations and Four-Screws]].

**Four-screw** (general $\psi, \theta$ with $\alpha = 0$): the matrix is block diagonal, a boost of rapidity $\psi$ in $\Pi_0$ and a rotation of angle $\theta$ in $\Pi_1$, the two blocks commuting. A **four-screw** of timelike plane $\Pi_0$ is the composition $\Lambda = S\circ R = R\circ S$ of a boost $S$ of $\Pi_0$ and a spatial rotation $R$ of $\Pi_0^\perp = \Pi_1$; see [[Def - Null Rotations and Four-Screws]]. Boosts ($\theta = 0$) and spatial rotations ($\psi = 0$) are the degenerate four-screws.

**Completeness.** Every restricted Lorentz transformation is a four-screw or a null rotation. It admits a unique invariant null direction iff it is a null rotation ($\psi = \theta = 0$, $\alpha \ne 0$); two distinct invariant null directions iff it is a four-screw with $\psi \ne 0$ or $\theta \ne 0$; and three or more iff it is the identity.

---

# Categorical / Structural Definition

The classification is the orbit structure of the conjugation action of $SO^+(1,3)$ on itself: two restricted transformations are conjugate iff they have the same type and the same parameters $(\psi, \theta)$ or $\alpha$. The conjugacy classes are therefore parametrised by:
- the boost-rapidity $\psi \ge 0$ and rotation-angle $\theta \in [0,\pi]$, for four-screws (a two-parameter family of classes, including the one-parameter sub-families of pure boosts $\theta = 0$ and pure rotations $\psi = 0$);
- the single parameter $\alpha > 0$ up to rescaling — in fact all null rotations with $\alpha > 0$ are conjugate, so there is a *single* conjugacy class of nontrivial null rotations;
- the identity, its own class.

This mirrors the Jordan classification of matrices: a four-screw is *diagonalisable* (over $\mathbb{C}$, with eigenvalues $e^{\pm\psi}$ and $e^{\pm i\theta}$), while a null rotation is a single nontrivial *Jordan block* (eigenvalue $1$, a $3\times 3$ unipotent block plus a $1\times 1$). The dichotomy "four-screw versus null rotation" is precisely "diagonalisable versus non-diagonalisable" for elements of $SO^+(1,3)$. Through the [[Thm - SL(2,C) is the Double Cover of the Restricted Lorentz Group|double cover]], it becomes the classification of conjugacy classes in $SL(2,\mathbb{C})$ by the trace of the $2\times 2$ matrix: $|\mathrm{tr}\,A| \ne 2$ gives a loxodromic (diagonalisable) element, a four-screw; $\mathrm{tr}\,A = \pm 2$ with $A \ne \pm I$ gives a parabolic (Jordan-block) element, a null rotation; $A = \pm I$ gives the identity.

---

# Relate to Other Fields / Compression

The classification is the Lorentzian analogue of the conjugacy-class structure of the Euclidean isometry group, with one extra type. In the plane, an orientation-preserving isometry is a rotation or a translation (a "rotation about a point at infinity"). On the Riemann sphere, a Möbius transformation is elliptic (two fixed points, rotation-like), hyperbolic/loxodromic (two fixed points, scaling-like), or parabolic (one fixed point). The restricted Lorentz group's classification is exactly the Möbius classification pulled back through the spinor map: spatial rotations are elliptic, boosts are hyperbolic, four-screws are loxodromic (elliptic $\times$ hyperbolic), and null rotations are parabolic.

**True name:** a restricted Lorentz transformation is "a conjugacy class in $SL(2,\mathbb{C})$ labelled by trace" — loxodromic ($|\mathrm{tr}| \ne 2$, a four-screw) or parabolic ($\mathrm{tr} = \pm 2$, a null rotation). The geometric description (which plane is invariant) is the official definition, but the operational characterisation that decides the type fastest is the trace of the $2\times 2$ lift, or equivalently the eigenvalue/Jordan structure of the $4\times 4$ matrix: diagonalisable means four-screw, a nontrivial Jordan block means null rotation.

---

# Examples / Corollaries

**Is an instance — a boost along $x$.** $\Lambda = \mathrm{diag}\big(\begin{smallmatrix}\cosh\psi & \sinh\psi\\ \sinh\psi & \cosh\psi\end{smallmatrix}, 1, 1\big)$ is the $\alpha = \theta = 0$ case. Its invariant null directions are $\mathrm{Span}(e_0 + e_1)$ and $\mathrm{Span}(e_0 - e_1)$ — two of them — confirming it is a four-screw (degenerate, with $\theta = 0$). Its trace is $2\cosh\psi + 2$.

**Is an instance — a rotation about $z$.** $\Lambda = \mathrm{diag}\big(1, \begin{smallmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{smallmatrix}, 1\big)$ acting on $(x,y)$ is the $\psi = \alpha = 0$ case. For $\theta \ne 0, \pi$ it has *no* real null eigenvector other than those on the fixed axis $\mathrm{Span}(e_0, e_3)$ direction... more precisely its invariant null directions are the two on the light cone of the fixed timelike plane $\mathrm{Span}(e_0, e_3)$, namely $\mathrm{Span}(e_0\pm e_3)$. Its trace is $2\cos\theta + 2$.

**Is an instance — a null rotation.** With $\psi = \theta = 0$, $\alpha = \tfrac12$, the matrix $\begin{pmatrix} 1 & 1 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 2 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$ in $(\ell, k, e_2, e_3)$ fixes only $\mathrm{Span}(\ell)$ among null directions. It is not diagonalisable: $\Lambda - \mathrm{Id}$ is nilpotent of index three.

**Is NOT an instance — a transformation with all three parameters nonzero is not a fifth type.** One might write down the general matrix with $\psi, \theta, \alpha$ all nonzero and call it a new "screw-with-shear." It is not a new type: the summary analysis shows that whenever $\psi \ne 0$ or $\theta \ne 0$, the second invariant null direction forces $\alpha$ to be removable by conjugation — such a transformation is conjugate to a four-screw with $\alpha = 0$. The three-parameter form is a *parametrisation by choice of frame*, not three independent physical invariants; the physical invariants are $(\psi, \theta)$ for a four-screw or $\alpha$ (up to scale, hence trivial) for a null rotation.

**Is NOT an instance — a boost-times-rotation in non-orthogonal planes is not a four-screw.** If a boost of one plane is composed with a rotation of a plane *not* orthogonal to it, the result is generally a four-screw of some *third* plane (or a null rotation), but it is not "the four-screw of either original plane." The four-screw requires the boost and rotation planes to be orthogonal complements; otherwise the composition must be re-classified from scratch, as in the Thomas-rotation analysis.

**Corollary — the trace test.** From the matrices: a four-screw has $\mathrm{tr}\,\Lambda = 2\cosh\psi + 2\cos\theta$, a boost $2\cosh\psi + 2$, a rotation $2\cos\theta + 2$, a null rotation $4$ (set $\psi = \theta = 0$: trace $= 1 + 1 + 1 + 1 = 4$). So a restricted transformation with $\mathrm{tr}\,\Lambda = 4$ is either the identity or a null rotation — and one tells them apart by whether $\Lambda = \mathrm{Id}$.

**Calibration check.** The reader who has understood the classification should be able to: (i) given $\ell$ with $\ell\cdot\ell = 0$ and a future $k$ with $\ell\cdot k = 2$, verify $e_0 = \tfrac12(\ell+k)$, $e_1 = \tfrac12(\ell-k)$ are orthonormal; (ii) from a $4\times 4$ restricted matrix, compute the trace and decide whether it is a boost ($> 4$, two real null eigenvectors), a rotation ($< 4$), or a null-rotation/identity candidate ($= 4$); (iii) state the number of invariant null directions for each of the four named types.

---

# Unlocked by This

> [!tip] The Jordan Normal Form over the Lorentz Group *(from linear algebra and Special Relativity XI)*
> The classification is the Jordan canonical form specialised to $SO^+(1,3)$: a four-screw is diagonalisable (eigenvalues $e^{\pm\psi}, e^{\pm i\theta}$), a null rotation is a single nontrivial Jordan block (eigenvalue $1$, unipotent of index three). Through the **spinor map** this becomes the trace classification of $SL(2,\mathbb{C})$ — loxodromic when $|\mathrm{tr}\,A| \ne 2$, parabolic when $\mathrm{tr}\,A = \pm 2$ — which is the cleanest algebraic statement of the whole taxonomy. See [[Special Relativity XI — SL(2,C), Spinors and the Spinor Map]] and [[Thm - SL(2,C) is the Double Cover of the Restricted Lorentz Group]].

> [!tip] The Generators of the Lie Algebra and the Exponential Map *(from Special Relativity X)*
> Each named type lies on a one-parameter subgroup $\exp(t\omega)$ of $SO^+(1,3)$, with $\omega$ in the [[Def - Lie Algebra of the Lorentz Group|Lie algebra]] $\mathfrak{so}(1,3)$: a boost generator $K_i$ (whose exponential is a boost), a rotation generator $J_i$ (a rotation), or the nilpotent combination $K_x + J_y$ (a null rotation, whose exponential is the unipotent matrix above). The classification of group elements mirrors the classification of Lie-algebra elements by their eigenvalue structure — diagonalisable generators give four-screws, nilpotent generators give null rotations. See [[Special Relativity X — The Lorentz Group as a Lie Group]].
