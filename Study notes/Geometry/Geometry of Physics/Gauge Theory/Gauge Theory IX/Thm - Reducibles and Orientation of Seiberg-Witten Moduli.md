---
type: theorem
subject: gauge-theory
prereqs: ["Thm - Slices and Generic Regularity for Seiberg-Witten Moduli", "Def - Determinant Line and Orientation of a Fredholm Operator"]
tags: [gauge-theory, seiberg-witten, reducible, orientation]
---

# Prerequisite Concepts

- [[Thm - Slices and Generic Regularity for Seiberg-Witten Moduli]]
- [[Def - Determinant Line and Orientation of a Fredholm Operator]]

# Statement

> [!theorem] Removing reducibles and orienting
> If $b_2^+(M)>0$, a generic perturbation has no reducible solutions. A homology orientation—an orientation of $H^1(M;\mathbb R)\oplus H^2_+(M;\mathbb R)$—orients every regular irreducible Seiberg–Witten moduli space.

# Formal Proof

> [!proof]- Formal Proof
> At a reducible, $\psi=0$ and the curvature equation says $F_A^+=\eta$. Relative to $A_0$, possible right sides form the affine subspace $F_{A_0}^++\operatorname{im}d^+$. Its cokernel is the $b_2^+$-dimensional space of harmonic self-dual forms. Therefore this wall has codimension $b_2^+$, and a generic perturbation avoids it when $b_2^+>0$.
>
> The determinant line of the gauge-fixed linearization is homotopic to that of $D_A^+\oplus(d^+\oplus d^*)$. The Dirac summand is complex linear and therefore canonically oriented as a real determinant line. The real summand has kernel $H^1$ and cokernel $H^0\oplus H^2_+$. For connected $M$, $H^0$ has its canonical orientation; choosing an orientation of $H^1\oplus H^2_+$ orients the remaining determinant. Homotopy transports this orientation to the actual operator and hence to the moduli space.

# Wall Warning

When $b_2^+=1$, a one-parameter family can cross the reducible wall, producing chamber dependence. This is handled in the invariant chapter.

