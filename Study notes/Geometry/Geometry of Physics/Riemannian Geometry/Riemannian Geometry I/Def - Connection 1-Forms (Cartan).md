---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Affine Connection on a Vector Bundle"
  - "Def - Christoffel Symbols"
  - "Def - Local Frame"
  - "Def - Differential k-Form on a Manifold"
tags: [geometry, riemannian-geometry, connections, cartan-formalism]
---

# Notation

$(M, \nabla)$ — smooth manifold with an affine connection on $TM$ (or more generally a vector bundle $E \to M$ with connection). $e = (e_1, \ldots, e_n)$ — a local frame of vector fields (sections of $TM$, or of $E$, on an open set $U \subseteq M$). $(\sigma^1, \ldots, \sigma^n)$ — the dual coframe, $\sigma^a(e_b) = \delta^a_b$. $\omega^a{}_b$ or $\Gamma^a{}_b$ — the **connection 1-forms** in the frame $e$. $\omega$ or $\Gamma$ — the $n \times n$ matrix of connection 1-forms. Full notation registry on [[Riemannian Geometry I — Connections and Covariant Differentiation]].

---

# Axiom Motivation

The Christoffel symbols $\Gamma^k_{ij}$ encode a connection on $TM$ in a *coordinate* frame. But not every useful frame is a coordinate frame — orthonormal frames in particular are typically not coordinate frames (their Lie brackets are usually nonzero, so they cannot all be expressed as $\partial/\partial x^i$ for any chart $x$). For computations in Riemannian geometry, the orthonormal frame is dramatically more efficient than the coordinate frame, because metric-compatibility takes the very clean form $\omega^a{}_b + \omega^b{}_a = 0$ (antisymmetry of the matrix of connection 1-forms).

The motivation for connection 1-forms is therefore: **generalise the Christoffel symbols to an arbitrary frame, packaging the data in a way that makes the computation in any frame uniform**. Given an arbitrary local frame $e = (e_1, \ldots, e_n)$, the connection is determined by its action on the frame:
$$
\nabla_X e_b = (\text{some vector field, depending linearly on } X) = \omega^a{}_b(X)\,e_a
$$
where $\omega^a{}_b$ are the $n^2$ 1-forms expressing this dependence. Concretely $\omega^a{}_b \in \Omega^1(U)$, with $\omega^a{}_b(X)$ a smooth function for each vector field $X$. The matrix $\omega = (\omega^a{}_b)$ is the **connection matrix** in the frame $e$.

For a coordinate frame $e_i = \partial_i$, $\omega^k{}_j(\partial_i) = \Gamma^k_{ij}$ and $\omega^k{}_j = \Gamma^k_{ij}\,dx^i$ — the Christoffel symbols are just the components of the connection 1-forms in the coordinate frame, organised by the second index. In a general frame, the $n^2$ functions $\omega^a_{cb}$ defined by $\nabla_{e_c}e_b = \omega^a_{cb}e_a$ play the role of "Christoffel symbols in the frame", but they are *not* in general the components of any tensor — they are subject to the gauge-transformation law $\omega' = g^{-1}\omega g + g^{-1}dg$ under change of frame (see [[Thm - Gauge Transformation Law for Connection 1-Forms]]).

**Why repackage Christoffel data as 1-forms?** Because the resulting formalism — **Cartan's structural equations** — makes computations dramatically cleaner. In the 1-form language:
- The first structural equation $d\sigma^a + \omega^a{}_b \wedge \sigma^b = \tau^a$ encodes both the connection and the torsion, and for a torsion-free connection it gives a direct way to *compute* $\omega^a{}_b$ from $\sigma^a$ alone (in conjunction with metric-compatibility).
- The second structural equation $\Omega^a{}_b = d\omega^a{}_b + \omega^a{}_c \wedge \omega^c{}_b$ encodes the curvature 2-forms (see [[Def - Curvature 2-Forms (Cartan)]]), and gives the most efficient practical algorithm for computing the Riemann tensor.
- The gauge-transformation law $\omega' = g^{-1}\omega g + g^{-1}dg$ has the familiar form from gauge theory, making the relationship to electromagnetism and Yang-Mills theory transparent.

**Why does the orthonormal frame give antisymmetric connection 1-forms?** Suppose $(e_a)$ is an orthonormal frame: $g(e_a, e_b) = \delta_{ab}$ (Riemannian case). Apply metric-compatibility $X g(e_a, e_b) = g(\nabla_X e_a, e_b) + g(e_a, \nabla_X e_b)$ with $X = e_c$. The left side is $e_c(\delta_{ab}) = 0$ (constant). The right side is $g(\omega^d{}_a(e_c)e_d, e_b) + g(e_a, \omega^d{}_b(e_c)e_d) = \omega^b{}_a(e_c) + \omega^a{}_b(e_c)$ (using orthonormality to identify $g(e_d, e_b) = \delta_{db}$). So $\omega^b{}_a + \omega^a{}_b = 0$, i.e., the connection 1-form matrix is antisymmetric. This is a deep simplification: the $n^2$ entries reduce to $n(n-1)/2$ independent ones, matching the [[Def - Dimension|dimension]] of $\mathfrak{o}(n)$. In Lorentzian signature with the orthonormal frame having $g(e_a, e_b) = \eta_{ab}$, the antisymmetry is with respect to $\eta$: $\eta_{bc}\omega^c{}_a + \eta_{ac}\omega^c{}_b = 0$, equivalently $\omega^b{}_a + \omega^a{}_b = 0$ after raising/lowering with $\eta$.

**What is the conceptual content of $\omega^a{}_b$?** A connection 1-form $\omega^a{}_b(X)$ tells you "the rate of rotation of $e_b$ towards $e_a$ as you move in the direction of $X$". In an orthonormal frame, the rotation is genuinely a rotation (antisymmetric matrix in $\mathfrak{o}(n)$), so $\omega(X)$ is an infinitesimal rotation that captures how the frame turns as you move. The frame is *parallel* if all $\omega^a{}_b = 0$ — meaning the frame stays "constant" in the connection's sense as you move. Such a frame exists locally only if the connection is flat; the obstruction to flatness is precisely the curvature 2-form $\Omega^a{}_b$.

---

# The Definition

Let $(M, \nabla)$ be a smooth manifold with an affine connection on $TM$ (or, more generally, a smooth vector bundle $E \to M$ with connection $\nabla$). Let $e = (e_1, \ldots, e_n)$ be a smooth local frame of $TM$ (or sections of $E$) over an open set $U \subseteq M$. The **connection 1-forms** of $\nabla$ in the frame $e$ are the $n^2$ smooth 1-forms $\omega^a{}_b \in \Omega^1(U)$ defined by
$$
\nabla e_b = e_a \otimes \omega^a{}_b, \qquad \text{equivalently} \qquad \nabla_X e_b = \omega^a{}_b(X)\,e_a
$$
for every vector field $X$ on $U$. The collection $\omega = (\omega^a{}_b)$ is a matrix of 1-forms, the **connection matrix**.

Writing $\omega^a{}_b = \omega^a_{cb}\,\sigma^c$ in the dual coframe gives $\nabla_{e_c}e_b = \omega^a_{cb}\,e_a$, i.e., the $n^3$ functions $\omega^a_{cb}$ are the **components of the connection in the frame**. When $e$ is a coordinate frame ($e_i = \partial_i$, $\sigma^i = dx^i$), these reduce to the [[Def - Christoffel Symbols|Christoffel symbols]] with a relabelling of indices: $\omega^k_{ij} = \Gamma^k_{ij}$, $\omega^k{}_j = \Gamma^k_{ij}\,dx^i$.

**Action on a general section.** For $s = s^b\,e_b \in \Gamma(E)$,
$$
\nabla_X s = \bigl[X(s^a) + \omega^a{}_b(X)\,s^b\bigr]\,e_a, \qquad \nabla s = \bigl(ds^a + \omega^a{}_b\,s^b\bigr) \otimes e_a.
$$
In matrix form with $s$ regarded as a column vector $(s^1, \ldots, s^n)^T$: $\nabla s = ds + \omega s$ (the matrix product of the connection matrix with the column $s$, added to the column $ds$ of exterior derivatives).

**Orthonormal frame.** When $(e_a)$ is an orthonormal frame for a Riemannian metric $g$ (so $g(e_a, e_b) = \delta_{ab}$) and $\nabla$ is metric-compatible, the connection 1-forms satisfy the **antisymmetry condition**
$$
\omega^a{}_b + \omega^b{}_a = 0,
$$
i.e., the connection matrix is antisymmetric, $\omega \in \Omega^1(U) \otimes \mathfrak{o}(n)$. (In Lorentzian signature with $g(e_a, e_b) = \eta_{ab}$, the analogous condition is $\eta_{ac}\omega^c{}_b + \eta_{bc}\omega^c{}_a = 0$, equivalently $\omega$ takes values in $\mathfrak{o}(p, q)$.)

**Gauge transformation.** Under a change of frame $e' = e\,g$ where $g : U \to \mathrm{GL}(n, \mathbb{R})$ is a smooth matrix-valued function, the connection matrix transforms as
$$
\omega' = g^{-1}\omega\,g + g^{-1}\,dg.
$$
See [[Thm - Gauge Transformation Law for Connection 1-Forms]] for the proof and discussion. This non-tensorial behaviour is the marker of "$\omega$ is a connection, not a tensor".

---

# Relate to Other Fields / Compression

The compression: **the connection 1-forms $\omega^a{}_b$ are the data of the connection $\nabla$ in a local frame, packaged as a matrix-valued 1-form**. They generalise the Christoffel symbols to arbitrary frames and are the central object in Cartan's moving-frame formalism.

In **physics / gauge theory**, the connection 1-form is the **gauge potential**. For a $U(1)$-bundle (electromagnetism), $\omega = iA$ where $A$ is the real electromagnetic vector potential and $A_\mu$ are its components in a coordinate frame. The gauge-transformation law $\omega' = g^{-1}\omega g + g^{-1}dg$ becomes, for $g = e^{i\chi}$, $A' = A + d\chi$ — the standard $U(1)$ gauge transformation. For a non-abelian gauge group $G$ (Yang-Mills theory), $\omega$ is $\mathfrak{g}$-valued and the same formula gives the non-abelian gauge transformation $A' = g^{-1}Ag + g^{-1}dg$. The curvature 2-form $\Omega = d\omega + \omega \wedge \omega$ is the **field strength** $F = dA + A \wedge A$, and the inhomogeneous Yang-Mills equation $d\star F + [A, \star F] = 0$ is the natural generalisation of Maxwell's $d\star F = 0$. Once one absorbs that "connection 1-form = gauge potential", the entire differential-geometric formalism transfers verbatim to gauge theory — see [[Gauge Theory III — Connections in Principal and Associated Bundles]] for the full development.

**True name:** The "true name" of the connection 1-form is **the matrix-valued 1-form that, applied to a tangent vector, gives the infinitesimal rotation of the frame as you move in that direction**. In an orthonormal frame this rotation is an honest infinitesimal rotation (antisymmetric matrix in $\mathfrak{o}(n)$); in a general frame it is an infinitesimal linear transformation in $\mathfrak{gl}(n)$. The connection 1-form *is* the infinitesimal rotation rate of the frame field with respect to parallel transport. The "true name" makes immediate why $\omega$ is not a tensor: rotating a frame depends on the frame, not just on the underlying geometry.

---

# Examples / Corollaries

**Example: connection 1-forms of the flat connection on $\mathbb{R}^n$ in Cartesian coordinates.** All $\Gamma^k_{ij} = 0$, so $\omega^k{}_j = 0$. The connection matrix is the zero matrix.

**Example: connection 1-forms of the flat connection on $\mathbb{R}^2$ in polar coordinates.** Using the coordinate frame $(e_r, e_\theta) = (\partial_r, \partial_\theta)$, $\Gamma^r_{\theta\theta} = -r$ and $\Gamma^\theta_{r\theta} = 1/r$, giving $\omega^r{}_\theta = -r\,d\theta$ (from $\nabla_{\partial_\theta}\partial_\theta = -r\partial_r$, contributing $\omega^r{}_\theta(\partial_\theta) = -r$) and $\omega^\theta{}_r = \omega^\theta{}_\theta = \tfrac{1}{r}d\theta$ ... actually let me redo carefully: $\nabla_{\partial_r}\partial_r = 0$, $\nabla_{\partial_r}\partial_\theta = (1/r)\partial_\theta$, $\nabla_{\partial_\theta}\partial_r = (1/r)\partial_\theta$, $\nabla_{\partial_\theta}\partial_\theta = -r\partial_r$. So $\omega^r{}_r = 0$, $\omega^\theta{}_r(\partial_r) = 0, \omega^\theta{}_r(\partial_\theta) = 1/r$, so $\omega^\theta{}_r = (1/r)d\theta$; $\omega^r{}_\theta(\partial_\theta) = -r$, so $\omega^r{}_\theta = -r\,d\theta$; $\omega^\theta{}_\theta(\partial_r) = 1/r$, so $\omega^\theta{}_\theta = (1/r)dr$. The connection matrix in the coordinate frame is non-antisymmetric (because the coordinate frame is not orthonormal). The connection is flat but $\omega \neq 0$ in this frame — illustrating that $\omega = 0$ is a *frame*-dependent statement.

**Example: connection 1-forms of the flat connection on $\mathbb{R}^2$ in the orthonormal frame.** Take the orthonormal frame $(e_1, e_2) = (\partial_r, (1/r)\partial_\theta)$ dual to $(\sigma^1, \sigma^2) = (dr, r\,d\theta)$. Then $d\sigma^1 = 0$, $d\sigma^2 = dr \wedge d\theta = (1/r)\sigma^1 \wedge \sigma^2$. Cartan's first structural equation $d\sigma^a + \omega^a{}_b \wedge \sigma^b = 0$ (torsion-free) and antisymmetry $\omega^1{}_2 = -\omega^2{}_1$ give $\omega^1{}_2 = -d\theta$ (so $\omega^2{}_1 = d\theta$). The curvature is $\Omega^1{}_2 = d\omega^1{}_2 + \omega^1{}_c \wedge \omega^c{}_2 = 0$ — confirming flat. In the orthonormal frame the antisymmetry is manifest.

**Example: connection 1-forms of the round 2-sphere.** Orthonormal coframe $(\sigma^1, \sigma^2) = (d\theta, \sin\theta\,d\varphi)$. Then $d\sigma^1 = 0$, $d\sigma^2 = \cos\theta\,d\theta \wedge d\varphi = (\cos\theta/\sin\theta)\,\sigma^1 \wedge \sigma^2 = \cot\theta\,\sigma^1 \wedge \sigma^2$. The first structural equation with antisymmetry gives $\omega^1{}_2 = -\cos\theta\,d\varphi$, $\omega^2{}_1 = \cos\theta\,d\varphi$. See [[Ex - Cartan Structural Equations on S^2]].

**Example: the electromagnetic connection on a $U(1)$-bundle.** Take the trivial complex line bundle $E = M \times \mathbb{C}$ with the single frame section $e_1 = 1$. The connection 1-form is the scalar 1-form $\omega^1{}_1 = i A$ where $A$ is the real electromagnetic vector potential. The covariant derivative of a complex-valued wavefunction $\psi$ is $\nabla_X \psi = X(\psi) + i A(X)\psi$, i.e., $D_\mu \psi = (\partial_\mu + i A_\mu)\psi$ — the gauge-covariant derivative of quantum mechanics. See [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection]].

**Non-example: $\omega^a{}_b$ as a tensor.** The connection 1-form has one upper and one lower index (a $(1, 1)$-tensor structure) plus the 1-form value, so it looks like a $(1, 2)$-tensor. It is not: the transformation law $\omega' = g^{-1}\omega g + g^{-1}dg$ has the inhomogeneous $g^{-1}dg$ term that prevents tensoriality. The curvature 2-form $\Omega = d\omega + \omega \wedge \omega$ *is* a tensor (transforms as $\Omega' = g^{-1}\Omega g$, no inhomogeneous term), and so is the torsion 2-form $\tau$, but the connection 1-form itself is not.

**Corollary (the connection 1-form determines parallel transport).** Parallel transport along a curve $\gamma$ is the solution of the linear matrix ODE $\dot V + \omega(\dot\gamma)V = 0$ in the frame $e$, where $V$ is the column of components of the parallel section. The solution is the path-ordered exponential $V(t) = \mathcal{T}\exp\bigl(-\int_0^t \omega(\dot\gamma)\,dt'\bigr) V(0)$. So the connection 1-forms are *all* you need to compute parallel transport — they are the local data of the connection.

**Corollary (the antisymmetry condition in an orthonormal frame is exactly metric-compatibility).** This is the cleanest formulation of [[Def - Metric-Compatible Connection|metric-compatibility]] in terms of frames: in an orthonormal frame the connection is metric-compatible if and only if the connection matrix is antisymmetric (in $\mathfrak{o}(n)$ or $\mathfrak{o}(p, q)$, depending on signature). This is what makes orthonormal frames the computational tool of choice.

**Calibration check.** If you can perform the following three computations, you have understood connection 1-forms. (i) Compute the connection 1-forms of the Euclidean metric on $\mathbb{R}^2$ in polar coordinates, in (a) the coordinate frame and (b) the orthonormal frame; verify they are related by the gauge-transformation law for the change-of-frame matrix $g = \mathrm{diag}(1, 1/r)$. (ii) Compute the connection 1-forms of the round 2-sphere in the orthonormal coframe $(d\theta, \sin\theta\,d\varphi)$ by Cartan's first structural equation, and verify they are antisymmetric. (iii) Show that for an orthonormal frame $(e_a)$ on a Riemannian manifold, the matrix $\omega^a{}_b$ is antisymmetric (in the entries, not just transposed) directly from metric-compatibility.

---

# Unlocked by This

> [!tip] Cartan's Structural Equations and the Riemann Tensor *(from Riemannian Geometry)*
> The connection 1-forms enter Cartan's two structural equations:
> 1. **First structural equation:** $d\sigma^a + \omega^a{}_b \wedge \sigma^b = \tau^a$, encoding the torsion 2-forms. For torsion-free connections this is the equation that *determines* $\omega$ from $\sigma$ together with antisymmetry. ([[Thm - Cartan's First Structural Equation]])
> 2. **Second structural equation:** $\Omega^a{}_b = d\omega^a{}_b + \omega^a{}_c \wedge \omega^c{}_b$, defining the curvature 2-forms in terms of the connection 1-forms. ([[Thm - Cartan's Second Structural Equation]], [[Def - Curvature 2-Forms (Cartan)]])
>
> Together these provide the most efficient practical method for computing the Riemann curvature tensor of a Riemannian metric, used in essentially every general-relativity textbook.

> [!tip] Yang-Mills Gauge Potentials *(from Gauge Theory)*
> A connection 1-form on a principal $G$-bundle is a $\mathfrak{g}$-valued 1-form on the total space (or locally on the base, given a trivialisation). This is the **Yang-Mills gauge potential** $A$, and the curvature 2-form $F = dA + A \wedge A$ is the **field strength**. The transformation law $A' = g^{-1}Ag + g^{-1}dg$ is the **non-abelian gauge transformation**. Electromagnetism is the abelian case $G = U(1)$ where $A \wedge A = 0$, giving the linear field strength $F = dA$. Yang-Mills theory and the strong/electroweak interactions are the non-abelian cases. See [[Gauge Theory III — Connections in Principal and Associated Bundles]] and [[Gauge Theory V — Hodge Theory, Maxwell, Yang–Mills, and Instantons]].

> [!tip] The Spin Connection *(from Spinors and the Dirac Equation)*
> On a spin manifold (a Riemannian or Lorentzian manifold with a spin structure), the Levi-Civita connection 1-forms in an orthonormal frame — which are antisymmetric and hence $\mathfrak{o}(n)$-valued — lift to a connection on the spinor bundle via the homomorphism $\mathrm{Spin}(n) \to \mathrm{SO}(n)$. This is the **spin connection** $\omega^{ab}$, the $\mathfrak{spin}(n)$-valued 1-form that lets you differentiate spinors covariantly. The curved-spacetime **Dirac operator** $\not D = \gamma^a e_a^\mu(\partial_\mu + \tfrac{1}{4}\omega^{ab}_\mu \gamma_{ab})$ uses the spin connection essentially. See [[Spinors and the Dirac Equation]].
