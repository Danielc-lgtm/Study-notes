---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Complex Line Bundle"
  - "Def - U(1) Gauge Field and Electromagnetic Connection"
tags: [gauge-theory, monopole, line-bundle, chern-class]
---

# Prerequisite Concepts

- [[Def - Complex Line Bundle]]
- [[Def - U(1) Gauge Field and Electromagnetic Connection]]

# Notation

Use spherical coordinates $(\theta,\varphi)$ on the unit sphere and fix $n\in\mathbb Z$. Let $U_N=S^2\setminus\{\text{south pole}\}$ and $U_S=S^2\setminus\{\text{north pole}\}$.

# The Definition

> [!definition] Dirac monopole line bundle
> The charge-$n$ **Dirac monopole bundle** $L_n\to S^2$ is obtained by gluing $U_N\times\mathbb C$ to $U_S\times\mathbb C$ with equatorial transition function
> $$h_{NS}(e^{i\varphi})=e^{in\varphi}.$$
> It carries local unitary connection forms
> $$
> \mathcal A_N=-\frac{in}{2}(1-\cos\theta)d\varphi,
> \qquad
> \mathcal A_S=\frac{in}{2}(1+\cos\theta)d\varphi.
> $$
> Their common curvature is
> $$
> \mathcal F=d\mathcal A_N=d\mathcal A_S=-\frac{in}{2}\sin\theta,d\theta\wedge d\varphi.
> $$

Each displayed potential is smooth on its own patch: the coefficient vanishes quadratically at the pole where $d\varphi$ is singular. On the overlap,
$$
\mathcal A_S-\mathcal A_N=in,d\varphi=h_{NS}^{-1}dh_{NS},
$$
up to reversing which frame is declared the transition source. This is exactly the connection gluing law.

# Topological Charge

With the displayed orientation,
$$
\frac{i}{2\pi}\int_{S^2}\mathcal F=n.
$$
Thus $c_1(L_n)[S^2]=n$ in this sign convention. Reversing the orientation or using $(2\pi i)^{-1}\mathcal F$ reverses the displayed sign; the transition-function degree fixes the convention-independent content.

# Axiom Motivation

A two-form with nonzero integral over $S^2$ cannot be $dA$ for one globally defined $1$-form, because Stokes would give $\int_{S^2}dA=0$. Local potentials are therefore forced. Their overlap mismatch is not an artificial “Dirac string”; it is the transition data of a nontrivial line bundle.

# Examples / Corollaries

$L_0$ is trivial. Tensor product adds charges: $L_m\otimes L_n\cong L_{m+n}$ because transition functions multiply. Dualization reverses charge: $L_n^*\cong L_{-n}$.

# Unlocked by This

[[Thm - Dirac Quantization Condition]] says that coupling to a charged field is globally consistent exactly when the normalized physical flux equals the integer Chern number.
