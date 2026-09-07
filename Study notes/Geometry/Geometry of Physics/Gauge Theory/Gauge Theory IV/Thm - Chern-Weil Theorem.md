---
type: theorem
subject: gauge-theory
prereqs: ["Def - Ad-Invariant Polynomial", "Thm - Bianchi Identity for Principal Connections"]
tags: [gauge-theory, chern-weil, characteristic-class]
---

# Prerequisite Concepts

- [[Def - Ad-Invariant Polynomial]]
- [[Thm - Bianchi Identity for Principal Connections]]

# Statement

> [!theorem] Chern–Weil
> Let $P\to M$ be a principal $G$-bundle, $A$ a connection with curvature $F_A$, and $f$ an invariant polynomial of degree $k$. Then $f(F_A^k)\in\Omega^{2k}(M)$ is closed. Its de Rham class is independent of $A$ and is natural under pullback.

# Motivation

The theorem converts differential data, which varies in an affine space, into topological data. Gauge covariance makes the form global; Bianchi makes it closed; a one-parameter family of connections makes every variation exact.

# Formal Proof

> [!proof]- Formal Proof
> In a gauge define $f(F_A^k)=f(F_A,\ldots,F_A)$, multiplying the form components by wedge product. On overlaps all inputs are conjugated, so invariance of $f$ makes the local forms agree.
>
> The infinitesimal invariance identity implies that replacing the ordinary derivative by $d_A=d+[A,\cdot]$ does not change the derivative after applying $f$:
> $$d f(\alpha_1,\ldots,\alpha_k)=\sum_j(-1)^{|\alpha_1|+\cdots+|\alpha_{j-1}|}f(\alpha_1,\ldots,d_A\alpha_j,\ldots,\alpha_k).$$
> With every $\alpha_j=F_A$ the signs are positive because $|F_A|=2$. Bianchi gives $d_AF_A=0$, hence $d f(F_A^k)=0$.
>
> Let $A_t=A_0+t a$ and $F_t$ its curvature. Direct differentiation of
> $F_t=dA_t+\tfrac12[A_t,A_t]$ gives $\dot F_t=d_{A_t}a$. Therefore
> $$\frac d{dt}f(F_t^k)=k f(d_{A_t}a,F_t^{k-1})=k\,d f(a,F_t^{k-1}),$$
> where Bianchi and invariant-polynomial cancellation justify the second equality. Integrating from $0$ to $1$ yields
> $$f(F_1^k)-f(F_0^k)=d\left(k\int_0^1f(a,F_t^{k-1})dt\right).$$
> Thus the class is connection-independent. Pulling back the bundle, connection, and curvature commutes with every operation in the construction, proving naturality.

# Key Mechanism

The covariant derivative differs from $d$ by commutators, and invariant polynomials annihilate the total commutator contribution.

# Consequences

The integral in the proof is the [[Def - Chern-Simons Transgression Form|transgression form]]. Determinant polynomials give Chern classes, while the Pfaffian gives the Euler class.
