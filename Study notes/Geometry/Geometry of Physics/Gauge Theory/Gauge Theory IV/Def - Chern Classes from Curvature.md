---
type: definition
subject: gauge-theory
prereqs: ["Thm - Chern-Weil Theorem"]
tags: [gauge-theory, chern-class, characteristic-class]
---

# The Definition

> [!definition] Chern forms and classes
> For a rank-$r$ Hermitian bundle with unitary connection $A$, define
> $$\det\left(I+\frac{i}{2\pi}F_A\right)=1+c_1(A)+\cdots+c_r(A).$$
> The de Rham class $c_j(E)=[c_j(A)]\in H^{2j}_{\mathrm{dR}}(M)$ is its $j$th Chern class, and $c(E)=1+c_1(E)+\cdots+c_r(E)$ is the total Chern class.

The normalization makes these real classes the images of integral cohomology classes. In particular
$$c_1(A)=\frac{i}{2\pi}\operatorname{tr}F_A,qquad
c_2(A)=\frac1{8\pi^2}\bigl(\operatorname{tr}(F_A\wedge F_A)-(\operatorname{tr}F_A)^2\bigr)$$

with the second formula interpreted under the anti-Hermitian convention; for $SU(r)$, $\operatorname{tr}F_A=0$ and the sign depends on whether curvature matrices are chosen Hermitian or anti-Hermitian. We use Haydys' anti-Hermitian convention, in which $c_2(P)=\frac1{8\pi^2}[\operatorname{tr}(F_A\wedge F_A)]$ for $SU(2)$.

# Structural Properties

Naturality follows by pulling back curvature. If $E\oplus F$ has the block-diagonal sum connection, determinants multiply, giving
$$c(E\oplus F)=c(E)c(F).$$
Dual curvature is $-F_A^{\mathsf T}$, hence $c_j(E^*)=(-1)^jc_j(E)$. A trivial bundle admits a flat connection, so all positive-degree classes vanish.

# Calibration

For a line bundle, $c_1(L)=\frac{i}{2\pi}[F_A]$ and every period over a closed oriented surface is integral. For the tautological line over $\mathbb CP^1$, the sign is fixed by $c_1(\mathcal O(-1))=-a$ for the positive generator $a$.

**True name:** Chern classes are the integral topological content retained by gauge-invariant polynomials of curvature.
