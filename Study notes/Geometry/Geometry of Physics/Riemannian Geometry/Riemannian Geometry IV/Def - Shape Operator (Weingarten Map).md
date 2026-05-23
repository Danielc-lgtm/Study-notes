---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Gauss Normal Map"
  - "Def - Second Fundamental Form"
  - "Def - First Fundamental Form"
tags: [geometry, riemannian-geometry, surfaces, shape-operator]
---

# Notation

Let $M \subset \mathbb{R}^3$ be an oriented regular surface with unit normal $N$. We identify $T_{N(p)}S^2$ with $T_pM$ via parallel translation in $\mathbb{R}^3$ (both are the orthogonal complement of $N(p) \in \mathbb{R}^3$). Full registry on [[Riemannian Geometry IV — Classical Geometry of Surfaces in R^3]].

---

# Axiom Motivation

The [[Def - Second Fundamental Form|second fundamental form]] $\mathrm{II}$ is a bilinear form on $T_pM$. The [[Def - First Fundamental Form|first fundamental form]] $\mathrm{I}$ is another bilinear form on $T_pM$. Any bilinear form on a finite-dimensional inner-product space is canonically identified with a linear operator (via the dual-space isomorphism induced by the inner product). The **shape operator** $S$ is the linear operator that corresponds to $\mathrm{II}$ under this identification using $\mathrm{I}$.

**Why convert a bilinear form to a linear operator?** Linear operators have all the machinery of linear algebra: eigenvalues, eigenvectors, trace, determinant, spectral theorem. A bilinear form by itself has only quadratic-form data (the diagonal $\mathrm{II}(X, X)$). The operator $S$ exposes the *eigenvalue structure* of $\mathrm{II}$ — namely the [[Def - Principal Curvatures and Directions|principal curvatures $\kappa_1, \kappa_2$]] and principal directions — which is exactly the data one wants to do geometry with. Without converting to the operator picture, the spectral theorem would not be available, and the principal curvatures could not be defined as "eigenvalues of curvature".

**Why $S = -dN$ rather than $S = +dN$?** This is a sign convention. Both choices are made in the literature (Frankel uses $-$, do Carmo uses $-$, others use $+$). The choice $S = -dN$ has the virtue that on a convex surface with outward normal — for instance the unit sphere from outside — the principal curvatures come out *positive*. Specifically on the unit sphere $N = p$, so $dN = \mathrm{id}$, and $S = -\mathrm{id}$ has eigenvalues $-1$; with the *inward* normal, $N = -p$, $dN = -\mathrm{id}$, $S = +\mathrm{id}$ has eigenvalues $+1$. So with **outward normal**, Frankel's convention gives the convex sphere $\kappa = -1$ (which can be jarring); with **inward normal**, Frankel's convention gives the convex sphere $\kappa = +1$. The product $K = \kappa_1\kappa_2 = +1 > 0$ is the same either way, and $H$ flips sign with the choice. We follow Frankel: $S = -dN$, and we mention the outward/inward sign at every relevant point.

**Why does the spectral theorem apply (self-adjointness)?** The shape operator is self-adjoint with respect to $\mathrm{I}$:
$$
\langle SX, Y\rangle_\mathrm{I} = \mathrm{II}(X, Y) = \mathrm{II}(Y, X) = \langle SY, X\rangle_\mathrm{I} = \langle X, SY\rangle_\mathrm{I},
$$
using the symmetry of $\mathrm{II}$ established for the second fundamental form. Self-adjointness is what makes the spectral theorem apply, guaranteeing that $S$ is diagonalisable over $\mathbb{R}$ with orthogonal eigenvectors — the principal directions. Without symmetry of $\mathrm{II}$, $S$ would not be self-adjoint and might have complex eigenvalues or non-orthogonal eigenvectors; this would prevent the clean "principal curvature" picture entirely.

**Why is this construction "the metric dual"?** Given any symmetric bilinear form $B$ on an inner-product space $(V, \langle\cdot,\cdot\rangle)$, there is a unique linear operator $A : V \to V$ such that $B(X, Y) = \langle AX, Y\rangle$ for all $X, Y$ — namely $A = \mathrm{I}^{-1}B$ in matrix form, where the inner product matrix $\mathrm{I}$ is used to "raise an index". For surfaces, in coordinates, $b^\alpha_{\;\beta} = g^{\alpha\gamma}b_{\gamma\beta}$ is exactly this index-raising operation, converting the $(0, 2)$-tensor $b_{\alpha\beta}$ into the $(1, 1)$-tensor (linear operator) $b^\alpha_{\;\beta}$.

A forward reference: the [[Def - Gauss Curvature and Mean Curvature|Gauss and mean curvatures]] $K = \det S$ and $H = \mathrm{tr}\, S$ are the **basis-independent invariants of $S$** at a point — every other algebraic invariant ($\kappa_1, \kappa_2$, the discriminant) is a function of these two. The shape operator is the right level of abstraction at which the curvature invariants live as natural objects.

---

# The Definition

> **Definition (Shape Operator / Weingarten Map).** Let $M \subset \mathbb{R}^3$ be an oriented regular surface with unit normal $N$. The **shape operator** at $p \in M$ is the linear map
> $$
> S_p : T_pM \to T_pM, \qquad S_p := -dN_p,
> $$
> where $dN_p : T_pM \to T_{N(p)}S^2$ is the differential of the [[Def - Gauss Normal Map|Gauss normal map]] and $T_{N(p)}S^2 \cong T_pM$ via parallel translation in $\mathbb{R}^3$.

Equivalently, $S_p$ is the unique linear map satisfying
$$
\langle S_p X, Y\rangle_\mathrm{I} = \mathrm{II}_p(X, Y), \qquad X, Y \in T_pM,
$$
the **metric dual** of the [[Def - Second Fundamental Form|second fundamental form]] $\mathrm{II}$.

In a local parametrisation $\mathbf{x}(u, v)$ with coordinate frame $\{\mathbf{x}_1, \mathbf{x}_2\}$, the matrix of $S$ is
$$
S(\mathbf{x}_\beta) = -N_\beta = -\partial N/\partial u^\beta = b^\alpha_{\;\beta}\mathbf{x}_\alpha,
\qquad b^\alpha_{\;\beta} = g^{\alpha\gamma}b_{\gamma\beta}.
$$
These are the **Weingarten equations**. The matrix
$$
[b^\alpha_{\;\beta}] = [g^{\alpha\gamma}][b_{\gamma\beta}] = \begin{pmatrix} E & F \\ F & G\end{pmatrix}^{-1}\begin{pmatrix} e & f \\ f & g_\mathrm{II}\end{pmatrix}
$$
has eigenvalues the [[Def - Principal Curvatures and Directions|principal curvatures]] $\kappa_1, \kappa_2$, trace $\mathrm{tr}\, S = b^\alpha_{\;\alpha} = H$ the mean curvature, and determinant $\det S = K$ the Gauss curvature.

**Self-adjointness.** $S_p$ is self-adjoint with respect to $\mathrm{I}_p$:
$$
\langle S_p X, Y\rangle = \langle X, S_p Y\rangle, \qquad X, Y \in T_pM,
$$
because $\mathrm{II}$ is symmetric. By the spectral theorem, $S_p$ is diagonalisable over $\mathbb{R}$ with orthogonal eigenvectors.

---

# Categorical / Structural Definition

Structurally, the shape operator is **the Weingarten map** $T_pM \to T_pM$ that measures how the tangent plane "rotates" as one moves on $M$. The framework is: the tangent bundle $TM \to M$ has fibres $T_pM$, each a $2$-plane in $\mathbb{R}^3$. As $p$ varies, $T_pM$ rotates — and the infinitesimal rate of rotation at each point is encoded by an element of the Lie algebra of the rotation group $\mathfrak{so}(3)$, decomposed into "in-plane rotation" (the [[Def - Connection on a Vector Bundle|connection]] of the metric, intrinsic) and "out-of-plane rotation" (the shape operator, extrinsic).

The standard categorical packaging: a hypersurface $M \subset \mathbb{R}^{n+1}$ has a Gauss map $N : M \to S^n$, and the differential $-dN : TM \to TM$ (after identifying $T_{N(p)}S^n$ with $T_pM$) is the shape operator. The construction is *exactly* "differentiate the classifying map of the normal bundle", and in modern language this is the curvature of the connection on the normal bundle. The codimension-$1$ feature is that the normal bundle is trivial of rank $1$, so the shape operator is a scalar-coefficient linear operator on $TM$.

For higher-codimension submanifolds $M^k \subset \mathbb{R}^n$, the shape operator becomes a **vector-valued** symmetric bilinear form $\mathrm{II} : T_pM \times T_pM \to \nu_pM$, or equivalently a family of scalar-valued shape operators $S_\xi$ indexed by normal vectors $\xi \in \nu_pM$, with $S_\xi(X, Y) = \langle\mathrm{II}(X, Y), \xi\rangle$. The codimension-$1$ Frankel definition picks out the single normal direction and gets the scalar-coefficient version.

Functorially: the shape operator at $p$ is a self-adjoint endomorphism of $T_pM$, so it lives in $\mathrm{End}(T_pM)$, and as $p$ varies it gives a smooth section of $\mathrm{End}(TM) \cong T^*M \otimes TM$. The trace and determinant of this section are well-defined smooth functions on $M$ — the **mean curvature** and **Gauss curvature**.

---

# Relate to Other Fields / Compression

The shape operator is the **linear-algebraic representative of the second fundamental form** in the same way the linear operator $A$ represents the bilinear form $B(X, Y) = \langle AX, Y\rangle$ in linear algebra. Working with $S$ rather than $\mathrm{II}$ enables eigenvalue computations, the spectral theorem, the trace and determinant, and the entire machinery of self-adjoint operator theory.

In **convex geometry**, the shape operator of a convex hypersurface has all positive (or all negative, depending on normal) eigenvalues. The convex case is also where the **support function** parametrisation becomes available, and the shape operator's inverse $S^{-1}$ has a nice geometric meaning (radii of curvature).

In **physics** (general relativity and continuum mechanics), the analogue is the **extrinsic curvature tensor** $K_{ij}$ of a spacelike slice, defined as the rate of change of the slice's metric under the lapse-and-shift flow. The eigenvalues of $K_{ij}$ are the principal extrinsic curvatures, and they enter the ADM Hamiltonian of general relativity directly.

In **conformal geometry**, the **trace-free part of the shape operator** $S - \tfrac{1}{2}H\cdot\mathrm{id}$ is the **umbilic tensor**, which measures deviation from being an umbilic (sphere-like) point. Vanishing of the umbilic tensor characterises totally umbilic surfaces.

**True name:** The shape operator is *the matrix whose eigenvalues are the principal curvatures*. The official "$S = -dN$" or "metric dual of $\mathrm{II}$" is the right definition, but the operational picture is: $S$ is the $2 \times 2$ matrix at each point, whose eigenvalues $(\kappa_1, \kappa_2)$ are the maximum and minimum normal-section curvatures, and whose eigenvectors give the principal directions. This eigenvalue picture is what one reaches for in computations and what makes $K = \det S$, $H = \mathrm{tr}\, S$ natural.

---

# Examples / Corollaries

**Is an instance — the unit sphere.** With outward normal, $N(p) = p$ on $S^2$, so $dN_p = \mathrm{id}$ and $S_p = -\mathrm{id}$. Every direction is an eigendirection with eigenvalue $-1$, so $\kappa_1 = \kappa_2 = -1$ (the sphere is **umbilic**), and $K = +1$, $H = -2$ (Frankel convention; under do Carmo, $H = -1$, dividing by 2). Every point of the sphere is an umbilic, consistent with classical theorems on umbilic surfaces.

**Is an instance — the cylinder.** With $\mathbf{x}(u, v) = (a\cos u, a\sin u, v)$ and outward normal $N = (\cos u, \sin u, 0)$, $\partial N/\partial u = (-\sin u, \cos u, 0) = -\mathbf{x}_u/a$, and $\partial N/\partial v = 0$. So $S(\mathbf{x}_u) = -\partial N/\partial u = \mathbf{x}_u/a$, i.e., $\mathbf{x}_u$ is an eigenvector with eigenvalue $1/a$; and $S(\mathbf{x}_v) = -\partial N/\partial v = 0$, so $\mathbf{x}_v$ is an eigenvector with eigenvalue $0$. The principal curvatures are $\kappa_1 = 1/a$ (around the cylinder) and $\kappa_2 = 0$ (along the axis); $K = 0$, $H = 1/a$.

**Is an instance — the saddle $z = uv$ at origin.** With $\mathbf{x}(u, v) = (u, v, uv)$, at origin $E = G = 1$, $F = 0$, $N = (0, 0, 1)$. $\mathbf{x}_{uu} = 0$, $\mathbf{x}_{vv} = 0$, $\mathbf{x}_{uv} = (0, 0, 1) = N$. So $b_{11} = b_{22} = 0$, $b_{12} = 1$. The shape operator matrix at origin is $\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$, with eigenvalues $\pm 1$ and eigenvectors $(1, \pm 1)/\sqrt 2$ — the principal directions are the diagonals of the saddle.

**Is NOT an instance — a non-self-adjoint operator.** Any non-self-adjoint $2 \times 2$ matrix (e.g., a rotation) does not arise as a shape operator, because shape operators are forced to be self-adjoint by symmetry of $\mathrm{II}$. So "rotation by $90°$" is not the shape operator of any surface.

**Is NOT an instance — a "shape operator" on a non-orientable surface globally.** The Möbius strip has no continuous unit normal field, hence no global Gauss map, hence no globally defined shape operator. Locally on each orientation-preserving chart, the shape operator is defined, but the sign is ambiguous globally.

**Corollary — the **principal curvatures and directions** are exactly the eigenvalues and eigenvectors of $S$.** Self-adjointness gives real eigenvalues; the spectral theorem orthogonality of eigenvectors (when eigenvalues differ); the case of repeated eigenvalues is umbilic, with every direction an eigendirection.

**Corollary — the Gauss curvature is $K = \det S$, the mean curvature is $H = \mathrm{tr}\, S$.** Both are basis-independent invariants of $S$ as a linear operator. Trace and determinant are the elementary symmetric polynomials in the eigenvalues $\kappa_1, \kappa_2$: $K = \kappa_1\kappa_2$ and $H = \kappa_1 + \kappa_2$.

**Corollary — under reversal of normal $N \to -N$, $S \to -S$.** The Gauss curvature $K = \det S$ is preserved (it depends on $\det(-S) = (-1)^2\det S = \det S$ for $2 \times 2$ matrices); the mean curvature $H = \mathrm{tr}\, S$ flips sign. This is the precise reason $K$ is intrinsic (after Theorema Egregium) and $H$ is not.

**Calibration check.** If you have understood the definition, you should be able to: (i) verify that for a surface of revolution with meridian curve of curvature $\kappa_m$ and "parallel" (longitudinal) direction with normal curvature $\kappa_p = \cos\phi/r$ (where $r$ is the distance to axis and $\phi$ the meridian angle from the horizontal), the principal curvatures are exactly $\kappa_1 = \kappa_m$ and $\kappa_2 = \kappa_p$ — the meridian and parallel directions are principal because the surface of revolution has a reflectional symmetry; (ii) check that the shape operator of a graph $z = f(x, y)$ at the origin (with $\nabla f(0) = 0$, so the tangent plane is $z = 0$) is just the Hessian matrix $\nabla^2 f(0)$ divided by the normalising factor $\sqrt{1 + |\nabla f|^2}$ — at origin the factor is $1$, so $S(0) = \nabla^2 f(0)$ for graphs whose tangent plane at origin is the $xy$-plane; (iii) verify by direct computation that on the sphere of radius $a$, the shape operator $S = -dN$ where $N(p) = p/a$ gives $S = -\mathrm{id}/a$, so $K = 1/a^2$.

---

# Unlocked by This

> [!tip] Principal Curvatures and Directions *(from §4.2)*
> The eigenvalues and eigenvectors of $S$ are the [[Def - Principal Curvatures and Directions|principal curvatures]] and principal directions, the canonical "diagonal coordinates" for surface curvature at a point. Euler's formula $\kappa(\theta) = \kappa_1\cos^2\theta + \kappa_2\sin^2\theta$ recovers the normal curvature in any direction from $\kappa_1, \kappa_2$ and the angle.

> [!tip] Gauss and Mean Curvatures *(from §4.2)*
> The two basis-independent invariants of $S$ are $K = \det S$ ([[Def - Gauss Curvature and Mean Curvature|Gauss curvature]]) and $H = \mathrm{tr}\, S$ (mean curvature). $K$ classifies the local shape (elliptic/hyperbolic/parabolic), and $H$ controls the variational problem of area (the minimal-surface equation is $H = 0$).

> [!tip] Lines of Curvature *(from Classical Surface Theory)*
> The integral curves of the principal-direction fields are the **lines of curvature**, an orthogonal net on $M$ (away from umbilics) that diagonalises both $\mathrm{I}$ and $\mathrm{II}$. The **principal coordinates** $(u, v)$ adapted to the lines of curvature satisfy $F = 0$ (orthogonality) and $f = 0$ (diagonalisation of $\mathrm{II}$), greatly simplifying the formulae for $K, H$. Dupin's theorem on triply orthogonal systems is one classical descendant.

> [!tip] Higher-Codimension Submanifolds *(from Differential Geometry)*
> For a submanifold $M^k \subset \mathbb{R}^n$ of codimension $> 1$, the shape operator becomes a **vector-valued bilinear form** $\mathrm{II} : TM \times TM \to \nu M$ into the normal bundle. The mean curvature vector $\vec H = \mathrm{tr}_g \mathrm{II}$ controls the first variation of $k$-volume, and minimal submanifolds satisfy $\vec H = 0$. This is the **geometric measure theory** generalisation of the surface case.
