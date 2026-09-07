---
type: theorem
subject: gauge-theory
prereqs: ["Def - Seiberg-Witten Invariant", "Thm - Weitzenbock Formula for a Dirac Bundle"]
tags: [gauge-theory, seiberg-witten, scalar-curvature, vanishing]
---

# Prerequisite Concepts

- [[Def - Seiberg-Witten Invariant]]
- [[Thm - Weitzenbock Formula for a Dirac Bundle]]

# Statement

> [!theorem] Witten's vanishing theorem
> If $b_2^+(X)\ge2$ and $X$ admits a metric of positive scalar curvature, then $\operatorname{SW}_X(\mathfrak s)=0$ for every spin-c structure $\mathfrak s$.

# Key mechanism

For sufficiently small perturbation, the positive scalar-curvature term and the nonnegative quartic spinor term force $\psi=0$. A generic perturbation can simultaneously avoid all reducibles, leaving no solutions.

> [!proof]- Formal Proof
> Choose a positive-scalar-curvature metric and let $s_0=\min_X s>0$. For a solution, pair the spin-c Weitzenböck formula with $\psi$ and substitute $F_A^+=q(\psi)+\eta$. Integration gives
> $$0=\|\nabla_A\psi\|_2^2+\int_X\frac{s}{4}|\psi|^2+\frac14|\psi|^4+\frac12\langle c(\eta)\psi,\psi\rangle.$$
> There is a convention-dependent constant $C$ with $|\langle c(\eta)\psi,\psi\rangle|\le C|\eta||\psi|^2$. Choose $\|\eta\|_\infty<s_0/(2C)$. Then every term after estimating the last one below is nonnegative, and the coefficient of $|\psi|^2$ is strictly positive. Thus $\psi\equiv0$.
>
> A solution would therefore be reducible and satisfy $F_A^+=\eta$. The reducible perturbations form an affine subset of codimension $b_2^+(X)\ge2$ in the self-dual perturbation space. Choose the preceding small $\eta$ generically outside it. Then the moduli space is empty and its invariant is zero. Perturbation independence from [[Thm - Bordism Invariance of the Seiberg-Witten Invariant]] shows that this is the invariant for $\mathfrak s$. Since $\mathfrak s$ was arbitrary, all Seiberg–Witten invariants vanish.
