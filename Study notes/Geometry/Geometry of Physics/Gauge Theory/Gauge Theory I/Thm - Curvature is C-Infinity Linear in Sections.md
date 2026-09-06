---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Curvature of a Vector-Bundle Connection"
  - "Def - Connection on a Vector Bundle"
tags: [geometry, gauge-theory, curvature, tensoriality]
---

# Notation

Let $\nabla$ be a connection on $E\to M$ and let $F_\nabla(X,Y)=[\nabla_X,\nabla_Y]-\nabla_{[X,Y]}$.

# Statement

> [!theorem] Tensoriality of curvature
> The map $(X,Y,s)\mapsto F_\nabla(X,Y)s$ is $C^\infty(M)$-linear in each variable and alternating in $X,Y$. Consequently
> $$F_\nabla\in\Omega^2(M;\operatorname{End}E).$$

# Why Is It True

The derivatives of scalar coefficients created by the Leibniz rule cancel. The bracket correction is exactly the term needed for cancellation in the vector-field slots.

# Rederivation Scaffold

1. Use $\nabla_{fX}=f\nabla_X$ and $[fX,Y]=f[X,Y]-Y(f)X$.
2. Use $\nabla_X(fs)=X(f)s+f\nabla_Xs$ twice in the section slot.
3. Obtain the second vector-field slot from alternation.

# Formal Proof

> [!proof]- Formal Proof
> Let $f\in C^\infty(M)$. In the first slot,
> $$
> \begin{aligned}
> F_\nabla(fX,Y)s
> &=f\nabla_X\nabla_Ys-\nabla_Y(f\nabla_Xs)-\nabla_{f[X,Y]-Y(f)X}s\\
> &=f\nabla_X\nabla_Ys-Y(f)\nabla_Xs-f\nabla_Y\nabla_Xs
>   -f\nabla_{[X,Y]}s+Y(f)\nabla_Xs\\
> &=fF_\nabla(X,Y)s.
> \end{aligned}
> $$
> Directly from the definition, $F_\nabla(Y,X)=-F_\nabla(X,Y)$; therefore
> $F_\nabla(X,fY)=-F_\nabla(fY,X)=-fF_\nabla(Y,X)=fF_\nabla(X,Y)$.
>
> For the section slot,
> $$
> \begin{aligned}
> \nabla_X\nabla_Y(fs)
> &=X(Yf)s+(Yf)\nabla_Xs+(Xf)\nabla_Ys+f\nabla_X\nabla_Ys,\\
> \nabla_Y\nabla_X(fs)
> &=Y(Xf)s+(Xf)\nabla_Ys+(Yf)\nabla_Xs+f\nabla_Y\nabla_Xs,\\
> \nabla_{[X,Y]}(fs)&=[X,Y](f)s+f\nabla_{[X,Y]}s.
> \end{aligned}
> $$
> Since $X(Yf)-Y(Xf)=[X,Y](f)$, all derivative terms cancel and
> $F_\nabla(X,Y)(fs)=fF_\nabla(X,Y)s$. Hence the value at $p$ depends only on $X_p,Y_p,s_p$ and gives an alternating bilinear map $T_pM^2\to\operatorname{End}(E_p)$ varying smoothly with $p$. This is precisely an element of $\Omega^2(M;\operatorname{End}E)$.

# Unlocked by This

Because curvature is tensorial, its local matrix transforms by conjugation and invariant polynomials in curvature define global differential forms.
