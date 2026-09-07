---
type: topic
subject: gauge-theory
chapter: "Gauge Theory III"
title: "Gauge Theory III — Principal Connections, Curvature, Holonomy, and Gauge Symmetry"
tags: [geometry, gauge-theory, principal-bundles, connections, holonomy]
---

# Notation Registry

$P\xrightarrow\pi M$ is a right principal $G$-bundle, $R_g(p)=pg$, and $\mathfrak g=T_eG$. For $\xi\in\mathfrak g$ the fundamental field is
$$\xi_P(p)=\left.\frac d{dt}\right|_0p\exp(t\xi).$$
A principal connection is $\omega\in\Omega^1(P;\mathfrak g)$ with
$$\omega(\xi_P)=\xi,\qquad R_g^*\omega=\operatorname{Ad}_{g^{-1}}\omega.$$
Its curvature is
$$\Omega=d\omega+\tfrac12[\omega,\omega].$$
For a local section $s_\alpha$, set $A_\alpha=s_\alpha^*\omega$ and $F_\alpha=s_\alpha^*\Omega$. If $s_\beta=s_\alpha g_{\alpha\beta}$, then
$$A_\beta=\operatorname{Ad}_{g_{\alpha\beta}^{-1}}A_\alpha+g_{\alpha\beta}^{-1}dg_{\alpha\beta},\qquad F_\beta=\operatorname{Ad}_{g_{\alpha\beta}^{-1}}F_\alpha.$$
For matrix groups, $F_A=dA+A\wedge A=dA+\tfrac12[A,A]$.

# Motivation

A principal bundle specifies which frames are admissible but not how to compare frames at different points. A connection supplies that comparison in four equivalent forms. It is a horizontal complement to the vertical tangent directions, a $\mathfrak g$-valued one-form reproducing infinitesimal group motion, a family of local gauge potentials, and a rule for lifting paths. Each form answers a different kind of question; none is merely notation for another.

Curvature measures the failure of horizontal directions to close under brackets. Holonomy integrates that failure along loops, while topology may leave nontrivial holonomy even when curvature vanishes. Gauge transformations change the bundle coordinates used to write the comparison rule. The moduli problem therefore studies connections only after quotienting by this change of coordinates.

# Concept Map

## §3.1 Lie-algebra-valued forms and Maurer–Cartan

- [[Def - Lie-Algebra-Valued Differential Form]] and [[Def - Bracket of g-Valued Forms]] fix the graded bracket.
- [[Def - The Maurer-Cartan Form]] is the canonical connection-like form on $G$.
- [[Thm - Maurer-Cartan Equation]] proves $d\theta+\tfrac12[\theta,\theta]=0$.
- [[Ex - The Maurer-Cartan Form on SU(2)]] calibrates the non-abelian signs.

> [!note] Exercises
> [[Exercise Index - §3.1 Lie-Algebra-Valued Forms and the Maurer-Cartan Form]]

## §3.2 Vertical and horizontal geometry

- [[Def - Fundamental Vector Field of a Principal Bundle]] identifies $\mathfrak g$ with each vertical tangent space.
- [[Def - Horizontal Subspace]] gives a $G$-equivariant complement $T_pP=H_p\oplus V_p$.
- [[Def - Connection 1-Form on a Principal Bundle]] packages the same projection algebraically.
- [[Thm - Principal Connection is Equivalent to a Horizontal Distribution]] proves the equivalence in both directions.

> [!note] Exercises
> [[Exercise Index - §3.2 Principal Connections]]

## §3.3 Local potentials, curvature, and covariance

- [[Def - Local Connection 1-Form (Gauge Potential)]] pulls the global connection down by a local section.
- [[Thm - Gauge Transformation Law for Local Connection 1-Forms]] derives the inhomogeneous term.
- [[Def - Curvature 2-Form on a Principal Bundle]] and [[Thm - Cartan Structural Equation for Principal Connections]] derive $F_A=dA+\tfrac12[A,A]$.
- [[Thm - Bianchi Identity for Principal Connections]] proves $d_AF_A=0$.
- [[Ex - Computing the Curvature in Two Different Gauges]] checks covariance directly.

> [!note] Exercises
> [[Exercise Index - §3.3 Curvature and the Bianchi Identity]]

## §3.4 Associated bundles and the adjoint bundle

- [[Def - Adjoint Bundle]] is $\operatorname{Ad}P=P\times_{\operatorname{Ad}}\mathfrak g$.
- [[Def - Exterior Covariant Derivative on Associated Bundles]] turns equivariant forms into bundle-valued forms.
- [[Thm - Principal Connection Induces a Connection on Every Associated Bundle]] proves independence of local gauge.
- [[Ex - The Affine Space of Connections on a Principal Bundle]] identifies the modelling space $\Omega^1(M;\operatorname{Ad}P)$.

> [!note] Exercises
> [[Exercise Index - §3.4 Induced Connections on Associated Bundles]]

## §3.5 Horizontal lifts, holonomy, and flat monodromy

- [[Thm - Horizontal Lift Existence and Uniqueness]] integrates the horizontal distribution along any path.
- [[Def - Parallel Transport of a Principal Connection]] records the resulting equivariant map of fibres.
- [[Def - Holonomy Group of a Principal Connection]] organizes loop transport.
- [[Def - Gauge Group of a Principal Bundle]] describes vertical bundle automorphisms as equivariant maps $P\to G$.
- [[Thm - Flat Connections and Monodromy Representations]] identifies flat gauge classes with conjugacy classes of representations of $\pi_1(M)$.

![[Exercise Index - §3.5 Parallel Transport, Holonomy, and Gauge Symmetry]]

# Sources and Targets

The source may be any one of four input types: a horizontal distribution, a principal connection form, compatible local potentials, or a parallel-transport rule. The principal task is to convert it into whichever representation makes the desired calculation easiest. Curvature questions are local and use $F=dA+A^2$. Global transport questions use horizontal lifts. Moduli questions use the affine space of connections and quotient by the gauge group.

# Legal Operations

1. Split $X\in T_pP$ into horizontal and vertical parts.
2. Recover the vertical generator as $\omega(X)\in\mathfrak g$.
3. Pull back by a local section to obtain $A=s^*\omega$.
4. Change section with $A^g=\operatorname{Ad}_{g^{-1}}A+g^{-1}dg$.
5. Form curvature and use its homogeneous transformation law.
6. Apply $d_A$ and the Bianchi identity, keeping graded signs explicit.
7. Solve the horizontal-lift ODE; concatenate or reverse paths only with the corresponding order of transport maps.
8. For flat connections, pass from homotopy classes of loops to monodromy representations.

# Problem-Solving Strategy

Fix the right-action and local-section convention before calculating. Work upstairs when proving invariance or defining horizontal lift; work downstairs when computing matrices. If an expression contains a naked $A$, expect an inhomogeneous gauge term. If it contains $F$ or $d_A\phi$, expect homogeneous transformation. When curvature vanishes, do not conclude global triviality until the fundamental group has been checked.

# Most Reusable Properties

- $\ker\omega$ is horizontal and $\omega|_{V_p}:V_p\to\mathfrak g$ is an isomorphism.
- Curvature is horizontal and equivariant, hence descends as an $\operatorname{Ad}P$-valued form.
- Connections form an affine space over $\Omega^1(M;\operatorname{Ad}P)$.
- Holonomy transforms by endpoint conjugation.
- Flatness removes local path dependence; monodromy records the remaining global dependence.

# Bridges

Gauge Theory IV applies invariant polynomials to $F$ and studies Chern–Simons and flat moduli. Gauge Theory V varies the curvature norm to obtain Yang–Mills. Gauge Theory IX linearizes a gauge equation and uses the infinitesimal gauge action to build a deformation complex.

# Sources

- Andriy Haydys, *Introduction to Gauge Theory*, §§2.2.3–2.2.5 and §3.3.
- Konstantin Wernli, *Mathematical Gauge Theory*, §§2.3–2.4 and §§2.6–2.7.
