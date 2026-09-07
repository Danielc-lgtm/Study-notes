---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Vector Bundle"
  - "Def - Section of a Vector Bundle"
  - "Def - Local Frame"
  - "Def - Differential k-Form on a Manifold"
tags: [geometry, gauge-theory, connection, covariant-derivative]
---

# Prerequisite Concepts

- [[Def - Vector Bundle]]
- [[Def - Section of a Vector Bundle]]
- [[Def - Local Frame]]
- [[Def - Differential k-Form on a Manifold]]

# Notation

Let $\mathbb K\in\{\mathbb R,\mathbb C\}$, let $E\to M$ be a smooth rank-$r$ $\mathbb K$-vector bundle, and write $\Omega^k(M;E)=\Gamma(\Lambda^kT^*M\otimes E)$. Thus $\Omega^0(M;E)=\Gamma(E)$.

# Axiom Motivation

Values $s(x)\in E_x$ and $s(y)\in E_y$ lie in different vector spaces, so their difference has no intrinsic meaning. A connection supplies a first-order comparison rule. It must be tensorial in the direction being tested, but it must differentiate scalar coefficients of the section. These requirements force the two axioms below.

# The Definition

> [!definition] Connection
> A **connection** (or **covariant derivative**) on $E$ is a $\mathbb K$-linear map
> $$
> \nabla:\Gamma(E)\longrightarrow\Omega^1(M;E)
> $$
> such that, for $f\in C^\infty(M,\mathbb K)$ and $s\in\Gamma(E)$,
> $$
> \nabla(fs)=df\otimes s+f\nabla s.
> $$
> For $X\in\mathfrak X(M)$, set $\nabla_Xs=(\nabla s)(X)$. Equivalently,
> $$
> \nabla_{fX+gY}s=f\nabla_Xs+g\nabla_Ys,\qquad
> \nabla_X(fs)=X(f)s+f\nabla_Xs.
> $$

Let $e=(e_1,\ldots,e_r)$ be a local frame on $U$ and write sections as column vectors, $s=e\,u$. There is a unique matrix $A=(A^a{}_b)\in\Omega^1(U;\mathfrak{gl}_r(\mathbb K))$ satisfying
$$
\nabla e_b=e_aA^a{}_b.
$$
Then
$$
\nabla(eu)=e(du+Au).
$$
If $e'=eg$ for $g:U\to\mathrm{GL}_r(\mathbb K)$, the same global connection has local matrix
$$
A'=g^{-1}Ag+g^{-1}dg.
$$
Indeed $\nabla(e' u')=\nabla(eg u')=e(d(gu')+Agu')=e'g^{-1}(d+A)g,u'$. The inhomogeneous term is not a defect: it is what compensates for differentiating the moving frame.

# Legal Operations

A connection extends uniquely to $E$-valued forms by
$$
d_\nabla(\alpha\otimes s)=d\alpha\otimes s+(-1)^k\alpha\wedge\nabla s,\qquad \alpha\in\Omega^k(M).
$$
In a frame, $d_\nabla\eta=d\eta+A\wedge\eta$. It also induces connections on $E^*$, direct sums, tensor products, and endomorphism bundles by requiring evaluation and tensor product to satisfy Leibniz rules. In particular,
$$
(\nabla_XT)(s)=\nabla_X(Ts)-T(\nabla_Xs),\qquad T\in\Gamma(\operatorname{End}E).
$$

The set $\mathcal A(E)$ of connections is affine over $\Omega^1(M;\operatorname{End}E)$: if $\nabla'$ and $\nabla$ are connections, $a=\nabla'-\nabla$ is $C^\infty(M)$-linear in $s$, hence is an endomorphism-valued $1$-form; conversely $\nabla+a$ is a connection.

# Examples / Corollaries

On a trivial bundle $M\times\mathbb K^r$, componentwise differentiation is the connection $d$. Every other connection is $d+A$. A connection on $TM$ is an affine connection. A Hermitian connection on a complex bundle additionally satisfies
$$
d\langle s,t\rangle=\langle\nabla s,t\rangle+\langle s,\nabla t\rangle;
$$
in a unitary frame its matrix is skew-Hermitian.

# Unlocked by This

The square $d_\nabla^2$ is no longer zero in general; it is multiplication by the [[Def - Curvature of a Vector-Bundle Connection|curvature]]. Parallel transport and holonomy are the integrated form of the same comparison rule.
