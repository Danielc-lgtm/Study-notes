---
type: theorem
subject: gauge-theory
prereqs: ["Def - Smooth Fredholm Map and Regular Value"]
tags: [gauge-theory, kuranishi-model, fredholm-map]
---

# Statement

> [!theorem] Kuranishi model
> Near a zero $x$ of a smooth Fredholm section $s$ with linearization $D$, its zero set is homeomorphic, and smoothly equivalent in suitable charts, to the zero set of a finite-dimensional smooth map
> $$\kappa:\ker D\supset U\to\operatorname{coker}D,$$
> with $\kappa(0)=0$ and $d\kappa_0=0$.

# Formal Proof

> [!proof]- Formal Proof
> Choose closed splittings $T_xX=K\oplus X'$ with $K=\ker D$ and $E_x=\operatorname{im}D\oplus C$, where $C\cong\operatorname{coker}D$. Let $\pi_I,\pi_C$ be the projections. The derivative of $\pi_I s$ in the $X'$ direction is $D|_{X'}:X'\to\operatorname{im}D$, an isomorphism. The implicit-function theorem therefore gives a unique smooth $h:U\subset K\to X'$ such that $\pi_I s(k+h(k))=0$. Define $\kappa(k)=\pi_Cs(k+h(k))$. Then $s(k+x')=0$ nearby iff $x'=h(k)$ and $\kappa(k)=0$. Differentiating at zero gives $dh_0=0$ and $d\kappa_0=\pi_C D|_K=0$.

# Significance

The kernel supplies infinitesimal deformations and the cokernel supplies obstructions. Surjectivity means the obstruction space vanishes and the moduli space is smooth of dimension $\operatorname{ind}D$.

