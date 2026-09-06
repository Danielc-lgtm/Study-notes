---
type: topic
subject: gauge-theory
chapter: "Gauge Theory VI"
title: "Gauge Theory VI — Clifford Algebras, Spin Geometry, and Dirac Operators"
tags: [gauge-theory, clifford-algebra, spin-geometry, dirac-operator]
---

# Notation Registry

$(M^n,g)$ is oriented and Riemannian. Clifford multiplication uses
$$c(\xi)c(\eta)+c(\eta)c(\xi)=-2g(\xi,\eta).$$
$F_{SO}(M)$ is the oriented orthonormal-frame bundle, $S$ a spinor bundle, $S^\pm$ its chiral pieces in even dimension, $L$ the determinant line of a spin-c structure, and $D_A$ the Dirac operator coupled to a unitary connection $A$.

# Motivation

A Laplacian is second order and loses directional phase information. Clifford multiplication supplies matrices whose anticommutator reproduces the metric, allowing a first-order operator with scalar principal square. Spin structures globalize the irreducible modules for those matrices. Spin-c structures add a central phase so that four-manifolds admit the spinorial objects needed by Seiberg–Witten theory even when ordinary spin structures do not exist.

The decisive identity is Weitzenböck: the square of a Dirac operator is a nonnegative connection Laplacian plus curvature. It converts a first-order equation into a second-order estimate and turns scalar or gauge curvature into algebraic control of solutions.

# Concept Map

## §6.1 Clifford algebra and spin groups

- [[Def - Clifford Algebra and Clifford Module]] derives the anticommutation relation and exterior-algebra module.
- [[Def - Spin Group and Low-Dimensional Spin Groups]] constructs the double cover and identifies $\operatorname{Spin}(3)$ and $\operatorname{Spin}(4)$.

![[Exercise Index - §6.1 Clifford Algebra and Spin Groups]]

## §6.2 Dirac bundles and operators

- [[Def - Dirac Bundle and Dirac Operator]] fixes metric and connection compatibility and proves ellipticity from the symbol.
- [[Thm - Formal Self-Adjointness of a Dirac Operator]] includes the boundary warning.
- [[Def - Connection Laplacian]] identifies the positive second-order part.

## §6.3 Spin and spin-c geometry

- [[Def - Spin and Spin-c Structures]] states the lifting problems, obstructions, determinant line, and torsor classifications.
- [[Def - Spinor Bundle, Chirality, and Twisted Dirac Operator]] constructs spinors, chirality, twisting, and the determinant-connection factor $1/2$.

## §6.4 Weitzenböck mechanism

- [[Thm - Weitzenbock Formula for a Dirac Bundle]] proves $D^2=\nabla^*\nabla+\mathcal R$ in a normal frame.

![[Exercise Index - §6.2 Dirac and Spin-c Geometry]]

# Sources and Targets

A metric vector space produces a Clifford algebra; a frame-bundle lift and representation produce a spinor bundle; a compatible connection produces a Dirac operator; squaring produces a connection Laplacian plus curvature. In reverse, a desired first-order elliptic operator suggests searching for a Clifford symbol, while vanishing questions suggest applying Weitzenböck and integrating.

# Legal Operations

1. **Polarize the Clifford square relation** to recover anticommutation.
2. **Lift oriented frames through the double cover** only after checking $w_2$.
3. **Twist spinors by a unitary bundle** and add the twisting connection to the spin connection.
4. **Split chirality in even dimension** and remember that one-form multiplication reverses it.
5. **Read ellipticity from the symbol** because $c(\xi)^{-1}=-c(\xi)/|\xi|^2$ for $\xi\ne0$.
6. **Square in a normal frame** so first derivatives of the frame vanish at the chosen point.
7. **Integrate Weitzenböck** to turn curvature positivity into a kernel-vanishing result.
8. **Twist spin-c structures by line bundles** while squaring the twist on the determinant line.

## Illegal but tempting

A spin representation is not a representation of $SO(n)$: the central $-1$ would have to act both trivially and nontrivially. An oriented manifold need not be spin; $w_2(TM)$ is the obstruction. A spin-c determinant connection does not enter the spinor connection with full weight; the determinant representation has weight two, producing the factor $1/2$.

# Problem-Solving Strategy

For global existence, translate geometry into a lifting problem for transition functions. For analysis of $Ds=0$, square first, insert Weitzenböck, pair with $s$, and integrate. For a coupled operator, separate Levi–Civita curvature from twisting curvature before estimating signs. The unifying question is: **how does the metric quadratic form become a first-order elliptic operator whose square exposes curvature?**

# Most Reusable Properties

- Clifford multiplication by a nonzero covector is invertible, so every Dirac operator is elliptic.
- Spin-c structures form an $H^2(M;\mathbb Z)$-torsor and have determinant class congruent to $w_2(TM)$ modulo two.
- Chirality turns a self-adjoint Dirac operator into the pair $D^+$ and its formal adjoint $D^-$.
- Weitzenböck isolates analysis in $\nabla^*\nabla$ and geometry in a zeroth-order curvature endomorphism.

# Insights

A spin-c structure is not a weakened spin structure obtained by ignoring an obstruction. It cancels that obstruction with a line-bundle cocycle. The determinant line records the cancellation globally, which is why its first Chern class is the integral lift of $w_2$.

The phrase “Dirac is a square root of the Laplacian” refers only to principal symbols on a curved manifold. The exact square necessarily remembers curvature; this error term is the source of the strongest geometric applications rather than a nuisance.

# Bridges

Gauge Theory VII treats Dirac operators as elliptic Fredholm operators on Sobolev spaces. Gauge Theory IX uses a spin-c Dirac operator coupled to the determinant connection in the Seiberg–Witten equations.

# Sources

- Andriy Haydys, *Introduction to Gauge Theory*, §§4.1–4.4.
