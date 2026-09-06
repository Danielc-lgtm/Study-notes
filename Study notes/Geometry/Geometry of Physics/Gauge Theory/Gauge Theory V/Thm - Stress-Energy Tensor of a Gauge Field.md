---
type: theorem
subject: gauge-theory
prereqs: ["Def - The Yang-Mills Action Functional", "Def - Hodge Star in Arbitrary Signature"]
tags: [gauge-theory, stress-energy, yang-mills]
---

# Statement

> [!theorem] Gauge-field stress-energy
> For an invariant inner product $\langle\ ,\ \rangle$ on $\mathfrak g$ and Yang–Mills Lagrangian $-\frac14\langle F_{\alpha\beta},F^{\alpha\beta}\rangle$, metric variation gives
> $$T_{\mu\nu}=\left\langle F_{\mu\alpha},F_\nu{}^\alpha\right\rangle-rac14g_{\mu\nu}\left\langle F_{\alpha\beta},F^{\alpha\beta}\right\rangle.$$
> If $d_AF=0$ and $d_A*F=*J$, then
> $$\nabla^\mu T_{\mu\nu}=\langle J^\alpha,F_{\nu\alpha}\rangle.$$
> In vacuum it is divergence-free; for $U(1)$ the right side is the Lorentz-force density.

# Proof

> [!proof]- Formal Proof
> Vary $g^{\mu\nu}$ while holding the connection fixed. The identity
> $\delta\sqrt{|g|}=-\frac12\sqrt{|g|}g_{\mu\nu}\delta g^{\mu\nu}$ gives the trace term. Each of the two inverse metrics used to raise the indices of $F_{\alpha\beta}$ contributes the same contraction; antisymmetry combines them into $\langle F_{\mu\alpha},F_\nu{}^\alpha\rangle$. Using
> $T_{\mu\nu}=-2|g|^{-1/2}\delta S/\delta g^{\mu\nu}$ yields the formula.
>
> Take a covariant divergence. Invariance of the Lie-algebra inner product lets ordinary derivatives be replaced by gauge-covariant ones inside a contraction. The term with $D^\mu F_{\mu\alpha}$ is $\langle J_\alpha,F_\nu{}^\alpha\rangle$ by Yang–Mills. For the remaining terms, contract Bianchi
> $D_\mu F_{\nu\alpha}+D_\nu F_{\alpha\mu}+D_\alpha F_{\mu\nu}=0$
> with $F^{\mu\alpha}$; antisymmetry shows that their sum is
> $\frac14\nabla_\nu\langle F_{\alpha\beta},F^{\alpha\beta}\rangle$, canceling the derivative of the trace term. This proves the divergence identity.

# Significance

The equation states local exchange of energy-momentum between matter current and gauge field. It is not an additional gauge equation: it follows from the field equations and diffeomorphism covariance.
