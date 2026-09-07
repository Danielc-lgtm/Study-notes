---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - The Yang-Mills Action Functional"
  - "Def - Gauge-Covariant Derivative"
  - "Thm - Bianchi Identity for Principal Connections"
tags: [gauge-theory, yang-mills, variational-calculus]
---

# Prerequisite Concepts

- [[Def - The Yang-Mills Action Functional]]
- [[Def - Gauge-Covariant Derivative]]
- [[Thm - Bianchi Identity for Principal Connections]]

# Statement

> [!theorem] Yang–Mills Euler–Lagrange equation
> Let $(M,g)$ be an oriented Riemannian manifold, $P\to M$ a principal compact $G$-bundle, and use an $\operatorname{Ad}$-invariant inner product on $\mathfrak g$. A connection $A$ is critical for
> $$S_{\mathrm{YM}}(A)=\frac12\int_M\langle F_A\wedge *F_A\rangle$$
> under all compactly supported variations if and only if
> $$d_A^*F_A=0,$$
> equivalently $d_A*F_A=0$ up to the conventional nonzero sign relating $d_A^*$ and $*d_A*$.

# Motivation

Curvature is the nonlinear derivative of a connection. The proof follows the ordinary Dirichlet-energy pattern: differentiate curvature, move one derivative off the variation, and use arbitrariness of the variation.

# Formal Proof

> [!proof]- Formal Proof
> The space of connections is affine over $\Omega^1(M;\operatorname{Ad}P)$, so every variation is $A_t=A+ta$ with compactly supported $a$. Expanding curvature gives
> $$F_{A_t}=F_A+t\,d_Aa+\frac{t^2}{2}[a,a],$$
> hence $\dot F_0=d_Aa$. Differentiating the quadratic action and using symmetry of the $L^2$ pairing yields
> $$\left.\frac d{dt}\right|_0S_{\mathrm{YM}}(A_t)
> =\int_M\langle d_Aa\wedge *F_A\rangle
> =(a,d_A^*F_A)_{L^2}.$$
> There is no boundary contribution because $a$ is compactly supported. If $d_A^*F_A=0$, the first variation vanishes. Conversely, if it vanishes for every compactly supported $a$, take $a=\chi d_A^*F_A$ for a nonnegative cutoff $\chi$ supported in a coordinate ball. Then
> $$0=\int_M\chi|d_A^*F_A|^2\operatorname{vol}_g.$$
> Varying the ball and cutoff proves $d_A^*F_A=0$ pointwise.

# What Makes the Proof Work

The key identity is $\delta F_A=d_A(\delta A)$. It is the exact nonlinear analogue of $\delta(dA)=d(\delta A)$; the commutator term merely replaces $d$ by $d_A$.

# Consequences

Together with Bianchi, a Yang–Mills connection has curvature that is covariantly closed and co-closed. If $F_A=\pm *F_A$ in Euclidean dimension four, Bianchi immediately supplies the Euler–Lagrange equation.
