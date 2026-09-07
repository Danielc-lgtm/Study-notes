---
type: theorem
subject: gauge-theory
prereqs: ["Def - Principal Symbol and Elliptic Differential Operator", "Thm - Sobolev Embedding, Compactness, and Multiplication"]
tags: [gauge-theory, elliptic-estimate, regularity]
---

# Prerequisite Concepts

- [[Def - Principal Symbol and Elliptic Differential Operator]]
- [[Thm - Sobolev Embedding, Compactness, and Multiplication]]

# Statement

> [!theorem] Global elliptic estimate
> If $L:\Gamma(E)\to\Gamma(F)$ is elliptic of order $\ell>0$ on a compact manifold, then for $k\ge0$ and $1<p<\infty$,
> $$\|s\|_{W^{k+\ell,p}}\le C\bigl(\|Ls\|_{W^{k,p}}+\|s\|_{L^p}\bigr).$$
> Consequently, $Ls\in W^{k,p}$ distributionally implies $s\in W^{k+\ell,p}$; if $Ls$ is smooth, then $s$ is smooth.

# Proof

> [!proof]- Formal Proof
> Symbol invertibility permits a local parametrix: freeze the principal coefficients, invert the Fourier multiplier $\sigma_L(x,\xi)$ for $|\xi|\ge1$, and correct the variable-coefficient error recursively. After localizing by cutoffs this gives operators $Q$ of order $-\ell$ and $R$ of order $-1$ such that $QL=I-R$. Fourier multiplier estimates give
> $$\|Qs\|_{W^{k+\ell,p}}\le C\|s\|_{W^{k,p}},\qquad
> \|Rs\|_{W^{k+\ell,p}}\le C\|s\|_{W^{k+\ell-1,p}}.$$
> Hence
> $$\|s\|_{W^{k+\ell,p}}\le C\|Ls\|_{W^{k,p}}+C\|s\|_{W^{k+\ell-1,p}}.$$
> The interpolation inequality $\|s\|_{W^{k+\ell-1,p}}\le\varepsilon\|s\|_{W^{k+\ell,p}}+C_\varepsilon\|s\|_{L^p}$ absorbs the first term for small $\varepsilon$. A finite partition of unity gives the global estimate.
>
> Apply the estimate successively to weak solutions to gain $\ell$ derivatives at each step. Sobolev embedding then turns membership in every $W^{m,p}$ into smoothness.

# Role of the Lower-Order Norm

The $L^p$ term controls the finite-dimensional kernel. It may be removed only after restricting to a complement of the kernel or imposing a coercive boundary/normalization condition.

