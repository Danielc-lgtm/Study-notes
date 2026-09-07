---
type: exercise
subject: gauge-theory
prereqs: ["Def - Seiberg-Witten Equations and Quadratic Spinor Map", "Thm - Weitzenbock Formula for a Dirac Bundle"]
tags: [gauge-theory, seiberg-witten, compactness]
---

# Prerequisite Concepts

- [[Def - Seiberg-Witten Equations and Quadratic Spinor Map]]
- [[Thm - Weitzenbock Formula for a Dirac Bundle]]

# Exercise

For a solution of $D_A^+\psi=0$ and $F_A^+=q(\psi)+\eta$, combine the spin-c Weitzenböck formula with
$$\langle q(\psi)\psi,\psi\rangle=\frac12|\psi|^4$$
to show that $|\psi|$ has a uniform pointwise bound depending only on the scalar curvature and $\eta$.

> [!solution]- Solution
> With the chapter normalization, pairing the Weitzenböck identity for $D_A^-D_A^+\psi=0$ with $\psi$ yields
> $$0=\frac12\Delta|\psi|^2+|\nabla_A\psi|^2+\frac{s}{4}|\psi|^2+\frac14|\psi|^4+\frac12\langle c(\eta)\psi,\psi\rangle.$$
> At a maximum point of $|\psi|^2$, the Laplacian term is nonnegative in the convention $\Delta=d^*d$, and the covariant-derivative term is nonnegative. Since $|\langle c(\eta)\psi,\psi\rangle|\le C|\eta||\psi|^2$ for the fixed Clifford convention, either $\psi=0$ there or
> $$\frac14|\psi|^2\le \frac14\|s_-\|_\infty+\frac C2\|\eta\|_\infty.$$
> The maximum controls $|\psi|$ everywhere. The precise numerical constant $C$ depends only on the norm convention for Clifford multiplication, not on the solution.

# Trigger

Whenever a Weitzenböck formula contains a positive quartic term, evaluate it at a maximum before attempting global Sobolev estimates.
