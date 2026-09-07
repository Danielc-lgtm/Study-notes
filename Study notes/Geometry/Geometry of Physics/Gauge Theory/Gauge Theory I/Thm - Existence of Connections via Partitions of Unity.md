---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Connection on a Vector Bundle"
  - "Def - Vector Bundle"
  - "Def - Partition of Unity on a Manifold"
tags: [geometry, gauge-theory, existence, partitions-of-unity]
---

# Prerequisite Concepts

- [[Def - Connection on a Vector Bundle]]
- [[Def - Vector Bundle]]
- [[Def - Partition of Unity on a Manifold]]

# Notation

Let $E\to M$ be a smooth vector bundle over a paracompact smooth manifold. Write $\mathcal A(E)$ for its set of connections.

# Statement

> [!theorem] Existence and affine structure
> Every smooth vector bundle over $M$ admits a connection. If $\nabla_0\in\mathcal A(E)$, then
> $$
> \Omega^1(M;\operatorname{End}E)\longrightarrow\mathcal A(E),
> \qquad a\longmapsto\nabla_0+a
> $$
> is a bijection. Thus $\mathcal A(E)$ is an affine space modelled on $\Omega^1(M;\operatorname{End}E)$, not a vector space with a preferred origin.

# Motivation

A bundle is locally trivial, so componentwise differentiation gives local connections. A partition of unity averages these affine objects. The identity $\sum\rho_\alpha=1$ is precisely what preserves the coefficient of $df$ in the Leibniz rule.

# Rederivation Scaffold

1. Choose a locally finite trivializing cover and subordinate partition of unity.
2. Extend $\rho_\alpha\nabla^\alpha s$ by zero; this is smooth because $\operatorname{supp}\rho_\alpha\subset U_\alpha$.
3. Sum locally finitely and use $\sum\rho_\alpha=1$.
4. Subtract two connections and observe that their $df$ terms cancel.

# Formal Proof

> [!proof]- Formal Proof
> Choose a locally finite trivializing cover $(U_\alpha)$ and a smooth partition of unity $(\rho_\alpha)$ subordinate to it. In a trivialization of $E|_{U_\alpha}$, componentwise differentiation defines a connection $\nabla^\alpha$. For $s\in\Gamma(E)$, the $E$-valued $1$-form $\rho_\alpha\nabla^\alpha(s|_{U_\alpha})$ has support contained in $\operatorname{supp}\rho_\alpha\subset U_\alpha$ and therefore extends smoothly by zero to $M$. Define
> $$
> \nabla s=\sum_\alpha\rho_\alpha\nabla^\alpha(s|_{U_\alpha}).
> $$
> The sum is locally finite, hence smooth and $\mathbb K$-linear. For $f\in C^\infty(M,\mathbb K)$,
> $$
> \begin{aligned}
> \nabla(fs)
> &=\sum_\alpha\rho_\alpha\bigl(df\otimes s+f\nabla^\alpha s\bigr)\\
> &=\Bigl(\sum_\alpha\rho_\alpha\Bigr)df\otimes s+f\nabla s
> =df\otimes s+f\nabla s.
> \end{aligned}
> $$
> Hence $\nabla$ is a connection.
>
> If $\nabla'$ is another connection, set $a=\nabla'-\nabla$. Then
> $$a(fs)=df\otimes s+f\nabla's-df\otimes s-f\nabla s=f,a(s).$$
> Thus $a:\Gamma(E)\to\Omega^1(M;E)$ is $C^\infty(M)$-linear and corresponds to a unique section of $T^*M\otimes\operatorname{End}E$. Conversely, for such an $a$,
> $$(\nabla+a)(fs)=df\otimes s+f(\nabla+a)s,$$
> so $\nabla+a$ is a connection. Uniqueness of $a=\nabla'-\nabla$ proves bijectivity.

# Bridges

For a principal $G$-bundle the analogous modelling space is $\Omega^1(M;\operatorname{Ad}P)$; unlike the vector-bundle proof, existence is usually obtained by the same local-gluing argument applied to horizontal distributions.
