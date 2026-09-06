---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Local Connection 1-Form (Gauge Potential)"
  - "Def - The Maurer-Cartan Form"
tags: [gauge-theory, gauge-transformation, local-connection]
---

# Statement

> [!theorem] Passive gauge law
> If local sections satisfy $s'=sg$ for $g:U\to G$, then
> $$
> A'=(s')^*\omega=\operatorname{Ad}_{g^{-1}}A+g^{-1}dg.
> $$
> Consequently $F_{A'}=\operatorname{Ad}_{g^{-1}}F_A$.

# Formal Proof

> [!proof]- Formal Proof
> Let $X\in T_xU$ and choose a curve $x(t)$ with $x(0)=x$, $\dot x(0)=X$. Differentiating $s'(x(t))=s(x(t))g(x(t))$ separates the velocity into
> $$
> ds'_xX=dR_{g(x)}(ds_xX)+\bigl(g^{-1}dg(X)\bigr)_P(s'(x)).
> $$
> The first term follows by holding $g$ fixed. For the second, write
> $g(x(t))=g(x)\exp(t\xi+o(t))$; then $\xi=g(x)^{-1}dg_xX$ and the derivative is $\xi_P$ at $s'(x)$.
>
> Apply $\omega$. Equivariance gives
> $$\omega(dR_gdsX)=\operatorname{Ad}_{g^{-1}}\omega(dsX)=\operatorname{Ad}_{g^{-1}}A(X),$$
> while reproduction gives $\omega(\xi_P)=\xi$. This proves the formula.
>
> Using $d(g^{-1})=-g^{-1}(dg)g^{-1}$, the graded Leibniz rule, and the Maurer–Cartan equation, direct expansion of $dA'+A'\wedge A'$ cancels all inhomogeneous terms and yields $g^{-1}F_Ag$ for matrix groups. The adjoint formula follows in general by applying the same calculation to the graded bracket.

# Infinitesimal Form

For $g_\varepsilon=\exp(\varepsilon\lambda)$,
$$A'=A+\varepsilon(d\lambda+[A,\lambda])+O(\varepsilon^2)=A+\varepsilon d_A\lambda+O(\varepsilon^2).$$
Using $s'=s\exp(-\varepsilon\lambda)$ reverses the sign. The sign is determined by the chosen finite transformation, not an independent convention.

# Rederivation Scaffold

Differentiate $s'=sg$: one term moves $s$ and transforms by $\operatorname{Ad}_{g^{-1}}$; the other moves vertically and is read by the Maurer–Cartan form.
