---
type: exercise-index
subject: ring-theory
section: "2.2"
tags: [algebra, ring-theory]
---

## §2.2 Homomorphisms, Ideals and Quotients — Exercises

The exercises of §2.2 drill the master technique of ring theory: identify a quotient by building a surjection with the right kernel and applying the first isomorphism theorem. Each exercise also rehearses an ideal-classification move — every ideal of $\mathbb{Z}$ is principal (by Euclidean minimality), $(2, X) \subseteq \mathbb{Z}[X]$ is *not* principal (by degree-and-reduction), and an ideal containing a unit is everything (the field criterion).

- [[Ex - Identifying a quotient ring with the first isomorphism theorem]] (⭐⭐) — identify $\mathbb{R}[X]/(X^2+1)\cong\mathbb{C}$ by building the evaluation homomorphism $X\mapsto i$, computing image and kernel, and running the first isomorphism theorem in reverse; the kernel computation uses polynomial division to force remainders to vanish ([[Def - Polynomial Ring]], [[Def - Ring Homomorphism]], [[Def - Ideal]], [[Def - Quotient Ring]], [[Thm - First Isomorphism Theorem for Rings]], [[Thm - Euclidean Algorithm for Polynomials]]).

- [[Ex - Every ideal of the integers is principal]] (⭐⭐) — classify the ideals of $\mathbb{Z}$ by naming the least positive element of a non-zero ideal and using the division algorithm with a minimality argument to kill the remainder, proving $\mathbb{Z}$ is a principal ideal domain ([[Def - Ring]], [[Def - Ideal]]).

- [[Ex - The ideal (2, X) is not principal]] (⭐⭐⭐) — prove a negative structural statement by contradiction: a single generator of $(2,X)\trianglelefteq\mathbb{Z}[X]$ would divide both $2$ and $X$, forcing it via a degree count to be the unit $\pm1$, so the ideal would be all of $\mathbb{Z}[X]$ — refuted by a reduction-mod-$2$ homomorphism showing the ideal is proper; hence $\mathbb{Z}[X]$ is not a PID ([[Def - Polynomial Ring]], [[Def - Unit and Field]], [[Def - Ideal]]).

- [[Ex - An ideal contains a unit exactly when it is the whole ring]] (⭐) — establish the equivalence $I=R\iff 1\in I\iff I$ contains a unit by closing a cycle of one-line strong-closure arguments, and deduce that a field has exactly the two ideals $\{0\}$ and itself ([[Def - Ring]], [[Def - Unit and Field]], [[Def - Ideal]]).
