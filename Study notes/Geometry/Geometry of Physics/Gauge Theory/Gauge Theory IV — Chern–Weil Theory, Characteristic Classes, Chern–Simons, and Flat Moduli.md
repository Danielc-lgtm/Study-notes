---
type: topic
subject: gauge-theory
chapter: "Gauge Theory IV"
title: "Gauge Theory IV — Chern–Weil Theory, Characteristic Classes, Chern–Simons, and Flat Moduli"
tags: [gauge-theory, chern-weil, characteristic-classes, chern-simons]
---

# Notation Registry

$P\to M$ is a principal $G$-bundle, $A$ is a connection, and $F_A=dA+A\wedge A$. An invariant degree-$k$ polynomial is written as its polarized symmetric map $f:\mathfrak g^k\to\mathbb R$. We use anti-Hermitian matrix Lie algebras. The normalization $\frac{i}{2\pi}F_A$ makes Chern forms real and integral in cohomology.

# Motivation

A connection is auxiliary differential data, but curvature can carry topology that no gauge can remove. The obstacle is that curvature is adjoint-valued rather than scalar. Invariant polynomials remove the gauge coordinates without discarding the global obstruction. The Chern–Weil mechanism is therefore a three-step compression: curvature transforms covariantly, invariance makes a scalar form global, and Bianchi makes it closed.

Connection independence has a stronger form than equality in cohomology. The difference of two characteristic forms is the derivative of an explicit odd-degree transgression form. On a three-manifold this primitive becomes the Chern–Simons functional, whose critical points are flat connections. Characteristic classes and flat moduli are thus two faces of the same curvature calculus: one integrates curvature in even dimension; the other studies its vanishing through an odd-dimensional action.

# Concept Map

## §4.1 Invariant polynomials and Chern–Weil

- [[Def - Ad-Invariant Polynomial]] isolates the scalar functions that survive gauge conjugation.
- [[Thm - Chern-Weil Theorem]] proves closedness, naturality, and connection independence with an explicit variation formula.

## §4.2 Characteristic classes

- [[Def - Chern Classes from Curvature]] fixes determinant normalization, Whitney sum, duality, and integrality.
- [[Def - Pfaffian]] produces the Euler form for oriented real bundles.
- [[Def - The Euler Class of a Real Oriented Vector Bundle]] and [[Thm - Gauss-Bonnet-Chern Theorem]] connect curvature to Euler characteristic.
- [[Thm - First Chern Class of the Hopf Bundle is One]] calibrates the sign and normalization.

## §4.3 Transgression and Chern–Simons

- [[Def - Chern-Simons Transgression Form]] is the explicit primitive comparing two characteristic forms.
- [[Def - Chern-Simons Functional]] gives the circle-valued three-dimensional action and proves that its critical points are flat.
- [[Def - Moduli Space of Flat Connections]] records the quotient, stabilizers, and deformation complex.

## §4.4 Holonomy as characteristic geometry

- [[Def - Berry Connection]] is the connection on an eigenline bundle.
- [[Thm - Berry Phase Equals Holonomy of the Berry Connection]] identifies the observable phase.
- [[Ex - Berry Phase for a Spin-Half in a Magnetic Field]] computes the curvature and Chern number.

# Sources and Targets

Starting from a connection, the target may be a closed even form, a topological cohomology class, an odd transgression form, or a flat-moduli problem. Conversely, a known characteristic number obstructs flatness or triviality; a boundary problem suggests transgression; and a representation of $\pi_1$ suggests a flat connection. The recurring conversion route is
$$A\longmapsto F_A\longmapsto f(F_A^k)\longmapsto [f(F_A^k)],$$
with the variation of the middle expression producing Chern–Simons theory.

# Legal Operations

1. **Polarize an invariant polynomial.** Replace a homogeneous polynomial by its symmetric multilinear form before inserting differential forms.
2. **Insert even-degree curvature forms.** Their wedge products commute, so no hidden Koszul signs occur between curvature factors.
3. **Replace $d$ by $d_A$ under $f$.** Infinitesimal invariance cancels the sum of commutator terms.
4. **Use Bianchi.** It turns $d_A F_A=0$ into closedness of every characteristic form.
5. **Interpolate affinely between connections.** The difference $A_1-A_0$ is tensorial, so $A_t=A_0+t(A_1-A_0)$ is globally meaningful.
6. **Transgress.** Integrating the first variation gives an explicit primitive for the difference of characteristic forms.
7. **Integrate only top-degree forms on oriented closed manifolds.** This produces characteristic numbers independent of the connection.
8. **Pass to $\mathbb R/\mathbb Z$ for Chern–Simons.** Large gauge transformations can shift a real lift by an integer.
9. **Linearize flatness modulo gauge.** The complex $\Omega^0\xrightarrow{d_A}\Omega^1\xrightarrow{d_A}\Omega^2$ controls stabilizers, tangents, and obstructions.

## Illegal but tempting

It is illegal to infer $F_A=0$ from vanishing characteristic numbers: a nonzero $SU(2)$ curvature can have $\operatorname{tr}(F_A\wedge F_A)=0$ pointwise. Flatness itself legalizes the inference only because it directly sets curvature to zero. It is illegal to treat a Chern–Simons lift as a gauge-invariant real number; a degree-one gauge transformation shifts it by an integer, while exponentiation or reduction modulo $\mathbb Z$ legalizes it. It is illegal to conclude that a flat bundle is trivial: a nontrivial representation $\pi_1(M)\to G$ gives nontrivial holonomy; simple connectivity removes this obstruction.

# Problem-Solving Strategy

First identify whether the desired output is local, cohomological, or variational. For a cohomology class, choose whichever connection makes curvature easiest and invoke connection independence. For a comparison of connections, do not recompute both characteristic forms separately: interpolate and transgress. On a boundary, ask whether the even-dimensional characteristic form has an odd-dimensional primitive. For flatness, replace nonlinear geometry by monodromy when possible and retain stabilizers rather than assuming the quotient is smooth.

The unifying question is: **which gauge-invariant information survives after the connection itself is allowed to vary?**

# Most Reusable Properties

- [[Thm - Chern-Weil Theorem|Chern–Weil classes]] depend on the bundle, not the chosen connection, so a convenient metric or connection may be selected for computation.
- [[Def - Chern-Simons Transgression Form|Transgression]] upgrades abstract cohomological independence to a formula and supplies boundary correction terms.
- [[Def - Chern Classes from Curvature|Chern forms]] are natural and multiplicative, turning pullbacks and direct sums into computational tools.
- [[Def - Chern-Simons Functional|Chern–Simons]] has flat connections as critical points, connecting characteristic classes to representation varieties and Floer theory.
- [[Def - Moduli Space of Flat Connections|Flat deformation cohomology]] separates infinitesimal automorphisms, deformations, and obstructions by degree.

# Insights

The true local-to-global mechanism is not integration. It is descent: curvature transforms homogeneously, and invariant polynomials erase its conjugation ambiguity. Closedness then moves the result from differential forms to cohomology, where connection dependence disappears. Integration is only the final pairing with a fundamental class.

Characteristic forms and Chern–Simons forms differ by one categorical level. The former are intrinsic closed forms; the latter compare two choices and are therefore relative. Forgetting this distinction causes both common errors: treating a local potential as global and treating Chern–Simons as an absolute real number.

# Bridges

Gauge Theory V uses $\int\operatorname{tr}(F\wedge *F)$ as an action and $\int\operatorname{tr}(F\wedge F)$ as its topological lower bound. Gauge Theory VIII interprets the flat deformation complex analytically. Gauge Theory XI pairs characteristic classes with four-manifold fundamental classes and compares them with intersection forms.

# Sources

- Andriy Haydys, *Introduction to Gauge Theory*, §§3.1–3.3.
- Konstantin Wernli, *Mathematical Gauge Theory*, §2.5.
