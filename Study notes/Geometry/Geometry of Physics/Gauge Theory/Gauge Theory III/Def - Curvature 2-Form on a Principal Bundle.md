---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Connection 1-Form on a Principal Bundle"
  - "Def - Bracket of g-Valued Forms"
tags: [gauge-theory, curvature, principal-bundle]
---

# The Definition

> [!definition] Principal curvature
> The curvature of a principal connection $\omega$ is
> $$
> \Omega=d\omega+\tfrac12[\omega,\omega]\in\Omega^2(P;\mathfrak g).
> $$

It is horizontal and equivariant:
$$\iota_{\xi_P}\Omega=0,qquad R_g^*\Omega=\operatorname{Ad}_{g^{-1}}\Omega.$$
Therefore it descends to a form in $\Omega^2(M;\operatorname{Ad}P)$.

# Local Form

For $A=s^*\omega$,
$$F_A=s^*\Omega=dA+\tfrac12[A,A].$$
For matrix groups, $\tfrac12[A,A]=A\wedge A$. Under $s'=sg$,
$$F_{A'}=\operatorname{Ad}_{g^{-1}}F_A.$$

# Geometric Meaning

If $X^H,Y^H$ are horizontal lifts, then
$$\Omega(X^H,Y^H)=-\omega([X^H,Y^H]).$$
Indeed the two terms differentiating the zero functions $\omega(X^H)$ and $\omega(Y^H)$ vanish in the exterior-derivative formula, and $[\omega,omega](X^H,Y^H)=0$. Thus curvature is the vertical component of the bracket of horizontal directions.
