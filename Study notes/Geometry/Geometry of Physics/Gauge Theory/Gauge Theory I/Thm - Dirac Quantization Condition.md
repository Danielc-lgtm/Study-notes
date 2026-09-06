---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - The Dirac Monopole Bundle"
  - "Def - U(1) Gauge Field and Electromagnetic Connection"
tags: [gauge-theory, monopole, quantization, chern-class]
---

# Notation

Let $L\to S^2$ be a Hermitian line bundle with unitary connection $\nabla=d+iqA_\alpha$ in local frames over northern and southern patches. Write $F=dA_\alpha$, which is globally defined. The charge convention is fixed by the representation $e^{i\theta}\mapsto e^{iq\theta}$; hence the mathematical curvature is $F_\nabla=iqF$.

# Statement

> [!theorem] Dirac quantization
> The flux of $F$ obeys
> $$
> \frac{q}{2\pi}\int_{S^2}F\in\mathbb Z.
> $$
> With the convention $c_1(L)=[iF_\nabla/(2\pi)]$, the real image of
> $c_1(L)$ is $[-qF/(2\pi)]$. If a monopole convention defines magnetic
> charge $g$ by $\int_{S^2}F=4\pi g$, then
> $$2qg\in\mathbb Z.$$
> Restoring $\hbar$ gives $2qg/\hbar\in\mathbb Z$; additional factors of $c$ depend on the electromagnetic unit convention.

# Why Is It True

The two local potentials differ on the equatorial overlap by the logarithmic derivative of the transition function. The flux becomes the winding number of that map $S^1\to U(1)$.

# Rederivation Scaffold

Cover $S^2$ by two discs, use Stokes on each, reduce the result to the equator, and identify the integral of $g^{-1}dg$ with $2\pi i$ times an integer.

# Formal Proof

> [!proof]- Formal Proof
> Choose oriented closed hemispheres $D_N,D_S$ with common equator $C=\partial D_N=-\partial D_S$. Let unitary frames satisfy $e_S=e_Nh$ on an annular overlap, where $h:C\to U(1)$. Write $h=e^{iq\chi}$ locally along subarcs. The passive frame-change law gives
> $$iqA_S=h^{-1}(iqA_N)h+h^{-1}dh=iqA_N+h^{-1}dh,$$
> hence $iq(A_S-A_N)=h^{-1}dh$. By Stokes and the boundary orientations,
> $$
> \begin{aligned}
> iq\int_{S^2}F
> &=iq\left(\int_{D_N}dA_N+\int_{D_S}dA_S\right)\\
> &=iq\int_C(A_N-A_S)=-\int_C h^{-1}dh.
> \end{aligned}
> $$
> For a smooth map $h:S^1\to U(1)$, $(2\pi i)^{-1}\int_C h^{-1}dh=\deg(h)\in\mathbb Z$. The preceding sign depends on which overlap transition is called $h$; therefore
> $$\frac{q}{2\pi}\int_{S^2}F=-\deg(h)\in\mathbb Z.$$
> Since $F_\nabla=iqF$, it follows at the same time that
> $c_1(L)[S^2]=\deg(h)$ in the convention fixed above.
> This proves integrality. Substituting $\int F=4\pi g$ gives $2qg\in\mathbb Z$.

# What Makes This Hard

The invariant statement is the normalized flux formula. Expressions such as “$qg$ is an integer” are meaningless until the definitions of $g$, the $U(1)$ representation, $\hbar$, and the flux normalization have been fixed.

# Unlocked by This

Magnetic charge is the first Chern number expressed in physical units. Gauge Theory IV derives the same integrality through Chern–Weil theory.
