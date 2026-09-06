---
type: topic
subject: gauge-theory
chapter: "Gauge Theory X"
title: "Gauge Theory X — Seiberg–Witten Invariants and Four-Manifold Applications"
tags: [gauge-theory, seiberg-witten, four-manifolds, invariant]
---

# Notation Registry

$X$ is a closed connected oriented four-manifold with $b_2^+(X)\ge2$ and a homology orientation. A spin-c structure is denoted $\mathfrak s$, its determinant line by $L$, and its expected dimension by
$$d(\mathfrak s)=\frac14\bigl(c_1(L)^2-2\chi(X)-3\sigma(X)\bigr).$$
For generic auxiliary data, $\mathcal M_\eta(\mathfrak s)$ is the compact oriented Seiberg–Witten moduli space built in Gauge Theory IX.

# Motivation

Analysis produces a compact oriented manifold, but topology needs a number that survives changes of metric and perturbation. In dimension zero, signs let us count points. In positive even dimension, a based gauge quotient produces a canonical degree-two class whose top power can be integrated. Parametric moduli spaces then show that the number is unchanged. Thus the invariant is not the solution set itself: it is a characteristic number extracted from its bordism class.

# Concept Map

- [[Def - Framed Seiberg-Witten Moduli Space and Mu Class]] constructs the degree-two class from the based gauge group.
- [[Def - Seiberg-Witten Invariant]] matches powers of that class to the expected dimension.
- [[Thm - Bordism Invariance of the Seiberg-Witten Invariant]] proves independence from generic metric and perturbation when $b_2^+\ge2$.
- [[Thm - Finiteness of Seiberg-Witten Basic Classes]] turns the curvature estimate into a finiteness statement in the integral cohomology lattice.
- [[Thm - Positive Scalar Curvature Forces Seiberg-Witten Vanishing]] gives a complete sample application of the Weitzenböck mechanism.
- [[Def - Landmark Applications of Seiberg-Witten Theory]] records the deeper connected-sum, symplectic, and smooth-structure results together with the extra machinery they require.

# Sources and Targets

A compact oriented moduli space targets an integer by matching a cohomology degree to its dimension. Two choices of auxiliary data target the same integer by constructing a compact parameterized moduli space. A nonzero invariant targets geometric obstruction results because any geometry forcing the moduli space to be empty contradicts nonvanishing.

# Legal Operations

1. Count points with determinant-line signs when $d=0$.
2. Pass to the based gauge group to retain a residual principal circle bundle.
3. Pair $\mu^{d/2}$ with the fundamental class when $d$ is nonnegative and even.
4. Compare generic choices through a generic one-parameter family.
5. Use $b_2^+\ge2$ precisely to avoid reducibles along that family.
6. Infer vanishing by finding one admissible metric and perturbation with empty moduli space.
7. Call $c_1(L)$ a basic class only after proving the corresponding invariant is nonzero.

## Illegal but tempting

Do not count an unorientable or noncompact moduli space. Do not integrate $\mu^{d/2}$ when $d$ is odd. Do not suppress chamber dependence at $b_2^+=1$. Do not claim that positive scalar curvature directly contradicts the equations without choosing a small perturbation and excluding reducibles. Do not use the landmark applications as proved lemmas: their gluing and pseudoholomorphic-curve theories lie beyond this unit.

# Problem-Solving Strategy

First compute the expected dimension. If it is negative or odd, the convention gives zero. If it is even, construct the based-gauge circle bundle and pair its Chern class with the moduli-space fundamental class. For invariance, turn a path of auxiliary choices into a bordism and verify both compactness and absence of reducibles. For applications, search for a geometric hypothesis that makes the Weitzenböck identity coercive.

# Rederivation Handles

Three handles recover the chapter. The quotient by based gauge remembers one $U(1)$ phase, and that residual phase is exactly a principal circle bundle. Characteristic numbers are invariant under oriented bordism because the relevant class extends over the bordism. Positive scalar curvature kills spinors because the integrated Weitzenböck identity becomes a sum of nonnegative terms.

# Bridges

[[Gauge Theory IX — Seiberg–Witten Equations, Compactness, and Moduli Spaces]] supplies compactness, regularity, and orientation. [[Gauge Theory IV — Chern–Weil Theory, Characteristic Classes, Chern–Simons, and Flat Moduli]] supplies the Chern class of the framed circle bundle. Gauge Theory XI supplies the intersection-form and four-manifold topology needed to interpret basic classes and Donaldson theory.

# Exercises

- [[Ex - Degree Matching in the Seiberg-Witten Invariant]]
- [[Exercise Index - §10.1 Invariants, Bordisms, and Applications]]

# Sources

- Andriy Haydys, *Introduction to Gauge Theory*, §§1 and 7.2–7.2.1.
