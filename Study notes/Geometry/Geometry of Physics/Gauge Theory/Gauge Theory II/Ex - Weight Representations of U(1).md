---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Representation of a Lie Group"
tags: [gauge-theory, representation-theory, u1]
---

# Prerequisite Concepts

- [[Def - Representation of a Lie Group]]

# Problem Statement

For $k\in\mathbb Z$, define $\rho_k:U(1)\to\mathrm{GL}_1(\mathbb C)$ by $\rho_k(z)=z^k$. Prove that it is a representation, compute its differentiated representation, and show
$$\rho_k\otimes\rho_\ell\cong\rho_{k+\ell},\qquad \rho_k^*\cong\rho_{-k}.$$
Explain why $z\mapsto z^a$ is not a single-valued continuous representation for nonintegral real $a$.

# Solution

> [!proof]- Solution
> Since $(zw)^k=z^kw^k$, $\rho_k$ is a homomorphism; smoothness is immediate for positive $k$, follows from inversion for negative $k$, and is trivial for $k=0$. Writing $z=e^{i\theta}$ gives $\rho_k(e^{i\theta})=e^{ik\theta}$, so
> $$d\rho_k(i t)=ik t.$$
> Tensoring one-dimensional representations multiplies their characters:
> $$z^kz^\ell=z^{k+\ell}.$$
> The dual action is the inverse transpose, which in one complex dimension is $z^{-k}$.
>
> A continuous homomorphism lifted along $\mathbb R\to U(1)$ must have the form $\theta\mapsto e^{ia\theta}$. It descends through the identification $\theta\sim\theta+2\pi$ exactly when $e^{2\pi ia}=1$, hence exactly when $a\in\mathbb Z$.

# Key Takeaways

The integer weight is simultaneously a representation-theoretic charge and, after association to a principal $U(1)$-bundle, the multiplier of its first Chern class.
