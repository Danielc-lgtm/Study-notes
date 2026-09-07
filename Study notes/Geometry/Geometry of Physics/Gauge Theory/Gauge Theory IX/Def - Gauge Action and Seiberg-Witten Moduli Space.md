---
type: definition
subject: gauge-theory
prereqs: ["Def - Seiberg-Witten Equations and Quadratic Spinor Map", "Def - Gauge Group of a Principal Bundle"]
tags: [gauge-theory, seiberg-witten, gauge-action, moduli]
---

# Prerequisite Concepts

- [[Def - Seiberg-Witten Equations and Quadratic Spinor Map]]
- [[Def - Gauge Group of a Principal Bundle]]

# The Definition

> [!definition] Gauge action and moduli space
> The gauge group $\mathcal G=C^\infty(M,U(1))$ acts by
> $$(\psi,A)\cdot g=(g^{-1}\psi,A+2g^{-1}dg).$$
> The moduli space is
> $$\mathcal M_\eta=\{(\psi,A):D_A^+\psi=0, F_A^+=q(\psi)+\eta\}/\mathcal G.$$

The factor two reflects that $A$ is a determinant-line connection. Gauge covariance of the Dirac operator and invariance of abelian curvature imply equivariance of the Seiberg–Witten map.

# Stabilizers

A stabilizing gauge transformation satisfies $dg=0$, hence is constant. If $\psi\not\equiv0$, then $g^{-1}\psi=\psi$ forces $g=1$; such configurations are irreducible. If $\psi=0$, the full constant $U(1)$ stabilizes the configuration; these are reducibles. Thus the irreducible quotient admits ordinary slices, while reducibles are singular points unless perturbations remove them.

