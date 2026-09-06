---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Gauge-Covariant Derivative"
  - "Def - Exterior Derivative on a Manifold"
  - "Def - The Wedge Product on a Manifold"
  - "Def - The Lie Algebra of a Lie Group"
tags: [geometry, gauge-theory, mathematical-physics]
---

# Notation

$M$ is a smooth manifold, $G$ a compact Lie group with Lie algebra $\mathfrak{g}$, and $A$ a $\mathfrak{g}$-valued 1-form on $M$ (the gauge potential). In local coordinates $A = A_\mu(x)\, dx^\mu$ with each $A_\mu(x) \in \mathfrak{g}$, and in matrix form $A_\mu = A_\mu^a T^a$ with $\{T^a\}$ a basis of $\mathfrak{g}$. The geometric connection is $\omega = -iqA$, where $q$ is the coupling constant.

The bracket $[A, B]$ on $\mathfrak{g}$-valued forms is **graded**: for $A$ a $p$-form and $B$ a $q$-form, $[A, B] = A \wedge B - (-1)^{pq} B \wedge A$, where the wedge involves multiplying coefficients via the Lie bracket on $\mathfrak{g}$. In particular for two 1-forms, $[A, A]_{\mu\nu} = [A_\mu, A_\nu] - [A_\nu, A_\mu] = 2[A_\mu, A_\nu]$, so $\tfrac12[A, A] = [A_\mu, A_\nu]dx^\mu\wedge dx^\nu$ (summing without the factor $1/2$).

Index conventions and the wider gauge-theory notation are in [[Gauge Theory V — Hodge Theory, Maxwell, Yang–Mills, and Instantons]].

---

# Axiom Motivation

The Yang–Mills field strength $F$ has one defining role: **it is the curvature of the gauge connection, measuring the failure of covariant derivatives to commute**. Every property of $F$ — its homogeneous transformation law, the formula $F = dA - iqA\wedge A$, the Bianchi identity $d_A F = 0$ — follows from this single identity. The definition is what one writes down to make the identity true.

The starting question is: given a gauge-covariant derivative $D_\mu = \partial_\mu - iqA_\mu$, when do two covariant derivatives commute? For ordinary partial derivatives in flat coordinates $[\partial_\mu, \partial_\nu] = 0$, but covariant derivatives generally do not: computing,
$$[D_\mu, D_\nu]\psi = (\partial_\mu - iqA_\mu)(\partial_\nu - iqA_\nu)\psi - (\mu \leftrightarrow \nu)$$
$$= -iq(\partial_\mu A_\nu - \partial_\nu A_\mu)\psi - q^2[A_\mu, A_\nu]\psi$$
$$= -iq(\partial_\mu A_\nu - \partial_\nu A_\mu - iq[A_\mu, A_\nu])\psi$$
$$= -iq F_{\mu\nu}\psi.$$
The expression $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu - iq[A_\mu, A_\nu]$ is *forced* by demanding that $[D_\mu, D_\nu] = -iqF_{\mu\nu}$ — it is the unique object satisfying this identity. The same calculation in coordinate-free form gives $F = dA - iqA\wedge A$ as a $\mathfrak{g}$-valued 2-form.

The non-abelian term $[A_\mu, A_\nu]$ is the entire new feature of Yang–Mills compared to Maxwell. For $G = U(1)$ the Lie algebra is one-dimensional and abelian, so $[A_\mu, A_\nu] = 0$, and $F = dA$ — the field strength is the ordinary exterior derivative of the potential, and Maxwell's equations are linear. For non-abelian $G$, the commutator is non-zero, $F$ is non-linear in $A$, and the field equations acquire cubic and quartic self-interaction terms. This non-linearity is responsible for confinement in QCD, for the existence of instantons, and for the fact that Yang–Mills theory has a much richer non-perturbative structure than electromagnetism.

Why does $F$ transform homogeneously even though $A$ does not? Under a gauge transformation $A \to A' = gAg^{-1} - (i/q)(dg)g^{-1}$, a brute-force calculation shows $F' = gFg^{-1}$. Conceptually, this is because $F$ is built from the gauge-covariant *commutator* $[D_\mu, D_\nu]$, and commutators of covariant operators are themselves covariant — the inhomogeneous parts cancel between the two factors. The structural reason: $A$ is *not* a tensor (it is a connection), but $F$ *is* a tensor (it is the curvature 2-form, a $\operatorname{ad}P$-valued 2-form on $M$). Curvatures are tensors; potentials are not.

A third role for $F$ is as the *natural object for gauge-invariant integrals*: $\operatorname{tr}(F\wedge\star F)$ is a globally-defined 4-form on $M$ (the integrand of the Yang–Mills action), and $\operatorname{tr}(F\wedge F)$ is a closed 4-form representing the second Chern class. Neither integrand can be built from $A$ alone in a gauge-invariant way — the closest one gets is the Chern–Simons 3-form $\operatorname{CS}(A) = \operatorname{tr}(A\wedge dA + \tfrac{2}{3}A\wedge A\wedge A)$, which is gauge-invariant only modulo $2\pi\mathbb{Z}$, and whose exterior derivative is precisely $\operatorname{tr}(F\wedge F)$.

What if one dropped the commutator term and used $F = dA$ as the definition for non-abelian gauge theory? The resulting object would fail to transform homogeneously: $dA' = d(gAg^{-1} - (i/q)(dg)g^{-1})$ produces a residual $(dg)\wedge(dg^{-1})$ term that does not cancel. The would-be "field strength" would not be gauge-covariant, $\operatorname{tr}((dA)^2)$ would not be gauge-invariant, and the Yang–Mills action would depend on the gauge — gauge invariance of the theory would be destroyed. The commutator term is non-negotiable.

---

# The Definition

Let $A$ be a $\mathfrak{g}$-valued 1-form on $M$ (a gauge potential for a compact Lie group $G$). The **Yang–Mills field strength** of $A$ is the $\mathfrak{g}$-valued 2-form

$$F = dA - iq A \wedge A,$$

equivalently in components

$$F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu - iq[A_\mu, A_\nu].$$

In purely geometric notation, writing $\omega = -iqA$ for the connection 1-form, the curvature 2-form is

$$\theta = d\omega + \tfrac{1}{2}[\omega, \omega] = d\omega + \omega\wedge\omega,$$

related to $F$ by $\theta = -iqF$.

**Equivalent characterisation (commutator of covariant derivatives).** $F$ is the unique $\mathfrak{g}$-valued 2-form satisfying

$$[D_\mu, D_\nu]\psi = -iq F_{\mu\nu}\,\psi$$

for every section $\psi$ of every associated bundle. This identity is the geometric content of the field strength: $F$ measures the failure of the covariant derivative to commute.

**Equivalent characterisation (parallel transport around an infinitesimal loop).** For an infinitesimal parallelogram in the $\mu$-$\nu$ plane with sides $\epsilon\partial_\mu$ and $\delta\partial_\nu$, parallel transporting a section around the boundary returns it rotated by $\exp(-iq\epsilon\delta\, F_{\mu\nu}) + O(\epsilon^2\delta, \epsilon\delta^2)$. The field strength is the infinitesimal "holonomy per unit area."

Under a gauge transformation $g : M \to G$, $A$ transforms inhomogeneously as $A \to A' = gAg^{-1} - (i/q)(dg)g^{-1}$, but $F$ transforms *homogeneously*:

$$F \to F' = gFg^{-1}.$$

This makes $F$ a section of the adjoint bundle $\operatorname{ad} P \otimes \Lambda^2 T^*M$, while $A$ is *not* a globally defined tensor.

---

# Relate to Other Fields / Compression

**$F$ is the curvature of a connection on a principal $G$-bundle.** This is its mathematical name; in differential geometry, the curvature of any linear connection on a vector bundle is the obstruction to flatness, defined exactly as $\Omega = d\omega + \omega\wedge\omega$ where $\omega$ is the connection 1-form. Yang–Mills $F$ is this construction specialised to the principal-bundle context. See [[Gauge Theory III — Principal Connections, Curvature, Holonomy, and Gauge Symmetry]] for the principal-bundle picture, and [[Riemannian Geometry III — Riemann Curvature and Topology]] for the Levi-Civita-connection version where the same formula produces the **Riemann curvature tensor**.

**$F$ is also the field strength tensor of electromagnetism, generalised**: for $G = U(1)$ and $A_\mu = (A_0, \vec A)$ the EM 4-potential, the components of $F_{\mu\nu}$ are exactly the electric and magnetic fields: $F_{0i} = E_i$, $F_{ij} = \epsilon_{ijk}B_k$. The two Maxwell equations involving $\vec E$ and $\vec B$ directly (Gauss's law for $\vec E$, Ampère–Maxwell) become $d\star F = \star J$; the other two ($\operatorname{div}\vec B = 0$, Faraday's law) become $dF = 0$. The Yang–Mills generalisation replaces $U(1)$ by an arbitrary compact $G$, the abelian curvature $F = dA$ by the non-abelian $F = dA - iqA\wedge A$, and the linear Maxwell equations by the non-linear Yang–Mills equations. The structural content is the same.

**True name:** $F$ is the *commutator of covariant derivatives*. The operational form $[D_\mu, D_\nu] = -iqF_{\mu\nu}$ is what you reach for when you want to extract $F$ from a calculation, when you want to prove a Ricci-type identity for the covariant derivative, or when you want to derive the Bianchi identity (which is just $[D_\rho, [D_\mu, D_\nu]] +$ cyclic $= 0$ via the Jacobi identity for commutators). The official formula $F = dA - iqA\wedge A$ is the *consequence* of this true name; the true name is the operational definition you remember and use.

---

# Examples / Corollaries

**Example 1 — Maxwell field strength on $\mathbb{R}^4$.** For $G = U(1)$, $A = A_\mu dx^\mu$ with $A_0 = -\phi$ (electric potential, with sign by convention) and $A_i$ the magnetic vector potential, the commutator $[A_\mu, A_\nu] = 0$ and $F = dA$. In components $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$, the antisymmetric "Faraday tensor". The non-zero independent components are $F_{0i} = -E_i$ and $F_{ij} = \epsilon_{ijk}B_k$, recovering the electric and magnetic field vectors.

**Example 2 — Pure-gauge connection has zero field strength.** A gauge potential of the form $A = -(i/q) g^{-1}dg$ for a smooth $g : M \to G$ has $F = 0$. To see this, compute: $dA = -(i/q)d(g^{-1}dg) = -(i/q)(dg^{-1}\wedge dg) = (i/q)(g^{-1}dg)\wedge(g^{-1}dg)$ (using $dg^{-1} = -g^{-1}(dg)g^{-1}$), so $dA = (i/q)A \cdot iq\cdot A\cdot iq\cdot(-1)/q = -iq\cdot A\wedge A$, hence $F = dA - iqA\wedge A = -iqA\wedge A + iqA\wedge A = 0$. (Or use the Maurer–Cartan equation $d(g^{-1}dg) + (g^{-1}dg)\wedge(g^{-1}dg) = 0$ directly.) Pure gauge configurations have zero field strength — they are gauge transformations of the trivial connection.

**Example 3 — Constant non-abelian field strength on $\mathbb{R}^4$.** Take $G = SU(2)$ and $A = \tfrac{1}{2}F^a_{\mu\nu}x^\nu (\sigma_a/2)\, dx^\mu$ for a *constant* $\mathfrak{su}(2)$-valued 2-form $F^a_{\mu\nu}$. Then $\partial_\mu A_\nu - \partial_\nu A_\mu = F^a_{\mu\nu}(\sigma_a/2)$ to leading order, and one verifies the higher-order $[A, A]$ corrections give zero only when $F^a_{\mu\nu}$ is "abelian" — meaning $F$ takes values in a one-dimensional subalgebra. This is a non-trivial example showing that constant non-abelian field strengths are highly constrained.

**Non-example — $F = dA$ alone is *not* the non-abelian field strength.** A common error is to write $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ for non-abelian gauge theory, forgetting the commutator. This expression does *not* transform homogeneously under gauge change: $\partial_\mu A'_\nu - \partial_\nu A'_\mu \neq g(\partial_\mu A_\nu - \partial_\nu A_\mu)g^{-1}$ in general. The commutator term $-iq[A_\mu, A_\nu]$ is exactly what is needed to compensate for the non-trivial transformation of $\partial A$, producing a homogeneously-transforming $F$. The non-example $F^{\text{wrong}} = dA$ would render the Yang–Mills action gauge-dependent and the entire theory ill-defined.

**Calibration check.** A reader who has internalised the definition should be able to: (a) verify directly from $F = dA - iqA\wedge A$ that $F$ transforms homogeneously under $A \to gAg^{-1} - (i/q)dg \cdot g^{-1}$, using the Maurer–Cartan identity $d(g^{-1}) = -g^{-1}(dg)g^{-1}$; (b) prove the Bianchi identity $d_A F = dF - iq[A, F] = 0$ from the definition (it follows from $d^2 = 0$ and the Jacobi identity in two lines); (c) compute the field strength of the abelian gauge potential $A = -\tfrac12 B(x^1\,dx^2 - x^2\,dx^1)$ on $\mathbb{R}^4$ and recover $F = B\, dx^1\wedge dx^2$, a uniform magnetic field in the $z$-direction.

---

# Unlocked by This

> [!tip] Chern Classes as Curvature Invariants *(from Algebraic Topology and Index Theory)*
> The trace polynomials of $F$ — specifically $\operatorname{tr}(F)$, $\operatorname{tr}(F\wedge F)$, $\operatorname{tr}(F\wedge F\wedge F)$, etc. — are closed differential forms whose de Rham cohomology classes are independent of the connection $A$. These classes are the **Chern characters** of the bundle, and (after a change of basis) the **Chern classes** $c_1, c_2, c_3, \dots \in H^*(M; \mathbb{Z})$. The Chern–Weil construction makes precise that "curvature determines topology": every characteristic class of a $G$-bundle can be computed from any connection on it as an explicit polynomial in the curvature. The second Chern class $c_2 = -\frac{1}{8\pi^2}\operatorname{tr}(F\wedge F)$ is the topological invariant whose integral counts the instanton number, and the **Pontryagin classes** of the tangent bundle of a manifold appear analogously as polynomials in the Riemann curvature. See [[Algebraic Topology III — Higher Homotopy and Chern Forms]].

> [!tip] The Wilson Loop and Holonomy *(from Quantum Gauge Theory)*
> Integrating the field strength over a 2-surface bounded by a loop gives, via Stokes' theorem, the *holonomy* $\operatorname{Pexp}\oint_C A$ of the connection around the loop. The trace of this holonomy, $W(C) = \operatorname{tr}(\operatorname{Pexp}\oint_C A)$, is the **Wilson loop**, the basic gauge-invariant observable of quantum gauge theory. Wilson-loop expectation values $\langle W(C)\rangle$ are the order parameter for confinement (area-law decay $\langle W(C)\rangle \sim e^{-\sigma\cdot\text{area}}$ signifies confinement, perimeter-law decay signifies a deconfined phase), and they are the natural observables in **lattice gauge theory**, where they are computable from Monte Carlo simulations. The 't Hooft–Polyakov **disorder operators** (magnetic-monopole worldlines) provide the dual order parameter, and the interplay between Wilson loops and 't Hooft loops underlies the modern understanding of gauge-theory phases.
