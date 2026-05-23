---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Connection 1-Forms (Cartan)"
  - "Def - Affine Connection on a Vector Bundle"
  - "Def - The Wedge Product on a Manifold"
  - "Def - Exterior Derivative on a Manifold"
tags: [geometry, riemannian-geometry, connections, cartan-formalism, curvature]
---

# Notation

$(M, \nabla)$ — smooth manifold with affine connection on $TM$ (or vector bundle $E \to M$). $e = (e_a)$ — a local frame; $\sigma^a$ — dual coframe. $\omega^a{}_b$ — connection 1-forms in the frame ([[Def - Connection 1-Forms (Cartan)]]). $\Omega^a{}_b$ or $\theta^a{}_b$ — **curvature 2-forms**. $\Omega$ or $\theta$ — matrix of curvature 2-forms. $R(X, Y)Z$ — Riemann curvature tensor: $R(X, Y)Z := \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X, Y]}Z$. Full notation registry on [[Riemannian Geometry I — Connections and Covariant Differentiation]].

---

# Axiom Motivation

The connection 1-forms $\omega^a{}_b$ encode the connection $\nabla$ locally in a frame, but they are *not* a tensor — they transform with an inhomogeneous gauge correction $\omega' = g^{-1}\omega g + g^{-1}dg$, so $\omega$ is gauge-dependent and unphysical in the same sense that the electromagnetic vector potential is gauge-dependent. The **curvature 2-forms** $\Omega^a{}_b$ are the geometric content of the connection — the gauge-invariant data that survives any change of frame.

The motivation for the specific formula $\Omega = d\omega + \omega \wedge \omega$ is the following. We have the covariant derivative $\nabla$ acting on vector fields by $\nabla v = e\,(dv + \omega v)$ in matrix-column notation (with $v$ the column of components in the frame). Apply $\nabla$ twice:
$$
\nabla\nabla v = \nabla\bigl(e\,(dv + \omega v)\bigr) = e\,\bigl[d(dv + \omega v) + \omega \wedge (dv + \omega v)\bigr],
$$
using the Leibniz rule for $\nabla$. Expanding: $d(dv) = 0$ (by $d^2 = 0$), and $d(\omega v) = d\omega \cdot v - \omega \wedge dv$ (Leibniz for $d$ with the sign convention for matrix forms), and $\omega \wedge dv = \omega \wedge dv$, and $\omega \wedge \omega v = (\omega \wedge \omega) v$. The $\omega \wedge dv$ terms cancel, leaving
$$
\nabla\nabla v = e\,\bigl[d\omega + \omega \wedge \omega\bigr] v = e\,\Omega\,v
$$
where $\Omega = d\omega + \omega \wedge \omega$ is the curvature matrix. The remarkable feature: **the result depends only on $v$, not on $dv$**. So $\nabla\nabla v = \Omega v$ is an algebraic (not differential) operation on $v$ — meaning $\nabla\nabla$ is a *tensor* operation, $\nabla\nabla \in \Gamma(\Lambda^2 T^*M \otimes \mathrm{End}\,TM)$. The curvature 2-form $\Omega$ measures this "second-order non-commutativity" of $\nabla$.

Equivalently, the Riemann curvature tensor $R(X, Y)Z$ defined by $R(X, Y)Z = \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X, Y]}Z$ has components in the frame given by $\Omega^a{}_b(X, Y) =$ the $(a, b)$-component of $\nabla\nabla$ applied to $e_b$:
$$
\Omega^a{}_b(X, Y) = g(R(X, Y)e_b, \sigma^a) = R^a{}_{bcd}\,\sigma^c(X)\sigma^d(Y) \cdot (1/2)
$$
or rather: $\Omega^a{}_b = \tfrac{1}{2}R^a{}_{bcd}\,\sigma^c \wedge \sigma^d$, which is the precise component formula. The curvature 2-forms are an organisation of the Riemann tensor as a matrix of 2-forms, indexed by frame slots $(a, b)$.

**Why does $\Omega$ transform homogeneously, $\Omega' = g^{-1}\Omega g$?** Compute $\Omega'$ in the changed frame from the curvature formula and the gauge-transformation law for $\omega$:
$$
\Omega' = d\omega' + \omega' \wedge \omega' = d(g^{-1}\omega g + g^{-1}dg) + (g^{-1}\omega g + g^{-1}dg) \wedge (g^{-1}\omega g + g^{-1}dg).
$$
Using $d(g^{-1}) = -g^{-1}(dg)g^{-1}$ and expanding, the inhomogeneous $g^{-1}dg$ pieces cancel out exactly, leaving $\Omega' = g^{-1}\Omega g$. This is a remarkable algebraic identity — the inhomogeneous parts in $d\omega'$ and in $\omega' \wedge \omega'$ are precisely tuned to cancel. So curvature is a genuine *tensor*, transforming homogeneously under frame change, while the connection is not.

**The geometric interpretation: curvature is the obstruction to path-independence of parallel transport.** Take a small parallelogram at $p$ with sides $\varepsilon X, \varepsilon Y$, and parallel-transport a vector $v$ around it. The result differs from $v$ to leading order by $-\varepsilon^2 R(X, Y)v$. Equivalently, taking two infinitesimal covariant derivatives in opposite orders gives $[\nabla_X, \nabla_Y]v - \nabla_{[X, Y]}v = R(X, Y)v$ — the failure of $\nabla$ to commute on functions, applied to the vector $v$. The curvature 2-form $\Omega^a{}_b$ encodes this rotation: $\Omega^a{}_b(X, Y)$ is the rate at which a vector in the $e_b$ direction picks up a component in the $e_a$ direction under parallel transport around the infinitesimal parallelogram spanned by $X, Y$.

**The Cartan formula $\Omega = d\omega + \omega \wedge \omega$ is geometric, not algebraic.** The "$d\omega$" part is the abelian curvature — for a $U(1)$ gauge theory or any connection in which $\omega$ is scalar-valued or commutes with itself, $\omega \wedge \omega = 0$ and only $d\omega$ survives. This is the classical case of Maxwell electromagnetism, where $F = dA$. The "$\omega \wedge \omega$" part is the non-abelian self-interaction, characteristic of Yang-Mills theory — the gauge field is its own source, and the resulting non-linearity is the geometric origin of the non-linearity of Yang-Mills equations and of the rich vacuum structure ([[Def - Instanton|instantons]], monopoles, vortices). In the Riemannian-geometry case the $\omega \wedge \omega$ term is always present because $\omega$ takes values in $\mathfrak{o}(n)$, which is non-abelian for $n \geq 3$.

---

# The Definition

Let $E \to M$ be a smooth vector bundle of rank $n$ with connection $\nabla$, and let $e = (e_1, \ldots, e_n)$ be a local frame with [[Def - Connection 1-Forms (Cartan)|connection 1-forms]] $\omega^a{}_b$ in the frame, organised into the matrix $\omega = (\omega^a{}_b)$. The **curvature 2-forms** of $\nabla$ in the frame $e$ are the entries of the $n \times n$ matrix
$$
\Omega := d\omega + \omega \wedge \omega,
$$
i.e., the 2-forms
$$
\Omega^a{}_b := d\omega^a{}_b + \omega^a{}_c \wedge \omega^c{}_b.
$$
This is **Cartan's second structural equation** (see [[Thm - Cartan's Second Structural Equation]]).

**Equivalent formulation via second covariant derivatives.** $\Omega$ is the matrix representation, in the frame $e$, of the second covariant differential operator $\nabla\nabla$: for any section $s = s^b e_b$,
$$
\nabla\nabla s = e\,\Omega\,s, \qquad \text{or in components} \qquad (\nabla\nabla s)^a = \Omega^a{}_b \cdot s^b.
$$
This says $\nabla\nabla$ is a *tensor* operation (no derivatives of $s$ appear on the right), and the tensor is the **curvature endomorphism** valued in 2-forms.

**Relation to the Riemann curvature tensor.** When $E = TM$, the curvature 2-forms have components
$$
\Omega^a{}_b = \tfrac{1}{2}\,R^a{}_{bcd}\,\sigma^c \wedge \sigma^d,
$$
where $R^a{}_{bcd}$ are the components of the **Riemann curvature tensor** $R(X, Y)Z = \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X, Y]}Z$ in the frame $e$ with dual coframe $\sigma^a$: explicitly $R(e_c, e_d)e_b = R^a{}_{bcd}\,e_a$.

**Gauge transformation.** Under a change of frame $e' = e\,g$ (with $g : U \to \mathrm{GL}(n, \mathbb{R})$), the curvature 2-forms transform **homogeneously**:
$$
\Omega' = g^{-1}\,\Omega\,g.
$$
The inhomogeneous terms from the connection's transformation $\omega' = g^{-1}\omega g + g^{-1}dg$ cancel exactly in the curvature, leaving the simple matrix-conjugation. This is what makes $\Omega$ a tensor (specifically, an $\mathrm{End}(E)$-valued 2-form, a section of $\Lambda^2 T^*M \otimes \mathrm{End}(E)$).

**In an orthonormal frame.** When $(e_a)$ is orthonormal for a Riemannian metric, the connection 1-forms are antisymmetric ($\omega^a{}_b + \omega^b{}_a = 0$), and consequently the curvature 2-forms are also antisymmetric: $\Omega^a{}_b + \Omega^b{}_a = 0$. This is the **first symmetry** of the Riemann tensor: $R_{abcd} = -R_{bacd}$ (lowering the upper index).

**Bianchi identities.** The curvature 2-forms satisfy two identities derived by exterior-differentiating the structural equations:
- **First (algebraic) Bianchi identity:** For a torsion-free connection, $\Omega^a{}_b \wedge \sigma^b = 0$, equivalently $R^a{}_{bcd} + R^a{}_{cdb} + R^a{}_{dbc} = 0$. (Without torsion-freeness this has correction terms involving $\tau$.)
- **Second (differential) Bianchi identity:** $d\Omega^a{}_b + \omega^a{}_c \wedge \Omega^c{}_b - \Omega^a{}_c \wedge \omega^c{}_b = 0$, equivalently $\nabla_e R_{abcd} + \nabla_c R_{abde} + \nabla_d R_{abec} = 0$ (the cyclic sum vanishes). This is the connection-theoretic analogue of the Yang-Mills homogeneous equation $dF + A \wedge F - F \wedge A = 0$.

---

# Relate to Other Fields / Compression

The compression: **the curvature 2-forms are the matrix-valued 2-form $\Omega = d\omega + \omega \wedge \omega$ that captures the geometric content of the connection — the gauge-invariant data that survives any change of frame.** They are the most efficient computational form of the Riemann curvature tensor in practice, and they are what gets integrated in characteristic-class constructions.

In **physics / gauge theory**, the curvature 2-form is the **Yang-Mills field strength** $F = dA + A \wedge A$. For electromagnetism ($G = U(1)$, abelian), $A \wedge A = 0$ and $F = dA$ — the field strength is the exterior derivative of the gauge potential. Its components $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ are the electric and magnetic field components. For a non-abelian gauge theory, $F = dA + A \wedge A$ has the additional non-linear self-interaction term, and the equation $F^a_{\mu\nu} = \partial_\mu A^a_\nu - \partial_\nu A^a_\mu + f^a_{bc}A^b_\mu A^c_\nu$ in components shows the structure constants of the gauge group entering. The **second Bianchi identity** $\nabla F = 0$ is the homogeneous equation (the analogue of $dF = 0$ in Maxwell theory), and the **Yang-Mills equation** $\nabla\star F = 0$ (or $\nabla\star F = J$ with source) is the inhomogeneous equation. The full theory is the content of [[Gauge Theory IV — Yang–Mills Fields and Instantons]].

In **algebraic topology**, the curvature 2-form $\Omega$ feeds into **Chern-Weil theory**: invariant polynomials of $\Omega$ (trace, determinant, Pfaffian) give closed differential forms whose de Rham cohomology classes are *independent of the connection* — they are topological invariants of the bundle called **characteristic classes**. The first Chern class is $c_1(E) = \tfrac{i}{2\pi}\mathrm{tr}\,\Omega$, the second is $c_2(E) = \tfrac{1}{8\pi^2}(\mathrm{tr}\,\Omega \wedge \Omega - \mathrm{tr}\,\Omega \wedge \mathrm{tr}\,\Omega)$. The integrals $\int_M c_k(E)$ are **Chern numbers** — integer-valued topological invariants of the bundle. The **Gauss-Bonnet theorem** on a closed orientable surface, $\int_M K\,dA = 2\pi\chi(M)$, is the simplest Chern-Weil identity, expressing the Euler characteristic as the integral of the trace of the curvature 2-form (Gaussian curvature) of the Levi-Civita connection in an orthonormal frame. See [[Algebraic Topology III — Higher Homotopy and Chern Forms]].

**True name:** The "true name" of the curvature 2-form is **the matrix-valued 2-form that encodes the failure of parallel transport to be path-independent**. Concretely $\Omega(X, Y)$ at $p$ is the infinitesimal rotation induced by parallel-transporting a vector around the infinitesimal parallelogram with sides $X, Y$ at $p$. The Cartan formula $\Omega = d\omega + \omega \wedge \omega$ is the algebraic expression of this geometric content, and the tensorial transformation $\Omega' = g^{-1}\Omega g$ is the diagnostic that this content is gauge-invariant.

---

# Examples / Corollaries

**Example: zero curvature of the flat connection on $\mathbb{R}^n$.** In Cartesian coordinates $\omega = 0$, so $\Omega = d\omega + \omega \wedge \omega = 0$ trivially. In any other coordinate system (e.g., polar on $\mathbb{R}^2$) $\omega \neq 0$ but the connection is still flat, so $\Omega$ must be zero — and indeed by direct computation $\Omega = d\omega + \omega \wedge \omega = 0$. The cancellation between $d\omega$ and $\omega \wedge \omega$ in non-Cartesian frames is the explicit calculation that confirms $\Omega$ is a tensor (zero in Cartesian frame = zero in any frame). See [[Ex - The Levi-Civita Connection of Polar Coordinates]].

**Example: the curvature of the round 2-sphere.** Orthonormal coframe $\sigma^1 = d\theta$, $\sigma^2 = \sin\theta\,d\varphi$, with connection 1-form $\omega^1{}_2 = -\cos\theta\,d\varphi$. Then $d\omega^1{}_2 = \sin\theta\,d\theta \wedge d\varphi = \sigma^1 \wedge \sigma^2$, and $\omega^1{}_c \wedge \omega^c{}_2 = \omega^1{}_2 \wedge \omega^2{}_2 + \omega^1{}_1 \wedge \omega^1{}_2 = 0$ (since $\omega^1{}_1 = \omega^2{}_2 = 0$ by antisymmetry). So $\Omega^1{}_2 = \sigma^1 \wedge \sigma^2$. Comparing to $\Omega^1{}_2 = \tfrac{1}{2}R^1{}_{2cd}\sigma^c \wedge \sigma^d$ gives $R^1{}_{212} = 1$ — the sectional curvature is $1$, as expected for the unit sphere. See [[Ex - Cartan Structural Equations on S^2]].

**Example: the curvature of a Schwarzschild metric.** For the Schwarzschild metric $g = -f(r)dt^2 + f(r)^{-1}dr^2 + r^2(d\theta^2 + \sin^2\theta\,d\varphi^2)$ with $f(r) = 1 - 2M/r$, the orthonormal coframe is $\sigma^0 = f^{1/2}dt$, $\sigma^1 = f^{-1/2}dr$, $\sigma^2 = r\,d\theta$, $\sigma^3 = r\sin\theta\,d\varphi$. The connection 1-forms are computed from Cartan's first equation, and the curvature 2-forms from the second equation give explicit components $R^a{}_{bcd}$. This is the standard general-relativity calculation; see [[Ex - Computing Curvature 2-Forms in an Orthonormal Frame]] for the worked computation, which gives sectional curvatures $\pm M/r^3$ in the various 2-planes.

**Example: the curvature 2-form of the electromagnetic connection.** On a $U(1)$-bundle with connection 1-form $\omega = iA$ for real 1-form $A$, the curvature 2-form is $\Omega = d\omega + \omega \wedge \omega = i\,dA$ (since $\omega \wedge \omega = (iA) \wedge (iA) = -A \wedge A = 0$ for scalar-valued 1-forms). So $\Omega = i\,dA$, and the curvature 2-form is essentially the electromagnetic field-strength 2-form $F = dA$, with components $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$. The Bianchi identity $d\Omega = 0$ becomes $d(dA) = 0$, automatic.

**Non-example: trying to apply $\Omega = d\omega + \omega \wedge \omega$ in the wrong sign convention.** Some texts use $\Omega = d\omega - \omega \wedge \omega$ (with a minus sign), which corresponds to a different convention for the structure equations and yields the same Riemann tensor with a sign flip in some places. The convention $\Omega = d\omega + \omega \wedge \omega$ used here matches Frankel and Lee's *[[Def - Riemannian Manifold|Riemannian Manifolds]]*. The opposite sign is also seen — physicists writing $F = dA - A \wedge A$ in some Yang-Mills texts. The lesson: always check the sign convention; the structural content is the same, but explicit formulas change sign in certain identities.

**Corollary (zero curvature ⟺ locally flat).** $\Omega \equiv 0$ on a connected open set if and only if there exists a parallel local frame on that set — i.e., a frame $(e_a)$ with $\omega^a{}_b = 0$ in that frame. Equivalently, $\Omega = 0$ iff the metric is locally Euclidean (for the Levi-Civita connection of a Riemannian metric). This is the **Riemann theorem** on local-flatness: zero Riemann tensor ⟺ locally Euclidean metric.

**Corollary (curvature 2-form is gauge-invariant up to conjugation).** Under change of frame $e' = e\,g$, $\Omega' = g^{-1}\Omega g$. The eigenvalues of $\Omega$ (as a matrix-valued 2-form, evaluated on any pair $(X, Y)$) are invariant under conjugation, so they are coordinate-independent geometric invariants. The trace, determinant, and other invariant polynomials of $\Omega$ are gauge-invariant — these are the inputs to Chern-Weil characteristic classes.

**Corollary (Bianchi identity from the structure equation).** Take the exterior derivative of Cartan's second structural equation: $d\Omega = d(d\omega + \omega \wedge \omega) = d(\omega \wedge \omega) = d\omega \wedge \omega - \omega \wedge d\omega = (\Omega - \omega \wedge \omega)\wedge \omega - \omega \wedge (\Omega - \omega \wedge \omega) = \Omega \wedge \omega - \omega \wedge \Omega$ (the $\omega \wedge \omega$ pieces cancel). So $d\Omega + \omega \wedge \Omega - \Omega \wedge \omega = 0$, which is the **second Bianchi identity** in component form. In gauge-theory language this is $\nabla F = 0$, automatic from the structural definition.

**Calibration check.** If you can perform the following three computations, you have understood curvature 2-forms. (i) Verify by direct computation that the curvature 2-form of the Euclidean metric on $\mathbb{R}^2$ in polar coordinates is zero, with the cancellation between $d\omega$ and $\omega \wedge \omega$ tracked explicitly. (ii) Compute the single nonzero curvature 2-form on the round 2-sphere via Cartan's second structural equation and verify the Gaussian curvature is $1$. (iii) Derive the second Bianchi identity from $d^2\omega = 0$ applied to the structural equation, and identify its analogue $dF + [A, F] = 0$ in Yang-Mills theory.

---

# Unlocked by This

> [!tip] The Riemann Curvature Tensor and All of Riemannian Geometry *(from Riemannian Geometry)*
> The curvature 2-forms organise the **Riemann curvature tensor** $R^a{}_{bcd}$ via $\Omega^a{}_b = \tfrac{1}{2}R^a{}_{bcd}\sigma^c \wedge \sigma^d$. The symmetries of $R$ (antisymmetry in $(a, b)$ from frame-antisymmetry, antisymmetry in $(c, d)$ from 2-form structure, pair symmetry $R_{abcd} = R_{cdab}$ from Levi-Civita, first Bianchi identity $R^a{}_{[bcd]} = 0$) reduce the independent components to $\tfrac{n^2(n^2 - 1)}{12}$. Contractions give the **Ricci tensor** $R_{ij} = R^a{}_{iaj}$, **scalar curvature** $R = g^{ij}R_{ij}$, **sectional curvature** $K(\Pi) = R_{abcd}u^a v^b u^c v^d$ in a 2-plane spanned by orthonormal $u, v$. The curvature-to-topology theorems (Bonnet-Myers, Cartan-Hadamard, Synge, Gauss-Bonnet) sit on top of these structures. Full development in [[Riemannian Geometry III — Riemann Curvature and Topology]].

> [!tip] Chern-Weil Theory and Characteristic Classes *(from Algebraic Topology)*
> Invariant polynomials of $\Omega$ — trace, determinant, Pfaffian, and the elementary symmetric functions of eigenvalues — give closed differential forms whose cohomology classes are **independent of the connection** and are topological invariants of the bundle: **Chern classes** $c_k$ for complex bundles, **Pontryagin classes** $p_k$ for real bundles, **Euler class** $e$ for oriented bundles. The **Gauss-Bonnet theorem** $\int_M K\,dA = 2\pi\chi(M)$ for surfaces is the simplest Chern-Weil identity. The **Atiyah-Singer index theorem** generalises this to relate the analytic index of an elliptic operator to topological invariants of the underlying bundles. See [[Algebraic Topology III — Higher Homotopy and Chern Forms]] and the **Chern-Weil theory** mentioned in [[Gauge Theory IV — Yang–Mills Fields and Instantons]] for instanton charges as second Chern numbers.

> [!tip] Yang-Mills Theory and Instantons *(from Gauge Theory)*
> In Yang-Mills theory, the curvature 2-form $F = dA + A \wedge A$ of a connection $A$ on a principal $G$-bundle is the **field strength**. The **Yang-Mills action** is $S_{\mathrm{YM}} = \tfrac{1}{2}\int\mathrm{tr}(F \wedge \star F)$ and the Yang-Mills equations are $d_A\star F = 0$. **Self-dual** (or anti-self-dual) configurations $F = \pm \star F$ on $\mathbb{R}^4$ are automatic solutions; the **BPST instanton** is the canonical self-dual $SU(2)$ field configuration with second Chern number $\tfrac{1}{8\pi^2}\int\mathrm{tr}(F \wedge F) = 1$. The vacuum structure of Yang-Mills theory, the QCD theta-angle, and quantum tunnelling between topologically distinct vacua are all governed by these curvature configurations. See [[Gauge Theory IV — Yang–Mills Fields and Instantons]].
