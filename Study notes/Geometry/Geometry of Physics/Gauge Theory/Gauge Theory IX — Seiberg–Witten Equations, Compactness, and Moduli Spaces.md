---
type: topic
subject: gauge-theory
chapter: "Gauge Theory IX"
title: "Gauge Theory IX — Seiberg–Witten Equations, Compactness, and Moduli Spaces"
tags: [gauge-theory, seiberg-witten, moduli-space, compactness]
---

# Notation Registry

$X$ is a closed, connected, oriented Riemannian four-manifold with a fixed spin-c structure. Its spinor bundles are $S^\pm$, its determinant line is $L$, and $A$ denotes a unitary connection on $L$. The gauge group is $\mathcal G=C^\infty(X,U(1))$. Self-dual projection is denoted by a superscript $+$, and $\eta\in\Omega^2_+(X;i\mathbb R)$ is a perturbation.

# Motivation

The Seiberg–Witten equations are nonlinear, gauge-invariant PDEs whose quotient of solutions is nevertheless finite-dimensional. Four mechanisms make this possible. The Dirac equation couples geometry to a spinor; the curvature equation supplies a coercive quartic term; gauge fixing removes the infinite-dimensional symmetry; ellipticity turns the remaining infinitesimal problem into finite-dimensional deformation theory. Compactness and orientation then convert regular moduli spaces into counts.

# Concept Map

- [[Def - Seiberg-Witten Equations and Quadratic Spinor Map]] introduces the coupled equations and the positivity hidden in $q(\psi)$.
- [[Def - Gauge Action and Seiberg-Witten Moduli Space]] distinguishes configurations, solutions, orbits, irreducibles, and reducibles.
- [[Thm - Seiberg-Witten Deformation Complex is Elliptic]] identifies infinitesimal stabilizers, deformations, and obstructions.
- [[Def - Sobolev Seiberg-Witten Configuration Space]] supplies the Banach setting in which slices and Fredholm arguments are legitimate.
- [[Thm - Compactness and Smoothness of the Seiberg-Witten Moduli Space]] combines the Weitzenböck estimate, abelian gauge fixing, and elliptic bootstrapping.
- [[Thm - Slices and Generic Regularity for Seiberg-Witten Moduli]] separates quotient geometry from transversality.
- [[Thm - Reducibles and Orientation of Seiberg-Witten Moduli]] isolates the wall and explains the homology orientation.

# Sources and Targets

Given a gauge-invariant PDE, first target an elliptic complex by linearizing both the equation and the group action. Given a sequence of solutions, target a convergent subsequence by bounding the spinor, then the curvature, then using Coulomb gauge and elliptic regularity. Given a singular quotient, target a regular manifold by excluding reducibles and varying the self-dual perturbation.

# Legal Operations

1. Replace a connection by $A_0+a$ and regard $a$ as an $i\mathbb R$-valued one-form.
2. Apply a gauge transformation before taking limits; compactness is modulo gauge.
3. Impose Coulomb gauge relative to a reference connection to control the exact part of $a$.
4. Use the Weitzenböck formula at a maximum of $|\psi|^2$ to obtain a uniform $C^0$ bound.
5. Linearize the equation together with the infinitesimal gauge action.
6. Compute expected dimension from the index of the gauge-fixed deformation operator.
7. Vary $\eta$ in the universal moduli problem to obtain generic regularity.
8. Orient the determinant line using an orientation of $H^1(X;\mathbb R)\oplus H^2_+(X;\mathbb R)$.

## Illegal but tempting

Do not call the raw solution set a moduli space without quotienting by $\mathcal G$. Do not infer compactness from ellipticity: the a priori estimate and gauge fixing are separate inputs. Do not apply a free-action slice theorem at a reducible solution, whose stabilizer contains the constant circle. Do not identify formal dimension with actual dimension unless the obstruction space vanishes.

# Problem-Solving Strategy

Write the equations and normalization first, because factors of two in the determinant connection affect both the gauge action and linearization. Identify stabilizers, pass to Sobolev completions, choose a slice, and form the elliptic deformation complex. Prove compactness independently through Weitzenböck, curvature bounds, Coulomb gauge, and bootstrapping. Only then use perturbations to obtain regularity and the determinant line to orient the result.

# Rederivation Handles

The whole chapter can be recovered from three ideas. First, $q(\psi)$ is chosen so that its action on $\psi$ produces a positive multiple of $|\psi|^4$; this closes the maximum-principle estimate. Second, the symbol of the gauge-fixed linearization is the direct sum of a Dirac symbol and the self-dual de Rham symbol; both are invertible in the relevant directions. Third, an abelian connection has linear curvature, so after Coulomb gauge an $L^2$ curvature bound controls the connection strongly enough for bootstrapping.

# Bridges

[[Gauge Theory VI — Clifford Algebras, Spin Geometry, and Dirac Operators]] supplies spin-c geometry and the Weitzenböck formula. [[Gauge Theory VII — Sobolev Spaces, Elliptic Operators, and Gauge-Fixing Complexes]] supplies analytic completions and elliptic regularity. [[Gauge Theory VIII — Fredholm Maps, Transversality, Determinant Lines, and Degree]] explains why regular, compact, oriented zero sets can be counted. Gauge Theory X performs that count and proves its invariance.

# Exercises

- [[Ex - Stabilizers of Seiberg-Witten Configurations]]
- [[Ex - Maximum-Principle Bound for a Seiberg-Witten Spinor]]
- [[Exercise Index - §9.1 Equations, Gauge Symmetry, and Ellipticity]]
- [[Exercise Index - §9.2 Compactness, Regularity, and Orientation]]

# Sources

- Andriy Haydys, *Introduction to Gauge Theory*, §§1 and 7.1–7.1.8.
