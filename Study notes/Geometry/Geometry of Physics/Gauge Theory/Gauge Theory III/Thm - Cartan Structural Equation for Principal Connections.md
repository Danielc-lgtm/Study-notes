---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Curvature 2-Form on a Principal Bundle"
tags: [gauge-theory, curvature, structure-equation]
---

# Statement

> [!theorem] Cartan structure equation
> For a principal connection $\omega$, the form
> $$\Omega=d\omega+\tfrac12[\omega,\omega]$$
> is horizontal and $\operatorname{Ad}$-equivariant. Its local representatives satisfy
> $$F_A=dA+\tfrac12[A,A],qquad F_{A^g}=\operatorname{Ad}_{g^{-1}}F_A.$$

# Formal Proof

> [!proof]- Formal Proof
> Equivariance follows because pullback commutes with $d$ and bracket:
> $$R_g^*\Omega=d(\operatorname{Ad}_{g^{-1}}\omega)+\tfrac12[\operatorname{Ad}_{g^{-1}}\omega,\operatorname{Ad}_{g^{-1}}\omega]=\operatorname{Ad}_{g^{-1}}\Omega.$$
> Here $g$ is constant for the right translation $R_g$.
>
> To prove horizontality, Cartan's formula and connection equivariance differentiated along the fundamental flow give
> $$\iota_{\xi_P}d\omega=\mathcal L_{\xi_P}\omega-d(\omega(\xi_P))=-[\xi,\omega].$$
> Since $\omega(\xi_P)=\xi$, direct evaluation gives
> $$\tfrac12\iota_{\xi_P}[\omega,\omega]=[\xi,\omega].$$
> The terms cancel. Pullback by $s$ gives the local structural equation. The local covariance follows either by pulling back global equivariance or by the direct calculation in [[Thm - Gauge Transformation Law for Local Connection 1-Forms]].

# Rederivation Scaffold

The correction $\frac12[\omega,\omega]$ has exactly the contraction needed to cancel the infinitesimal adjoint rotation of $d\omega$ along vertical directions.
