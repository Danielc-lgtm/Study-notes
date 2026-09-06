---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - The Dirac Monopole Bundle"
  - "Thm - Dirac Quantization Condition"
tags: [geometry, gauge-theory, monopole, Chern, line-bundle]
---

# Problem Statement

Let the physical monopole field on $S^2$ be
$$F=g\sin\theta,d\theta\wedge d\varphi.$$
Use
$$A_N=g(1-\cos\theta)d\varphi,qquad
A_S=-g(1+\cos\theta)d\varphi$$
on the northern and southern patches. Prove that they define a connection for a charge-$q$ field exactly when $2qg\in\mathbb Z$ (units $\hbar=1$), and compute the first Chern number.

# Convergent Strategy

Differentiate each potential, compare them on the overlap, exponentiate the gauge parameter, then test single-valuedness around the equator. Keep the mathematical curvature $iqF$ separate from the real physical field $F$.

# Solution

> [!proof]- Solution
> Direct differentiation gives
> $$dA_N=dA_S=g\sin\theta,d\theta\wedge d\varphi=F.$$
> The factors $1-\cos\theta$ and $1+\cos\theta$ vanish quadratically at the north and south pole respectively, so the local forms are smooth on their stated patches.
>
> On the overlap,
> $$A_S-A_N=-2g,d\varphi.$$
> For the convention $\nabla=d+iqA$, a passive frame change $e_S=e_Nh$ requires $h^{-1}dh=iq(A_S-A_N)$. Thus one may take
> $$h(\varphi)=e^{-2iqg\varphi}.$$
> This is single-valued under $\varphi\mapsto\varphi+2\pi$ exactly when $e^{-4\pi iqg}=1$, equivalently $2qg\in\mathbb Z$.
>
> The unitary curvature is $\mathcal F=iqF$. With the convention
> $c_1(L)=[i\mathcal F/(2\pi)]$,
> $$
> c_1(L)[S^2]=-\frac{q}{2\pi}\int_{S^2}F
> =-\frac{q}{2\pi}(4\pi g)=-2qg.
> $$
> The sign agrees with the degree of the transition map for the overlap
> convention used here. By [[Thm - First Chern Class Classifies Line Bundles over a CW Complex]], line bundles over $S^2$ are classified by this
> integer, the bundle is the corresponding tensor power of a Hopf line bundle,
> with the dual chosen if the opposite Hopf generator is used.

# Key Takeaways

A nonzero flux forbids one global potential by Stokes' theorem. Two nonsingular local potentials solve the problem, and the winding of their transition function is the quantized magnetic charge.
