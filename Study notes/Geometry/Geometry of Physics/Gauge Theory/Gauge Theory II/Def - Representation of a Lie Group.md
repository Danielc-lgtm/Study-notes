---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Lie Group"
  - "Def - Lie Group Homomorphism"
tags: [gauge-theory, lie-groups, representations]
---

# Notation

Let $G$ be a Lie group, $V$ a finite-dimensional real or complex vector space, and $\mathfrak g=T_eG$.

# The Definition

> [!definition] Lie-group representation
> A **representation** of $G$ on $V$ is a smooth homomorphism
> $$\rho:G\to\mathrm{GL}(V).$$
> It is **faithful** if $\rho$ is injective. Two representations $\rho$ on $V$ and $\rho'$ on $V'$ are **equivalent** if an isomorphism $T:V\to V'$ satisfies $T\rho(g)=\rho'(g)T$ for every $g$.

Differentiation at the identity gives the Lie-algebra representation
$$
\rho_*:\mathfrak g\to\mathfrak{gl}(V),qquad
\rho_*([X,Y])=[\rho_*X,\rho_*Y].
$$
The bracket identity follows from [[Thm - Lie Group Homomorphism Induces Lie Algebra Homomorphism]].

# Legal Operations

From $\rho_i:G\to\mathrm{GL}(V_i)$ one obtains
$$
\begin{aligned}
(\rho_1\oplus\rho_2)(g)(v_1,v_2)&=(\rho_1(g)v_1,\rho_2(g)v_2),\\
(\rho_1\otimes\rho_2)(g)(v_1\otimes v_2)&=\rho_1(g)v_1\otimes\rho_2(g)v_2,\\
\rho^*(g)\lambda&=\lambda\circ\rho(g)^{-1}.
\end{aligned}
$$
The inverse in the dual action is forced by the homomorphism law. Tensor powers preserve the symmetric and alternating subspaces, giving $\operatorname{Sym}^kV$ and $\Lambda^kV$. A real representation complexifies on $V\otimes_\mathbb R\mathbb C$.

# Examples / Corollaries

The adjoint representation is $\operatorname{Ad}:G\to\mathrm{GL}(\mathfrak g)$. It is trivial for abelian $G$. Matrix groups have their defining representations. Every complex representation of compact $G$ admits an invariant Hermitian inner product: average any inner product over normalized Haar measure; invariance follows from right invariance of that measure.

For $U(1)$, irreducible complex representations are the integer weights $z\mapsto z^k$. For $SU(2)$, the irreducibles are $\operatorname{Sym}^k(\mathbb C^2)$; this classification is stated here for source coverage and used concretely only through low-dimensional examples.

# Relate to Other Fields / Compression

A representation specifies a **type of fibre** on which a gauge frame acts. Applied to a principal bundle it produces [[Def - Associated Bundle|an associated bundle]]. Equivalent representations produce isomorphic associated bundles, but the isomorphism is canonical only after an intertwiner is chosen.
